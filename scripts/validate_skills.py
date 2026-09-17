#!/usr/bin/env python3
"""Validate the canonical XV2 skills JSON and its deterministic index."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'docs/data/skills.json'; INDEX=ROOT/'docs/data/skills-index.json'; SCHEMA=ROOT/'docs/data/skills.schema.json'
ALLOWED_CLASS={'Super','Ultimate','Evasive','Awoken','Counter','Mixed'}
ALLOWED_SUB={'Ki Blast','Strike','Power Up','Other','Race','Special','Counter'}
ALLOWED_RESEARCH={'indexed','partially_enriched','enriched','page_unavailable'}
def key(r): return (str(r.get('name','')).casefold(),r.get('class',''),r.get('subcategory',''))
def main():
 d=json.loads(DATA.read_text(encoding='utf-8')); idx=json.loads(INDEX.read_text(encoding='utf-8')); schema=json.loads(SCHEMA.read_text(encoding='utf-8'))
 rs=d.get('records',[]); ir=idx.get('records',[]); errors=[]
 if d.get('record_count')!=len(rs):errors.append('skills.json record_count mismatch')
 if idx.get('record_count')!=len(ir):errors.append('skills-index.json record_count mismatch')
 if len(rs)!=len(ir):errors.append('skills/index record lengths differ')
 keys=[key(r) for r in rs]
 if len(keys)!=len(set(keys)):errors.append('duplicate canonical skill keys')
 for r in rs:
  if r.get('class') not in ALLOWED_CLASS:errors.append(f"{r.get('name')}: invalid class {r.get('class')}")
  if r.get('subcategory') not in ALLOWED_SUB:errors.append(f"{r.get('name')}: invalid subcategory {r.get('subcategory')}")
  if r.get('research_status') not in ALLOWED_RESEARCH:errors.append(f"{r.get('name')}: invalid research_status {r.get('research_status')}")
 ikeys=[key(r) for r in ir]
 if keys!=ikeys:errors.append('skills-index.json is not in the same deterministic record order/content key sequence as skills.json')
 for a,b in zip(rs,ir):
  for f in ('name','class','subcategory','verification_status','research_status','sources'):
   if a.get(f)!=b.get(f):errors.append(f"index mismatch for {a.get('name')}: {f}")
 awoken=[r for r in rs if r.get('class')=='Awoken' and r.get('subcategory')=='Race']
 if len(awoken)!=15:errors.append(f'expected 15 canonical Awoken parent records, found {len(awoken)}')
 counts=d.get('category_counts',{}); targets=d.get('target_category_counts',{})
 if counts.get('Transformations')!=len(awoken):errors.append('Transformation count does not equal canonical Awoken parent count')
 if targets.get('Transformations')!=15:errors.append('Transformation target must be 15 canonical parent records')
 if idx.get('category_counts')!=counts:errors.append('index category_counts mismatch')
 if idx.get('target_category_counts')!=targets:errors.append('index target_category_counts mismatch')
 if errors:
  print('Skill validation failed:'); print('\n'.join(dict.fromkeys(errors))); return 1
 print(f'Validated {len(rs)} skills; index synchronized; {len(awoken)} canonical Awoken parent records.')
 return 0
if __name__=='__main__':raise SystemExit(main())
