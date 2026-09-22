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
    canonical_pairs = {
        (int(str(r["pq"]).replace("pq-", "")), str(r["target"]))
        for r in canonical.get("verified_relationships", [])
        if r.get("relationship") == "pq_rewards_super_soul"
        and 41 <= int(str(r["pq"]).replace("pq-", "")) <= 186
    }
    index_pairs = {
        (int(record["pq"]), str(name))
        for record in index.get("records", [])
        if 41 <= int(record["pq"]) <= 186
        for name in record.get("super_souls", [])
    }
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
    result = {
        "status": "pass",
        "scope": "PQ41-186",
        "canonical_pairs": len(canonical_pairs),
        "index_pairs": len(index_pairs),
        "exact_pair_overlap": len(canonical_pairs & index_pairs),
        "canonical_missing_from_index": len(missing),
        "index_only_pairs": len(extra),
        "case_variant_pairs": case_variants,
        "exact_missing_pairs": exact_missing,
        "semantics": "informational_reconciliation_only",
        "rule": "Do not rewrite canonical relationships or promote research-only acquisition pairs from this partial projection without independent source evidence.",
    }
    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
