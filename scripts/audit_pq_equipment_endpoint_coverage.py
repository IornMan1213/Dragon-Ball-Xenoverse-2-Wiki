#!/usr/bin/env python3
"""Audit canonical PQ equipment endpoint identity coverage.

The canonical relationship store is authoritative. Endpoint layers are
secondary projections; unmatched targets are enrichment gaps, never negative
reward claims.
"""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REL=ROOT/"docs/data/pq-reward-relationships.json"
LAYERS=[ROOT/"docs/data/equipment-accessories-record-layer.json",ROOT/"docs/data/equipment-record-layer.json"]
def main():
    try:
        rel=json.loads(REL.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"{REL}: invalid JSON: {exc}")
    if not isinstance(rel, dict):
        raise SystemExit("PQ reward relationship root must be an object")
    relationships=rel.get("verified_relationships")
    if not isinstance(relationships, list) or any(not isinstance(r, dict) for r in relationships):
        raise SystemExit("verified_relationships must be a list of objects")
    targets=sorted({r["target"] for r in relationships if r.get("relationship")=="pq_rewards_equipment" and isinstance(r.get("target"),str) and r["target"].strip()})
    endpoint_names=set()
    for p in LAYERS:
        try:
            j=json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise SystemExit(f"{p}: invalid JSON: {exc}")
        if not isinstance(j, dict) or not isinstance(j.get("records"), list):
            raise SystemExit(f"{p}: root must be an object with a records list")
        if any(not isinstance(r,dict) for r in j["records"]):
            raise SystemExit(f"{p}: every record must be an object")
        endpoint_names.update(r.get("name") for r in j["records"] if isinstance(r.get("name"),str) and r.get("name").strip())
    matches=sorted(set(targets)&endpoint_names)
    gaps=sorted(set(targets)-endpoint_names)
    print(json.dumps({"canonical_edges":sum(1 for r in rel.get("verified_relationships",[]) if r.get("relationship")=="pq_rewards_equipment"),"unique_targets":len(targets),"endpoint_identity_matches":len(matches),"endpoint_identity_gaps":len(gaps),"status":"canonical_projection_complete_endpoint_enrichment_incomplete" if gaps else "canonical_projection_complete_endpoint_identity_complete"},indent=2))
if __name__=="__main__": raise SystemExit(main())
