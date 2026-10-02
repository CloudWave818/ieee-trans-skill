#!/usr/bin/env python3
"""Retrieve candidates from the preferred 29; selection still requires source inspection."""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / 'references/preferred_29'
GROUPS = [
    ('tracking','tracker','追踪','跟踪'), ('prediction','predict','预测'), ('intention','意图'),
    ('formation','swarm','multi-agent','编队','集群','多机','多智能体'),
    ('reinforcement','rl','ppo','policy','强化学习','策略'),
    ('safety','safe','shield','cbf','安全','屏蔽'),
    ('trajectory','planner','planning','navigation','轨迹','规划','导航'),
    ('training','train','训练'), ('deployment','deploy','部署'),
    ('vision','visual','rgb','camera','monocular','视觉','单目'),
    ('point','cloud','点云'), ('hardware','morph','morphing','机构','形变','硬件'),
    ('reset','sampling','curriculum','重置','采样','课程'),
    ('domain','adaptation','gradient','域适应','对抗','梯度'),
    ('control','controller','控制'), ('localization','odometry','vio','定位','里程计'),
    ('speed','agility','速度','敏捷'), ('hierarchical','outer','high-level','层级','外环','高层'),
]
STOP = {'the','and','for','with','paper','method','write','plan','only','full','task','section','design','my','a','an','to','in','of'}

# Figure purpose is separate from the paper's topic. In particular, "RL" and
# "tracking" do not explain whether a figure should show gradients, deployment,
# an intention mechanism, or just module interfaces. These source-observed
# features rank candidates; they do not approve a style or require a component.
FIGURE_CONCEPTS = {
    'interfaces': ('interface','interfaces','signal flow','block diagram','接口','信号流','模块连接'),
    'sensing': ('sensor','sensors','onboard','perception','传感器','感知','机载'),
    'mapping': ('map','mapping','local map','地图','建图'),
    'tracking': ('tracking','tracker','追踪','跟踪'),
    'planning': ('planner','planning','trajectory','规划','轨迹'),
    'control': ('control','controller','控制'),
    'intention': ('intention','intent','意图'),
    'prediction': ('prediction','predictor','predict','future target','预测','未来目标'),
    'geometry': ('visibility','occlusion','geometric','geometry','视线','可见性','遮挡','几何'),
    'policy': ('policy','reinforcement','rl','ppo','策略','强化学习'),
    'hierarchy': ('hierarchical','hierarchy','high-level','high level','outer loop','outer-loop','outer','层级','高层','外环'),
    'agility': ('agility','speed','速度','敏捷'),
    'asymmetry': ('asymmetric','asymmetry','privileged','非对称','特权'),
    'actor_critic': ('actor critic','actor-critic','actor_critic','actor–critic','演员评论家'),
    'training': ('training','train','训练'),
    'deployment': ('deployment','deploy','部署'),
    'safety_filter': ('hocbf','cbf','safety filter','shield','安全过滤','安全滤波','安全屏蔽'),
    'domain': ('domain','domain adaptation','domain-adversarial','sim-to-real','sim2real','域适应','域对抗','域对齐'),
    'gradient': ('gradient','grl','gradient reversal','梯度','梯度反转'),
    'adversarial': ('adversarial','adversary','对抗'),
    'reset_sampling': ('reset','sampling','curriculum','重置','采样','课程'),
    'reward': ('reward','奖励'),
    'distribution': ('distribution','biased','分布','偏置'),
    'hardware': ('hardware','mechanism design','morphing','morph','硬件','机构','形变'),
    'dynamics': ('dynamics','forces','force','动力学','受力','力学'),
    'software': ('software','软件'),
    'functional_bands': ('horizontal bands','functional bands','functional layers','software architecture','task layer','planning layer','control layer','横向分层','功能分层','软件架构','功能带','横向色带'),
    'estimation': ('estimation','estimator','odometry','vio','状态估计','估计器','里程计'),
    'actuation': ('actuation','actuator','actuators','执行器','驱动'),
    'multipanel': ('multipanel','multi-panel','多面板','多子图'),
}
FRAMEWORK_FOCUS = {
    'R01-F2': {
        'purpose': 'Compact module interfaces and the sensing/planning/control chain',
        'features': {'interfaces':12,'sensing':8,'mapping':8,'tracking':4,'planning':8,'control':8,'estimation':4},
        'combinations': [('interface_chain', ('sensing','planning','control'),18),
                         ('state_map_interfaces', ('mapping','control'),10)],
    },
    'R06-F2': {
        'purpose': 'Target intention, future prediction and geometric planning mechanisms',
        'features': {'intention':22,'prediction':16,'geometry':12,'tracking':4,'sensing':2,'mapping':2,'planning':4,'control':2},
        'combinations': [('intention_prediction', ('intention','prediction'),20),
                         ('predictive_geometric_planning', ('prediction','geometry','planning'),12)],
    },
    'R12-F2': {
        'purpose': 'Learned high-level action linked to a model-based planner and low-level tracking',
        'features': {'hierarchy':22,'policy':6,'agility':12,'planning':6,'control':3,'sensing':2,'mapping':2},
        'combinations': [('hierarchical_policy_planner', ('hierarchy','policy','planning'),22),
                         ('agility_policy', ('agility','policy'),12)],
    },
    'R20-F2': {
        'purpose': 'Training reset/distribution mechanism, closed-loop policy and reward decomposition',
        'features': {'reset_sampling':22,'reward':16,'distribution':14,'training':6,'policy':4},
        'combinations': [('training_reset_distribution', ('training','reset_sampling','distribution'),20),
                         ('reset_reward', ('reset_sampling','reward'),12)],
    },
    'R23-F3': {
        'purpose': 'Data-domain lanes, actor/critic networks and adversarial gradient paths',
        'features': {'domain':22,'gradient':22,'adversarial':14,'actor_critic':4,'asymmetry':3,'training':4,'policy':2},
        'combinations': [('domain_gradient_paths', ('domain','gradient'),22),
                         ('domain_adversarial', ('domain','adversarial'),12)],
    },
    'R25-F1': {
        'purpose': 'Asymmetric actor/critic branches with distinct training and deployed safety-control paths',
        'features': {'asymmetry':18,'actor_critic':12,'training':6,'deployment':18,'safety_filter':16,'policy':2,'control':3},
        'combinations': [('asymmetric_actor_critic', ('asymmetry','actor_critic'),14),
                         ('training_deployment', ('training','deployment'),14),
                         ('deployed_safety_filter', ('deployment','safety_filter'),14)],
    },
    'R29-F2': {
        'purpose': 'Hardware, software and dynamics in a full multipanel system figure',
        'features': {'hardware':20,'dynamics':20,'software':3,'multipanel':16,'control':2,'planning':2},
        'combinations': [('hardware_dynamics', ('hardware','dynamics'),18),
                         ('hardware_software_dynamics', ('hardware','software','dynamics'),12)],
    },
    'R29-F2-software': {
        'purpose': 'Functional software bands linking task/planning/control to estimation and actuation',
        'features': {'functional_bands':22,'software':12,'planning':6,'control':6,'estimation':10,'actuation':12},
        'combinations': [('control_estimation_actuation', ('control','estimation','actuation'),14),
                         ('software_planning_control', ('software','planning','control'),14)],
    },
}


