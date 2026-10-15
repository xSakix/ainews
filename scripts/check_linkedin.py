#!/usr/bin/env python3
"""Check LinkedIn newsletter editions (content/linkedin/YYYY-MM-DD.sk.md).

Usage:
    python3 scripts/check_linkedin.py                 # all editions, format checks only
    python3 scripts/check_linkedin.py --strict FILE…  # new editions: also front matter
                                                      # and the comparison with the digest

An edition condenses the Slovak digest named in its `digest` field (see
prompts/linkedin-edition-prompt.md). The strict check makes sure every top
story of the digest has its block, in order, linking only that story's
sources, and that the body uses only the formatting LinkedIn's editor keeps
when the page is pasted into it.

Exits 1 if any check fails.
"""
import re
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_posts import ENGLISH_HEADINGS, ENGLISH_LABELS, H1, LEAKS, URL, urls  # noqa: E402

EDITIONS = Path("content/linkedin")
POSTS = Path("content/posts")
FILE_NAME = re.compile(r"^(\d{4})-(\d{2})-(\d{2})\.sk\.md$")
DIGEST = re.compile(r"^ai-daily-digest-for-(\d{1,2})-([a-z]+)-(\d{4})$")
MONTHS = ["january", "february", "march", "april", "may", "june", "july",
          "august", "september", "october", "november", "december"]

TOP_STORIES = "## Hlavné správy"
FURTHER = "## Ďalej v dnešnom prehľade"
SOURCE_LINE = re.compile(r"^(\*\*)?Zdroje?:(\*\*)? ")
LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
HASHTAG = re.compile(r"(?:^|\s)#[^\W\d_][^\s#]*")  # #AI, not #1 or C#
CITED = re.compile(r"(?:^|\s)Zdroje?: (.+)$")
WWW = re.compile(r"(?<![/\w.@])www\.\w")  # Hugo turns a bare www. address into a link
EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\uFE0F]")
PARAGRAPH_BREAK = re.compile(r"\n[ \t]*\n")

# Markdown that LinkedIn's article editor drops or mangles on paste.
UNSUPPORTED = [
    (re.compile(r"^#{3,} "), "heading deeper than ##"),
    (re.compile(r"^\s*\|"), "table"),
    (re.compile(r"^\s*(```|~~~)"), "code block"),
    (re.compile(r"^( {4,}|\t)\S"), "indented code block"),
    (re.compile(r"`"), "inline code"),
    (re.compile(r"!\["), "image"),
    (re.compile(r"</?[a-zA-Z][^>]*>"), "HTML tag"),
    (re.compile(r"^\s*>"), "block quote"),
    (re.compile(r"^\s*\d+[.)] "), "numbered list"),
    (re.compile(r"^\s{2,}[-*+] "), "nested list"),
    (re.compile(r"^\s*[*+] "), "list item not written with '- '"),
    (re.compile(r"^(\*{3,}|-{3,}|_{3,})\s*$"), "horizontal rule"),
]

LIMITS = {"title": 70, "description": 160, "heading": 90, "bullet": 160, "hook": 200}
# images.Text wraps the cover title only at spaces; a longer word runs off the image.
COVER_WORD = 28
SHARE_CHARS = (300, 700)
MAX_HASHTAGS = 3
BODY_WORDS = (200, 900)
FURTHER_ITEMS = (4, 6)


def split_front_matter(text):
    if not text.startswith("+++"):
        raise ValueError("no TOML front matter (+++)")
    try:
        _, fm, body = text.split("+++", 2)
    except ValueError:
        raise ValueError("unterminated front matter")
    return tomllib.loads(fm), body


def sections(body):
    """Return [(heading or None, [lines])] split at ## headings."""
    out = [(None, [])]
    for line in body.split("\n"):
        if line.startswith("## "):
            out.append((line.rstrip(), []))
        else:
            out[-1][1].append(line)
    return out


def plain(text):
    """Text as LinkedIn shows it: link labels instead of links, no markers."""
    text = LINK.sub(r"\1", text)
    return re.sub(r"\*+|_", "", text).strip()


def digest_top_stories(body):
    """For each top story in a digest's Hlavné správy section: every URL in
    the story, and the URLs of its Zdroj:/Zdroje: line in their order."""
    for heading, lines in sections(body):
        if heading and heading.startswith(TOP_STORIES):
            stories = []
            for line in lines:
                if line.startswith("**"):
                    stories.append(([], []))
                if stories:
                    stories[-1][0].extend(urls(line))
                    if m := CITED.search(line):
                        stories[-1][1].extend(u.rstrip(".,;:") for u in URL.findall(m[1]))
            return stories
    return []


