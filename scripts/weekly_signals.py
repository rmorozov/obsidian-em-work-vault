#!/usr/bin/env python3
"""Print non-task bullets under '## Daily Record' from dated daily notes.

Uses only the local directory supplied by the caller. It never accesses network
services or sends content to an LLM.
"""
import argparse
import datetime as dt
import re
from pathlib import Path

DATE = re.compile(r"^(\d{4}-\d{2}-\d{2})\.md$")
BULLET = re.compile(r"^\s*[-*+]\s+(?!\[[ xX]\]\s)(.+?)\s*$")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def records(text):
    inside = False
    for line in text.splitlines():
        match = HEADING.match(line)
        if match:
            level, title = match.groups()
            if level == "##":
                inside = title.casefold() == "daily record"
            elif inside and len(level) < 3:
                inside = False
            continue
        if inside:
            bullet = BULLET.match(line)
            if bullet and bullet.group(1).strip():
                yield bullet.group(1).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("daily_dir", type=Path)
    parser.add_argument("--week", required=True, help="ISO week, e.g. 2026-W38")
    args = parser.parse_args()
    try:
        year, week = map(int, args.week.split("-W"))
        start = dt.date.fromisocalendar(year, week, 1)
    except (ValueError, TypeError) as exc:
        parser.error(f"invalid ISO week: {exc}")
    end = start + dt.timedelta(days=7)
    if not args.daily_dir.is_dir():
        parser.error(f"not a directory: {args.daily_dir}")
    for path in sorted(args.daily_dir.glob("*.md")):
        match = DATE.match(path.name)
        if not match:
            continue
        try:
            date = dt.date.fromisoformat(match.group(1))
        except ValueError:
            continue
        if start <= date < end:
            for item in records(path.read_text(encoding="utf-8")):
                print(f"- {item} — [[{path.stem}]]")


if __name__ == "__main__":
    main()
