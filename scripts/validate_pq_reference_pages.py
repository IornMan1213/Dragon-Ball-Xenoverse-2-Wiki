#!/usr/bin/env python3
"""Validate general PQ reference pages against the canonical local PQ/relationship layers."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "data"

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def main():
    page = (ROOT / "docs" / "Parallel-Quests.md").read_text(encoding="utf-8")
    audit = (ROOT / "docs" / "Parallel-Quest-Audit.md").read_text(encoding="utf-8")
    pqs = load(DATA / "parallel-quests-record-layer.json")["records"]
    rel = load(DATA / "pq-reward-relationships.json")["verified_relationships"]
    farming = sorted(
        int(e["pq"].split("-")[1])
        for e in rel if e.get("relationship") == "pq_farming_route"
    )
    canonical = len(pqs)
    edge_counts = {}
    for e in rel:
        edge_counts[e["relationship"]] = edge_counts.get(e["relationship"], 0) + 1
    expected_farming = [15, 22, 44, 45, 68, 83, 88]
    checks = {
        "canonical_pq_count_is_186": canonical == 186,
        "reference_page_declares_186_records": "**186 numbered PQ records" in page,
        "audit_declares_pq186": "through **PQ186**" in audit,
        "relationship_total_is_860": sum(edge_counts.values()) == 860,
        "skill_edge_count_is_244": edge_counts.get("pq_rewards_skill", 0) == 244,
        "super_soul_edge_count_is_151": edge_counts.get("pq_rewards_super_soul", 0) == 151,
        "equipment_edge_count_is_125": edge_counts.get("pq_rewards_equipment", 0) == 125,
        "character_edge_count_is_247": edge_counts.get("pq_features_character", 0) == 247,
        "dlc_edge_count_is_86": edge_counts.get("pq_requires_dlc", 0) == 86,
        "farming_edge_count_is_7": edge_counts.get("pq_farming_route", 0) == 7,
        "reference_page_declares_860_edges": "**860 unique edges**" in page,
        "audit_declares_860_edges": "**860 unique edges**" in audit,
        "farming_set_matches_canonical": farming == expected_farming,
        "reference_page_farming_set_matches": "15 / 22 / 44 / 45 / 68 / 83 / 88" in page,
        "stale_pq13_farming_claim_absent": "13 / 15 / 22 / 68" not in page,
        "reference_page_links_live_explorer": "Parallel-Quests-All.html" in page,
    }
    result = {
        "schema_version": "1.0.0",
        "scope": "general PQ reference/index pages",
        "sources": [
            "docs/data/parallel-quests-record-layer.json",
            "docs/data/pq-reward-relationships.json",
        ],
        "consumers": ["docs/Parallel-Quests.md", "docs/Parallel-Quest-Audit.md"],
        "canonical": {
            "pq_records": canonical,
            "relationship_edges": sum(edge_counts.values()),
            "relationship_counts": edge_counts,
            "farming_pqs": farming,
        },
        "checks": checks,
        "status": "clean" if all(checks.values()) else "unresolved",
        "evidence_boundary": "This validator checks deterministic count/set/navigation statements only. It does not promote community efficiency claims, infer missing reward mechanics, or replace source-backed PQ research.",
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] == "clean" else 1

if __name__ == "__main__":
    raise SystemExit(main())
