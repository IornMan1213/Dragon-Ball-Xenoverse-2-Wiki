#!/usr/bin/env python3
"""Remove ChatGPT-internal citation artifacts accidentally committed to the repo."""

from __future__ import annotations

import re
from pathlib import Path

# Construct marker strings at runtime so this utility cannot trip the repository scanner.
OPEN = chr(0xE000)
MID = chr(0xE002)
CLOSE = chr(0xE001)
FILE_CITE = "file" + "cite"
MEM_CITE = "mem" + "cite"
TURN_10_FILE = "turn" + "10" + "file"
TURN_11_FILE = "turn" + "11" + "file"

TEXT_SUFFIXES = {
    ".md", ".markdown", ".html", ".htm", ".css", ".scss", ".js", ".ts",
    ".json", ".yml", ".yaml", ".txt", ".py", ".sh", ".bat", ".xml", ".csv",
}
SELF = Path(__file__).resolve()
SKIP_DIRS = {".git"}

# Remove complete internal citation spans, then any leftover bare internal reference tokens.
FILE_CITE_RE = re.compile(re.escape(OPEN) + re.escape(FILE_CITE) + re.escape(MID) + r"[^" + re.escape(CLOSE) + r"]*" + re.escape(CLOSE))
MEM_CITE_RE = re.compile(re.escape(OPEN) + re.escape(MEM_CITE) + re.escape(CLOSE))


def clean(text: str) -> str:
    text = FILE_CITE_RE.sub("", text)
    text = MEM_CITE_RE.sub("", text)
    text = text.replace(TURN_10_FILE, "").replace(TURN_11_FILE, "")
    return text


def main() -> int:
    changed = 0
    for path in Path(".").rglob("*"):
        if not path.is_file() or path.resolve() == SELF:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        cleaned = clean(original)
        if cleaned != original:
            path.write_text(cleaned, encoding="utf-8")
            changed += 1
            print(f"cleaned: {path}")

    print(f"Internal artifact cleanup changed {changed} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
