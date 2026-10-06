#!/usr/bin/env python3
"""List the English posts that need a translation, in the order to do them.

Usage:
    python3 scripts/translation_queue.py nl              # Dutch, defaults
    python3 scripts/translation_queue.py nl --days 3 --backlog 10

Prints one line per post: "<reason> content/posts/<slug>.md", where reason is
  missing  dated within the last --days days (today included) and no twin yet
  stale    has a twin, but the English file was committed after the twin
  backlog  older than the window and no twin yet (newest first, at most
           --backlog of them)
Within each group, newer posts come first; posts with the same date keep
their timestamp order, which is the day's rank order.

"Today" is the date in Europe/Bratislava. Drafts are skipped.
"""
import argparse
import subprocess
import sys
import tomllib
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

POSTS = Path("content/posts")
TZ = ZoneInfo("Europe/Bratislava")


def english_posts():
    for path in sorted(POSTS.glob("*.md")):
        name = path.name
        # <slug>.md only: skip <slug>.<lang>.md twins and _index pages.
        if name.startswith("_index") or "." in name[: -len(".md")]:
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("+++"):
            continue
        try:
            meta = tomllib.loads(text.split("+++", 2)[1])
        except tomllib.TOMLDecodeError:
            continue
        date = meta.get("date")
        if meta.get("draft") or not isinstance(date, datetime):
            continue
        if date.tzinfo is None:
            date = date.replace(tzinfo=TZ)
        yield path, date


def committed_at(path):
    """Unix time of the last commit touching path, or 0 if uncommitted."""
    out = subprocess.run(["git", "log", "-1", "--format=%ct", "--", str(path)],
                         capture_output=True, text=True).stdout.strip()
    return int(out) if out else 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("lang", help="language code of the twin, e.g. nl")
    ap.add_argument("--days", type=int, default=3)
    ap.add_argument("--backlog", type=int, default=10)
    args = ap.parse_args(argv)

    today = datetime.now(TZ).date()
    first_day = today - timedelta(days=args.days - 1)
    missing, stale, backlog = [], [], []
    for path, date in english_posts():
        twin = path.with_name(path.stem + f".{args.lang}.md")
        recent = date.astimezone(TZ).date() >= first_day
        if not twin.exists():
            (missing if recent else backlog).append((date, path))
        elif recent and committed_at(path) > committed_at(twin):
            stale.append((date, path))

    for reason, group, limit in (("missing", missing, None),
                                 ("stale", stale, None),
                                 ("backlog", backlog, args.backlog)):
        for _, path in sorted(group, key=lambda x: x[0], reverse=True)[:limit]:
            print(f"{reason} {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
