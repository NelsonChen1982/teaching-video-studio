#!/usr/bin/env python3
"""Validate design-decision completeness, not artistic quality."""
import argparse
import json
from pathlib import Path


def validate(data, require_reviewed=False):
    errors=[]
    def need(ok,message):
        if not ok: errors.append(message)
    def text(v):return isinstance(v,str) and bool(v.strip())
    need(isinstance(data,dict),'Root must be an object')
    if not isinstance(data,dict):return errors
    need(data.get('version')==1,'version must be 1')
    need(data.get('engine') in {'hyperframes','remotion'},'Choose one render engine')
    style=data.get('style',{})
    if not isinstance(style,dict):style={}
    for key in ['intent','motion']:need(text(style.get(key)),f'style.{key} is required')
    evidence=style.get('evidence')
    need(isinstance(evidence,list) and len(evidence)>0 and all(text(x) for x in evidence),'Record observable style evidence or explicit named-style assumptions')
    traits=style.get('traits',{})
    if not isinstance(traits,dict):traits={}
    for key in ['line','shape','palette','material','composition','type']:need(text(traits.get(key)),f'style.traits.{key} is required')
    transitions=data.get('transitions')
    need(isinstance(transitions,list) and len(transitions)>0,'At least one handoff decision (including none) required')
    ids=set()
    for i,tr in enumerate(transitions if isinstance(transitions,list) else []):
        label=f'transitions[{i}]'
        if not isinstance(tr,dict):errors.append(label+' must be an object');continue
        ident=tr.get('id');need(text(ident) and ident not in ids,label+' needs a unique id')
        if text(ident):ids.add(ident)
        need(tr.get('relation') in {'continuation','cause-effect','comparison','location-change','time-jump','chapter-change'},label+' needs scene relationship')
        need(tr.get('asset_mode') in {'plate','cutout','layers','scene3d'},label+' needs actual asset mode')
        for key in ['reason','implementation']:need(text(tr.get(key)),label+'.'+key+' required')
        candidates=tr.get('candidates',[])
        valid=isinstance(candidates,list) and len(candidates)>=2 and all(isinstance(c,dict) and text(c.get('id')) and text(c.get('tradeoff')) for c in candidates)
        need(valid,label+' needs at least two candidates and tradeoffs')
        if valid:
            options=[c['id'] for c in candidates]
            need(len(options)==len(set(options)),label+' candidate ids must be unique')
            need(bool(set(options)&{'cut','none','match-continuity'}),label+' needs a low-effect alternative')
            need(tr.get('selected') in options,label+' selected must name a candidate')
        times=tr.get('qa_times',[])
        need(isinstance(times,list) and all(isinstance(t,(int,float)) and not isinstance(t,bool) and 0<=t<=1 for t in times) and all(t in times for t in [0,.25,.5,.75,1]),label+' needs five transition sampling points')
    review=data.get('review',{})
    if not isinstance(review,dict):review={}
    for key in ['styleframe','transition_sample']:
        need(review.get(key) in {'pending','passed','failed'},'review.'+key+' must be pending/passed/failed')
        if require_reviewed:need(review.get(key)=='passed','review.'+key+' has not passed')
    if require_reviewed:need(isinstance(review.get('evidence'),list) and len(review['evidence'])>0 and all(text(x) for x in review['evidence']),'Reviewed delivery needs actual evidence locations')
    return errors


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('path');p.add_argument('--require-reviewed',action='store_true');args=p.parse_args()
    try:errors=validate(json.loads(Path(args.path).read_text()),args.require_reviewed)
    except (OSError,ValueError) as exc:p.exit(1,str(exc)+'\n')
    if errors:p.exit(1,'\n'.join(errors)+'\n')
    print('Decision structure valid. Visual quality is not certified.')
