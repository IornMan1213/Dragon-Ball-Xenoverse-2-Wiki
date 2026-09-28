#!/usr/bin/env python3
"""Validate the current PQ->skill consumer projection from canonical forward data."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REL=ROOT/"docs/data/pq-reward-relationships.json"; REV=ROOT/"docs/data/skill-pq-reverse-index-2026-09-26.json"; REPORT=ROOT/"docs/data/pq-skill-crosslink-report.json"; SKILLS=ROOT/"docs/data/skills.json"
ALIASES={"Chain Destructo-disc Barrage":"Chain Destructo-Disc Barrage","Starfall":"Destruction's Concerto: Starfall","Giant Cluster":"Gigantic Cluster","III Bomber":"Ill Bomber"}
def load_object(path):
 try:
  value=json.loads(path.read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError) as exc:
  raise SystemExit(f"{path}: invalid JSON: {exc}")
 if not isinstance(value,dict):
  raise SystemExit(f"{path}: root must be an object")
 return value
def main():
 rel=load_object(REL); rev=load_object(REV); skills=load_object(SKILLS)
 skill_records=skills.get("records")
 if not isinstance(skill_records,list):
  raise SystemExit("skills.json: records must be a list")
 canonical_skill_count=len(skill_records)
 pq_ids=rev.get("pq_ids",{})
 if not isinstance(pq_ids,dict):
  raise SystemExit("skill reverse index pq_ids must be an object")
 names=set()
 for pq, payload in pq_ids.items():
  if not isinstance(payload,dict):
   raise SystemExit(f"skill reverse index entry {pq!r} must be an object")
  skills=payload.get("skills",[])
  if not isinstance(skills,list) or any(not isinstance(n,str) or not n.strip() for n in skills):
   raise SystemExit(f"skill reverse index entry {pq!r} skills must be a list of non-empty strings")
  names.update(skills)
 relationships=rel.get("verified_relationships")
 if not isinstance(relationships,list):
  raise SystemExit("pq-reward-relationships.json: verified_relationships must be a list")
 rows=[]
 for i,r in enumerate(relationships):
  if not isinstance(r,dict):
   continue
  if r.get("relationship")=="pq_rewards_skill":
   rows.append(r)
 seen=set(); links=[]; unresolved=[]; aliases=[]
 for index, r in enumerate(rows):
  if not isinstance(r, dict):
   raise SystemExit(f"malformed PQ-skill relationship row {index}: expected object")
  pq=r.get("pq"); target=r.get("target")
  if not isinstance(pq, str) or len(pq)!=6 or not pq.startswith("pq-") or not pq[3:].isdigit() or not 1 <= int(pq[3:]) <= 186:
   raise SystemExit(f"malformed PQ-skill relationship row {index}: pq must be pq-001 through pq-186")
  if not isinstance(target, str) or not target.strip():
   raise SystemExit(f"malformed PQ-skill relationship row {index}: target must be a non-empty string")
  key=(pq,target)
  if key in seen: raise SystemExit(f"duplicate PQ-skill relationship: {key}")
  seen.add(key); canonical=ALIASES.get(target,target)
  if canonical not in names: unresolved.append({"pq":int(pq[3:]),"skill":target})
  else:
   item={"pq":int(r["pq"][3:]),"skill":target,"canonical_skill":canonical,"match":"alias" if canonical!=target else "exact"}; links.append(item)
   if item["match"]=="alias": aliases.append(item)
 report=json.loads(REPORT.read_text(encoding="utf-8")) if REPORT.exists() else {}
 report.update({"schema_version":"2.0","generated_by":"scripts/validate_pq_skill_links.py","generated_at":"2026-09-28","source_dataset":"docs/data/pq-reward-relationships.json","canonical_skill_dataset":"docs/data/skills.json","canonical_skill_records":canonical_skill_count,"linked_skill_rewards":len(links),"alias_matches":aliases,"unresolved":unresolved,"status":"resolved" if not unresolved else "unresolved_links","unique_forward_relationships":len(rows),"resolved_skill_rewards":links})
 REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
 if len(links) != len(rows):
  raise SystemExit(f"PQ-skill relationship projection mismatch: {len(rows)} forward rows but {len(links)} resolved canonical links")
 print(f"Validated {len(links)} canonical PQ-skill links; aliases={len(aliases)}; unresolved={len(unresolved)}")
 return 0 if not unresolved else 1
if __name__=="__main__": raise SystemExit(main())
