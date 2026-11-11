# Agents

Read [README.md](README.md) first: it describes what each file holds.

## Working on Tau Ceti

Pick work from [tasks/ready-to-formalize-in-tau-ceti.md](tasks/ready-to-formalize-in-tau-ceti.md).
Every definition there is a target of a merged roadmap. The roadmap items on the way to it, with
their status and whether each can start now, are in [prerequisites.md](prerequisites.md), and the
definition's census file has the full prerequisite chain. Work on the roadmap item, in the roadmap's
order and at the roadmap's generality, not on the Annals definition in isolation.

Prepare pull requests to Tau Ceti by following its
[AGENTS.md](https://github.com/TauCetiProject/TauCeti/blob/main/AGENTS.md) and
[README.md](https://github.com/TauCetiProject/TauCeti/blob/main/README.md).

Definitions in the other `tasks/` files are not ready for Tau Ceti code: they need a roadmap
reviewed or written first.

## Writing statements

When [tasks/ready-to-write-statements.md](tasks/ready-to-write-statements.md) lists a paper, every
one of the 100 definitions it needs is formalized. Formalize the paper's main theorem statements and
contribute them to [lean-eval](https://github.com/leanprover/lean-eval) or
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures), following that
repository's contribution instructions. Check first that the statement does not need further
notions that are missing; if it does, record them in the definitions' census files.

## Reviewing or writing roadmaps

To help someone find roadmap work matching their expertise, ask about their area, then look in
[tasks/needs-roadmap-review.md](tasks/needs-roadmap-review.md) (open roadmap PRs to review, listed by
PR) and [tasks/needs-roadmap-written.md](tasks/needs-roadmap-written.md) (sections to add to
existing roadmaps, and new roadmaps, with sources). Weigh how many definitions each item serves, and
for new roadmaps the suggested order at the top of that file. The census files' "Library-scale gap"
sections describe the theory involved.

Roadmap review and writing follow TauCetiRoadmap's
[README.md](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/README.md) (especially
"Writing a roadmap") and
[CONTRIBUTING.md](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/CONTRIBUTING.md). A
roadmap covers a whole theory, not just the definitions listed here.

## Updating the repository

The census describes a snapshot, recorded in [README.md](README.md#sources). To bring it up to date:

1. **Get the sources locally.** Clone Tau Ceti and TauCetiRoadmap, check out Mathlib at the revision
   in Tau Ceti's `lake-manifest.json`, and fetch every roadmap PR with
   `git fetch origin '+refs/pull/*/head:refs/remotes/origin/pr/*'` in the TauCetiRoadmap clone.
   Search the clones rather than the GitHub API, which rate-limits a census of this size.
2. **Find what moved.** Since the previous snapshot, look for: roadmap PRs that merged or closed
   (every PR cited in [tasks/needs-roadmap-review.md](tasks/needs-roadmap-review.md) and in the
   census files); new roadmaps and roadmap PRs; Tau Ceti code for the items in
   [prerequisites.md](prerequisites.md) (check the code, since `STATUS.md` files can lag); and new
   Mathlib declarations for the definitions.
3. **Update the census files first.** For each affected definition, rewrite the sections of
   `census/NNN.md` to describe the current state, with evidence: Lean declaration names and file
   paths, roadmap sections, PR numbers. Re-decide the status on the first line of `## Status`.
4. **Then update the views from the census files.**
   - Move the definition to the right `tasks/` file, by the placement rule in
     [README.md](README.md#tasks).
   - Update its row in [definitions.md](definitions.md).
   - Update [prerequisites.md](prerequisites.md): drop finished items, update the status and
     readiness of the others, and add items for newly merged roadmaps.
   - Regroup [papers.md](papers.md) if a paper's least-advanced definition changed.
5. **Update the snapshot** in [README.md](README.md#sources).

Write every file as a description of the current state. Do not record history: no "previously",
"reclassified", "was wrong", or notes about the update itself; git keeps that. State what exists and
where. Say what is missing only when it decides where a definition is placed or what a paper still
needs.
