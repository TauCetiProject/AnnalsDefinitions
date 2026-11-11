# Ready to formalize in Tau Ceti

Snapshot 2026-11-11 (Tau Ceti `a6027b1d24fc`, Mathlib `1b1ccf4b088b`, roadmaps `5f7befb6`, 437 open roadmap PRs).

Every one of the 100 definitions is in exactly one of four files: [ready-to-write-statements.md](ready-to-write-statements.md), [ready-to-formalize-in-tau-ceti.md](ready-to-formalize-in-tau-ceti.md), [needs-roadmap-review.md](needs-roadmap-review.md), [needs-roadmap-written.md](needs-roadmap-written.md). A definition is placed in the furthest-along file whose condition holds for the definition as Kevin Buzzard's text states it; gaps that matter only for a particular paper are noted on the entry.

**Condition:** a merged roadmap names the definition as a target, so implementation work can be dispatched against the roadmap now. Implementation status of every merged-roadmap item involved is in [prerequisites.md](../prerequisites.md), which also lists the merged-roadmap prerequisites of definitions filed elsewhere.

## Definitions

9 definitions.

- **#14 The volume form $\omega^n$ and integration on a compact Kähler (or Hermitian) manifold.** [ComplexKahlerGeometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/ComplexKahlerGeometry/README.md) §5.9 (`dvol_g = ωⁿ/n!`), §6.1.  
  Papers: [2023·198(1)·4] On $L^\infty$ estimates for complex Monge-Ampère equations; [2024·200(1)·6] On $L^\infty$ estimates for fully non-linear partial differential equations. [census](../census/014.md)
- **#18 Cup product in étale cohomology.** [EtaleCohomologyFoundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/EtaleCohomologyFoundations/README.md) §F.1 (schemes). The paper uses the rigid-analytic case, as do PRs [#875](https://github.com/TauCetiProject/TauCetiRoadmap/pull/875) and [#1549](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1549).  
  Papers: [2025·201(3)·2] Mod-$p$ Poincaré Duality in $p$-adic analytic geometry. [census](../census/018.md)
- **#28 Points of an algebraic stack.** [SchemeAndStackFoundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/SchemeAndStackFoundations/README.md) §1.20 (`Stacks.points`, `automorphismGroup`).  
  Papers: [2020·191(3)·1] A Luna étale slice theorem for algebraic stacks. [census](../census/028.md)
- **#30 Theta divisor of a Jacobian.** [JacobianChallenge](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/JacobianChallenge/README.md) Layers C, E; relative Θ in PR [#1225](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1225) Layer 3. The relative theta divisor the paper uses is in PR [#1225](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1225) Layer 3.  
  Papers: [2026·203(1)·2] Arithmetic bigness and a uniform Bogomolov-type result. [census](../census/030.md)
- **#32 The spaces $C^k(M)$ and $C^{k,\alpha}(M)$ on a compact manifold.** Code: C^k(M) Banach space, Hölder spaces on metric spaces; C^{k,α}(M) in [PseudodifferentialOperators](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/PseudodifferentialOperators/README.md) §5.4.  
  Papers: [2023·197(1)·2] Smooth mixing Anosov flows in dimension three are exponentially mixing; [2023·198(1)·3] Naked singularities for the Einstein vacuum equations: The exterior solution; [2024·199(3)·5] Exponential mixing implies Bernoulli. [census](../census/032.md)
- **#49 Second fundamental form, principal curvatures and mean curvature of a hypersurface.** [RiemannianGeometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/RiemannianGeometry/README.md) R5a, R5a.2 (Euclidean case in code).  
  Papers: [2020·191(1)·4] Minimal surfaces and the Allen--Cahn equation on 3-manifolds: index, multiplicity, and curvature estimates; [2020·192(2)·2] Uniqueness of two-convex closed ancient solutions to the mean curvature flow; [2020·192(3)·3] On the Multiplicity One Conjecture in min-max theory; [2021·194(1)·1] Local and global boundary rigidity and the geodesic X-ray transform in the normal gauge; [2023·197(3)·4] Stable minimal hypersurfaces in ℝ^N+1+ℓ with singular set an arbitrary closed K⊂{0}×ℝ^ℓ; [2025·202(1)·2] Weil-Petersson curves, $\beta$-numbers, and minimal surfaces. [census](../census/049.md)
- **#52 Minimal hypersurface in a Riemannian manifold.** [RiemannianGeometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/RiemannianGeometry/README.md) R5a.2, R5b.  
  Papers: [2020·191(1)·4] Minimal surfaces and the Allen--Cahn equation on 3-manifolds: index, multiplicity, and curvature estimates; [2020·192(3)·3] On the Multiplicity One Conjecture in min-max theory; [2023·197(3)·1] Existence of infinitely many minimal hypersurfaces in closed manifolds; [2025·202(1)·2] Weil-Petersson curves, $\beta$-numbers, and minimal surfaces. [census](../census/052.md)
- **#63 Space of compatible almost complex structures.** [HeegaardFloer](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/HeegaardFloer/README.md) §4.1 (F2.1).  
  Papers: [2023·198(1)·2] Transversality and super-rigidity for multiply covered holomorphic curves. [census](../census/063.md)
- **#92 Billiard ball map of a convex billiard table.** [CotangentLagrangian](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/SymplecticGeometry/CotangentLagrangian/README.md) C3.1 ([SymplecticGeometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/SymplecticGeometry/README.md)). The paper needs C^2 tables (the roadmap specifies C^∞) and rotational invariant curves (92.5).  
  Papers: [2022·196(1)·2] The Birkhoff-Poritsky conjecture for centrally-symmetric billiard tables. [census](../census/092.md)
