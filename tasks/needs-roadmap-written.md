# Needs roadmap written

Snapshot 2026-11-23 (Tau Ceti `b958110ba`, Mathlib `31ce06eaadf4`, roadmaps `886c89ef3`, 495 open roadmap PRs).

Every one of the 100 definitions is in exactly one of four files: [ready-to-write-statements.md](ready-to-write-statements.md), [ready-to-formalize-in-tau-ceti.md](ready-to-formalize-in-tau-ceti.md), [needs-roadmap-review.md](needs-roadmap-review.md), [needs-roadmap-written.md](needs-roadmap-written.md). A definition is placed in the furthest-along file whose condition holds for the definition as Kevin Buzzard's text states it; gaps that matter only for a particular paper are noted on the entry.

**Condition:** neither a merged roadmap nor an open PR names the definition as a target (or the ones that do cover only part of it). Something has to be written: a section of an existing roadmap or PR, or a new roadmap. Either way the unit of work is the theory the definition belongs to, not the definition. The groupings are proposals; each census file's "Library-scale gap" describes the theory in more detail.

No new roadmap is needed for any of the 100.

## Extend an existing roadmap or PR

1 definition.


### Characteristic data for compressible Euler (Part II of PR #2442)

Sources: Christodoulou–Miao, *Compressible Flow and Euler's Equations*; Christodoulou, *The Formation of Shocks in 3-Dimensional Fluids*; Luo–Yu 2023, Definition 2.13.

PR [#2442](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2442) (CompressibleEulerEquations) specifies the Euler systems, `Hᵏ` well-posedness, developments of data on open subsets of a slice, maximal developments and the nullity of their regular boundary, on PR [#2232](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2232) and PR [#2246](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2246). It shows that Proposition 33.4's uniqueness claim fails in general, and leaves characteristic data and the null-geodesic ruling of the boundary to a Part II.

- **#33 Domain of dependence and development of initial data for the compressible Euler equations.** PR [#2442](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2442) §§1.2, 3.1–3.3 (33.1–33.2), §8.1 (developments of type (i) data), §8.2 (maximal developments; uniqueness only under its criterion), §8.4 (null regular boundary); acoustical metric and `D⁺_D(S)` also PR [#2232](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2232) §7.3, §12.6. Characteristic data (33.3 (ii)) and the ruling of the characteristic boundary by null geodesics remain.  
  Papers: [2025·202(2)·2] On the stability of multi-dimensional rarefaction waves I: the energy estimates; [2025·202(2)·3] On the stability of multi-dimensional rarefaction waves II: existence of solutions and applications to the Riemann problem. [census](../census/033.md)

## Beyond the 100

The cited papers also need theory that is not among the 100 definitions and that no roadmap plans: Deligne–Lusztig theory of finite reductive groups (for #2's and #8's papers; Digne–Michel, *Representations of Finite Groups of Lie Type*), algebraic toric varieties over an arbitrary field (#26), Margulis superrigidity (#68), Sen theory (#77), torus and cosection localization of virtual classes (#27), and the regularity theory of singular minimal hypersurfaces beyond strict stability (Hardt–Simon foliations, uniqueness of tangent cones; #65). The census files record these under "Library-scale gap".
