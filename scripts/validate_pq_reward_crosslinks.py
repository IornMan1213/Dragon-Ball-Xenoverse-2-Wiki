#!/usr/bin/env python3
"""Validate explicit PQ reward endpoints across skills, equipment, accessories and Super Souls."""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(path): return json.loads((ROOT/path).read_text(encoding="utf-8"))
def pq_id(n): return f"pq-{int(n):03d}"
def edges_from_records(records,source_fields=("source_quest_or_shop","acquisition_source")):
    out=[]
    for r in records:
        text="; ".join(str(r.get(k,"")) for k in source_fields)
        m=re.search(r"\b(?:parallel quest|pq)\s*#?\s*(\d+)\b",text,re.I)
        if m: out.append({"pq_id":pq_id(m.group(1)),"pq_number":int(m.group(1)),"target_id":r.get("id"),"target_name":r.get("name") or r.get("canonical_name"),"status":"source_backed"})
    return out
def reverse(edges):
    out={}
    for e in edges:
        x=out.setdefault(e["target_id"],{"target_id":e["target_id"],"target_name":e["target_name"],"pq_ids":[],"pq_numbers":[]})
        if e["pq_id"] not in x["pq_ids"]: x["pq_ids"].append(e["pq_id"]);x["pq_numbers"].append(e["pq_number"])
    return sorted(out.values(),key=lambda x:str(x["target_name"]).casefold())
def main():
    domains={}
    domains["equipment"]=load(Path("docs/data/equipment-record-layer.json"))["records"]
    domains["super_souls"]=load(Path("docs/data/super-souls-record-layer.json"))["records"]
    acc_bridge=load(Path("docs/data/accessory-pq-canonical-bridge.json"))["records"]
    acc_canon=load(Path("docs/data/accessory-canonical-reconciliation.json"))["records"]
    canon={x["id"]:x for x in acc_canon}
    acc_edges=[{"pq_id":pq_id(x["pq"]),"pq_number":x["pq"],"target_id":x["canonical_id"],"target_name":canon.get(x["canonical_id"],{}).get("canonical_name",x["name"]),"status":"identity_matched"} for x in acc_bridge if x.get("canonical_id") and x.get("pq") is not None]
    report={}
    for name,records in domains.items():
        edges=edges_from_records(records)
        report[name]={"canonical_target_records":len(records),"forward_edge_count":len(edges),"reverse_target_count":len(reverse(edges)),"unresolved_target_count":len(records)-len(edges),"forward_edges":edges,"reverse_edges":reverse(edges)}
    report["accessories"]={"canonical_identity_records":len(acc_canon),"research_records":len(acc_bridge),"forward_edge_count":len(acc_edges),"reverse_target_count":len(reverse(acc_edges)),"unresolved_research_count":len(acc_bridge)-len(acc_edges),"forward_edges":acc_edges,"reverse_edges":reverse(acc_edges)}
    print(json.dumps({k:{a:v[a] for a in ("canonical_target_records","forward_edge_count","reverse_target_count") if a in v}|{"unresolved":v.get("unresolved_target_count",v.get("unresolved_research_count"))} for k,v in report.items()},indent=2))
if __name__=="__main__": main()
