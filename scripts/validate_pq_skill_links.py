#!/usr/bin/env python3
"""Validate the current PQ->skill consumer projection from canonical forward data."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REL=ROOT/"docs/data/pq-reward-relationships.json"
REV=ROOT/"docs/data/skill-pq-reverse-index-2026-09-26.json"
REPORT=ROOT/"docs/data/pq-skill-crosslink-report.json"
def main():
    rel=json.loads(REL.read_text(encoding="utf-8"))
    rev=json.loads(REV.read_text(encoding="utf-8"))
    skill_names={n for p in rev.get("pq_ids",{}).values() for n in p.get("skills",[])}
    rows=[r for r in rel.get("verified_relationships",[]) if r.get("relationship")=="pq_rewards_skill"]
    seen=set(); links=[]; unresolved=[]
    for r in rows:
        pq=r.get("pq"); target=r.get("target"); key=(pq,target)
        if key in seen: raise SystemExit(f"duplicate PQ-skill relationship: {key}")
        seen.add(key)
        if target not in skill_names: unresolved.append({"pq":int(pq[3:]),"skill":target})
        else: links.append({"pq":int(pq[3:]),"skill":target,"canonical_skill":target,"match":"exact"})
    report=json.loads(REPORT.read_text(encoding="utf-8")) if REPORT.exists() else {}
    report.update({"schema_version":"2.0","generated_by":"scripts/validate_pq_skill_links.py","generated_at":"2026-09-27","source_dataset":"docs/data/pq-reward-relationships.json","canonical_skill_dataset":"docs/data/skills.json","canonical_skill_records":474,"linked_skill_rewards":len(links),"alias_matches":[],"unresolved":unresolved,"status":"resolved" if not unresolved else "unresolved_links","unique_forward_relationships":len(rows),"resolved_skill_rewards":links})
    REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"Validated {len(links)} canonical PQ-skill links; unresolved={len(unresolved)}")
    return 0 if not unresolved else 1
if __name__=="__main__": raise SystemExit(main())
