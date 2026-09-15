#!/usr/bin/env python3
"""Build a normalized XV2 skill catalog from Fandom categories + page data.

The sync is deliberately conservative: category membership is indexed automatically,
while mechanics/acquisition fields are promoted only when the source page exposes a
usable value. Missing fields stay explicit rather than being guessed.
"""
from __future__ import annotations

import html
import json
import re
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_OUT = ROOT / "docs" / "data" / "skills-index.json"
CANONICAL_OUT = ROOT / "docs" / "data" / "skills.json"
BASE = "https://dbxv2.fandom.com"
API = BASE + "/api.php"

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
    "Counter Skills": ("Counter", "Counter"),
}

HEADERS = {
    "User-Agent": "XV2-Wiki-Skills-Sync/3.0 (+https://github.com/IornMan1213/Dragon-Ball-Xenoverse-2-Wiki)",
    "Accept": "application/json,text/plain,*/*",
    "Accept-Language": "en-US,en;q=0.9",
}

FIELD_ALIASES = {
    "ki_cost": {"ki cost", "ki", "ki required", "ki req"},
    "stamina_cost": {"stamina cost", "stamina", "stamina required", "stamina req"},
    "damage_type": {"type", "damage type", "attack type"},
    "unlock_method": {"unlock", "how to obtain", "obtained", "obtain", "acquisition", "acquired from"},
    "source_quest_or_shop": {"source", "quest", "parallel quest", "pq", "shop", "obtained from"},
    "dlc_requirement": {"dlc", "dlc requirement", "pack", "expansion"},
    "race_restriction": {"race", "race restriction", "available to"},
    "character_source": {"character", "user", "users", "cast", "character source"},
    "usable_by_cac": {"cac", "usable by cac", "custom character", "custom characters"},
}


def http_json(url: str) -> dict:
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.loads(response.read().decode("utf-8", "replace"))


def api(params: dict[str, str | int]) -> dict:
    query = urllib.parse.urlencode({"format": "json", "formatversion": 2, **params})
    return http_json(f"{API}?{query}")


def normalize_text(value: str) -> str:
    value = re.sub(r"<ref[^>]*>.*?</ref>", "", value, flags=re.I | re.S)
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\{\{[^{}]*\}\}", "", value)
    value = re.sub(r"\[\[(?:[^\]|]+\|)?([^\]]+)\]\]", r"\1", value)
    value = re.sub(r"'{2,5}", "", value)
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip(" |\t\r\n")


def canonical_key(label: str) -> str:
    label = normalize_text(label).casefold()
    label = re.sub(r"[^a-z0-9]+", " ", label).strip()
    return label


def extract_infobox(wikitext: str) -> dict[str, str]:
    """Extract first template that looks like an infobox without parsing nested templates."""
    start = re.search(r"\{\{\s*(?:Skill|Move|Technique|Infobox[^\n}]*)", wikitext, flags=re.I)
    if not start:
        return {}
    pos = start.start()
    depth = 0
    end = None
    for i in range(pos, len(wikitext) - 1):
        pair = wikitext[i:i + 2]
        if pair == "{{":
            depth += 1
        elif pair == "}}":
            depth -= 1
            if depth == 0:
                end = i + 2
                break
    block = wikitext[pos:end] if end else wikitext[pos:pos + 12000]
    fields: dict[str, str] = {}
    for match in re.finditer(r"^\s*\|\s*([^=\n]+?)\s*=\s*(.*?)\s*$", block, flags=re.M | re.S):
        key = canonical_key(match.group(1))
        value = normalize_text(match.group(2))
        if key and value:
            fields[key] = value
    return fields


def find_field(fields: dict[str, str], aliases: set[str]) -> str | None:
    aliases_normalized = {canonical_key(a) for a in aliases}
    for key, value in fields.items():
        if key in aliases_normalized:
            return value
    for key, value in fields.items():
        if any(alias in key for alias in aliases_normalized):
            return value
    return None


def extract_description(wikitext: str) -> str | None:
    """Pick the first useful prose paragraph after removing templates/headings."""
    cleaned = re.sub(r"\{\{.*?\}\}", "", wikitext, flags=re.S)
    cleaned = re.sub(r"<[^>]+>", " ", cleaned)
    paragraphs = re.split(r"\n\s*\n+", cleaned)
    for paragraph in paragraphs:
        text = normalize_text(paragraph)
        if len(text) < 50:
            continue
        if text.startswith(("#", "==", "This page", "Categories", "Navigation")):
            continue
        if text.startswith(("Obtained", "How to", "Unlock")):
            continue
        return text[:1000]
    return None


def page_records(titles: list[str]) -> dict[str, dict]:
    """Fetch up to 50 skill pages at a time through the MediaWiki API."""
    result: dict[str, dict] = {}
    for offset in range(0, len(titles), 50):
        batch = titles[offset:offset + 50]
        data = api({
            "action": "query",
            "prop": "revisions|info",
            "rvprop": "content",
            "rvslots": "main",
            "inprop": "url",
            "titles": "|".join(batch),
        })
        for page in data.get("query", {}).get("pages", []):
            title = page.get("title")
            revision = (page.get("revisions") or [{}])[0]
            slots = revision.get("slots") or {}
            content = (slots.get("main") or {}).get("content") or revision.get("content") or ""
            result[title] = {
                "wikitext": content,
                "url": page.get("fullurl") or f"{BASE}/wiki/{urllib.parse.quote(str(title).replace(' ', '_'))}",
            }
        print(f"Fetched skill pages {min(offset + 50, len(titles))}/{len(titles)}")
        time.sleep(0.2)
    return result


