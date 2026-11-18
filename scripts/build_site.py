#!/usr/bin/env python3
"""Generate docs/index.html, the census as one web page.

The page has two views, "By definition" (the tables of definitions.md) and "By roadmap" (the
content of roadmaps.md), with a text filter and filters by area and status. It is a single file
with its style sheet and script inline, so it can be opened from disk or served by GitHub Pages
from the docs/ folder.

Inputs, all in this repository:

  README.md                the title, the opening paragraphs and the snapshot paragraph
  definitions.md           the status legend and one row per definition
  census/NNN.md            the first line of "Status", and the roadmap citations
  roadmap-descriptions.md  a title and a short description for each cited roadmap

Usage:

  python3 scripts/build_site.py           write docs/index.html
  python3 scripts/build_site.py --check   fail if docs/index.html is stale

Only the Python standard library is used, and the output depends on the input files alone.
"""

import argparse
import html
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # leave no __pycache__ in the repository
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_roadmaps as census  # noqa: E402

ROOT = census.ROOT
OUTPUT = "docs/index.html"
REPOSITORY = "https://github.com/TauCetiProject/AnnalsDefinitions"
BLOB = REPOSITORY + "/blob/main/"

# The status codes that open a census file's "Status" section, and the names definitions.md
# gives them.
STATUS_NAMES = {
    "IN-CODE": "In Tau Ceti",
    "PARTIAL-CODE": "Partly in code",
    "ROADMAP-MERGED": "Merged roadmap",
    "ROADMAP-PR": "Roadmap PR",
    "PREREQS-ROADMAPPED": "Prerequisites planned",
    "UNPLANNED": "Unplanned",
}
STATUS_CLASS = {
    "In Tau Ceti": "s-code",
    "Partly in code": "s-part",
    "Merged roadmap": "s-merged",
    "Roadmap PR": "s-pr",
    "Prerequisites planned": "s-prereq",
    "Unplanned": "s-none",
}


def esc(text):
    return html.escape(text, quote=True)


# ---------------------------------------------------------------------------
# Inline Markdown and simple TeX
# ---------------------------------------------------------------------------

TEX_SYMBOLS = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε", "lambda": "λ",
    "mu": "μ", "pi": "π", "rho": "ρ", "sigma": "σ", "tau": "τ", "phi": "φ", "chi": "χ",
    "psi": "ψ", "omega": "ω", "Gamma": "Γ", "Delta": "Δ", "Lambda": "Λ", "Sigma": "Σ",
    "Phi": "Φ", "Psi": "Ψ", "Omega": "Ω", "ell": "ℓ", "infty": "∞", "times": "×",
    "otimes": "⊗", "to": "→", "le": "≤", "ge": "≥",
}
# Only letters of the Basic Multilingual Plane, which every system font set covers.
TEX_ALPHABETS = {
    "mathbb": {"C": "ℂ", "H": "ℍ", "N": "ℕ", "P": "ℙ", "Q": "ℚ", "R": "ℝ", "Z": "ℤ"},
    "mathcal": {"B": "ℬ", "E": "ℰ", "F": "ℱ", "H": "ℋ", "L": "ℒ", "M": "ℳ", "R": "ℛ"},
    "mathscr": {"B": "ℬ", "E": "ℰ", "F": "ℱ", "H": "ℋ", "L": "ℒ", "M": "ℳ", "R": "ℛ"},
}


class _TexError(Exception):
    pass


def _tex_group(src, i):
    """Read one TeX argument at src[i:]: a braced group, a command, or one character."""
    if i >= len(src):
        raise _TexError
    if src[i] == "{":
        depth, j = 1, i + 1
        while j < len(src) and depth:
            depth += {"{": 1, "}": -1}.get(src[j], 0)
            j += 1
        if depth:
            raise _TexError
        return src[i + 1:j - 1], j
    if src[i] == "\\":
        m = re.match(r"\\[A-Za-z]+", src[i:])
        if not m:
            raise _TexError
        return m.group(0), i + m.end()
    return src[i], i + 1


