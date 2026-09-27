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

def key(r):
 if not isinstance(r,dict): return None
 values=(r.get('name'),r.get('class'),r.get('subcategory'))
 if any(not isinstance(v,str) or not v.strip() for v in values): return None
 return (values[0].casefold(),values[1],values[2])

def main():
 try:
  d=json.loads(DATA.read_text(encoding='utf-8')); idx=json.loads(INDEX.read_text(encoding='utf-8')); schema=json.loads(SCHEMA.read_text(encoding='utf-8'))
 except (OSError,json.JSONDecodeError) as exc:
  print(f'Skill validation failed: invalid JSON: {exc}'); return 1
 if not all(isinstance(x,dict) for x in (d,idx,schema)):
  print('Skill validation failed: skills, index, and schema roots must be objects'); return 1
 rs=d.get('records',[]); ir=idx.get('records',[]); errors=[]
 if not isinstance(rs,list): errors.append('skills.json records must be a list'); rs=[]
 if not isinstance(ir,list): errors.append('skills-index.json records must be a list'); ir=[]
 if not isinstance(d.get('category_counts',{}),dict): errors.append('skills.json category_counts must be an object')
 if not isinstance(d.get('target_category_counts',{}),dict): errors.append('skills.json target_category_counts must be an object')
 if d.get('record_count')!=len(rs):errors.append('skills.json record_count mismatch')
 if idx.get('record_count')!=len(ir):errors.append('skills-index.json record_count mismatch')
 if len(rs)!=len(ir):errors.append('skills/index record lengths differ')
 keys=[key(r) for r in rs]
 if any(k is None for k in keys): errors.append('canonical skill name/class/subcategory must be non-empty strings')
 valid_keys=[k for k in keys if k is not None]
 if len(valid_keys)!=len(set(valid_keys)):errors.append('duplicate canonical skill keys')
 for r in rs:
  if r.get('class') not in ALLOWED_CLASS:errors.append(f"{r.get('name')}: invalid class {r.get('class')}")
  if r.get('subcategory') not in ALLOWED_SUB:errors.append(f"{r.get('name')}: invalid subcategory {r.get('subcategory')}")
  if r.get('research_status') not in ALLOWED_RESEARCH:errors.append(f"{r.get('name')}: invalid research_status {r.get('research_status')}")
  uf=r.get('ultimate_finish_required')
  if uf is False and not r.get('ultimate_finish_evidence'):
   errors.append(f"{r.get('name')}: ultimate_finish_required=false lacks explicit evidence")
  if uf not in (None,True,False):
   errors.append(f"{r.get('name')}: invalid ultimate_finish_required value")
  if r.get('usable_by_cac') is True:
   if not any(r.get(f) not in (None,'',[]) for f in ('race_restriction','character_source','unlock_method')):
    errors.append(f"{r.get('name')}: usable_by_cac=true lacks player-character evidence")
  for source in r.get('sources',[]):
   if isinstance(source,str) and ('543This' in source or source.endswith('This')):
    errors.append(f"{r.get('name')}: malformed source URL {source}")
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
