#!/usr/bin/env python3
"""Say whether a story is already covered, so research and planning can skip it.

Usage:
    python3 scripts/seen.py URL_OR_TERM…     # where each one already appears
    python3 scripts/seen.py --titles [DAYS]  # titles of recent English posts

For each URL or term, lists the English posts (content/posts/<slug>.md, not the
translations) and the earlier briefings (reports/*-briefing-*.md and
reports/*-ai-briefing*.md) that contain it, oldest first. Today's files are left
out: they are the day's own work. A URL matches whatever its scheme, "www.",
trailing slash or arXiv form (abs, pdf, html, with or without a version), so
https://arxiv.org/pdf/2611.14996v2 finds a post citing arxiv.org/abs/2611.14996.
A term is matched as a case-insensitive phrase; use it for a project, model or
paper name when the URL may differ ("Gemini 4 Hydrogen").

--titles prints the date, title and description of every English post from the
past DAYS days (default 14), newest first: read it once to spot a story that an
earlier post covered under another URL.

Exits 0 whatever it finds; "new" means no earlier post or briefing has it.
"""
import datetime
import re
import sys
import tomllib
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
TRANSLATION = re.compile(r"\.(sk|nl|fr|de|es|zh)\.md$")
ARXIV = re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", re.I)
DATED = re.compile(r"^(\d{4}-\d{2}-\d{2})-")


def today():
    return datetime.datetime.now(ZoneInfo("Europe/Bratislava")).date()


def english_posts():
    for path in sorted((ROOT / "content/posts").glob("*.md")):
        if not TRANSLATION.search(path.name) and not path.name.startswith("_index"):
            yield path


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("+++"):
        return {}
    try:
        return tomllib.loads(text.split("+++", 2)[1])
    except (tomllib.TOMLDecodeError, IndexError):
        return {}


def post_date(meta):
    date = meta.get("date")
    if isinstance(date, datetime.datetime):
        return date.date()
    return date if isinstance(date, datetime.date) else None


def needle(term):
    """The lower-case string to look for in a file's lower-cased text."""
    if m := ARXIV.search(term):
        return "arxiv.org/", m.group(1)
    term = re.sub(r"^https?://(www\.)?", "", term.strip(), flags=re.I)
    return term.rstrip("/").lower(), None


def contains(text, term):
    key, arxiv_id = needle(term)
    if arxiv_id:
        return bool(re.search(r"arxiv\.org/(?:abs|pdf|html)/" + re.escape(arxiv_id), text))
    return key in text


def search(terms):
    day = today()
    posts = []
    for path in english_posts():
        meta = front_matter(path)
        date = post_date(meta)
        if date and date >= day:
            continue
        posts.append((str(date or "undated"), path, meta.get("title", ""), path.read_text(encoding="utf-8").lower()))
    briefings = []
    for path in sorted((ROOT / "reports").glob("*briefing*.md")):
        m = DATED.match(path.name)
        if m and m.group(1) < str(day):
            briefings.append((m.group(1), path, path.read_text(encoding="utf-8").lower()))

    for term in terms:
        hits = [f"  post      {date}  {path.relative_to(ROOT)}  — {title}"
                for date, path, title, text in posts if contains(text, term)]
        hits += [f"  briefing  {date}  {path.relative_to(ROOT)}"
                 for date, path, text in briefings if contains(text, term)]
        print(f"{term}: {'new' if not hits else f'seen in {len(hits)} file(s)'}")
        for line in sorted(hits, key=lambda l: l.split()[1]):
            print(line)


def titles(days):
    since = today() - datetime.timedelta(days=days)
    rows = []
    for path in english_posts():
        meta = front_matter(path)
        date = post_date(meta)
        if date and date >= since:
            rows.append((date, path.name, meta.get("title", ""), str(meta.get("description", "")).strip()))
    for date, name, title, description in sorted(rows, reverse=True):
        print(f"{date}  {title}  [{name}]")
        if description and not name.startswith("ai-daily-digest-for-"):
            print(f"            {description}")


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 0
    if argv[0] == "--titles":
        titles(int(argv[1]) if len(argv) > 1 else 14)
    else:
        search(argv)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
