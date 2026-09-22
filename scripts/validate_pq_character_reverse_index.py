#!/usr/bin/env python3
"""Validate the canonical PQ -> character reverse navigation projection.

Canonical relationship data is authoritative. This validator checks exact character
name resolution and reverse PQ-set parity; aliases are presentation metadata only.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "data"
REL = DATA / "pq-reward-relationships.json"
CHARS = DATA / "characters-record-layer.json"
REVERSE = DATA / "characters" / "pq-reverse-index.json"

def load(path: Path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)

def main() -> int:
    relationships = load(REL).get("verified_relationships", [])
    edges = [e for e in relationships if e.get("relationship") == "pq_features_character"]
    canonical = set(load(CHARS).get("character_names", []))
    reverse = load(REVERSE)
    indexes = reverse.get("indexes", {})

    forward = {(e.get("target"), e.get("pq")) for e in edges}
    reverse_pairs = {(name, f"pq-{int(pq):03d}") for name, pqs in indexes.items() for pq in pqs}
    targets = {e.get("target") for e in edges if e.get("target")}
    missing = sorted(targets - canonical)
    orphan = sorted(set(indexes) - canonical)
    missing_reverse = sorted(forward - reverse_pairs)
    extra_reverse = sorted(reverse_pairs - forward)
    duplicate_forward = len(edges) - len(forward)

    result = {
        "schema_version": "1.0.0",
        "source_of_truth": str(REL.relative_to(ROOT)),
        "canonical_identity_layer": str(CHARS.relative_to(ROOT)),
        "reverse_index": str(REVERSE.relative_to(ROOT)),
        "forward_edges": len(edges),
        "unique_character_targets": len(targets),
        "reverse_targets": len(indexes),
        "reverse_entries": sum(len(v) for v in indexes.values()),
        "missing_canonical_targets": missing,
        "orphan_reverse_targets": orphan,
        "missing_reverse_pairs": missing_reverse,
        "extra_reverse_pairs": extra_reverse,
        "duplicate_forward_pairs": duplicate_forward,
        "status": "pass" if not (missing or orphan or missing_reverse or extra_reverse or duplicate_forward) else "fail",
        "rules": [
            "Canonical relationship data is authoritative.",
            "Exact canonical character names are required for direct navigation.",
            "Aliases are presentation/source metadata only and never create canonical identities.",
            "Generic enemy appearance and inferred roster presence are excluded."
        ]
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] == "pass" else 1

if __name__ == "__main__":
    raise SystemExit(main())
