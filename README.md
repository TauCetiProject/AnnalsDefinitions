# Annals definitions

Kevin Buzzard compiled a list of 100 definitions that Mathlib lacks and that are needed to *state*
the main theorems of Annals of Mathematics papers from 2020 to mid-2026 (see the Zulip thread
[Roadmaps for Annals theorem statements](https://leanprover.zulipchat.com/#narrow/channel/610393-Tau-Ceti/topic/Roadmaps.20for.20Annals.20theorem.20statements/with/637731475)).
Of the 207 papers, about 50 can already be stated importing only Mathlib. With these 100 definitions,
he estimates that about 50 more could be stated and about 60 more partly stated.

This repository tracks where each of those definitions stands with respect to
[Tau Ceti](https://github.com/TauCetiProject/TauCeti) and its
[roadmaps](https://github.com/TauCetiProject/TauCetiRoadmap). It is not a roadmap: roadmaps remain
the only specifications of work, and nothing here asks for a definition to be built outside the
theory it belongs to.

## Layout

```
README.md          this file
AGENTS.md          instructions for agents working from or on this repository
tasks/             what to do next, one file per kind of work; together they partition the 100
definitions.md     all 100 in one table
prerequisites.md   merged-roadmap work on the path to the definitions
papers.md          the Annals papers and the definitions each needs
census/NNN.md      the evidence, one file per definition
sources/           Kevin Buzzard's definition texts (markdown and PDF)
```

### `tasks/`

Every definition is in exactly one of these four files: the furthest-along one whose condition
holds for the definition as Kevin Buzzard's text states it. Gaps that matter only for a particular
paper are noted on the entry.

| File | Condition |
| --- | --- |
| [ready-to-write-statements.md](tasks/ready-to-write-statements.md) | The definition is in Mathlib or Tau Ceti code, in the generality its papers need, with basic API. Also lists the papers all of whose listed definitions are here. |
| [ready-to-formalize-in-tau-ceti.md](tasks/ready-to-formalize-in-tau-ceti.md) | A merged roadmap names the definition as a target, so implementation can be dispatched against it. |
| [needs-roadmap-review.md](tasks/needs-roadmap-review.md) | Only open roadmap PRs specify the definition. Listed by PR and by definition. |
| [needs-roadmap-written.md](tasks/needs-roadmap-written.md) | No roadmap or PR specifies the definition (or those that do cover only part of it). Grouped by the roadmap section or new roadmap that should cover it, with standard sources, a suggested order, and the further theory the papers need beyond the 100. |

### Supporting files

- [definitions.md](definitions.md) has one row per definition: a finer status (in code, partly in
  code, merged roadmap, roadmap PR, prerequisites planned, unplanned), the `tasks/` file it is in,
  and where in Mathlib, Tau Ceti or the roadmaps it lives.
- [prerequisites.md](prerequisites.md) lists the items that merged roadmaps specify, that Tau Ceti
  has not yet implemented, and that lie on the prerequisite chain of at least one definition. Each
  item gives its status, whether it can start now, and the definitions it serves.
- [papers.md](papers.md) lists the cited Annals papers, grouped by the least-advanced definition each
  one needs.
- [`census/NNN.md`](census/) holds the evidence for definition NNN under fixed headings: `Status`
  (the finer status on its first line), `Mathlib`, `Tau Ceti code`, `Merged roadmaps`,
  `Open roadmap PRs`, `Prerequisite chain`, `Library-scale gap`, `Papers`. Every other file is a view
  of these, so when they disagree the census file is the one to fix first.

## Sources

- **Definitions.** "100 definitions for Tau Ceti: textbook versions", 22 October 2026, by Kevin
  Buzzard's team, in [`sources/`](sources/) as
  [`definitions_100_v2_textbook.md`](sources/definitions_100_v2_textbook.md) and
  [`astra_definitions_100_v2.pdf`](sources/astra_definitions_100_v2.pdf), as attached to the Zulip
  thread above. Definition
  numbers, and references such as "Definition 56.3", are that document's. Its texts were drafted by
  AI agents and have not been reviewed by a human.
- **Papers.** The definition texts cite Annals papers as [year, volume(issue), no. n], resolved here
  to titles through Crossref. Only the papers named in each definition's "use in the Annals papers"
  remarks are linked, 71 in all. The full definition-to-paper map (`definitions_100_v2.md`) is not
  public, so [papers.md](papers.md) undercounts.
- **Snapshot.** The census describes Tau Ceti `main` at `c56184862`, Mathlib at Tau Ceti's pinned
  revision `e8ba86fa9744`, TauCetiRoadmap `main` at `e1cd6a508`, and the 467 roadmap PRs open on
  2026-11-14. It was carried out by Claude agents reading the code and the roadmaps. Every status is
  a judgment, and borderline calls are flagged in the census files.

See [AGENTS.md](AGENTS.md) for how to bring the repository up to date.
