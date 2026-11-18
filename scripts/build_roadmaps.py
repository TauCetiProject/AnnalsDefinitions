#!/usr/bin/env python3
"""Generate roadmaps.md, the by-roadmap view of the census.

Inputs, all in this repository:

  README.md                the snapshot paragraph
  definitions.md           one row per definition; its "Where" column cites roadmaps and PRs
  census/NNN.md            the "Merged roadmaps" and "Open roadmap PRs" sections
  roadmap-descriptions.md  a title and a short description for each cited roadmap

Output: roadmaps.md.

Usage:

  python3 scripts/build_roadmaps.py           write roadmaps.md
  python3 scripts/build_roadmaps.py --check   fail if roadmaps.md is stale, or if a cited
                                              roadmap or PR has no description

Only the Python standard library is used, and the output depends on the input files alone.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = "roadmaps.md"
DESCRIPTIONS = "roadmap-descriptions.md"

ROADMAP_REPO = "https://github.com/TauCetiProject/TauCetiRoadmap"
FOLDER_LINK = re.compile(
    r"\[(?P<text>[^\[\]]+)\]\((?P<url>" + re.escape(ROADMAP_REPO)
    + r"/(?:blob|tree)/main/(?P<path>[^)\s#]+))\)"
)
PR_LINK = re.compile(
    r"\[#(?P<num>\d+)\]\((?P<url>" + re.escape(ROADMAP_REPO) + r"/pull/(?P=num))\)"
)
PR_URL = re.compile(re.escape(ROADMAP_REPO) + r"/pull/(\d+)")
# In a census file a PR is written "#N"; "#N" with N up to 100 refers to a definition.
PR_BARE = re.compile(r"(?<![\w/\[#])#(\d+)\b")
CITING_SECTIONS = ("Merged roadmaps", "Open roadmap PRs")


class CensusError(Exception):
    pass


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Reading the census
# ---------------------------------------------------------------------------

def snapshot_line():
    """The snapshot line of the views, built from the snapshot paragraph of README.md."""
    text = read("README.md")
    m = re.search(r"\*\*Snapshot\.\*\*(.*?)(?:\n\s*\n|\Z)", text, re.S)
    if not m:
        raise CensusError("README.md: no **Snapshot.** paragraph")
    para = " ".join(m.group(1).split())
    fields = {
        "tau_ceti": r"Tau Ceti `main` at `(\w+)`",
        "mathlib": r"Mathlib at Tau Ceti's pinned revision `(\w+)`",
        "roadmaps": r"TauCetiRoadmap `main` at `(\w+)`",
        "open_prs": r"the (\d+) roadmap PRs open on \d{4}-\d{2}-\d{2}",
        "date": r"roadmap PRs open on (\d{4}-\d{2}-\d{2})",
    }
    found = {}
    for name, pattern in fields.items():
        mm = re.search(pattern, para)
        if not mm:
            raise CensusError(f"README.md: cannot read '{name}' from the snapshot paragraph")
        found[name] = mm.group(1)
    return (
        "Snapshot {date} (Tau Ceti `{tau_ceti}`, Mathlib `{mathlib}`, roadmaps `{roadmaps}`, "
        "{open_prs} open roadmap PRs).".format(**found)
    )


def split_row(line):
    """The cells of a Markdown table row."""
    cells = re.split(r"(?<!\\)\|", line.strip())
    return [c.strip() for c in cells[1:-1]]


def read_definitions():
    """definitions.md as (legend, areas, rows).

    legend: the rows of the status table, as (status, meaning, count).
    areas:  the area headings, in order.
    rows:   one dict per definition: number, name, status, file, where, evidence, area.
    """
    legend, areas, rows = [], [], []
    area = None
    in_legend = False
    for line in read("definitions.md").splitlines():
        if line.startswith("## "):
            area = line[3:].strip()
            areas.append(area)
            continue
        if not line.startswith("|"):
            in_legend = False
            continue
        cells = split_row(line)
        if cells and cells[0] == "Status":
            in_legend = True
            continue
        if cells and set(cells[0]) <= set("-: "):
            continue
        if in_legend and len(cells) == 3:
            legend.append(tuple(cells))
            continue
        if len(cells) == 6 and cells[0].isdigit():
            rows.append(
                {
                    "number": int(cells[0]),
                    "name": cells[1],
                    "status": cells[2],
                    "file": cells[3],
                    "where": cells[4],
                    "evidence": cells[5],
                    "area": area,
                }
            )
    numbers = [r["number"] for r in rows]
    if numbers != sorted(set(numbers)) or not rows:
        raise CensusError("definitions.md: definition numbers are missing, repeated or unordered")
    for row in rows:
        if not (ROOT / census_path(row["number"])).is_file():
            raise CensusError(f"definitions.md: no census file for definition {row['number']}")
    return legend, areas, rows


def census_path(number):
    return f"census/{number:03d}.md"


def census_sections(number):
    """The text of each `## ` section of a census file, by heading."""
    sections, heading = {}, None
    for line in read(census_path(number)).splitlines():
        if line.startswith("## "):
            heading = line[3:].strip()
            sections[heading] = []
        elif heading is not None:
            sections[heading].append(line)
    return {h: "\n".join(lines) for h, lines in sections.items()}


def folder_key(path):
    """The roadmap folder named by the path of a link into TauCetiRoadmap main."""
    path = path.rstrip("/")
    if path.endswith("/README.md"):
        path = path[: -len("/README.md")]
    if path.startswith("TauCetiRoadmap/"):
        path = path[len("TauCetiRoadmap/"):]
    return path


# ---------------------------------------------------------------------------
# Sections quoted after a citation in the "Where" column
# ---------------------------------------------------------------------------

_CODE = r"(?:[A-Z]{1,3}(?:[-.]?[A-Z]?\d|\.[A-Z0-9])\w*(?:\.\w+)*|\d\w*(?:\.\w+)*)"
_RANGE = _CODE + r"(?:[–/]" + _CODE + r")?"
SECTION_TOKEN = re.compile(
    r"(?<![\w.])(?:§§?\s?" + _RANGE
    + r"|Layers?\s(?:\d+|[A-Z])(?:–\d+)?(?!\w)"
    + r"|Lane [A-Z] item \d+"
    + r"|" + _RANGE + r")(?![\w])"
)
_LEAD = re.compile(r"[A-Za-z]+(?: [A-Za-z]+){0,2}")
_ROADMAP_LIKE = re.compile(r"[A-Z][a-z]+[A-Z]")
_MASK = "\x00"


def _mask(text):
    """Replace code spans and balanced parentheticals by filler of the same length."""
    out = list(text)
    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if ch == "`":
            j = text.find("`", i + 1)
            if j < 0:
                break
            out[i:j + 1] = _MASK * (j + 1 - i)
            i = j + 1
        elif ch == "(":
            depth, j = 1, i + 1
            while j < n and depth:
                if text[j] == "`":
                    k = text.find("`", j + 1)
                    j = n if k < 0 else k
                elif text[j] == "(":
                    depth += 1
                elif text[j] == ")":
                    depth -= 1
                j += 1
            if depth:
                break
            out[i:j] = _MASK * (j - i)
            i = j
        else:
            i += 1
    return "".join(out)


def quoted_sections(tail):
    """The section references that open `tail`, the text following a citation.

    Reads comma-separated items for as long as each is a section reference (`§1.3`, `Layer 4`,
    `R5a.2`, ...), with the code span or parenthesis that glosses it, and stops at the first
    semicolon or at the first item that is prose.
    """
    masked = _mask(tail)
    stop = len(masked)
    for mark in (";", ")"):
        at = masked.find(mark)
        if at >= 0:
            stop = min(stop, at)
    tail, masked = tail[:stop], masked[:stop]

    kept, start = [], 0
    while start <= len(masked):
        end = masked.find(",", start)
        if end < 0:
            end = len(masked)
        item, item_masked = tail[start:end], masked[start:end]
        start = end + 1
        lead_space = len(item) - len(item.lstrip())
        item = item.strip()
        item_masked = item_masked[lead_space:lead_space + len(item)]
        if not item:
            if end >= len(masked):
                break
            continue
        tokens = list(SECTION_TOKEN.finditer(item_masked))
        if not tokens:
            only_gloss = not item_masked.replace(_MASK, "").strip()
            if only_gloss:
                kept.append(item)
                continue
            break
        lead = item_masked[: tokens[0].start()].strip()
        if lead and (not _LEAD.fullmatch(lead) or _ROADMAP_LIKE.search(lead)):
            break
        cut = max(tokens[-1].end(), item_masked.rfind(_MASK) + 1)
        kept.append(item[:cut].rstrip())
        if item_masked[cut:].strip():
            break
    return ", ".join(kept)


def where_citations(where):
    """The citations in a "Where" cell, in order, as (kind, id, url, sections).

    kind is "folder" (id: the roadmap folder) or "pr" (id: the PR number).
    """
    found = []
    for m in FOLDER_LINK.finditer(where):
        found.append((m.start(), m.end(), "folder", folder_key(m.group("path")), m.group("url")))
    for m in PR_LINK.finditer(where):
        found.append((m.start(), m.end(), "pr", int(m.group("num")), m.group("url")))
    found.sort()
    citations = []
    for i, (_, end, kind, ident, url) in enumerate(found):
        nxt = found[i + 1][0] if i + 1 < len(found) else len(where)
        citations.append((kind, ident, url, quoted_sections(where[end:nxt])))
    return citations


def evidence_citations(number):
    """Roadmap folders and PRs cited in a census file's citing sections.

    Returns (folders, prs): folders maps a folder to the URL the census links, prs is a set of
    PR numbers. PR numbers are read from "Open roadmap PRs" only: under "Merged roadmaps" a
    number names the PR that merged a roadmap the same line links.
    """
    sections = census_sections(number)
    folders, prs = {}, set()
    for heading in CITING_SECTIONS:
        if heading not in sections:
            raise CensusError(f"{census_path(number)}: no '## {heading}' section")
        text = sections[heading]
        for m in FOLDER_LINK.finditer(text):
            folders.setdefault(folder_key(m.group("path")), m.group("url"))
        if heading == "Open roadmap PRs":
            for m in PR_URL.finditer(text):
                prs.add(int(m.group(1)))
            for m in PR_BARE.finditer(text):
                if int(m.group(1)) > 100:
                    prs.add(int(m.group(1)))
    return folders, prs


# ---------------------------------------------------------------------------
# Reading the descriptions
# ---------------------------------------------------------------------------

def read_descriptions():
    """roadmap-descriptions.md as (roadmaps, other_prs).

    roadmaps:  folder -> {"title", "pr" (int or None), "description"}
    other_prs: PR number -> {"title", "description"}, for `## #N` entries
    """
    roadmaps, other_prs = {}, {}
    heading, block = None, []

    def close():
        if heading is None:
            return
        fields, prose = {}, []
        for line in block:
            m = re.fullmatch(r"(Title|PR):\s*(.+)", line.strip())
            if m and not prose:
                fields[m.group(1)] = m.group(2).strip()
            elif line.strip():
                prose.append(line.strip())
        where = f"{DESCRIPTIONS}: '## {heading}'"
        if "Title" not in fields:
            raise CensusError(f"{where} has no 'Title:' line")
        if not prose:
            raise CensusError(f"{where} has no description")
        entry = {"title": fields["Title"], "description": " ".join(prose)}
        pr_heading = re.fullmatch(r"#(\d+)", heading)
        if pr_heading:
            target, key = other_prs, int(pr_heading.group(1))
            if "PR" in fields:
                raise CensusError(f"{where} is a PR entry and takes no 'PR:' line")
        else:
            target, key = roadmaps, heading
            entry["pr"] = None
            if "PR" in fields:
                m = re.fullmatch(r"#(\d+)", fields["PR"])
                if not m:
                    raise CensusError(f"{where}: write the PR as 'PR: #N'")
                entry["pr"] = int(m.group(1))
        if key in target:
            raise CensusError(f"{where} appears twice")
        target[key] = entry

    for line in read(DESCRIPTIONS).splitlines():
        if line.startswith("#"):
            close()
            heading, block = (line[3:].strip() if line.startswith("## ") else None), []
        elif heading is not None:
            block.append(line)
    close()
    return roadmaps, other_prs


# ---------------------------------------------------------------------------
# The model: who cites what
# ---------------------------------------------------------------------------

def build_model():
    """Everything roadmaps.md shows.

    Returns a dict with:
      snapshot    the snapshot line
      rows        the rows of definitions.md, by number
      merged      entries for roadmaps the census links on TauCetiRoadmap main
      open        entries for roadmaps the census cites only by their PR
      other       entries for cited PRs that add no roadmap folder
      problems    citations without a description (the view is incomplete if not empty)
      unused      description headings that nothing cites

    An entry is a dict: name, url, state, title, description, cited (a list of
    (number, sections) from definitions.md) and evidence (the numbers of the further
    definitions whose census file cites it).
    """
    _, _, rows = read_definitions()
    by_number = {r["number"]: r for r in rows}
    roadmaps, other_prs = read_descriptions()

    pr_folders = {}
    for folder, entry in roadmaps.items():
        if entry["pr"] is not None:
            pr_folders.setdefault(entry["pr"], []).append(folder)
    for number in other_prs:
        if number in pr_folders:
            raise CensusError(
                f"{DESCRIPTIONS}: PR #{number} has its own entry and is the 'PR:' of "
                f"'## {pr_folders[number][0]}'"
            )

    main_url = {}      # folder -> the main link, as the census writes it
    cited = {}         # ("folder", name) or ("pr", N) -> {number: [sections, ...]}
    evidence = {}      # same keys -> set of numbers

    for row in rows:
        for kind, ident, url, sections in where_citations(row["where"]):
            if kind == "folder":
                main_url.setdefault(ident, url)
            cited.setdefault((kind, ident), {}).setdefault(row["number"], []).append(sections)
    for row in rows:
        folders, prs = evidence_citations(row["number"])
        for folder, url in folders.items():
            main_url.setdefault(folder, url)
            evidence.setdefault(("folder", folder), set()).add(row["number"])
        for number in prs:
            evidence.setdefault(("pr", number), set()).add(row["number"])

    problems = []
    for kind, ident in sorted(set(cited) | set(evidence), key=lambda k: (k[0], str(k[1]))):
        if kind == "folder" and ident not in roadmaps:
            problems.append(f"roadmap '{ident}' is cited and has no entry in {DESCRIPTIONS}")
        if kind == "pr" and ident not in pr_folders and ident not in other_prs:
            problems.append(f"PR #{ident} is cited and has no entry in {DESCRIPTIONS}")

    def gather(keys):
        table, extra = {}, set()
        for key in keys:
            for number, sections in cited.get(key, {}).items():
                table.setdefault(number, []).extend(s for s in sections if s)
            extra |= evidence.get(key, set())
        table_list = [(n, "; ".join(dict.fromkeys(table[n]))) for n in sorted(table)]
        return table_list, sorted(extra - set(table))

    merged, opened, other, unused = [], [], [], []
    for folder in sorted(roadmaps, key=lambda s: (s.lower(), s)):
        entry = roadmaps[folder]
        keys = [("folder", folder)]
        if entry["pr"] is not None:
            keys.append(("pr", entry["pr"]))
        table_list, extra = gather(keys)
        if not table_list and not extra:
            unused.append(folder)
            continue
        item = {
            "name": folder,
            "title": entry["title"],
            "description": entry["description"],
            "cited": table_list,
            "evidence": extra,
            "pr": entry["pr"],
        }
        if folder in main_url:
            item["url"], item["state"] = main_url[folder], "merged"
            merged.append(item)
        elif entry["pr"] is not None:
            item["url"] = f"{ROADMAP_REPO}/pull/{entry['pr']}"
            item["state"] = f"open PR #{entry['pr']}"
            opened.append(item)
        else:
            problems.append(
                f"'## {folder}' in {DESCRIPTIONS} has no 'PR:' line and the census does not "
                "link the folder on main"
            )
    for number in sorted(other_prs):
        entry = other_prs[number]
        table_list, extra = gather([("pr", number)])
        if not table_list and not extra:
            unused.append(f"#{number}")
            continue
        other.append(
            {
                "name": f"#{number}",
                "title": entry["title"],
                "description": entry["description"],
                "cited": table_list,
                "evidence": extra,
                "pr": number,
                "url": f"{ROADMAP_REPO}/pull/{number}",
                "state": "",
            }
        )
    return {
        "snapshot": snapshot_line(),
        "rows": by_number,
        "merged": merged,
        "open": opened,
        "other": other,
        "problems": problems,
        "unused": unused,
    }


# ---------------------------------------------------------------------------
# Writing roadmaps.md
# ---------------------------------------------------------------------------

def definition_link(row):
    return f"[#{row['number']} {row['name']}]({census_path(row['number'])})"


def render_entry(item, rows):
    lines = [f"### [{item['name']}]({item['url']})", ""]
    if item["state"]:
        state = item["state"][0].upper() + item["state"][1:]
        lines += [f"*{item['title']}.* {state}.", "", item["description"], ""]
    else:
        lines += [f"*{item['title']}.* {item['description']}", ""]
    for number, sections in item["cited"]:
        line = "- " + definition_link(rows[number])
        if sections:
            line += ": " + sections
        lines.append(line)
    if item["evidence"]:
        links = ", ".join(definition_link(rows[n]) for n in item["evidence"])
        lines.append(f"- Also cited in the evidence for {links}.")
    lines.append("")
    return lines


def render(model):
    rows = model["rows"]
    out = [
        "# The roadmaps the census cites",
        "",
        model["snapshot"],
        "",
        "Every roadmap and roadmap PR that [definitions.md](definitions.md) or a census file "
        "cites, with a short description of what it contains and the definitions that cite it. "
        "See [README.md](README.md) for sources and the snapshot this describes. This file is "
        "generated by [scripts/build_roadmaps.py](scripts/build_roadmaps.py) from "
        "[definitions.md](definitions.md), the files in [`census/`](census/) and "
        f"[{DESCRIPTIONS}]({DESCRIPTIONS}): edit those and run the script.",
        "",
        "A roadmap is *merged* when the census links its folder on TauCetiRoadmap `main`, and "
        "an *open PR* when the census cites only the pull request that adds it. Under each "
        "roadmap, the definitions whose row in [definitions.md](definitions.md) cites it come "
        "first, with the sections that row gives. \"Also cited in the evidence for\" lists the "
        "definitions whose census file links the roadmap, or cites its PR, under `Merged "
        "roadmaps` or `Open roadmap PRs` and whose row does not: there the roadmap can be a "
        "prerequisite, a neighbouring notion, or one the census found not to cover the "
        "definition, so read the census file.",
        "",
        "| Group | Count |",
        "| --- | --- |",
        f"| [Merged roadmaps](#merged-roadmaps) | {len(model['merged'])} |",
        f"| [Roadmaps in open PRs](#roadmaps-in-open-prs) | {len(model['open'])} |",
        f"| [Other cited PRs](#other-cited-prs) | {len(model['other'])} |",
        "",
        "",
        "## Merged roadmaps",
        "",
    ]
    for item in model["merged"]:
        out += render_entry(item, rows)
    out += ["", "## Roadmaps in open PRs", ""]
    for item in model["open"]:
        out += render_entry(item, rows)
    out += [
        "",
        "## Other cited PRs",
        "",
        "Pull requests that the census cites and that add no roadmap folder of their own.",
        "",
    ]
    for item in model["other"]:
        out += render_entry(item, rows)
    while out and not out[-1]:
        out.pop()
    return "\n".join(out) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help=f"write nothing; fail if {OUTPUT} is stale or a cited roadmap has no description",
    )
    args = parser.parse_args(argv)
    try:
        model = build_model()
    except CensusError as err:
        print(f"error: {err}", file=sys.stderr)
        return 1
    for name in model["unused"]:
        print(f"note: '## {name}' in {DESCRIPTIONS} is not cited by the census", file=sys.stderr)
    if model["problems"]:
        for problem in model["problems"]:
            print(f"error: {problem}", file=sys.stderr)
        return 1
    text = render(model)
    path = ROOT / OUTPUT
    if args.check:
        if not path.is_file() or path.read_text(encoding="utf-8") != text:
            print(f"error: {OUTPUT} is stale; run python3 scripts/build_roadmaps.py",
                  file=sys.stderr)
            return 1
        return 0
    path.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
