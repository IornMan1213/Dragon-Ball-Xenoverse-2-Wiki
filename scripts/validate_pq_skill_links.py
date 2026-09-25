#!/usr/bin/env python3
"""Validate bidirectional Parallel Quest <-> skill relationships using stable endpoint IDs."""
from __future__ import annotations
import json,re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PQ_LAYER=ROOT/"docs/data/parallel-quests-record-layer.json"
SKILLS=ROOT/"docs/data/skills.json"
REPORT=ROOT/"docs/data/pq-skill-crosslink-report.json"

ALIASES={
    "kamekameha":"kamehameha",
    "iii bomber":"ill bomber",
    "giant cluster":"gigantic cluster",
    "x100 big bang kamehameha":"x100 big bang kamehameha",
    "x 100 big bang kamehameha":"x 100 big bang kamehameha",
}

def norm(value:str)->str:
    return re.sub(r"\s+"," ",re.sub(r"[^a-z0-9 ]+"," ",str(value).casefold())).strip()

def pq_number(value):
    m=re.search(r"\b(?:parallel quest|pq)\s*#?\s*(\d+)\b",str(value or ""),re.I)
    return int(m.group(1)) if m else None

def main():
    pq=json.loads(PQ_LAYER.read_text(encoding="utf-8"))
    skills=json.loads(SKILLS.read_text(encoding="utf-8"))
    pq_records=pq.get("records",[])
    skill_records=skills.get("records",[])
    pq_by_number={int(r["number"]):r for r in pq_records if isinstance(r.get("number"),int)}
    skill_by_name={norm(r.get("name")):r for r in skill_records if r.get("name")}
    forward=[]; unresolved=[]; seen=set()
    for q in pq_records:
        for raw in q.get("skill_rewards",[]) or []:
            raw=str(raw).strip()
            key=(q.get("id"),norm(raw))
            if key in seen: continue
            seen.add(key)
            target=ALIASES.get(norm(raw),norm(raw))
            skill=skill_by_name.get(target)
            if skill:
                forward.append({"pq_id":q["id"],"pq_number":q.get("number"),"pq_name":q.get("name"),"skill_id":skill["id"],"skill":raw,"canonical_skill":skill["name"],"match":"alias" if target!=norm(raw) else "exact"})
            else:
                unresolved.append({"pq_id":q.get("id"),"pq_number":q.get("number"),"skill":raw,"reason":"missing_skill_endpoint"})
    reverse_map={}
    for edge in forward:
        bucket=reverse_map.setdefault(edge["skill_id"],{"skill_id":edge["skill_id"],"skill":edge["canonical_skill"],"pq_ids":[],"pq_numbers":[]})
        if edge["pq_id"] not in bucket["pq_ids"]:
            bucket["pq_ids"].append(edge["pq_id"]); bucket["pq_numbers"].append(edge["pq_number"])
    reverse=sorted(reverse_map.values(),key=lambda x:x["skill"].casefold())
    orphaned=[]
    source_audit=[]
    for skill in skill_records:
        declared=pq_number(skill.get("source_quest"))
        if declared is None: declared=pq_number(skill.get("source_quest_or_shop"))
        if declared is None: declared=pq_number(skill.get("unlock_method"))
        if declared is None: continue
        expected=pq_by_number.get(declared)
        linked=reverse_map.get(skill.get("id"))
        ok=bool(expected and linked and expected["id"] in linked["pq_ids"])
        item={"skill_id":skill.get("id"),"skill":skill.get("name"),"declared_pq_id":expected["id"] if expected else f"pq-{declared:03d}","declared_pq_number":declared,"reverse_contains_declared_pq":ok,"status":"resolved" if ok else "orphaned_reverse_source"}
        source_audit.append(item)
        if not ok: orphaned.append(item)
    # Current-state invariants: the reverse endpoint count may be lower than the
    # forward edge count because multiple PQs can legitimately point to one skill.
    # Validate the actual forward graph rather than treating reverse endpoint count
    # as a relationship count.
    forward_pair_keys={(e["pq_id"], e["skill_id"]) for e in forward}
    invalid_forward_pq_ids=[e for e in forward if e.get("pq_id") not in {r.get("id") for r in pq_records}]
    duplicate_forward_pairs=len(forward)-len(forward_pair_keys)
    current_invariants={
        "pq_record_count":len(pq_records),
        "skill_record_count":len(skill_records),
        "forward_edge_count":len(forward),
        "reverse_skill_endpoint_count":len(reverse),
        "expected_pq_record_count":186,
        "expected_skill_record_count":469,
        "expected_forward_edge_count":244,
        "duplicate_forward_pairs":duplicate_forward_pairs,
        "invalid_forward_pq_id_count":len(invalid_forward_pq_ids),
        "pq_number_range_is_1_to_186":sorted(pq_by_number)==list(range(1,187)),
        "canonical_forward_invariants_pass":(
            len(pq_records)==186 and len(skill_records)==469 and len(forward)==244
            and duplicate_forward_pairs==0 and not invalid_forward_pq_ids
            and sorted(pq_by_number)==list(range(1,187))
        ),
    }
    report={
        "schema_version":"2.0",
        "generated_by":"scripts/validate_pq_skill_links.py",
        "generated_at":"2026-09-21",
        "canonical_pq_records":len(pq_records),
        "canonical_skill_records":len(skill_records),
        "forward_edge_count":len(forward),
        "reverse_skill_endpoint_count":len(reverse),
        "unresolved_forward_edges":unresolved,
        "orphaned_reverse_sources":orphaned,
        "status":"resolved" if not unresolved and not orphaned and current_invariants["canonical_forward_invariants_pass"] else "unresolved_links",
        "current_invariants":current_invariants,
        "interpretation":"ID-based bidirectional relationship report. Forward edges come from the canonical PQ record layer; reverse endpoints are derived from those same evidence-backed edges. Canonical skill acquisition routes are separately checked against their declared PQ endpoint.",
        "forward_edges":forward,
        "reverse_edges":reverse,
        "source_route_audit":source_audit,
    }
    REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({k:report[k] for k in ("canonical_pq_records","canonical_skill_records","forward_edge_count","reverse_skill_endpoint_count","unresolved_forward_edges","orphaned_reverse_sources","status")},indent=2))
    return 1 if report["status"]!="resolved" else 0

if __name__=="__main__":
    raise SystemExit(main())