def read(path, default):
    return json.loads(path.read_text(encoding='utf-8-sig')) if path.is_file() else default


def flatten(value):
    if isinstance(value, dict): return ' '.join(flatten(v) for v in value.values())
    if isinstance(value, list): return ' '.join(flatten(v) for v in value)
    return str(value)


def contains(text, term):
    if re.fullmatch(r'[a-z0-9_-]+', term):
        return bool(re.search(r'(?<![a-z0-9])' + re.escape(term) + r'(?![a-z0-9])', text))
    return term in text


def score(text, query):
    text = text.casefold(); query = query.casefold()
    group_hits = sum(any(contains(query, t) for t in g) and any(contains(text, t) for t in g) for g in GROUPS)
    tokens = [t for t in re.findall(r'[a-z][a-z0-9_-]{2,}|[\u4e00-\u9fff]+', query) if t not in STOP]
    literal_hits = sum(contains(text, t) for t in set(tokens))
    return group_hits * 10 + literal_hits, group_hits, literal_hits


def figure_concepts(query):
    query = query.casefold()
    found = {name for name, aliases in FIGURE_CONCEPTS.items() if any(contains(query, t) for t in aliases)}
    if contains(query, 'actor') and contains(query, 'critic'):
        found.add('actor_critic')
    return found


