#!/usr/bin/env python3
"""Fail when internal assistant/file-citation artifacts are committed."""

from __future__ import annotations

from pathlib import Path

BAD_MARKERS = (
    "filecite",
    "memcite",
    "turn10file",
    "turn11file",
)

SKIP_DIRS = {".git", ".github"}
TEXT_SUFFIXES = {
    ".md", ".markdown", ".html", ".htm", ".css", ".scss", ".js", ".ts",
    ".json", ".yml", ".yaml", ".txt", ".py", ".sh", ".bat", ".xml", ".csv",
}


def main() -> int:
    failures: list[str] = []

    for path in Path(".").rglob("*"):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        lowered = text.lower()
        for marker in BAD_MARKERS:
            if marker.lower() in lowered:
                failures.append(f"{path}: contains forbidden marker {marker!r}")
                break

    if failures:
        print("Forbidden internal citation artifacts found:")
        print("\n".join(f"- {item}" for item in failures))
        return 1

    print("No internal citation artifacts found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