def _tex(src, upright=False):
    out, i = [], 0
    while i < len(src):
        ch = src[i]
        if ch == "\\":
            m = re.match(r"\\([A-Za-z]+)", src[i:])
            if not m:
                raise _TexError
            name, i = m.group(1), i + m.end()
            if name in TEX_SYMBOLS:
                out.append(TEX_SYMBOLS[name])
            elif name in ("mathrm", "operatorname", "text"):
                arg, i = _tex_group(src, i)
                out.append(_tex(arg, upright=True))
            elif name in TEX_ALPHABETS:
                arg, i = _tex_group(src, i)
                if arg in TEX_ALPHABETS[name]:
                    out.append(TEX_ALPHABETS[name][arg])
                elif name != "mathbb" and len(arg) == 1 and arg.isascii() and arg.isupper():
                    out.append("<i>" + arg + "</i>")
                else:
                    raise _TexError
            elif name == "overline":
                arg, i = _tex_group(src, i)
                out.append('<span class="ov">' + _tex(arg, upright) + "</span>")
            else:
                raise _TexError
        elif ch in "^_":
            arg, i = _tex_group(src, i + 1)
            tag = "sup" if ch == "^" else "sub"
            out.append(f"<{tag}>" + _tex(arg, upright) + f"</{tag}>")
        elif ch in "{}$":
            raise _TexError
        elif ch == "-":
            out.append("−")
            i += 1
        elif ch.isalpha() and ch.isascii() and not upright:
            j = i
            while j < len(src) and src[j].isalpha() and src[j].isascii():
                j += 1
            out.append("<i>" + esc(src[i:j]) + "</i>")
            i = j
        else:
            out.append(esc(ch))
            i += 1
    return "".join(out)


def tex(src):
    """Simple TeX as HTML; the source, unchanged, when it uses anything not handled here."""
    try:
        return '<span class="math">' + _tex(src.strip()) + "</span>"
    except _TexError:
        return '<span class="tex">$' + esc(src) + "$</span>"


_LINK = re.compile(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(([^()\s]*(?:\([^()\s]*\)[^()\s]*)*)\)")
_PUNCT = set("!\"#$%&'()*+,-./:;<=>?[\\]^_`{|}~")


def absolute(url):
    """Links inside the repository become links to the file on GitHub."""
    if re.match(r"[a-z][a-z0-9+.-]*:", url) or url.startswith("#"):
        return url
    return BLOB + url.lstrip("./")


def inline(text):
    """The inline Markdown the census tables use, as HTML: links, code, emphasis, `$...$`."""
    out, i, n = [], 0, len(text)
    while i < n:
        ch = text[i]
        if ch == "\\" and i + 1 < n and text[i + 1] in _PUNCT:
            out.append(esc(text[i + 1]))
            i += 2
            continue
        if ch == "`":
            j = text.find("`", i + 1)
            if j > 0:
                out.append("<code>" + esc(text[i + 1:j]) + "</code>")
                i = j + 1
                continue
        if ch == "$":
            j = text.find("$", i + 1)
            if j > 0:
                out.append(tex(text[i + 1:j]))
                i = j + 1
                continue
        if ch == "[":
            m = _LINK.match(text, i)
            if m:
                out.append(f'<a href="{esc(absolute(m.group(2)))}">' + inline(m.group(1)) + "</a>")
                i = m.end()
                continue
        if ch == "*":
            mark = "**" if text.startswith("**", i) else "*"
            j = _closing(text, i, mark)
            if j > 0:
                tag = "strong" if mark == "**" else "em"
                out.append(f"<{tag}>" + inline(text[i + len(mark):j]) + f"</{tag}>")
                i = j + len(mark)
                continue
        if ch == "-" and text.startswith("--", i) and 0 < i < n - 2 \
                and text[i - 1].isalnum() and text[i + 2].isalnum():
            out.append("–")
            i += 2
            continue
        out.append(esc(ch))
        i += 1
    return "".join(out)


def _closing(text, start, mark):
    """The index of the delimiter closing the emphasis opened at `start`, or -1."""
    after = start + len(mark)
    if after >= len(text) or text[after].isspace():
        return -1
    before = text[start - 1] if start else " "
    if text[after] in _PUNCT and not (before.isspace() or before in _PUNCT):
        return -1
    j = after
    while True:
        j = text.find(mark, j + 1)
        if j < 0:
            return -1
        if text[j - 1] == "\\" or text[j - 1].isspace():
            continue
        if mark == "*" and (text.startswith("**", j) or text[j - 1] == "*"):
            continue
        return j


def breakable(name):
    """A folder name with break opportunities at its word boundaries."""
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=/)", "<wbr>", esc(name))


