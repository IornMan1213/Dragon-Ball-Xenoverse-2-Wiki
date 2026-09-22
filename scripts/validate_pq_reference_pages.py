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
    pq_layer_path = DATA / "parallel-quests-record-layer.json"
    rel_path = DATA / "pq-reward-relationships.json"
    pqs = load(pq_layer_path)["records"]
    rel = load(rel_path)["verified_relationships"]
    explorer = (ROOT / "docs" / "Parallel-Quests-All.html").read_text(encoding="utf-8")
    pq_numbers = sorted(int(str(record["number"])) for record in pqs)
    pq_ids = [str(record["id"]) for record in pqs]
    relationship_keys = [
        (str(e.get("relationship")), str(e.get("pq")), str(e.get("target")))
        for e in rel
    ]
    farming = sorted(
        int(e["pq"].split("-")[1])
        for e in rel if e.get("relationship") == "pq_farming_route"
    )
    canonical_pq_id_set = {str(record["id"]) for record in pqs}
    relationship_pq_ids = {str(e.get("pq")) for e in rel if e.get("pq")}
    invalid_relationship_pq_ids = sorted(relationship_pq_ids - canonical_pq_id_set)
    duplicate_pq_numbers = len(pq_numbers) - len(set(pq_numbers))
    duplicate_pq_ids = len(pq_ids) - len(set(pq_ids))
    expected_relationship_types = {
        "pq_rewards_skill",
        "pq_rewards_super_soul",
        "pq_rewards_equipment",
        "pq_features_character",
        "pq_requires_dlc",
        "pq_farming_route",
    }
    canonical = len(pqs)
    edge_counts = {}
    for e in rel:
        edge_counts[e["relationship"]] = edge_counts.get(e["relationship"], 0) + 1
    expected_farming = [15, 22, 44, 45, 68, 83, 88]
    checks = {
        "canonical_pq_count_is_186": canonical == 186,
        "canonical_pq_numbers_are_exact_1_to_186": pq_numbers == list(range(1, 187)),
        "canonical_pq_ids_are_unique": len(pq_ids) == len(set(pq_ids)),
        "canonical_relationship_types_are_known": {
            str(e.get("relationship")) for e in rel
        } <= expected_relationship_types,
        "canonical_relationship_keys_are_unique": len(relationship_keys) == len(set(relationship_keys)),
        "canonical_relationship_pq_ids_resolve": not invalid_relationship_pq_ids,
        "canonical_pq_numbers_are_unique": duplicate_pq_numbers == 0,
        "canonical_pq_ids_are_unique": duplicate_pq_ids == 0,
        "explorer_loads_canonical_pq_layer": '"/data/parallel-quests-record-layer.json"' in explorer,
        "explorer_loads_canonical_relationship_layer": '"/data/pq-reward-relationships.json"' in explorer,
        "explorer_treats_pq_records_as_array": "Array.isArray(data.records)" in explorer,
        "explorer_treats_relationships_as_array": "rel.verified_relationships||[]" in explorer,
        "explorer_has_canonical_search_surface": '"/Search/"' in explorer,
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
        "schema_version": "1.1.0",
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
            "invalid_relationship_pq_ids": invalid_relationship_pq_ids,
            "duplicate_pq_numbers": duplicate_pq_numbers,
            "duplicate_pq_ids": duplicate_pq_ids,
        },
        "checks": checks,
        "status": "clean" if all(checks.values()) else "unresolved",
        "evidence_boundary": "This validator checks deterministic count/set/navigation statements only, including the published explorer's canonical data dependencies. It does not promote community efficiency claims, infer missing reward mechanics, or replace source-backed PQ research.",
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] == "clean" else 1

if __name__ == "__main__":
    raise SystemExit(main())
