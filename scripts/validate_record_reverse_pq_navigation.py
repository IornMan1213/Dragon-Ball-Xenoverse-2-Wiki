#!/usr/bin/env python3
"""Validate Super Soul and equipment/accessory reverse PQ explorer consumers."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"docs/data"
def load(p): return json.loads((DATA/p).read_text(encoding="utf-8"))
def audit(domain,record_file,html,relationship):
    records=load(record_file)["records"]; names={r["name"] for r in records}
    edges=[e for e in load("pq-reward-relationships.json")["verified_relationships"] if e.get("relationship")==relationship]
    unresolved=sorted({e.get("target") for e in edges if e.get("target") not in names})
    h=(ROOT/"docs"/html).read_text(encoding="utf-8")
    checks={"target_records_resolve":not unresolved,"relationship_loaded":"pq-reward-relationships.json" in h,"relationship_filter":relationship in h,"pq_links_rendered":"Canonical PQs:" in h,"query_navigation":"URLSearchParams(location.search).get('q')" in h}
    return {"record_count":len(records),"canonical_edges":len(edges),"unique_canonical_targets":len({e.get("target") for e in edges}),"unresolved_targets":unresolved,"checks":checks,"status":"clean" if all(checks.values()) else "unresolved"}
def main():
    out={"schema_version":"1.0.0","scope":"canonical record reverse PQ navigation","consumers":{
      "super_souls":audit("super_soul","super-souls-record-layer.json","Super-Souls-All.html","pq_rewards_super_soul"),
      "equipment":audit("equipment","equipment-accessories-record-layer.json","Equipment-All.html","pq_rewards_equipment")}}
    out["status"]="clean" if all(v["status"]=="clean" for v in out["consumers"].values()) else "unresolved"
    out["evidence_boundary"]="PQ links are canonical relationship navigation only; they do not establish reward guarantees, Ultimate Finish requirements, drop rates, or unresolved acquisition claims."
    print(json.dumps(out,indent=2,ensure_ascii=False)); return 0 if out["status"]=="clean" else 1
if __name__=="__main__": raise SystemExit(main())
