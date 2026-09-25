#!/usr/bin/env python3
"""Validate current non-PQ skill producer coverage against the 470-skill registry."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SKILLS=ROOT/"docs/data/skills.json"
PQ=ROOT/"docs/data/pq-reward-relationships.json"
FILES=[
"docs/data/mentor-endpoints.json","docs/data/expert-mission-endpoints.json",
"docs/data/skill-shop-endpoints.json","docs/data/time-rift-story-tournament-endpoints.json",
"docs/data/tokipedia-endpoints.json","docs/data/conton-city-patrol-endpoints.json",
"docs/data/special-acquisition-endpoints.json","docs/data/character-exclusive-skill-endpoints.json",
"docs/data/starting-move-endpoints.json"]
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def main():
 skills=load(SKILLS); rows=skills.get("skills",skills if isinstance(skills,list) else [])
 ids={x["id"] for x in rows if x.get("id")}
 pq=load(PQ); pqids={x.get("skill_id") for x in pq.get("relationships",pq if isinstance(pq,list) else []) if x.get("skill_id")}
 union=set()
 per={}
 for f in FILES:
  d=load(ROOT/f); rs=d.get("endpoints",d.get("records",[]))
  found={sid for r in rs for sid in r.get("skills",([r["skill_id"]] if r.get("skill_id") else [])) if sid}
  union|=found; per[f]=len(found)
 nonpq=ids-pqids
 missing=sorted(nonpq-union); broken=sorted(union-ids)
 checks={"canonical_skill_count":len(ids)==470,"duplicate_skill_ids":len(ids)==len(rows),"all_non_pq_covered":not missing,"no_broken_endpoint_ids":not broken}
 print(json.dumps({"canonical_skill_count":len(ids),"pq_skill_targets":len(pqids),"non_pq_skills":len(nonpq),"endpoint_union":len(union),"missing_non_pq_skills":missing,"broken_endpoint_ids":broken,"endpoint_layer_unique_counts":per,"checks":checks,"status":"pass" if all(checks.values()) else "fail"},indent=2))
 return 0 if all(checks.values()) else 1
if __name__=="__main__": raise SystemExit(main())
