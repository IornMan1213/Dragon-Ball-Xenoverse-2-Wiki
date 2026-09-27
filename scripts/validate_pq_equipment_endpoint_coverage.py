#!/usr/bin/env python3
"""Validate canonical PQ→equipment endpoint coverage without changing data.

Canonical relationship data is authoritative. Endpoint records are secondary
identity/enrichment projections; missing endpoints are reported as gaps, not
negative acquisition claims.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REL = ROOT / "docs/data/pq-reward-relationships.json"
ACC = ROOT / "docs/data/equipment-accessories-record-layer.json"
EQ = ROOT / "docs/data/equipment-record-layer.json"
REPORT = ROOT / "docs/data/pq-equipment-endpoint-coverage-audit-2026-09-27.json"

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def records(data):
    return data.get("records", data) if isinstance(data, (dict, list)) else []

def main():
    rel = records(load(REL))
    acc = records(load(ACC))
    eq = records(load(EQ))
    forward = [r for r in rel if r.get("relationship") == "pq_rewards_equipment"]
    targets = sorted({str(r.get("target", "")).strip() for r in forward if str(r.get("target", "")).strip()})
    endpoint_names = {str(r.get("name", "")).strip() for r in acc + eq if str(r.get("name", "")).strip()}
    matches = sorted(set(targets) & endpoint_names)
    gaps = sorted(set(targets) - endpoint_names)
    report = {
        "schema_version": "1.0",
        "audit_date": "2026-09-27",
        "domain": "pq_equipment",
        "canonical_edges": len(forward),
        "unique_targets": len(targets),
        "endpoint_identity_matches": len(matches),
        "endpoint_identity_gaps": gaps,
        "endpoint_records": {
            "accessories": len(acc),
            "equipment": len(eq),
            "unique_named_endpoints": len(endpoint_names),
        },
        "status": "passed" if not gaps else "passed_with_endpoint_enrichment_gaps",
        "semantics": "Canonical PQ→equipment relationships remain authoritative. Missing endpoint identities are enrichment gaps, not negative acquisition claims.",
    }
    print(json.dumps(report, indent=2))
    if REPORT.exists():
        expected = load(REPORT)
        if expected.get("canonical_edges") != report["canonical_edges"] or expected.get("unique_targets") != report["unique_targets"]:
            raise SystemExit("coverage audit is stale relative to canonical relationship data")
        if expected.get("endpoint_identity_gaps") != report["endpoint_identity_gaps"]:
            raise SystemExit("coverage audit endpoint gap list is stale")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
