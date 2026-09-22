#!/usr/bin/env python3
"""Validate Skills-All canonical reverse navigation to Parallel Quests."""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"docs/data"; HTML=ROOT/"docs/Skills-All.html"
def main():
    skills=json.loads((DATA/"skills.json").read_text(encoding="utf-8"))["records"]
    rel=json.loads((DATA/"pq-reward-relationships.json").read_text(encoding="utf-8"))["verified_relationships"]
    canonical={}
    for e in rel:
        if e.get("relationship")=="pq_rewards_skill":
            canonical.setdefault(e["target"],set()).add(int(str(e["pq"]).replace("pq-","")))
    mismatches=[]
    for r in skills:
        actual=set(map(int,r.get("source_parallel_quests",[])))
        expected=canonical.get(r["name"],set())
        if actual!=expected:
            mismatches.append({"skill":r["name"],"source_parallel_quests":sorted(actual),"canonical_graph":sorted(expected)})
    h=HTML.read_text(encoding="utf-8")
    checks={
      "pq_url_builder": "const pqUrl=" in h and 'Parallel-Quests-All/' in h,
      "pq_links_rendered": "Canonical PQs:" in h and "source_parallel_quests" in h,
      "pq_search_is_encoded": "encodeURIComponent('PQ '+v)" in h,
      "search_includes_pq_field": "s.source_parallel_quests" in h,
      "canonical_reverse_sets_match": not mismatches,
    }
    out={"schema_version":"1.0.0","scope":"Skills-All canonical PQ reverse navigation",
         "consumer":"docs/Skills-All.html","canonical_source":"docs/data/pq-reward-relationships.json",
         "skill_count":len(skills),"canonical_pq_skill_edges":sum(len(v) for v in canonical.values()),
         "reverse_set_mismatches":mismatches,"checks":checks,
         "status":"clean" if all(checks.values()) else "unresolved",
         "evidence_boundary":"Links expose only canonical PQ identity. They do not imply reward guarantees, Ultimate Finish requirements, drop rates, or other acquisition semantics."}
    print(json.dumps(out,indent=2,ensure_ascii=False)); return 0 if out["status"]=="clean" else 1
if __name__=="__main__": raise SystemExit(main())
