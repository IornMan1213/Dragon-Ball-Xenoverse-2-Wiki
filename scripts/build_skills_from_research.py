#!/usr/bin/env python3
"""Build the canonical skill catalog from structured public research records.

This is intentionally conservative: it imports structured facts only, preserves
source provenance, and never promotes a record to fully verified automatically.
"""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/data/skills.json"
INDEX = ROOT / "docs/data/skills-index.json"
MD = ROOT / "docs/Skills-Auto-Database.md"
RESEARCH = Path("/tmp/xv2-research/content/skills")

TARGET_COUNTS = {
    "Ki Blast Supers": 183, "Strike Supers": 130, "Ki Blast Ultimates": 110,
    "Strike Ultimates": 30, "Other Supers": 32, "Power Up Supers": 20,
    "Ki Blast Evasives": 23, "Strike Evasives": 16, "Other Evasives": 11,
    "Power Up Evasives": 2, "Other Ultimates": 3, "Saiyan Skills": 10,
    "Majin Skills": 10, "Namekian Skills": 4, "Frieza Race Skills": 4,
    "Human Skills": 4, "Unavailable for CaC": 37, "Counter Skills": 25,
    "Transformations": 18,
}


def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def scalar(value: str):
    value = value.strip().strip('"\'')
    if re.fullmatch(r"\d+", value):
        return int(value)
    return value


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    out: dict = {}
    for line in parts[1].splitlines():
        m = re.match(r"^([A-Za-z][A-Za-z0-9_]*)\s*:\s*(.*)$", line)
        if not m:
            continue
        key, value = m.groups()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            out[key] = re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', value)
        else:
            out[key] = scalar(value)
    return out


def classify(data: dict) -> tuple[str, str]:
    cls = str(data.get("class", "")).casefold()
    element = str(data.get("element", "")).casefold().replace("_", " ").replace("-", " ")
    if cls == "super":
        primary = "Super"
        category = "Ki Blast" if "blast" in element or element == "ki" else "Strike" if "strike" in element else "Other"
    elif cls == "ultimate":
        primary = "Ultimate"
        category = "Ki Blast" if "blast" in element or element == "ki" else "Strike" if "strike" in element else "Power Up" if "power" in element else "Other"
    elif cls == "evasive":
        primary = "Evasive"
        category = "Ki Blast" if "blast" in element or element == "ki" else "Strike" if "strike" in element else "Power Up" if "power" in element else "Other"
    elif cls == "counter":
        return "Counter", "Counter"
    elif cls == "awoken":
        return "Awoken", "Race"
    else:
        primary = "Mixed"
        category = "Special"
    return primary, category


def load_existing() -> dict[tuple[str, str, str], dict]:
    try:
        data = json.loads(OUT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    out = {}
    for record in data.get("records", []):
        key = (record.get("name", "").casefold(), record.get("class", ""), record.get("subcategory", ""))
        if key[0]:
            out[key] = record
    return out


def build_record(data: dict, path: Path) -> dict | None:
    name = data.get("name")
    if not name:
        return None
    cls, sub = classify(data)
    source_url = f"https://github.com/Madreag/xenoverse_2_wiki/blob/main/content/skills/{path.name}"
    record = {
        "name": name,
        "class": cls,
        "subcategory": sub,
        "verification_status": "partially_verified",
        "research_status": "partially_enriched",
        "sources": [source_url],
    }
    if isinstance(data.get("sources"), list):
        record["sources"].extend(x for x in data["sources"] if isinstance(x, str) and x.startswith("http"))
    if data.get("kiCost") is not None:
        record["ki_cost"] = data["kiCost"]
    if data.get("element"):
        record["damage_type"] = str(data["element"]).title()
    if data.get("source"):
        record["source_quest_or_shop"] = data["source"]
        record["unlock_method"] = "See source record"
    if data.get("mentor"):
        record["character_source"] = data["mentor"]
    if isinstance(data.get("properties"), list) and data["properties"]:
        props = "; ".join(str(x) for x in data["properties"])
        record["mechanics_notes"] = props
        record["skill_description"] = props
    if data.get("summary"):
        record.setdefault("skill_description", str(data["summary"]))
    if data.get("lastVerified"):
        record["last_verified"] = str(data["lastVerified"])
    if data.get("confidence"):
        record["research_status"] = "enriched"
    return record


def md(value) -> str:
    if value in (None, ""):
        return "—"
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def main() -> int:
    if not RESEARCH.exists():
        raise SystemExit("Structured research corpus is missing.")
    existing = load_existing()
    merged = dict(existing)
    imported = 0
    for path in sorted(RESEARCH.glob("*.md")):
        try:
            data = parse_frontmatter(path)
            record = build_record(data, path)
        except Exception:
            record = None
        if not record:
            continue
        key = (record["name"].casefold(), record["class"], record["subcategory"])
        old = merged.get(key, {})
        merged_record = dict(record)
        for k, v in old.items():
            if v not in (None, "", [], "—"):
                merged_record[k] = v
        merged_record["sources"] = list(dict.fromkeys(old.get("sources", []) + record.get("sources", [])))
        if old.get("verification_status") == "verified":
            merged_record["verification_status"] = "verified"
        merged[key] = merged_record
        imported += 1

    rows = sorted(merged.values(), key=lambda r: (r["name"].casefold(), r["class"], r["subcategory"]))
    payload = {
        "schema_version": "1.2",
        "game": "Dragon Ball Xenoverse 2",
        "source_index": "https://dbxv2.fandom.com/wiki/Category:Skills",
        "generated": date.today().isoformat(),
        "status": "structured_research_catalog",
        "target_category_counts": TARGET_COUNTS,
        "record_count": len(rows),
        "records": rows,
        "notes": "Structured secondary research is used as a cross-reference. Records remain partially verified until independently curated against primary game/wiki sources.",
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    INDEX.write_text(json.dumps({
        "schema_version": "1.2", "source_index": payload["source_index"], "generated": payload["generated"],
        "target_category_counts": TARGET_COUNTS, "record_count": len(rows),
        "records": [{k: r[k] for k in ("name", "class", "subcategory", "verification_status", "research_status", "sources")} for r in rows],
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    verified = sum(r["verification_status"] == "verified" for r in rows)
    partial = sum(r["verification_status"] == "partially_verified" for r in rows)
    lines = [
        "# Skills — Exhaustive Research Database", "",
        f"> Generated {payload['generated']}. Imported {imported} structured individual skill records and retained existing curated records.",
        f"> **Current records:** {len(rows)} · **Verified:** {verified} · **Partially verified:** {partial}",
        f"> **Coverage target:** {sum(TARGET_COUNTS.values())} indexed skill-category memberships.",
        "",
        "| Skill | Class | Subcategory | Effect / properties | How to get it | Source | Ki | Status |",
        "|---|---|---|---|---|---|---:|---|",
    ]
    for r in rows:
        lines.append("| " + " | ".join(md(r.get(k)) for k in ("name", "class", "subcategory", "skill_description", "unlock_method", "source_quest_or_shop", "ki_cost", "verification_status")) + " |")
    lines += ["", "## Verification policy", "", "Structured research is a discovery and cross-reference layer. It does not automatically promote records to fully verified status. Missing fields are intentionally left blank.", ""]
    MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Imported {imported}; total records={len(rows)}; partial={partial}; verified={verified}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