def framework_score(anchor, query, concepts, main_paper_id):
    aid = anchor.get('anchor_id', anchor.get('case_id'))
    focus = FRAMEWORK_FOCUS.get(aid, {})
    # Search factual source identity and observed figure content. Instructions
    # such as "do not copy a neural network" must not count as network evidence.
    observed = flatten([anchor.get(k, '') for k in ('title','family','zones','distinctive_features')])
    _, groups, literal = score(observed, query)
    relationship_score = groups * 3 + min(literal, 8)
    matches = [{'concept':name,'weight':weight} for name, weight in focus.get('features', {}).items() if name in concepts]
    combinations = [{'name':name,'concepts':list(required),'weight':weight}
                    for name, required, weight in focus.get('combinations', []) if set(required) <= concepts]
    purpose_score = sum(m['weight'] for m in matches) + sum(m['weight'] for m in combinations)
    focus_conflicts = []
    # A specific stated purpose may be shared by several papers; distinguish
    # the two visually similar network anchors only when that purpose is clear.
    if aid == 'R23-F3' and {'training','deployment'} <= concepts and not concepts & {'domain','gradient','adversarial'}:
        focus_conflicts.append({'reason':'Query foregrounds training/deployment; this source foregrounds domain and gradient paths.','penalty':12})
    if aid == 'R25-F1' and concepts & {'domain','gradient','adversarial'} and not concepts & {'deployment','safety_filter'}:
        focus_conflicts.append({'reason':'Query foregrounds domain/gradient mechanisms; this source foregrounds asymmetric training and deployed control.','penalty':12})
    main_paper_bonus = 15 if main_paper_id and aid.startswith(main_paper_id+'-') else 0
    total = relationship_score + purpose_score + main_paper_bonus - sum(c['penalty'] for c in focus_conflicts)
    return total, {'relationship_groups':groups,'literal_hits':literal,'relationship_score':relationship_score,
                   'mechanism_matches':matches,'purpose_combinations':combinations,'purpose_score':purpose_score,
                   'focus_conflicts':focus_conflicts,'main_paper_bonus':main_paper_bonus}, focus.get('purpose', anchor['family'])


def list_records(value):
    if isinstance(value, list): return value
    if isinstance(value, dict):
        for key in ('profiles','papers','anchors','records'):
            if isinstance(value.get(key), list): return value[key]
    return []


