#!/usr/bin/env python3
"""Apply an explicit, identity-scoped patch to the canonical skill database.

This utility is intentionally narrow: it loads the complete local skills.json,
locates exactly one existing skill by name/id, updates only fields supplied by
the patch manifest, rebuilds the matching skills-index record, and refuses to
write if identity/count/parity checks fail.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "docs/data/skills.json"
INDEX = ROOT / "docs/data/skills-index.json"

PATCHES = {
    "skill-energy-wave-combo": {
        "name": "Energy Wave Combo",
        "fields": {
            "unlock_method": "Skill Shop / default Future Warrior Super Skill",
            "source_quest_or_shop": "Skill Shop",
            "ultimate_finish_required": None,
        },
    },
    "x20-kaioken-kamehameha": {
        "name": "X20 Kaioken Kamehameha",
        "fields": {
            "race_restriction": "All CaC races",
        },
    }
}

def load(path: Path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)

def save(path: Path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill-id", required=True, choices=sorted(PATCHES))
    ap.add_argument("--write", action="store_true", help="write changes; default is dry-run")
    args = ap.parse_args()

    data = load(SKILLS)
    index = load(INDEX)
    records = data.get("records")
    index_records = index.get("records")
    if not isinstance(records, list) or not isinstance(index_records, list):
        raise SystemExit("skills.json and skills-index.json must both contain records arrays")

    patch = PATCHES[args.skill_id]
    matches = [r for r in records if r.get("name") == patch["name"] or r.get("id") == args.skill_id]
    if len(matches) != 1:
        raise SystemExit(f"Expected exactly one canonical match; found {len(matches)}")
    record = matches[0]

    before = {k: record.get(k) for k in patch["fields"]}
    for key, value in patch["fields"].items():
        record[key] = value

    index_matches = [r for r in index_records if r.get("name") == patch["name"]]
    if len(index_matches) != 1:
        raise SystemExit(f"Expected exactly one index match; found {len(index_matches)}")

    # Index is a consumer: preserve its schema and mirror only fields it already
    # exposes; never let the index become a second source of truth.
    for key in patch["fields"]:
        if key in index_matches[0]:
            index_matches[0][key] = record[key]

    if len(records) != len(index_records):
        raise SystemExit("Canonical/index record counts differ before write")

    if not args.write:
        print(json.dumps({"skill_id": args.skill_id, "before": before,
                          "after": patch["fields"], "record_count": len(records),
                          "mode": "dry-run"}, indent=2))
        return

    save(SKILLS, data)
    save(INDEX, index)
    print(json.dumps({"skill_id": args.skill_id, "before": before,
                      "after": patch["fields"], "record_count": len(records),
                      "mode": "write"}, indent=2))

if __name__ == "__main__":
    main()
