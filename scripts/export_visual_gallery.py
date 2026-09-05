#!/usr/bin/env python3
"""Build a local case viewer without copying source images into the skill."""
import argparse
import html
import json
import os
from pathlib import Path
from urllib.parse import quote


def export(output):
    folder=Path(__file__).resolve().parents[1]/'references/visual_cases'
    cases=json.loads((folder/'cases.json').read_text(encoding='utf-8'))
    output.mkdir(parents=True,exist_ok=True)
    def link(path): return quote(os.path.relpath(path,output).replace('\\','/'),safe='/.:')
    e=html.escape
    count=sum(len(c['panels']) for c in cases)
    head='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>IEEE 原图视觉案例库</title><style>body{margin:0;background:#f3f5f7;color:#172a3a;font:16px/1.8 system-ui,"Microsoft YaHei",sans-serif}main{max-width:1150px;margin:auto;padding:36px}h1{font-size:32px;line-height:1.3}header{padding:26px;background:#132d44;color:white;border-radius:16px}input{font:inherit;width:90%;padding:12px;margin:24px 0;border:1px solid #9baab8;border-radius:8px}article{background:white;border-radius:14px;padding:24px;margin-bottom:24px;box-shadow:0 3px 16px #1231}.grid{display:grid;grid-template-columns:38% 1fr;gap:28px}img{width:100%;border:1px solid #ddd}h2{margin-top:0;font-size:22px}h3{font-size:16px;color:#176a78;margin-bottom:3px}p{margin:6px 0 15px}a{color:#176a78}pre{white-space:pre-wrap;background:#eef3f7;padding:14px;font:14px/1.6 monospace}.meta{color:#54687b;font-size:14px}.warning{border-left:4px solid #c37f29;padding-left:12px}@media(max-width:750px){.grid{grid-template-columns:1fr}main{padding:16px}}</style><main><header><h1>从原图学画法</h1>'''
    parts=[head,f'<p>{len({c["p"] for c in cases})}篇论文 · {count}张指定图 · {len(cases)}个图组案例</p><p>已结合原页、图注与正文进行AI视觉检查；并非全文逐图精读。每个案例区分观察、局限与新的迁移设计。</p></header>',
           '<input id="q" placeholder="检索：扰动 / 机制 / safety / hardware / uncertainty …" aria-label="检索案例"><div id="items">']
    for c in cases:
        image=(folder/c['page_image_relative']).resolve()
        context=(folder/c['context_relative']).resolve()
        search=e(' '.join([c['title'],*c['tags'],c['p'],c['purpose']]))
        part=f'<article data-search="{search}"><h2>{e(c["case_id"]+" · "+c["title"])}</h2><p class="meta">Fig. {e(", ".join(c["panels"]))} · PDF p.{c["pdf_page"]} · <a href="https://doi.org/{e(c["doi"])}">DOI</a> · <a href="{link(context)}">本地邻页正文</a> · <a href="{link(folder/(c["case_id"]+".md"))}">案例文件</a></p><div class="grid">'
        if image.is_file():
            part+=f'<a href="{link(image)}"><img loading="lazy" src="{link(image)}" alt="{e(c["p"])}原论文第{c["pdf_page"]}页"></a>'
        else:
            part+='<p class="warning">本地原页不可用；当前仅能读取历史AI检查记录。请从已标识的本地PDF重建后复查。</p>'
        part+='<div>'
        for title,field in [('看到了什么','observed'),('图注和正文解释','purpose'),('不可照搬 / 尚未确认','boundary'),('本稿怎样迁移（设计判断）','transfer'),('实验前保存什么','collect')]:
            part+=f'<h3>{title}</h3><p class="{"warning" if field=="boundary" else ""}">{e(c[field])}</p>'
        parts.append(part+f'<h3>迁移布局草图</h3><pre>{e(c["sketch"])}</pre><p class="meta">正文定位：{e(c["context"])}</p></div></div></article>')
    parts.append('''</div><p>状态：VISUAL_AND_CONTEXT_REVIEWED（Codex AI，2026-09-05）。这不是独立人工复核或新手稿作图质量认证。原页仅保存在本地研究工作区。</p></main><script>document.getElementById('q').addEventListener('input',e=>{const q=e.target.value.toLowerCase();document.querySelectorAll('article').forEach(a=>a.hidden=!a.dataset.search.toLowerCase().includes(q))})</script></html>''')
    target=output/'index.html'
    target.write_text(''.join(parts),encoding='utf-8')
    return target


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,required=True)
    print(export(parser.parse_args().output_dir.resolve()))
