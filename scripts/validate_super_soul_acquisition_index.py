#!/usr/bin/env python3
"""Audit the partial Super Soul PQ acquisition projection against canonical PQ relationships.

Canonical relationships remain authoritative. This validator classifies exact pair gaps and
case-only name drift without promoting either side into the other.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "docs" / "data" / "pq-reward-relationships.json"
INDEX = ROOT / "docs" / "data" / "super-souls" / "pq-acquisition-index-041-186.json"

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    canonical = load(CANONICAL)
    index = load(INDEX)
    records = index.get("records", [])
    record_pqs = [record.get("pq") for record in records]
    duplicate_record_pqs = sorted({pq for pq in record_pqs if record_pqs.count(pq) > 1})
    malformed_records = [
        record.get("pq") for record in records
        if not isinstance(record.get("pq"), int)
        or not isinstance(record.get("super_souls"), list)
    ]
    canonical_pairs = {
        (int(str(r["pq"]).replace("pq-", "")), str(r["target"]))
        for r in canonical.get("verified_relationships", [])
        if r.get("relationship") == "pq_rewards_super_soul"
        and 41 <= int(str(r["pq"]).replace("pq-", "")) <= 186
    }
    index_pair_rows = [
        (int(record["pq"]), str(name))
        for record in records
        if isinstance(record.get("pq"), int)
        and 41 <= int(record["pq"]) <= 186
        and isinstance(record.get("super_souls"), list)
        for name in record.get("super_souls", [])
    ]
    index_pairs = set(index_pair_rows)
    duplicate_pair_count = len(index_pair_rows) - len(index_pairs)
    missing = sorted(canonical_pairs - index_pairs, key=lambda x: (x[0], x[1].casefold()))
    extra = sorted(index_pairs - canonical_pairs, key=lambda x: (x[0], x[1].casefold()))
    case_variants = []
    exact_missing = []
    for pq, name in missing:
        matches = [other for other_pq, other in index_pairs if other_pq == pq and other.casefold() == name.casefold()]
        if matches:
            case_variants.append({"pq": pq, "canonical": name, "indexed": matches[0]})
        else:
            exact_missing.append({"pq": pq, "canonical": name})
    structural_failures = []
    if duplicate_record_pqs:
        structural_failures.append("duplicate_pq_records")
    if malformed_records:
        structural_failures.append("malformed_records")
    if duplicate_pair_count:
        structural_failures.append("duplicate_structured_pairs")
    result = {
        "status": "clean_audit_with_reconciliation_findings" if not structural_failures else "unresolved_structural_error",
        "scope": "PQ41-186",
        "canonical_pairs": len(canonical_pairs),
        "index_records": len(records),
        "unique_index_pq_count": len(set(record_pqs)),
        "duplicate_record_pqs": duplicate_record_pqs,
        "malformed_records": malformed_records,
        "index_pairs": len(index_pairs),
        "duplicate_structured_pair_count": duplicate_pair_count,
        "exact_pair_overlap": len(canonical_pairs & index_pairs),
        "canonical_missing_from_index": len(missing),
        "index_only_pairs": len(extra),
        "case_variant_pairs": case_variants,
        "exact_missing_pairs": exact_missing,
        "semantics": "informational_reconciliation_only",
        "rule": "Do not rewrite canonical relationships or promote research-only acquisition pairs from this partial projection without independent source evidence.",
        "structural_failures": structural_failures,
    }
    print(json.dumps(result, indent=2))
    return 1 if structural_failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
