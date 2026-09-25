#!/usr/bin/env python3
"""Validate exact canonical reward-target parity and navigation contracts for the PQ explorer."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "data"
HTML = ROOT / "docs" / "Parallel-Quests-All.html"


def load(path: str):
    with (DATA / path).open(encoding="utf-8") as f:
        return json.load(f)


def relationship_pairs(relationships, relationship_name):
    return {
        (int(str(edge["pq"]).replace("pq-", "")), str(edge["target"]))
        for edge in relationships
        if edge.get("relationship") == relationship_name
    }


def report_pairs(report):
    return {
        (int(edge["pq_number"]), str(edge["target_name"]))
        for edge in report.get("forward_edges", [])
    }


def pair_diff(expected, actual):
    return {
        "missing": sorted(expected - actual),
        "extra": sorted(actual - expected),
    }


def main():
    rel = load("pq-reward-relationships.json")["verified_relationships"]
    reports = {
        "skills": load("pq-skill-crosslink-report.json"),
        "super_souls": load("pq-super-soul-crosslink-report.json"),
        "equipment": load("pq-equipment-crosslink-report.json"),
    }

    canonical_sets = {
        "skills": relationship_pairs(rel, "pq_rewards_skill"),
        "super_souls": relationship_pairs(rel, "pq_rewards_super_soul"),
        "equipment": relationship_pairs(rel, "pq_rewards_equipment"),
    }
    structured_sets = {
        domain: report_pairs(report)
        for domain, report in reports.items()
    }
    parity = {}
    for domain in canonical_sets:
        diff = pair_diff(canonical_sets[domain], structured_sets[domain])
        parity[domain] = {
            "canonical": len(canonical_sets[domain]),
            "structured": len(structured_sets[domain]),
            "missing": len(diff["missing"]),
            "extra": len(diff["extra"]),
            "missing_examples": diff["missing"][:10],
            "extra_examples": diff["extra"][:10],
        }

    dlc = load("dlc/canonical-dlc-identity.json")["records"]
    dlc_names = {record["name"] for record in dlc}
    dlc_ids = {record.get("id") for record in dlc if record.get("id")}
    dlc_name_to_id = {record["name"]: record.get("id") for record in dlc if record.get("name")}
    dlc_edges = [
        edge for edge in rel
        if edge.get("relationship") == "pq_requires_dlc"
    ]
    dlc_unresolved = sorted({
        str(edge.get("target"))
        for edge in dlc_edges
        if edge.get("target") not in dlc_names
    })
    dlc_pairs = [(str(edge.get("pq")), str(edge.get("target"))) for edge in dlc_edges]
    dlc_duplicate_pairs = len(dlc_pairs) - len(set(dlc_pairs))
    dlc_duplicate_names = len(dlc_names) != len(dlc)
    dlc_duplicate_ids = len(dlc_ids) != len(dlc)
    relationship_keys = [
        (str(edge.get("relationship")), str(edge.get("pq")), str(edge.get("target")))
        for edge in rel
    ]
    relationship_type_counts = {}
    for key in relationship_keys:
        relationship_type_counts[key[0]] = relationship_type_counts.get(key[0], 0) + 1
    duplicate_canonical_relationship_keys = len(relationship_keys) - len(set(relationship_keys))
    expected_relationship_counts = {
        "pq_rewards_skill": 244,
        "pq_rewards_super_soul": 145,
        "pq_rewards_equipment": 124,
        "pq_features_character": 247,
        "pq_requires_dlc": 86,
        "pq_farming_route": 7,
    }

    skills = {record["name"] for record in load("skills.json")["records"]}
    souls = {record["name"] for record in load("super-souls-record-layer.json")["records"]}
    equipment = {record["name"] for record in load("equipment-accessories-record-layer.json")["records"]}

    h = HTML.read_text(encoding="utf-8")
    skill_html = (ROOT / "docs" / "Skills-All.html").read_text(encoding="utf-8")
    unresolved = {
        "skills": sorted({
            name for _, name in structured_sets["skills"]
            if name not in skills
        }),
        "souls": sorted({
            name for _, name in structured_sets["super_souls"]
            if name not in souls
        }),
        "equipment": sorted({
            name for _, name in structured_sets["equipment"]
            if name not in equipment
        }),
        "dlc": dlc_unresolved,
    }

    checks = {
        "skill_explorer_query_support": "new URLSearchParams(location.search).get('q')" in skill_html,
        "pq_explorer_query_deep_link_support": "new URLSearchParams(window.location.search).get('q')" in h,
        "pq_dlc_navigation_uses_search_deep_link": "const dlcUrl=(term)=>'{{ \"/Search/\" | relative_url }}?q='+encodeURIComponent(term);" in h,
        "pq_skill_links_use_skill_explorer": "skillUrl" in h and "rewardLinks(r.skill_rewards,'Skills',skillUrl)" in h,
        "pq_soul_links_present": "rewardLinks(r.super_soul_rewards,'Super Souls',soulUrl)" in h,
        "pq_soul_links_use_super_soul_explorer": "const soulUrl='{{ \"/Super-Souls-All/\" | relative_url }}?q='" in h,
        "pq_equipment_links_present": "rewardLinks(r.equipment_rewards,'Equipment',equipmentUrl)" in h,
        "pq_character_links_use_character_explorer": "characterUrl" in h and "characterLinks(pqId)" in h,
        "pq_dlc_links_present": "dlcUrl" in h and "dlcByPq" in h and "pq_requires_dlc" in h,
        "pq_dlc_labels_use_canonical_identity": "canonicalDlc=dlcByPq[r.id]||''" in h,
        "equipment_explorer_dlc_search_links": "r.dlc_provenance" in (ROOT / "docs" / "Equipment-All.html").read_text(encoding="utf-8") and "Open DLC in local wiki search" in (ROOT / "docs" / "Equipment-All.html").read_text(encoding="utf-8"),
        "dlc_overview_reverse_pq_table": "## Canonical DLC → PQ Reverse Navigation" in (ROOT / "docs" / "DLC-Overview.md").read_text(encoding="utf-8"),
        "dlc_targets_resolve": not dlc_unresolved,
        "dlc_identity_names_unique": not dlc_duplicate_names,
        "dlc_identity_ids_unique": not dlc_duplicate_ids,
        "dlc_relationship_pairs_unique": dlc_duplicate_pairs == 0,
        "canonical_relationship_total_is_853": len(rel) == 853,
        "canonical_relationship_type_counts_match_live_baseline": relationship_type_counts == expected_relationship_counts,
        "canonical_relationship_keys_unique": duplicate_canonical_relationship_keys == 0,
        "dlc_identity_has_id_for_every_name": len(dlc_name_to_id) == len(dlc_names),
        "skill_targets_resolve": not unresolved["skills"],
        "soul_targets_resolve": not unresolved["souls"],
        "equipment_targets_resolve": not unresolved["equipment"],
        "skill_pair_parity": parity["skills"]["missing"] == 0 and parity["skills"]["extra"] == 0,
        "soul_pair_parity": parity["super_souls"]["missing"] == 0 and parity["super_souls"]["extra"] == 0,
        "equipment_pair_parity": parity["equipment"]["missing"] == 0 and parity["equipment"]["extra"] == 0,
        "no_duplicate_structured_skill_pairs": len(structured_sets["skills"]) == len(reports["skills"].get("forward_edges", [])),
        "no_duplicate_structured_soul_pairs": len(structured_sets["super_souls"]) == len(reports["super_souls"].get("forward_edges", [])),
        "no_duplicate_structured_equipment_pairs": len(structured_sets["equipment"]) == len(reports["equipment"].get("forward_edges", [])),
    }

    out = {
        "schema_version": "1.1.0",
        "scope": "PQ explorer reward-domain navigation",
        "canonical_sources": [
            "docs/data/pq-reward-relationships.json",
            "docs/data/dlc/canonical-dlc-identity.json",
            "docs/data/pq-skill-crosslink-report.json",
            "docs/data/pq-super-soul-crosslink-report.json",
            "docs/data/pq-equipment-crosslink-report.json",
            "docs/data/skills.json",
            "docs/data/super-souls-record-layer.json",
            "docs/data/equipment-accessories-record-layer.json",
        ],
        "consumer": "docs/Parallel-Quests-All.html",
        "counts": {
            "skills": len(canonical_sets["skills"]),
            "super_souls": len(canonical_sets["super_souls"]),
            "equipment": len(canonical_sets["equipment"]),
            "dlc_edges": len(dlc_edges),
            "dlc_unique_targets": len({edge["target"] for edge in dlc_edges}),
            "dlc_identity_records": len(dlc),
            "dlc_duplicate_pairs": dlc_duplicate_pairs,
            "relationship_type_counts": relationship_type_counts,
            "duplicate_canonical_relationship_keys": duplicate_canonical_relationship_keys,
        },
        "unresolved_canonical_targets": unresolved,
        "checks": checks,
        "structured_reward_consumer_parity": parity,
        "dlc_identity_contract": {
            "duplicate_names": dlc_duplicate_names,
            "duplicate_ids": dlc_duplicate_ids,
            "identity_name_count": len(dlc_names),
            "identity_id_count": len(dlc_ids),
            "relationship_pair_count": len(dlc_pairs),
        },
        "status": "clean" if all(checks.values()) else "unresolved",
        "evidence_boundary": (
            "Canonical PQ reward and DLC identity layers are authoritative. "
            "This validator checks exact (PQ,target) parity for the structured reward "
            "crosslink reports as well as target identity and HTML link construction. "
            "Search/landing-page URLs do not establish that a dedicated per-record page exists; "
            "acquisition semantics remain owned by the canonical relationship reports."
        ),
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0 if out["status"] == "clean" else 1


if __name__ == "__main__":
    raise SystemExit(main())
