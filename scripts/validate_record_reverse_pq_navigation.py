#!/usr/bin/env python3
"""Validate Super Soul and equipment/accessory reverse PQ consumers and acquisition crosslinks.

Canonical PQ relationship endpoints are authoritative for structured reverse navigation.
Acquisition prose may contain documented historical/source conflicts; those are reported
as evidence conflicts rather than silently normalized into canonical relationships.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs/data"

def load(path: str):
    return json.loads((DATA / path).read_text(encoding="utf-8"))

def pq_tokens(value):
    text = value if isinstance(value, str) else " ".join(map(str, value)) if isinstance(value, list) else str(value or "")
    out = []
    for m in re.finditer(r"\b(?:Parallel Quest|PQ)[\s_-]*(\d{1,3})\b", text, re.I):
        out.append(f"pq-{int(m.group(1)):03d}")
    return sorted(set(out))

def audit(domain, record_file, html, relationship, structured_field):
    records = load(record_file)["records"]
    by_name = {r["name"]: r for r in records}
    edges = [e for e in load("pq-reward-relationships.json")["verified_relationships"]
             if e.get("relationship") == relationship]
    canonical = {}
    for e in edges:
        canonical.setdefault(e["target"], []).append(e["pq"])
    unresolved = sorted(set(canonical) - set(by_name))
    structured_mismatches = []
    source_route_conflicts = []
    source_route_subsets = []

    for name, target_pqs in sorted(canonical.items()):
        record = by_name.get(name)
        if not record:
            continue
        expected = sorted(set(target_pqs))
        actual = sorted(set(
            f"pq-{int(x):03d}" if isinstance(x, int) or str(x).isdigit() else str(x)
            for x in (record.get(structured_field) or [])
        ))
        if actual != expected:
            structured_mismatches.append({
                "id": record.get("id"), "name": name,
                "expected": expected, "actual": actual
            })

        route_text = []
        for field in ("acquisition_source", "first_clear_or_repeat", "acquisition_routes"):
            value = record.get(field)
            if value is not None:
                route_text.extend(pq_tokens(value))
        route_text = sorted(set(route_text))
        extras = [pq for pq in route_text if pq not in expected]
        if extras:
            source_route_conflicts.append({
                "id": record.get("id"), "name": name,
                "canonical_pqs": expected, "documented_pqs": route_text,
                "conflicting_pqs": extras
            })
        elif route_text and any(pq not in route_text for pq in expected):
            source_route_subsets.append({
                "id": record.get("id"), "name": name,
                "canonical_pqs": expected, "documented_pqs": route_text
            })

    h = (ROOT / "docs" / html).read_text(encoding="utf-8")
    checks = {
        "target_records_resolve": not unresolved,
        "structured_pq_sets_match": not structured_mismatches,
        "relationship_loaded": "pq-reward-relationships.json" in h,
        "relationship_filter": relationship in h,
        "pq_links_rendered": "Canonical PQs:" in h,
        "query_navigation": "URLSearchParams(location.search).get('q')" in h,
    }
    return {
        "record_count": len(records),
        "canonical_edges": len(edges),
        "unique_canonical_targets": len(canonical),
        "unresolved_targets": unresolved,
        "structured_field": structured_field,
        "structured_pq_mismatches": structured_mismatches,
        "source_route_conflicts": source_route_conflicts,
        "source_route_subsets": source_route_subsets,
        "checks": checks,
        "status": "clean" if all(checks.values()) else "unresolved",
    }

def main():
    out = {
        "schema_version": "1.1.0",
        "scope": "canonical record reverse PQ navigation and acquisition crosslink synchronization",
        "consumers": {
            "super_souls": audit(
                "super_soul", "super-souls-record-layer.json",
                "Super-Souls-All.html", "pq_rewards_super_soul",
                "source_parallel_quests"
            ),
            "equipment": audit(
                "equipment", "equipment-accessories-record-layer.json",
                "Equipment-All.html", "pq_rewards_equipment",
                "parallel_quest_ids"
            ),
        },
        "evidence_boundary": (
            "Canonical PQ links establish relationship identity only. Acquisition prose may preserve "
            "historical/source conflicts and does not establish reward guarantees, Ultimate Finish "
            "requirements, drop rates, or unresolved acquisition claims."
        ),
    }
    out["status"] = "clean" if all(v["status"] == "clean" for v in out["consumers"].values()) else "unresolved"
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0 if out["status"] == "clean" else 1

if __name__ == "__main__":
    raise SystemExit(main())
