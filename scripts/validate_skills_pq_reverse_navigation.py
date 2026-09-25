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
    canonical_pairs=set()
    for e in rel:
        if e.get("relationship")=="pq_rewards_skill":
            pq=int(str(e["pq"]).replace("pq-",""))
            canonical.setdefault(e["target"],set()).add(pq)
            canonical_pairs.add((e["target"],pq))
    mismatches=[]
    actual_pairs=set()
    duplicate_pairs=[]
    canonical_pair_list=[]
    for e in rel:
        if e.get("relationship")=="pq_rewards_skill" and e.get("target") and e.get("pq"):
            canonical_pair_list.append((e["target"], int(str(e["pq"]).replace("pq-",""))))
    duplicate_pairs = sorted({p for p in canonical_pair_list if canonical_pair_list.count(p) > 1})
    malformed_canonical_rows = [
        e for e in rel if e.get("relationship")=="pq_rewards_skill"
        and (not isinstance(e.get("pq"),str) or not isinstance(e.get("target"),str) or not e.get("pq") or not e.get("target"))
    ]
    invalid_canonical_pqs = sorted({
        int(str(e["pq"]).replace("pq-","")) for e in rel
        if e.get("relationship")=="pq_rewards_skill" and isinstance(e.get("pq"),str)
        and str(e["pq"]).replace("pq-","").isdigit()
        and not 1 <= int(str(e["pq"]).replace("pq-","")) <= 186
    })
    for r in skills:
        actual=set(map(int,r.get("source_parallel_quests",[])))
        expected=canonical.get(r["name"],set())
        for pq in actual: actual_pairs.add((r["name"],pq))
        if actual!=expected:
            mismatches.append({"skill":r["name"],"source_parallel_quests":sorted(actual),"canonical_graph":sorted(expected)})
    missing_pairs=sorted(canonical_pairs-actual_pairs)
    extra_pairs=sorted(actual_pairs-canonical_pairs)
    unresolved_targets=sorted(set(canonical)-{r["name"] for r in skills})
    h=HTML.read_text(encoding="utf-8")
    checks={
      "pq_url_builder": "const pqUrl=" in h and 'Parallel-Quests-All/' in h,
      "pq_links_rendered": "Canonical PQs:" in h and "source_parallel_quests" in h,
      "pq_search_is_encoded": "encodeURIComponent('PQ '+v)" in h,
      "search_includes_pq_field": "s.source_parallel_quests" in h,
      "canonical_skill_edge_count_is_244": len(canonical_pair_list)==244,
      "canonical_skill_pq_ids_are_1_to_186": not invalid_canonical_pqs,
      "canonical_skill_rows_are_well_formed": not malformed_canonical_rows,
      "canonical_reverse_sets_match": not mismatches,
      "exact_forward_reverse_pair_parity": not missing_pairs and not extra_pairs,
      "canonical_targets_resolve": not unresolved_targets,
      "duplicate_reverse_pairs_absent": not duplicate_pairs,
      "canonical_relationship_pairs_unique": not duplicate_pairs,
    }
    out={"schema_version":"1.0.0","scope":"Skills-All canonical PQ reverse navigation",
         "consumer":"docs/Skills-All.html","canonical_source":"docs/data/pq-reward-relationships.json",
         "skill_count":len(skills),"canonical_pq_skill_edges":sum(len(v) for v in canonical.values()),
         "reverse_set_mismatches":mismatches,"missing_reverse_pairs":missing_pairs,"extra_reverse_pairs":extra_pairs,"unresolved_canonical_targets":unresolved_targets,"duplicate_reverse_pairs":duplicate_pairs,"malformed_canonical_rows":len(malformed_canonical_rows),"invalid_canonical_pqs":invalid_canonical_pqs,"checks":checks,
         "status":"clean" if all(checks.values()) else "unresolved",
         "evidence_boundary":"Links expose only canonical PQ identity. They do not imply reward guarantees, Ultimate Finish requirements, drop rates, or other acquisition semantics."}
    print(json.dumps(out,indent=2,ensure_ascii=False)); return 0 if out["status"]=="clean" else 1
if __name__=="__main__": raise SystemExit(main())
