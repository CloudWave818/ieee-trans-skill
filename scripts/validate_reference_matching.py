#!/usr/bin/env python3
"""Check source identities, cross-resource coverage and retrieval invariants."""
import hashlib
import json
import sys
from pathlib import Path
from select_style_reference import select_references

ROOT=Path(__file__).resolve().parents[1]
REF=ROOT/'references/preferred_29'

def validate():
    checks=[]
    def check(name, ok, detail=''):
        checks.append({'check':name,'passed':bool(ok),'detail':detail})
    papers=json.loads((REF/'papers.json').read_text(encoding='utf-8'))
    by_id={p['paper']:p for p in papers}
    manuscript=json.loads((REF/'manuscript_profiles/profiles.json').read_text(encoding='utf-8'))
    evidence=json.loads((REF/'evidence_profiles/profiles.json').read_text(encoding='utf-8'))['profiles']
    blocks=json.loads((REF/'manuscript_profiles/source_blocks.json').read_text(encoding='utf-8'))
    bmap={p['paper']:p for p in blocks}
    for label, records in [('manuscript',manuscript),('evidence',evidence)]:
        ids=[p['paper_id'] for p in records]
        check(label+':complete_unique_source_coverage',len(ids)==len(set(ids)) and set(ids)==set(by_id))
        for p in records:
            pid=p['paper_id']; source=by_id[pid]
            check(label+':'+pid+':portable_card',(REF/f'{label}_profiles'/f'{pid}.md').is_file())
            if label=='manuscript':
                check(pid+':exact_profile_source',p['source']['sha256']==source['sha256'] and p['source']['pdf_filename']==source['filename'])
                samples=p['rhetorical_samples']
                check(pid+':source_grounded_rhetoric',bool(samples) and all(1<=s['page']<=source['pdf_pages'] and 0<=s['block']<len(bmap[pid]['pages'][s['page']-1]['blocks']) for s in samples))
                check(pid+':source_specific_blueprint',bool(p.get('blueprint')) and bool(p.get('sections')))
            else:
                pages=p['evidence_pages']+p['reference_pages']+p['visual_reviewed_pages']
                check(pid+':evidence_source_pages',all(1<=n<=source['pdf_pages'] for n in pages))
                check(pid+':experiment_protocol_and_boundary',all(p.get(k) for k in ('experiment_order','controls_and_sampling','transfer_boundary','citation_profile')))
    for p in papers:
        pdf=ROOT/'papers/preferred_29'/p['filename']
        check(p['paper']+':bundled_source_hash',pdf.is_file() and hashlib.sha256(pdf.read_bytes()).hexdigest()==p['sha256'])
    anchors=json.loads((REF/'framework_anchors/anchors.json').read_text(encoding='utf-8'))
    check('anchors:unique_anchor_ids',len({a['anchor_id'] for a in anchors})==len(anchors))
    for a in anchors:
        check(a['anchor_id']+':actual_crop_and_card',(ROOT/a['crop_path']).is_file() and (ROOT/a['card_path']).is_file() and a['artifact_kind']=='SOURCE_FAITHFUL_CROP')
        check(a['anchor_id']+':crop_identity',hashlib.sha256((ROOT/a['crop_path']).read_bytes()).hexdigest()==a['crop_sha256'])
    r=select_references('意图 预测 tracking',limit=1)
    check('retrieval:intention_predictor_not_generic_framework',r['paper_candidates'][0]['paper_id']=='R06' and r['framework_candidates'][0]['anchor_id']=='R06-F2')
    # These contrasts vary the explanatory purpose, not just the broad topic.
    # They guard against flattening all transfer warnings into search evidence
    # or reusing one measured anchor for every tracking/RL manuscript.
    purpose_queries=[
        ('asymmetric_training_deployment','asymmetric actor critic training deployment HOCBF','R25-F1'),
        ('domain_gradient_paths','asymmetric actor critic training domain adversarial gradient reversal sim real CNN GRU','R23-F3'),
        ('module_interfaces','onboard sensors local map controller tracking planner','R01-F2'),
        ('intention_prediction_mechanism','onboard sensors local map controller tracking planner intention future prediction visibility','R06-F2'),
        ('hierarchical_policy_planner','hierarchical learned agility policy trajectory planner speed weight','R12-F2'),
        ('reset_distribution_rewards','biased reset sampling reward training distribution','R20-F2'),
        ('hardware_software_dynamics','robot hardware software dynamics forces multipanel','R29-F2'),
        ('software_functional_bands','software task planning control actuation estimation horizontal bands','R29-F2-software'),
    ]
    for name, query, expected in purpose_queries:
        r=select_references(query,limit=3)
        actual=r['framework_candidates'][0]['anchor_id'] if r['framework_candidates'] else None
        check('retrieval:purpose:'+name,actual==expected,{'expected':expected,'actual':actual})
        check('retrieval:purpose:'+name+':explainable_candidate',
              all(a['inspection_required'] and a['figure_purpose'] and 'purpose_combinations' in a['score_breakdown'] for a in r['framework_candidates']) and r['status']=='CANDIDATES_REQUIRE_INSPECTION')
    r=select_references('非对称 actor critic 训练 部署 HOCBF',limit=1)
    check('retrieval:bilingual_training_deployment',r['framework_candidates'][0]['anchor_id']=='R25-F1')
    r=select_references('无人机',article_form='LETTER',paper_id='R22',framework_id='R29-F2-software',limit=1)
    check('retrieval:explicit_reference_preserved',r['paper_candidates'][0]['paper_id']=='R22' and r['framework_candidates'][0]['anchor_id']=='R29-F2-software')
    r=select_references('外环强化学习 动态速度 轨迹权重',article_form='LETTER',paper_id='R12',limit=1)
    check('retrieval:hierarchical_letter_uses_its_own_framework',r['framework_candidates'][0]['anchor_id']=='R12-F2' and r['main_paper_framework_sources'][0]['case_id']=='R12-F2')
    check('retrieval:no_forced_unknown_match',select_references('xyz_nonexistent_relationship')['status']=='NO_MATCHING_REFERENCE')
    r=select_references('xyz_nonexistent_relationship',article_form='LETTER')
    check('retrieval:article_form_alone_does_not_select_framework',bool(r['paper_candidates']) and not r['framework_candidates'])
    r=select_references('onboard sensors local map controller tracking planner',framework_id='R06-F2',limit=1)
    check('retrieval:explicit_framework_beats_purpose_ranking',r['framework_candidates'][0]['anchor_id']=='R06-F2')
    try:
        select_references('test',paper_id='R99')
        unknown_rejected=False
    except ValueError:
        unknown_rejected=True
    check('retrieval:invalid_source_id_rejected',unknown_rejected)
    result={'status':'PASS' if all(c['passed'] for c in checks) else 'FAIL','checks':checks,'papers':len(papers),'manuscript_profiles':len(manuscript),'evidence_profiles':len(evidence),'actual_framework_crops':len(anchors),'scope':'Source identity, coverage, locator and retrieval checks. Does not certify aesthetic fidelity or correctness of all scientific interpretations.'}
    return result

if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    result=validate()
    (ROOT/'validation/REFERENCE_MATCH_VALIDATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=False))
    for c in result['checks']:
        if not c['passed']: print('FAIL',c['check'],c['detail'])
    raise SystemExit(result['status']!='PASS')
