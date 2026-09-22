#!/usr/bin/env python3
"""Validate PQ cross-domain presentation/reverse indexes against canonical identities."""

from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def records(data):
    if isinstance(data, list):
        return data
    for key in ("skills", "records", "super_souls", "equipment", "identities"):
        value = data.get(key)
        if isinstance(value, list):
            return value
    return []

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def canonical_name_pairs(relationships, relationship_name):
    return {
        (str(e.get("target")), str(e.get("pq")))
        for e in relationships
        if e.get("relationship") == relationship_name
    }

def report_name_pairs(report, name_key):
    return {
        (str(edge.get(name_key)), str(edge.get("pq_id")))
        for edge in report.get("forward_edges", report.get("matched_forward_edges", []))
    }

def check_reverse(report, id_key, canonical, label, canonical_pairs=None, name_key="target_name"):

    reverse = report.get("reverse_edges", [])
    missing = [x.get(id_key) for x in reverse if x.get(id_key) not in canonical]
    mismatches = [
        {
            "id": x.get(id_key),
            "report_name": x.get("target_name", x.get("skill")),
            "canonical_name": canonical.get(x.get(id_key)),
        }
        for x in reverse
        if x.get(id_key) in canonical
        and x.get("target_name", x.get("skill")) != canonical.get(x.get(id_key))
    ]
    unresolved = report.get("unresolved_target_routes", report.get("unresolved_forward_edges", []))
    pair_missing = sorted((canonical_pairs or set()) - report_name_pairs(report, name_key))
    pair_extra = sorted(report_name_pairs(report, name_key) - (canonical_pairs or set()))
    pair_list = list(report.get("forward_edges", report.get("matched_forward_edges", [])))
    pair_keys = [(str(x.get(name_key)), str(x.get("pq_id"))) for x in pair_list]
    require(not missing, f"{label}: missing canonical IDs: {missing}")
    require(not mismatches, f"{label}: canonical name mismatches: {mismatches}")
    require(not unresolved, f"{label}: unresolved routes remain: {unresolved}")
    require(not pair_missing, f"{label}: missing canonical pairs: {pair_missing}")
    require(not pair_extra, f"{label}: extra report pairs: {pair_extra}")
    require(len(pair_keys) == len(set(pair_keys)), f"{label}: duplicate forward pairs: {pair_keys}")
    return {
        "reverse_records": len(reverse),
        "missing_ids": missing,
        "name_mismatches": mismatches,
        "canonical_pair_count": len(canonical_pairs or set()),
        "report_pair_count": len(report_name_pairs(report, name_key)),
        "missing_pairs": pair_missing,
        "extra_pairs": pair_extra,
        "duplicate_forward_pairs": len(pair_keys) - len(set(pair_keys)),
    }

def main():
    skills = {x["id"]: x["name"] for x in records(load("docs/data/skills.json"))}
    souls = {x["id"]: x["name"] for x in records(load("docs/data/super-souls-record-layer.json"))}
    equipment = {x["id"]: x["name"] for x in records(load("docs/data/equipment-accessories-record-layer.json"))}
    dlc = {x["id"]: x["name"] for x in records(load("docs/data/dlc/canonical-dlc-identity.json"))}
    relationships = load("docs/data/pq-reward-relationships.json").get("verified_relationships", [])
    skill_pairs = canonical_name_pairs(relationships, "pq_rewards_skill")
    soul_pairs = canonical_name_pairs(relationships, "pq_rewards_super_soul")
    equipment_pairs = canonical_name_pairs(relationships, "pq_rewards_equipment")
    accessory_names = {x["name"] for x in records(load("docs/data/equipment-accessories-record-layer.json")) if str(x.get("id","")).startswith("acc-")}
    accessory_pairs = {pair for pair in equipment_pairs if pair[0] in accessory_names}

    results = {
        "skills": check_reverse(load("docs/data/pq-skill-crosslink-report.json"), "skill_id", skills, "skills", skill_pairs, "skill"),
        "super_souls": check_reverse(load("docs/data/pq-super-soul-crosslink-report.json"), "super_soul_id", souls, "super_souls", soul_pairs, "target_name"),
        "equipment": check_reverse(load("docs/data/pq-equipment-crosslink-report.json"), "target_id", equipment, "equipment", equipment_pairs, "target_name"),
        "accessories": check_reverse(load("docs/data/pq-accessory-crosslink-report.json"), "target_id", equipment, "accessories", accessory_pairs, "target_name"),
    }

    bridge = load("docs/data/pq-endpoint-alias-granularity-map.json")
    bridge_results = {}
    for domain, target_map in (("equipment", equipment), ("dlc", dlc)):
        failures = []
        for row in bridge.get(domain, []):
            for target in row.get("canonical_targets", []):
                if target not in target_map.values():
                    failures.append({"source_label": row.get("source_label"), "target": target})
        bridge_results[domain] = {"records": len(bridge.get(domain, [])), "unresolved_targets": failures}
        require(not failures, f"{domain}: unresolved alias/granularity targets: {failures}")

    projection = load("docs/data/relationships/dlc-content-links.json")
    projection_failures = [
        target
        for row in projection.get("relationships", [])
        for target in row.get("canonical_dlc_ids", [])
        if target not in dlc
    ]
    require(not projection_failures, f"DLC projection unresolved canonical IDs: {projection_failures}")

    output = {
        "schema_version": "1.1.0",
        "scope": "PQ cross-domain presentation/reverse-index identity parity",
        "canonical_sources": {
            "pq_relationships": "docs/data/pq-reward-relationships.json",
            "skills": "docs/data/skills.json",
            "super_souls": "docs/data/super-souls-record-layer.json",
            "equipment_accessories": "docs/data/equipment-accessories-record-layer.json",
            "dlc": "docs/data/dlc/canonical-dlc-identity.json",
        },
        "results": results,
        "alias_granularity_bridge": bridge_results,
        "dlc_content_projection": {
            "records": len(projection.get("relationships", [])),
            "unresolved_canonical_ids": projection_failures,
        },
        "status": "resolved",
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
