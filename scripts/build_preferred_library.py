#!/usr/bin/env python3
"""Publish manually reviewed preferred-paper notes; never infer review from rendering.

Rendered pages/context stay in a local library; source PDFs are in papers/preferred_29.
Rebuild after editing review_notes.tsv, papers.tsv or key_designs.json.
"""
import argparse
import csv
import hashlib
import html
import json
import os
from pathlib import Path
from textwrap import wrap

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / 'references/preferred_29'
COLORS = {'blue':'#E3F0FC','green':'#E5F2E3','pink':'#F8E4EC','peach':'#FBE8D5',
          'purple':'#ECE5F7','yellow':'#FFF3CC','gray':'#F0F1F3','photo':'#EDF0F2',
          'spatial':'#F4F8FC','axis':'#FFFFFF'}


def tsv(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def rel(path, folder):
    return os.path.relpath(path, folder).replace('\\', '/')


def sketch(key):
    """Editable empty layout; all text comes from a manually written key case."""
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 640" width="180mm" height="115.2mm">',
           '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#38434B"/></marker></defs>',
           '<rect width="1000" height="640" fill="white"/>',
           '<g font-family="Arial, sans-serif" fill="#26343E">']
    for x,y,w,h,label,kind in key['zones']:
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{COLORS[kind]}" stroke="#687681" stroke-width="1.8"/>')
        lines=wrap(label,width=max(8,int(w/11)))
        for i,line in enumerate(lines):
            out.append(f'<text x="{x+w/2}" y="{y+24+25*i}" text-anchor="middle" font-size="20">{html.escape(line)}</text>')
        if kind=='axis':
            out.append(f'<path d="M{x+30},{y+h-25} H{x+w-20} M{x+30},{y+h-25} V{y+min(85,h/2)}" fill="none" stroke="#495760" stroke-width="2"/>')
        elif kind=='photo':
            out.append(f'<path d="M{x+15},{y+h-18} l{w/4},-20 l{w/5},16 l{w/4},-27" fill="none" stroke="#A8B1B8" stroke-width="2"/>')
    for edge in key['edges']:
        x1,y1,x2,y2,label,*style=edge
        dash=' stroke-dasharray="7 5"' if style and style[0]=='dashed' else ''
        out.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#38434B" stroke-width="2" fill="none" marker-end="url(#arrow)"{dash}/>')
        # White halo keeps labels legible; placement is checked in rendered previews.
        position=f'x="{(x1+x2)/2}" y="{(y1+y2)/2-8}" text-anchor="middle" font-size="17"'
        out.append(f'<text {position} fill="none" stroke="white" stroke-width="5">{html.escape(label)}</text>')
        out.append(f'<text {position} fill="#26343E">{html.escape(label)}</text>')
    out.append(f'<text x="30" y="623" font-size="18">{key["case_id"]} | layout study only • no source image or measured curve reconstructed</text></g></svg>')
    return '\n'.join(out)


