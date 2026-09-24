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

def pair_contract(relationships, records, relationship, field, pq_ids):
    canonical_rows=[
        (str(e.get("pq")), str(e.get("target")))
        for e in relationships if e.get("relationship")==relationship
    ]
    canonical_pairs=set(canonical_rows)
    record_rows=[]
    shape_errors=[]
    for r in records:
        value=r.get(field, [])
        if value is None:
            value=[]
        if not isinstance(value, list):
            shape_errors.append({"pq":r.get("id"), "field":field, "type":type(value).__name__})
            continue
        for target in value:
            record_rows.append((str(r.get("id")), str(target)))
    record_pairs=set(record_rows)
    return {
        "canonical_pairs": canonical_pairs,
        "record_pairs": record_pairs,
        "canonical_count":len(canonical_rows),
        "record_count":len(record_rows),
        "missing":sorted(canonical_pairs-record_pairs),
        "extra":sorted(record_pairs-canonical_pairs),
        "canonical_duplicates":len(canonical_rows)-len(canonical_pairs),
        "record_duplicates":len(record_rows)-len(record_pairs),
        "shape_errors":shape_errors,
        "relationship_pq_ids_invalid":sorted({pq for pq,_ in canonical_pairs if pq not in pq_ids}),
    }

def main():
    html=PAGE.read_text(encoding="utf-8")
    skill_html=SKILL_PAGE.read_text(encoding="utf-8")
    awoken_html=AWOKEN_PAGE.read_text(encoding="utf-8")
    records=json.loads(LAYER.read_text(encoding="utf-8")).get("records",[])
    search=SEARCH.read_text(encoding="utf-8")
    relationships=json.loads(REL.read_text(encoding="utf-8")).get("verified_relationships",[])
    ids=[str(r.get("id")) for r in records]
    nums=[str(r.get("number")) for r in records]
    pq_ids=set(ids)
    relationship_fields={
      "pq_rewards_skill":"skill_rewards",
      "pq_rewards_super_soul":"super_soul_rewards",
      "pq_rewards_equipment":"equipment_rewards",
      "pq_features_character":"character_links",
      "pq_requires_dlc":"dlc_link",
    }
    contracts={}
    for rel,field in relationship_fields.items():
        if field in {"skill_rewards","super_soul_rewards","equipment_rewards"}:
            contracts[rel]=pair_contract(relationships,records,rel,field,pq_ids)

    character_rows=[(e.get("pq"),e.get("target")) for e in relationships if e.get("relationship")=="pq_features_character"]
    dlc_rows=[(e.get("pq"),e.get("target")) for e in relationships if e.get("relationship")=="pq_requires_dlc"]
    character_pairs=set(character_rows)
    dlc_pairs=set(dlc_rows)
    character_pq_counts={}
    dlc_pq_counts={}
    for pq,_ in character_rows:
        character_pq_counts[pq]=character_pq_counts.get(pq,0)+1
    for pq,_ in dlc_rows:
        dlc_pq_counts[pq]=dlc_pq_counts.get(pq,0)+1
    checks={
      "pq_local_record_layer_reference": '"/data/parallel-quests-record-layer.json"' in html,
      "pq_external_corpus_removed": "api.github.com/repos/Madreag" not in html and "raw.githubusercontent.com/Madreag" not in html,
      "pq_search_query_links_present": '"/Search/"' in html and "encodeURIComponent(term)" in html,
      "search_js_query_parameter_support": "URLSearchParams(window.location.search)" in search and "params.get('q')" in search,
      "canonical_pq_record_count_nonzero": bool(records),
      "unique_pq_ids": len(set(ids))==len(records),
      "unique_pq_numbers": len(set(nums))==len(records),
      "pq_skill_crosslinks_use_skill_explorer": "skill_rewards" in html and "skillUrl(v)" in html and "rewardLinks(r.skill_rewards,'Skills',skillUrl)" in html,
      "canonical_skill_reward_fields_match": not contracts["pq_rewards_skill"]["missing"] and not contracts["pq_rewards_skill"]["extra"] and not contracts["pq_rewards_skill"]["canonical_duplicates"] and not contracts["pq_rewards_skill"]["record_duplicates"] and not contracts["pq_rewards_skill"]["shape_errors"] and not contracts["pq_rewards_skill"]["relationship_pq_ids_invalid"],
      "canonical_super_soul_reward_fields_match": not contracts["pq_rewards_super_soul"]["missing"] and not contracts["pq_rewards_super_soul"]["extra"] and not contracts["pq_rewards_super_soul"]["canonical_duplicates"] and not contracts["pq_rewards_super_soul"]["record_duplicates"] and not contracts["pq_rewards_super_soul"]["shape_errors"] and not contracts["pq_rewards_super_soul"]["relationship_pq_ids_invalid"],
      "canonical_equipment_reward_fields_match": not contracts["pq_rewards_equipment"]["missing"] and not contracts["pq_rewards_equipment"]["extra"] and not contracts["pq_rewards_equipment"]["canonical_duplicates"] and not contracts["pq_rewards_equipment"]["record_duplicates"] and not contracts["pq_rewards_equipment"]["shape_errors"] and not contracts["pq_rewards_equipment"]["relationship_pq_ids_invalid"],
      "character_relationships_are_rendered": "characterByPq" in html and "characterLinks" in html and "pq_features_character" in html,
      "dlc_relationships_are_rendered": "dlcByPq" in html and "dlcLink" in html and "pq_requires_dlc" in html,
      "all_character_relationship_pqs_exist": {p for p,_ in character_pairs} <= pq_ids,
      "all_dlc_relationship_pqs_exist": {p for p,_ in dlc_pairs} <= pq_ids,
      "character_relationship_pairs_unique": len(character_rows)==len(character_pairs),
      "dlc_relationship_pairs_unique": len(dlc_rows)==len(dlc_pairs),
      "dlc_scalar_projection_is_unambiguous": all(count==1 for count in dlc_pq_counts.values()),
      "character_projection_target_count_nonzero": bool(character_pairs),
      "dlc_projection_target_count_nonzero": bool(dlc_pairs),
      "skill_page_uses_canonical_local_db": '"/data/skills.json"' in skill_html and "api.github.com/repos/Madreag" not in skill_html and "raw.githubusercontent.com/Madreag" not in skill_html,
      "awoken_page_uses_canonical_local_db": '"/data/skills.json"' in awoken_html and "api.github.com/repos/Madreag" not in awoken_html and "raw.githubusercontent.com/Madreag" not in awoken_html,
    }
    bad=[k for k,v in checks.items() if not v]
    result={
      "status":"pass" if not bad else "fail",
      "pq_record_count":len(records),
      "unique_pq_ids":len(set(ids)),
      "unique_pq_numbers":len(set(nums)),
      "canonical_reward_pairs":{k:v["canonical_count"] for k,v in contracts.items()},
      "structured_reward_pairs":{k:v["record_count"] for k,v in contracts.items()},
      "reward_pair_contracts":{
        k:{
          "missing":len(v["missing"]),
          "extra":len(v["extra"]),
          "canonical_duplicates":v["canonical_duplicates"],
          "structured_duplicates":v["record_duplicates"],
          "shape_errors":len(v["shape_errors"]),
          "invalid_relationship_pq_ids":len(v["relationship_pq_ids_invalid"])
        } for k,v in contracts.items()
      },
      "canonical_navigation_pairs":{
        "pq_features_character":len(character_pairs),
        "pq_requires_dlc":len(dlc_pairs)
      },
      "navigation_pair_contracts":{
        "pq_features_character":{"rows":len(character_rows),"unique_pairs":len(character_pairs),"duplicate_pairs":len(character_rows)-len(character_pairs)},
        "pq_requires_dlc":{"rows":len(dlc_rows),"unique_pairs":len(dlc_pairs),"duplicate_pairs":len(dlc_rows)-len(dlc_pairs),"max_edges_per_pq":max(dlc_pq_counts.values(),default=0)}
      },
      "failed_checks":bad,
      "checks":checks
    }
    print(json.dumps(result,indent=2))
    return 0 if not bad else 1

if __name__=="__main__":
    raise SystemExit(main())
