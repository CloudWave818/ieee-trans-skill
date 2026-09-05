#!/usr/bin/env python3
"""Check provenance, retrieval and editable artifacts; not scientific/visual certification."""
import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from query_visual_cases import query_preferred

ROOT=Path(__file__).resolve().parents[1]


def validate(local=False):
    folder=ROOT/'references/preferred_29'
    cases=json.loads((folder/'cases.json').read_text(encoding='utf-8'))
    papers=json.loads((folder/'papers.json').read_text(encoding='utf-8'))
    keys=json.loads((folder/'key_designs.json').read_text(encoding='utf-8'))
    checks=[]
    def check(name,ok):checks.append({'check':name,'passed':bool(ok)})
    check('unique_figures',len(cases)==len({c['case_id'] for c in cases}))
    check('paper_coverage',{p['paper'] for p in papers}=={c['paper_id'] for c in cases})
    check('key_figures_exist',all(k['case_id'] in {c['case_id'] for c in cases} for k in keys))
    check('separate_supplementary_numbering',{'R09-FS1','R09-FS2','R09-FS3'}.issubset({c['case_id'] for c in cases}))
    check('not_inventing_unlocated_figures','R07-F2' not in {c['case_id'] for c in cases})
    for p in papers:
        group=[c for c in cases if c['paper_id']==p['paper']]
        check(p['paper']+':declared_count',len(group)==p['reviewed_figures'])
        check(p['paper']+':page_bounds',all(1<=c['pdf_page']<=p['pdf_pages'] for c in group))
        if local:
            pdf=ROOT.parent/'范本pdf'/p['filename']
            check(p['paper']+':pdf_digest',pdf.is_file() and hashlib.sha256(pdf.read_bytes()).hexdigest()==p['sha256'])
    for c in cases:
        check(c['case_id']+':card',(ROOT/c['card']).is_file())
        check(c['case_id']+':content',all(c.get(k) for k in ['observed','purpose','transfer','review_scope','source_sha256']))
        if local:
            check(c['case_id']+':local_source',all((folder/c[k]).is_file() for k in ['page_image_relative','context_relative']))
    for path in list((folder/'sketches').glob('*.svg'))+list((ROOT/'examples/preferred_uav_rl').glob('*.svg')):
        try:
            doc=ET.parse(path).getroot()
            ok=doc.tag.endswith('svg') and bool(doc.attrib.get('viewBox'))
        except ET.ParseError:ok=False
        check(path.name+':editable_xml',ok)
    check('no_forced_match',query_preferred(cases,'xyz_nonexistent_relationship')==[])
    check('unreviewed_renders_not_promoted',query_preferred([dict(c,review_status='RENDERED_NOT_REVIEWED') for c in cases],'safety training')==[])
    matches=query_preferred(cases,'safety training',3)
    check('safety_learning_retrieval',matches and matches[0]['case_id']=='R25-F2')
    direct=query_preferred(cases,'R05-F4',1)
    check('exact_case_locator',direct and direct[0]['case_id']=='R05-F4')
    check('zero_shot_not_labeled_RL',all(p['learning_type']=='ZERO_SHOT_NOT_RL' for p in papers if p['paper'] in ['R24','R26','R28']))
    check('neural_estimation_not_labeled_RL',next(p for p in papers if p['paper']=='R22')['learning_type']=='SUPERVISED_NOT_RL')
    rl=query_preferred(cases,'rl training',5)
    check('RL_query_excludes_frozen_and_supervised_models',all(next(c for c in cases if c['case_id']==r['case_id'])['learning_type'].startswith('RL_') for r in rl))
    return {'status':'PASS' if all(c['passed'] for c in checks) else 'FAIL','papers':len(papers),
            'pages':sum(p['pdf_pages'] for p in papers),'figure_notes':len(cases),'key_designs':len(keys),
            'scope':'Provenance, coverage, query behavior and XML only; not drawing quality or scientific certification.',
            'checks':checks}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--local-sources',action='store_true');parser.add_argument('--output',type=Path)
    args=parser.parse_args();result=validate(args.local_sources)
    if args.output:args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
    for c in result['checks']:
        if not c['passed']:print('FAIL',c['check'])
    raise SystemExit(result['status']!='PASS')
