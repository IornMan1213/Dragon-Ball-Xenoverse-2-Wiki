#!/usr/bin/env python3
"""Fail when internal assistant/file-citation artifacts are committed.

The checker scans Git-tracked text files only, which keeps generated workspace
files from affecting CI while still auditing every committed text artifact.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
CLEANER = ROOT / "scripts" / "strip_internal_artifacts.py"
TEXT_SUFFIXES = {
    ".md", ".markdown", ".html", ".htm", ".css", ".scss", ".js", ".ts",
    ".json", ".yml", ".yaml", ".txt", ".py", ".sh", ".bat", ".xml", ".csv",
}

BAD_MARKERS = tuple(
    "".join(parts)
    for parts in (
        ("file" + "cite",),
        ("mem" + "cite",),
        ("turn", "10", "file"),
        ("turn", "11", "file"),
    )
)
TURN_REF_RE = re.compile(
    r"\bturn(?:\d+|x)(?:search|file|image|youtube|news|product|business)\d*\b",
    re.IGNORECASE,
)
# The content-reference UI delimiter used by the assistant is U+E000/U+E001.
# Do not reject unrelated Unicode private-use characters: projects may legitimately
# use private-use glyphs in fonts/assets, and the artifact contract targets the
# assistant citation delimiters specifically.
PUA_RE = re.compile(r"[\uE000\uE001]")


def tracked_files() -> list[Path]:
    """Return Git-tracked paths so CI audits the committed tree deterministically."""
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        text=False,
    )
    return [ROOT / raw.decode("utf-8") for raw in result.stdout.split(b"\0") if raw]


def main() -> int:
    failures: list[str] = []
    paths = tracked_files()

    for path in paths:
        if path.resolve() in {SELF, CLEANER} or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        lowered = text.lower()
        relative = path.relative_to(ROOT)

        if PUA_RE.search(text):
            failures.append(f"{relative}: contains assistant content-reference delimiter")
            continue
        if TURN_REF_RE.search(lowered):
            failures.append(f"{relative}: contains internal tool-result artifact")
            continue
        for marker in BAD_MARKERS:
            if marker.lower() in lowered:
                failures.append(f"{relative}: contains forbidden internal artifact")
                break

    if failures:
        print("Forbidden internal citation artifacts found:")
        print("\n".join(f"- {item}" for item in failures))
        return 1

    print(f"No internal citation artifacts found across {len(paths)} tracked file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
