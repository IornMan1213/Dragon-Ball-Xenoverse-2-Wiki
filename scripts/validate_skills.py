#!/usr/bin/env python3
"""Validate the canonical XV2 skills JSON and its deterministic index."""
from __future__ import annotations
import json,re
from pathlib import Path
try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    Draft202012Validator = None
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'docs/data/skills.json'; INDEX=ROOT/'docs/data/skills-index.json'; SCHEMA=ROOT/'docs/data/skills.schema.json'
ALLOWED_CLASS={'Super','Ultimate','Evasive','Awoken','Counter','Mixed'}
ALLOWED_SUB={'Ki Blast','Strike','Power Up','Other','Race','Special','Counter','Transformation'}
ALLOWED_RESEARCH={'indexed','partially_enriched','enriched','page_unavailable'}
ALLOWED_ACQUISITION={'quest_or_mission','parallel_quest','skill_shop','tp_medal_shop','character_only','starting_move','other_nonquest'}
CLASS_SUBCATEGORIES={'Super':{'Ki Blast','Strike','Other','Power Up'},'Ultimate':{'Ki Blast','Strike','Other','Power Up'},'Evasive':{'Ki Blast','Strike','Other','Power Up'},'Awoken':{'Race','Transformation'},'Counter':{'Counter'},'Mixed':{'Special'}}

def key(r): return (str(r.get('name','')).casefold(),r.get('class',''),r.get('subcategory',''))

def main():
 d=json.loads(DATA.read_text(encoding='utf-8')); idx=json.loads(INDEX.read_text(encoding='utf-8')); schema=json.loads(SCHEMA.read_text(encoding='utf-8'))
 rs=d.get('records',[]); ir=idx.get('records',[]); errors=[]
 if Draft202012Validator is None:
  errors.append('jsonschema dependency is required for JSON Schema validation')
 else:
  try:
   Draft202012Validator.check_schema(schema)
   validator=Draft202012Validator(schema, format_checker=FormatChecker())
   for i,r in enumerate(rs):
    for e in validator.iter_errors(r):
     errors.append(f"schema error at records[{i}] {e.json_path}: {e.message}")
  except Exception as e:
   errors.append(f'JSON Schema validation error: {e}')
 if d.get('record_count')!=len(rs):errors.append('skills.json record_count mismatch')
 if d.get('schema_version')!=idx.get('schema_version'):errors.append('skills/index schema_version mismatch')
 if d.get('generated')!=idx.get('generated'):errors.append('skills/index generated date mismatch')
 if d.get('source_index')!=idx.get('source_index'):errors.append('skills/index source_index mismatch')
 if idx.get('record_count')!=len(ir):errors.append('skills-index.json record_count mismatch')
 if len(rs)!=len(ir):errors.append('skills/index record lengths differ')
 keys=[key(r) for r in rs]
 if len(keys)!=len(set(keys)):errors.append('duplicate canonical skill keys')
 for r in rs:
  if r.get('class') not in ALLOWED_CLASS:errors.append(f"{r.get('name')}: invalid class {r.get('class')}")
  if r.get('subcategory') not in ALLOWED_SUB:errors.append(f"{r.get('name')}: invalid subcategory {r.get('subcategory')}")
  if r.get('class') in CLASS_SUBCATEGORIES and r.get('subcategory') not in CLASS_SUBCATEGORIES[r.get('class')]:errors.append(f"{r.get('name')}: subcategory {r.get('subcategory')} is invalid for class {r.get('class')}")
  if r.get('race_restriction')=='Character-only' and r.get('usable_by_cac') is not False:errors.append(f"{r.get('name')}: Character-only restriction requires usable_by_cac=false")

  if r.get('acquisition_type')=='character_only' and r.get('usable_by_cac') is not False:errors.append(f"{r.get('name')}: character_only acquisition requires usable_by_cac=false")
  if r.get('acquisition_type')=='starting_move' and r.get('usable_by_cac') is not True:errors.append(f"{r.get('name')}: starting_move acquisition requires usable_by_cac=true")
  if r.get('class')=='Awoken' and r.get('subcategory')=='Race' and (r.get('usable_by_cac') is not True or not r.get('race_restriction')):errors.append(f"{r.get('name')}: canonical Awoken Race record requires CaC eligibility and race restriction")
  if r.get('research_status') not in ALLOWED_RESEARCH:errors.append(f"{r.get('name')}: invalid research_status {r.get('research_status')}")
  if r.get('acquisition_type') not in ALLOWED_ACQUISITION:errors.append(f"{r.get('name')}: invalid acquisition_type {r.get('acquisition_type')}")
  acquisition=r.get('acquisition_type'); has_quest=r.get('source_quest') not in (None,'')
  if acquisition=='quest_or_mission' and not has_quest:errors.append(f"{r.get('name')}: quest_or_mission acquisition requires source_quest")
  if acquisition in {'tp_medal_shop','character_only','starting_move','other_nonquest'} and has_quest:errors.append(f"{r.get('name')}: {acquisition} acquisition cannot have source_quest")
  if acquisition in {'skill_shop','tp_medal_shop','character_only','starting_move','other_nonquest'} and not r.get('source_quest_or_shop'):errors.append(f"{r.get('name')}: {acquisition} acquisition requires source_quest_or_shop")
  if acquisition=='parallel_quest' and not any(str(r.get(f,'' )).casefold().find('parallel quest') >= 0 or str(r.get(f,'' )).casefold().find('pq') >= 0 for f in ('source_quest','source_quest_or_shop','unlock_method')):errors.append(f"{r.get('name')}: parallel_quest acquisition requires explicit PQ provenance")
  if acquisition=='parallel_quest' and not isinstance(r.get('source_quest'),str):errors.append(f"{r.get('name')}: parallel_quest acquisition requires textual source_quest provenance")
  if acquisition=='parallel_quest' and not re.search(r'\\bparallel quest\\s*#?\\s*\\d+\\b|\\bpq\\s*#?\\s*\\d+\\b', str(r.get('source_quest','')).casefold()):errors.append(f"{r.get('name')}: parallel_quest source_quest must identify a PQ number")
  if acquisition=='skill_shop' and ('starting move' in str(r.get('unlock_method','')).casefold() or 'starting fighting-style choice' in str(r.get('source_quest_or_shop','')).casefold()):errors.append(f"{r.get('name')}: explicit starting-choice route must not be classified as skill_shop")
  if acquisition=='tp_medal_shop' and r.get('source_quest') not in (None,'') and re.search(r'\bparallel quest\s*#?\s*\d+\b|\bpq\s*#?\s*\d+\b', str(r.get('source_quest_or_shop','')).casefold()):errors.append(f"{r.get('name')}: mixed PQ + TP Medal route must preserve quest_or_mission acquisition_type")
  if isinstance(r.get('source_quest'),int) and (r.get('source_quest') < 1 or r.get('source_quest') > 186):errors.append(f"{r.get('name')}: numeric source_quest must be a canonical PQ ID from 1 through 186")
  uf=r.get('ultimate_finish_required')
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
  for f in ('name','class','subcategory','verification_status','research_status','acquisition_type','sources'):
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
