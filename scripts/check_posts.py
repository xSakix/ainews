#!/usr/bin/env python3
"""Check posts for problems that hurt readers or search engines.

Usage:
    python3 scripts/check_posts.py                 # all posts, leak checks only
    python3 scripts/check_posts.py --strict FILE…  # new posts: also front matter

Exits 1 if any check fails.
"""
import re
import sys
import tomllib
from pathlib import Path

TAGS = {"models", "tools", "business", "research", "agents",
        "policy", "safety", "hardware", "community"}

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
    return errors


def main(argv):
    strict = "--strict" in argv
    files = [Path(a) for a in argv if not a.startswith("--")]
    if not files:
        files = sorted(Path("content/posts").glob("*.md"))
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
