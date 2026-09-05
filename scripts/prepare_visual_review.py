#!/usr/bin/env python3
"""Render selected local source pages and collect context; never certify visual review."""
import argparse
import csv
import hashlib
import json
import shutil
import subprocess
from pathlib import Path


def prepare(mapping, selection, output, corpus_root=None):
    import fitz
    papers = {r['Paper_ID']: r for r in csv.DictReader(mapping.open(encoding='utf-8-sig'))}
    output.mkdir(parents=True, exist_ok=True)
    records = []
    renderer = shutil.which('pdftoppm')
    if not renderer:
        raise RuntimeError('pdftoppm is required for source-page rendering')
    for item in selection:
        paper = papers[item['paper_id']]
        pdf = Path(paper['Local_PDF_path'])
        if corpus_root is not None:
            matches = list(corpus_root.rglob(pdf.name))
            # Prefer the original papers layout over CORE/EXTENDED duplicate copies.
            preferred = [p for p in matches if 'papers' in p.parts]
            matches = preferred or matches
            if len(matches) != 1:
                raise ValueError(f'Ambiguous or missing source: {pdf.name}')
            pdf = matches[0]
        if not pdf.is_file():
            raise FileNotFoundError(pdf)
        page = int(item['pdf_page'])
        stem = f"{item['paper_id']}_p{page:02}"
        with fitz.open(pdf) as doc:
            if not 1 <= page <= len(doc):
                raise ValueError(f'Page out of range: {stem}')
            context = '\n\n'.join(f'--- PDF PAGE {i+1} ---\n'+doc[i].get_text()
                                   for i in range(max(0, page-2), min(len(doc), page+1)))
        context_path = output / f'{stem}_context.txt'
        context_path.write_text(context, encoding='utf-8')
        subprocess.run([renderer, '-f', str(page), '-l', str(page), '-singlefile',
                        '-r', '125', '-png', str(pdf), str(output/stem)], check=True,
                       capture_output=True)
        records.append({**item, 'doi': paper['DOI'], 'title': paper['Title'],
                        'corpus_role': paper['Corpus_role'], 'source_pdf': str(pdf.resolve()),
                        'source_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
                        'page_image': str((output/f'{stem}.png').resolve()),
                        'context_file': str(context_path.resolve()),
                        'status': 'RENDERED_NOT_REVIEWED'})
    (output/'render_manifest.json').write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
    return records


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mapping', type=Path, required=True)
    parser.add_argument('--selection', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--corpus-root', type=Path)
    args = parser.parse_args()
    records = prepare(args.mapping, json.loads(args.selection.read_text(encoding='utf-8')),
                      args.output, args.corpus_root)
    print(f'{len(records)} pages rendered; zero automatically reviewed.')