# ---------------------------------------------------------------------------
# Reading the census
# ---------------------------------------------------------------------------

def readme_opening():
    """The title of README.md and its paragraphs before the first `## ` heading."""
    title, paragraphs, block = None, [], []
    for line in census.read("README.md").splitlines():
        if line.startswith("## "):
            break
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
        elif line.strip():
            block.append(line.strip())
        elif block:
            paragraphs.append(" ".join(block))
            block = []
    if block:
        paragraphs.append(" ".join(block))
    if not title:
        raise census.CensusError("README.md: no title")
    return title, paragraphs


def definitions_intro():
    """The paragraphs of definitions.md outside its tables, before the first area."""
    before, after, seen_table = [], [], False
    for line in census.read("definitions.md").splitlines():
        if line.startswith("## "):
            break
        if line.startswith("|"):
            seen_table = True
        elif line.strip() and not line.startswith("# "):
            (after if seen_table else before).append(line.strip())
    return before, after


def status_line(number):
    """(code, qualifier) from the first line of a census file's "Status" section."""
    text = census.census_sections(number).get("Status", "")
    first = next((line.strip() for line in text.splitlines() if line.strip()), "")
    m = re.match(r"([A-Z]+(?:-[A-Z]+)*)(?:, ([^.:]+))?", first)
    if not m:
        raise census.CensusError(f"{census.census_path(number)}: 'Status' opens with no status")
    return m.group(1), (m.group(2) or "").strip()


def slug(name):
    return "r-" + re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-")


def load():
    """Everything the page shows, checked for consistency."""
    legend, areas, rows = census.read_definitions()
    model = census.build_model()
    if model["problems"]:
        raise census.CensusError("; ".join(model["problems"]))
    counts = {}
    for row in rows:
        code, qualifier = status_line(row["number"])
        name = STATUS_NAMES.get(code)
        if name is None:
            print(f"note: {census.census_path(row['number'])}: status {code} has no name here",
                  file=sys.stderr)
        elif name != row["status"]:
            raise census.CensusError(
                f"definition {row['number']}: definitions.md says '{row['status']}', "
                f"{census.census_path(row['number'])} says {code}"
            )
        row["qualifier"] = qualifier
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    for status, _, count in legend:
        if counts.get(status, 0) != int(count):
            raise census.CensusError(
                f"definitions.md: the legend counts {count} '{status}', the tables have "
                f"{counts.get(status, 0)}"
            )
    unknown = sorted(set(counts) - {status for status, _, _ in legend})
    if unknown:
        raise census.CensusError(f"definitions.md: status not in the legend: {unknown[0]}")
    return legend, areas, rows, model


# ---------------------------------------------------------------------------
# The page
# ---------------------------------------------------------------------------

