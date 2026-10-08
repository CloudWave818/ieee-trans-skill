#!/usr/bin/env python3
"""Verify scene-library source identities, inspected-page scope and figure locators.

This checks provenance and packaging, not experiment completion or visual quality.
Requires PyMuPDF, like the existing source-reading tooling.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re

import pymupdf

ROOT = Path(__file__).resolve().parents[1]


def figure_numbers(label):
    match = re.search(r'Fig(?:ure)?\.?\s*(\d+)(.*)', label, re.I)
    if not match:
        return []
    first, rest = int(match.group(1)), match.group(2)
    end = re.match(r'\s*[–−-]\s*(\d+)', rest)
    if end:
        return list(range(first, int(end.group(1)) + 1))
    return [first] + [int(n) for n in re.findall(r'/\s*(\d+)', rest)]


def validate():
    library = ROOT / 'references/preferred_29/real_world_scenes'
    data = json.loads((library / 'cases.json').read_text(encoding='utf-8'))
    metadata = {p['paper']: p for p in json.loads((ROOT / 'references/preferred_29/papers.json').read_text(encoding='utf-8'))}
    checks = []

    def check(name, ok, detail=''):
        checks.append({'check': name, 'passed': bool(ok), 'detail': detail})

    records = data['papers']
    check('complete_unique_preferred_29', len(records) == len(metadata) == len({p['paper_id'] for p in records}) and {p['paper_id'] for p in records} == set(metadata))
    for field, value in {
        'papers_count': len(records), 'scenes_count': sum(len(p['scenes']) for p in records),
        'showcase_count': sum(len(p['showcases']) for p in records),
        'reviewed_page_count': sum(len(p['reviewed_pdf_pages']) for p in records),
    }.items():
        check(field + ':matches_records', data[field] == value)
    ids = [s['scene_case_id'] for p in records for s in p['showcases']]
    check('unique_showcase_ids', len(ids) == len(set(ids)))
    for p in records:
        pid = p['paper_id']; meta = metadata[pid]
        path = ROOT / p['source_pdf_relative']
        check(pid + ':portable_source_path', not Path(p['source_pdf_relative']).is_absolute() and path.resolve().is_relative_to(ROOT.resolve()))
        check(pid + ':exact_bundled_source', path.is_file() and p['filename'] == meta['filename'] and hashlib.sha256(path.read_bytes()).hexdigest() == p['source_sha256'] == meta['sha256'])
        check(pid + ':classification_and_scene_content', isinstance(p['execution_classification'], dict) and isinstance(p['execution_classification'].get('category'), str) and bool(p['scenes']) and bool(p['source_observations']))
        with pymupdf.open(path) as doc:
            check(pid + ':source_page_count', len(doc) == p['pdf_page_count'] == meta['pdf_pages'])
            reviewed = p['reviewed_pdf_pages']
            check(pid + ':reviewed_pages_valid', bool(reviewed) and len(reviewed) == len(set(reviewed)) and all(isinstance(n, int) and 1 <= n <= len(doc) for n in reviewed))
            for s in p['showcases']:
                sid = s['scene_case_id']; pages = s['pdf_pages']
                valid = bool(pages) and all(isinstance(n, int) and n in reviewed and 1 <= n <= len(doc) for n in pages)
                check(sid + ':locator_in_inspected_scope', valid)
                nums = figure_numbers(s['figure'])
                text = ' '.join(doc[n-1].get_text() for n in pages) if valid else ''
                # Confirms that the specified figure label occurs on the supplied
                # page(s); this is not an automated caption/content adjudication.
                check(sid + ':figure_label_on_source_pages', bool(nums) and all(re.search(r'Fig(?:ure)?\.?\s*' + str(n) + r'(?=\D|$)', text, re.I) for n in nums), {'label': s['figure'], 'pages': pages})
                check(sid + ':source_observation_content', bool(s['observations']))
                check(sid + ':normalized_handoff_fields', all(s['observations'].get(k) for k in ('visual_material', 'composition', 'temporal_identity', 'transfer_note')))
    serialized = json.dumps(data, ensure_ascii=False)
    check('no_private_review_cache_paths', 'real_scene_audit_20261008' not in serialized and not re.search(r'[A-Z]:[/\\]', serialized))
    return {'status': 'PASS' if all(c['passed'] for c in checks) else 'FAIL',
            'scope': 'Source identities, coverage, inspected-page scope and figure-label locators; no certification of experiment or image quality.',
            'papers': len(records), 'scenes': data['scenes_count'], 'showcases': len(ids), 'reviewed_pdf_pages': data['reviewed_page_count'], 'checks': checks}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = validate()
    if args.output:
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'checks'}, ensure_ascii=False))
    for c in result['checks']:
        if not c['passed']:
            print('FAIL', c['check'], c['detail'])
    raise SystemExit(0 if result['status'] == 'PASS' else 1)
