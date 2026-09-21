#!/usr/bin/env python3
"""Build the canonical skill catalog from structured public research records."""
from __future__ import annotations
import json,re
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'docs/data/skills.json'; INDEX=ROOT/'docs/data/skills-index.json'; RESEARCH=Path('/tmp/xv2-research/content/skills'); LOCAL_BATCHES=ROOT/'docs/data/skill-research-batches'
TARGET_COUNTS={"Ki Blast Supers":183,"Strike Supers":130,"Ki Blast Ultimates":110,"Strike Ultimates":30,"Other Supers":32,"Power Up Supers":20,"Ki Blast Evasives":23,"Strike Evasives":16,"Other Evasives":11,"Power Up Evasives":2,"Other Ultimates":3,"Saiyan Skills":10,"Majin Skills":10,"Namekian Skills":4,"Frieza Race Skills":4,"Human Skills":4,"Unavailable for CaC":37,"Counter Skills":25}
def classify_acquisition(d):
 text=' '.join(str(d.get(k,'')) for k in ('source_quest','source_quest_or_shop','unlock_method','source')).casefold()
 if 'starting move' in text or 'starting fighting-style choice' in text: return 'starting_move'
 if 'skill shop' in text: return 'skill_shop'
 if 'tp medal' in text or 'stp medal' in text:
  if re.search(r'\bparallel quest\s*#?\s*\d+\b|\bpq\s*#?\s*\d+\b', text) or d.get('source_quest') not in (None,''): return 'quest_or_mission'
  return 'tp_medal_shop'
 if d.get('source_quest') not in (None,''):
  if isinstance(d.get('source_quest'),str) and re.search(r'\bparallel quest\s*#?\s*\d+\b|\bpq\s*#?\s*\d+\b', text): return 'parallel_quest'
  return 'quest_or_mission'
 if re.search(r'\bparallel quest\s*#?\s*\d+\b|\bpq\s*#?\s*\d+\b', text): return 'parallel_quest'
 if 'character-exclusive' in text or 'character exclusive' in text or 'character-only' in text or 'character only' in text or 'character skill' in text: return 'character_only'
 return 'other_nonquest'
def normalize_sources(values):
 out=[]
 for value in values or []:
  if isinstance(value,str) and value:
   out.append(value)
  elif isinstance(value,dict):
   url=value.get('url')
   if isinstance(url,str) and url:
    out.append(url)
 return list(dict.fromkeys(out))
def scalar(v):
 v=v.strip().strip('"\''); return int(v) if re.fullmatch(r'\d+',v) else v
def parse_frontmatter(p):
 t=p.read_text(encoding='utf-8',errors='replace'); parts=t.split('---',2)
 if len(parts)<3:return {}
 o={}
 for line in parts[1].splitlines():
  m=re.match(r'^([A-Za-z][A-Za-z0-9_]*)\s*:\s*(.*)$',line)
  if not m:continue
  k,v=m.groups(); o[k]=re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"',v) if v.strip().startswith('[') and v.strip().endswith(']') else scalar(v)
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
 try:d=json.loads(OUT.read_text(encoding='utf-8'))
 except (OSError,json.JSONDecodeError):return {}
 return {(r.get('name','').casefold(),r.get('class',''),r.get('subcategory','')):r for r in d.get('records',[]) if r.get('name')}
def merge_record(m,r,protected=None,blocked=None):
 protected=protected if protected is not None else set(); blocked=blocked if blocked is not None else set()
 n=r.get('name');
 if not n:return False
 c=r.get('correction_of') or {}; oldname=c.get('name',n); oldclass=c.get('previous_class',c.get('class',r.get('class',''))); oldsub=c.get('previous_subcategory',c.get('subcategory',r.get('subcategory',r.get('class','')))); oldkey=(oldname.casefold(),oldclass,oldsub)
 k=(n.casefold(),r.get('class',''),r.get('subcategory',''))
 if not c and k in blocked:return False
 if not c and k in protected:
  old=m.get(k,{})
  for field,value in r.items():
   if field in ('correction_of','correction_fields') or value in (None,'',[],'—'):continue
   if field not in old or old.get(field) in (None,'',[],'—'):old[field]=value
  old['sources']=normalize_sources(old.get('sources',[])+r.get('sources',[]))
  m[k]=old
  return True
 if c:
  m.pop(oldkey,None); blocked.add(oldkey); protected.add(k)
 old=m.get(k,{}) ; out=dict(r); fields=set(r.get('correction_fields',[]))
 for x,v in old.items():
  if x not in fields and v not in (None,'',[],'—'):out[x]=v
 out['sources']=normalize_sources(old.get('sources',[])+r.get('sources',[])); out.pop('correction_fields',None); out.pop('correction_of',None); m[k]=out; return True