CSS = """
:root{color-scheme:light dark;
--bg:#ffffff;--fg:#1c1e21;--muted:#5a6069;--line:#d5d9df;--soft:#f5f6f8;--link:#0b55c4;
--code-bg:#dcf2ef;--code-fg:#0b4a44;--part-bg:#e4f3d9;--part-fg:#2c4f12;
--merged-bg:#e1ecfb;--merged-fg:#143f8a;--pr-bg:#f0e6fb;--pr-fg:#55208a;
--prereq-bg:#fbeed3;--prereq-fg:#6a4300;--none-bg:#e9ebee;--none-fg:#3b4149}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);
font:15px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
.wrap{max-width:78rem;margin:0 auto;padding:0 1rem}
a{color:var(--link);text-decoration-thickness:.06em;text-underline-offset:.15em}
a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,summary:focus-visible{
outline:2px solid var(--link);outline-offset:2px}
h1{font-size:1.5rem;line-height:1.25;margin:1.4rem 0 .5rem}
h2{font-size:1.2rem;margin:1.6rem 0 .3rem}
h3{font-size:1.02rem;margin:1.5rem 0 .4rem}
p{margin:.4rem 0}
code{font:.88em ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;overflow-wrap:anywhere}
sub,sup{font-size:.72em;line-height:0}
.ov{text-decoration:overline}
.lede{max-width:56rem}
.meta{color:var(--muted);font-size:.9rem}
table{border-collapse:collapse;width:100%}
th,td{text-align:left;vertical-align:top;padding:.4rem .6rem;border-bottom:1px solid var(--line);
overflow-wrap:break-word}
th{font-size:.82rem;font-weight:600;color:var(--muted);border-bottom:2px solid var(--line);white-space:nowrap}
td.num{font-variant-numeric:tabular-nums;color:var(--muted);white-space:nowrap}
table.legend{width:auto;margin:.6rem 0}
table.legend td.n{text-align:right;font-variant-numeric:tabular-nums}
table.defs td.name{width:22%}table.defs td.status{width:13%}
table.rms td.rmname{width:22%}table.rms td.cites{width:36%}
.badge{display:inline-block;font-size:.8rem;border-radius:.25rem;padding:.05rem .4rem;white-space:nowrap}
button.badge{font:inherit;font-size:.8rem;cursor:pointer;border:1px solid transparent}
button.badge[aria-pressed="true"]{border-color:currentColor}
.s-code{background:var(--code-bg);color:var(--code-fg)}
.s-part{background:var(--part-bg);color:var(--part-fg)}
.s-merged{background:var(--merged-bg);color:var(--merged-fg)}
.s-pr{background:var(--pr-bg);color:var(--pr-fg)}
.s-prereq{background:var(--prereq-bg);color:var(--prereq-fg)}
.s-none{background:var(--none-bg);color:var(--none-fg)}
.small{display:block;font-size:.84rem;font-weight:400;color:var(--muted);margin-top:.15rem}
.rmname .folder{font-weight:600;overflow-wrap:anywhere}
.rmname .title{display:block;font-style:italic;margin-top:.1rem}
details{margin-top:.35rem;font-size:.9rem}
summary{cursor:pointer;color:var(--muted)}
details ul,td.cites ul{margin:.3rem 0 0;padding-left:1.1rem}
td.cites ul{margin-top:0}
li{margin:.15rem 0}
.also{color:var(--muted);font-size:.9rem}
.controls{display:none;background:var(--bg);border-bottom:1px solid var(--line);padding:.55rem 0;margin-top:1rem}
.js .controls{display:block}
.controls .row{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center}
.controls input,.controls select{font:inherit;color:var(--fg);background:var(--bg);
border:1px solid var(--line);border-radius:.3rem;padding:.35rem .5rem;min-width:0}
.controls input{flex:1 1 14rem}
.controls select{flex:0 1 auto;max-width:100%}
.controls label{position:absolute;left:-999rem}
.tabs{display:inline-flex}
.tabs button{font:inherit;cursor:pointer;color:var(--fg);background:var(--bg);
border:1px solid var(--line);padding:.35rem .7rem}
.tabs button:first-child{border-radius:.3rem 0 0 .3rem}
.tabs button:last-child{border-radius:0 .3rem .3rem 0;border-left:0}
.tabs button[aria-pressed="true"]{background:var(--fg);color:var(--bg);border-color:var(--fg)}
.count{color:var(--muted);font-size:.9rem;margin:.35rem 0 0}
.js main.v-def #by-roadmap,.js main.v-rm #by-definition{display:none}
tr[hidden],section[hidden]{display:none}
tr:target>td{background:var(--soft)}
tr[id]{scroll-margin-top:7rem}
.empty{display:none;color:var(--muted);padding:1rem 0}
footer{color:var(--muted);font-size:.88rem;padding:1.5rem 0 3rem}
"""

