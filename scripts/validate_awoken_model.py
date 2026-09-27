#!/usr/bin/env python3
"""Validate the canonical Awoken parent/stage model and promoted fields."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SKILLS=ROOT/'docs/data/skills.json'; OVERRIDES=ROOT/'docs/data/awoken-canonical-overrides.json'; ROSTER=ROOT/'docs/data/awoken-research-batches/awoken-batch-07-canonical-roster-correction.json'
STAGED={"Super Saiyan 2":"Super Saiyan","Super Saiyan 3":"Super Saiyan","Super Vegeta 2":"Super Vegeta","Kaioken x3":"Kaioken","Kaioken x20":"Kaioken"}
REQUIRED=['name','class','subcategory','race_restriction','usable_by_cac','ki_cost','unlock_method','verification_status']
def key(r): return (str(r.get('name','')).casefold(),r.get('class',''),r.get('subcategory',''))
def main():
    skills=json.loads(SKILLS.read_text(encoding='utf-8')); ov=json.loads(OVERRIDES.read_text(encoding='utf-8')); roster=json.loads(ROSTER.read_text(encoding='utf-8'))['canonical_transformation_roster']
    records={key(r):r for r in skills.get('records',[])}; errors=[]
    if len(ov.get('records',[]))!=15: errors.append(f"override layer expected 15 parent records, found {len(ov.get('records',[]))}")
    if len(roster)!=20: errors.append(f"roster expected 20 individually documented forms, found {len(roster)}")
    roster_names={str(r).casefold() if isinstance(r,str) else str(r.get('name','')).casefold() for r in roster}
    for r in ov.get('records',[]):
        k=key(r); name=r.get('name')
        if r.get('class')!='Awoken' or r.get('subcategory')!='Race': errors.append(f'{name}: canonical type must be Awoken/Race')
        if k not in records: errors.append(f'{name}: missing canonical record')
        for f in REQUIRED:
            if f not in r: errors.append(f'{name}: missing promoted field {f}')
        if r.get('ki_cost') is not None and (not isinstance(r.get('ki_cost'),int) or r.get('ki_cost')<0): errors.append(f'{name}: invalid ki_cost')
        if r.get('usable_by_cac') is not True: errors.append(f'{name}: usable_by_cac must be true')
    for stage,parent in STAGED.items():
        if stage.casefold() not in roster_names: errors.append(f'stage missing from roster: {stage}')
        if parent.casefold() not in roster_names: errors.append(f'parent missing from roster: {parent}')
    if errors:
        print('Awoken model validation failed:'); print('\n'.join(dict.fromkeys(errors))); return 1
    print('Awoken model validated: 15 canonical parents, 20 documented forms/stages, required promoted fields present.')
    return 0
if __name__=='__main__': raise SystemExit(main())
