#!/usr/bin/env python3
"""Validate the canonical Awoken parent/stage model and promoted fields."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SKILLS=ROOT/'docs/data/skills.json'
OVERRIDES=ROOT/'docs/data/awoken-canonical-overrides.json'
ROSTER=ROOT/'docs/data/awoken-research-batches/awoken-batch-07-canonical-roster-correction.json'
STAGED={"Super Saiyan 2":"Super Saiyan","Super Saiyan 3":"Super Saiyan","Super Vegeta 2":"Super Vegeta","Kaioken x3":"Kaioken","Kaioken x20":"Kaioken"}
REQUIRED=['name','class','subcategory','race_restriction','usable_by_cac','ki_cost','unlock_method','verification_status']


def key(r):
    name=r.get('name')
    cls=r.get('class')
    sub=r.get('subcategory')
    if not all(isinstance(x, str) and x.strip() for x in (name, cls, sub)):
        return None
    return (name.casefold(), cls, sub)


def require_records(payload, label):
    if not isinstance(payload, dict):
        raise SystemExit(f"{label}: root must be an object")
    records=payload.get('records')
    if not isinstance(records, list):
        raise SystemExit(f"{label}.records must be a list")
    if any(not isinstance(r, dict) for r in records):
        raise SystemExit(f"{label}.records must contain only objects")
    return records


def main():
    skills=json.loads(SKILLS.read_text(encoding='utf-8'))
    ov=json.loads(OVERRIDES.read_text(encoding='utf-8'))
    roster_payload=json.loads(ROSTER.read_text(encoding='utf-8'))
    skill_records=require_records(skills,'skills')
    override_records=require_records(ov,'overrides')
    if not isinstance(roster_payload, dict):
        raise SystemExit("roster: root must be an object")
    roster=roster_payload.get('canonical_transformation_roster')
    if not isinstance(roster, list):
        raise SystemExit("roster.canonical_transformation_roster must be a list")
    if any(not isinstance(r,(str,dict)) for r in roster):
        raise SystemExit("roster entries must be strings or objects")

    records={}
    duplicate_keys=[]
    for i,r in enumerate(skill_records):
        k=key(r)
        if k is None:
            raise SystemExit(f"skills.records[{i}] must have non-empty string name/class/subcategory")
        if k in records:
            duplicate_keys.append(k)
        records[k]=r
    if duplicate_keys:
        raise SystemExit(f"duplicate canonical skill keys: {duplicate_keys[:10]}")

    errors=[]
    if len(override_records)!=15: errors.append(f"override layer expected 15 parent records, found {len(override_records)}")
    if len(roster)!=20: errors.append(f"roster expected 20 individually documented forms, found {len(roster)}")

    roster_names=set()
    for i,r in enumerate(roster):
        name=r if isinstance(r,str) else r.get('name')
        if not isinstance(name,str) or not name.strip():
            errors.append(f'roster[{i}]: name must be a non-empty string')
            continue
        roster_names.add(name.casefold())

    for r in override_records:
        k=key(r); name=r.get('name')
        if k is None:
            errors.append(f'{name!r}: name/class/subcategory must be non-empty strings')
            continue
        if r.get('class')!='Awoken' or r.get('subcategory')!='Race': errors.append(f'{name}: canonical type must be Awoken/Race')
        if k not in records: errors.append(f'{name}: missing canonical record')
        for f in REQUIRED:
            if f not in r: errors.append(f'{name}: missing promoted field {f}')
        if r.get('ki_cost') is not None and (not isinstance(r.get('ki_cost'),int) or isinstance(r.get('ki_cost'),bool) or r.get('ki_cost')<0): errors.append(f'{name}: invalid ki_cost')
        if r.get('usable_by_cac') is not True: errors.append(f'{name}: usable_by_cac must be true')

    for stage,parent in STAGED.items():
        if stage.casefold() not in roster_names: errors.append(f'stage missing from roster: {stage}')
        if parent.casefold() not in roster_names: errors.append(f'parent missing from roster: {parent}')
    if errors:
        print('Awoken model validation failed:'); print('\n'.join(dict.fromkeys(errors))); return 1
    print('Awoken model validated: 15 canonical parents, 20 documented forms/stages, required promoted fields present.')
    return 0

if __name__=='__main__': raise SystemExit(main())