# Style sheets with a media condition, each written as its own <style media="..."> element.
CSS_MEDIA = [
    ("(prefers-color-scheme: dark)", """
:root{--bg:#15171b;--fg:#e4e6e9;--muted:#a2a9b3;--line:#363b43;--soft:#1e2127;--link:#8fb6f9;
--code-bg:#0f3a37;--code-fg:#a3e4dc;--part-bg:#243c14;--part-fg:#c3e6a6;
--merged-bg:#172d53;--merged-fg:#adc9fa;--pr-bg:#35214f;--pr-fg:#dbbcf8;
--prereq-bg:#40300c;--prereq-fg:#f2d48f;--none-bg:#2b2f36;--none-fg:#c5cad2}
"""),
    ("(min-width: 48rem) and (min-height: 34rem)", """
.controls{position:sticky;top:0;z-index:2}
"""),
    ("(max-width: 48rem)", """
table.defs,table.rms,table.defs tbody,table.rms tbody,table.defs tr,table.rms tr,
table.defs td,table.rms td{display:block;width:auto}
table.defs thead,table.rms thead{position:absolute;left:-999rem}
table.defs tr,table.rms tr{padding:.6rem 0;border-bottom:1px solid var(--line)}
table.defs tr[hidden],table.rms tr[hidden]{display:none}
table.defs td,table.rms td{border:0;padding:.12rem 0}
table.defs td.name,table.defs td.status,table.rms td.rmname,table.rms td.cites{width:auto}
table.defs td.num{float:left;margin-right:.5rem}
table.defs td.name{font-weight:600}
tr[id]{scroll-margin-top:1rem}
"""),
    ("print", """
.js .controls{display:none}
.js main.v-def #by-roadmap,.js main.v-rm #by-definition{display:block}
"""),
]

JS = """
(function(){
var doc=document;doc.body.classList.add('js');
var main=doc.querySelector('main'),q=doc.getElementById('q'),
area=doc.getElementById('area'),status=doc.getElementById('status'),count=doc.getElementById('count');
function all(sel){return [].slice.call(doc.querySelectorAll(sel));}
var defs=all('tr.def'),rms=all('tr.rm'),groups=all('section.group'),
tabs=all('.tabs button'),chips=all('button.badge');
var emptyD=doc.getElementById('empty-def'),emptyR=doc.getElementById('empty-rm');
function norm(s){s=s.toLowerCase();if(s.normalize){s=s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'');}
return s.replace(/[\\u2010-\\u2015]/g,'-').replace(/\\s+/g,' ');}
defs.concat(rms).forEach(function(el){el._t=norm(el.textContent);});
var view='def';
function setView(v){view=v;main.className=(v==='rm')?'v-rm':'v-def';
tabs.forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-view')===v?'true':'false');});apply();}
function has(list,value){return ('|'+list+'|').indexOf('|'+value+'|')>=0;}
function apply(){
var words=norm(q.value).split(' ').filter(Boolean),a=area.value,s=status.value,nd=0,nr=0;
function hit(el){for(var i=0;i<words.length;i++){if(el._t.indexOf(words[i])<0)return false;}return true;}
defs.forEach(function(el){var ok=hit(el)&&(!a||el.getAttribute('data-area')===a)&&(!s||el.getAttribute('data-status')===s);
el.hidden=!ok;if(ok)nd++;});
rms.forEach(function(el){var ok=hit(el)&&(!a||has(el.getAttribute('data-areas'),a))&&(!s||has(el.getAttribute('data-statuses'),s));
el.hidden=!ok;if(ok)nr++;});
groups.forEach(function(sec){sec.hidden=!sec.querySelector('tr.def:not([hidden]),tr.rm:not([hidden])');});
emptyD.style.display=nd?'none':'block';emptyR.style.display=nr?'none':'block';
count.textContent=(view==='rm')?('Showing '+nr+' of '+rms.length+' roadmaps and PRs'):('Showing '+nd+' of '+defs.length+' definitions');
chips.forEach(function(b){b.setAttribute('aria-pressed',(s&&b.getAttribute('data-status')===s)?'true':'false');});}
function go(){var id=decodeURIComponent(location.hash.slice(1));if(!id)return;
var el=doc.getElementById(id);if(!el)return;
var want=(id==='by-roadmap'||id.indexOf('r-')===0)?'rm':((id==='by-definition'||id.indexOf('d-')===0)?'def':view);
if(want!==view)setView(want);
if(el.hidden){q.value='';area.value='';status.value='';apply();}
el.scrollIntoView();}
q.addEventListener('input',apply);area.addEventListener('change',apply);status.addEventListener('change',apply);
tabs.forEach(function(b){b.addEventListener('click',function(){setView(b.getAttribute('data-view'));});});
chips.forEach(function(b){b.addEventListener('click',function(){var v=b.getAttribute('data-status');
status.value=(status.value===v)?'':v;apply();});});
window.addEventListener('hashchange',go);
setView('def');go();
})();
"""


