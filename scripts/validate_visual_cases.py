#!/usr/bin/env python3
"""Check case provenance/coverage and retrieval behavior, not visual quality."""
import argparse
import hashlib
import json
from pathlib import Path
from query_visual_cases import query


def validate(local=False):
    root=Path(__file__).resolve().parents[1]
    folder=root/'references/visual_cases'
    cases=json.loads((folder/'cases.json').read_text(encoding='utf-8'))
    selected=json.loads((folder/'selection.json').read_text(encoding='utf-8'))
    scope={(r['paper_id'],str(f),r['pdf_page']) for r in selected for f in r['figures']}
    checks=[]
    def check(name, passed): checks.append({'check':name,'passed':bool(passed)})
    ids=[c['case_id'] for c in cases]
    check('unique_case_ids',len(ids)==len(set(ids)))
    check('declared_a_level_sample',all(c.get('corpus_role')=='A' and c.get('journal') and c.get('corpus_layer') in {'CORE','EXTENDED'} for c in cases))
    reviewed={(c['p'],f,c['pdf_page']) for c in cases for f in c['panels']}
    check('exact_selected_figure_scope',reviewed==scope)
    for c in cases:
        check(c['case_id']+':source_locator',bool(c['doi']) and len(c['source_sha256'])==64 and c['pdf_page']>0)
        check(c['case_id']+':card_exists',(folder/(c['case_id']+'.md')).is_file())
        check(c['case_id']+':review_content',all(c.get(k) for k in ['observed','context','purpose','boundary','transfer','collect','sketch','reviewer']))
        check(c['case_id']+':positive_panel_counts',all(type(n)==int and n>0 for n in c['panels'].values()))
        if local:
            for field in ['page_image_relative','context_relative']:
                check(c['case_id']+':'+field,(folder/c[field]).is_file())
            sources=list((root.parent/'IEEE_TRANS_CORPUS/papers').rglob(c['source_pdf_name']))
            check(c['case_id']+':source_digest',len(sources)==1 and hashlib.sha256(sources[0].read_bytes()).hexdigest()==c['source_sha256'])
    check('unknown_relationship_no_forced_match',query(cases,'zz_no_matching_relationship_zz')==[])
    altered=[dict(c,review_status='RENDERED_NOT_REVIEWED') for c in cases]
    check('renders_not_promoted_to_inspected_references',query(altered,'control safety')==[])
    check('retrieval_respects_limit',len(query(cases,'control safety mechanism',2))==2)
    robust=query(cases,'robust_rl',1)
    check('robust_action_case_retrievable',bool(robust) and robust[0]['case_id']=='VC-P077')
    return {'status':'PASS' if all(c['passed'] for c in checks) else 'FAIL',
            'scope':'Provenance, selected coverage and retrieval behavior only; not drawing quality.',
            'papers':len({c['p'] for c in cases}),'cases':len(cases),'figures':len(reviewed),
            'checks':checks}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--local-sources',action='store_true')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=validate(args.local_sources)
    if args.output:
        args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=False))
    for c in result['checks']:
        if not c['passed']: print('FAIL',c['check'])
    raise SystemExit(0 if result['status']=='PASS' else 1)
