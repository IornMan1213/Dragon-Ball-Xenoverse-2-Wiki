#!/usr/bin/env python3
"""Validate canonical target coverage and navigation contracts for the PQ explorer."""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"docs"/"data"; HTML=ROOT/"docs"/"Parallel-Quests-All.html"
def load(name):
    with (DATA/name).open(encoding="utf-8") as f:return json.load(f)
def main():
    reports={"skills":load("pq-skill-crosslink-report.json"),"souls":load("pq-super-soul-crosslink-report.json"),"equipment":load("pq-equipment-crosslink-report.json")}
    rel=load("pq-reward-relationships.json")["verified_relationships"]
    dlc=load("dlc/canonical-dlc-identity.json")["records"]
    dlc_names={r["name"] for r in dlc}
    dlc_edges=[e for e in rel if e.get("relationship")=="pq_requires_dlc"]
    dlc_unresolved=sorted({e.get("target") for e in dlc_edges if e.get("target") not in dlc_names})
    skills={r["name"] for r in load("skills.json")["records"]}
    souls={r["name"] for r in load("super-souls-record-layer.json")["records"]}
    equipment={r["name"] for r in load("equipment-accessories-record-layer.json")["records"]}
    h=HTML.read_text(encoding="utf-8")
    unresolved={
      "skills":sorted({e.get("target_name") for e in reports["skills"]["forward_edges"] if e.get("target_name") and e["target_name"] not in skills}),
      "souls":sorted({e.get("target_name") for e in reports["souls"]["forward_edges"] if e.get("target_name") and e["target_name"] not in souls}),
      "equipment":sorted({e.get("target_name") for e in reports["equipment"]["forward_edges"] if e.get("target_name") and e["target_name"] not in equipment}),
      "dlc":dlc_unresolved,
    }
    checks={
      "skill_explorer_query_support":'new URLSearchParams(location.search).get(\'q\')' in (ROOT/"docs"/"Skills-All.html").read_text(encoding="utf-8"),
      "pq_skill_links_use_skill_explorer":'skillUrl' in h and 'rewardLinks(r.skill_rewards,\'Skills\',skillUrl)' in h,
      "pq_soul_links_present":'rewardLinks(r.super_soul_rewards,\'Super Souls\',soulUrl)' in h,
      "pq_equipment_links_present":'rewardLinks(r.equipment_rewards,\'Equipment\',equipmentUrl)' in h,
      "pq_dlc_links_present":'dlcUrl' in h and 'dlcByPq' in h and 'pq_requires_dlc' in h,
      "dlc_targets_resolve":not dlc_unresolved,
      "skill_targets_resolve":not unresolved["skills"],
      "soul_targets_resolve":not unresolved["souls"],
      "equipment_targets_resolve":not unresolved["equipment"],
    }
    out={"schema_version":"1.0.0","scope":"PQ explorer reward-domain navigation",
      "canonical_sources":["docs/data/pq-reward-relationships.json","docs/data/dlc/canonical-dlc-identity.json","docs/data/pq-skill-crosslink-report.json","docs/data/pq-super-soul-crosslink-report.json","docs/data/pq-equipment-crosslink-report.json","docs/data/skills.json","docs/data/super-souls-record-layer.json","docs/data/equipment-accessories-record-layer.json"],
      "consumer":"docs/Parallel-Quests-All.html",
      "counts":{k:reports[k]["forward_edge_count"] if "forward_edge_count" in reports[k] else len(reports[k]["forward_edges"]) for k in reports},
      "unresolved_canonical_targets":unresolved,"checks":checks,
      "status":"clean" if all(checks.values()) else "unresolved",
      "evidence_boundary":"This validates canonical target identity and link construction. Search/landing-page URLs do not establish that a dedicated per-record page exists; acquisition semantics remain owned by the canonical relationship reports."}
    print(json.dumps(out,indent=2,ensure_ascii=False)); return 0 if out["status"]=="clean" else 1
if __name__=="__main__":raise SystemExit(main())
