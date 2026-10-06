#!/usr/bin/env python3
"""Check posts for problems that hurt readers or search engines.

Usage:
    python3 scripts/check_posts.py                 # all posts, leak checks only
    python3 scripts/check_posts.py --strict FILE…  # new posts: also front matter

Translations (<slug>.<lang>.md for sk, nl, fr, de, es, zh) are also checked
against their English twin (<slug>.md): same tags, date and source URLs, and
claim labels in the translation's language only.

Exits 1 if any check fails.
"""
import re
import sys
import tomllib
from pathlib import Path

TAGS = {"models", "tools", "business", "research", "agents",
        "policy", "safety", "hardware", "community", "projects", "essays"}

# Pipeline notes that must never reach a published page.
LEAKS = [
    (re.compile(r"^=== "), "pipeline delimiter"),
    (re.compile(r"EDITOR NOTES|Editor.s note", re.I), "editor notes"),
    (re.compile(r"Cold-reader", re.I), "cold-reader sentence"),
    (re.compile(r"Glossary candidates", re.I), "glossary candidates"),
    (re.compile(r"^After reading this, the reader knows"), "gate sentence"),
]
H1 = re.compile(r"^# ")
DEK = re.compile(r"^\*[^*].*[^*]\*\s*$")

ENGLISH_LABELS = re.compile(r"\b(VERIFIED|PARTIALLY VERIFIED|VENDOR-REPORTED|UNVERIFIED)\b")
ENGLISH_HEADINGS = re.compile(r"^## (Why it matters|Verification|In brief|Releases|Research|Prompting techniques|What people are building|Worth reading|Business, briefly)\b")

# Translated editions: file suffix -> (language, translator-note pattern, labels to use).
TRANSLATIONS = {
    ".sk.md": ("Slovak",
               re.compile(r"pozn[áa]mk[ay]? prekladate[ľl]a|translat(or|ion)'?s? notes?", re.I),
               "OVERENÉ, ČIASTOČNE OVERENÉ, PODĽA SPOLOČNOSTI, NEOVERENÉ"),
    ".nl.md": ("Dutch",
               re.compile(r"noot van de vertaler|vertaal(notitie|opmerking)|translat(or|ion)'?s? notes?", re.I),
               "GEVERIFIEERD, GEDEELTELIJK GEVERIFIEERD, VOLGENS HET BEDRIJF, NIET GEVERIFIEERD"),
    ".fr.md": ("French",
               re.compile(r"note du traducteur|N\.d\.T\.|translat(or|ion)'?s? notes?", re.I),
               "VÉRIFIÉ, PARTIELLEMENT VÉRIFIÉ, SELON LA SOCIÉTÉ, NON VÉRIFIÉ"),
    ".de.md": ("German",
               re.compile(r"Anm\. d\. Übers|Anmerkung de[sr] Übersetzer|Übersetzungshinweis|translat(or|ion)'?s? notes?", re.I),
               "VERIFIZIERT, TEILWEISE VERIFIZIERT, LAUT UNTERNEHMEN, NICHT VERIFIZIERT"),
    ".es.md": ("Spanish",
               re.compile(r"nota del traductor|N\. del T\.|translat(or|ion)'?s? notes?", re.I),
               "VERIFICADO, PARCIALMENTE VERIFICADO, SEGÚN LA EMPRESA, NO VERIFICADO"),
    ".zh.md": ("Simplified Chinese",
               re.compile(r"译者注|译注|translat(or|ion)'?s? notes?", re.I),
               "已核实, 部分核实, 据公司称, 未核实"),
}
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
URL = re.compile(r"https?://[^\s)\]|>\"]+")


