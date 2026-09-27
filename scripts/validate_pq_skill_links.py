#!/usr/bin/env python3
"""Validate the current PQ->skill consumer projection from canonical forward data."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REL=ROOT/"docs/data/pq-reward-relationships.json"; REV=ROOT/"docs/data/skill-pq-reverse-index-2026-09-26.json"; REPORT=ROOT/"docs/data/pq-skill-crosslink-report.json"
ALIASES={"Chain Destructo-disc Barrage":"Chain Destructo-Disc Barrage","Starfall":"Destruction's Concerto: Starfall","Giant Cluster":"Gigantic Cluster","III Bomber":"Ill Bomber"}
def main():
 rel=json.loads(REL.read_text(encoding="utf-8")); rev=json.loads(REV.read_text(encoding="utf-8"))
 names={n for p in rev.get("pq_ids",{}).values() for n in p.get("skills",[])}
 rows=[r for r in rel.get("verified_relationships",[]) if r.get("relationship")=="pq_rewards_skill"]; seen=set(); links=[]; unresolved=[]; aliases=[]
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
 report.update({"schema_version":"2.0","generated_by":"scripts/validate_pq_skill_links.py","generated_at":"2026-09-27","source_dataset":"docs/data/pq-reward-relationships.json","canonical_skill_dataset":"docs/data/skills.json","canonical_skill_records":474,"linked_skill_rewards":len(links),"alias_matches":aliases,"unresolved":unresolved,"status":"resolved" if not unresolved else "unresolved_links","unique_forward_relationships":len(rows),"resolved_skill_rewards":links})
 REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"); print(f"Validated {len(links)} canonical PQ-skill links; aliases={len(aliases)}; unresolved={len(unresolved)}")
 return 0 if not unresolved else 1
if __name__=="__main__": raise SystemExit(main())