def check_format(body, start):
    errors = []
    for n, line in enumerate(body.split("\n"), start=start):
        for pattern, what in LEAKS:
            if pattern.search(line):
                errors.append(f"line {n}: {what} leaked into the edition")
        if H1.match(line):
            errors.append(f"line {n}: H1 in body (the title is a separate field in LinkedIn)")
        for pattern, what in UNSUPPORTED:
            if pattern.search(line):
                errors.append(f"line {n}: {what} (LinkedIn's editor does not keep it)")
        if ENGLISH_HEADINGS.search(line) or ENGLISH_LABELS.search(line):
            errors.append(f"line {n}: English heading or claim label")
        linked = {u for _, u in LINK.findall(line)}
        if bare := [u for u in URL.findall(line) if u.rstrip(".,;:") not in linked and u not in linked]:
            errors.append(f"line {n}: bare URL {bare[0]} (write [label](URL))")
        if "ai-news-daily.xyz" in line:
            errors.append(f"line {n}: link to the site (the page appends the digest link itself)")
        if HASHTAG.search(LINK.sub("", line)):
            errors.append(f"line {n}: hashtag in the body (hashtags belong in the share post)")
        if WWW.search(LINK.sub("", line)):
            errors.append(f"line {n}: bare www. address (Hugo turns it into a link; write [label](URL))")
        if EMOJI.search(line):
            errors.append(f"line {n}: emoji")
    return errors


def check_structure(body, digest_body):
    errors = []
    parts = sections(body)
    opening = [l for l in parts[0][1] if l.strip()]
    if not opening:
        errors.append("no opening paragraph before the first story")
    if any(l.startswith("- ") for l in opening):
        errors.append("the opening is one or two sentences, not a list")

    stories = [(h, ls) for h, ls in parts[1:] if not h.startswith(FURTHER)]
    further = [(h, ls) for h, ls in parts[1:] if h.startswith(FURTHER)]
    if further and parts[-1][0] != further[0][0]:
        errors.append(f"'{FURTHER}' must be the last section")
    if len(further) > 1:
        errors.append(f"'{FURTHER}' appears more than once")

    for heading, lines in stories:
        if len(plain(heading[3:])) > LIMITS["heading"]:
            errors.append(f"heading longer than {LIMITS['heading']} characters: {heading[3:50]}…")
        if heading.endswith("."):
            errors.append(f"heading ends with a period: {heading[3:50]}…")
        nonblank = [l for l in lines if l.strip()]
        if len(nonblank) < 2 or not SOURCE_LINE.match(nonblank[-1]):
            errors.append(f"story '{heading[3:40]}…' needs its paragraph, then the Zdroj line last")

    expected = digest_top_stories(digest_body) if digest_body is not None else None
    if expected is not None:
        if not expected:
            errors.append(f"digest has no '{TOP_STORIES}' section with bold-led stories")
        elif len(stories) != len(expected):
            errors.append(f"{len(stories)} story blocks, but the digest has {len(expected)} top stories")
        for i, ((heading, lines), (sources, cited)) in enumerate(zip(stories, expected), start=1):
            source_lines = [l for l in lines if SOURCE_LINE.match(l)]
            if len(source_lines) != 1:
                errors.append(f"story {i} ({heading[3:40]}…) needs exactly one 'Zdroj:'/'Zdroje:' line")
            linked = [u for l in lines for _, u in LINK.findall(l)]
            if not linked:
                errors.append(f"story {i} ({heading[3:40]}…) links no source")
            if stray := [u for u in linked if u not in sources]:
                errors.append(f"story {i} ({heading[3:40]}…) links {stray[0]}, which is not among that top story's sources in the digest")
            given = [u for l in source_lines for _, u in LINK.findall(l)]
            if cited and source_lines and given != cited[:3]:
                errors.append(f"story {i} ({heading[3:40]}…): the Zdroj line must link {cited[:3]}, the digest's sources for that story in their order")

    if further:
        items = [l for l in further[0][1] if l.startswith("- ")]
        if stray := [l for l in further[0][1] if l.strip() and not l.startswith(("- ", "  "))]:
            errors.append(f"'{FURTHER}' holds only the list (the page appends the closing block); remove: {stray[0][:60]}")
        if not FURTHER_ITEMS[0] <= len(items) <= FURTHER_ITEMS[1]:
            errors.append(f"'{FURTHER}' needs {FURTHER_ITEMS[0]}-{FURTHER_ITEMS[1]} items, has {len(items)}")
        if linked := [l for l in further[0][1] if LINK.search(l)]:
            errors.append(f"'{FURTHER}' has a link (the digest link below carries them): {linked[0][:50]}…")
        for item in items:
            if len(plain(item[2:])) > LIMITS["bullet"]:
                errors.append(f"'{FURTHER}' item longer than {LIMITS['bullet']} characters: {item[2:50]}…")
    else:
        errors.append(f"missing '{FURTHER}' section")

    words = len(plain(body).split())
    if not BODY_WORDS[0] <= words <= BODY_WORDS[1]:
        errors.append(f"body has {words} words; an edition has {BODY_WORDS[0]}-{BODY_WORDS[1]}")
    return errors