def parse(path):
    """Return (meta, body) for a TOML post, or (None, body) otherwise."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("+++"):
        return None, text
    _, fm, body = text.split("+++", 2)
    return tomllib.loads(fm), body


def urls(body):
    return sorted(u.rstrip(".,;:") for u in URL.findall(body))


def translation_suffix(path):
    return next((sfx for sfx in TRANSLATIONS if path.name.endswith(sfx)), None)


def check_translation(path, suffix, meta, body, strict):
    errors = []
    _, notes, labels = TRANSLATIONS[suffix]
    leaks = [
        (notes, "translator notes"),
        (ENGLISH_LABELS, f"English claim label (use {labels})"),
        (ENGLISH_HEADINGS, "untranslated heading"),
    ]
    twin = path.with_name(path.name[: -len(suffix)] + ".md")
    if not twin.exists():
        return [f"English twin {twin.name} not found (the file names must match)"]
    try:
        en_meta, en_body = parse(twin)
    except tomllib.TOMLDecodeError:
        return [f"English twin {twin.name} has invalid front matter"]

    for n, line in enumerate(body.split("\n"), start=1):
        for pattern, what in leaks:
            if pattern.search(line):
                errors.append(f"body line {n}: {what}")

    if urls(body) != urls(en_body):
        missing = sorted(set(urls(en_body)) - set(urls(body)))
        extra = sorted(set(urls(body)) - set(urls(en_body)))
        detail = "; ".join(filter(None, [
            missing and f"missing {missing[:3]}",
            extra and f"not in English {extra[:3]}",
        ])) or "same URLs, different counts"
        errors.append(f"source URLs differ from {twin.name}: {detail}")

    for heading_id, en_heading in (("why-it-matters", "## Why it matters"),
                                   ("verification", "## Verification")):
        if en_heading in en_body and "{#" + heading_id + "}" not in body:
            errors.append(f"heading for '{en_heading[3:]}' needs {{#{heading_id}}}")

    if strict and meta is not None:
        slug = str(meta.get("slug", ""))
        if not SLUG.match(slug) or len(slug) > 60:
            errors.append(f"slug {slug!r} must be lowercase ASCII words joined by hyphens, max 60 chars")
        if len(str(meta.get("title", ""))) > 70:
            errors.append("title longer than 70 characters")
        if en_meta is not None:
            for key in ("tags", "date"):
                if meta.get(key) != en_meta.get(key):
                    errors.append(f"{key} differs from {twin.name}")
    return errors


def check(path, strict):
    errors = []
    text = path.read_text(encoding="utf-8")
    delim = text[:3]
    if delim not in ("+++", "---"):
        return ["no front matter"]
    try:
        _, fm, body = text.split(delim, 2)
    except ValueError:
        return ["unterminated front matter"]

    meta = {}
    if delim == "+++":
        try:
            meta = tomllib.loads(fm)
        except tomllib.TOMLDecodeError as e:
            return [f"front matter is not valid TOML: {e}"]
    elif strict:
        errors.append("front matter must be TOML (+++)")

    in_fence = False
    for n, line in enumerate(body.split("\n"), start=fm.count("\n") + 1):
        if line.startswith("```"):
            in_fence = not in_fence
        if in_fence:
            continue
        for pattern, what in LEAKS:
            if pattern.search(line):
                errors.append(f"line {n}: {what} leaked into the post")
        if H1.match(line):
            errors.append(f"line {n}: H1 in body (the theme already renders the title)")

    if strict:
        if not meta.get("title"):
            errors.append("missing title")
        if not meta.get("date"):
            errors.append("missing date")
        if not str(meta.get("description", "")).strip():
            errors.append("missing description (the dek)")
        tags = meta.get("tags") or []
        if not 2 <= len(tags) <= 4:
            errors.append(f"needs 2-4 tags, has {len(tags)}")
        if bad := [t for t in tags if t not in TAGS]:
            errors.append(f"unknown tags {bad}; allowed: {sorted(TAGS)}")
        first = next((l for l in body.split("\n") if l.strip()), "")
        if DEK.match(first.strip()):
            errors.append("body starts with an italic dek; put it in description")
    if suffix := translation_suffix(path):
        errors += check_translation(path, suffix, meta if delim == "+++" else None, body, strict)
    return errors


def main(argv):
    strict = "--strict" in argv
    files = [Path(a) for a in argv if not a.startswith("--")]
    if not files:
        files = sorted(Path("content/posts").glob("*.md"))
    # _index.md / _index.<lang>.md describe the section, not a post.
    files = [f for f in files if not f.name.startswith("_index")]
    failed = 0
    for path in files:
        errors = check(path, strict)
        if errors:
            failed += 1
            for e in errors:
                print(f"{path}: {e}")
    print(f"{len(files)} checked, {failed} with problems")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
