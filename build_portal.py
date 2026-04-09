#!/usr/bin/env python3
"""Build WoW Portal — pre-rendered HTML, zero f-strings in template."""

import json, os, re, html as html_mod
from markdown_it import MarkdownIt

V2_DIR = "/home/tanmay/Ways of Working/v2"
OUT = "/home/tanmay/Ways of Working/wow-portal.html"

DOCUMENTS = [
    {"id":"executive-summary","file":"WoW_Summary.md","title":"Executive Summary","subtitle":"Quick overview of intent, structure &amp; key concepts","color":"#0f766e","category":"overview"},
    {"id":"master-framework","file":"WoW_Proposed_Approach.md","title":"Master Framework","subtitle":"Architecture, Stages, Gates &amp; RACI","color":"#4f46e5","category":"core"},
    {"id":"solutioning-requirements","file":"Granular_Solutioning_Requirements.md","title":"Solutioning &amp; Requirements","subtitle":"Discovery, Workshops, POC, Client Management","color":"#7c3aed","category":"process"},
    {"id":"eval-datasets","file":"Granular_Eval_Dataset_Lifecycle.md","title":"Evaluation Datasets","subtitle":"Creation, Scoring, CI/CD Integration","color":"#059669","category":"process"},
    {"id":"skills-kb","file":"Granular_Skills_KB_Lifecycle.md","title":"Skills &amp; Knowledge Bases","subtitle":"Lifecycle, Versioning, Auto-Refinement","color":"#d97706","category":"process"},
    {"id":"build-test-deploy","file":"Granular_Build_Test_Deploy.md","title":"Build, Test &amp; Deploy","subtitle":"Code Contribution, Pipeline, Monitoring","color":"#dc2626","category":"process"},
    {"id":"cross-cutting","file":"Granular_Cross_Cutting_Operations.md","title":"Cross-Cutting Operations","subtitle":"Communication, Sprints, Stakeholders, Risk","color":"#0891b2","category":"process"},
    {"id":"upskilling-plan","file":"Upskilling_Plan.md","title":"Upskilling Plan","subtitle":"What every role needs to learn for the WoW to work","color":"#9333ea","category":"enablement"},
]

CAT_LABELS = {"overview":"Start Here","core":"Core Framework","process":"Granular Process Modules","enablement":"Enablement"}
FILE_TO_ID = {d["file"]: d["id"] for d in DOCUMENTS}

# ── Markdown ──
md_renderer = MarkdownIt("commonmark", {"html": True}).enable("table").enable("strikethrough")

