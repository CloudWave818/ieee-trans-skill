#!/usr/bin/env python3
"""Inventory a user-selected PDF collection and render it for actual review.

Caption candidates are not confirmed figures. This script never marks inspection complete.
"""
import argparse
import concurrent.futures
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path


def prepare(source, output, workers=3):
    import fitz
    renderer=shutil.which('pdftoppm')
    if not renderer: raise RuntimeError('pdftoppm is required')
    output.mkdir(parents=True,exist_ok=True)
    papers=[]
    cap=re.compile(r'^(?:Fig(?:ure)?\.?)[ \n]*(S?\d+)[.:\s]',re.I)
    for n,path in enumerate(sorted(source.glob('*.pdf')),1):
        pid=f'R{n:02d}'
        folder=output/pid;folder.mkdir(exist_ok=True)
        page_records=[];full=[]
        with fitz.open(path) as doc:
            for i,page in enumerate(doc):
                text=page.get_text(sort=True)
                (folder/f'p{i+1:02}.txt').write_text(text,encoding='utf-8')
                full.append(f'\n--- PDF PAGE {i+1} ---\n{text}')
                candidates=[]
                for b in page.get_text('blocks'):
                    if b[6]!=0: continue
                    block=b[4].strip();m=cap.match(block)
                    if m:
                        candidates.append({'figure':m.group(1),'text':block,
                                           'bbox':list(b[:4]),'status':'CAPTION_CANDIDATE'})
                page_records.append({'page':i+1,'caption_candidates':candidates,
                                     'image':f'{pid}/page-{i+1:02}.png',
                                     'status':'RENDERED_NOT_REVIEWED'})
            record={'paper_id':pid,'filename':path.name,'source_pdf':str(path.resolve()),
                    'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                    'pdf_pages':len(doc),'first_page_text':doc[0].get_text(sort=True),
                    'pages':page_records,'source_set':'USER_PREFERRED_29'}
        (folder/'fulltext.txt').write_text(''.join(full),encoding='utf-8')
        (folder/'candidates.json').write_text(json.dumps(page_records,ensure_ascii=False,indent=2),encoding='utf-8')
        papers.append(record)
    def render(record):
        folder=output/record['paper_id']
        subprocess.run([renderer,'-r','110','-png',record['source_pdf'],str(folder/'page')],capture_output=True,check=True)
        # Poppler uses one digit for documents with fewer than ten pages.
        for p in list(folder.glob('page-*.png')):
            target=folder/f"page-{int(p.stem.split('-')[-1]):02}.png"
            if p!=target:p.rename(target)
        return record['paper_id']
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        for pid in pool.map(render,papers):print(pid,'rendered',flush=True)
    (output/'manifest.json').write_text(json.dumps(papers,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'{len(papers)} papers, {sum(p["pdf_pages"] for p in papers)} pages. None automatically reviewed.')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();prepare(args.source,args.output)
