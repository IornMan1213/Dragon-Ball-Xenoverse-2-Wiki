#!/usr/bin/env python3
"""Build the canonical skill catalog from structured public research records."""
from __future__ import annotations
import json,re
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'docs/data/skills.json'; INDEX=ROOT/'docs/data/skills-index.json'; SCHEMA=ROOT/'docs/data/skills.schema.json'; RESEARCH=Path('/tmp/xv2-research/content/skills'); LOCAL_BATCHES=ROOT/'docs/data/skill-research-batches'
CATALOG_SCHEMA_VERSION='1.2'
CATALOG_GAME='Dragon Ball Xenoverse 2'
CATALOG_SOURCE_INDEX='https://dbxv2.fandom.com/wiki/Category:Skills'
DEFAULT_CATALOG_STATUS='structured_research_catalog'
DEFAULT_CATALOG_NOTES='Transformation category counts canonical parent records (15); five additional named forms are documented as stages in the Awoken parent records. Unresolved fields remain blank rather than inferred.'
TARGET_COUNTS={"Ki Blast Supers":183,"Strike Supers":130,"Ki Blast Ultimates":110,"Strike Ultimates":30,"Other Supers":32,"Power Up Supers":20,"Ki Blast Evasives":23,"Strike Evasives":16,"Other Evasives":11,"Power Up Evasives":2,"Other Ultimates":3,"Saiyan Skills":10,"Majin Skills":10,"Namekian Skills":4,"Frieza Race Skills":4,"Human Skills":4,"Unavailable for CaC":37,"Counter Skills":25}
INDEX_PROJECTION_FIELDS=('name','class','subcategory','verification_status','research_status','acquisition_type','sources','unlock_method','ultimate_finish_required','last_verified','race_restriction','notes','mechanics_notes','source_quest','source_quest_or_shop')
def classify_acquisition(d):
 text=' '.join(str(d.get(k,'')) for k in ('source_quest','source_quest_or_shop','unlock_method')).casefold()
 if 'starting move' in text or 'starting fighting-style choice' in text: return 'starting_move'
 if 'skill shop' in text: return 'skill_shop'
 if 'tp medal' in text or 'stp medal' in text:
  if re.search(r'\bparallel quest\s*#?\s*\d+\b|\bpq\s*#?\s*\d+\b', text) or d.get('source_quest') not in (None,''): return 'quest_or_mission'
  return 'tp_medal_shop'
 if re.search(r'\bparallel quest\s*#?\s*\d+\b|\bpq\s*#?\s*\d+\b', text) and (d.get('source_quest') in (None,'') or re.search(r'\bparallel quest\s*#?\s*\d+\b|\bpq\s*#?\s*\d+\b', str(d.get('source_quest','')).casefold())):
  return 'parallel_quest'
 if d.get('source_quest') not in (None,''):
  return 'quest_or_mission'
 if ('built-in' in text or 'not separately acquirable' in text) and ('character-exclusive' in text or 'character exclusive' in text or 'character-only' in text or 'character only' in text): return 'other_nonquest'
 if 'character-exclusive' in text or 'character exclusive' in text or 'character-only' in text or 'character only' in text or 'character skill' in text: return 'character_only'
 return 'other_nonquest'
def normalize_sources(values):
 if values is None:return []
 if not isinstance(values,list):
  raise ValueError('sources must be a list')
 out=[]
 for index,value in enumerate(values):
  if isinstance(value,str) and value:
   out.append(value)
  elif isinstance(value,dict):
   url=value.get('url')
   if isinstance(url,str) and url:
    out.append(url)
   else:
    raise ValueError(f'sources[{index}] object must contain a non-empty url')
  else:
   raise ValueError(f'sources[{index}] must be a non-empty string or object with url')
 return list(dict.fromkeys(out))