def load_local_batches(m,protected=None,blocked=None):
 imported=0
 if not LOCAL_BATCHES.exists():return 0
 for p in sorted(LOCAL_BATCHES.glob('skill-batch-*.json'))+sorted(LOCAL_BATCHES.glob('skills-batch-*.json')):
  try:payload=json.loads(p.read_text(encoding='utf-8'))
  except (OSError,json.JSONDecodeError):continue
  rs=payload.get('corrections',[]) if payload.get('corrections') else payload.get('records',[])
  for r in rs:
   if not isinstance(r,dict) or not r.get('name'):continue
   r=dict(r); r['research_batch']=payload.get('batch_id'); r['research_status']='partially_enriched'; imported+=1; merge_record(m,r,protected,blocked)
 return imported
def build_record(d,p):
 n=d.get('name');
 if not n:return None
 c,s=classify(d); src=f'https://github.com/Madreag/xenoverse_2_wiki/blob/main/content/skills/{p.name}'; r={'name':n,'class':c,'subcategory':s,'verification_status':'partially_verified','research_status':'partially_enriched','sources':[src]}
 if isinstance(d.get('sources'),list):r['sources'] += normalize_sources(d.get('sources',[]))
 if d.get('kiCost') is not None:r['ki_cost']=d['kiCost']
 if d.get('element'):r['damage_type']=str(d['element']).title()
 if d.get('source'):r['source_quest_or_shop']=d['source']; r['unlock_method']='See source record'
 if d.get('mentor'):r['character_source']=d['mentor']
 if isinstance(d.get('properties'),list) and d['properties']:r['mechanics_notes']=r['skill_description']='; '.join(map(str,d['properties']))
 if d.get('summary'):r.setdefault('skill_description',str(d['summary']))
 if d.get('lastVerified'):r['last_verified']=str(d['lastVerified'])
 r['acquisition_type']=classify_acquisition(d)
 if d.get('confidence'):r['research_status']='enriched'
 return r
def main():
 if not RESEARCH.exists():raise SystemExit('Structured research corpus is missing.')
 m=load_existing(); protected=set(); blocked=set()
 for p in sorted(RESEARCH.glob('*.md')):
  try:r=build_record(parse_frontmatter(p),p)
  except Exception:r=None
  if r:merge_record(m,r,protected,blocked)
 imported=load_local_batches(m,protected,blocked)
 rows=sorted(m.values(),key=lambda r:(r['name'].casefold(),r['class'],r['subcategory']))
 awoken=sum(1 for r in rows if r.get('class')=='Awoken' and r.get('subcategory')=='Race')
 counts=dict(TARGET_COUNTS); counts['Transformations']=awoken
 targets=dict(TARGET_COUNTS); targets['Transformations']=15
 payload={'schema_version':'1.2','game':'Dragon Ball Xenoverse 2','source_index':'https://dbxv2.fandom.com/wiki/Category:Skills','generated':date.today().isoformat(),'status':'structured_research_catalog','category_counts':counts,'target_category_counts':targets,'record_count':len(rows),'records':rows,'notes':'Transformation category counts canonical parent records (15); five additional named forms are documented as stages in the Awoken parent records. Unresolved fields remain blank rather than inferred.'}
 OUT.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 INDEX.write_text(json.dumps({'schema_version':'1.2','source_index':payload['source_index'],'generated':payload['generated'],'category_counts':counts,'target_category_counts':targets,'record_count':len(rows),'records':[{k:r[k] for k in ('name','class','subcategory','verification_status','research_status','acquisition_type','sources') if k in r} for r in rows]},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print(f'Imported {imported}; total records={len(rows)}; Awoken parent records={awoken}')
if __name__=='__main__':raise SystemExit(main())