def slugify(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    return re.sub(r'-+', '-', text).strip('-')

def render_md(text):
    rendered = md_renderer.render(text)
    # Add IDs to headings
    def heading_replacer(m):
        tag, content = m.group(1), m.group(2)
        return '<%s id="%s">%s</%s>' % (tag, slugify(content), content, tag)
    rendered = re.sub(r'<(h[2-6])>(.*?)</\1>', heading_replacer, rendered)
    # Wrap tables
    rendered = rendered.replace('<table>', '<div class="tw"><table>').replace('</table>', '</table></div>')
    # Fix cross-doc links
    def fix_links(html_str):
        def replacer(m):
            href = m.group(1)
            if href.startswith('./') and '.md' in href:
                fname = href.split('#')[0].replace('./', '')
                if fname in FILE_TO_ID:
                    return 'href="javascript:void(0)" onclick="loadDoc(\'%s\')"' % FILE_TO_ID[fname]
            return m.group(0)
        return re.sub(r'href="([^"]*)"', replacer, html_str)
    rendered = fix_links(rendered)
    return rendered

# ── Build all content ──
doc_html = {}
doc_toc = {}
doc_lines = {}

for doc in DOCUMENTS:
    with open(os.path.join(V2_DIR, doc["file"])) as f:
        raw = f.read()
    doc_lines[doc["id"]] = len(raw.split("\n"))
    doc_html[doc["id"]] = render_md(raw)
    toc = []
    for line in raw.split("\n"):
        if line.startswith("## "):
            text = line[3:].strip()
            toc.append({"t": text[:48], "s": slugify(text), "d": 2})
        elif line.startswith("### "):
            text = line[4:].strip()
            toc.append({"t": text[:46], "s": slugify(text), "d": 3})
    doc_toc[doc["id"]] = toc

# ── Search index ──
search_idx = []
for doc in DOCUMENTS:
    with open(os.path.join(V2_DIR, doc["file"])) as f:
        raw = f.read()
    heading = doc["title"]
    for line in raw.split("\n"):
        if line.startswith("## ") or line.startswith("### "):
            heading = re.sub(r'^#+\s*', '', line)
        if len(line.strip()) > 10:
            search_idx.append({"d": doc["id"], "dt": doc["title"], "h": heading, "t": line})

# ── Build HTML pieces (no f-strings anywhere) ──

# Home cards
home_parts = ['<h1>Ways of Working</h1>',
    '<p>A comprehensive operational framework for the GenAI team. 8 interconnected documents covering the full lifecycle from requirements to production.</p>']
last_cat = ""
for doc in DOCUMENTS:
    if doc["category"] != last_cat:
        if last_cat: home_parts.append('</div>')
        last_cat = doc["category"]
        home_parts.append('<div class="hcat">%s</div><div class="hg">' % CAT_LABELS[doc["category"]])
    home_parts.append(
        '<div class="hc" style="--cc:%s" onclick="loadDoc(\'%s\')">'
        '<div class="hc-dot" style="background:%s"></div>'
        '<h3>%s</h3><p>%s</p>'
        '</div>'
        % (doc["color"], doc["id"], doc["color"], doc["title"], doc["subtitle"])
    )
home_parts.append('</div>')
home_html = "\n".join(home_parts)

# Sidebar nav
nav_parts = []
last_cat = ""
for doc in DOCUMENTS:
    if doc["category"] != last_cat:
        last_cat = doc["category"]
        nav_parts.append('<div class="sc">%s</div>' % CAT_LABELS[doc["category"]])
    nav_parts.append(
        '<div class="si" id="si-%s" onclick="loadDoc(\'%s\')">'
        '<div class="si-dot" style="background:%s"></div>'
        '<div class="si-t"><div class="si-n">%s</div>'
        '<div class="si-s">%s</div></div></div>'
        % (doc["id"], doc["id"], doc["color"], doc["title"], doc["subtitle"])
    )
    nav_parts.append('<div class="st" id="st-%s">' % doc["id"])
    for entry in doc_toc[doc["id"]]:
        cls = "d3" if entry["d"] == 3 else ""
        t = html_mod.escape(entry["t"])
        nav_parts.append('<a class="%s" data-s="%s" onclick="scrollH(\'%s\')">%s</a>' % (cls, entry["s"], entry["s"], t))
    nav_parts.append('</div>')
nav_html = "\n".join(nav_parts)

# Doc views
dv_parts = []
for doc in DOCUMENTS:
    cat = CAT_LABELS[doc["category"]]
    dv_parts.append(
        '<div class="dv" id="dv-%s">'
        '<div class="dt">'
        '<button class="dt-b" onclick="goHome()">&#8592; All Documents</button>'
        '<span class="dt-c">%s &rsaquo; <b>%s</b></span>'
        '</div>'
        '<div class="db"><div class="dh">'
        '<div class="dh-badge" style="background:%s18;color:%s">%s</div>'
        '<h1>%s</h1>'
        '<div class="dh-sub">%s</div>'
        '<div class="dh-m"><span>April 2026</span></div>'
        '</div><div class="prose">%s</div></div></div>'
        % (doc["id"], cat, doc["title"], doc["color"], doc["color"], cat,
           doc["title"], doc["subtitle"], doc_html[doc["id"]])
    )
dv_html = "\n".join(dv_parts)

# ── Write final HTML using a plain template with markers ──
TEMPLATE = r'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ways of Working &mdash; GenAI Team</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;0,8..60,700;1,8..60,400&family=IBM+Plex+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{--fs:'Source Serif 4',Georgia,serif;--fb:'IBM Plex Sans',-apple-system,sans-serif;--fm:'IBM Plex Mono',Menlo,monospace;--sw:290px;--mw:780px;--r:8px;--rl:12px}
[data-theme="light"]{--bg0:#f7f8fa;--bg1:#fff;--bg2:#f1f3f6;--bgc:#1a1e2e;--bgh:#eef0f4;--bga:#eef2ff;--bgth:#f5f6f9;--bgs:#fafbfc;--bgq:#f0f4ff;--b1:#dfe2e8;--b2:#ebedf2;--t1:#111827;--t2:#374151;--t3:#6b7280;--t4:#9ca3af;--ac:#4f46e5;--act:#3730a3;--ct:#d4d4d8;--sh:0 1px 3px rgba(0,0,0,.06);--shm:0 4px 16px rgba(0,0,0,.07)}
[data-theme="dark"]{--bg0:#0b0d12;--bg1:#11131a;--bg2:#181b24;--bgc:#0d0f16;--bgh:#1a1e2a;--bga:#1a1e36;--bgth:#14171f;--bgs:#12141c;--bgq:#151828;--b1:#252a38;--b2:#1c2030;--t1:#e5e7ed;--t2:#a0a6b8;--t3:#646c84;--t4:#3e4560;--ac:#818cf8;--act:#a5b4fc;--ct:#c0c4d0;--sh:0 1px 3px rgba(0,0,0,.3);--shm:0 4px 16px rgba(0,0,0,.4)}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
html{font-size:15px;-webkit-font-smoothing:antialiased}
body{font-family:var(--fb);background:var(--bg0);color:var(--t2);line-height:1.7;height:100vh;overflow:hidden}
button{cursor:pointer;font-family:inherit}
.shell{display:flex;height:100vh}
/* Sidebar */
.sb{width:var(--sw);flex-shrink:0;background:var(--bg1);border-right:1px solid var(--b1);display:flex;flex-direction:column;height:100vh;z-index:30;transition:width .2s,min-width .2s;min-width:var(--sw);overflow:hidden}
.sb.c{width:0;min-width:0;border-right:none}
.sb.c .sb-h,.sb.c .sb-n,.sb.c .sb-f{opacity:0;pointer-events:none}
.sbt{position:fixed;top:14px;left:calc(var(--sw) + 8px);z-index:40;width:28px;height:28px;border-radius:50%;background:var(--bg1);border:1px solid var(--b1);display:flex;align-items:center;justify-content:center;cursor:pointer;color:var(--t3);font-size:14px;transition:left .2s,background .15s;box-shadow:var(--sh)}
.sbt:hover{background:var(--bgh);color:var(--t1)}
.sbt.sh{left:14px}
.sb-h{padding:16px 14px 10px;border-bottom:1px solid var(--b1);flex-shrink:0}
.sb-br{display:flex;align-items:center;gap:9px;margin-bottom:10px}
.sb-logo{width:28px;height:28px;background:linear-gradient(135deg,#4f46e5,#7c3aed);border-radius:var(--r);display:flex;align-items:center;justify-content:center;color:#fff;font-family:var(--fs);font-weight:700;font-size:12px}
.sb-nm{font-family:var(--fs);font-size:14px;font-weight:600;color:var(--t1)}
.sb-vr{font-size:9.5px;color:var(--t4)}
.sb-sr{position:relative}
.sb-sr input{width:100%;padding:6px 10px 6px 28px;background:var(--bg2);border:1px solid var(--b1);border-radius:var(--r);color:var(--t1);font-size:11.5px;outline:none;font-family:var(--fb)}
.sb-sr input:focus{border-color:var(--ac)}
.sb-sr input::placeholder{color:var(--t4)}
.sb-sr svg{position:absolute;left:7px;top:50%;transform:translateY(-50%);color:var(--t4);pointer-events:none}
.sb-n{flex:1;overflow-y:auto;padding:4px 0}
.sb-n::-webkit-scrollbar{width:3px}
.sb-n::-webkit-scrollbar-thumb{background:var(--b1);border-radius:3px}
.sc{padding:12px 14px 3px;font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:1.3px;color:var(--t4)}
.sc:first-child{padding-top:2px}
.si{display:flex;align-items:flex-start;gap:8px;padding:5px 10px 5px 14px;cursor:pointer;transition:.15s;border-left:2.5px solid transparent}
.si:hover{background:var(--bgh)}
.si.on{background:var(--bga);border-left-color:var(--ac)}
.si-dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;margin-top:5px;opacity:.7}
.si.on .si-dot{opacity:1}
.si-t{min-width:0}
.si-n{font-size:11.5px;font-weight:500;color:var(--t2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.si.on .si-n{color:var(--act);font-weight:600}
.si-s{font-size:9.5px;color:var(--t4);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-top:1px}
.st{overflow:hidden;max-height:0;transition:max-height .3s}
.si.on+.st{max-height:4000px}
.st a{display:block;padding:3px 14px 3px 34px;font-size:10.5px;color:var(--t3);cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-decoration:none;transition:.12s}
.st a:hover{color:var(--t1);background:var(--bgh)}
.st a.on{color:var(--ac)}
.st a.d3{padding-left:48px;font-size:9.5px;color:var(--t4)}
.sb-f{padding:8px 14px;border-top:1px solid var(--b1);display:flex;align-items:center;justify-content:space-between;flex-shrink:0}
.sb-f span{font-size:9.5px;color:var(--t4)}
.thm{background:none;border:1px solid var(--b1);border-radius:var(--r);padding:3px 7px;color:var(--t3);font-size:9.5px;transition:.2s}
.thm:hover{background:var(--bgh);color:var(--t1)}
/* Content */
.cnt{flex:1;overflow-y:auto;position:relative}
.cnt::-webkit-scrollbar{width:5px}
.cnt::-webkit-scrollbar-thumb{background:var(--b1);border-radius:5px}
.pb{position:sticky;top:0;height:2px;z-index:5;background:var(--b2)}
.pf{height:100%;width:0%;background:linear-gradient(90deg,var(--ac),#7c3aed);transition:width 80ms}
/* Home */
.hm{padding:48px 36px;max-width:880px;margin:0 auto}
.hm h1{font-family:var(--fs);font-size:2.1rem;font-weight:600;color:var(--t1);letter-spacing:-.6px;line-height:1.2;margin-bottom:8px}
.hm>p{font-size:14px;color:var(--t3);max-width:500px;line-height:1.7;margin-bottom:28px}
.hcat{font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:1.4px;color:var(--t4);margin:22px 0 8px}
.hcat:first-of-type{margin-top:0}
.hg{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px}
.hc{background:var(--bg1);border:1px solid var(--b1);border-radius:var(--rl);padding:18px;cursor:pointer;transition:.2s;position:relative;overflow:hidden}
.hc:hover{border-color:var(--t4);box-shadow:var(--shm);transform:translateY(-1px)}
.hc::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--cc);transform:scaleX(0);transform-origin:left;transition:transform .2s}
.hc:hover::after{transform:scaleX(1)}
.hc-dot{width:8px;height:8px;border-radius:50%;margin-bottom:10px}
.hc h3{font-family:var(--fs);font-size:14px;font-weight:600;color:var(--t1);margin-bottom:3px}
.hc p{font-size:11.5px;color:var(--t3);line-height:1.5}
.hc-m{font-size:9.5px;color:var(--t4);margin-top:7px}
/* Doc */
.dv{display:none}
.dt{position:sticky;top:0;z-index:5;background:var(--bg0);border-bottom:1px solid var(--b1);padding:8px 36px;display:flex;align-items:center;gap:8px}
.dt-b{display:flex;align-items:center;gap:4px;font-size:11.5px;color:var(--t3);padding:4px 8px;border-radius:var(--r);border:none;background:none;transition:.15s;font-family:var(--fb)}
.dt-b:hover{background:var(--bgh);color:var(--t1)}
.dt-c{font-size:10.5px;color:var(--t4)}
.dt-c b{color:var(--t3);font-weight:500}
.db{max-width:var(--mw);margin:0 auto;padding:28px 36px 100px}
.dh{margin-bottom:28px;padding-bottom:20px;border-bottom:1px solid var(--b1)}
.dh-badge{display:inline-block;font-size:9px;font-weight:600;text-transform:uppercase;letter-spacing:1px;padding:2px 8px;border-radius:20px;margin-bottom:10px}
.dh h1{font-family:var(--fs);font-size:1.8rem;font-weight:600;color:var(--t1);letter-spacing:-.3px;line-height:1.25;margin-bottom:4px}
.dh-sub{font-size:13px;color:var(--t3)}
.dh-m{margin-top:7px;font-size:10.5px;color:var(--t4);display:flex;gap:10px}
/* Prose */
.prose{font-size:.92rem;color:var(--t2)}
.prose>h1{display:none}
.prose h2{font-family:var(--fs);font-size:1.4rem;font-weight:600;color:var(--t1);margin:44px 0 10px;padding-bottom:7px;border-bottom:1px solid var(--b1);letter-spacing:-.2px;line-height:1.3;scroll-margin-top:48px}
.prose h3{font-family:var(--fs);font-size:1.05rem;font-weight:600;color:var(--t1);margin:28px 0 7px;line-height:1.35;scroll-margin-top:48px}
.prose h4{font-size:.85rem;font-weight:600;color:var(--t2);margin:18px 0 5px;scroll-margin-top:48px}
.prose h5,.prose h6{font-size:.82rem;font-weight:600;color:var(--t3);margin:14px 0 4px}
.prose p{margin-bottom:11px;line-height:1.75}
.prose strong{color:var(--t1);font-weight:600}
.prose a{color:var(--ac);text-decoration:none;transition:.2s}
.prose a:hover{text-decoration:underline}
.prose ul,.prose ol{padding-left:20px;margin-bottom:11px}
.prose li{margin-bottom:3px;line-height:1.7}
.prose li::marker{color:var(--t4)}
.prose li>ul,.prose li>ol{margin-top:3px;margin-bottom:0}
.prose blockquote{border-left:3px solid var(--ac);padding:10px 14px;margin:18px 0;background:var(--bgq);border-radius:0 var(--r) var(--r) 0}
.prose blockquote p:last-child{margin-bottom:0}
.prose blockquote strong{color:var(--act)}
.prose code{font-family:var(--fm);font-size:.8em;background:var(--bg2);border:1px solid var(--b1);padding:1px 4px;border-radius:4px;color:var(--t1);word-break:break-word}
.prose pre{background:var(--bgc);border:1px solid var(--b1);border-radius:var(--rl);padding:14px 18px;margin:16px 0;overflow-x:auto}
.prose pre code{background:none;border:none;padding:0;font-size:11.5px;line-height:1.65;color:var(--ct)}
.prose hr{border:none;border-top:1px solid var(--b1);margin:36px 0}
.prose input[type="checkbox"]{margin-right:5px;accent-color:var(--ac)}
.tw{overflow-x:auto;margin:16px 0;border:1px solid var(--b1);border-radius:var(--rl)}
.prose table{width:100%;border-collapse:collapse;font-size:11.5px;min-width:380px}
.prose thead th{background:var(--bgth);padding:8px 10px;text-align:left;font-weight:600;font-size:10px;text-transform:uppercase;letter-spacing:.5px;color:var(--t3);border-bottom:2px solid var(--b1);white-space:nowrap}
.prose tbody td{padding:7px 10px;border-bottom:1px solid var(--b2);color:var(--t2);vertical-align:top;line-height:1.55}
.prose tbody tr:last-child td{border-bottom:none}
.prose tbody tr:nth-child(even) td{background:var(--bgs)}
.prose tbody tr:hover td{background:var(--bgh)}
/* Search overlay */
.sov{position:fixed;inset:0;background:rgba(0,0,0,.35);z-index:100;display:none;align-items:flex-start;justify-content:center;padding-top:10vh;backdrop-filter:blur(3px)}
.sov.on{display:flex}
.smo{background:var(--bg1);border:1px solid var(--b1);border-radius:var(--rl);width:92%;max-width:540px;box-shadow:var(--shm);overflow:hidden}
.smo input{width:100%;padding:13px 14px;background:transparent;border:none;border-bottom:1px solid var(--b1);color:var(--t1);font-size:13.5px;outline:none;font-family:var(--fb)}
.smo input::placeholder{color:var(--t4)}
.sr{max-height:340px;overflow-y:auto}
.sr::-webkit-scrollbar{width:3px}
.sr::-webkit-scrollbar-thumb{background:var(--b1);border-radius:3px}
.sri{padding:10px 14px;cursor:pointer;border-bottom:1px solid var(--b2);transition:.15s}
.sri:last-child{border-bottom:none}
.sri:hover{background:var(--bgh)}
.sri-d{font-size:8.5px;text-transform:uppercase;letter-spacing:1px;color:var(--t4);margin-bottom:1px}
.sri-h{font-size:12px;font-weight:500;color:var(--t1);margin-bottom:2px}
.sri-p{font-size:11px;color:var(--t3);line-height:1.5;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.sri-p mark{background:rgba(79,70,229,.15);color:var(--act);padding:1px 2px;border-radius:3px}
.sr-e{padding:20px 14px;text-align:center;color:var(--t4);font-size:11.5px}
@media(max-width:840px){
.sb{position:fixed;left:0;z-index:50;box-shadow:var(--shm);width:260px;min-width:260px}
.sb.c{left:-270px;width:260px;min-width:260px;border-right:1px solid var(--b1)}
.sb.c .sb-h,.sb.c .sb-n,.sb.c .sb-f{opacity:1;pointer-events:auto}
.sbt{left:12px}
.db{padding:20px 16px 80px}
.dt{padding:6px 14px}
.hm{padding:20px 16px}
.hm h1{font-size:1.5rem}}
</style>
</head>
<body>
<div class="shell">
<button class="sbt" id="sbt" onclick="toggleSB()" title="Toggle sidebar">&#10005;</button>
<aside class="sb" id="sb">
<div class="sb-h">
<div class="sb-br"><div class="sb-logo">W</div><div><div class="sb-nm">Ways of Working</div><div class="sb-vr">GenAI &middot; Indegene</div></div></div>
<div class="sb-sr"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
<input type="text" placeholder="Search (Ctrl+K)" readonly onclick="openS()"></div>
</div>
<nav class="sb-n" id="sbn">%%NAV%%</nav>
<div class="sb-f"><span>April 2026</span><button class="thm" onclick="toggleT()" id="tb">&#9789; Dark</button></div>
</aside>
<div class="cnt" id="cnt">
<div class="pb"><div class="pf" id="pf"></div></div>
<div class="hm" id="hv">%%HOME%%</div>
%%DOCVIEWS%%
</div>
</div>
<div class="sov" id="sov" onclick="if(event.target===this)closeS()">
<div class="smo"><input type="text" id="si" placeholder="Search all documents..." autocomplete="off"><div class="sr" id="sr"></div></div>
</div>
<script>
var SI=%%SEARCHINDEX%%;
var DI=%%DOCIDS%%;
var cur=null;
function loadDoc(id){cur=id;document.getElementById('hv').style.display='none';DI.forEach(function(x){var e=document.getElementById('dv-'+x);if(e)e.style.display=x===id?'block':'none'});document.querySelectorAll('.si').forEach(function(e){e.classList.toggle('on',e.id==='si-'+id)});document.getElementById('cnt').scrollTop=0;document.getElementById('sb').classList.remove('open')}
function goHome(){cur=null;document.getElementById('hv').style.display='block';DI.forEach(function(x){var e=document.getElementById('dv-'+x);if(e)e.style.display='none'});document.querySelectorAll('.si').forEach(function(e){e.classList.remove('on')});document.getElementById('cnt').scrollTop=0}
function scrollH(s){var e=document.getElementById(s);if(e)e.scrollIntoView({behavior:'smooth',block:'start'})}
document.getElementById('cnt').addEventListener('scroll',function(){var p=(this.scrollTop/(this.scrollHeight-this.clientHeight))*100;document.getElementById('pf').style.width=(p||0)+'%';if(!cur)return;var a=null;var hs=document.querySelectorAll('#dv-'+cur+' .prose h2,#dv-'+cur+' .prose h3');hs.forEach(function(h){if(h.getBoundingClientRect().top<=66)a=h.id});document.querySelectorAll('#st-'+cur+' a').forEach(function(e){e.classList.toggle('on',e.getAttribute('data-s')===a)})});
function openS(){document.getElementById('sov').classList.add('on');var i=document.getElementById('si');i.value='';i.focus();document.getElementById('sr').innerHTML='<div class="sr-e">Type at least 3 characters</div>'}
function closeS(){document.getElementById('sov').classList.remove('on')}
document.getElementById('si').addEventListener('input',function(){var q=this.value.trim().toLowerCase();var c=document.getElementById('sr');if(q.length<3){c.innerHTML='<div class="sr-e">Type at least 3 characters</div>';return}var m=[],seen={};SI.forEach(function(e){if(e.t.toLowerCase().indexOf(q)>-1){var k=e.d+'|'+e.h;if(!seen[k]&&m.length<16){seen[k]=true;var i=e.t.toLowerCase().indexOf(q);var s=Math.max(0,i-50),end=Math.min(e.t.length,i+q.length+80);var pv=(s>0?'\u2026':'')+e.t.substring(s,end)+(end<e.t.length?'\u2026':'');var re=new RegExp('('+q.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','gi');pv=pv.replace(re,'<mark>$1</mark>');m.push({d:e.d,dt:e.dt,h:e.h,p:pv})}}});if(!m.length){c.innerHTML='<div class="sr-e">No results</div>';return}c.innerHTML=m.map(function(x){return'<div class="sri" onclick="loadDoc(\''+x.d+'\');closeS()"><div class="sri-d">'+x.dt+'</div><div class="sri-h">'+x.h+'</div><div class="sri-p">'+x.p+'</div></div>'}).join('')});
document.addEventListener('keydown',function(e){if((e.metaKey||e.ctrlKey)&&e.key==='k'){e.preventDefault();openS()}if(e.key==='Escape')closeS()});
function toggleSB(){var s=document.getElementById('sb'),b=document.getElementById('sbt');var c=s.classList.toggle('c');b.classList.toggle('sh',c);b.innerHTML=c?'&#9776;':'&#10005;';localStorage.setItem('sc',c?'1':'0')}
(function(){if(localStorage.getItem('sc')==='1'){document.getElementById('sb').classList.add('c');var b=document.getElementById('sbt');b.classList.add('sh');b.innerHTML='&#9776;'}})();
function toggleT(){var t=document.documentElement.getAttribute('data-theme')==='light'?'dark':'light';document.documentElement.setAttribute('data-theme',t);document.getElementById('tb').innerHTML=t==='light'?'&#9789; Dark':'&#9788; Light';localStorage.setItem('wt',t)}
(function(){var s=localStorage.getItem('wt');if(s){document.documentElement.setAttribute('data-theme',s);document.getElementById('tb').innerHTML=s==='light'?'&#9789; Dark':'&#9788; Light'}})();
</script>
</body>
</html>'''

# Replace markers
output = TEMPLATE
output = output.replace('%%NAV%%', nav_html)
output = output.replace('%%HOME%%', home_html)
output = output.replace('%%DOCVIEWS%%', dv_html)
output = output.replace('%%SEARCHINDEX%%', json.dumps(search_idx, ensure_ascii=False))
output = output.replace('%%DOCIDS%%', json.dumps([d["id"] for d in DOCUMENTS]))

with open(OUT, "w") as f:
    f.write(output)

print("Portal built: %s" % OUT)
print("Size: %d KB" % (os.path.getsize(OUT) // 1024))
print("Zero f-strings in template. Zero client-side markdown. All pre-rendered.")