def badge(status, tag="span", extra=""):
    cls = STATUS_CLASS.get(status, "s-none")
    return f'<{tag} class="badge {cls}"{extra}>{esc(status)}</{tag}>'


def roadmap_index(model):
    """Citation -> the entry of the roadmap view that describes it."""
    index = {}
    for group in ("merged", "open", "other"):
        for item in model[group]:
            if group == "other":
                index[("pr", item["pr"])] = [item]
                continue
            index[("folder", item["name"])] = [item]
            if item["pr"] is not None:
                index.setdefault(("pr", item["pr"]), []).append(item)
    return index


def state_text(item):
    return item["state"][0].upper() + item["state"][1:] if item["state"] else "PR"


def render_definition(row, index, evidence):
    number = row["number"]
    described, seen = [], set()
    for kind, ident, _, _ in census.where_citations(row["where"]):
        for item in index.get((kind, ident), []):
            if item["name"] not in seen:
                seen.add(item["name"])
                described.append(item)
    also = [item for item in evidence.get(number, []) if item["name"] not in seen]
    cell = [inline(row["where"])]
    if described or also:
        cell.append("<details><summary>What the cited roadmaps contain</summary>")
        if described:
            cell.append("<ul>")
            for item in described:
                cell.append(
                    f'<li><a href="#{slug(item["name"])}">{breakable(item["name"])}</a> '
                    f'({esc(item["state"] or "pull request")}): '
                    f'{inline(item["title"])}. {inline(item["description"])}</li>'
                )
            cell.append("</ul>")
        if also:
            links = ", ".join(
                f'<a href="#{slug(item["name"])}">{breakable(item["name"])}</a>' for item in also
            )
            cell.append(f'<p class="also">Also cited in its census file: {links}.</p>')
        cell.append("</details>")
    qualifier = f'<span class="small">{esc(row["qualifier"])}</span>' if row["qualifier"] else ""
    task = f'<span class="small">Task file: {inline(row["file"])}</span>' if row["file"] else ""
    evidence_link = f'<span class="small">{inline(row["evidence"])} file</span>'
    return (
        f'<tr class="def" id="d-{number}" data-area="{esc(row["area"])}" '
        f'data-status="{esc(row["status"])}">'
        f'<td class="num">{number}</td>'
        f'<td class="name">{inline(row["name"])}{evidence_link}</td>'
        f'<td class="status">{badge(row["status"])}{qualifier}{task}</td>'
        f'<td class="where">{"".join(cell)}</td></tr>'
    )


