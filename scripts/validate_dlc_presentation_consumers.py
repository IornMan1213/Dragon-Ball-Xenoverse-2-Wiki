#!/usr/bin/env python3
"""Validate DLC presentation consumers against the canonical DLC identity layer."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"docs"/"data"
IDENTITY=DATA/"dlc"/"canonical-dlc-identity.json"
CONTENT=DATA/"relationships"/"dlc-content-links.json"
FUTURE=DATA/"future-saga-content-map.json"
OVERVIEW=ROOT/"docs"/"DLC-Overview.md"
PQ=DATA/"pq-reward-relationships.json"
DLC_REVERSE=DATA/"dlc"/"pq-reverse-index.json"
DLC_REVERSE_AUDIT=DATA/"dlc"/"pq-reverse-navigation-audit.json"

def load(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)

def main():
    identity=load(IDENTITY)
    records=identity.get("records", [])
    canonical={r.get("id"):r for r in records if r.get("id")}
    content=load(CONTENT).get("relationships", [])
    future=load(FUTURE).get("chapters", [])
    content_ids=[]
    content_unresolved=[]
    malformed_content_id_fields=[]
    content_pair_list=[]
    for rel in content:
        ids=rel.get("canonical_dlc_ids", [])
        if not isinstance(ids, list):
            malformed_content_id_fields.append({"relationship":rel.get("relationship"),"type":type(ids).__name__})
            ids=[]
        content_ids.extend(ids)
        for did in ids:
            content_pair_list.append((rel.get("relationship"), did))
            if did not in canonical:
                content_unresolved.append({"consumer":"dlc-content-links","dlc_id":did})
    future_ids=[c.get("dlc_id") for c in future if c.get("dlc_id")]
    malformed_future_dlc_fields=[{"chapter":c.get("chapter"),"type":type(c.get("dlc_id")).__name__} for c in future if c.get("dlc_id") is not None and not isinstance(c.get("dlc_id"), str)]
    future_unresolved=[did for did in future_ids if did not in canonical]
    future_duplicates=len(future_ids)!=len(set(future_ids))
    future_chapters=sorted(c.get("chapter") for c in future if c.get("chapter") is not None)
    pq=load(PQ)
    reverse=load(DLC_REVERSE)
    reverse_audit=load(DLC_REVERSE_AUDIT)
    forward_pairs={(e.get("pq"),e.get("target")) for e in pq.get("verified_relationships",[]) if e.get("relationship")=="pq_requires_dlc"}
    reverse_pair_list=[]
    malformed_reverse_pq_fields=[]
    duplicate_reverse_dlc_ids=[]
    for rec in reverse.get("records",[]):
        pq_ids=rec.get("pq_ids",[])
        if not isinstance(pq_ids,list):
            malformed_reverse_pq_fields.append({"dlc_id":rec.get("dlc_id"),"type":type(pq_ids).__name__})
            pq_ids=[]
        for pq_id in pq_ids:
            reverse_pair_list.append((pq_id,rec.get("dlc_id")))
    reverse_pairs=set(reverse_pair_list)
    reverse_dlc_ids=[rec.get("dlc_id") for rec in reverse.get("records",[]) if rec.get("dlc_id")]
    duplicate_reverse_dlc_ids=sorted(x for x in set(reverse_dlc_ids) if reverse_dlc_ids.count(x)>1)
    overview=OVERVIEW.read_text(encoding="utf-8")
    required_links=[
        "./data/dlc/canonical-dlc-identity.json",
        "./data/dlc/pq-reverse-index.json",
        "./data/dlc/pq-reverse-navigation-audit.json",
        "./data/future-saga-content-map.json",
    ]
    overview_missing=[link for link in required_links if link not in overview]
    checks={
        "canonical_dlc_identity_count_is_20":len(records)==20,
        "canonical_dlc_ids_are_unique":len(canonical)==len(records),
        "canonical_dlc_ids_unique":len(canonical)==len(records),
        "content_projection_id_fields_are_lists":not malformed_content_id_fields,
        "content_projection_pairs_unique":len(content_pair_list)==len(set(content_pair_list)),
        "content_projection_targets_resolve":not content_unresolved,
        "future_saga_chapter_ids_resolve":not future_unresolved,
        "future_saga_has_exactly_chapters_1_to_4":future_chapters==[1,2,3,4],
        "future_saga_dlc_ids_unique":not future_duplicates,
        "future_saga_dlc_fields_are_strings":not malformed_future_dlc_fields,
        "dlc_overview_links_present":not overview_missing,
        "canonical_pq_dlc_edges_are_86":len(forward_pairs)==86,
        "dlc_reverse_index_exact_pair_parity":forward_pairs==reverse_pairs,
        "dlc_reverse_pq_fields_are_lists":not malformed_reverse_pq_fields,
        "dlc_reverse_pairs_unique":len(reverse_pair_list)==len(reverse_pairs),
        "dlc_reverse_dlc_ids_unique":not duplicate_reverse_dlc_ids,
        "dlc_reverse_audit_reports_zero_forward_reverse_mismatch":reverse_audit.get("results",{}).get("forward_to_reverse_mismatches")==0,
        "all_canonical_dlc_targets_have_reverse_pq_navigation":set(canonical)<=set(reverse.get("reverse_index",{})),
    }
    failed=[k for k,v in checks.items() if not v]
    report={
        "schema_version":"1.0.0",
        "scope":"DLC presentation consumers and Future Saga content-map identity resolution",
        "canonical_identity_source":str(IDENTITY.relative_to(ROOT)),
        "consumers":[str(CONTENT.relative_to(ROOT)),str(FUTURE.relative_to(ROOT)),str(OVERVIEW.relative_to(ROOT))],
        "results":{
            "canonical_dlc_records":len(records),
            "content_projection_records":len(content),
            "content_projection_dlc_references":len(content_ids),
            "future_saga_chapters":len(future),
            "future_saga_dlc_references":len(future_ids),
            "canonical_pq_dlc_edges":len(forward_pairs),
            "dlc_reverse_pairs":len(reverse_pairs),
            "dlc_reverse_pair_missing":len(forward_pairs-reverse_pairs),
            "dlc_reverse_pair_extra":len(reverse_pairs-forward_pairs),
            "unresolved_content_projection_targets":content_unresolved,
            "unresolved_future_saga_dlc_ids":future_unresolved,
            "missing_dlc_overview_links":overview_missing,
            "malformed_content_id_fields":malformed_content_id_fields,
            "malformed_future_dlc_fields":malformed_future_dlc_fields,
            "malformed_reverse_pq_fields":malformed_reverse_pq_fields,
            "duplicate_reverse_dlc_ids":duplicate_reverse_dlc_ids,
            "checks":checks,
            "status":"clean" if not failed else "unresolved",
        },
        "evidence_boundary":"Identity resolution is deterministic. Content-domain lists describe required downstream coverage; they do not prove that every concrete content record has been populated.",
        "rules":[
            "Canonical DLC identity records remain authoritative for endpoint identity.",
            "Presentation consumers may resolve existing canonical dlc_id values but may not create new DLC identities.",
            "Future Saga bundle/grouping names never replace chapter-level canonical identities.",
            "Missing downstream content records remain unresolved rather than inferred."
        ]
    }
    print(json.dumps(report,indent=2,ensure_ascii=False))
    return 1 if failed else 0

if __name__=="__main__":
    raise SystemExit(main())
