#!/usr/bin/env python3
"""Reconcile the canonical PQ forward relationship store with reverse projections.

The forward relationship store is authoritative for this check. Reverse indexes
are consumers/projections; mismatches are reported, never silently repaired.
Equipment is projected through both clothing and accessories.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORWARD = ROOT / "docs/data/pq-reward-relationships.json"
REVERSE = ROOT / "docs/data/pq-reward-normalization/pq-unified-reverse-index-1-186.json"
REPORT = ROOT / "docs/data/pq-forward-reverse-reconciliation-audit-2026-09-27.json"

MAP = {
    "pq_rewards_skill": ("skills",),
    "pq_rewards_super_soul": ("super_souls",),
    "pq_rewards_equipment": ("clothing", "accessories"),
    "pq_features_character": ("characters",),
    "pq_requires_dlc": ("dlc",),
    "pq_farming_route": ("farming",),
}

def load(path: Path):
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit(f"{path}: root must be an object")
    return value

def main() -> int:
    forward = load(FORWARD)
    reverse = load(REVERSE)
    rows = forward.get("verified_relationships")
    if not isinstance(rows, list):
        raise SystemExit("forward verified_relationships must be a list")

    result = {"schema_version":"1.0","audited_at":"2026-09-27","status":"passed",
              "authoritative_side":"docs/data/pq-reward-relationships.json",
              "categories":{}, "evidence_boundary":
              "Reverse files are projections. A mismatch is diagnostic; this validator never mutates or infers reward relationships."}

    for rel, buckets in MAP.items():
        fw = {}
        for row in rows:
            if not isinstance(row, dict) or row.get("relationship") != rel:
                continue
            pq = row.get("pq")
            target = row.get("target")
            if not isinstance(pq, str) or not isinstance(target, str) or not target:
                continue
            try:
                n = int(pq.removeprefix("pq-"))
            except ValueError:
                continue
            fw.setdefault(target, set()).add(n)

        rv = {}
        for bucket in buckets:
            data = reverse.get(bucket)
            if not isinstance(data, dict):
                result["status"] = "failed"
                result["categories"].setdefault(rel, {})["missing_reverse_bucket"] = bucket
                continue
            for target, pqs in data.items():
                if not isinstance(target, str) or not isinstance(pqs, list):
                    continue
                valid = {n for n in pqs if isinstance(n, int) and not isinstance(n, bool)}
                rv.setdefault(target, set()).update(valid)

        forward_not_reverse = sorted((target, pq) for target, pqs in fw.items()
                                     for pq in pqs if pq not in rv.get(target, set()))
        reverse_not_forward = sorted((target, pq) for target, pqs in rv.items()
                                      for pq in pqs if pq not in fw.get(target, set()))
        if forward_not_reverse or reverse_not_forward:
            result["status"] = "failed"
        result["categories"][rel] = {
            "forward_rows": sum(1 for row in rows if isinstance(row, dict) and row.get("relationship") == rel),
            "forward_targets": len(fw), "reverse_targets": len(rv),
            "forward_not_reverse": forward_not_reverse,
            "reverse_not_forward": reverse_not_forward,
            "exact_projection": not forward_not_reverse and not reverse_not_forward,
        }

    REPORT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "passed" else 1

if __name__ == "__main__":
    raise SystemExit(main())