def select_references(query, article_form='UNDECIDED', paper_id=None, framework_id=None, limit=3):
    if not 1 <= limit <= 5: raise ValueError('limit must be 1..5')
    papers = read(REF / 'papers.json', [])
    ids = re.findall(r'(?<![A-Za-z0-9])(R\d{2})(?![-A-Za-z0-9])', query, re.I)
    if not paper_id and len(set(x.upper() for x in ids)) == 1:
        paper_id = ids[0].upper()
    known = {p['paper'] for p in papers}
    if paper_id and paper_id not in known: raise ValueError('Unknown preferred_paper_id: ' + str(paper_id))
    profiles = list_records(read(REF / 'manuscript_profiles/profiles.json', []))
    by_id = {p.get('paper_id', p.get('paper', p.get('id'))): p for p in profiles}
    ranked = []
    for p in papers:
        pid = p['paper']; profile = by_id.get(pid, {})
        value, groups, literal = score(flatten([p['title'], p['tags'], p['paper_story']]), query)
        # A source-confirmed Letter is preferred for a Letter task; compact morphology
        # alone is never upgraded to a verified publication category.
        form_record = profile.get('article_form', {})
        confirmed_form = form_record.get('value') if isinstance(form_record, dict) else form_record
        form_bonus = 20 if article_form != 'UNDECIDED' and confirmed_form == article_form else 0
        morphology = profile.get('morphology', '')
        morphology_bonus = 6 if ((article_form == 'LETTER' and morphology == 'IEEE_COMPACT') or
                                (article_form == 'TRANSACTIONS' and morphology == 'IEEE_EXTENDED')) else 0
        if paper_id: value += 1000 if pid == paper_id else 0
        elif not value and not form_bonus: continue
        ranked.append((value + form_bonus + morphology_bonus, pid, p, groups, literal, form_bonus, morphology_bonus))
    ranked.sort(key=lambda x: (-x[0], x[1]))
    candidates = [{'paper_id':pid,'title':p['title'],'score':val,
                   'score_breakdown':{'relationship_groups':groups,'literal_hits':literal,'confirmed_form_bonus':bonus,'layout_bonus':morph_bonus},
                   'observed_form':by_id.get(pid,{}).get('article_form',{}),
                   'observed_morphology':by_id.get(pid,{}).get('morphology','UNKNOWN'),
                   'source_pdf':'papers/preferred_29/' + p['filename'],
                   'profile':'references/preferred_29/manuscript_profiles/' + pid + '.md',
                   'evidence_profile':'references/preferred_29/evidence_profiles/' + pid + '.md',
                   'publication_identity':'Read exact profile evidence; page length is not venue verification'}
                  for val,pid,p,groups,literal,bonus,morph_bonus in ranked[:limit]]
    anchors = list_records(read(REF / 'framework_anchors/anchors.json', []))
    anchor_ids = {a.get('anchor_id', a.get('case_id')) for a in anchors}
    if framework_id and framework_id not in anchor_ids:
        raise ValueError('Unknown preferred_framework_id: ' + str(framework_id))
    aranked=[]
    concepts = figure_concepts(query)
    for a in anchors:
        aid = a.get('anchor_id', a.get('case_id'))
        val, breakdown, purpose = framework_score(a, query, concepts, candidates[0]['paper_id'] if candidates else None)
        explicit_bonus = 1000 if framework_id and aid == framework_id else 0
        val += explicit_bonus
        breakdown['explicit_framework_bonus'] = explicit_bonus
        # Article form alone can retrieve a manuscript profile. It cannot select
        # a framework when the query supplies no figure evidence or source ID.
        query_evidence = breakdown['relationship_score'] or breakdown['purpose_score']
        if not query_evidence and not explicit_bonus and not (paper_id and aid.startswith(paper_id+'-')):
            continue
        if val > 0: aranked.append((val, aid, a, breakdown, purpose))
    aranked.sort(key=lambda x: (-x[0], x[1]))
    framework_candidates = [{'anchor_id':aid,'case_id':a.get('case_id',aid),'score':val,
                             'score_breakdown':breakdown,'figure_purpose':purpose,
                             'card':a.get('card_path','references/preferred_29/framework_anchors/' + aid + '.md'),
                             'source_pdf':a['source_pdf'],'pdf_page':a['pdf_page'],
                             'original_crop':a['crop_path'],'family':a['family'],
                             'aspect_ratio':a['aspect_ratio'],
                            'inspection_required':True} for val,aid,a,breakdown,purpose in aranked[:limit]]
    # Measured anchors are a subset, so expose a semantically closer original
    # from the selected paper instead of forcing that paper into another style.
    cases=read(REF/'cases.json',[])
    source_candidates=[]
    primary_ids={p['paper_id'] for p in candidates[:1]}
    for c in cases:
        observed=c.get('observed','').casefold()
        framework_like=any(t in observed for t in ('框图','框架','系统结构','闭环','网络结构','训练流程','pipeline','architecture','framework','actor','critic','policy','cnn','mlp')) and not any(t in observed for t in ('曲线','横轴','纵轴'))
        if c.get('paper_id') not in primary_ids or not framework_like: continue
        val,_,_=score(flatten([c.get('observed'),c.get('purpose'),c.get('tags')]),query)
        source_candidates.append({'case_id':c['case_id'],'score':val,'card':c['card'],
                                  'source_pdf':c['source_pdf'],'pdf_page':c['pdf_page'],
                                  'measured_anchor_available':c['case_id'] in anchor_ids,
                                  'inspection_required':True,
                                  'use':'Exact source candidate from the main paper; open PDF figure when no crop exists.'})
    source_candidates.sort(key=lambda c:(-c['score'],c['case_id']))
    return {'status':'CANDIDATES_REQUIRE_INSPECTION' if candidates or framework_candidates else 'NO_MATCHING_REFERENCE',
            'article_form':article_form, 'paper_candidates':candidates,
            'framework_candidates':framework_candidates,
            'main_paper_framework_sources':source_candidates[:limit],
            'query_figure_concepts':sorted(concepts),
            'framework_selection_note':'Purpose and mechanism matches rank source candidates only. Broad topic words do not determine a figure style; inspect originals and the actual method graph before selecting.',
            'explicit_paper_id':paper_id,'explicit_framework_id':framework_id,
            'contract':'Select one main paper and one actual framework crop as needed; no automatic style approval or invented venue identity.'}


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('query')
    ap.add_argument('--form', choices=['LETTER','TRANSACTIONS','CONFERENCE','OTHER','UNDECIDED'], default='UNDECIDED')
    ap.add_argument('--paper'); ap.add_argument('--framework'); ap.add_argument('--limit', type=int, default=3)
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    result = select_references(args.query,args.form,args.paper,args.framework,args.limit)
    rendered = json.dumps(result,ensure_ascii=False,indent=2)
    if args.output: args.output.write_text(rendered,encoding='utf-8')
    print(rendered)
