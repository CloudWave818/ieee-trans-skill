#!/usr/bin/env python3
"""Retrieve inspected cases by scientific relationship; absence is explicit."""
import argparse
import json
import sys
from pathlib import Path

DEFAULT_CASES = Path(__file__).resolve().parents[1]/'references/visual_cases/cases.json'
PREFERRED_CASES = Path(__file__).resolve().parents[1]/'references/preferred_29/cases.json'

# Match the scientific relationship in the figure, not merely the paper's topic.
ALIASES = [
    ('training','训练','学习曲线'), ('reinforcement','rl','强化学习'),
    ('safety','安全','约束'), ('shield','屏蔽','过滤器','hocbf'),
    ('trajectory','轨迹'), ('formation','编队','队形'),
    ('tracking','追踪','跟踪'), ('intention','意图'),
    ('prediction','预测'), ('curriculum','课程','重置'),
    ('domain','域适应'), ('grasping','抓取','抓握'),
    ('hardware','硬件','机构'), ('point-cloud','点云'),
]


def query_preferred(cases, terms, limit=3):
    if not 1 <= limit <= 5:
        raise ValueError('limit must be between 1 and 5')
    tokens=[x.casefold() for x in terms.split() if x.strip()]
    expanded=[next((group for group in ALIASES if token in group),(token,)) for token in tokens]
    ranked=[]
    for c in cases:
        if c.get('review_status') != 'VISUAL_AND_CONTEXT_REVIEWED':continue
        if any('reinforcement' in group for group in expanded) and not c['learning_type'].startswith('RL_'):
            continue
        design=c.get('design',{})
        local=' '.join([c['observed'],c['purpose'],c['transfer'],design.get('focus',''),
                        design.get('ports_or_axes',''),design.get('mechanism_to_evidence','')]).casefold()
        paper=' '.join([c['title'],*c['tags'],c['learning_type']]).casefold()
        local_hits=sum(any(t in local for t in group) for group in expanded)
        paper_hits=sum(any(t in paper for t in group) for group in expanded)
        exact=c['case_id'].casefold() in tokens or c['paper_id'].casefold() in tokens
        if not local_hits and not exact:continue
        score=8*local_hits+paper_hits+2*bool(design)+50*exact
        # Favor actual learning charts over a framework for learning-curve requests.
        asks_training=any('training' in group for group in expanded)
        if asks_training and any(t in c['observed'] for t in ('训练','回报','Reward','Return','Steps','Iterations')):
            if any(t in c['observed'] for t in ('曲线','vs','横轴','纵轴')):score+=8
        ranked.append((score,c['case_id'],c))
    ranked.sort(key=lambda r:(-r[0],r[1]))
    return [{'case_id':c['case_id'],'score':score,'title':c.get('design',{}).get('focus',c['title']),
             'card':c['card'],'figures':[c['figure']],'pdf_page':c['pdf_page'],
             'review_status':c['review_status'],'detail_level':c['detail_level'],
             'source_set':c['source_set'],'source_pdf':c.get('source_pdf'),
             'boundary':c.get('design',{}).get('boundary',c['transfer'])}
            for score,_,c in ranked[:limit]]


def query(cases, terms, limit=3):
    if not 1 <= limit <= 5:
        raise ValueError('limit must be between 1 and 5')
    tokens = [x.casefold() for x in terms.split() if x.strip()]
    ranked = []
    for case in cases:
        if case.get('review_status') != 'VISUAL_AND_CONTEXT_REVIEWED':
            continue
        tags = ' '.join([*case['tags'],case.get('journal',''),case.get('corpus_layer','')]).casefold()
        title = case['title'].casefold()
        body = ' '.join(case[k] for k in ['observed','purpose','transfer']).casefold()
        score = sum(3*(token in tags)+2*(token in title)+(token in body) for token in tokens)
        if score:
            ranked.append((score, case['case_id'], case))
    ranked.sort(key=lambda r: (-r[0], r[1]))
    return [{'case_id':c['case_id'],'score':score,'title':c['title'],
             'card':f"references/visual_cases/{c['case_id']}.md",
             'figures':list(c['panels']),'pdf_page':c['pdf_page'],
             'review_status':c['review_status'],'boundary':c['boundary']}
            for score, _, c in ranked[:limit]]


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('terms', help='English tags or Chinese terms; whitespace-separated')
    parser.add_argument('--limit', type=int, default=3)
    parser.add_argument('--source', choices=['auto','preferred','legacy'],default='auto',
                        help='auto uses the user-preferred 29 first; legacy only if no preferred figure matches')
    args = parser.parse_args()
    results=[];source='USER_PREFERRED_29'
    if args.source!='legacy' and PREFERRED_CASES.is_file():
        results=query_preferred(json.loads(PREFERRED_CASES.read_text(encoding='utf-8')),args.terms,args.limit)
    if args.source=='legacy' or (args.source=='auto' and not results):
        source='LEGACY_VISUAL_CASES'
        results = query(json.loads(DEFAULT_CASES.read_text(encoding='utf-8')), args.terms, args.limit)
    print(json.dumps({'status':'MATCHES' if results else 'NO_MATCHING_INSPECTED_REFERENCE',
                      'source_set':source,'results':results,
                      'use':'Read the card and its limits; lexical relevance is not scientific applicability. Title-only plans remain provisional.'},ensure_ascii=False,indent=2))
