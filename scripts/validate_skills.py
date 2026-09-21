#!/usr/bin/env python3
"""Validate the canonical XV2 skills JSON and its deterministic index."""
from __future__ import annotations
import json,re
from pathlib import Path
from build_skills_from_research import CATALOG_GAME, CATALOG_SCHEMA_VERSION, CATALOG_SOURCE_INDEX, INDEX_PROJECTION_FIELDS, TARGET_COUNTS
try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    Draft202012Validator = None
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'docs/data/skills.json'; INDEX=ROOT/'docs/data/skills-index.json'; SCHEMA=ROOT/'docs/data/skills.schema.json'

def key(r): return (str(r.get('name','')).casefold(),r.get('class',''),r.get('subcategory',''))
def expected_skill_id(r):
 slug=re.sub(r'[^a-z0-9]+','-',str(r.get('name','')).casefold()).strip('-')
 return f'skill-{slug}'
def valid_skill_id(value): return isinstance(value,str) and bool(re.fullmatch(r'skill-[a-z0-9]+(?:-[a-z0-9]+)*',value))

def main():
 d=json.loads(DATA.read_text(encoding='utf-8')); idx=json.loads(INDEX.read_text(encoding='utf-8')); schema=json.loads(SCHEMA.read_text(encoding='utf-8'))
 ALLOWED_CLASS=set(schema['properties']['class']['enum']); ALLOWED_SUB=set(schema['properties']['subcategory']['enum']); ALLOWED_RESEARCH=set(schema['properties']['research_status']['enum']); ALLOWED_ACQUISITION=set(schema['properties']['acquisition_type']['enum'])
 projection=set(INDEX_PROJECTION_FIELDS); schema_fields=set(schema.get('properties',{}))
 rs=d.get('records',[]); ir=idx.get('records',[]); errors=[]
 if d.get('schema_version') != CATALOG_SCHEMA_VERSION: errors.append(f"skills.json schema_version mismatch: expected {CATALOG_SCHEMA_VERSION!r}")
 if d.get('game') != CATALOG_GAME: errors.append(f"skills.json game mismatch: expected {CATALOG_GAME!r}")
 if d.get('source_index') != CATALOG_SOURCE_INDEX: errors.append('skills.json source_index mismatch with builder metadata')
 if not isinstance(d.get('status'),str) or not d['status'].strip(): errors.append('skills.json status must be a non-empty string')
 if not isinstance(d.get('notes'),str) or not d['notes'].strip(): errors.append('skills.json notes must be a non-empty string')
 if idx.get('schema_version') != CATALOG_SCHEMA_VERSION: errors.append(f"skills-index.json schema_version mismatch: expected {CATALOG_SCHEMA_VERSION!r}")
 if idx.get('source_index') != CATALOG_SOURCE_INDEX: errors.append('skills-index.json source_index mismatch with builder metadata')
 if not projection.issubset(schema_fields):errors.append(f"index projection contains non-canonical fields: {', '.join(sorted(projection-schema_fields))}")
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
 ids=[r.get('id') for r in rs]
 if len(ids)!=len(set(ids)):errors.append('duplicate canonical skill ids')
 if keys!=sorted(keys):errors.append('skills.json records are not in deterministic (casefolded name, class, subcategory) order')
 actual_counts={}
 for r in rs:
  label='Transformations' if r.get('class')=='Awoken' and r.get('subcategory')=='Race' else r.get('subcategory')
  actual_counts[label]=actual_counts.get(label,0)+1
 expected_counts=d.get('category_counts',{})
 for label,count in actual_counts.items():
  if label=='Transformations': continue
  if expected_counts.get(label)!=count:errors.append(f"skills.json category_counts mismatch for {label}: expected {expected_counts.get(label)}, actual {count}")
 if expected_counts.get('Transformations')!=actual_counts.get('Transformations',0):errors.append('skills.json Transformations count does not match Awoken/Race record count')
 targets=d.get('target_category_counts')
 expected_targets=dict(TARGET_COUNTS); expected_targets['Transformations']=15
 if not isinstance(targets,dict):errors.append('skills.json target_category_counts must be an object')
 elif targets!=expected_targets:errors.append('skills.json target_category_counts drift from builder target metadata')
 for r in rs:
  if not valid_skill_id(r.get('id')):errors.append(f"{r.get('name')}: invalid or missing deterministic skill id {r.get('id')!r}")
  if r.get('id') != expected_skill_id(r): errors.append(f"{r.get('name')}: skill id does not match deterministic name slug: {r.get('id')!r}")
  if r.get('class') not in ALLOWED_CLASS:errors.append(f"{r.get('name')}: invalid class {r.get('class')}")
  if r.get('subcategory') not in ALLOWED_SUB:errors.append(f"{r.get('name')}: invalid subcategory {r.get('subcategory')}")

  if r.get('research_status') not in ALLOWED_RESEARCH:errors.append(f"{r.get('name')}: invalid research_status {r.get('research_status')}")
  if r.get('acquisition_type') not in ALLOWED_ACQUISITION:errors.append(f"{r.get('name')}: invalid acquisition_type {r.get('acquisition_type')}")
  acquisition=r.get('acquisition_type'); has_quest=r.get('source_quest') not in (None,'')
  if acquisition in {'tp_medal_shop','character_only','starting_move','other_nonquest'} and has_quest:errors.append(f"{r.get('name')}: {acquisition} acquisition cannot have source_quest")
  pq_provenance_fields=('source_quest','source_quest_or_shop','unlock_method')
  if acquisition=='parallel_quest' and not any(re.search(r'\bparallel quest\s*#?\s*\d+\b|\bpq\s*#?\s*\d+\b', str(r.get(f,'')).casefold()) for f in pq_provenance_fields):errors.append(f"{r.get('name')}: parallel_quest acquisition requires explicit PQ-number provenance")
  if acquisition=='skill_shop' and ('starting move' in str(r.get('unlock_method','')).casefold() or 'starting fighting-style choice' in str(r.get('source_quest_or_shop','')).casefold()):errors.append(f"{r.get('name')}: explicit starting-choice route must not be classified as skill_shop")
  provenance=' '.join(str(r.get(f,'')).casefold() for f in ('source_quest','source_quest_or_shop','unlock_method'))
  if acquisition=='skill_shop' and 'skill shop' not in provenance:errors.append(f"{r.get('name')}: skill_shop acquisition requires explicit Skill Shop provenance")
  if acquisition=='tp_medal_shop' and not re.search(r'\b(?:tp|stp) medal\b', provenance):errors.append(f"{r.get('name')}: tp_medal_shop acquisition requires explicit TP Medal Shop provenance")
  if acquisition=='starting_move' and not re.search(r'starting (?:move|fighting-style choice)', provenance):errors.append(f"{r.get('name')}: starting_move acquisition requires explicit starting-choice provenance")
  if acquisition=='character_only' and not re.search(r'character(?:[- ]only|[- ]exclusive)|character skill', provenance):errors.append(f"{r.get('name')}: character_only acquisition requires explicit character-only provenance")
  uf=r.get('ultimate_finish_required')
  if acquisition=='tp_medal_shop' and r.get('source_quest') not in (None,'') and re.search(r'\bparallel quest\s*#?\s*\d+\b|\bpq\s*#?\s*\d+\b', str(r.get('source_quest_or_shop','')).casefold()):errors.append(f"{r.get('name')}: mixed PQ + TP Medal route must preserve quest_or_mission acquisition_type")
  if uf is True and not any(re.search(r'\bultimate finish\b|\bUF\b', str(r.get(f,'')), re.I) for f in ('unlock_method','source_quest_or_shop')):
   errors.append(f"{r.get('name')}: ultimate_finish_required=true lacks explicit Ultimate Finish provenance")
  if r.get('usable_by_cac') is True:
   if not any(r.get(f) not in (None,'',[]) for f in ('race_restriction','character_source','unlock_method')):
    errors.append(f"{r.get('name')}: usable_by_cac=true lacks player-character evidence")
  for source in r.get('sources',[]):
   if isinstance(source,str) and ('543This' in source or source.endswith('This')):
    errors.append(f"{r.get('name')}: malformed source URL {source}")
 ikeys=[key(r) for r in ir]
 if keys!=ikeys:errors.append('skills-index.json is not in the same deterministic record order/content key sequence as skills.json')
 for a,b in zip(rs,ir):
  expected={f:a[f] for f in INDEX_PROJECTION_FIELDS if f in a}
  if b != expected: errors.append(f"index projection mismatch for {a.get('name')}")
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
