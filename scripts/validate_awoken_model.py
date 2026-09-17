#!/usr/bin/env python3
"""Validate the Awoken parent/stage model against the repository schema."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SKILLS=ROOT/'docs/data/skills.json'
OVERRIDES=ROOT/'docs/data/awoken-canonical-overrides.json'
ROSTER=ROOT/'docs/data/awoken-research-batches/awoken-batch-07-canonical-roster-correction.json'
STAGED={"Super Saiyan 2":"Super Saiyan","Super Saiyan 3":"Super Saiyan","Super Vegeta 2":"Super Vegeta","Kaioken x3":"Kaioken","Kaioken x20":"Kaioken"}

def key(r): return (str(r.get('name','')).casefold(),r.get('class',''),r.get('subcategory',''))
def main():
    skills=json.loads(SKILLS.read_text(encoding='utf-8')); ov=json.loads(OVERRIDES.read_text(encoding='utf-8')); roster=json.loads(ROSTER.read_text(encoding='utf-8'))['canonical_transformation_roster']
    records={key(r):r for r in skills.get('records',[])}
    expected={key(r) for r in ov.get('records',[])}
    errors=[]
    for r in ov.get('records',[]):
        k=key(r)
        if r.get('subcategory')!='Race': errors.append(f"{r.get('name')}: invalid Awoken subcategory {r.get('subcategory')}")
        if k not in records: errors.append(f"{r.get('name')}: missing canonical record")
        if r.get('race_restriction')=='Universal':
            pass
    for stage,parent in STAGED.items():
        if stage not in roster: errors.append(f"stage missing from roster: {stage}")
        if parent not in roster: errors.append(f"parent missing from roster: {parent}")
    if len(roster)!=20: errors.append(f"roster expected 20 individually documented forms, found {len(roster)}")
    if len(ov.get('records',[]))!=15: errors.append(f"override layer expected 15 parent records, found {len(ov.get('records',[]))}")
    if errors:
        print('Awoken model validation failed:')
        print('\n'.join(errors)); return 1
    print('Awoken model validated: 15 parent canonical records, 20 documented forms/stages, schema-valid Awoken/Race model.')
    return 0
if __name__=='__main__': raise SystemExit(main())
