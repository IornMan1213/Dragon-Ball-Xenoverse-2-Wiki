#!/usr/bin/env python3
"""Validate canonical local catalog consumer contracts."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PAGE=ROOT/"docs/Parallel-Quests-All.html"
SKILL_PAGE=ROOT/"docs/Skills-All.html"
AWOKEN_PAGE=ROOT/"docs/Awoken-All.html"
LAYER=ROOT/"docs/data/parallel-quests-record-layer.json"
SEARCH=ROOT/"docs/assets/search.js"
REL=ROOT/"docs/data/pq-reward-relationships.json"

def main():
    html=PAGE.read_text(encoding="utf-8")
    skill_html=SKILL_PAGE.read_text(encoding="utf-8")
    awoken_html=AWOKEN_PAGE.read_text(encoding="utf-8")
    records=json.loads(LAYER.read_text(encoding="utf-8")).get("records",[])
    search=SEARCH.read_text(encoding="utf-8")
    relationships=json.loads(REL.read_text(encoding="utf-8")).get("verified_relationships",[])
    ids={r.get("id") for r in records}
    nums={r.get("number") for r in records}
    relationship_fields={
      "pq_rewards_skill":"skill_rewards",
      "pq_rewards_super_soul":"super_soul_rewards",
      "pq_rewards_equipment":"equipment_rewards",
    }
    canonical_pairs={rel:{(e.get("pq"),e.get("target")) for e in relationships if e.get("relationship")==rel} for rel in relationship_fields}
    record_pairs={rel:{(r.get("id"),target) for r in records for target in (r.get(field) or [])} for rel,field in relationship_fields.items()}
    checks={
      "pq_local_record_layer_reference": '"/data/parallel-quests-record-layer.json"' in html,
      "pq_external_corpus_removed": "api.github.com/repos/Madreag" not in html and "raw.githubusercontent.com/Madreag" not in html,
      "pq_search_query_links_present": '"/Search/"' in html and "encodeURIComponent(term)" in html,
      "search_js_query_parameter_support": "URLSearchParams(window.location.search)" in search and "params.get('q')" in search,
      "canonical_pq_record_count_nonzero": bool(records),
      "unique_pq_ids": len(ids)==len(records),
      "unique_pq_numbers": len(nums)==len(records),
      "pq_skill_crosslinks_use_search": "skill_rewards" in html and "searchUrl(v)" in html,
      "canonical_skill_reward_fields_match": canonical_pairs["pq_rewards_skill"] == record_pairs["pq_rewards_skill"],
      "canonical_super_soul_reward_fields_match": canonical_pairs["pq_rewards_super_soul"] == record_pairs["pq_rewards_super_soul"],
      "canonical_equipment_reward_fields_match": canonical_pairs["pq_rewards_equipment"] == record_pairs["pq_rewards_equipment"],
      "skill_page_uses_canonical_local_db": '"/data/skills.json"' in skill_html and "api.github.com/repos/Madreag" not in skill_html and "raw.githubusercontent.com/Madreag" not in skill_html,
      "awoken_page_uses_canonical_local_db": '"/data/skills.json"' in awoken_html and "api.github.com/repos/Madreag" not in awoken_html and "raw.githubusercontent.com/Madreag" not in awoken_html,
    }
    bad=[k for k,v in checks.items() if not v]
    result={"status":"pass" if not bad else "fail","pq_record_count":len(records),"unique_pq_ids":len(ids),"unique_pq_numbers":len(nums),"canonical_reward_pairs":{k:len(v) for k,v in canonical_pairs.items()},"structured_reward_pairs":{k:len(v) for k,v in record_pairs.items()},"failed_checks":bad,"checks":checks}
    print(json.dumps(result,indent=2))
    return 0 if not bad else 1

if __name__=="__main__":
    raise SystemExit(main())
