# Needs roadmap written

Snapshot 2026-11-22 (Tau Ceti `93a012eae`, Mathlib `31ce06eaadf4`, roadmaps `886c89ef3`, 495 open roadmap PRs).

Every one of the 100 definitions is in exactly one of four files: [ready-to-write-statements.md](ready-to-write-statements.md), [ready-to-formalize-in-tau-ceti.md](ready-to-formalize-in-tau-ceti.md), [needs-roadmap-review.md](needs-roadmap-review.md), [needs-roadmap-written.md](needs-roadmap-written.md). A definition is placed in the furthest-along file whose condition holds for the definition as Kevin Buzzard's text states it; gaps that matter only for a particular paper are noted on the entry.

**Condition:** neither a merged roadmap nor an open PR names the definition as a target (or the ones that do cover only part of it). Something has to be written: a section of an existing roadmap or PR, or a new roadmap. Either way the unit of work is the theory the definition belongs to, not the definition. The groupings are proposals; each census file's "Library-scale gap" describes the theory in more detail.

Order: the two extensions are independent of one another. No new roadmap is needed for any of the 100.

## Extend an existing roadmap or PR

2 definitions.


### Classical split groups (ReductiveGroups or ChevalleyGroups)

Sources: Knus–Merkurjev–Rost–Tignol, *The Book of Involutions*, §§12–13, 23.

- **#11 Split classical groups $\mathrm{Sp}_{2n}$, $\mathrm{SO}_l$ and general spin groups $\mathrm{GSpin}_l$.** Code: `Sp₂ₘ` pinned group scheme, `SOₙ` of the identity form. Merged [AutomorphicLFunctionsAndLocalFactorsPartII](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/AutomorphicLFunctionsAndLocalFactorsPartII/README.md) §0.0 constructs `GSpin_c` over characteristic-0 fields with a pinned root datum, without Definition 11.2's root datum, the spinor norm `ν` or the sequence `1 → G_m → GSpin → SO → 1`; its input MetaplecticAutomorphicForms §3.2a is merged; §0.3 fixes pinnings of split `Sp_c`, `SO_c`, `GSpin_c`. Open Tau Ceti PR https://git.taucetiproject.org/TauCetiProject/TauCeti/pulls/2348 constructs the group of points `GSpin(Q)` with `e₀∨` and the exact sequence on points over a field. Missing: the split `SO_l` of `J_l` as a pinned group and GSpin as a group scheme over a general base.  
  Papers: [2024·200(3)·2] Doubling constructions: Global functoriality for non-generic cuspidal representations. [census](../census/011.md)

### Characteristic data for compressible Euler (Part II of PR #2442)

Sources: Christodoulou–Miao, *Compressible Flow and Euler's Equations*; Christodoulou, *The Formation of Shocks in 3-Dimensional Fluids*; Luo–Yu 2023, Definition 2.13.

PR [#2442](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2442) (CompressibleEulerEquations) specifies the Euler systems, `Hᵏ` well-posedness, developments of data on open subsets of a slice, maximal developments and the nullity of their regular boundary, on PR [#2232](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2232) and PR [#2246](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2246). It shows that Proposition 33.4's uniqueness claim fails in general, and leaves characteristic data and the null-geodesic ruling of the boundary to a Part II.

- **#33 Domain of dependence and development of initial data for the compressible Euler equations.** PR [#2442](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2442) §§1.2, 3.1–3.3 (33.1–33.2), §8.1 (developments of type (i) data), §8.2 (maximal developments; uniqueness only under its criterion), §8.4 (null regular boundary); acoustical metric and `D⁺_D(S)` also PR [#2232](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2232) §7.3, §12.6. Characteristic data (33.3 (ii)) and the ruling of the characteristic boundary by null geodesics remain.  
  Papers: [2025·202(2)·2] On the stability of multi-dimensional rarefaction waves I: the energy estimates; [2025·202(2)·3] On the stability of multi-dimensional rarefaction waves II: existence of solutions and applications to the Riemann problem. [census](../census/033.md)

## Beyond the 100

The cited papers also need theory that is not among the 100 definitions and that no roadmap plans: Deligne–Lusztig theory of finite reductive groups (for #2's and #8's papers; Digne–Michel, *Representations of Finite Groups of Lie Type*), algebraic toric varieties over an arbitrary field (#26), Margulis superrigidity (#68), Sen theory (#77), torus and cosection localization of virtual classes (#27), and the regularity theory of singular minimal hypersurfaces beyond strict stability (Hardt–Simon foliations, uniqueness of tangent cones; #65). The census files record these under "Library-scale gap".
