#!/usr/bin/env python3
"""Remove ChatGPT-internal citation/export artifacts accidentally committed to the repo."""

from __future__ import annotations

import re
from pathlib import Path

OPEN = chr(0xE000)
CLOSE = chr(0xE001)

TEXT_SUFFIXES = {
    ".md", ".markdown", ".html", ".htm", ".css", ".scss", ".js", ".ts",
    ".json", ".yml", ".yaml", ".txt", ".py", ".sh", ".bat", ".xml", ".csv",
}
SELF = Path(__file__).resolve()
SKIP_DIRS = {".git"}

# Content-reference spans are internal UI/export markup and must never be committed.
PUA_SPAN_RE = re.compile(re.escape(OPEN) + r"[^" + re.escape(CLOSE) + r"]*" + re.escape(CLOSE))
# Any remaining Unicode private-use character is also forbidden by the artifact checker.
# This catches malformed/partial exports where the opening/closing delimiters are missing.
PUA_RE = re.compile(r"[\uE000-\uF8FF]")
# Remove bare tool-result identifiers left behind after a citation span was stripped.
BARE_MARKER_RE = re.compile(r"\\b(?:filecite|memcite)\\b", re.IGNORECASE)
TURN_REF_RE = re.compile(
    r"\bturn(?:\d+|X)(?:search|file|image|youtube|news|product|business)\d*\b",
    re.IGNORECASE,
)


def clean(text: str) -> str:
    text = PUA_SPAN_RE.sub("", text)
    text = PUA_RE.sub("", text)
    text = BARE_MARKER_RE.sub("", text)
    text = TURN_REF_RE.sub("", text)
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