def build(library):
    manifest=json.loads((library/'source_pages/manifest.json').read_text(encoding='utf-8'))
    sources={p['paper_id']:p for p in manifest}
    # IDs came from this exact inventory. Adding/reordering PDFs must not transfer
    # old human-authored AI review notes silently to a different source version.
    prior_index=REF/'papers.json'
    if prior_index.is_file():
        prior=json.loads(prior_index.read_text(encoding='utf-8'))
        for p in prior:
            current=sources.get(p['paper'])
            if not current or (current['filename'],current['sha256']) != (p['filename'],p['sha256']):
                raise ValueError(f'Source identity changed for {p["paper"]}; reconcile/review notes before rebuilding')
    papers=tsv(REF/'papers.tsv')
    meta={p['paper']:p for p in papers}
    keys={k['case_id']:k for k in json.loads((REF/'key_designs.json').read_text(encoding='utf-8'))}
    cards=REF/'cards';cards.mkdir(exist_ok=True)
    sketches=REF/'sketches';sketches.mkdir(exist_ok=True)
    for key in keys.values():
        (sketches/f'{key["case_id"]}.svg').write_text(sketch(key),encoding='utf-8')
    records=[];seen=set()
    for row in tsv(REF/'review_notes.tsv'):
        pid=row['paper'];num=row['figure'];page=int(row['page']);cid=f'{pid}-F{num}'
        if cid in seen:raise ValueError(f'Duplicate review: {cid}')
        seen.add(cid)
        source=sources[pid];paper=meta[pid]
        if not 1<=page<=source['pdf_pages']:raise ValueError(f'Invalid page: {cid}')
        image=library/'source_pages'/pid/f'page-{page:02}.png'
        context=library/'source_pages'/pid/f'p{page:02}.txt'
        if not image.is_file() or not context.is_file():raise FileNotFoundError(cid)
        # A matched text block is supplementary retrieval help, not verified transcription.
        candidates=[c['text'] for c in source['pages'][page-1]['caption_candidates']
                    if c['figure']==num.removeprefix('S')]
        rec={'case_id':cid,'paper_id':pid,'figure':num,'pdf_page':page,
             'title':paper['title'],'filename':source['filename'],'source_sha256':source['sha256'],
             'source_pdf':f'papers/preferred_29/{source["filename"]}',
             'source_set':'USER_PREFERRED_29','learning_type':paper['learning_type'],
             'tags':paper['tags'].split(),'paper_story':paper['paper_story'],
             'observed':row['panels_and_encoding'],'purpose':row['purpose_and_context'],
             'transfer':row['transfer_and_boundary'],
             'review_status':'VISUAL_AND_CONTEXT_REVIEWED',
             'review_scope':'AI page-level visual/caption/context reading; not every small axis label transcribed',
             'detail_level':'KEY_DESIGN_REVIEW' if cid in keys else 'FIGURE_READING_NOTE',
             'review_date':'2026-09-05','reviewer':'Codex AI; not human verification',
             'caption_candidates':candidates,'caption_text_status':'AUTOMATIC_BLOCK_MATCH_NOT_VERBATIM_VERIFIED',
             'card':f'references/preferred_29/cards/{cid}.md',
             'page_image_relative':rel(image,REF),'context_relative':rel(context,REF)}
        if cid in keys:
            rec['design']=keys[cid]
            rec['sketch']=f'references/preferred_29/sketches/{cid}.svg'
        records.append(rec)
        lines=[f'# {cid} · {paper["title"]}', '',
               f'- 原 PDF：`{source["filename"]}`；Fig. {num}；PDF 第 {page} 页（从 1 计，与刊印页码区分）。',
               f'- [仓库原始 PDF]({rel(ROOT/rec["source_pdf"],cards)}#page={page})（可直接下载；下方页面图/正文链接为本地渲染缓存）。',
               f'- 来源：USER_PREFERRED_29；SHA256：`{source["sha256"]}`。',
               f'- 阅读：2026-09-05，Codex AI；{rec["detail_level"]}。已读页面原图、图注及相关上下文；未逐一转录全部小字。',
               f'- [原图所在页]({rel(image,cards)}) · [该页图注与正文]({rel(context,cards)}) · [全文上下文]({rel(context.parent/"fulltext.txt",cards)})',
               '', '## 论文怎样组织图',paper['paper_story'],'','## 图里是什么',rec['observed'],
               '','## 它证明什么',rec['purpose'],'','## 迁移方式及边界',rec['transfer']]
        if cid in keys:
            key=keys[cid]
            for title,field in [('原图布局','observed_layout'),('接口、坐标与曲线','ports_or_axes'),
                                ('机制到证据','mechanism_to_evidence'),('可执行迁移方案','recipe'),
                                ('必须采集什么','data_contract'),('不能照搬什么','boundary')]:
                lines.extend(['',f'## {title}',key[field]])
            lines.extend(['','## 布局草图（分析用，非原图重绘）',f'![{cid} layout](../sketches/{cid}.svg)'])
        lines.extend(['','## 阅读精度','本条是图级人工编写的 AI 阅读记录，不等于所有坐标刻度、统计定义和正文主张都已逐项复核。关键数字与微小图例用于本稿之前，应打开上方原页；不确定信息不得自动补齐。'])
        (cards/f'{cid}.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    if set(meta)!=set(sources) or {r['paper_id'] for r in records}!=set(meta):
        raise ValueError('Paper/source/review coverage mismatch')
    (REF/'cases.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    inventory=[]
    for p in papers:
        src=sources[p['paper']];group=[r for r in records if r['paper_id']==p['paper']]
        inventory.append({**p,'filename':src['filename'],'sha256':src['sha256'],
                          'pdf_pages':src['pdf_pages'],'reviewed_figures':len(group)})
    (REF/'papers.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    index=['# 用户优先范本：29 篇逐图学习库','',
           f'{len(papers)} 篇，{sum(p["pdf_pages"] for p in inventory)} 页，{len(records)} 条逐图记录，{len(keys)} 张关键图的细化方案和 SVG 布局草图。',
           '这不是训练模型权重，而是后续任务可检索、可追溯的项目知识。全部条目是 AI 阅读记录；小字/统计定义未全量转录。原 PDF 随仓库保存在 papers/preferred_29；页面图和提取全文是可重建的本地缓存。',
           '', '[风格与模仿规则](STYLE_PLAYBOOK.md) · [强化学习图组](RL_FIGURE_PLAYBOOK.md)',
           '', '检索：`python scripts/query_visual_cases.py "safety training"`；优先检索本库，无相关匹配再查旧库。',
           '', '|论文|主题/故事|图数|学习类型|','|---|---|---:|---|']
    for p in inventory:
        first=next(r for r in records if r['paper_id']==p['paper'])
        index.append(f'|[{p["paper"]} {p["title"]}](cards/{first["case_id"]}.md)|{p["paper_story"]}|{p["reviewed_figures"]}|{p["learning_type"]}|')
    index.extend(['','## 关键构图'])
    for key in keys.values():index.append(f'- [{key["case_id"]}：{key["focus"]}](cards/{key["case_id"]}.md)')
    index.extend(['','## 全部图索引'])
    for p in inventory:
        group=[r for r in records if r['paper_id']==p['paper']]
        index.append(f'- {p["paper"]}：'+ ' · '.join(f'[{r["figure"]} / p{r["pdf_page"]}](cards/{r["case_id"]}.md)' for r in group))
    (REF/'INDEX.md').write_text('\n'.join(index)+'\n',encoding='utf-8')
    write_gallery(library,inventory,records)
    print(json.dumps({'papers':len(papers),'pages':sum(p['pdf_pages'] for p in inventory),
                      'figure_notes':len(records),'key_designs':len(keys),'gallery':str(library/'index.html')},ensure_ascii=False))


def write_gallery(library,papers,records):
    links=[]
    for p in papers:
        links.append(f'<a href="#paper-{p["paper"]}">{p["paper"]} · {html.escape(p["title"])} <small>{p["reviewed_figures"]} 图</small></a>')
    chunks=[]
    e=html.escape
    for paper in papers:
        pid=paper['paper'];group=[r for r in records if r['paper_id']==pid]
        chunks.append(f'<section id="paper-{pid}"><h2>{pid} · {e(paper["title"])}</h2><p>{e(paper["paper_story"])}</p>')
        for r in group:
            cid=r['case_id'];page=r['pdf_page'];img=f'source_pages/{pid}/page-{page:02}.png'
            tags=' '.join(r['tags'])
            search=e(' '.join([cid,r['title'],tags,r['observed'],r['purpose'],r['learning_type']]))
            chunks.append(f'<article data-search="{search}"><header><h3>{cid} · PDF {page} 页</h3><span>{e(r["detail_level"])}</span></header><div class="card"><a class="source" href="{img}" target="_blank"><img loading="lazy" src="{img}" alt="{cid} 原图所在 PDF 页"></a><div class="notes">')
            chunks.append(f'<p class="tags">{e(tags)}</p><h4>图里是什么</h4><p>{e(r["observed"])}</p><h4>为什么这样组合</h4><p>{e(r["purpose"])}</p><h4>可以怎样迁移</h4><p>{e(r["transfer"])}</p>')
            chunks.append(f'<p><a target="_blank" href="{rel(ROOT/r["source_pdf"],library)}#page={page}">原始 PDF</a> · <a target="_blank" href="source_pages/{pid}/p{page:02}.txt">本页图注与正文</a> · <a target="_blank" href="source_pages/{pid}/fulltext.txt">全文上下文</a> · <a href="{rel(ROOT/r["card"],library)}">详细卡片</a></p>')
            if 'design' in r:
                k=r['design'];chunks.append('<details open><summary>细化方案与布局草图</summary>')
                for label,field in [('原图布局','observed_layout'),('坐标 / 接口','ports_or_axes'),('机制与证据','mechanism_to_evidence'),('迁移方案','recipe'),('数据采集','data_contract'),('边界','boundary')]:
                    chunks.append(f'<h4>{label}</h4><p>{e(k[field])}</p>')
                chunks.append(f'<a href="{rel(ROOT/r["sketch"],library)}"><img class="sketch" loading="lazy" src="{rel(ROOT/r["sketch"],library)}" alt="{cid} 分析草图"></a></details>')
            if r['caption_candidates']:
                chunks.append('<details><summary>自动定位的图注文本块（请对照原图）</summary><pre>'+e('\n\n'.join(r['caption_candidates']))+'</pre></details>')
            chunks.append(f'<small>来源 {e(r["filename"])} · Codex AI 阅读 · 图级记录，微小标注未全部复核。</small></div></div></article>')
        chunks.append('</section>')
    css='''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f3f5f7;color:#263746;font:16px/1.65 "Segoe UI","Microsoft YaHei",sans-serif}aside{position:fixed;top:0;bottom:0;width:265px;overflow:auto;padding:20px;background:#20364a;color:white}aside a{display:block;color:#e6eff7;text-decoration:none;padding:11px 0;border-bottom:1px solid #456}aside small{color:#a8d9e7}main{margin-left:265px;padding:30px;max-width:1800px}h1{font-size:29px}h2{font-size:22px;scroll-margin-top:20px}h3{margin:0}h4{margin:14px 0 3px}p{margin:6px 0 14px}a{color:#176c8b}article{background:white;border:1px solid #d6dee5;border-radius:12px;margin:22px 0;overflow:hidden}article header{display:flex;justify-content:space-between;gap:14px;padding:14px 20px;background:#e8f1f7}header span{font-size:12px;color:#526879}.card{display:grid;grid-template-columns:minmax(300px,43%) 1fr;gap:22px;padding:20px}.source img{width:100%;height:auto;border:1px solid #ddd}.source{align-self:start}.notes{min-width:0}.tags,small{color:#637987;font-size:12px}.sketch{width:100%;margin-top:12px}input{width:min(700px,100%);padding:12px;border:1px solid #aac;border-radius:8px;font:inherit}details{border-top:1px solid #ddd;padding-top:10px;margin-top:15px}summary{cursor:pointer;color:#24617c}pre{white-space:pre-wrap;font:12px/1.7 sans-serif}.banner{padding:18px;background:#fff7dc;border-left:4px solid #bd9a32}.hidden{display:none!important}@media(max-width:1000px){aside{display:none}main{margin-left:0;padding:16px}.card{grid-template-columns:1fr}.source img{max-width:650px}}'''
    js='''const q=document.querySelector('#q'), count=document.querySelector('#count');q.addEventListener('input',()=>{const terms=q.value.toLowerCase().trim().split(/\\s+/).filter(Boolean);let n=0;document.querySelectorAll('article').forEach(a=>{const ok=terms.every(t=>a.dataset.search.toLowerCase().includes(t));a.classList.toggle('hidden',!ok);n+=ok;});document.querySelectorAll('section').forEach(s=>s.classList.toggle('hidden',!s.querySelector('article:not(.hidden)')));count.textContent=n+' 张匹配图';});'''
    output=f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>29 篇无人机范本 · 逐图学习库</title><style>{css}</style><aside><b>29 篇优先范本</b>{''.join(links)}</aside><main><h1>从原图学会“这张图怎样讲清方法”</h1><p>29 篇 · 337 页 · {len(records)} 条图级记录 · {sum("design" in r for r in records)} 张关键图细化方案</p><p class="banner">本库优先于旧风格库。原页、图注/正文、阅读结论与迁移方案对应保存。全部是 AI 阅读记录，关键小字和统计定义仍需按具体使用复核；不是对所有曲线数值的认证。</p><p><a href="{rel(REF/'STYLE_PLAYBOOK.md',library)}">风格与模仿规则</a> · <a href="{rel(REF/'RL_FIGURE_PLAYBOOK.md',library)}">强化学习图组</a> · <a href="{rel(ROOT/'examples/preferred_uav_rl/PAPER_FIGURE_DESCRIPTION.md',library)}">题目驱动作图示例</a></p><input id="q" type="search" placeholder="筛选：training、安全、编队、R25-F1…"><p id="count">{len(records)} 张图</p>{''.join(chunks)}</main><script>{js}</script></html>'''
    output=output.replace('</script>', "document.querySelectorAll('aside a').forEach(a=>a.addEventListener('click',()=>{q.value='';q.dispatchEvent(new Event('input'));}));</script>")
    (library/'index.html').write_text(output,encoding='utf-8')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--library',type=Path,default=ROOT.parent/'USER_PREFERRED_VISUAL_LIBRARY')
    args=parser.parse_args();build(args.library.resolve())
