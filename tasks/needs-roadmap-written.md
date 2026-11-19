# Needs roadmap written

Snapshot 2026-11-19 (Tau Ceti `91942aa9f`, Mathlib `048fffa1dbcd`, roadmaps `890b66de0`, 350 open roadmap PRs).

Every one of the 100 definitions is in exactly one of four files: [ready-to-write-statements.md](ready-to-write-statements.md), [ready-to-formalize-in-tau-ceti.md](ready-to-formalize-in-tau-ceti.md), [needs-roadmap-review.md](needs-roadmap-review.md), [needs-roadmap-written.md](needs-roadmap-written.md). A definition is placed in the furthest-along file whose condition holds for the definition as Kevin Buzzard's text states it; gaps that matter only for a particular paper are noted on the entry.

**Condition:** neither a merged roadmap nor an open PR names the definition as a target (or the ones that do cover only part of it). Something has to be written: a section of an existing roadmap or PR, or a new roadmap. Either way the unit of work is the theory the definition belongs to, not the definition. The groupings are proposals; each census file's "Library-scale gap" describes the theory in more detail.

Order: the extensions are independent of one another. The one new roadmap, filling invariants, consumes merged GeometricCurrents.

## Extend an existing roadmap or PR

5 definitions.


### Classical split groups (ReductiveGroups or ChevalleyGroups)

Sources: Knus–Merkurjev–Rost–Tignol, *The Book of Involutions*, §§12–13, 23.

- **#11 Split classical groups $\mathrm{Sp}_{2n}$, $\mathrm{SO}_l$ and general spin groups $\mathrm{GSpin}_l$.** Code: `Sp₂ₘ` pinned group scheme, `SOₙ` of the identity form. Merged [AutomorphicLFunctionsAndLocalFactorsPartII](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/AutomorphicLFunctionsAndLocalFactorsPartII/README.md) §0.0 constructs `GSpin_c` over characteristic-0 fields with a pinned root datum, without Definition 11.2's root datum, the spinor norm `ν` or the sequence `1 → G_m → GSpin → SO → 1`, and needs MetaplecticAutomorphicForms §3.2a from open PR [#1063](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1063); §0.3 fixes pinnings of split `Sp_c`, `SO_c`, `GSpin_c`. Missing: the split `SO_l` of `J_l` as a pinned group and GSpin over a general base.  
  Papers: [2024·200(3)·2] Doubling constructions: Global functoriality for non-generic cuspidal representations. [census](../census/011.md)

### Stacks and moduli (SchemeAndStackFoundations)

Sources: Alper, *Good moduli spaces for Artin stacks*.

Cohomologically affine morphisms and good moduli spaces after §§1.22–1.23.

- **#17 Cohomologically affine morphisms of algebraic stacks.** [SchemeAndStackFoundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/SchemeAndStackFoundations/README.md) §1.22 (`QCoh.pushforward`), §1.23; the Luna-slice local data (normal spaces `N_x`) in merged [StackPointsAndResidualGerbes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/StackPointsAndResidualGerbes/README.md) Layer 7.  
  Papers: [2020·191(3)·1] A Luna étale slice theorem for algebraic stacks. [census](../census/017.md)

### Singular minimal hypersurfaces and minimal cones (RiemannianGeometry R5b, on Varifolds)

Sources: Simon, *Introduction to Geometric Measure Theory*; Hardt–Simon 1985.

Merged [Varifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/Varifolds/README.md) specifies the stationary varifold of a smooth hypersurface, its singular set and tangent cones, and states Simon's theorem without its strict-stability clause.

- **#65 Strict stability of a minimal cone/hypersurface (Simon's inequality).** [RiemannianGeometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/RiemannianGeometry/README.md) R5a.2, R5b; [Varifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/Varifolds/README.md) §§2.3, 4.3, 9.1, 9.4 for the stationary varifold and singular set (strict stability not restated).  
  Papers: [2023·197(3)·4] Stable minimal hypersurfaces in ℝ^N+1+ℓ with singular set an arbitrary closed K⊂{0}×ℝ^ℓ. [census](../census/065.md)

### Normal operators of pseudoholomorphic curves (TaubesGromov, HeegaardFloer)

Sources: McDuff–Salamon, *J-holomorphic Curves and Symplectic Topology*, Ch. 3; Wendl, *Automatic transversality and orbifolds of punctured holomorphic curves in dimension four* (Comment. Math. Helv. 85 (2010)), §3.3.

- **#60 Normal Cauchy–Riemann operator of a J-holomorphic curve.** [TaubesGromov](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/TaubesGromov/README.md) TG1, [HeegaardFloer](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/HeegaardFloer/README.md) F2.6e (embedded case); finite critical sets in HeegaardFloer F2.2a and [AnalyticStableMaps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/AnalyticStableMaps/README.md) §0.4. Code: the local normal linearization, covariant under target and source coordinate changes, with its elliptic real CR symbol, and isolated point preimages of J-curves. Missing: the generalised normal bundle through critical points.  
  Papers: [2023·198(1)·2] Transversality and super-rigidity for multiply covered holomorphic curves. [census](../census/060.md)

### Characteristic data for compressible Euler (Part II of PR #2442)

Sources: Christodoulou–Miao, *Compressible Flow and Euler's Equations*; Christodoulou, *The Formation of Shocks in 3-Dimensional Fluids*; Luo–Yu 2023, Definition 2.13.

PR [#2442](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2442) (CompressibleEulerEquations) specifies the Euler systems, `Hᵏ` well-posedness, developments of data on open subsets of a slice, maximal developments and the nullity of their regular boundary, on PR [#2232](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2232) and PR [#2246](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2246). It shows that Proposition 33.4's uniqueness claim fails in general, and leaves characteristic data and the null-geodesic ruling of the boundary to a Part II.

- **#33 Domain of dependence and development of initial data for the compressible Euler equations.** PR [#2442](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2442) §§1.2, 3.1–3.3 (33.1–33.2), §8.1 (developments of type (i) data), §8.2 (maximal developments; uniqueness only under its criterion), §8.4 (null regular boundary); acoustical metric and `D⁺_D(S)` also PR [#2232](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2232) §7.3, §12.6. Characteristic data (33.3 (ii)) and the ruling of the characteristic boundary by null geodesics remain.  
  Papers: [2025·202(2)·2] On the stability of multi-dimensional rarefaction waves I: the energy estimates; [2025·202(2)·3] On the stability of multi-dimensional rarefaction waves II: existence of solutions and applications to the Riemann problem. [census](../census/033.md)

## New roadmaps

1 definition.


### Filling invariants

Sources: Gromov, *Filling Riemannian Manifolds*; Bridson, *The Geometry of the Word Problem*. Neighbour: GeometricCurrents.

- **#57 Lipschitz singular chains and their mass.** [GeometricCurrents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/GeometricCurrents/README.md) G1–G3; [GeometricMeasureTheory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/GeometricMeasureTheory/README.md) G2.  
  Papers: [2021·193(3)·2] Filling functions of arithmetic groups. [census](../census/057.md)

## Beyond the 100

The cited papers also need theory that is not among the 100 definitions and that no roadmap plans: Deligne–Lusztig theory of finite reductive groups (for #2's and #8's papers; Digne–Michel, *Representations of Finite Groups of Lie Type*), algebraic toric varieties over an arbitrary field (#26), Margulis superrigidity (#68), Sen theory (#77), and torus and cosection localization of virtual classes (#27). The census files record these under "Library-scale gap".