def category_members(category: str) -> list[str]:
    titles: list[str] = []
    params: dict[str, str | int] = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": f"Category:{category}",
        "cmnamespace": 0,
        "cmlimit": 500,
    }
    while True:
        data = api(params)
        titles.extend(item["title"] for item in data.get("query", {}).get("categorymembers", []))
        cont = data.get("continue")
        if not cont:
            break
        params.update(cont)
    return sorted(set(titles), key=str.casefold)


def load_curated() -> dict[tuple[str, str, str], dict]:
    if not CANONICAL_OUT.exists():
        return {}
    try:
        data = json.loads(CANONICAL_OUT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    result: dict[tuple[str, str, str], dict] = {}
    for record in data.get("records", []):
        key = (record.get("name", "").casefold(), record.get("class", ""), record.get("subcategory", ""))
        if key[0]:
            result[key] = {k: v for k, v in record.items() if k not in {"name", "class", "subcategory", "sources"}}
    return result


def enrich(record: dict, page: dict | None) -> dict:
    if not page:
        record["research_status"] = "page_unavailable"
        return record

    fields = extract_infobox(page.get("wikitext", ""))
    mapping = {
        "ki_cost": "ki_cost",
        "stamina_cost": "stamina_cost",
        "damage_type": "damage_type",
        "unlock_method": "unlock_method",
        "source_quest_or_shop": "source_quest_or_shop",
        "dlc_requirement": "dlc_requirement",
        "race_restriction": "race_restriction",
        "character_source": "character_source",
        "usable_by_cac": "usable_by_cac",
    }
    for output_key, _ in mapping.items():
        value = find_field(fields, FIELD_ALIASES[output_key])
        if value:
            if output_key == "usable_by_cac":
                low = value.casefold()
                record[output_key] = not any(token in low for token in ("no", "not", "false", "cannot"))
            else:
                record[output_key] = value

    description = extract_description(page.get("wikitext", ""))
    if description:
        record["skill_description"] = description

    populated = sum(1 for key in (
        "ki_cost", "stamina_cost", "damage_type", "unlock_method",
        "source_quest_or_shop", "dlc_requirement", "skill_description",
    ) if record.get(key))
    record["research_status"] = "enriched" if populated >= 3 else "partially_enriched"
    record["verification_status"] = "verified" if populated >= 5 else "partially_verified"
    return record


def main() -> int:
    curated = load_curated()
    members_by_category: dict[str, list[str]] = {}
    all_titles: set[str] = set()
    counts: dict[str, int] = {}

    for category in CATEGORIES:
        members = category_members(category)
        members_by_category[category] = members
        counts[category] = len(members)
        all_titles.update(members)
        time.sleep(0.15)

    pages = page_records(sorted(all_titles, key=str.casefold))
    records_by_key: dict[tuple[str, str, str], dict] = {}

    for category, (skill_class, subtype) in CATEGORIES.items():
        source_url = f"{BASE}/wiki/Category:{urllib.parse.quote(category.replace(' ', '_'))}"
        for title in members_by_category[category]:
            record = {
                "name": title,
                "class": skill_class,
                "subcategory": subtype,
                "verification_status": "indexed",
                "research_status": "indexed",
                "sources": [source_url],
            }
            record.update(curated.get((title.casefold(), skill_class, subtype), {}))
            page = pages.get(title)
            if page:
                record.setdefault("sources", []).append(page["url"])
            record = enrich(record, page)
            record["sources"] = list(dict.fromkeys(record["sources"]))
            records_by_key[(title.casefold(), skill_class, subtype)] = record

    records = sorted(records_by_key.values(), key=lambda r: (r["name"].casefold(), r["class"], r["subcategory"]))
    generated = date.today().isoformat()

    payload = {
        "schema_version": "1.2",
        "game": "Dragon Ball Xenoverse 2",
        "source_index": f"{BASE}/wiki/Category:Skills",
        "generated": generated,
        "status": "enriched_catalog",
        "notes": "Category membership is indexed automatically. Mechanics/acquisition fields are promoted only when page data supplied a usable value; missing information is left explicit rather than guessed.",
        "category_counts": counts,
        "record_count": len(records),
        "records": records,
    }
    CANONICAL_OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    INDEX_OUT.write_text(json.dumps({
        "schema_version": "1.2",
        "source_index": payload["source_index"],
        "generated": generated,
        "category_counts": counts,
        "record_count": len(records),
        "records": [{k: r[k] for k in ("name", "class", "subcategory", "verification_status", "sources")} for r in records],
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Wrote {len(records)} unique category records from {len(CATEGORIES)} categories")
    for category, count in counts.items():
        print(f"{category}: {count}")
    verified = sum(r["verification_status"] == "verified" for r in records)
    partial = sum(r["verification_status"] == "partially_verified" for r in records)
    print(f"Verification coverage: verified={verified}, partially_verified={partial}, indexed={len(records) - verified - partial}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
