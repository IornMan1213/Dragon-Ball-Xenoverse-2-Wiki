#!/usr/bin/env python3
"""Validate the canonical character explorer's data contracts."""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"docs/data"
def load(p): return json.loads((DATA/p).read_text(encoding="utf-8"))
def main():
 c=load("characters-record-layer.json"); p=load("character-presets-record-layer.json"); b=load("characters/character-id-identity-bridge.json"); r=load("characters/pq-reverse-index.json")
 names=set(c["character_names"]); bm={x["canonical_character_name"]:x["character_id"] for x in b["records"]}
 preset_ids={x["character_id"] for x in p["records"] if x.get("character_id")}
 unresolved=sorted(preset_ids-set(x["character_id"] for x in b["records"]))
 reverse=r.get("indexes",{})
 orphan=sorted(set(reverse)-names)
 page=(ROOT/"docs/Characters-All.html").read_text(encoding="utf-8")
 checks={
  "canonical_count_matches":len(names)==c["canonical_character_record_count"],
  "all_preset_ids_bridged":not unresolved,
  "reverse_targets_canonical":not orphan,
  "explorer_loads_character_layer":"characters-record-layer.json" in page,
  "explorer_loads_preset_layer":"character-presets-record-layer.json" in page,
  "explorer_loads_identity_bridge":"character-id-identity-bridge.json" in page,
  "explorer_loads_pq_reverse_index":"pq-reverse-index.json" in page,
  "explorer_has_local_search":"Search/" in page,
  "explorer_has_pq_links":"Parallel-Quests-All/" in page,
 }
 out={"schema_version":"1.0.0","scope":"canonical character explorer consumer","canonical_characters":len(names),"preset_records":len(p["records"]),"preset_distinct_character_ids":len(preset_ids),"reverse_character_targets":len(reverse),"reverse_pq_references":sum(len(v) for v in reverse.values()),"unresolved_preset_ids":unresolved,"orphan_reverse_targets":orphan,"checks":checks,"status":"clean" if all(checks.values()) else "unresolved","evidence_boundary":"Explorer navigation exposes canonical identity, indexed preset records, and explicit PQ reverse references only; it does not infer complete unlock routes, preset loadouts, raid rotation, DLC ownership, or drop mechanics."}
 print(json.dumps(out,indent=2,ensure_ascii=False)); return 0 if out["status"]=="clean" else 1
if __name__=="__main__":raise SystemExit(main())
