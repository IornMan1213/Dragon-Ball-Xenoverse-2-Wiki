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
    name_counts = {}
    malformed_structured_fields = []
    for r in records:
        name = r.get("name")
        name_counts[name] = name_counts.get(name, 0) + 1
        value = r.get(structured_field)
        if value is not None and not isinstance(value, list):
            malformed_structured_fields.append({"id": r.get("id"), "name": name, "type": type(value).__name__})
    duplicate_record_names = sorted(name for name, count in name_counts.items() if count > 1)
    by_name = {r["name"]: r for r in records}
    all_edges = load("pq-reward-relationships.json")["verified_relationships"]
    edges = [e for e in all_edges if e.get("relationship") == relationship]
    malformed_canonical_rows = [e for e in edges if not isinstance(e.get("target"), str) or not e.get("target") or not isinstance(e.get("pq"), str) or not re.fullmatch(r"pq-\\d{3}", e.get("pq", ""))]
    invalid_canonical_pq_ids = sorted({int(e["pq"].split("-")[1]) for e in edges if isinstance(e.get("pq"), str) and re.fullmatch(r"pq-\\d{3}", e["pq"]) and not 1 <= int(e["pq"].split("-")[1]) <= 186})
    canonical = {}
    for e in edges:
        canonical.setdefault(e["target"], []).append(e["pq"])
    unresolved = sorted(set(canonical) - set(by_name))
    structured_mismatches = []
    noncanonical_structured_pq_fields = []
    source_route_conflicts = []
    source_route_subsets = []
    structured_pair_keys = set()
    structured_pair_list = []
    invalid_structured_pq_ids = []

    canonical_names = set(canonical)
    for record in records:
        name = record.get("name")
        if name not in canonical_names and record.get(structured_field):
            noncanonical_structured_pq_fields.append({
                "id": record.get("id"), "name": name,
                "structured_pqs": sorted(set(record.get(structured_field) or [])),
                "interpretation": "Preserved source/acquisition metadata; not a canonical PQ relationship target."
            })

    for record in records:
        for raw_pq in (record.get(structured_field) or []):
            tokens = pq_tokens(raw_pq)
            if isinstance(raw_pq, int) or (isinstance(raw_pq, str) and raw_pq.strip().isdigit()):
                n = int(raw_pq)
                tokens = [f"pq-{n:03d}"]
            if not tokens:
                invalid_structured_pq_ids.append({"id": record.get("id"), "name": record.get("name"), "value": raw_pq})
                continue
            for pq in tokens:
                pq_num = int(pq.split("-")[1])
                if not 1 <= pq_num <= 186:
                    invalid_structured_pq_ids.append({"id": record.get("id"), "name": record.get("name"), "value": raw_pq})
                pair = (record.get("name"), pq)
                structured_pair_keys.add(pair)
                structured_pair_list.append(pair)

    canonical_pair_list = [(e.get("target"), e.get("pq")) for e in edges]
    canonical_pair_keys = set(canonical_pair_list)
    duplicate_canonical_pairs = len(canonical_pair_list) - len(canonical_pair_keys)
    canonical_target_pairs = {(name, pq) for name, pqs in canonical.items() for pq in pqs}
    reverse_pair_missing = sorted(canonical_pair_keys - structured_pair_keys)
    reverse_pair_extra = sorted((structured_pair_keys & {(name, pq) for name in canonical_names for pq in [f"pq-{i:03d}" for i in range(1, 187)]}) - canonical_pair_keys)

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
        "unique_record_names": not duplicate_record_names,
        "structured_field_is_list": not malformed_structured_fields,
        "structured_pq_sets_match": not structured_mismatches,
        "relationship_loaded": "pq-reward-relationships.json" in h,
        "relationship_filter": relationship in h,
        "pq_links_rendered": "Canonical PQs:" in h,
        "query_navigation": "URLSearchParams(location.search).get('q')" in h,\n        "record_search_links": "searchUrl(r.name)" in h and "Open local wiki search" in h,
        "reverse_pair_parity": not reverse_pair_missing and not reverse_pair_extra,
        "structured_pq_ids_valid": not invalid_structured_pq_ids,
        "duplicate_structured_pairs": len(structured_pair_list) == len(set(structured_pair_list)),
        "canonical_domain_edge_count_matches_live_baseline": len(edges) == {"pq_rewards_super_soul":145,"pq_rewards_equipment":124}[relationship],
        "canonical_rows_well_formed": not malformed_canonical_rows,
        "canonical_pq_ids_valid": not invalid_canonical_pq_ids,
        "duplicate_canonical_pairs": duplicate_canonical_pairs == 0,
    }
    return {
        "record_count": len(records),
        "canonical_edges": len(edges),
        "unique_canonical_targets": len(canonical),
        "unresolved_targets": unresolved,
        "structured_field": structured_field,
        "structured_pq_mismatches": structured_mismatches,
        "noncanonical_structured_pq_fields": noncanonical_structured_pq_fields,
        "source_route_conflicts": source_route_conflicts,
        "source_route_subsets": source_route_subsets,
        "canonical_pair_count": len(canonical_pair_keys),
        "structured_pair_count_for_canonical_targets": len(structured_pair_keys & canonical_target_pairs),
        "reverse_pair_missing": reverse_pair_missing,
        "reverse_pair_extra": reverse_pair_extra,
        "invalid_structured_pq_ids": invalid_structured_pq_ids,
        "malformed_structured_fields": malformed_structured_fields,
        "duplicate_record_names": duplicate_record_names,
        "duplicate_canonical_pairs": duplicate_canonical_pairs,
        "malformed_canonical_rows": malformed_canonical_rows,
        "invalid_canonical_pq_ids": invalid_canonical_pq_ids,
        "duplicate_structured_pairs": len(structured_pair_list) - len(set(structured_pair_list)),
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
