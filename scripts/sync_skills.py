#!/usr/bin/env python3
"""Build a normalized XV2 skills index from Fandom category pages."""
from __future__ import annotations

import html as html_lib
import json
import re
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_OUT = ROOT / "docs" / "data" / "skills-index.json"
CANONICAL_OUT = ROOT / "docs" / "data" / "skills.json"
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
    "Power Up Ultimates": ("Ultimate", "Power Up"),
    "Other Ultimates": ("Ultimate", "Other"),
    "Saiyan Skills": ("Awoken", "Race"),
    "Majin Skills": ("Awoken", "Race"),
    "Namekian Skills": ("Awoken", "Race"),
    "Frieza Race Skills": ("Awoken", "Race"),
    "Human Skills": ("Awoken", "Race"),
    "Transformations": ("Awoken", "Race"),
    "Unavailable for CaC": ("Mixed", "Special"),
}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={
        "User-Agent": "XV2-Wiki-Skills-Sync/2.0",
        "Accept-Language": "en-US,en;q=0.9",
    })
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read().decode("utf-8", "replace")


def clean_title(raw: str) -> str:
    raw = re.sub(r"<[^>]+>", "", raw)
    return re.sub(r"\s+", " ", html_lib.unescape(raw)).strip()


def parse_members(source: str) -> list[str]:
    """Extract only links inside Fandom's category member groups."""
    groups = re.findall(
        r'<div[^>]*class=["\'][^"\']*mw-category-group[^"\']*["\'][^>]*>(.*?)</div>',
        source,
        re.S | re.I,
    )
    if not groups:
        raise RuntimeError("Fandom category member container not found; refusing to generate an empty index")

    found: list[str] = []
    seen: set[str] = set()
    for group in groups:
        for href, label in re.findall(r'<a[^>]+href=["\'](/wiki/[^"\'#?]+)["\'][^>]*>(.*?)</a>', group, re.S | re.I):
            title = urllib.parse.unquote(href.removeprefix("/wiki/")).replace("_", " ")
            label = clean_title(label)
            if not label or title.startswith(("Category:", "File:", "Template:", "Help:", "Special:")):
                continue
            if title not in seen:
                seen.add(title)
                found.append(label)
    return sorted(found, key=str.casefold)


def load_curated() -> dict[tuple[str, str, str], dict]:
    if not CANONICAL_OUT.exists():
        return {}
    try:
        data = json.loads(CANONICAL_OUT.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    result = {}
    for record in data.get("records", []):
        key = (record.get("name", "").casefold(), record.get("class", ""), record.get("subcategory", ""))
        if key[0]:
            result[key] = {k: v for k, v in record.items() if k not in {"name", "class", "subcategory", "sources", "verification_status"}}
    return result


def main() -> int:
    curated = load_curated()
    records: list[dict] = []
    counts: dict[str, int] = {}
    for category, (kind, subtype) in CATEGORIES.items():
        url = BASE.format(urllib.parse.quote(category.replace(" ", "_")))
        members = parse_members(fetch(url))
        counts[category] = len(members)
        for name in members:
            key = (name.casefold(), kind, subtype)
            record = {
                "name": name,
                "class": kind,
                "subcategory": subtype,
                "verification_status": "indexed",
                "sources": [url],
            }
            record.update(curated.get(key, {}))
            records.append(record)

    records.sort(key=lambda x: (x["name"].casefold(), x["class"], x["subcategory"]))
    index_payload = {
        "schema_version": "1.1",
        "source_index": "https://dbxv2.fandom.com/wiki/Category:Skills",
        "generated": date.today().isoformat(),
        "category_counts": counts,
        "records": records,
    }
    INDEX_OUT.write_text(json.dumps(index_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    canonical = {
        "schema_version": "1.1",
        "game": "Dragon Ball Xenoverse 2",
        "source_index": index_payload["source_index"],
        "generated": index_payload["generated"],
        "status": "indexed_catalog",
        "notes": "Category membership is indexed automatically. Mechanics, costs, unlock methods and meta claims remain unverified until separately checked.",
        "category_counts": counts,
        "records": records,
    }
    CANONICAL_OUT.write_text(json.dumps(canonical, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(records)} category records")
    print(json.dumps(counts, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