def render_roadmap(item, rows):
    numbers = [n for n, _ in item["cited"]] + list(item["evidence"])
    areas = "|".join(sorted({rows[n]["area"] for n in numbers}))
    statuses = "|".join(sorted({rows[n]["status"] for n in numbers}))
    cites = []
    if item["cited"]:
        cites.append("<ul>")
        for number, sections in item["cited"]:
            line = f'<a href="#d-{number}">#{number} {inline(rows[number]["name"])}</a>'
            if sections:
                line += ": " + inline(sections)
            cites.append(f"<li>{line}</li>")
        cites.append("</ul>")
    if item["evidence"]:
        links = ", ".join(
            f'<a href="{esc(BLOB + census.census_path(n))}">#{n} {inline(rows[n]["name"])}</a>'
            for n in item["evidence"]
        )
        cites.append(f'<p class="also">Also cited in the evidence for {links}.</p>')
    state = f'<span class="small">{esc(state_text(item))}</span>' if item["state"] else ""
    return (
        f'<tr class="rm" id="{slug(item["name"])}" data-areas="{esc(areas)}" '
        f'data-statuses="{esc(statuses)}">'
        f'<td class="rmname"><a class="folder" href="{esc(item["url"])}">'
        f'{breakable(item["name"])}</a>'
        f'<span class="title">{inline(item["title"])}</span>{state}</td>'
        f'<td class="about">{inline(item["description"])}</td>'
        f'<td class="cites">{"".join(cites)}</td></tr>'
    )