def scalar(v):
 v=v.strip().strip('"\\'')
 if not v:
  return ''
 if re.fullmatch(r'\d+',v): return int(v)
 if v.startswith('[') or v.startswith('{'):
  raise ValueError(f'unsupported structured frontmatter scalar: {v}')
 return v
def parse_frontmatter(p):
 t=p.read_text(encoding='utf-8',errors='replace'); parts=t.split('---',2)
 if len(parts)<3: raise ValueError('missing YAML frontmatter delimiters')
 o={}
 for line_number,line in enumerate(parts[1].splitlines(),1):
  if not line.strip(): continue
  m=re.match(r'^([A-Za-z][A-Za-z0-9_]*)\s*:\s*(.*)$',line)
  if not m: raise ValueError(f'invalid frontmatter line {line_number}: {line!r}')
  k,v=m.groups()
  if v.strip().startswith('[') and v.strip().endswith(']'):
   matches=re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"',v)
   if not matches and v.strip()!='[]': raise ValueError(f'invalid frontmatter list for {k}: {v!r}')
   o[k]=matches
  else:
   o[k]=scalar(v)
 return o
def classify(d):
 c=str(d.get('class','')).casefold(); e=str(d.get('element','')).casefold().replace('_',' ').replace('-',' ')
 if c=='super':return 'Super','Ki Blast' if 'blast' in e or e=='ki' else 'Strike' if 'strike' in e else 'Other'
 if c=='ultimate':return 'Ultimate','Ki Blast' if 'blast' in e or e=='ki' else 'Strike' if 'strike' in e else 'Power Up' if 'power' in e else 'Other'
 if c=='evasive':return 'Evasive','Ki Blast' if 'blast' in e or e=='ki' else 'Strike' if 'strike' in e else 'Power Up' if 'power' in e else 'Other'
 if c=='counter':return 'Mixed','Special'
 if c=='awoken':return 'Awoken','Race'
 return 'Mixed','Special'
def load_existing():
 if not OUT.exists():
  return {}
 try:
  d=json.loads(OUT.read_text(encoding='utf-8'))
 except (OSError,json.JSONDecodeError) as exc:
  raise RuntimeError(f'Failed to load existing canonical skill catalog {OUT}: {exc}') from exc
 if not isinstance(d,dict):
  raise ValueError(f'{OUT}: canonical catalog payload must be an object')
 records=d.get('records')
 if not isinstance(records,list):
  raise ValueError(f'{OUT}: canonical catalog records must be a list')
 m={}
 for index,r in enumerate(records):
  if not isinstance(r,dict) or not r.get('name'):
   raise ValueError(f'{OUT}: canonical record {index} must be an object with a name')
  k=(r['name'].casefold(),r.get('class',''),r.get('subcategory',''))
  if k in m:
   raise ValueError(f'{OUT}: duplicate canonical skill key {k}')
  m[k]=r
 return m,d
def merge_record(m,r,protected=None,blocked=None):
 protected=protected if protected is not None else set(); blocked=blocked if blocked is not None else set()
 try:
  schema=json.loads(SCHEMA.read_text(encoding='utf-8'))
 except (OSError,json.JSONDecodeError) as exc:
  raise RuntimeError(f'Failed to load canonical skill schema {SCHEMA}: {exc}') from exc
 properties=schema.get('properties')
 if not isinstance(properties,dict) or not properties:
  raise ValueError(f'{SCHEMA}: schema properties must be a non-empty object')
 canonical_fields=set(properties)
 canonical_fields.discard('sources')
 n=r.get('name')
 if not isinstance(n,str) or not n.strip():return False
 target_class=r.get('class',''); target_subcategory=r.get('subcategory','')
 if not isinstance(target_class,str) or not target_class.strip() or not isinstance(target_subcategory,str) or not target_subcategory.strip():
  raise ValueError(f"invalid skill key for {n}: class and subcategory must be non-empty strings")
 c=r.get('correction_of')
 if c is not None and not isinstance(c,dict):
  raise ValueError(f"invalid correction metadata for {n}: correction_of must be an object")
 if isinstance(c,dict) and not c:
  raise ValueError(f"invalid correction metadata for {n}: correction_of must not be empty")
 c=c or {}
 oldname=c.get('name',n); oldclass=c.get('previous_class',c.get('class',r.get('class',''))); oldsub=c.get('previous_subcategory',c.get('subcategory',r.get('subcategory',r.get('class',''))))
 if not isinstance(oldname,str) or not oldname.strip() or not isinstance(oldclass,str) or not oldclass.strip() or not isinstance(oldsub,str) or not oldsub.strip():
  raise ValueError(f"invalid correction metadata for {n}: correction target name/class/subcategory must be non-empty strings")
 oldkey=(oldname.casefold(),oldclass,oldsub)
 k=(n.casefold(),r.get('class',''),r.get('subcategory',''))
 if not c and k in blocked:return False
 if not c and k in protected:
  old=m.get(k,{})
  for field,value in r.items():
   if field in ('correction_of','correction_fields') or field not in canonical_fields or value in (None,'',[],'—'):continue
   if field not in old or old.get(field) in (None,'',[],'—'):old[field]=value
  old['sources']=normalize_sources(old.get('sources',[])+r.get('sources',[]))
  m[k]=old
  return True
 if c:
  if not isinstance(correction_of := r.get('correction_of'), dict):
   raise ValueError(f"invalid correction metadata for {n}: correction_of must be an object")
  declared_fields=r.get('correction_fields')
  if not isinstance(declared_fields,list) or not declared_fields or not all(isinstance(field,str) and field for field in declared_fields) or len(set(declared_fields)) != len(declared_fields):
   raise ValueError(f"invalid correction metadata for {n}: correction_fields must be a non-empty list of unique field names")
  if 'sources' in declared_fields:
   raise ValueError(f"invalid correction metadata for {n}: sources is provenance and cannot be replaced or cleared by correction_fields")
  unsupported=[field for field in declared_fields if field not in canonical_fields]
  if unsupported:
   raise ValueError(f"invalid correction metadata for {n}: unsupported correction fields: {', '.join(unsupported)}")
  if oldkey not in m:
   raise ValueError(f"correction target not found for {n}: {oldname}/{oldclass}/{oldsub}")
  if oldkey in blocked:
   raise ValueError(f"correction target already superseded for {n}: {oldname}/{oldclass}/{oldsub}")
  if k in m and k != oldkey:
   raise ValueError(f"correction destination already exists for {n}: {r.get('class','')}/{r.get('subcategory','')}")
  m.pop(oldkey,None); blocked.add(oldkey); protected.add(k)
 old=m.get(k,{}) ; out={field:value for field,value in r.items() if field in canonical_fields}; fields=set(r.get('correction_fields',[]))
 for x,v in old.items():
  if x not in fields and v not in (None,'',[],'—'):out[x]=v
 out['sources']=normalize_sources(old.get('sources',[])+r.get('sources',[])); out.pop('correction_fields',None); out.pop('correction_of',None); m[k]=out; return True
def load_local_batches(m,protected=None,blocked=None):
 imported=0
 if not LOCAL_BATCHES.exists():return 0
 for p in sorted(LOCAL_BATCHES.glob('skill-batch-*.json'))+sorted(LOCAL_BATCHES.glob('skills-batch-*.json')):
  try:
   payload=json.loads(p.read_text(encoding='utf-8'))
  except (OSError,json.JSONDecodeError) as exc:
   raise RuntimeError(f'Failed to load local research batch {p.name}: {exc}') from exc
  if not isinstance(payload,dict): raise ValueError(f'{p.name}: batch payload must be an object')
  batch_id=payload.get('batch_id')
  if not isinstance(batch_id,str) or not batch_id.strip():
   raise ValueError(f'{p.name}: batch_id must be a non-empty string')
  batch_status=payload.get('research_status','partially_enriched')
  if batch_status not in ('indexed','partially_enriched','enriched','page_unavailable'):
   raise ValueError(f'{p.name}: invalid research_status: {batch_status!r}')
  rs=payload.get('corrections',[]) if payload.get('corrections') else payload.get('records',[])
  if not isinstance(rs,list): raise ValueError(f'{p.name}: corrections/records must be a list')
  for r in rs:
   if not isinstance(r,dict) or not r.get('name'):
    raise ValueError(f'{p.name}: research record must be an object with a name')
   r=dict(r); r.setdefault('research_status',batch_status); imported+=1; merge_record(m,r,protected,blocked)
 return imported
def build_record(d,p):
 n=d.get('name')
 if not isinstance(n,str) or not n.strip():
  raise ValueError('frontmatter record requires a non-empty name')
 c,s=classify(d); src=f'https://github.com/Madreag/xenoverse_2_wiki/blob/main/content/skills/{p.name}'; r={'name':n,'class':c,'subcategory':s,'verification_status':'partially_verified','research_status':'partially_enriched','sources':[src]}
 if isinstance(d.get('sources'),list):r['sources'] += normalize_sources(d.get('sources',[]))
 if d.get('kiCost') is not None:r['ki_cost']=d['kiCost']
 if d.get('staminaCost') is not None:r['stamina_cost']=d['staminaCost']
 if d.get('element'):r['damage_type']=str(d['element']).title()
 if d.get('source'):r['source_quest_or_shop']=d['source']; r['unlock_method']='See source record'
 if d.get('mentor'):r['character_source']=d['mentor']
 if d.get('dlc') is not None:r['dlc_requirement']=d['dlc']
 if isinstance(d.get('properties'),list) and d['properties']:r['mechanics_notes']=r['skill_description']='; '.join(map(str,d['properties']))
 if d.get('mechanics'):r['mechanics']=str(d['mechanics'])
 if d.get('summary'):r.setdefault('skill_description',str(d['summary']))
 if d.get('lastVerified'):r['last_verified']=str(d['lastVerified'])
 elif re.fullmatch(r'\d{4}-\d{2}-\d{2}',str(d.get('asOfDate',''))):r['last_verified']=str(d['asOfDate'])
 r['acquisition_type']=classify_acquisition(d)
 if d.get('confidence') in ('confirmed','datamined','community'):r['research_status']='enriched'
 return r
def main():
 if not RESEARCH.exists():raise SystemExit('Structured research corpus is missing.')
 m,existing=load_existing(); protected=set(); blocked=set()
 if existing:
  for field,expected in (('schema_version',CATALOG_SCHEMA_VERSION),('game',CATALOG_GAME),('source_index',CATALOG_SOURCE_INDEX)):
   if existing.get(field) != expected:
    raise ValueError(f'{OUT}: {field} must be {expected!r} when rebuilding the canonical catalog')
  for field in ('status','notes'):
   if not isinstance(existing.get(field),str) or not existing[field].strip():
    raise ValueError(f'{OUT}: {field} must be a non-empty string when rebuilding the canonical catalog')
 for p in sorted(RESEARCH.glob('*.md')):
  try:
   r=build_record(parse_frontmatter(p),p)
  except Exception as exc:
   raise RuntimeError(f'Failed to build structured skill record from {p.name}: {exc}') from exc
  if r:merge_record(m,r,protected,blocked)
 imported=load_local_batches(m,protected,blocked)
 rows=sorted(m.values(),key=lambda r:(r['name'].casefold(),r['class'],r['subcategory']))
 awoken=sum(1 for r in rows if r.get('class')=='Awoken' and r.get('subcategory')=='Race')
 counts=dict(TARGET_COUNTS); counts['Transformations']=awoken
 targets=dict(TARGET_COUNTS); targets['Transformations']=15
 payload={'schema_version':existing.get('schema_version',CATALOG_SCHEMA_VERSION),'game':existing.get('game',CATALOG_GAME),'source_index':existing.get('source_index',CATALOG_SOURCE_INDEX),'generated':date.today().isoformat(),'status':existing.get('status',DEFAULT_CATALOG_STATUS),'category_counts':counts,'target_category_counts':targets,'record_count':len(rows),'records':rows,'notes':existing.get('notes',DEFAULT_CATALOG_NOTES)}
 OUT.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 INDEX.write_text(json.dumps({'schema_version':'1.2','source_index':payload['source_index'],'generated':payload['generated'],'category_counts':counts,'target_category_counts':targets,'record_count':len(rows),'records':[{k:r[k] for k in INDEX_PROJECTION_FIELDS if k in r} for r in rows]},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print(f'Imported {imported}; total records={len(rows)}; Awoken parent records={awoken}')
if __name__=='__main__':raise SystemExit(main())