def check(path, strict):
    if not (m := FILE_NAME.match(path.name)):
        return ["file name must be YYYY-MM-DD.sk.md"]
    text = path.read_text(encoding="utf-8")
    try:
        meta, body = split_front_matter(text)
    except (ValueError, tomllib.TOMLDecodeError) as e:
        return [f"front matter: {e}"]

    errors = check_format(body, start=text[: len(text) - len(body)].count("\n") + 1)
    for key in ("author", "hideAuthor", "tags"):
        if key in meta:
            errors.append(f"front matter must not set {key}")
    if (li := meta.get("linkedin")) and not str(li).startswith("https://www.linkedin.com/"):
        errors.append("linkedin must be the edition's https://www.linkedin.com/ address")
    if not strict:
        return errors

    for key in ("title", "description", "digest", "date", "share"):
        if not str(meta.get(key, "")).strip():
            errors.append(f"missing {key}")
    for key in ("title", "description"):
        if len(str(meta.get(key, ""))) > LIMITS[key]:
            errors.append(f"{key} longer than {LIMITS[key]} characters")
    title = str(meta.get("title", "")).strip()
    if title.endswith("."):
        errors.append("title ends with a period")
    if long := [w for w in title.split() if len(w) > COVER_WORD]:
        errors.append(f"title word {long[0]!r} is longer than {COVER_WORD} characters (the cover image cannot wrap it)")
    for key in ("title", "description", "share"):
        if EMOJI.search(str(meta.get(key, ""))):
            errors.append(f"{key} has an emoji")
    if meta.get("draft") is not False:
        errors.append("draft must be false")

    share = str(meta.get("share", "")).strip()
    if share and not SHARE_CHARS[0] <= len(share) <= SHARE_CHARS[1]:
        errors.append(f"share post has {len(share)} characters; it needs {SHARE_CHARS[0]}-{SHARE_CHARS[1]}")
    if len(PARAGRAPH_BREAK.split(share)[0]) > LIMITS["hook"]:
        errors.append(f"share post's first paragraph is longer than {LIMITS['hook']} characters (LinkedIn folds the post there)")
    if len(HASHTAG.findall(share)) > MAX_HASHTAGS:
        errors.append(f"share post has more than {MAX_HASHTAGS} hashtags")
    if URL.search(share) or re.search(r"(?i)\bwww\.|ai-news-daily\.xyz", share):
        errors.append("share post has a link or web address (LinkedIn attaches the edition itself)")

    digest_body = None
    name = str(meta.get("digest", ""))
    if not (d := DIGEST.match(name)):
        errors.append(f"digest {name!r} must be a digest file name such as ai-daily-digest-for-14-october-2026")
    else:
        day, month, year = int(d[1]), d[2], int(d[3])
        if month not in MONTHS or (year, MONTHS.index(month) + 1, day) != (int(m[1]), int(m[2]), int(m[3])):
            errors.append(f"digest {name} is not the digest of {path.name[:10]}")
        twin = POSTS / f"{name}.sk.md"
        if not twin.exists():
            errors.append(f"Slovak digest {twin} not found")
        else:
            try:
                digest_meta, digest_body = split_front_matter(twin.read_text(encoding="utf-8"))
            except (ValueError, tomllib.TOMLDecodeError) as e:
                errors.append(f"Slovak digest {twin.name}: {e}")
            else:
                if meta.get("date") != digest_meta.get("date"):
                    errors.append(f"date differs from {twin.name}")
                if extra := sorted(set(urls(body)) - set(urls(digest_body))):
                    errors.append(f"URLs not in {twin.name}: {extra[:3]}")
    errors += check_structure(body, digest_body)
    return errors


def main(argv):
    strict = "--strict" in argv
    files = [Path(a) for a in argv if not a.startswith("--")]
    if not files:
        files = sorted(EDITIONS.glob("*.md"))
    # _index.<lang>.md describes the section, not an edition.
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
