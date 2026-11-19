# Ready to write statements

Snapshot 2026-11-19 (Tau Ceti `91942aa9f`, Mathlib `048fffa1dbcd`, roadmaps `890b66de0`, 350 open roadmap PRs).

Every one of the 100 definitions is in exactly one of four files: [ready-to-write-statements.md](ready-to-write-statements.md), [ready-to-formalize-in-tau-ceti.md](ready-to-formalize-in-tau-ceti.md), [needs-roadmap-review.md](needs-roadmap-review.md), [needs-roadmap-written.md](needs-roadmap-written.md). A definition is placed in the furthest-along file whose condition holds for the definition as Kevin Buzzard's text states it; gaps that matter only for a particular paper are noted on the entry.

**Condition:** the definition is in Mathlib or Tau Ceti code, in the generality its papers need, with basic API. A paper is ready when every one of the 100 it needs is here (necessary, not sufficient: it may need other notions too).

## Definitions

2 definitions.

- **#14 The volume form $\omega^n$ and integration on a compact Kähler (or Hermitian) manifold.** Code: `SmoothTwoForm.volumeForm` (ωⁿ/n!, `TauCeti/Geometry/Symplectic/Manifold/Volume.lean`), `SmoothTwoForm.liouvilleMeasure` (μ_ω = n!·`liouvilleMeasure`, `.../LiouvilleMeasure.lean`), `SmoothTwoForm.Compatible`, `SmoothTwoForm.IsKahler` (`.../Kahler.lean`). Not in code: the comparison with `riemannianVolume` ([ComplexKahlerGeometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/ComplexKahlerGeometry/README.md) §5.9; also [ComplexHessianEquations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/ComplexHessianEquations/README.md) §3.2) and the cohomological invariance of Proposition 14.4. The Guo–Phong statement's eigenvalue vector `λ[h_φ]` and admissible pairs `(f, Γ)` are [ComplexHessianEquations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/ComplexHessianEquations/README.md) §3.1 and §2.4.  
  Papers: [2023·198(1)·4] On $L^\infty$ estimates for complex Monge-Ampère equations; [2024·200(1)·6] On $L^\infty$ estimates for fully non-linear partial differential equations. [census](../census/014.md)
- **#63 Space of compatible almost complex structures.** Code: `SmoothAlmostComplexStructure.frameTopology` (the C^∞ topology, `TauCeti/Geometry/Symplectic/Manifold/AlmostComplex/Topology.lean`) and the subspaces `{J // ω.Compatible J}`, `{J // ω.Tames J}`, with Hausdorff, closed embedding into sections and independence of the covering frames; the ambient space of sections is completely metrizable and Baire (`ContMDiffSection.isCompletelyMetrizableSpace_frameTopology`, `baireSpace_frameTopology`, `TauCeti/Geometry/Manifold/VectorBundle/Section/CompletelyMetrizable.lean`). Not in code: completeness, the Baire property and contractibility of Proposition 63.4 ([HeegaardFloer](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/HeegaardFloer/README.md) §4.1, F2.1; complete metrizability and Baire for compact M in [AnalyticStableMaps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/AnalyticStableMaps/README.md) §2.1). The paper's genericity statements can be written with Mathlib `residual`.  
  Papers: [2023·198(1)·2] Transversality and super-rigidity for multiply covered holomorphic curves. [census](../census/063.md)

## Papers

1 paper all of whose listed definitions are here.

- [2024·200(1)·6] On $L^\infty$ estimates for fully non-linear partial differential equations (Guo, Phong), https://doi.org/10.4007/annals.2024.200.1.6: #14. Theorem 1 (the `L^∞` bound for `C²` solutions of `f(λ[h_φ]) = e^F` on a compact Hermitian manifold) also needs two notions not in code, both small and definable inline over Tau Ceti: the eigenvalue vector `λ[h_φ]` of `ω + i∂∂̄φ` relative to `ω`, and the admissible pair `(f, Γ)`. Merged [ComplexHessianEquations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/ComplexHessianEquations/README.md) specifies both (§3.1 `λ[α]`, §2.4 admissible pairs) ([census 014](../census/014.md), [census 038](../census/038.md)). The rest is `TauCeti.manifoldLeviForm` (`i∂∂̄φ` for `C²` `φ`), `SmoothTwoForm.liouvilleMeasure` and `SmoothAlmostComplexStructure.ofComplexManifold`. Venue: [lean-eval](https://github.com/leanprover/lean-eval), which depends on Tau Ceti, once its stable Tau Ceti pin includes `liouvilleMeasure` and `ofComplexManifold` (its rc pin does); formal-conjectures depends only on Mathlib and is not a fit.

The closest further definitions are ten with a special case or close variant in code (#4, #5, #6, #11, #12, #32, #50, #59, #92, #98); each is filed according to where the rest of it is specified.
