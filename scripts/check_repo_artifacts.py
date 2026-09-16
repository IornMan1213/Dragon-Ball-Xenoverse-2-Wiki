#!/usr/bin/env python3
"""Fail when internal assistant/file-citation artifacts are committed."""

from __future__ import annotations

from pathlib import Path

# Build markers at runtime so this checker does not match its own source.
BAD_MARKERS = tuple(
    "".join(parts)
    for parts in (
        ("file", "cite"),
        ("mem", "cite"),
        ("turn", "10", "file"),
        ("turn", "11", "file"),
    )
)

SKIP_DIRS = {".git"}
SELF = Path(__file__).resolve()
TEXT_SUFFIXES = {
    ".md", ".markdown", ".html", ".htm", ".css", ".scss", ".js", ".ts",
    ".json", ".yml", ".yaml", ".txt", ".py", ".sh", ".bat", ".xml", ".csv",
}


def main() -> int:
    failures: list[str] = []

    for path in Path(".").rglob("*"):
        if not path.is_file() or path.resolve() == SELF:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        lowered = text.lower()
        # Detect all current tool-result identifier families, not only historical examples.
        if "turn" in lowered and any(
            token in lowered
            for token in (
                "search", "file", "image", "youtube", "news", "product", "business"
            )
        ):
            import re
            if re.search(r"\bturn(?:\d+|x)(?:search|file|image|youtube|news|product|business)\d*\b", lowered):
                failures.append(f"{path}: contains internal tool-result artifact")
                continue

        for marker in BAD_MARKERS:
            if marker.lower() in lowered:
                failures.append(f"{path}: contains forbidden internal artifact")
                break

    if failures:
        print("Forbidden internal citation artifacts found:")
        print("\n".join(f"- {item}" for item in failures))
        return 1

    print("No internal citation artifacts found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
