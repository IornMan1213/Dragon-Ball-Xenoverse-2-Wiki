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

def check_reverse(report, id_key, canonical, label):
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
    require(not missing, f"{label}: missing canonical IDs: {missing}")
    require(not mismatches, f"{label}: canonical name mismatches: {mismatches}")
    require(not unresolved, f"{label}: unresolved routes remain: {unresolved}")
    return {"reverse_records": len(reverse), "missing_ids": missing, "name_mismatches": mismatches}

def main():
    skills = {x["id"]: x["name"] for x in records(load("docs/data/skills.json"))}
    souls = {x["id"]: x["name"] for x in records(load("docs/data/super-souls-record-layer.json"))}
    equipment = {x["id"]: x["name"] for x in records(load("docs/data/equipment-accessories-record-layer.json"))}
    dlc = {x["id"]: x["name"] for x in records(load("docs/data/dlc/canonical-dlc-identity.json"))}

    results = {
        "skills": check_reverse(load("docs/data/pq-skill-crosslink-report.json"), "skill_id", skills, "skills"),
        "super_souls": check_reverse(load("docs/data/pq-super-soul-crosslink-report.json"), "super_soul_id", souls, "super_souls"),
        "equipment": check_reverse(load("docs/data/pq-equipment-crosslink-report.json"), "target_id", equipment, "equipment"),
        "accessories": check_reverse(load("docs/data/pq-accessory-crosslink-report.json"), "target_id", equipment, "accessories"),
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
        "schema_version": "1.0.0",
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