def render():
    legend, areas, rows, model = load()
    by_number = model["rows"]
    for row in rows:
        by_number[row["number"]]["qualifier"] = row["qualifier"]
    title, opening = readme_opening()
    intro, notes = definitions_intro()
    index = roadmap_index(model)
    evidence = {}
    for group in ("merged", "open", "other"):
        for item in model[group]:
            for number in item["evidence"]:
                evidence.setdefault(number, []).append(item)

    out = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{esc(title)}</title>",
        f"<style>{CSS}</style>",
    ]
    for media, css in CSS_MEDIA:
        out.append(f'<style media="{esc(media)}">{css}</style>')
    out += ["</head>", "<body>", '<div class="wrap">', "<header>", f"<h1>{esc(title)}</h1>"]
    for paragraph in opening:
        out.append(f'<p class="lede">{inline(paragraph)}</p>')
    out.append(
        f'<p class="meta">{inline(model["snapshot"])} This page is generated from the files of '
        f'<a href="{esc(REPOSITORY)}">{esc(REPOSITORY.split("//")[1])}</a>, which hold the '
        "evidence for every entry.</p>"
    )
    out.append("</header>")

    out += ['<section id="legend">', "<h2>Status</h2>"]
    for paragraph in intro:
        out.append(f"<p>{inline(paragraph)}</p>")
    out += [
        '<table class="legend">',
        "<thead><tr><th>Status</th><th>Meaning</th><th>Count</th></tr></thead>",
        "<tbody>",
    ]
    for status, meaning, count in legend:
        chip = badge(status, "button", f' type="button" data-status="{esc(status)}" '
                     'aria-pressed="false"')
        out.append(f'<tr><td>{chip}</td><td>{inline(meaning)}</td><td class="n">{esc(count)}</td></tr>')
    out += ["</tbody>", "</table>"]
    for paragraph in notes:
        out.append(f"<p>{inline(paragraph)}</p>")
    out.append("</section>")

    out += [
        '<div class="controls"><div class="row">',
        '<span class="tabs" role="group" aria-label="View">'
        '<button type="button" data-view="def" aria-pressed="true">By definition</button>'
        '<button type="button" data-view="rm" aria-pressed="false">By roadmap</button></span>',
        '<label for="q">Filter by text</label>'
        '<input id="q" type="search" placeholder="Filter: a word, a roadmap, a section">',
        '<label for="area">Area</label><select id="area"><option value="">All areas</option>',
    ]
    for area in areas:
        out.append(f'<option value="{esc(area)}">{esc(area)}</option>')
    out.append("</select>")
    out.append('<label for="status">Status</label><select id="status">'
               '<option value="">All statuses</option>')
    for status, _, _ in legend:
        out.append(f'<option value="{esc(status)}">{esc(status)}</option>')
    out += ["</select>", "</div>", '<p class="count" id="count" aria-live="polite"></p>', "</div>"]

    out += ['<main class="v-def">', '<section id="by-definition">', "<h2>By definition</h2>"]
    for area in areas:
        out += [
            '<section class="group">',
            f"<h3>{esc(area)}</h3>",
            '<table class="defs">',
            "<thead><tr><th>#</th><th>Definition</th><th>Status</th><th>Where</th></tr></thead>",
            "<tbody>",
        ]
        for row in rows:
            if row["area"] == area:
                out.append(render_definition(row, index, evidence))
        out += ["</tbody>", "</table>", "</section>"]
    out.append('<p class="empty" id="empty-def">No definition matches the filters.</p>')
    out.append("</section>")

    out += [
        '<section id="by-roadmap">',
        "<h2>By roadmap</h2>",
        "<p>Every roadmap and roadmap PR that the census cites, with a short description of "
        "what it contains and the definitions that cite it. The definitions listed first are "
        "those whose row in the table cites the roadmap, with the sections the row gives. "
        "Those listed as cited in the evidence have the roadmap in their census file only: "
        "there it can be a prerequisite, a neighbouring notion, or one the census found not to "
        "cover the definition. The area and status filters keep the roadmaps cited by a "
        "definition of that area and status.</p>",
    ]
    groups = [
        ("merged", "Merged roadmaps", ""),
        ("open", "Roadmaps in open PRs", ""),
        ("other", "Other cited PRs",
         "Pull requests that the census cites and that add no roadmap folder of their own."),
    ]
    for key, heading, note in groups:
        if not model[key]:
            continue
        out += ['<section class="group">', f"<h3>{esc(heading)} ({len(model[key])})</h3>"]
        if note:
            out.append(f"<p>{esc(note)}</p>")
        out += [
            '<table class="rms">',
            "<thead><tr><th>Roadmap</th><th>What it contains</th><th>Definitions</th></tr></thead>",
            "<tbody>",
        ]
        for item in model[key]:
            out.append(render_roadmap(item, by_number))
        out += ["</tbody>", "</table>", "</section>"]
    out.append('<p class="empty" id="empty-rm">No roadmap matches the filters.</p>')
    out += ["</section>", "</main>"]

    out += [
        "<footer>",
        f'<p>Generated by <a href="{esc(BLOB)}scripts/build_site.py">scripts/build_site.py</a> '
        f'from <a href="{esc(BLOB)}definitions.md">definitions.md</a>, the files in '
        f'<a href="{esc(REPOSITORY)}/tree/main/census">census/</a> and '
        f'<a href="{esc(BLOB)}{census.DESCRIPTIONS}">{census.DESCRIPTIONS}</a>. '
        "Every status is a judgment; the census files give the evidence.</p>",
        "</footer>",
        "</div>",
        f"<script>{JS}</script>",
        "</body>",
        "</html>",
    ]
    return "\n".join(out) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--check", action="store_true",
                        help=f"write nothing; fail if {OUTPUT} is stale")
    args = parser.parse_args(argv)
    try:
        text = render()
    except census.CensusError as err:
        print(f"error: {err}", file=sys.stderr)
        return 1
    path = ROOT / OUTPUT
    if args.check:
        if not path.is_file() or path.read_text(encoding="utf-8") != text:
            print(f"error: {OUTPUT} is stale; run python3 scripts/build_site.py", file=sys.stderr)
            return 1
        return 0
    path.parent.mkdir(exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
