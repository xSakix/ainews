#!/usr/bin/env python3
"""Check posts for problems that hurt readers or search engines.

Usage:
    python3 scripts/check_posts.py                 # all posts, leak checks only
    python3 scripts/check_posts.py --strict FILE…  # new posts: also front matter

Translations (<slug>.<lang>.md for sk, nl, fr, de, es, zh) are also checked
against their English twin (<slug>.md): same tags, date and source URLs, and
claim labels in the translation's language only. With --strict they must also
have the same number of headings, paragraphs, list items and table rows as the
twin, no paragraph left in English and, for Slovak, none of the unambiguous
`avoid` forms of prompts/translation-maps/sk.yaml.

Lines starting "note:" are not failures: they point at wording a writer or
translator should look at once (a phrase from the prompts' avoid lists, a
number format). A passing --strict check of one file prints an "ok:" line with
the counts it compared; runs copy that line into their log.

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
ENGLISH_HEADINGS = re.compile(r"^## (Why it matters|Verification|Top stories|In brief|Releases|Research|Economy and work|Prompting techniques|What people are building|Worth reading|Business, briefly|What to watch|References)\b")

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
# The fixed line an article carries after an invented opening scene
# (prompts/article-writer-prompt.md). Translators replace it with their
# language's fixed line, so the English one must not survive in a twin.
ILLUSTRATION_NOTE = "are illustrations; the people in them are invented"

# Unambiguous `avoid` forms from prompts/translation-maps/sk.yaml: these stems
# are wrong in every sense an AI post uses them in. Forms that are correct in
# another sense (politika, zisk, stopa, zručnosť ...) stay with the translator.
SK_AVOID = [
    (re.compile(r"\bhraničn\w*\s+(model|laborat|AI\b|chatbot|asistent|systém)", re.I), "hraničný for frontier (use špičkový)"),
    (re.compile(r"\bzarovnan\w*", re.I), "zarovnanie for alignment (use zosúladenie)"),
    (re.compile(r"\bposilňovac\w*\s+učen|\bučen\w*\s+posilňovaním", re.I), "use posilňované učenie"),
    (re.compile(r"\bserviln\w*|\bpritakáv\w*", re.I), "use pochlebovanie for sycophancy"),
    (re.compile(r"\bagenty\b|\bagentov(ý|á|é|ého|ej|ých|ými|ú)\b", re.I), "agenti is animate; use agentický, not agentový"),
    (re.compile(r"\breťaz\w*\s+myšlienok", re.I), "use reťazec uvažovania"),
]
# English function words that no other edition's language shares.
ENGLISH_WORDS = re.compile(r"\b(the|and|that|with|which|this|from|have|were|their|would|about)\b", re.I)
# Phrases the writer prompts ask to avoid (English posts; notes only).
STOCK = re.compile(
    r"\b(delv(e|es|ed|ing)|showcas(e|es|ed|ing)|underscor(e|es|ed|ing)|pivotal|seamless(ly)?|"
    r"game-changer|revolutionary|it'?s worth noting|notably|not just\b[^.]{0,60}\bbut)\b", re.I)
UNSPACED_PERCENT = re.compile(r"\d%")

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


def blocks(body):
    """Count the body's blocks by kind; a translation keeps every count."""
    counts = {"headings": 0, "paragraphs": 0, "list items": 0, "table rows": 0}
    in_para = in_fence = False
    for line in body.split("\n"):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
        if not stripped or in_fence:
            in_para = False
        elif re.match(r"#{2,6} ", stripped):
            counts["headings"] += 1
            in_para = False
        elif re.match(r"([-*+]|\d+\.) ", stripped):
            counts["list items"] += 1
            in_para = False
        elif stripped.startswith("|"):
            if not re.fullmatch(r"\|[\s:|-]+\|?", stripped):
                counts["table rows"] += 1
            in_para = False
        elif not in_para:
            counts["paragraphs"] += 1
            in_para = True
    return counts


def prose_lines(body):
    """Yield (line number, text without URLs and code) up to the reference list."""
    in_fence = False
    for n, line in enumerate(body.split("\n"), start=1):
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or line.lstrip().startswith("|"):
            continue
        if re.match(r"## (References|Použité zdroje|Quellen|Referenties|Bronnen|Références|Referencias|参考)", line):
            return
        yield n, re.sub(r"`[^`]*`", "", URL.sub("", line))


def translation_suffix(path):
    return next((sfx for sfx in TRANSLATIONS if path.name.endswith(sfx)), None)


def check_translation(path, suffix, meta, body, strict, notes_out):
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

    if ILLUSTRATION_NOTE in body:
        errors.append("the illustration note is still in English (use the translator prompt's fixed line)")

    if strict:
        en_blocks, own_blocks = blocks(en_body), blocks(body)
        for kind, n in en_blocks.items():
            if own_blocks[kind] != n:
                errors.append(f"{own_blocks[kind]} {kind}, {twin.name} has {n}")
        for n, line in prose_lines(body):
            words = re.findall(r"[A-Za-z']+", re.sub(r"[\"“„«»].*?[\"”“»]|\*[^*]+\*", "", line))
            if len(words) >= 12 and len(ENGLISH_WORDS.findall(" ".join(words))) >= 0.15 * len(words):
                errors.append(f"body line {n}: paragraph left in English")
            if suffix == ".sk.md":
                for pattern, what in SK_AVOID:
                    if m := pattern.search(line):
                        errors.append(f"body line {n}: „{m.group(0)}“: {what}")
            if suffix in (".sk.md", ".de.md", ".fr.md") and UNSPACED_PERCENT.search(line):
                notes_out.append(f"body line {n}: percent sign without a space")
        if suffix == ".sk.md" and meta is not None:
            for field in ("title", "description"):
                for pattern, what in SK_AVOID:
                    if m := pattern.search(str(meta.get(field, ""))):
                        errors.append(f"{field}: „{m.group(0)}“: {what}")
        if not errors:
            summary = ", ".join(f"{n} {kind}" for kind, n in own_blocks.items() if n)
            notes_out.append(f"ok: {summary} and {len(urls(body))} source URLs match {twin.name}")

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


def check(path, strict, notes_out=None):
    """Return the file's failures; append non-failing remarks to notes_out."""
    errors = []
    if notes_out is None:
        notes_out = []
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
    # The site-wide author marks every post as AI-generated (EU AI Act,
    # Art. 50); a per-post author would replace that label.
    if "author" in meta or "hideAuthor" in meta:
        errors.append("front matter must not set author or hideAuthor (posts are labelled AI-generated site-wide)")

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
        errors += check_translation(path, suffix, meta if delim == "+++" else None, body, strict, notes_out)
    elif strict:
        for n, line in prose_lines(body):
            if m := STOCK.search(re.sub(r"[\"“].*?[\"”]", "", line)):
                notes_out.append(f"note: body line {n}: \"{m.group(0)}\" is on the writer prompts' avoid list")
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
        notes = []
        errors = check(path, strict, notes)
        if errors:
            failed += 1
            for e in errors:
                print(f"{path}: {e}")
        if strict:
            for note in notes:
                print(f"{path}: {note if note.startswith(('ok:', 'note:')) else 'note: ' + note}")
    print(f"{len(files)} checked, {failed} with problems")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
