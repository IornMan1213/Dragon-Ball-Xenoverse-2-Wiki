#!/usr/bin/env python3
"""Build a normalized XV2 skills index from Fandom category pages.

This tool intentionally indexes names/category membership first. It does not
invent mechanics, costs, unlocks, or damage values. Those fields belong in the
canonical JSON records only after independent verification.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "data" / "skills-index.json"
BASE = "https://dbxv2.fandom.com/wiki/Category:{}"
CATEGORIES = {
    "Ki Blast Supers": ("Super", "Ki Blast"),
    "Strike Supers": ("Super", "Strike"),
    "Ki Blast Ultimates": ("Ultimate", "Ki Blast"),
    "Strike Ultimates": ("Ultimate", "Strike"),
    "Other Supers": ("Super", "Other"),
    "Power Up Supers": ("Super", "Power Up"),
    "Ki Blast Evasives": ("Evasive", "Ki Blast"),
    "Strike Evasives": ("Evasive", "Strike"),
    "Other Evasives": ("Evasive", "Other"),
    "Power Up Evasives": ("Evasive", "Power Up"),
    "Other Ultimates": ("Ultimate", "Other"),
    "Saiyan Skills": ("Awoken", "Race"),
    "Majin Skills": ("Awoken", "Race"),
    "Namekian Skills": ("Awoken", "Race"),
    "Frieza Race Skills": ("Awoken", "Race"),
    "Human Skills": ("Awoken", "Race"),
    "Unavailable for CaC": ("Mixed", "Special"),
}


def fetch(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "XV2-Wiki-Skills-Sync/1.0",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read().decode("utf-8", "replace")


def clean_title(raw: str) -> str:
    raw = re.sub(r"<[^>]+>", "", raw)
    raw = raw.replace("&#39;", "'").replace("&amp;", "&")
    return re.sub(r"\s+", " ", raw).strip()


def parse_members(html: str) -> list[str]:
    # Fandom category pages expose member links with mw-category-generated markup.
    # Restrict parsing to wiki links and discard namespace/category/navigation links.
    found: list[str] = []
    seen: set[str] = set()
    for href, label in re.findall(r'href="(/wiki/[^"#?]+)"[^>]*>(.*?)</a>', html, re.S):
        title = urllib.parse.unquote(href.removeprefix("/wiki/")).replace("_", " ")
        label = clean_title(label)
        if not label or title.startswith(("Category:", "File:", "Template:", "Help:", "Special:")):
            continue
        if title not in seen and re.search(r"mw-category|CategoryTree", html):
            seen.add(title)
            found.append(label)
    return sorted(found, key=str.casefold)


def main() -> int:
    records: list[dict] = []
    counts: dict[str, int] = {}
    for category, (kind, subtype) in CATEGORIES.items():
        url = BASE.format(urllib.parse.quote(category.replace(" ", "_")))
        html = fetch(url)
        members = parse_members(html)
        counts[category] = len(members)
        for name in members:
            records.append(
                {
                    "name": name,
                    "class": kind,
                    "subcategory": subtype,
                    "verification_status": "indexed",
                    "sources": [url],
                }
            )

    payload = {
        "schema_version": "1.0",
        "source_index": "https://dbxv2.fandom.com/wiki/Category:Skills",
        "category_counts": counts,
        "records": sorted(records, key=lambda x: (x["name"].casefold(), x["class"], x["subcategory"])),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(records)} indexed records to {OUT}")
    print(json.dumps(counts, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
