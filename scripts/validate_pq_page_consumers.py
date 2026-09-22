#!/usr/bin/env python3
"""Validate the canonical local PQ explorer consumer contract."""
from __future__ import annotations
import json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PAGE=ROOT/"docs/Parallel-Quests-All.html"
LAYER=ROOT/"docs/data/parallel-quests-record-layer.json"
SEARCH=ROOT/"docs/assets/search.js"

def main():
    html=PAGE.read_text(encoding="utf-8")
    records=json.loads(LAYER.read_text(encoding="utf-8")).get("records",[])
    search=SEARCH.read_text(encoding="utf-8")
    ids={r.get("id") for r in records}
    nums={r.get("number") for r in records}
    checks={
      "local_record_layer_reference": '"/data/parallel-quests-record-layer.json"' in html,
      "external_quest_api_removed": "api.github.com/repos/Madreag/xenoverse_2_wiki/contents/content/parallel-quests" not in html,
      "external_quest_download_removed": "download_url" not in html,
      "search_query_links_present": '"/Search/"' in html and "encodeURIComponent(term)" in html,
      "search_js_query_parameter_support": "URLSearchParams(window.location.search)" in search and "params.get('q')" in search,
      "canonical_record_count_nonzero": bool(records),
      "unique_pq_ids": len(ids)==len(records),
      "unique_pq_numbers": len(nums)==len(records),
      "skill_crosslinks_use_search": "skill_rewards" in html and 'searchUrl(v)' in html,
    }
    bad=[k for k,v in checks.items() if not v]
    result={"status":"pass" if not bad else "fail","record_count":len(records),"unique_ids":len(ids),"unique_numbers":len(nums),"failed_checks":bad,"checks":checks}
    print(json.dumps(result,indent=2))
    return 0 if not bad else 1
if __name__=="__main__":
    raise SystemExit(main())
