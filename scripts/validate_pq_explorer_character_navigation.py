#!/usr/bin/env python3
"""Validate the PQ explorer's character navigation contract against canonical data."""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"docs"/"data"
HTML=ROOT/"docs"/"Parallel-Quests-All.html"
def load(p):
    return json.loads(p.read_text(encoding="utf-8"))
def main():
    rel=load(DATA/"pq-reward-relationships.json").get("verified_relationships",[])
    chars=set(load(DATA/"characters-record-layer.json").get("character_names",[]))
    pqs={f"pq-{i:03d}" for i in range(1,187)}
    edges=[e for e in rel if e.get("relationship")=="pq_features_character"]
    targets={e.get("target") for e in edges if e.get("target")}
    source_pqs={e.get("pq") for e in edges if e.get("pq")}
    missing=sorted(targets-chars)
    invalid_pq=sorted(source_pqs-pqs)
    html=HTML.read_text(encoding="utf-8")
    checks={
      "loads_canonical_pq_layer":'"/data/parallel-quests-record-layer.json"' in html,
      "loads_canonical_relationship_layer":'"/data/pq-reward-relationships.json"' in html,
      "filters_character_relationships":"pq_features_character" in html,
      "renders_character_links":"characterLinks(r.id)" in html,
      "canonical_character_targets_resolve":not missing,
      "relationship_pq_ids_in_range":not invalid_pq
    }
    out={"schema_version":"1.0.0","scope":"PQ explorer character navigation consumer",
      "canonical_sources":["docs/data/pq-reward-relationships.json","docs/data/characters-record-layer.json"],
      "consumer":"docs/Parallel-Quests-All.html",
      "results":{"character_edges":len(edges),"unique_character_targets":len(targets),
        "source_pqs":len(source_pqs),"missing_canonical_targets":missing,
        "invalid_pq_ids":invalid_pq,"checks":checks,
        "status":"clean" if all(checks.values()) else "unresolved"},
      "evidence_boundary":"This validates deterministic explorer navigation from canonical relationship edges. It does not assert that every roster appearance is a canonical relationship."}
    print(json.dumps(out,indent=2,ensure_ascii=False))
    return 0 if out["results"]["status"]=="clean" else 1
if __name__=="__main__":raise SystemExit(main())
