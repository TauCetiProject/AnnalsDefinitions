# Merged-roadmap work on the prerequisite chains of the 100 Annals definitions

Specified in a merged roadmap (`TauCetiRoadmap/<Name>/` at roadmap commit 890b66d, 2026-11-19), not
yet (fully) implemented in Tau Ceti main (91942aa, 2026-11-19), and on the prerequisite chain of at
least one definition. Each item was checked against the README section, STATUS.md (snapshot date
given per roadmap; several are stale) and a grep of Tau Ceti code. Item format: status
(NOT-STARTED / PARTIAL with what exists), ready now (yes / no: needs X), definitions served,
evidence. Section and layer ids are the roadmap's own.

## Summary: roadmaps ranked by number of the 100 definitions served

Counts exclude items found DONE. "Ready now" counts items whose verdict begins "yes" (some are "yes for a named sub-part"; see the item).

| Roadmap | # defs served | Items (not-started / partial) | Ready now | Definitions served |
|---|---|---|---|---|
| SchemeAndStackFoundations | 16 | 35 (20 / 15) | 15 | 16, 17, 19, 20, 21, 24, 25, 26, 27, 28, 29, 30, 71, 80, 84, 85 |
| AutomorphicFormsOnReductiveGroups | 13 | 7 (7 / 0) | 4 | 1, 4, 5, 7, 67, 72, 73, 76, 79, 83, 86, 88, 90 |
| ArithmeticLocallySymmetricSpaces | 12 | 3 (3 / 0) | 0 | 1, 4, 7, 62, 67, 72, 73, 76, 77, 79, 88, 90 |
| AbelianSchemesAndArithmeticModuli | 11 | 6 (6 / 0) | 1 | 12, 13, 23, 70, 71, 74, 78, 80, 85, 87, 89 |
| AdelicAlgebraicGroups | 10 | 8 (8 / 0) | 1 | 15, 31, 67, 68, 73, 76, 77, 83, 88, 90 |
| RepresentationTheory/LieGroups | 10 | 4 (1 / 3) | 2 | 1, 4, 5, 7, 15, 31, 54, 62, 79, 83 |
| RiemannianGeometry | 10 | 9 (6 / 3) | 4 | 15, 31, 37, 38, 48, 49, 52, 62, 65, 66 |
| ReductiveGroupsPartII | 8 | 3 (2 / 1) | 2 | 11, 67, 68, 73, 82, 83, 88, 90 |
| ComplexComparisonPartII | 7 | 4 (4 / 0) | 0 | 12, 13, 15, 23, 74, 85, 89 |
| RealSemisimpleLieGroups | 7 | 5 (5 / 0) | 2 | 1, 4, 15, 31, 54, 62, 79 |
| ShimuraVarieties | 7 | 5 (5 / 0) | 2 | 13, 15, 23, 31, 70, 75, 89 |
| JacobianChallenge | 6 | 4 (0 / 4) | 2 | 19, 30, 71, 80, 84, 85 |
| ReductiveGroups | 6 | 5 (3 / 2) | 1 | 1, 4, 11, 23, 68, 79 |
| SmoothBundlesConnections | 6 | 3 (1 / 2) | 1 | 15, 31, 37, 48, 49, 62 |
| SmoothRepresentationsOfLocalGroups | 6 | 5 (3 / 2) | 2 | 67, 73, 83, 86, 88, 90 |
| EtaleCohomologyFoundations | 5 | 7 (5 / 2) | 2 | 18, 19, 69, 77, 84 |
| LieGroupsPartII | 4 | 4 (3 / 1) | 1 | 1, 4, 54, 79 |
| ModularCurves | 4 | 2 (1 / 1) | 1 | 25, 26, 69, 71 |
| NeronModelsAndSemistableAbelianVarieties | 4 | 8 (8 / 0) | 1 | 78, 85, 87, 89 |
| OperatorTheory/UnboundedOperators | 4 | 5 (3 / 2) | 2 | 34, 35, 40, 45 |
| StackPointsAndResidualGerbes | 4 | 8 (8 / 0) | 0 | 16, 17, 28, 29 |
| AlgebraicModuliForArithmeticGeometry | 3 | 2 (2 / 0) | 1 | 25, 26, 29 |
| AnalyticStableMaps | 3 | 3 (2 / 1) | 1 | 56, 60, 63 |
| GeometricCurrents | 3 | 3 (2 / 1) | 0 | 53, 57, 65 |
| GeometricMeasureTheory | 3 | 2 (0 / 2) | 2 | 53, 55, 57 |
| HeegaardFloer | 3 | 5 (2 / 3) | 1 | 56, 60, 64 |
| JacobianChallengePartII | 3 | 6 (6 / 0) | 0 | 30, 71, 80 |
| ModularCurvesPartII | 3 | 8 (8 / 0) | 1 | 69, 71, 77 |
| PELModuli | 3 | 4 (4 / 0) | 1 | 23, 70, 82 |
| RepresentationTheory/LieHighestWeight | 3 | 1 (1 / 0) | 1 | 5, 7, 88 |
| RepresentationTheory/ModularCharactersAndBlocks | 3 | 5 (5 / 0) | 2 | 2, 3, 9 |
| ShimuraData | 3 | 1 (1 / 0) | 0 | 13, 23, 89 |
| SobolevMapsBetweenManifolds | 3 | 5 (5 / 0) | 1 | 41, 42, 47 |
| Varifolds | 3 | 10 (10 / 0) | 2 | 52, 53, 65 |
| VonNeumannAlgebras | 3 | 3 (3 / 0) | 1 | 15, 31, 36 |
| ArakelovGeometryAndAbelianHeights | 2 | 4 (4 / 0) | 1 | 80, 85 |
| ArithmeticGaloisRepresentations | 2 | 3 (2 / 1) | 3 | 69, 89 |
| AutomorphicLFunctionsAndLocalFactors | 2 | 3 (3 / 0) | 0 | 72, 88 |
| AutomorphicLFunctionsAndLocalFactorsPartII | 2 | 1 (1 / 0) | 0 | 11, 88 |
| BallQuotientsAndComplexHyperbolicLattices | 2 | 3 (3 / 0) | 0 | 15, 31 |
| CharacteristicClasses | 2 | 2 (2 / 0) | 0 | 37, 48 |
| ComplexKahlerGeometry | 2 | 4 (2 / 2) | 1 | 38, 40 |
| CountableStructureSpaces | 2 | 4 (1 / 3) | 3 | 94, 98 |
| CStarAlgebras | 2 | 9 (5 / 4) | 5 | 36, 46 |
| DerivedModuleAlgebra | 2 | 2 (2 / 0) | 0 | 27, 81 |
| DiracScatteringAndNonlinearFourierTransform | 2 | 4 (4 / 0) | 2 | 43, 44 |
| EnhancedDerivedSheaves | 2 | 1 (0 / 1) | 0 | 18, 27 |
| GaloisActionOnEtaleCohomology | 2 | 3 (3 / 0) | 1 | 18, 22 |
| GeometricTopology | 2 | 3 (1 / 2) | 1 | 59, 66 |
| IntegralHeckeAndGaloisDeterminants | 2 | 1 (1 / 0) | 0 | 69, 88 |
| MathematicalBilliards | 2 | 5 (5 / 0) | 4 | 92, 93 |
| NashBlowups | 2 | 12 (12 / 0) | 4 | 25, 26 |
| NoncompactQuantumSymmetry | 2 | 1 (1 / 0) | 0 | 1, 4 |
| OperatorTheory/SelfAdjointSpectralTheory | 2 | 1 (1 / 0) | 1 | 35, 45 |
| PseudodifferentialOperators | 2 | 2 (1 / 1) | 1 | 32, 40 |
| PseudoholomorphicCurveAnalysis | 2 | 4 (1 / 3) | 1 | 56, 60 |
| RiemannianManifoldsWithConvexBoundary | 2 | 6 (6 / 0) | 1 | 49, 66 |
| VirtualFundamentalClass | 2 | 8 (8 / 0) | 0 | 16, 27 |
| WeilConjectures | 2 | 1 (1 / 0) | 0 | 19, 20 |
| YangMillsConnectionsAndCaloricGauge | 2 | 5 (4 / 1) | 0 | 37, 48 |
| AdicEtaleGeometry | 1 | 2 (1 / 1) | 1 | 22 |
| AdicSpacesPartII | 1 | 1 (0 / 1) | 1 | 22 |
| AdicSpacesPartIV | 1 | 1 (1 / 0) | 0 | 22 |
| AlgebraicModularFormsAndSerreWeights | 1 | 3 (3 / 0) | 0 | 69 |
| AlgebraicModuliForArithmeticGeometryPartII | 1 | 1 (1 / 0) | 0 | 95 |
| AmenableTracesOnCStarAlgebras | 1 | 7 (7 / 0) | 2 | 36 |
| AnabelianGeometryAndNonabelianChabauty | 1 | 1 (1 / 0) | 0 | 84 |
| ArithmeticGaloisDuality | 1 | 1 (1 / 0) | 1 | 87 |
| AutomorphicSpectralTheory | 1 | 1 (1 / 0) | 1 | 43 |
| CompletedCohomologyPartII | 1 | 4 (4 / 0) | 0 | 77 |
| ComplexHessianEquations | 1 | 6 (6 / 0) | 2 | 38 |
| CongruenceSpectralGap | 1 | 1 (1 / 0) | 0 | 40 |
| CyclotomicClassGroupsAndStickelberger | 1 | 1 (1 / 0) | 0 | 71 |
| DerivedDeRhamCohomology | 1 | 1 (1 / 0) | 0 | 27 |
| DGAInfinity | 1 | 1 (0 / 1) | 1 | 10 |
| DifferentialGeometry | 1 | 1 (0 / 1) | 0 | 52 |
| DimerModelsAndLozengeTilings | 1 | 8 (8 / 0) | 3 | 100 |
| EulerSystemsAndKolyvaginSystems | 1 | 1 (1 / 0) | 0 | 10 |
| FlagVarieties | 1 | 1 (1 / 0) | 0 | 79 |
| FourManifolds | 1 | 2 (1 / 1) | 1 | 64 |
| FukayaTheory | 1 | 1 (1 / 0) | 0 | 56 |
| GaussianIsoperimetryAndClusters | 1 | 5 (5 / 0) | 2 | 55 |
| GL2AutomorphicRepresentationsAndTransfer | 1 | 2 (2 / 0) | 0 | 72 |
| KTheoryFiniteLocalFields | 1 | 1 (1 / 0) | 0 | 10 |
| NoncommutativeIntegration | 1 | 1 (1 / 0) | 0 | 46 |
| PadicDifferentialEquationsAndRigidCohomology | 1 | 1 (1 / 0) | 1 | 22 |
| PerfectoidSpaces | 1 | 1 (0 / 1) | 0 | 81 |
| PrismaticCohomology | 1 | 3 (2 / 1) | 1 | 81 |
| RiemannianGeometry/MinimalSurfaces | 1 | 1 (1 / 0) | 0 | 52 |
| SelmerIwasawaCohomology | 1 | 2 (2 / 0) | 1 | 87 |
| SpectralSequencesAndConvergence | 1 | 3 (3 / 0) | 1 | 6 |
| SpinGeometry | 1 | 1 (0 / 1) | 0 | 64 |
| StableReduction | 1 | 2 (0 / 2) | 1 | 24 |
| SymplecticGeometry/CotangentLagrangian | 1 | 1 (0 / 1) | 1 | 92 |
| TaubesGromov | 1 | 1 (1 / 0) | 0 | 60 |
| VariationalMethods | 1 | 1 (1 / 0) | 0 | 34 |

Distinct definitions served: 88. Items: see per-roadmap sections.

## Key ordering facts across items

- SchemeAndStackFoundations §4.14 (Hilbert/Quot) is the choke point for the Jacobian cluster
  (defs 19, 24, 30, 71, 80, 84, 85). Required order: JacobianChallenge §C.1 coherence (whose proper
  case needs SSF §4.12 Chow's lemma; only Chow's graph-closure construction is in code) and §C.2
  base change, then SSF §4.14, then §D.3 Hilbert quotients and §D.4 projective Picard
  representability, then §D.5 `Pic⁰` and the Abel maps and §D.8 the Jacobian. `Symᵈ X` (§C.4) needs
  only §C.2, not §4.14; §D.5 needs it.
- SSF Layer 1 is a linear chain: §1.3 (done), then §1.5, §1.6, §1.7/§1.8, §1.9, then §1.19, §1.20,
  §1.21, §1.22, §1.23. §1.5 is partial (`EtaleEquivRel` in code), so §1.6 waits on §1.5's quotient
  sheaf. §1.18 has `StackInGroupoids` in code; its stackification and 2-fibre products, which §1.19
  needs, can proceed in parallel with §1.5.
- LieGroups Layer 7 (compact real form, Cartan involution θ) unblocks Layer 9 beyond `GL n`. Layer 9
  in turn heads the real-reductive chain: ArithmeticLocallySymmetricSpaces ALS.F.1 and ALS.0.1–ALS.0.3,
  then AutomorphicFormsOnReductiveGroups §2.3a and §§2.3–2.4, then RealSemisimpleLieGroups Layers 2–5
  and §5.7, for defs 1, 4, 7, 15, 31, 54, 62, 79. Layer 7 is partial (`serreCompactInvolution`, the
  conjugate-linear Chevalley involution of a Serre presentation) and ready now; RealSemisimpleLieGroups
  Layers 0–1 can start now with the existence of Cartan involutions as a hypothesis.
- EtaleCohomologyFoundations §F.0.1 (étale module sheaves) precedes every étale cohomology item
  (§F.1, §F.2.x, §F.4.x). It is partial (geometric stalks, finite lisse sheaves and the monoidal
  structure with monoidal stalks in code), and its constructible part is ready now.
- RiemannianGeometry R5a (B, S, normal connection) is formally blocked on SmoothBundlesConnections
  B3–B4 per its README, though that dependency looks soft: the normal bundle `ν_f` with its
  projection and the derivative along a map `CovariantDerivative.alongMap` are in code. It heads the
  chain R5a, then R5a.2 (with R5a.1, which is partial and ready now), then R5b (whose operator part,
  `IsCoercive.formOperator`, is in code), then R5c, then MinimalSurfaces MS6, for defs 49, 52, 65,
  66. Varifolds §5.1 and RiemannianManifoldsWithConvexBoundary §3.6 also consume R5a.
- DifferentialGeometry 12.5's outward unit normal (`exists_halfSpaceOutwardUnitNormal`, not in code)
  blocks RiemannianManifoldsWithConvexBoundary §1.2, and with it every later item of that roadmap
  (def 66), and RiemannianGeometry R7.9, which RiemannianManifoldsWithConvexBoundary §§3.1, 4.3
  consume. Its own input 12.4 waits on `integralDensity`, which can start now.
- SchemeAndStackFoundations §§1.19–1.20 (`IsAlgebraicStack`, points of a stack) head all of
  StackPointsAndResidualGerbes (defs 16, 17, 28, 29), none of whose items can start before them;
  they sit at the end of the SSF Layer 1 chain above.
- VirtualFundamentalClass (defs 16, 27) starts at Layer 0 (stack dimension), which needs SSF Layer 1
  through §1.19 (DM stacks) and §1.21 (quotient stacks); its Layer 1 also needs SSF §§1.10, 1.22 and
  §5.5, and its Layer 3 the cotangent-complex chain DerivedModuleAlgebra §0.4, then
  DerivedDeRhamCohomology §5.8. No item can start now.
- AlgebraicModuliForArithmeticGeometry §1.3 `coherentGrassmannian` (needing ModularCurves §0.7 over
  a non-affine base) blocks NashBlowups §0.4 and §§1.2–1.5, hence Layers 2, 6 and 7 (defs 25, 26).
  NashBlowups §§0.1–0.3, 0.6, 0.7 can start now.
- LieGroups Layer 9 (`CartanInvolution`, `IwasawaData` beyond `GL n`) also blocks LieGroupsPartII
  Layers 1–3 and §§7.1, 8.1 (defs 1, 4, 54, 79).
- The modular-curve cluster (defs 69, 71, 77) runs through ModularCurvesPartII, whose items wait on
  ModularCurves Layer 10 (untouched), JacobianChallengePartII Layers 0–1 (on JacobianChallenge
  Layers D–E) and EtaleCohomologyFoundations §§F.1–F.4. Only ModularCurvesPartII §3.8 can start now.
  CompletedCohomologyPartII (def 77) waits on the same ModularCurvesPartII §§14.1–14.4a and on
  ArithmeticLocallySymmetricSpaces §§0.1–0.7.
- ShimuraVarieties §§P.1–P.5 (Hodge structures as representations of the Deligne torus) head both
  Mumford–Tate specifications, ShimuraVarieties §P.3a and ShimuraData Layer 1 (defs 13, 23, 89).
- BallQuotientsAndComplexHyperbolicLattices (defs 15, 31) starts from RealSemisimpleLieGroups §5.7,
  hence from LieGroups Layer 9, and its quotients need ComplexComparisonPartII §C-1.1.
- ModularCharactersAndBlocks §0.2 (block idempotents) and §6.1 (relative traces) can start now; they
  head the chain to blocks, defect groups and heights (defs 2, 3, 9).

## TauCetiRoadmap/SchemeAndStackFoundations
STATUS.md snapshot: a5cae7f 2026-11-16, generated against Tau Ceti aa6e43e (Tau Ceti checked at 91942aa9f, 2026-11-19)

### §1.4 AlgSpace.overEquiv (algebraic spaces over a base)
- Status: PARTIAL: §1.3 is complete in code: the predicates `SchemePresheaf`, `Spaces.RepresentableDiagonal`, `Spaces.EtaleAtlas`, `Spaces.IsAlgebraicSpace` (TauCeti/AlgebraicGeometry/AlgebraicSpace/Basic.lean), `Spaces.isAlgebraicSpace_of_etale_cover` with `EtaleAtlas.of_sigma` (AlgebraicSpace/EtaleCover.lean) and `IsAlgebraicSpace.diagonal_locallyQuasiFinite` with `EtaleAtlas.locallyOfFiniteType_diag` (AlgebraicSpace/Diagonal.lean). §1.4 has `Spaces.AlgSpace`, `toPresheaf`, `ofScheme` (Full/Faithful), `homFromSchemeEquiv`, terminal `Spec ℤ`, initial `∅` (AlgebraicSpace/Category.lean). The presheaf-level input exists: `TauCeti.overYonedaEquivPresheafOver X : Over (yoneda.obj X) ≌ (Over X)ᵒᵖ ⥤ Type` with `overYonedaEquivPresheafOverYonedaIso` (TauCeti/CategoryTheory/Comma/Presheaf/OverYoneda.lean). Missing: `IsAlgebraicSpaceOver S` and `AlgSpace.overEquiv` (algebraic spaces over `h_S` ≃ fppf sheaves on `Over S` satisfying `IsAlgebraicSpaceOver S`). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43599 (AlgebraicSpace/Over.lean: `IsAlgebraicSpaceOver S` and the equivalence `AlgSpace.overEquiv S`, completing the §1.4 declarations).
- Ready now: yes (needs only §1.3, which is done; the presheaf equivalence is in code)
- Serves defs: 16, 20, 28
- Evidence: README l.2899 "### 1.4 The category of algebraic spaces" (l.2905 `IsAlgebraicSpaceOver S`); STATUS Layer 1 remaining "... algebraic spaces over a base (1.4), 1.5 onward"; grep `overEquiv|IsAlgebraicSpaceOver` in AlgebraicSpace/ empty.

### §1.2 fppf descent of quasi-finite morphisms and of algebraic spaces
- Status: NOT-STARTED
- Ready now: no. `quasiFiniteDescent` (Stacks 02W8) needs effective fpqc descent of quasi-affine morphisms (Stacks 0247; Mathlib has only `Scheme.IsQuasiAffine`, Tau Ceti has effective descent of affine morphisms in Descent/AffineMorphism.lean) and gluing over stable quasi-compact opens; Mathlib's Zariski's Main Theorem supplies quasi-finite separated implies quasi-affine. `spaceFppfDescent` (Stacks 04SK) and 0ADV need §1.17 `artinBootstrap` (not started). The README's *Needs* line lists only §1.3.
- Serves defs: 20 ("fppf descent for alg spaces")
- Evidence: README l.2819 "### 1.2 Fppf descent of quasi-finite morphisms and of algebraic spaces" (Needs §1.3; Mathlib `Presheaf.IsSheaf`, `MorphismProperty.presheaf`, `LocallyQuasiFinite`); no matching declarations in Tau Ceti.

### §1.5 étale equivalence relations and the quotient sheaf
- Status: PARTIAL: `TauCeti.AlgebraicGeometry.Spaces.EtaleEquivRel s t` (Mathlib's internal `IsEquivalenceRelation t s` with `s`, `t` étale) with `refl`, `symm`, `trans` and their laws, `swap`, `hom_ext`, `etale_refl`, `etale_trans`, `id`, `of_isKernelPair` (TauCeti/AlgebraicGeometry/AlgebraicSpace/EtaleEquivRel.lean), on `TauCeti.CategoryTheory.isEquivalenceRelation_iff` (jointly monic plus an equivalence relation on `T`-points, the README's `IsEquivRel`), `IsKernelPair.isEquivalenceRelation` and `IsEquivalenceRelation.id` (TauCeti/CategoryTheory/EquivalenceRelation.lean). Missing: `EtaleEquivRel.restrict`, `EtaleEquivRel.ofAtlas`, and all of the quotient sheaf: `quotientSheaf s t`, `quotientSheaf.π`, `.desc`, `.kernelPair`, `.represented_of`, `.restrict`. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43597 (AlgebraicSpace/QuotientSheaf.lean: `quotientPresheaf`, `quotientSheaf s t` with `quotientSheaf.π`, `.desc`, `.isColimit` and `.kernelPair`; not `.represented_of`, `.restrict`, `EtaleEquivRel.restrict`, `EtaleEquivRel.ofAtlas`).
- Ready now: yes (needs §1.3 only)
- Serves defs: 16, 20, 28 (as the start of the §1.6–§1.9 chain)
- Evidence: README l.2917 "### 1.5 Étale equivalence relations and the quotient sheaf"; grep `quotientSheaf` in AlgebraicSpace/ empty (the hits in Curves/NodalGluing/ and AlgebraicGeometry/Quotient/EquivalenceRelation.lean are unrelated).

### §1.6–§1.9 presentations, points |X|, fibre products and étale-local properties, separation and properness
- Status: NOT-STARTED (no `etaleQuotientTheorem`, `spacePresentation`, `points`, `isAlgebraicSpace_pullback`, `EtaleLocal`, `IsSeparatedSpace`, `IsProperSpace`)
- Ready now: no: §1.6 needs §1.5's `quotientSheaf` (§1.5 is partial: `EtaleEquivRel` is in code, the quotient sheaf is not); §1.7 and §1.8 need §1.6; §1.9 needs §1.7 and §1.8
- Serves defs: 16, 20, 28 (§1.7 `points F` for 28; §1.9 `IsProperSpace` for 16/20)
- Evidence: README l.2955 "### 1.6 Quotients by étale equivalence relations and presentations" (Needs §1.3, §1.5; `etaleQuotientTheorem` is about "the quotient sheaf `U/R`"), l.2969 "### 1.7 Points of an algebraic space" (Needs §1.3, §1.6), l.2996 "### 1.8 Fibre products and étale-local properties of morphisms" (Needs §1.3, §1.6), l.3064 "### 1.9 Separation and properness" (Needs §1.3, §1.7, §1.8); every named declaration greps empty.

### §1.10 smallEtale, the small étale site of an algebraic space
- Status: NOT-STARTED (grep `smallEtale` in TauCeti/AlgebraicGeometry/AlgebraicSpace/ empty)
- Ready now: no: needs §1.4 (partial), §1.8, §1.9 (not started)
- Serves defs: 27 (VirtualFundamentalClass §1.1 ringed sites of DM stacks and §3.3 cotangent complexes of algebraic spaces)
- Evidence: README l.3085 "### 1.10 The small étale site of an algebraic space" (`smallEtale F`, `structureSheaf F`; *Needs* §1.4, §1.8, §1.9); VirtualFundamentalClass README §1.1 *Needs* "SchemeAndStackFoundations §§1.10, 1.22", §3.3 *Needs* "SchemeAndStackFoundations §1.10".

### §1.14 groupoids in algebraic spaces, stabilizer, stabilizerAt
- Status: NOT-STARTED (TauCeti/AlgebraicGeometry/Inertia/Basic.lean is decomposition/inertia groups of a point under a group acting on a scheme, unrelated)
- Ready now: no: needs §1.5, §1.8, §1.13 (group spaces, which needs §1.4, §1.8)
- Serves defs: 28, 29
- Evidence: README l.3247 "### 1.14 Groupoids in algebraic spaces and stabilizers", l.3267 "`stabilizerAt` for a field-valued point"; grep `stabilizerAt` returns nothing.

### §1.18 StackInGroupoids, stackification, 2-fibre products
- Status: PARTIAL: `TauCeti.AlgebraicGeometry.StackInGroupoids` (a `SchPseudofunctor` with groupoid fibres that is a stack for `Scheme.fppfTopology`), `StackInGroupoids.Hom` (strong transformations), `Hom.IsFiberwiseEquiv` with identities, composition and two-out-of-three (TauCeti/AlgebraicGeometry/Stack/StackInGroupoids.lean). Missing: `StackInGroupoids.ofSheaf`, `yonedaEquiv`, `isFiberedInGroupoids`, `limit`, the site-level `Stack.stackification` with `toStackification`, `isStack_stackification`, `stackificationUniversal`, and `Stack.twoFibreProduct`/`twoFiberProduct`. §1.1's `Descent.qcohPseudofunctor` (an fpqc prestack: Descent/QuasicoherentSheaf/Prestack.lean) and fpqc uniqueness of descended morphisms are prerequisites, not §1.18. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/38597 (`StackInGroupoids.ofSheaf`, the stack in setoids of an fppf sheaf, on `Pseudofunctor.ofPresheaf` with `isStack_ofPresheaf_iff`, CategoryTheory/Sites/Descent/Discrete.lean).
- Ready now: yes: the missing definitions use only Mathlib `Pseudofunctor`, `IsStack`, `DescentData`, `sheafHom`, `CategoricalPullback`, `StrongTrans` and the existing carrier; README lists §1.1, which is PARTIAL (effective descent of objects missing)
- Serves defs: 20, 24, 27, 28, 29
- Evidence: README l.3538 "### 1.18 Stacks in groupoids, stackification and 2-fibre products", Needs l.3580 "§1.1; Mathlib `Pseudofunctor`, `IsStack`, `IsPrestack`, ..."; grep `twoFiberProduct|twoFibreProduct|stackification|yonedaEquiv` in AlgebraicGeometry/Stack/ empty.

### §1.19 IsRepresentableBySpaces, IsAlgebraicStack, IsDeligneMumford
- Status: NOT-STARTED
- Ready now: no: needs §1.4 (partial), §1.9, §1.18 (partial: 2-fibre products missing)
- Serves defs: 16, 17, 24, 27, 28, 29
- Evidence: README l.3612 "### 1.19 Representable morphisms, algebraic stacks and Deligne–Mumford stacks" (Needs §1.4, §1.9, §1.18); grep `AlgebraicStack|DeligneMumford` empty.

### §1.20 inertia, automorphismGroup, Stacks.points, IsProperStack
- Status: NOT-STARTED
- Ready now: no: needs §1.7, §1.8, §1.9, §1.14, §1.18, §1.19
- Serves defs: 16, 24, 28, 29
- Evidence: README l.3638 "### 1.20 Inertia, the setoid criterion, properties of morphisms and presentations" (`automorphismGroup x` l.3641, `Stacks.points` l.3652, `IsProperStack` l.3679); grep `automorphismGroup` hits only unrelated algebra/topology files; `IsProperStack`, `Stacks.points` empty.

### §1.21 quotient stacks, BG, root stacks
- Status: NOT-STARTED
- Ready now: no: needs §1.13, §1.14, §1.15, §1.19, §1.20
- Serves defs: 16, 17, 27, 29 (16 and 27 through VirtualFundamentalClass §0.3 and Layer 4)
- Evidence: README l.3744 "### 1.21 Quotient stacks, line bundles with a section, root stacks", Needs l.3770; grep `QuotientStack|classifyingStack` empty.

### §1.22 Stacks.QCoh, QCoh.pushforward
- Status: NOT-STARTED
- Ready now: no: needs §1.1 (partial), §1.11, §1.18 (partial), §1.21
- Serves defs: 17, 27, 29
- Evidence: README l.3797 "### 1.22 Quasi-coherent modules on stacks" (Needs §1.1, §1.11, §1.18, §1.21; Mathlib `CoGrothendieck`); grep `Stacks.QCoh` empty.

### §1.23 moduli functors, coarse moduli, Keel–Mori, IsTame
- Status: NOT-STARTED (the existing `IsTame` hits are tame ramification, unrelated)
- Ready now: no: needs §1.17, §1.19, §1.20, §1.22
- Serves defs: 16, 17, 24
- Evidence: README l.3829 "### 1.23 Moduli functors, fine and coarse moduli spaces, Keel–Mori, tame stacks", Needs l.3866; grep `CoarseModuli|KeelMori` empty.

### §2.6 quasi-coherent cohomology (cited for 20)
- Status: PARTIAL: higher direct images of quasi-coherent modules along qcqs morphisms are quasi-coherent (`Scheme.Hom.isQuasicoherent_higherDirectImage`), with sections over a basic open of an affine base `Hⁿ(f⁻¹ D(g), M)` (`Scheme.Hom.higherDirectImageBasicOpenSectionsAddEquiv`) and the localization property (`isLocalizedModule_higherDirectImagePresheaf_map_basicOpen`) (Cohomology/HigherDirectImage/Quasicoherent.lean, Presheaf.lean, Scalars.lean); flat base change over an affine base for qcqs `X` (`TauCeti.AlgebraicGeometry.bijective_cohomologyBaseChange`, Cohomology/FlatBaseChange.lean); uniform vanishing (QuasiSeparated.lean); `H^q(ℙⁿ_A, O(d))` in every degree, the top degree as the dual of `Sym^j` (`Module.Basis.nonempty_linearEquiv_cohomology_top_twistingSheaf_dual`, Cohomology/ProjectiveSpace/TopDual.lean). Missing: commutation of `R^p f_*` with filtered colimits and with flat base change over a non-affine base, `ample_serre_vanishing`, `proper_fibreDimension_vanishing`, the vanishing-implies-affine direction of `serre_affineness_criterion` (`QCoh.isAffine_of_H1_vanishing`). Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/38440 (the vanishing-implies-affine direction of `serre_affineness_criterion`, `Scheme.isAffine_of_subsingleton_cohomology_one`, Cohomology/AffinenessCriterion.lean) and https://github.com/TauCetiProject/TauCeti/pull/40274 (cohomology of quasi-coherent modules on qcqs opens commutes with filtered colimits, `isColimitMapCoconeCohomologyFunctor`, Cohomology/FilteredColimit.lean).
- Ready now: yes (needs §0.3, §0.4, both begun, plus existing Tau Ceti cohomology; `ample_serre_vanishing` also needs StableReduction Layer 2 relative ampleness)
- Serves defs: 20, 21 (via §2.7, §2.10)
- Evidence: README l.4357 "### 2.6 Quasi-coherent cohomology", Needs "§0.3, §0.4; Tau Ceti `Scheme.Modules.Cohomology`, ...; StableReduction Layer 2; JacobianChallenge Layer C"; grep `ample_serre_vanishing|isAffine_of_H1` empty.

### §2.7 cohomology with supports and local cohomology
- Status: PARTIAL: the topological-space case for abelian and module sheaves: cohomology with closed supports `CategoryTheory.Sheaf.supportedH` with the support long exact sequence and excision (TauCeti/Topology/Sheaves/SupportedCohomology.lean, SupportedCohomology/), the local cohomology sheaves `supportedHSheaf` with their long exact sequence and the edge comparison (Topology/Sheaves/LocalCohomology/); `localCohomology_degreeZero` as `localCohomology.degreeZeroToModule_injective` and `range_degreeZeroToModule` (Algebra/Homology/LocalCohomology/DegreeZero.lean). Missing: the scheme versions `sectionsWithSupport`, `cohomologyWithSupport` with their `O(X)`-module structure, `rHZ_adjunction`, `localToGlobal`, `localCohomology_colimit_ext_comparison`, `localCohomology_module_comparison`, `localCohomology_flat_baseChange`, `depth_localCohomology_vanishing`.
- Ready now: no for the scheme-level part: needs §2.1 and §2.6 (partial). The ring-level `localCohomology_flat_baseChange` and `depth_localCohomology_vanishing` use only Mathlib's `localCohomology` and depth and could start now
- Serves defs: 21
- Evidence: README l.4433 "### 2.7 Cohomology with supports and local cohomology" (Needs §0.17, §2.1, §2.6; *Lean:* "nothing of this subsection"); grep `sectionsWithSupport|cohomologyWithSupport` empty.

### §2.10 comparisons between the fppf, étale, Nisnevich and Zariski topologies
- Status: PARTIAL: the étale-to-Nisnevich morphism of topoi `etaleToNisnevich X` through its functors: `AlgebraicGeometry.Scheme.etaleToNisnevichPushforward` (direct image, fully faithful), `etaleToNisnevichPullback` (étale sheafification, exact when sheafification preserves finite limits), `etaleToNisnevichAdjunction` (TauCeti/AlgebraicGeometry/Sites/Nisnevich/EtaleComparison.lean). Missing: `epsilonFppfEtale`, `aX`, `nisnevichToZariski`, `comparison_comp`, `comparison_baseChange`, `aX_inverseImage_obj`, `quasiCoherent_topology_comparison`, `etale_pullback_fppf_comparison`, `smoothGroup_fppf_etale_comparison`, and the pro-étale part (`Scheme.toProEt`, `proetalePushforward`, `proetaleComparison`).
- Ready now: no for the cohomology comparisons: they need §2.1, §2.6, §2.9, §2.12 (all partial). The remaining morphisms of topoi `epsilonFppfEtale`, `aX`, `nisnevichToZariski` can be defined from the Mathlib topologies and the existing Nisnevich site, as `etaleToNisnevich` is
- Serves defs: 21 (20 also cites it)
- Evidence: README l.4643 "### 2.10 Comparison morphisms between the topologies of a scheme", Needs "§2.1, §2.6, §2.9, §2.12"; grep `epsilonFppfEtale|nisnevichToZariski|quasiCoherent_topology_comparison|toProEt` empty.

### §2.20 relative dualising complexes, Serre duality (cited for 19, 20)
- Status: NOT-STARTED
- Ready now: no: needs §0.18, §2.18, §2.19, §2.21
- Serves defs: 19 (`relativeDualizingModule_smooth`, `ω ≅ ⋀^d Ω`, gives the canonical sheaf of a smooth surface), 20
- Evidence: README l.5380 "### 2.20 Relative dualising complexes and modules, Serre duality, curve comparison"; grep `relativeDualizingModule|RelativeDualizingComplex|cm_serre_duality` empty.

### §4.1 thickenings and formally smooth/étale morphisms (cited for 20)
- Status: PARTIAL: thickenings (Morphisms/Thickening.lean); `TauCeti.AlgebraicGeometry.FormallySmooth` and `FormallyEtale` for morphisms of schemes (lifting along affine first-order thickenings), stable under isomorphisms, composition and base change, `FormallyEtale.formallySmooth`, `formallyEtale_iff` (Morphisms/FormallySmooth.lean). Missing: `IsThickening.factor_firstOrder`, `formallySmooth_specMap_iff`, `FormallySmooth.iff_affineLocally`, `FormallyEtale.of_isOpenImmersion`, `FormallySmooth.of_smooth`, `smooth_iff_formallySmooth`, `etale_iff_formallyEtale`, `smooth_lifting_torsor`. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43601 (`formallySmooth_specMap_iff`, its étale analogue, `FormallyEtale.of_isOpenImmersion` and `IsFirstOrderThickening.exists_iso_quotient`, Morphisms/FormallySmooth.lean).
- Ready now: yes for the API and the smooth/étale comparisons; `smooth_lifting_torsor` needs §2.3 (partial)
- Serves defs: 20
- Evidence: README l.6278 "### 4.1 Thickenings, formally smooth and étale morphisms, the lifting criterion, torsors of lifts", Needs "§2.3; Tau Ceti `.../Morphisms/Thickening.lean`"; STATUS Layer 4 remaining "lifting criterion (4.1)".

### §4.14 Hilbert/Quot/Hom/Isom schemes
- Status: NOT-STARTED for Hilbert/Quot/Hom/Isom (no `hilbert_quot_schemes`, Quot or Hilb functor anywhere in Tau Ceti)
- Ready now: no: needs §2.6 (partial), §4.12 (partial: the graph-closure construction of Chow's lemma, `TauCeti.AlgebraicGeometry.graphClosure` with `isModification_graphClosureFst` and `isImmersion_graphClosureSnd`, Morphisms/Modification/GraphClosure.lean; no `generic_flatness`, `chow_lemma`), StableReduction Layer 2 (partial: "coherent cohomology and base change ... ampleness criterion and openness" remaining), JacobianChallenge §§C.1–C.2 (partial: "coherence of R^q f_* for proper f, flat base change over a non-affine base, semicontinuity, cohomology and base change" remaining). JacobianChallenge §§D.3–D.4 consume §4.14; §C.4's `Symᵈ` does not
- Serves defs: 24, 30 (and, through JacobianChallenge §§D.3–D.4, 19, 71, 80, 84, 85)
- Evidence: README l.7025 "### 4.14 Hilbert and Quot schemes", Needs l.7042 "§2.6, §4.12; StableReduction Layer 2; JacobianChallenge Layer C". STATUS's Layer 4 "remaining" list (lifting criterion 4.1, deformation functors 4.3, formal functions and algebraization 4.9–4.10, strict transforms 4.11, Bertini 4.13) only names sections that have started; §4.14 is untouched, not done.

### §4.14 (Grassmannian clause) relative Grassmannian Gr(E, d), Plücker embedding
- Status: PARTIAL: the affine case is done. `Module.Grassmannian.scheme R M k` over `Spec R` for any module `M`, with charts and gluing (Grassmannian/Basic.lean), functor of points on affine tests (`schemeHomEquiv`, Points.lean), separated and proper for finite `M` (`isProper_toSpec`, Proper.lean), base change along `Spec R' → Spec R` (`Module.Grassmannian.isPullback_baseChangeHom`, BaseChange.lean), plus ideal/rank/isotropic loci and the universal quotient. Missing: gluing over a non-affine base `S`, representability on all `S`-schemes, the Plücker closed immersion with `det Q` very ample. No `Plucker` in AlgebraicGeometry; there is only linear-algebra `LinearAlgebra/Projectivization/Plucker.lean`. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43522 (`Module.Grassmannian.schemeIsoOfLinearEquiv`, the isomorphism `G(k, M) ≅ G(k, M')` induced by a linear equivalence, a step toward gluing over a non-affine base; Grassmannian/Congr.lean).
- Ready now: yes. This clause does not need §4.12; it is the same object that ModularCurves §0.7 owns (see below), so implement it once there
- Serves defs: 25, 26 (through AlgebraicModuliForArithmeticGeometry §1.3, whose coherent Grassmannian is built from this locally free one)
- Evidence: README l.7035 "The construction embeds Quot into a relative Grassmannian, which is stated here: for `S` Noetherian, `E` locally free of rank `r`..."; ModularCurves §0.7 claims ownership of the same object.

### §4.15 StableCurves.Mbar g n
- Status: NOT-STARTED (grep `Mbar|StableCurves|isom_stable_curves` empty)
- Ready now: no: the definition needs §1.18 `StackInGroupoids` (in code) and StableReduction Layer 3 stable families (partial: "semistable and stable families with their criteria" remaining). Algebraicity needs §1.20, §4.6, §4.14 and StableReduction Layers 2–3, 8–9
- Serves defs: 24
- Evidence: README l.7054 "### 4.15 The moduli stack of stable pointed curves" (l.7056 "Define `StableCurves.Mbar g n : StackInGroupoids` (§1.18)").

### §4.11 modifications and strict transforms (weak link for 25)
- Status: PARTIAL: `TauCeti.AlgebraicGeometry.IsModification` with `.birational`, `.comp`, `.isIso_of_isFinite` (Morphisms/Modification/*); the centre: `Scheme.Hom.isoLocus`, `Scheme.Hom.centre` (Morphisms/IsoLocus.lean) with `IsModification.dense_isoLocus`, `IsModification.isNowhereDense_centre` (Modification/Centre.lean); the strict transform under a blow-up as a scheme-theoretic closure (Blowup/StrictTransform.lean, Blowup/Pullback.lean). Missing: `IsModification.functionField_equiv`, `.isAlteration`, and the general witness-based `strictTransform*` API (`strictTransform_eq_closure`, `strictTransformModule`, `strictTransform_supportComparison`). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43528 (`IsModification.functionField_equiv` via `Scheme.Hom.isIso_functionFieldMap_iff_isIso_stalkMap`; modifications are dominant and surjective; Modification/FunctionField.lean).
- Ready now: yes (Needs §0.9 and StableReduction Layer 4 blow-ups, which exist)
- Serves defs: 25
- Evidence: README l.6824 "### 4.11 Modifications and strict transforms"; STATUS Layer 4 remaining "strict transforms (4.11)"; grep `functionField_equiv|isAlteration|strictTransformModule` empty.

### §0.20 Japanese/Nagata rings, finiteness of normalization
- Status: PARTIAL: `TauCeti.Ring.IsN1`, `IsJapanese`, `IsUniversallyJapanese`, `IsNagata` and their API (RingTheory/Japanese.lean, Nagata.lean, UniversallyJapanese.lean), `IsJapanese.polynomial`, `IsJapanese.of_quasiFinite` (the README's *IsJapanese.of_quasiFinite_extension*, RingTheory/Japanese/QuasiFinite.lean), `IsUniversallyJapanese.isNagata_of_finiteType`, the README's *IsNagata.integralClosure_finite* as `TauCeti.Ring.IsNagata.finite_integralClosure` (Stacks 03GH, RingTheory/Nagata.lean), and `isFinite_fromNormalization_of_isJapanese` (AlgebraicGeometry/Normalization/Finite.lean). Missing: Nagata's theorem, i.e. `IsNagata.polynomial`, `IsNagata.of_finiteType`, `isNagata_iff_isUniversallyJapanese`; the complete-local cases `IsJapanese.of_complete_local`, `IsNagata.of_complete_local`; `IsNagata.not_nonJapaneseDVR`; `IsQuasiExcellentRing.isNagata`.
- Ready now: no: the complete-local cases (Stacks 032W) are proved from the Cohen structure theorem (Stacks 032A, 032D), and Nagata's theorem ("Nagata implies universally Japanese", 0334, with `IsNagata.polynomial` and `IsNagata.of_finiteType`) rests on 032W; the Cohen structure theorem is in neither Tau Ceti nor Mathlib (grep `Cohen` finds nothing; it is a target of DeformationAndDerivedPatchingAlgebra §1.10). `IsNagata.not_nonJapaneseDVR` needs §0.22's non-Japanese discrete valuation ring and `IsQuasiExcellentRing.isNagata` needs excellence, neither in code. The README's *Needs* line lists only the existing Japanese/Nagata files
- Serves defs: 26
- Evidence: README l.1930 "### 0.20 Japanese and Nagata rings"; STATUS Layer 0 remaining "0.20-0.21", which understates §0.20: grep shows none of the missing names. 26's finiteness does not wait on this item: finite-type algebras over a field are Japanese and Nagata (`IsUniversallyJapanese.of_field`, `.isJapanese`, `.isNagata_of_finiteType`), and `isFinite_fromNormalization_of_isJapanese` turns that into finiteness of normalization for integral schemes of finite type over `k`.

### §3.3 degrees of vector bundles
- Status: PARTIAL: `FiniteLocallyFreeSheaf.FixedRank.vectorBundleDegree` (VectorBundle/Degree.lean) with additivity in short exact sequences under finiteness hypotheses on cohomology (`vectorBundleDegree_add_of_shortExact`, `_of_isCurveOver`), direct sums (`vectorBundleDegree_biprod`), `_elementaryModification`, `_baseChange`, pullback along finite flat maps (`vectorBundleDegree_pullback_of_finrank_eq`, `vectorBundleDegree_pullback_eq_finrank_functionField_mul`), twisting by a line bundle and by an effective Cartier divisor (`vectorBundleDegree_twist`, `vectorBundleDegree_twist_of_isEffective`), and tensoring a finitely supported modification with a vector bundle (`vectorBundleDegree_tensor_eq_add_mul_eulerCharBelow_of_shortExact`). Rank-one Riemann–Roch `InvertibleSheaf.eulerCharBelow_eq_relativeDegree_add_one_sub_genus` (WeilDivisor/Scheme/RiemannRoch/Basic.lean) and `LineBundleClass.intersectionNumber` (IntersectionNumber/Basic.lean). Missing: `_tensor` for a general vector bundle `V`, `_dual`, `_det`, the discharge of the finiteness hypotheses on proper `X` of dimension `≤ 1`, `vectorBundle_riemann_roch`, `curve_serre_duality`. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43642 (VectorBundle/Affine/ExteriorPowerDual.lean: exterior powers of duals of finite projective modules, toward `det (E^∨) ≅ (det E)^∨` for the `_dual` law).
- Ready now: no for `_tensor`, `_det`, `_dual`. `_tensor` (Stacks 0AYX) needs a full-rank injection `𝒪_X(-D)^r ⟶ E` with finite cokernel on a proper curve (not in code: `rationalTrivializationHom` is rank one) and open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/38691 (degrees of tensored modifications with finitely supported cokernel). `_det` also needs determinant compatibility with subsheaves (its local length input is in code: `Matrix.length_quotient_range_mulVecLin_eq_ord_det` over 1-dimensional Noetherian domains, RingTheory/Length/Determinant.lean); `_dual` needs `det(E^∨) ≅ (det E)^∨` (not in code), which can start now. Discharging the hypotheses needs §2.6, and Riemann–Roch and duality need §2.6 and §2.20
- Serves defs: 24 (curve class β)
- Evidence: README l.5863 "### 3.3 Degrees of vector bundles, Riemann–Roch and Serre duality on curves"; STATUS Layer 3 remaining "degree laws for tensor, dual and determinant, Riemann-Roch on curves (3.3)".

### §3.7 Picard stacks, universal sections, Abel maps
- Status: NOT-STARTED (`picardStack`, `sectionStack`, `picard_norm_sequence` absent). Functor-level Abel maps exist in TauCeti/AlgebraicGeometry/PicardFunctor/Abel/*, but they belong to JacobianChallenge Layers D/F, not to §3.7's stack-level maps.
- Ready now: no: needs §1.18 (partial), §1.19, §3.4, §3.5, §3.6 and JacobianChallenge Layers C–D
- Serves defs: 30
- Evidence: README l.6146 "### 3.7 Picard stacks, universal sections, Abel maps and the norm sequence", Needs l.6183 "§1.18, §1.19, §3.4, §3.5, §3.6; JacobianChallenge Layers C–D".

### §5.2 proper pushforward beyond closed immersions
- Status: PARTIAL: cycle-level pushforward over a field, `Chow.cyclesMap` (functorial, degree-compatible), in Chow/Pushforward.lean; Chow-group pushforward along closed immersions (Chow/ClosedImmersion.lean); restriction of cycles to an open subscheme `Chow.cyclesRestrict` (the flat pullback along an open immersion) and the cycle-level localization sequence `Chow.range_cyclesPushforward_eq_ker_cyclesRestrict` (Chow/OpenRestriction.lean). Missing: descent of proper pushforward to `ChowGroup`, general `flatPullback`, `flatPullback_properPushforward`, `localization_exact` on Chow groups. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/41379 (the localization sequence on Chow groups, `Chow.ChowGroup.exact_pushforward_restrict`, `restrict_surjective`, Chow/Localization.lean) and https://github.com/TauCetiProject/TauCeti/pull/43531 (flat pullback of cycles along morphisms of pure relative dimension, Chow/FlatPullback.lean).
- Ready now: yes (needs §5.1, which is present; injectivity of homotopy invariance needs §5.4)
- Serves defs: 16, 27
- Evidence: README l.8057 "### 5.2 Proper pushforward, flat pullback and the localisation sequence"; STATUS Layer 5 remaining "proper pushforward on Chow groups, flat pullback and Chow localization (5.2)".

### §5.4 projective bundles and Chern classes
- Status: NOT-STARTED (grep `chernClass|ChernClass|firstChernClass` empty in AlgebraicGeometry)
- Ready now: no: needs §0.3 (begun), §5.2 (partial), §5.3 (not started; needs §3.3, §5.1, §5.2)
- Serves defs: 27
- Evidence: README l.8122 "### 5.4 Projective bundles and Chern classes", Needs l.8142 "§0.3, §5.2, §5.3; AlgebraicVectorBundles".

### §5.5 normalCone, deformationToNormalCone, refined Gysin
- Status: NOT-STARTED. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/38421 (NormalCone/Basic.lean: the conormal sheaf and the graded normal-cone algebra of a closed immersion).
- Ready now: no: needs §0.2, §0.3, §5.2, §5.3, §5.4 and StableReduction Layer 4. `normalCone` and `conormal` as definitions need only §0.2 (relative Spec) and Mathlib `reesAlgebra`, so they could start now
- Serves defs: 27
- Evidence: README l.8166 "### 5.5 Normal cones, deformation to the normal cone and refined Gysin maps"; grep `normalCone|deformationToNormalCone|refinedGysin` empty.

### §5.9–§5.10 surface pairing Chow.intersectionNumber, numerical equivalence, Num
- Status: PARTIAL: the definitions are in code: `Chow.intersectionNumber k S L M` (`χ(𝒪) − χ(L⁻¹) − χ(M⁻¹) + χ(L⁻¹ ⊗ M⁻¹)`, symmetric, invariant under isomorphism), its descent `Chow.classIntersectionNumber` to `LineBundleClass S`, `Chow.NumericallyEquivalent` and the quotient type `Chow.Num` with the descended pairing (AlgebraicGeometry/Chow/SurfaceIntersection.lean). Missing: bilinearity of the pairing and the group structure on `Num` (from the numerical polynomial, Stacks 0BEM), the comparison with intersection of curves, adjunction, Riemann–Roch on surfaces, Noether's formula, Hodge index.
- Ready now: no. Bilinearity (and with it the group structure on `Num`) is the numerical-polynomial lemma (Stacks 0BEM), which needs §2.6 finiteness of coherent cohomology on proper (at least projective) schemes (open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/41909, https://github.com/TauCetiProject/TauCeti/pull/43063, https://github.com/TauCetiProject/TauCeti/pull/43068 for the projective case) and `proper_fibreDimension_vanishing` (Stacks 02UZ), neither in code. The theorems (Hodge index, Riemann–Roch on surfaces) need §2.20, §3.3, §5.3, §5.6.
- Serves defs: 19
- Evidence: README l.8519 "### 5.9 Surfaces: the relative intersection pairing ...", l.8625 "### 5.10 ...", l.8639 "**Numerical equivalence.** *Chow.NumericallyEquivalent* / *Num*".

### §5.10 "Numerical Néron–Severi finiteness" `Num.free_finiteRank`
- Status: NOT-STARTED
- Ready now: no: needs the group structure on `Num` (above) and the Néron–Severi theorem
- Serves defs: 78 (paper only, not the definition)
- Evidence: README l.8649 "**Numerical Néron–Severi finiteness.** *Num.free_finiteRank*". It is stated only for smooth projective surfaces over algebraically closed fields.

### §2.2 Leray and Čech spectral sequences (cited for 20)
- Status: PARTIAL: the Leray edge map and acyclicity: `Sheaf.H.lerayEdge_sheafAdjunctionContinuous_bijective` (CategoryTheory/Sites/SheafCohomology/Leray/Edge.lean); Čech computation of quasi-coherent cohomology `homologyCechComplexIsoCohomology` (AlgebraicGeometry/Cohomology/Cech/Basic.lean). Missing: `leray_spectral_sequence` itself, its relative form, `cech_to_cohomology` (STATUS frontier: "What remains is `H^p(D, R^q f_* F) ⇒ H^{p+q}(C, F)` itself, its relative form, and the Čech-to-cohomology spectral sequence"). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/39141 (Leray's acyclicity theorem for a covering of a site, `homologyCechComplexIsoH`, CategoryTheory/Sites/SheafCohomology/Cech/Leray.lean, an input to `cech_to_cohomology`; neither spectral sequence).
- Ready now: yes (needs §2.1, not in STATUS's Layer 2 remaining list, and Mathlib `SpectralObject`, `HasSpectralSequence`, `Arrow.cechNerve`)
- Serves defs: 20
- Evidence: README l.4184 "### 2.2 Leray and Čech spectral sequences" (*Needs:* §2.1; Mathlib `SpectralObject`, `HasSpectralSequence`, `Arrow.cechNerve`).

### §2.3 Torsors and NonabelianH1 (cited for 20)
- Status: PARTIAL: `Torsor`, `NonabelianH1` (CategoryTheory/Sites/NonabelianCohomology/Torsor.lean), `NonabelianH1.map` (Map.lean), `connecting` (Connecting.lean), the exact sequence `map_eq_one_iff_mem_range_connecting`, `map_eq_one_iff_mem_range_map` (ExactSequence.lean), `equivSheafH` with `equivSheafH_connecting`, `equivSheafH_map` (SheafH.lean). Missing: `pullback` of torsor classes along a morphism of sites (STATUS: "most of §2.3, though pullback of torsor classes along morphisms of sites is missing"). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/42463 (pullback of torsors and torsor classes along a morphism of sites, CategoryTheory/Sites/NonabelianCohomology/Pullback.lean).
- Ready now: yes (needs only Tau Ceti's torsor file and Mathlib `Sheaf.H`)
- Serves defs: 20
- Evidence: README l.4206 "### 2.3 Torsors and the first cohomology: the carrier of torsor classes".

### §2.4 abelian-extension boundaries `abelianBoundary` (cited for 20)
- Status: NOT-STARTED (grep `abelianBoundary` empty); its inputs `NonabelianH1.equivSheafH` and `equivSheafH_symm_δ` are in code (CategoryTheory/Sites/NonabelianCohomology/SheafH.lean). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43698 (`NonabelianH1.abelianBoundary`, CategoryTheory/Sites/NonabelianCohomology/AbelianBoundary.lean).
- Ready now: yes (needs §2.3, whose `equivSheafH` is in code, and Mathlib `Sheaf.H.δ`, `HasExt`)
- Serves defs: 20
- Evidence: README l.4247 "### 2.4 Abelian-extension boundaries" (*Needs:* §2.3; Mathlib `Sheaf.H`, `HasExt`, `ShortComplex.ShortExact`).

### §2.11 Hilbert 90 for schemes, Kummer and Artin–Schreier sequences, finite pushforward (cited for 20)
- Status: NOT-STARTED: no scheme-level `hilbert90` (only Galois `TauCeti.hilbert90`, FieldTheory/GaloisCohomology/Hilbert90.lean), `fppf_kummer_sequence`, `artinSchreier_sequence` or `finite_pushforward_exact`. Inputs in code: `LineBundleClass`, Kummer covers (AlgebraicGeometry/FiniteEtale/Kummer.lean), `Algebra/CharP/ArtinSchreier.lean`.
- Ready now: no: needs §2.9 (partial, in STATUS's Layer 2 remaining list) and §2.10 (partial; no `epsilonFppfEtale`)
- Serves defs: 20
- Evidence: README l.4707 "### 2.11 Hilbert 90, the Kummer and Artin–Schreier sequences, finite pushforward" (*Needs:* §2.1, §2.9, §2.10; Tau Ceti `LineBundleClass`).

### §2.15 étale cohomology: Gabber, fields, limits, Hochschild–Serre (cited for 20)
- Status: NOT-STARTED (grep `gabber_affine_proper_base_change|etale_galois_comparison|etale_cohomology_limits|hochschildSerre_galois_covering` empty).
- Ready now: no: needs §0.9 (partial), §0.14 (partial), §2.2 (partial), §2.11 (not started), ProfiniteCohomology Layers 9–10
- Serves defs: 20
- Evidence: README l.4913 "### 2.15 Étale cohomology: Gabber, fields, limits, Hochschild–Serre" (*Needs* l.4929: §0.9, §0.14, §2.1, §2.2, §2.11).

### §2.22 sheaves of algebras, Azumaya algebras, Brauer group of a scheme (cited for 20)
- Status: NOT-STARTED: no `SheafAlgebra`, `Azumaya`, `IsAzumaya.exists_etale_matrix_splitting` or `isAzumaya_iff_positive_fibres_mulLeftRight`. Brauer groups of fields are in code (`brauerCohomologyEquiv`, Algebra/CrossedProduct/). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43705 (the finite-cover adapter `IsAzumaya.etale_matrix_splitting_of_finite_cover`, Algebra/Azumaya/EtaleSplitting.lean; not `IsAzumaya.exists_etale_matrix_splitting` or `isAzumaya_iff_positive_fibres_mulLeftRight`).
- Ready now: yes for the ring-level splitting theorems the README places in Suggested.lean (`IsAzumaya.exists_etale_matrix_splitting`, `isAzumaya_iff_positive_fibres_mulLeftRight`, on Mathlib `IsAzumaya`, `Algebra.Etale`); the sheaf-level part needs §1.1 (partial), §§2.4, 2.11, 2.15 (not started) and §2.9 (partial)
- Serves defs: 20
- Evidence: README l.5543 "### 2.22 Sheaves of algebras, Azumaya algebras and the Brauer group of a scheme" (*Needs* l.5606: §1.1, §2.4, §2.9, §2.11, §2.15; Mathlib `IsAzumaya`, `BrauerGroup`).

## TauCetiRoadmap/ReductiveGroupsPartII
STATUS.md snapshot: d92acc5 2026-11-09 (Tau Ceti checked at 91942aa9f, 2026-11-19)

### RG2.0 Topologies on rational points (local and adelic G(F_v))
- Status: PARTIAL. Exists: the affine point topology and topological group (Topology/Algebra/PointTopology/Basic.lean, Group.lean, Separation.lean); compact open integral points `isOpenEmbedding_integralPoints` (Topology/Algebra/PointTopology/IntegralPoints.lean); congruence subgroups (Algebra/AlgebraicGroup/CongruenceSubgroup/Topology.lean, ProP.lean); scheme point topology with open and closed immersions, separation and functoriality (PointTopology/Scheme/, including ClosedImmersion.lean, Separation.lean, Functoriality.lean), fibre products as homeomorphisms of points `pointsHomeomorphOfIsPullback` (Scheme/FiberProduct.lean) and local compactness for schemes locally of finite type `locallyCompactSpace_of_locallyOfFiniteType` (Scheme/LocallyCompact.lean); Frobenius fixed points of Ĕ, `TauCeti.MaxUnramifiedCompletion.fixedPoints_frobenius`, `fixedPoints_integerFrobenius`, `frobenius_congr` (NumberTheory/LocalField/Unramified/Frobenius.lean), and `G(E) = G(Ĕ)^σ` on points of affine groups, `rationalPointsContinuousMulEquiv` (NumberTheory/LocalField/Unramified/Points.lean). Missing: smooth maps open on points and analytic charts with Haar Jacobians (the archimedean charts are here). Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/43504 (RG2.0.2 local compactness and Hausdorffness of points over a nonarchimedean local field and its valuation ring, `SchemePointTopology.locallyCompactSpace_of_localField`, `locallyCompactSpace_of_integer`) and https://github.com/TauCetiProject/TauCeti/pull/42812 (polynomial Jacobian local coordinates and open projection, the inverse-function input to `smooth-morphism-open-map`, Analysis/MvPolynomial/Implicit.lean).
- Ready now: yes. The remaining items depend only on this layer and on Mathlib/LocalFields. Adelic points themselves are owned by AdelicAlgebraicGroups (see its section), which consumes the RG2.0 analytic charts.
- Serves defs: 67, 68, 73, 83, 90
- Evidence: README l.437 "## Layer RG2.0: topologies on rational points"; STATUS "remaining: smooth maps open on points, analytic charts and Haar Jacobians, Frobenius fixed points of Ĕ, scheme-level functoriality" (STATUS predates `fixedPoints_frobenius`, `rationalPointsContinuousMulEquiv` and the scheme functoriality files).

### RG2.3 (RG2.3.1) Reductive integral models and hyperspecial subgroups
- Status: NOT-STARTED. No `SmoothModel`, `IsHyperspecialSubgroup` or `ModelField`. The relative reductivity predicate `reductiveCommHopfAlgPropertyOver` exists (Algebra/AlgebraicGroup/Reductive/Over.lean). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/37909 (RG2.3.1: `IntegralModel.SmoothModel`, reductive models, `IntegralModel.integralPoints`, the hyperspecial-subgroup predicate and the standard model of `GL_n`, Algebra/AlgebraicGroup/IntegralModel/).
- Ready now: yes for RG2.3.1 (*smooth-affine-model*, *reductive-model*): it needs RG2.0 integral points (done) and ReductiveGroups Layer 3. The rest of RG2.3 (parahorics, Bruhat-Tits schemes) needs RG2.1 (partial) and RG2.2 (untouched).
- Serves defs: 67, 82, 83, 88, 90 (88 and 90 through SmoothRepresentationsOfLocalGroups SR.4 and AdelicAlgebraicGroups AA.3.1)
- Evidence: README l.3760 "## Layer RG2.3: parahoric and congruence group schemes", l.3858 "**Reductive models over O and hyperspecial subgroups.** (*reductive-model*)"; STATUS RG2.3 "untouched". AdelicAlgebraicGroups l.2572 and SmoothRepresentationsOfLocalGroups (From ReductiveGroupsPartII) cite RG2.3 *reductive-model*, *hyperspecial-vertices*.

### RG2.5 Dual group and L-group
- Status: NOT-STARTED. No `AbsoluteRootData`, `LGroup` or dual-group declarations. Supplier pieces exist: `TauCeti.Pinning`, `RootPairingIsogeny`, `centerGroupScheme`, `IsCentralIsogeny`.
- Ready now: no: needs RG2.1 (π₁(G), z-extensions; partial), the ReductiveGroups Layer 7 root datum and the Layer 9 pinned Chevalley-Demazure group (both partial).
- Serves defs: 11, 88, 90 (through SmoothRepresentationsOfLocalGroups SR.4.2 spherical parameters)
- Evidence: README l.6704 "## Layer RG2.5: integral dual data", l.6724 "### RG2.5.1 the dual group and its Galois action", l.6931 "### RG2.5.2 the L-group and its functoriality"; STATUS RG2.5 "untouched".

## TauCetiRoadmap/AdelicAlgebraicGroups
No STATUS.md (roadmap merged 2026-11-13; Tau Ceti checked at 91942aa9f, 2026-11-19). No Suggested.lean declaration (`Reduction.IsSArithmetic`, `Reduction.levelArithmetic`, `Neat.IsNeatLevel`, adelic points) exists in Tau Ceti.

### AA.0 Restricted products of Haar measures; Haar measures of the adeles and ideles
- Status: NOT-STARTED. Suppliers in code: `TauCeti.awayDecomposition` (Topology/Algebra/RestrictedProduct/Away/Decomposition.lean), `InfiniteAdeleRing.homeomorphMixedSpace` (NumberTheory/NumberField/Global/Adeles/Basic.lean), `restrictedProductCongr`.
- Ready now: partly. AA.0.1 (Borel structure of a restricted product) needs only Mathlib. The measure targets (AA.0.2–AA.0.4) need AnalyticNumberTheoryPartII §5.3f `exists_unique_restrictedAddHaar` (not implemented).
- Serves defs: 68, 83, 90
- Evidence: README l.633 "## Layer 0: restricted products of Haar measures", l.989 Dependencies ("AnalyticNumberTheoryPartII §5.3f for the restricted product of Haar measures").

### AA.1.1–AA.1.3 Adelic points, integral models, restricted-product comparison, Lie group structure of archimedean points, rational points and the centre
- Status: NOT-STARTED. Suppliers in code: point topology `TauCeti.PointTopology` with `isOpenEmbedding_mapValue_integer`, `isCompact_range_mapValue_integer`; Weil restriction; `TauCeti.GlobalNumberFields.adeleBaseChangeEquiv`; congruence subgroups `TauCeti.HopfAlgebra.congruenceSubgroup`. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/40862 (`TauCeti.AdelicPoints`, `FiniteAdelicPoints`, `InfinitePoints`, `LocalPoints`, diagonals and projections), https://github.com/TauCetiProject/TauCeti/pull/41854 (adelic point groups over a Dedekind domain, `S`-integral Hopf models and the restricted-product comparison, Algebra/AlgebraicGroup/Adelic/) and https://github.com/TauCetiProject/TauCeti/pull/42588 (adelic points, `S`-integral models and `IntegralModel.exists_restrictedProductEquiv`, Algebra/AlgebraicGroup/AdelicPoints/).
- Ready now: yes for AA.1.1 (adelic points, integral models over `S`-integers, spreading out, reductive models outside finitely many places): it needs only Tau Ceti's points and point topology. AA.1.2 needs AA.0.3 (measure-free clauses aside) and, for "Archimedean points are a Lie group with finitely many components", RepresentationTheory/LieGroups layer 2.
- Serves defs: 67, 68, 73, 76, 83, 88, 90
- Evidence: README l.996 "## Layer 1: adelic points of algebraic groups", l.1003 "### 1.1 Affine points and integral models", l.1155 "### 1.2 Restricted-product realization", l.1211 "**Archimedean points are a Lie group with finitely many components.**", l.1258 "### 1.3 Rational points and functoriality" ("The centre on adelic points").

### AA.1.5 Unimodularity and compact open levels
- Status: NOT-STARTED.
- Ready now: no: needs AA.1.2, AA.0.1 and, for local unimodularity of reductive groups, ReductiveGroupsPartII RG2.4 (untouched).
- Serves defs: 67, 68, 76, 83, 90
- Evidence: README l.1444 "### 1.5 Unimodularity and compact open levels"; l.3420 (arithmetic lattices need "AA.1.5 (*The modular character on compact and central elements*)").

### AA.2.1 Characters, the Harish-Chandra map H_G and the split centre A_G
- Status: NOT-STARTED.
- Ready now: no: needs AA.1 and, for `A_G`, ReductiveGroups layers 4 and 7 and ReductiveGroupsPartII RG2.1 (partial).
- Serves defs: 73, 90
- Evidence: README l.1564 "### 2.1 Characters, logarithms and the split centre" (*split-centre-decomposition* `G(𝔸) = G(𝔸)^1 × A_G(ℝ)^0`).

### AA.2.2–AA.2.3 Quotient integration and rational quotients
- Status: NOT-STARTED. Suppliers in code: `MeasureTheory.Measure.exists_isFundamentalDomain_of_properlyDiscontinuousSMul` (MeasureTheory/Group/ProperlyDiscontinuous.lean), `measure_preimage_mul_right_eq_modularCharacter_mul_of_regular` (MeasureTheory/Group/ModularCharacter.lean).
- Ready now: no: needs AA.1, RG2.4 (parabolic modulus) and AnalyticNumberTheoryPartII §5.3k `exists_unique_quotientMeasure` (not implemented).
- Serves defs: 15, 31 (lattices in PU(1,n)), 68, 90
- Evidence: README l.1773 "### 2.2 Parabolic modulus and homogeneous integration", l.1885 "### 2.3 Rational quotients".

### AA.3.1 Rational parabolics, Iwasawa integration, admissible maximal compact K = ∏K_v
- Status: NOT-STARTED.
- Ready now: no: needs ReductiveGroups layer 7, ReductiveGroupsPartII RG2.1, RG2.3 (*reductive-model*, *hyperspecial-vertices*) and RG2.4 (*iwasawa-parabolic-integral*).
- Serves defs: 67, 83, 90
- Evidence: README l.2401 "### 3.1 Rational parabolics and Iwasawa integration", l.2563 "**Admissible maximal compact subgroup of `G(𝔸)`.**".

### AA.3.4 Adelic reduction, S-arithmetic subgroups, Borel–Harish-Chandra, arithmetic lattices in a real Lie group
- Status: NOT-STARTED.
- Ready now: no: needs AA.1–AA.3.3 (and through them RG2.1, RG2.3, RG2.4, LieGroups layer 9).
- Serves defs: 15, 31 (lattices in PU(1,n)), 68 (target: "Arithmetic lattices in a real Lie group" is Def. 68.3), 90
- Evidence: README l.3112 "### 3.4 Adelic reduction and arithmetic quotients", l.3184 `Reduction.IsSArithmetic`, l.3215 "**Borel–Harish-Chandra criterion for arithmetic covolume.**", l.3384 "**Arithmetic lattices in a real Lie group.**".

### AA.4.2 and AA.5.2 Strong approximation; GL₂ over ℚ, K₀(N), and the GL₂ quotients as quotients of the upper half-plane
- Status: NOT-STARTED. Suppliers in code: `TauCeti.HopfAlgebra.congruenceSubgroup`, `IsDedekindDomain.FiniteAdeleRing.integralAdeles`, `FiniteAdeleRing.denseRange_algebraMap`.
- Ready now: no: AA.4.2 needs AA.1–AA.3; AA.5.2's level definitions (*number-field-congruence-levels*) accompany AA.1.5, and its quotient statements follow AA.4.
- Serves defs: 76, 77
- Evidence: README l.4262 "### 4.2 Strong approximation and arithmetic closures", l.5410 "### 5.2 `GL₂` over `ℚ` and principal levels" ("**The `GL_2/ℚ` quotient and the upper half-plane.**").

## TauCetiRoadmap/SmoothRepresentationsOfLocalGroups
No STATUS.md (roadmap merged 2026-11-13; Tau Ceti checked at 91942aa9f, 2026-11-19). None of the Suggested.lean declarations (`SmoothRep`, `smoothVectors`, `IsAdmissible`, `HeckeAlgebraLevel`, `isAdmissible_of_isIrreducible`, `WeilDeligneParameter`) exists in Tau Ceti for this purpose.

### SR.0.1–SR.0.4 The smooth category over any ring: smoothness, the abelian category, invariants and averaging, admissibility, smooth characters, the centre
- Status: PARTIAL: *van-dantzig* (SR.0.1) is in code: `TauCeti.IsTopologicalGroup.locallyCompact_totallyDisconnected_tfae` (locally compact and totally disconnected, locally compact and nonarchimedean, and compact open subgroups forming a basis at `1` are equivalent), `NonarchimedeanGroup.nhds_one_hasBasis_isCompact_openSubgroup`, `IsCompact.exists_openSubgroup_subset`, `OpenSubgroup.directedOn_isCompact` (Topology/Algebra/Group/OpenSubgroup/Compact.lean). Missing: the rest of SR.0.1 (`Representation.IsSmooth`, `smoothVectors`) and SR.0.2–SR.0.4. Suppliers in code: the smooth discrete carrier `TauCeti.SmoothDiscreteTopRep` and `discreteRepEquivSmoothTopRep` (RepresentationTheory/Homological/ContCohomology/SmoothDiscrete/Basic.lean). Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/43075 (SR.0.1: van Dantzig's theorem, `Representation.IsSmooth`, `Representation.smoothVectors`; its van Dantzig part duplicates the code above), https://github.com/TauCetiProject/TauCeti/pull/40280, https://github.com/TauCetiProject/TauCeti/pull/40494 and https://github.com/TauCetiProject/TauCeti/pull/40590 (overlapping parts of SR.0.1), and https://github.com/TauCetiProject/TauCeti/pull/41359 (*unit-pro-order*, `TauCeti.HasUnitProOrder`).
- Ready now: yes. Its suppliers are Mathlib's `Representation`, `Rep`, invariants and `CatCenter`, and Tau Ceti's discrete carrier and profinite exhaustion (ProfiniteCohomology layers 0–1, Completed/ProfiniteProPGroups layer 1).
- Serves defs: 67, 73, 83, 88, 90
- Evidence: README l.581 "## Layer SR.0: the smooth category and its basic API", l.588 "### SR.0.1 Locally profinite groups and smoothness" (l.590 *van-dantzig*), l.869 "### SR.0.4 Admissibility, characters, duals, coefficients and the centre", l.1037 Dependencies.

### SR.1.1–SR.1.3 Hecke algebras over rings: C_c^∞(G), convolution, level algebras, smooth representations as Hecke modules
- Status: NOT-STARTED. Supplier in code: the double-coset Hecke ring (NumberTheory/HeckeRing/).
- Ready now: no: needs SR.0. The reductive-group statements also need ReductiveGroups layer 7 and ReductiveGroupsPartII RG2.3 and RG2.4 (untouched).
- Serves defs: 67, 83
- Evidence: README l.1042 "## Layer SR.1: Hecke algebras over rings", l.1050 "### SR.1.1 Functions, measures and convolution", l.1220 "### SR.1.2 Level algebras and the double-coset ring", l.1299 "### SR.1.3 Smooth representations as Hecke modules", l.1661 Dependencies.

### SR.3a.1 Irreducible representations are admissible; Schur's lemma; central character
- Status: NOT-STARTED.
- Ready now: no: needs SR.0, SR.1 and SR.2 (Jacquet functors, parabolic induction; not started) and ReductiveGroupsPartII RG2.0, RG2.3, RG2.4.
- Serves defs: 67, 73
- Evidence: README l.2419 "**Irreducible representations are admissible** (*admissibility-of-irreducibles*)" ("V has a central character ω_V : Z(G) → ℂ^×"), l.2556 Dependencies.

### SR.4.1–SR.4.2 The Satake transform and isomorphism; spherical parameters
- Status: NOT-STARTED. Classical `GL₂` input in code: `HeckeRing.GL2.Newform.satakeParameters` (NumberTheory/ModularForms/Newforms/Satake.lean).
- Ready now: no: needs SR.1 and SR.2, ReductiveGroupsPartII RG2.1, RG2.3 (hyperspecial `K`), RG2.4 and RG2.5 (dual group, untouched).
- Serves defs: 67, 88, 90
- Evidence: README l.3184 "## Layer SR.4: spherical representations and Satake", l.3193 *satake-transform*, l.3252 *satake-isomorphism*, l.3317 *spherical-parameter*, l.3701 Dependencies.

### SR.5.2 (WD parameters) *wd-raw-parameters*, *nilpotent-exp-log*, *wd-parameter-operations*, *wd-algebraic-composition*
- Status: PARTIAL: *nilpotent-exp-log* is in code: `IsNilpotent.log` with `log_eq_sum` (independence of the vanishing bound), `isNilpotent_log`, `map_log`, `log_conj`, `log_exp`, `exp_log`, `expEquiv`, `Units.log_zpow` (RingTheory/Nilpotent/Log.lean); the unique unipotent `m`-th root `Units.existsUnique_isNilpotent_sub_one_and_zpow_eq` with `nilpotentExpUnit_inv_smul_log_zpow` (RingTheory/Nilpotent/UnipotentRoot.lean); the `ℤ_ℓ`-homomorphism formula `MonoidHom.padicInt_coe_apply_eq_exp_smul_log` (`h x = exp (x • log (h 1))`, NumberTheory/Padics/UnipotentHom.lean, Tau Ceti PR #40919); matrix one-parameter subgroups `exp(tX)` (`nilpotentOneParameterCoordinateMap`, Algebra/AlgebraicGroup/GeneralLinear/Unipotent/OneParameter.lean). NOT-STARTED for *wd-raw-parameters*, *wd-parameter-operations* and *wd-algebraic-composition* (no `WeilDeligneParameter`). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/40845 (*wd-raw-parameters*: `TauCeti.WeilDeligneParameter`, `IsFrobeniusSemisimple`, `Hom`, `Iso`, transport, RepresentationTheory/WeilDeligne/).
- Ready now: yes. *wd-raw-parameters* needs Mathlib and ClassFieldTheory layer 9 (done); *wd-parameter-operations* adds RepresentationTheory/InductionRestriction layers 0 and 2; *wd-algebraic-composition* adds ReductiveGroups Layers 2 and 4 (done) and 5P (partial, its matrix exponential and logarithm are in code). None needs the earlier SR layers.
- Serves defs: 86 (target: *wd-algebraic-composition* is Def. 86.1–86.3)
- Evidence: README l.4475 "#### WD raw parameters", l.4513 "#### Nilpotent exp-log", l.4561 "#### WD parameter operations", *wd-algebraic-composition* l.4590 ("**Composition with an algebraic representation and symmetric powers**"); ArithmeticGaloisRepresentations §2.4 (arithmetic Weil–Deligne adapter) consumes it.

## TauCetiRoadmap/AutomorphicFormsOnReductiveGroups
No STATUS.md (merged as roadmap PR #1037; Tau Ceti checked at 91942aa9f, 2026-11-19). None of `LieTestFunction`, `AdelicSchwartzFunction`, `RestrictedTensor`, `WeilGroupReal`, `HasInfinitesimalCharacter`, `IsGFinite`/`gFiniteSubmodule` exists in Tau Ceti.

### §§0.1a–0.3 Lie test functions, adelic test functions and the adelic Schwartz algebra
- Status: NOT-STARTED. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/43595 (§0.1a test functions `TauCeti.LieTestFunction` with translations, involution and smooth approximate identities, Geometry/Lie/TestFunction/) and https://github.com/TauCetiProject/TauCeti/pull/43598 (`TauCeti.contMDiffAt_parametric_integral_of_isCompact` and `contMDiff_integral_inv_mul`, the smoothness input for the convolution of Lie test functions).
- Ready now: yes for §0.1a (`LieTestFunction`, convolution, `smoothApproximateIdentity`): it needs Mathlib `ContMDiffMap`, `TestFunction` and LieGroups Layer 0 (done). §§0.2–0.3 need AdelicAlgebraicGroups Layers 0–3, ArithmeticLocallySymmetricSpaces ALS.F.1, ALS.F.6 and SmoothRepresentationsOfLocalGroups SR.0–SR.1 (not started), and LieGroups Layer 9 `KAK` (partial) for `integrable_height_rpow_neg`.
- Serves defs: 83 (target: `AdelicSchwartzFunction`, §0.3), 90
- Evidence: README l.87 "## Layer 0: Smooth adelic functions, growth and convolution", l.114 "### 0.1a Test functions on the archimedean group", l.127 "### 0.2 Test functions and their topology", l.143 "### 0.3 Schwartz functions on the group", l.228 Dependencies.

### §§2.1–2.4, 2.6–2.7 Harish-Chandra modules, infinitesimal characters, real induction, discrete series, explicit GL₂ modules, smooth vectors and globalization
- Status: NOT-STARTED. Inputs in code: `TauCeti.harishChandraIso`, `centralCharacterModules`, `TauCeti.centerToEnd`, `TauCeti.envelopingAction`, `lieExp`. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43608 (RepresentationTheory/Continuous/LieSmoothVector.lean: §2.7 smooth vectors and the derived action).
- Ready now: yes for the smooth vectors of §2.7 (`IsLieSmoothVector`, `lieSmoothVectors` of a Banach `ContRepresentation`), which use `lieExp` and Mathlib `ContMDiff`. §2.1 needs CompactGroups Layer 5's `IsGFinite`, `gFiniteSubmodule_dense` (recorded as `gap:banach-gfinite-density`, not in code); §2.2 needs LieHighestWeight §9.2 (ready, not started); §§2.3–2.4 need ArithmeticLocallySymmetricSpaces ALS.F.1 and ALS.0.1–ALS.0.3 (not started) and LieGroups Layers 7 and 9 (partial).
- Serves defs: 5 (target: §2.2 `HasInfinitesimalCharacter`), 7 (target: `IsSquareIntegrable` §2.4, `D_k(μ)` §2.6), 67, 73, 76 (§2.6), 83 (§2.7 smooth vectors), 88 (§2.2)
- Evidence: README l.299 "## Layer 2: real reductive representations and globalizations", l.301 "### 2.1 Compact-finite vectors and admissibility", l.345 "### 2.2 Infinitesimal characters and Harish-Chandra finiteness" (*Needs* l.351), l.390 §2.3, l.416 §2.4, l.462 "### 2.6 Explicit GL₂ modules and the generic unitary dual", l.487 "### 2.7 Smooth Fréchet representations and globalization", l.520 Dependencies.

### §2.3a Minimal parabolic subgroups and the Langlands decomposition
- Status: NOT-STARTED (only the `GL_n` Iwasawa decomposition `TauCeti.iwasawaDiffeomorph`, Geometry/Lie/Iwasawa.lean, and dynamic parabolics for the algebraic comparison).
- Ready now: no: needs LieGroups Layer 9 (partial), ArithmeticLocallySymmetricSpaces ALS.F.1 and ALS.0.1–ALS.0.3 (not started), and ReductiveGroups Layer 7 (partial) for the algebraic comparison.
- Serves defs: 79 (target), 4 (minimal parabolics), 1 (maximal `ℝ`-split torus for RealSemisimpleLieGroups §2.4)
- Evidence: README l.372 "### 2.3a Minimal parabolic subgroups and the Langlands decomposition", *Needs* l.380.

### §2.5 Weil groups and archimedean parameters
- Status: NOT-STARTED. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43493 (the first part of §2.5: `WeilGroupComplex`, `WeilGroupReal`, `includeComplex`, `j`, `norm`, `abelianizationEquiv`, NumberTheory/ClassFieldTheory/WeilGroup/Archimedean.lean; not the characters, `induceCharacter` or `irreducibleClassification`).
- Ready now: yes for the first paragraph (`WeilGroupComplex`, `WeilGroupReal`, `norm`, `induceCharacter`, `irreducibleClassification`, symmetric powers of semisimple continuous Weil representations): Mathlib only. `recGL` needs §§2.3–2.4.
- Serves defs: 86 (target: 86.4), 5 (Remark 2)
- Evidence: README l.446 "### 2.5 Weil groups and archimedean parameters" ("For every `m≥0`, the `m`-th symmetric power `w↦Sym^m(r(w))` ... is again a semisimple continuous representation").

### §§3.1–3.5 Adelic automorphic modules, central characters, restricted tensor products and Flath factorization
- Status: NOT-STARTED. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/43596 (§3.4 restricted tensor products `TauCeti.RestrictedTensor` with `ofFinite`, `tprod`, `lift`, `stageMap_injective`, LinearAlgebra/PiTensorProduct/Restricted.lean) and https://github.com/TauCetiProject/TauCeti/pull/43600 (the existence half of `TauCeti.finiteCornerFactorization` for simple modules over `A ⊗[k] B`, Algebra/TensorProduct/SimpleModule.lean). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43644 (RingTheory/Idempotents/Corner/Simple.lean: the §3.4 corner simplicity step).
- Ready now: yes for the algebraic part of §3.4 (`RestrictedTensor`, `ofFinite`, `tprod`, `finiteCornerFactorization`): Mathlib finite tensor products, filtered colimits and finite-dimensional density only. The rest needs ArithmeticLocallySymmetricSpaces ALS.F.6, Layers 0–2, AdelicAlgebraicGroups §§1.1, 3.1, 3.4, SmoothRepresentationsOfLocalGroups SR.0, SR.1, SR.4.1 and ReductiveGroupsPartII RG2.3 (none started).
- Serves defs: 67 (target: §§3.4–3.5), 72 (`twist`, `centralCharacter`, §3.2, used by GL2AutomorphicRepresentationsAndTransfer R16.4.6), 73 (target: `centralCharacter`, §3.2), 76, 88, 90
- Evidence: README l.524 "## Layer 3: adelic modules and their local factors", l.543 "### 3.2 The global algebra and automorphic representations", l.581 "### 3.4 Restricted tensor products and finite corners", l.598 "### 3.5 Spherical lines and Flath factorization", l.620 Dependencies.

### §§4.1–4.2 Constant terms, cuspidal globalization and discrete occurrences
- Status: NOT-STARTED.
- Ready now: no: needs Layers 0–3, ArithmeticLocallySymmetricSpaces ALS.F.6, AdelicAlgebraicGroups §§2.2, 3.4, 4.2 and ReductiveGroupsPartII RG2.4.
- Serves defs: 72, 90
- Evidence: README l.624 "## Layer 4: constant terms, cuspidal realizations and Fourier tests", l.644 "### 4.2 Cuspidal globalization and actual discrete occurrences" (`DiscreteOccurrence(G,ω)`), l.731 Dependencies.

### §§7.2–7.3 The GL₂ adelization, adelic lifts, Hecke and diamond normalization
- Status: NOT-STARTED. Classical inputs in code: `HeckeRing.GL2.Newform`, `EigenformAwayFromLevel.conductor`, `primitiveAssociate` (NumberTheory/ModularForms/Newforms/Conductor.lean), `HeckeCharacter.finiteConductor`.
- Ready now: no: needs Layers 0–6 as listed in its Dependencies, in particular §§3.1–3.2, §2.6 and AdelicAlgebraicGroups AA.4.2, AA.5.2 (strong approximation, `K₀(N)`).
- Serves defs: 76 (target: `adelize` and the newform's cuspidal occurrence)
- Evidence: README l.1148 "### 7.2 The GL₂ adelization and its inverse", l.1174 §7.2a, l.1187 "### 7.3 Hecke and diamond normalization for GL₂", l.1305 Dependencies.

## TauCetiRoadmap/ArithmeticLocallySymmetricSpaces
No STATUS.md (merged as roadmap PR #871; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `IsCartanInvolution`, `LocallySymmetric.AutomorphicForm` in Tau Ceti: no hits; the matrix polar and Cartan decompositions `Subgroup.cartanHomeomorph` exist.

### ALS.F.1, ALS.0.1–ALS.0.4 Real points and maximal compact subgroups, Cartan involutions of real reductive groups, the Cartan datum, the symmetric space X^G
- Status: NOT-STARTED.
- Ready now: no: ALS.F.1 and ALS.0.1 need LieGroups Layer 9 (partial); ALS.0.1–ALS.0.2 also AdelicAlgebraicGroups AA.3.7; ALS.0.4 needs ALS.0.1, ALS.0.3 and AdelicAlgebraicGroups §2.1 (`A_G`, not started).
- Serves defs: 1, 79 (ALS.0.1 conjugacy of Cartan involutions), 4, 7 (through AutomorphicFormsOnReductiveGroups §§2.3a–2.4), 62 (ALS.0.4)
- Evidence: README l.579 "### ALS.F.1 Real points of linear algebraic groups and their maximal compact subgroups", l.1167 "### ALS.0.1 Cartan involutions of real reductive groups", l.1246 "### ALS.0.2 Real points and the Lie-theoretic Cartan datum", l.1287 "### ALS.0.3 Maximal compact subgroups from Cartan involutions", l.1309 "### ALS.0.4 The symmetric space of G with the split-centre correction".

### ALS.F.6 Automorphic forms, constant terms and cusp forms
- Status: NOT-STARTED (no `LocallySymmetric.AutomorphicForm`).
- Ready now: no: needs ALS.F.1, AdelicAlgebraicGroups §§1.3, 2.1, 3.4, 3.6 and SmoothRepresentationsOfLocalGroups SR.0 (not started); LieHighestWeight Layer 7 is done.
- Serves defs: 67, 72, 73, 76, 88, 90
- Evidence: README l.995 "### ALS.F.6 Automorphic forms, constant terms and cusp forms" (`cuspidalSpectrum_discrete`, `cuspidalRepresentation`).

### ALS.0.6, ALS.1, ALS.3 Arithmetic locally symmetric spaces X_K, Betti complexes and finite-level Hecke actions
- Status: NOT-STARTED.
- Ready now: no: ALS.0.6 needs ALS.0.4 and AdelicAlgebraicGroups §§3.4, 4.4; ALS.1.1 needs ALS.0.6, ALS.0.9 and ALS.F.4; ALS.3.1 needs SmoothRepresentationsOfLocalGroups SR.1.1–SR.1.2 (not started).
- Serves defs: 77 (the finite-level spaces `X_K` with Betti cohomology and Hecke actions)
- Evidence: README l.1399 "### ALS.0.6 The arithmetic locally symmetric space `X_K`" (*Needs* "ALS.0.4; AdelicAlgebraicGroups §4.4 ... §3.4"), l.1754 "## Layer ALS.1: Arithmetic coefficients and Betti complexes", l.2680 "## Layer ALS.3: Finite-level Hecke actions and correspondences".

## TauCetiRoadmap/RepresentationTheory/LieGroups
STATUS.md snapshot: a6027b1 2026-11-11 (umbrella RepresentationTheory/STATUS.md; Tau Ceti checked at 91942aa9f, 2026-11-19)

### Layer 7 (first bullet) Compact real form of a complex semisimple Lie algebra; Cartan involution θ of a real semisimple 𝔤₀
- Status: PARTIAL. Exists: the conjugate-linear involution τ of the Serre-presented algebra, `TauCeti.serreCompactInvolution` (τHᵢ = −Hᵢ, τEᵢ = −Fᵢ, τFᵢ = −Eᵢ, `serreCompactInvolution_lie`, `serreCompactInvolution_involutive`, uniqueness `eq_serreCompactInvolution`, agreement with `serreChevalleyInvolution` for a trivial star; Algebra/Lie/Presentation/Serre/CompactInvolution.lean), on the conjugate Lie algebra `TauCeti.ConjLieAlgebra` (Algebra/Lie/Conjugate.lean). Other ingredients: `serreLiftEquiv` (Serre/Injective.lean), `serreChevalleyInvolution` (Serre/Automorphism.lean), Chevalley involution and structure-constant normalization (Algebra/Lie/Weights/Chevalley/Involution.lean, Algebra/Lie/Weights/StructureConstant/Normalization.lean). Missing: the Hermitian form H_τ(x, y) = −B(x, τy) and its positivity, the compact real form 𝔲 = Fix τ, real-form descent, and θ = στ|𝔤₀ (grep `compactRealForm|CartanInvolution` empty). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43614 (Algebra/Lie/CompactRealForm/: compact real forms of complex semisimple Lie algebras).
- Ready now: yes. This is a purely Lie-algebraic bullet. Its inputs (LieHighestWeight Layer 7 Serre presentation and Layer 0 sl₂ strings, and τ) are in place. H_τ positivity, real-form descent and θ = στ|𝔤₀ can all be built now. The later group-level Layer 7 bullets (universal complexification, compact integration) are not ready: they need Layer 4 integration (partial) and Layer 5 covers.
- Serves defs: 1, 4, 7, 15, 31, 54, 62, 79
- Evidence: README l.787 "### Layer 7: complexification and real forms", first bullet l.788 "**Compact real forms of semisimple Lie algebras.**", θ at l.802-806 ("Layer 9 consumes this θ"); STATUS "Layer 7 holding only realification"; Tau Ceti PR #37665 (CompactInvolution.lean). Consumers: RealSemisimpleLieGroups Layers 0 and 2 (existence of Cartan involutions, real forms §2.5) and AutomorphicFormsOnReductiveGroups §§2.3–2.4.

### Layer 9 Cartan, Iwasawa, KAK decompositions (CartanInvolution, IsRealReductive, cartan_polar_decomposition, IwasawaData, restricted roots, kakDecomposition)
- Status: PARTIAL. Only matrix cases exist: Iwasawa `iwasawaDiffeomorph` (Geometry/Lie/Iwasawa.lean, LinearAlgebra/Matrix/GeneralLinearGroup/Iwasawa.lean), KAK for GL_n(ℝ/ℂ) (LinearAlgebra/Matrix/GeneralLinearGroup/Cartan.lean), maximal compact (…/MaximalCompact.lean), symplectic polar and Cartan involution (Analysis/Matrix/Polar/Symplectic.lean, Geometry/Lie/Symplectic/Cartan.lean), unitary upper-triangular with positive diagonal = 1 (Analysis/Matrix/Triangular.lean); the Cartan decomposition `Subgroup.cartanHomeomorph` of a star-stable subgroup of the units of a C*-algebra (Analysis/SpecialFunctions/ContinuousFunctionalCalculus/Cartan.lean), instantiated for `SL n`, `Sp(2n, ℝ)` and the realified `GL(n, ℂ)` (Analysis/Matrix/Cartan.lean, Analysis/Matrix/Cartan/Realify.lean), with the polar order `A = exp X * realify U` on `Sp(2n, ℝ)` as `TauCeti.GLSymplectic.leftCartanHomeomorph` (Analysis/Matrix/Cartan/Realify.lean); the positive upper-triangular group as a Lie group with global exponential coordinates and its real-diagonal triangular Lie algebra (`TauCeti.Lie.posUpperTriangularLieGroup`, `posUpperTriangularLog`, Geometry/Lie/Subgroup/PosUpperTriangular/{Basic,Exponential}.lean; `upperTriangularRealDiagonalLieSubalgebra`, Algebra/Lie/GeneralLinear/RealTriangular.lean). None of the Suggested.lean names exist: `FiniteCartanMatrixModel`, `CartanInvolution`, `IsRealReductive`, `IwasawaData`, `IsIwasawaTriple`, `iwasawaDecomposition`, `kakDecomposition`, `cartan_polar_decomposition`, `restrictedRoots`, `Nplus`, `triangularRealDiagonal`, `positiveTriangular`, `bijOn_exp_triangular`, `lieExp_bijective_of_immersed_positiveTriangular`.
- Ready now: partly. Ready: the global matrix-cover model with `cartan_polar_decomposition` for a closed transpose-stable H ≤ GL_N (it consumes the matrix polar decomposition and `Subgroup.cartanHomeomorph`), and the "Connected subgroups of the positive triangular group" bullet, whose carrier and exponential coordinates are in code. Not ready: the semisimple finite-center specialization, restricted roots/KAK and the general Iwasawa theorem. These need Layer 7's θ (partial: τ only) and Layer 6 tori (partial).
- Serves defs: 1, 4, 7, 15, 31, 54, 62, 79, 83
- Evidence: README l.1199 "### Layer 9: the Cartan, Iwasawa, and KAK decompositions", l.1230 `cartan_polar_decomposition`/`CartanInvolution`/`IsRealReductive`, l.1354 "**Restricted roots and KAK.**"; STATUS "remaining: the global real-reductive Cartan, Iwasawa and KAK decompositions beyond GL n"; Suggested.lean l.459-652. Consumers: RealSemisimpleLieGroups Layers 2–5 (§5.7 for 15, 31), AutomorphicFormsOnReductiveGroups §§2.3a–2.4 and ArithmeticLocallySymmetricSpaces ALS.F.1, ALS.0.1.

### Layer 5 enveloping-algebra bullet U(𝔤) as left-invariant differential operators; central characters
- Status: PARTIAL. Done: `TauCeti.envelopingAction` and `range_envelopingAction` (Geometry/Lie/EnvelopingAlgebra/Basic.lean); `envelopingAction_injective` and `envelopingAlgEquivAdjoin` (Geometry/Lie/EnvelopingAlgebra/Faithful.lean); the central action `TauCeti.centerToEnd : Z(A) →ₐ[k] End_A(M)` for any module over any algebra (RingTheory/Semisimple/CentralCharacter.lean), so `Z(U_ℝ(𝔤)) → End_{U(𝔤)}(V)`; the scalar central character of a finite-dimensional irreducible Lie module over an algebraically closed field, `TauCeti.UniversalEnvelopingAlgebra.centralCharacter` with `representation_eq_centralCharacter_smul`, `centerEigenspace_centralCharacter`, `centralCharacter_congr` (Algebra/Lie/UniversalEnveloping/CentralCharacter.lean, Tau Ceti PR #37752), whose docstring records the real circle rotation module example. Missing: the scalar central character of real absolutely irreducible modules, and the division-commutant statement for irreducible real modules. The highest-weight version exists in LieHighestWeight (`vermaCentralCharacter`). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43492 (central action through the division commutant and the scalar central character beyond algebraically closed fields: `TauCeti.isField_center`, `centerToCenterEnd`, Algebra/Lie/UniversalEnveloping/CentralCharacter.lean).
- Ready now: yes. Layer 5's other bullets (covers, centres) are listed separately; this bullet needs only LieHighestWeight Layer 3 PBW, which is done.
- Serves defs: 1, 5, 83
- Evidence: README l.518 "### Layer 5: simply-connected covers and the enveloping algebra", bullet l.626 "**The universal enveloping algebra.**"; STATUS Layer 5 "partial" (no remaining text); grep envelopingAction hits the 2 files above.

### Layer 8 Borel-Weil, complex flag manifolds, Bruhat (minimal parabolics P_α)
- Status: NOT-STARTED
- Ready now: no: needs the Layer 7 algebraization of compact complexifications and ReductiveGroups Layer 7 generic Bruhat (partial).
- Serves defs: 4 (weak link)
- Evidence: README l.1078 "### Layer 8: Borel-Weil, flag manifolds, and Bruhat"; the minimal parabolics are complex algebraic P_α ⊂ G_ℂ (l.1155 "minimal-parabolic map pα:G/B+→G/Pα+"), not real parabolics; STATUS Layer 8 "untouched".

## TauCetiRoadmap/RepresentationTheory/LieHighestWeight
STATUS.md snapshot: a6027b1 2026-11-11 (umbrella RepresentationTheory/STATUS.md; Tau Ceti checked at 91942aa9f, 2026-11-19; README at roadmap 890b66d)

### §9.2 Reductive enveloping centers and the reductive Harish-Chandra isomorphism
- Status: NOT-STARTED. No `productEnveloping`, `productCenterEquiv` or reductive HC isomorphism (grep empty). The inputs exist: `TauCeti.UniversalEnvelopingAlgebra.mapEquiv` (Algebra/Lie/UniversalEnveloping/Functoriality.lean), `prodEquivTensor` (UniversalEnveloping/Prod.lean), `symmetricAlgebraEquiv` (UniversalEnveloping/Abelian.lean), `pbwSymmetrization_mem_center_iff` (UniversalEnveloping/PBW/Symmetrization/Basic.lean), the semisimple `TauCeti.harishChandraIso`/`harishChandraLinearIso` (Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.lean), `LieSubalgebra.lieChevalleyRestrictionIso` (HighestWeight/ChevalleyRestriction.lean), and the reductive structure with `centralWeight` (Algebra/Lie/Reductive/Basic.lean, Algebra/Lie/Weights/Central.lean). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43603 (the §9.3 product map §9.2 builds on: `TauCeti.UniversalEnvelopingAlgebra.productEnveloping : U(Z × S) ≃ₐ Sym(Z) ⊗ U(S)` and `productCenterEquiv : Z(U(Z × S)) ≃ₐ Sym(Z) ⊗ Z(U(S))`, Algebra/Lie/UniversalEnveloping/ProductCenter.lean; not the reductive HC isomorphism).
- Ready now: yes. The README builds `U(L) ≃ Sym(z(L)) ⊗ U([L,L])` from universal properties, then `Z(U(L)) ≃ Sym(z(L)) ⊗ Z(U([L,L]))`, then the reductive HC isomorphisms by tensoring the derived algebra's `harishChandraIso` with the identity; all of these are in code.
- Serves defs: 5, 7, 88 (AutomorphicFormsOnReductiveGroups §2.2 consumes it)
- Evidence: README l.2695 "## Layer 9: reductive Lie algebras and `gl_n`", l.2819 "### 9.2 Reductive enveloping centers and the actual invariant maps" ("Tensor the derived algebra's native **raw** HC isomorphism `TauCeti.harishChandraIso` with the identity on `Sym(z(L))`"); this is the gap merged AutomorphicFormsOnReductiveGroups records as `gap:reductive-enveloping-centers`.

## TauCetiRoadmap/RealSemisimpleLieGroups
No STATUS.md (merged as roadmap PR #2229; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `IsCartanInvolution|restrictedRoot|realRank|IsRiemannianSymmetricSpace` in Tau Ceti: no hits.

### Layers 0–1 Cartan involutions of real semisimple and reductive Lie algebras; restricted roots and real rank (§§0.1–0.4, 1.1–1.4)
- Status: NOT-STARTED. Only special cases: `LieAlgebra.Symplectic.cartanInvolution` (Algebra/Lie/Symplectic/Cartan.lean), `TauCeti.serreCompactInvolution` (Algebra/Lie/Presentation/Serre/CompactInvolution.lean). Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/43400 (§0.1: `LieEquiv.IsCartanInvolution`, `cartanP`, `cartanForm`, the Cartan decomposition `isCompl_fixedSubalgebra_cartanP`, reductive Cartan involutions, Algebra/Lie/CartanInvolution/), https://github.com/TauCetiProject/TauCeti/pull/43026 (§0.1 and the conjugacy and uniqueness part of §0.2 over `ℝ`, with classical examples) and https://github.com/TauCetiProject/TauCeti/pull/43203 (§§0.1–0.4: uniqueness and inner conjugacy of Cartan involutions, ideals, products and classical matrix realizations); these three overlap.
- Ready now: yes for §0.1, §0.3, §0.4 and the direct route of §1.1, with existence of Cartan involutions taken as a hypothesis (README "Ordering"); §0.2 and §1.3 need LieGroups Layers 2, 4 and 9 (`Int(𝔤₀)`, `Ad(K)𝔞 = 𝔭`; Layer 9 partial).
- Serves defs: 1 (target: §1.3 `realRank`), 4, 54, 62, 79
- Evidence: README l.327 "## Layer 0: Cartan involutions of real semisimple and reductive Lie algebras", l.448 "## Layer 1: restricted roots and real rank", l.511 "### 1.3 Conjugacy of maximal abelian subspaces and the real rank"; l.1349 "## Ordering".

### Layer 2 Real rank of groups, global Cartan involution, restricted Weyl group, split tori, real forms (§§2.1–2.5)
- Status: NOT-STARTED.
- Ready now: no: needs Layer 1 and LieGroups Layers 4, 5A, 7 and 9 (§2.4 also AutomorphicFormsOnReductiveGroups §2.3a and ReductiveGroups Layers 4, 6).
- Serves defs: 1 (target: §2.1 `groupRealRank`, §2.4 Borel–Tits rank), 4, 54 (§2.5 is Definition 54.1), 62 (§2.2), 79 (§2.4)
- Evidence: README l.585 "## Layer 2: real rank, restricted Weyl group, hyperbolic elements and real forms", l.587 §2.1, l.621 §2.2, l.674 §2.4, l.734 "### 2.5 Real forms of complex reductive groups"; *Needs* l.619, l.638, l.731, l.788.

### Layers 3–4 Minimal parabolics, Bruhat decomposition, standard and general parabolic subgroups (§§3.1–4.5)
- Status: NOT-STARTED. Inputs in code: Tits systems and standard parabolics (GroupTheory/TitsSystem/), algebraic `IsParabolic` and `Cocharacter.parabolic`.
- Ready now: no: needs Layer 2, AutomorphicFormsOnReductiveGroups §2.3a and LieGroups Layer 9.
- Serves defs: 4 (target: §3.1, §§4.1–4.5), 79 (§3.1 for non-linear groups with finite centre)
- Evidence: README l.802 "## Layer 3: minimal parabolic subgroups and the Bruhat decomposition", l.910 "## Layer 4: parabolic subgroups and Langlands decompositions"; *Needs* l.838, l.897, l.956, l.1029, l.1063.

### Layer 5 (§§5.1–5.6) Riemannian symmetric spaces: G/K, Killing metric, maximal compacts, flats, quotients
- Status: NOT-STARTED. Inputs in code: `TauCeti.RiemannianIsometry`, `CovariantDerivative.HasParallelCurvature` (Geometry/Manifold/Riemannian/Isometry/LocallySymmetric.lean), the free proper quotient theorem (Geometry/Manifold/GroupAction/Quotient.lean), O'Neill's curvature formula (Geometry/Manifold/Riemannian/Submersion/Curvature.lean). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43454 (§5.1: `IsGeodesicSymmetryAt`, `IsRiemannianSymmetricSpace`, `geodesicSymmetry`, `transvectionSubgroup`, covering lifts and examples, Geometry/Manifold/Riemannian/Symmetric/).
- Ready now: yes for §5.1 (`IsRiemannianSymmetricSpace`; needs Tau Ceti isometries and parallel curvature, HopfRinow, RiemannianGeometry R1.2); no for §§5.2–5.6: they need Layer 2 (§2.2), LieGroups Layer 9, SmoothBundlesConnections B1.4's `G/H`, RiemannianGeometry R1.3 and R4 item 4.
- Serves defs: 62 (target), 15, 31 (§5.7 builds on §§5.2, 5.3, 5.5)
- Evidence: README l.1076 "## Layer 5: Riemannian symmetric spaces", l.1078 §5.1, l.1104 §5.2, l.1133 §5.3, l.1168 §5.4, l.1219 §5.5, l.1253 §5.6; *Needs* l.1101, l.1131, l.1166, l.1216, l.1282.

### §5.7 Complex hyperbolic space (U(1,n), PU(1,n), the ball, ω_X, complex totally geodesic submanifolds)
- Status: NOT-STARTED (no `PU(1,n)` or ball in Tau Ceti; only the `n = 1` Fuchsian theory).
- Ready now: no: needs §0.4, §§5.2, 5.3, 5.5, LieGroups Layer 9 and ComplexKahlerGeometry Kähler forms.
- Serves defs: 15, 31 (Setting 31.1, Proposition 31.3)
- Evidence: README l.1285 "### 5.7 Complex hyperbolic space"; *Needs* l.1337.

## TauCetiRoadmap/JacobianChallenge
STATUS.md snapshot: 794f43e 2026-11-16, generated against Tau Ceti aa6e43e (Tau Ceti checked at 91942aa9f, 2026-11-19; README at roadmap 890b66d)

### Layer C §§C.1–C.2 relative coherent cohomology and base change, §C.4 Hilbᵈ = Symᵈ X
- Status: PARTIAL. §C.1: higher direct images local on the target `Scheme.Hom.higherDirectImageRestrictIso`, quasi-coherent for qcqs `f` `Scheme.Hom.isQuasicoherent_higherDirectImage` (Cohomology/HigherDirectImage/Quasicoherent.lean), vanishing along affine morphisms `isZero_higherDirectImage_succ_of_isAffineHom` and finite presentation along finite morphisms `isFinitePresentation_higherDirectImage_of_isFinite` (HigherDirectImage/Affine.lean); Hartshorne II.5.14 `exists_map_eq_tmulRight_tensorPowSection` (LineBundle/TwistedSections.lean). §C.2: flat base change over an affine base `bijective_cohomologyBaseChange` (Cohomology/FlatBaseChange.lean), Mumford's finite projective model `CochainComplex.exists_quasiIso_finite_projective` (Algebra/Homology/ModuleCat/BaseChange.lean) and `LinearMap.upperSemicontinuous_finrank_fiber_homology` (RingTheory/Spectrum/Prime/Semicontinuity.lean). §C.4: the functor `relativeEffectiveCartierDegreeSubfunctor` (EffectiveCartierDivisor/Degree/Basic.lean), representable for `d ≤ 1` (`graphDivisorDegreeOne`, EffectiveCartierDivisor/Representable.lean). Missing: coherence of `R^q f_*` for proper `f`, flat base change over a non-affine base, semicontinuity and cohomology and base change for proper flat `f`, Grauert, `Hilbᵈ` for `d ≥ 2`. Open Tau Ceti PRs for §C.1 in the projective case https://github.com/TauCetiProject/TauCeti/pull/41421 (Serre's global generation of twists and quotients of `𝒪(-n)` on `Proj`, Hartshorne II.5.17–5.18), https://github.com/TauCetiProject/TauCeti/pull/41909, https://github.com/TauCetiProject/TauCeti/pull/43063, https://github.com/TauCetiProject/TauCeti/pull/43068 and https://github.com/TauCetiProject/TauCeti/pull/43532 (overlapping: Serre finiteness and vanishing and coherence of higher direct images for projective schemes over a Noetherian base, HigherDirectImage/Projective.lean, `exists_epi_free_tensorPow_of_isAmple`); for §C.2 https://github.com/TauCetiProject/TauCeti/pull/39928 (sections of `Rⁿ f_* M` over affine opens of any base), https://github.com/TauCetiProject/TauCeti/pull/42059 (semicontinuity for flat families over a Noetherian affine base, Cohomology/Semicontinuity.lean) and https://github.com/TauCetiProject/TauCeti/pull/42452 (Grauert's theorem for complexes over a reduced ring, `LinearMap.flat_homology_of_isLocallyConstant_finrank_fiber_homology`).
- Ready now: yes for §C.1 in the projective case (global generation of high twists from II.5.14); the proper case needs SchemeAndStackFoundations §4.12 Chow's lemma (partial: graph closure only). §C.2 follows §C.1. §C.4 needs only A.2 and C.2, no Hilbert or Quot scheme.
- Serves defs: 30 (§C.4, and through Layer D); 19, 71, 80, 84, 85 (through SchemeAndStackFoundations §4.14 and Layer D)
- Evidence: README l.673 "## Layer C: relative coherent cohomology and base change"; l.677 "### C.1 Coherent higher direct images under proper morphisms" (*Needs:* B.1; SchemeAndStackFoundations §4.12); l.714 "### C.2 Flat base change, semicontinuity, cohomology and base change"; l.785 "### C.4 The Hilbert scheme of points of a curve" (`isRepresentable_relativeEffectiveCartierDegreeSubfunctor`, "the construction needs no Quot scheme", *Needs:* A.2, C.2); Dependencies l.829 "SchemeAndStackFoundations §4.9, §4.12 (not §4.14, which consumes this layer)". STATUS Layer C remaining "coherence of R^q f_* for proper f, flat base change over a non-affine base, semicontinuity, cohomology and base change, Grauert, Hilb^d"; frontier "Coherence of higher direct images (C.1, hence B.1). Use II.5.14 ...".

### Layer D §§D.2–D.5, D.8 Picard scheme, Pic^0, Jacobian
- Status: PARTIAL: the fppf Picard sheaf `relativePicardFppfSheaf` (PicardFunctor/Fppf.lean) with base change `relativePicardPresheafBaseChangeIso`, the rigidified functor `rigidifiedPicardFunctor`, `relativePicardFiberDegree`, `Pic⁰_{X/S}` as `relativePicardDegreeZeroFppfSheaf` (PicardFunctor/PicZero/), Abel maps on functors `abelJacobiMapOfDegree`, `abelJacobiMapToPicZeroFppf` (PicardFunctor/Abel/), point separation `abelJacobiMap_app_injective_of_genus_pos`. Missing: the named `HasPicardScheme`/`picardScheme` (§D.2), Hilbert quotients (§D.3), projective Picard representability (§D.4), representability of `Pic⁰` and the Abel morphisms `AJ_d` (§D.5), smoothness and properness (§§D.6–D.7), `jacobianScheme` (§D.8). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43607 (PicardFunctor/Scheme.lean: §D.2 `HasPicardScheme` and the Picard scheme as the representing object).
- Ready now: yes for §D.2 (needs only D.1, in code, and Mathlib representability API). No for §§D.3–D.8: §D.3 needs C.2 and SchemeAndStackFoundations §§1.1, 4.14 (not started); §D.4 needs C.1–C.3, D.3 and SSF §§0.9, 4.9, 4.14.
- Serves defs: 19, 30, 71, 80, 84, 85
- Evidence: README l.834 "## Layer D: the relative Picard functor and the Jacobian scheme"; l.862 "### D.2 The Picard scheme as a named representing object" (*Needs:* D.1); l.903 "### D.3 Hilbert quotients for Picard charts" (*Needs:* C.2; SchemeAndStackFoundations §1.1, §4.14); l.922 "### D.4 Projective Picard representability"; l.974 "### D.5 The degree-zero piece and the Abel maps of the curve"; l.1064 "### D.8 The Jacobian over any field" (`jacobianScheme X := (picZeroSets X).reprX`); Dependencies l.1144. STATUS Layer D remaining "named Picard scheme, Hilbert quotients, representability, smoothness and properness of Pic0, the Jacobian over any field". `HasPicardScheme`, `picardScheme`, `jacobianScheme` absent from Tau Ceti.

### Layer E §§E.1–E.5 cube and square, projectivity, dual, polarizations and theta W_{g−1}
- Status: PARTIAL: the `AbelianVariety` carrier, rigidity (`existsUnique_snd_comp_eq_of_flat`, Rigidity/Relative.lean; pointed morphisms of proper flat group schemes are homomorphisms, Rigidity/GroupScheme.lean), the tangent space, dimension zero, elliptic curves. No theorem of the cube or square, projectivity, dual abelian variety, polarization, `W_{g−1}` or theta (grep `cube|thetaDivisor` in AlgebraicGeometry empty).
- Ready now: no. §E.1 (cube over a field) needs C.2 (remaining); §E.3 (dual) needs D.4; §E.5 (theta) needs D.5, D.8, E.1, E.3, E.4.
- Serves defs: 30, 80
- Evidence: README l.1148 "## Layer E: abelian varieties"; l.1150 "### E.1 Cube and square" (*Needs:* A.1, C.2); l.1183 "### E.2 Abelian varieties and projectivity"; l.1203 "### E.3 The higher-dimensional Picard functor and dual" (*Needs:* D.1, D.4, E.1, E.2); l.1240 "### E.5 Polarizations and theta" ("construct the Cartier divisor `W_{g−1} ⊂ Pic^{g−1}` of effective classes", *Needs:* D.5, D.8, E.1, E.3, E.4). STATUS Layer E: "It lacks every milestone: cube, projectivity, dual, polarizations, autoduality, and `[n]` for `n ≠ 0`."

### Layer F §F.1 Abel–Jacobi and the Albanese property
- Status: PARTIAL: Abel–Jacobi on functors of points (PicardFunctor/Abel/{Jacobi,Fppf,PicZero,Degree}.lean, `abelJacobiMapToPicZeroFppf`), point separation, the `AbelianVariety.IsAlbanese` carrier (AbelianVariety/Albanese.lean). No `abelJacobi` morphism of schemes, `isAlbanese_abelJacobi`, closed immersion or base change.
- Ready now: no: needs D.5, D.8, E.4, E.6
- Serves defs: 30, 84 (Prop. 84.2 through PR #1739 §0.2; §F.2 `isClosedImmersion_abelJacobi` also needs D.6, B.2, B.4)
- Evidence: README l.1329 "## Layer F: Abel–Jacobi and the universal property"; l.1331 "### F.1 Abel–Jacobi and the Albanese property" (*Needs:* D.5, D.8, E.4, E.6); STATUS Layer F "lacks the morphism, the universal property, the closed immersion and base change".

## TauCetiRoadmap/AbelianSchemesAndArithmeticModuli
No STATUS.md (merged; Tau Ceti checked at 91942aa9f, 2026-11-19). No `AbelianScheme`, `AbelianLattice`, `AbelianNS` in Tau Ceti; only the field carrier `TauCeti.AlgebraicGeometry.AbelianVariety` with `TangentSpace`.

### §A0.1 `AbelianScheme S`, §A1.3 invariant differentials, §A2.2 dual, §A4.3 `H¹_dR`
- Status: NOT-STARTED. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/42982 (§A0.1 `AbelianScheme S` with base change, products, the field equivalence and relative dimension, AlgebraicGeometry/AbelianScheme/).
- Ready now: yes for §A0.1 (needs only Mathlib `GrpObj`, `IsProper`, `Smooth`, `GeometricallyConnected`, `Over.pullback` and Tau Ceti `AbelianVariety`). §A1.3 needs A0.3 and SchemeAndStackFoundations §3.8; §A2.2 needs A2.1 (Raynaud) and JacobianChallenge Layer E; §A4.3 needs A1.3, A2.2, A4.2.
- Serves defs: 70, 74, 78, 85; 87 (§A2.2, through SelmerIwasawaCohomology §2.12a)
- Evidence: README l.600 "### A0.1 Abelian schemes" (*Needs* l.658), l.789 "### A1.3 Invariant differentials", l.1093 "### A2.2 The dual abelian scheme and the Poincaré bundle", l.1916 "### A4.3 First de Rham cohomology".

### §A1.5 relative cube and multiplication pullbacks; §A2.10 Néron–Severi group
- Status: NOT-STARTED (no cube theorem or `AbelianNS` in Tau Ceti).
- Ready now: no: §A1.5 needs A0.3, A1.2, A1.4 and JacobianChallenge §E.1; §A2.10 needs A2.3, AlgebraicModuliForArithmeticGeometry Layer 7 and JacobianChallenge Layer E.
- Serves defs: 80 (§A1.5: `[n]^*L` for symmetric and antisymmetric `L`), 78 (§A2.10, for the paper)
- Evidence: README l.898 "### A1.5 The theorem of the cube and multiplication pullbacks"; l.1343 "### A2.10 The Néron–Severi group".

### §§A3.3, A6.3, A6.5 Quotients by finite locally free subgroups, images of homomorphisms, Poincaré complete reducibility
- Status: NOT-STARTED.
- Ready now: no: §A3.3 needs A2.1, A3.1 and SchemeAndStackFoundations §§1.5–1.6 (quotient sheaves, §1.5 partial) and §1.17; §A6.3 needs A3.1 and JacobianChallenge Layer E; §A6.5 needs A2.3, A2.5, A2.8, A3.4, A6.3, A6.4.
- Serves defs: 71 (abelian subvarieties, images and quotients `B/C`); 87 (§A3.3, isogeny quotients, through SelmerIwasawaCohomology §2.12a)
- Evidence: README l.1481 "### A3.3 Quotients by finite locally free subgroups" (*Needs* "A2.1, A3.1; ModularCurves 0E; SchemeAndStackFoundations Layer 1 §§1.5–1.6 (quotient sheaves), §1.17"), l.2868 "### A6.3 Images of homomorphisms over the original field", l.2921 "### A6.5 Poincaré complete reducibility".

### §§A5.1–A5.7 Lattice uniformization, Riemann forms, the polarized Hodge equivalence, analytic families, degree-one realizations
- Status: NOT-STARTED. Tau Ceti inputs in code: `lieExp`, `isLocalDiffeomorphAt_lieExp_zero`, `IsRiemannForm`, `latticeHodgeStructure`, `latticeHodgeStructureEquiv`, `isRiemannForm_iff_isPolarization`, `HodgeStructureOn.dual`, ComplexTori Milestone 1's orbit quotient and homology. No `AbelianLattice`, `RiemannForm.hodgeDual` or `polarizedHodgeEquivalence`.
- Ready now: no: §A5.1 needs ComplexComparisonPartII §§C-1.1, C4.4 (not started) and A4.1 (the integral Tate module); §A5.3 needs Chow's theorem and proper GAGA (ComplexComparisonPartII §§C1.9, C4.2). §A5.2's purely lattice-theoretic API (`RiemannForm.hermitian`, `scale`, `homological`, `hodgeDual` on an abstract lattice with complex structure) uses only Tau Ceti and Mathlib and could start now; its application to `A` needs §A5.1.
- Serves defs: 12 (target: §§A5.1–A5.5), 13, 23 (through 12), 74 (§§A5.1, A5.6–A5.7), 85 (§A5.1), 89 (Layer A5)
- Evidence: README l.2518 "## Layer A5: Complex uniformization and families", l.2527 "### A5.1 Lattice uniformization" (*Needs:* A4.1; ComplexTori; ComplexComparisonPartII C−1.1, C4.4), l.2574 "### A5.2 Riemann forms" (*Needs* l.2606), l.2678 "### A5.5 The polarized Hodge equivalence" (*Needs* l.2695), l.2698 "### A5.6 Analytic families and the algebraic comparison", l.2736 "### A5.7 Degree-one realization conventions".

### §§A6.11, A6.21 The characteristic polynomial on the Tate module; Frobenius semisimplicity
- Status: NOT-STARTED.
- Ready now: no: §A6.11 needs A4.1 (the Tate module) and A6.10; §A6.21 needs A6.8, A6.11, A6.14.
- Serves defs: 89
- Evidence: README l.3042 "### A6.11 The characteristic polynomial on the Tate module", l.3360 "### A6.21 Frobenius semisimplicity".

### §A6.38 The Hodge line bundle
- Status: NOT-STARTED.
- Ready now: no: needs A1.3, A5.8 and AlgebraicVectorBundles L0C (determinants).
- Serves defs: 85
- Evidence: README l.3867 "### A6.38 The Hodge line bundle" (`λ_H = det ω_A`, `ω_A = e^*Ω¹_{A/S}`).

## TauCetiRoadmap/ComplexComparisonPartII
No STATUS.md (merged as roadmap PR #848; Tau Ceti checked at 91942aa9f, 2026-11-19). Tau Ceti has the holomorphic structure sheaf `TauCeti.holomorphicSheaf` (Analysis/Complex/HolomorphicSheaf.lean) and the holomorphic structure sheaf of complex manifolds (Geometry/Manifold/Complex/StructureSheaf/); no `ComplexAnalyticSpace` or `complexSchemeAnalytification`.

### §C-1.1 Analytic local models and scheme analytification `complexSchemeAnalytification`
- Status: NOT-STARTED.
- Ready now: no: the local models need ComplexKahlerGeometry K3–K4 and RealAnalyticGeometry R3.2 item 0; the scheme analytification also cites ReductiveGroups §§3A.5c–3A.5e (smooth complex charts, not started).
- Serves defs: 12, 15, 13, 23, 74, 85 (the last four through AbelianSchemesAndArithmeticModuli §A5.1)
- Evidence: README l.1003 "### C-1.1 Analytic local models and scheme analytification", l.1053 "Define `complexSchemeAnalytification` ..."; *Needs* lines cite "ComplexKahlerGeometry K3–K4", "RealAnalyticGeometry R3.2 item 0", "ReductiveGroups §3A.5c–3A.5e".

### §C-1.2, §C1.9, §§C4.1–C4.4 Analytic quotients and completed stalks, proper GAGA, Remmert, Chow, maps out of proper schemes
- Status: NOT-STARTED.
- Ready now: no: §C-1.2 needs §C-1.1, AlgebraicModuliForArithmeticGeometry Layer 3 and SchemeAndStackFoundations Layer 1; §C1.9 needs C0, C1.5, C1.7 (`CoherentAnalytification`, `cartanTheoremB`, `projectiveLerayCover`); §C4.1 needs §C-1.1; §C4.4 needs §C1.9.
- Serves defs: 15 (target for analytification of quasi-projective varieties and GAGA), 12, 13, 23, 74, 85, 89 (through AbelianSchemesAndArithmeticModuli §§A5.1, A5.3)
- Evidence: README l.1103 "### C-1.2 Complex analytic quotients and completed stalks", l.1976 "### C1.9 Projective and proper coherent GAGA", l.2678 "### C4.1 Remmert's theorems", l.2700 "### C4.2 Chow's theorem with nilpotents", l.2741 "### C4.4 Holomorphic maps out of proper schemes".

### §C5.1 The ordinary comparison
- Status: NOT-STARTED.
- Ready now: no: needs DerivedDeRhamCohomology Layer 2 §§2.1–2.19 (`DeRham.complex`, not in Tau Ceti) and AlgebraicVectorBundles L0C exterior powers.
- Serves defs: 74 (Betti duality in open PR #1543 §5.1 builds on it)
- Evidence: README l.2993 "### C5.1 The ordinary comparison".

### §C6.6 Integral and rational Artin comparison
- Status: NOT-STARTED.
- Ready now: no: needs §§C6.0–C6.5 and EtaleCohomologyFoundations §F.4 (`normalizedAdicSystems`, `classicalAdicRealization`, `rationalAdicRealization`; not started).
- Serves defs: 89
- Evidence: README l.5145 "### C6.6 Integral and rational Artin comparison".

## TauCetiRoadmap/CyclotomicClassGroupsAndStickelberger
No STATUS.md (merged; Tau Ceti checked at 91942aa9f, 2026-11-19).

### §4.3 Abelian subvariety quotient B/C and the Albanese modular quotient A_f
- Status: NOT-STARTED (Tau Ceti has `AbelianVariety`, `AbelianVariety.MorphismGroup`, isogenies and newform coefficient fields; no quotient of an abelian variety, no Jacobian of `X₁(N)`).
- Ready now: no: `B/C` needs JacobianChallenge Layer E (ample bundles, duality, polarization) and ModularCurves 0C; `A_f` needs JacobianChallenge Layers D–F (the Jacobian) and ModularCurves Layers 4–10 (`X₁(N)` and Hecke correspondences).
- Serves defs: 71 (its `J₁(N)` variant, imported as ModularCurvesPartII §16.2; the `J₀(N)` form is ModularCurvesPartII §16.5)
- Evidence: README l.754 "### 4.3 Shared abelian arithmetic and the modular residual extension"; l.778 "The shared modular construction is the Albanese quotient A_f ..."; l.780 "Construct the abelian subvariety quotient B/C for any abelian subvariety C of an abelian variety B over a field k".

## TauCetiRoadmap/ReductiveGroups
STATUS.md snapshot: 23dce4e 2026-11-16, generated against Tau Ceti aa6e43e (Tau Ceti checked at 91942aa9f, 2026-11-19; README at roadmap 890b66d)

### Layer 5 (solvable groups) Structure of smooth connected solvable groups, G = G_u ⋊ T
- Status: PARTIAL. Exists: `torus_coinvariants_unipotentRadical` (G/G_u is a torus), and the triviality of homomorphisms from diagonalizable groups to unipotent groups, scheme-theoretically, so a diagonalizable closed subgroup of a unipotent group is trivial (`TauCeti.geometricallyUnipotentPointsCommHopfAlgProperty.bialgHom_eq_unit_comp_counit_of_groupLikeSetSpan_eq_top`, Algebra/AlgebraicGroup/Unipotent/Diagonalizable.lean, on `Module.Basis.map_coefficientMatrix_eq_one_of_isUpperTriangular_of_groupLikeSetSpan_eq_top`, Algebra/AlgebraicGroup/Representation/UpperUnitriangular.lean). Missing: the consequence that a maximal torus T meets G_u trivially and maps isomorphically onto G/G_u, the decomposition G = G_u ⋊ T, and conjugacy of subgroups of multiplicative type into T by G_u(k̄) (Milne, Theorem 16.33(b),(d)). STATUS lists Layer 5 as done. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43516 (a diagonalizable closed subgroup or torus meets `R_u(G)` trivially and maps with trivial kernel to `G ⧸ R_u(G)`, Algebra/AlgebraicGroup/Unipotent/Radical/Diagonalizable/; not the decomposition `G = G_u ⋊ T`).
- Ready now: yes. It is the input that Layer 7 torus conjugacy, and through it the root datum, wait on.
- Serves defs: 1, 4, 11, 23, 79
- Evidence: README l.2268 "## Layer 5: solvable and unipotent groups; the unipotent radical", l.2293 "**Solvable groups.**" bullet ("Prove, over `k̄`, the decomposition `G = G_u ⋊ T` ... (Milne, Theorem 16.33(d), p. 336)"; *Needs:* the unipotent theory, the pinned Lie–Kolchin theorem and torus quotient, Layer 4's tori, Layer 3's quotients); grep finds no `G_u ⋊ T` decomposition in Algebra/AlgebraicGroup/Solvable/ (SemidirectProduct.lean only proves solvability of semidirect products); Layer 7 torus conjugacy goes through Borel containment (Borel/Conjugacy/Containment.lean) and then conjugacy of maximal tori inside the solvable Borel.

### Layer 7 Root datum, relative root system, parabolics P_G(λ) and Levi decompositions
- Status: PARTIAL. Exists: the parabolic predicates `IsParabolic`/`IsParabolicOverAlgClosed` (Algebra/AlgebraicGroup/Parabolic/Basic.lean); dynamic `parabolicDefiningHopfIdeal`/`leviDefiningHopfIdeal` with `parabolicLeviFppfQuotientIso` (Algebra/AlgebraicGroup/Dynamic/…); GL_n weight parabolics proved parabolic (Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Borel.lean); torus conjugacy under extra hypotheses (Torus/Conjugation.lean); maximal-torus descent along any field extension `HopfIdeal.isMaximalTorus_of_baseChange` (Torus/Maximal.lean) on the base change of tori `torusCommHopfAlgProperty.baseChange` (Torus/BaseChange.lean). Missing: `StructureAcceptance.exists_conjugate_eq_of_isMaximalTorus` (unconditional), `exists_levi_complement_of_isParabolic`, `exists_titsSystem_of_isBorel`, P_G(λ) parabolic for general reductive G, the root datum of (G,T), and the relative root system.
- Ready now: no. Unconditional torus conjugacy needs the structure of smooth connected solvable groups, G = G_u ⋊ T with subgroups of multiplicative type conjugate into T by G_u(k̄) (Milne, Theorem 16.33(b),(d)). The README assigns this to Layer 5's "Solvable groups" bullet, which STATUS lists as done, but Tau Ceti has only `torus_coinvariants_unipotentRadical` (G/G_u is a torus) and the triviality of diagonalizable subgroups of unipotent groups (Unipotent/Diagonalizable.lean); Borel containment (Borel/Conjugacy/Containment.lean) is in place. The split root datum needs torus conjugacy, then the rank-one subgroups G_α with their coroots (Milne 21.11) and generation of N/T by reflections (Milne 21.37). The roots, pinnings and rational Weyl group exist (Tangent/RootSpace.lean, Pinning/Basic.lean, DiagonalizableGroup/Normalizer/WeylGroup.lean). The completeness of G/P needs the Layer 3 quotient representability (partial). Bruhat cells need Layer 7C (partial).
- Serves defs: 1, 4, 11, 23, 79
- Evidence: README l.2821 "## Layer 7: structure theory", l.2861 "**Parabolic subgroup schemes and Levi decompositions.**", l.2916 "**Root datum**", l.2929 "**relative root system** for non-split groups"; Torus/Conjugation.lean has `exists_conjugate_eq_of_isMaximalTorus` only with containment hypotheses (`hcontainI`); STATUS "remaining: unconditional torus conjugacy, root datum, centralizer equals torus, Bruhat and general parabolic Levi theory".

### Layer 7b Algebraic parabolics and Levi intersections (comparison with standard parabolics)
- Status: NOT-STARTED
- Ready now: no: needs Layer 7 Levi complements, Bruhat decomposition and the common-torus theorem, plus Layer 7a rational points (partial).
- Serves defs: 1, 4, 11, 23, 79
- Evidence: README l.3236 "## Layer 7b: algebraic parabolics and Levi intersections" (l.3275 double cosets "consuming Layer 7's Bruhat decomposition, common-torus theorem"; Dependencies l.3314 "Layers 7 and 7a"); STATUS Layer 7b "untouched"; grep `exists_levi_complement_of_isParabolic|exists_titsSystem_of_isBorel` empty.

### Layer 9D Isomorphism and existence theorems: split reductive groups ↔ root data
- Status: NOT-STARTED for the isomorphism and existence theorems. Related pieces exist: pinning transport across isomorphisms (Algebra/AlgebraicGroup/Pinning/Isomorphism.lean) and the Chevalley carriers, including Algebra/AlgebraicGroup/Chevalley/Orthogonal.lean.
- Ready now: no: needs the Layer 7 root datum, Layer 8 split data over general bases (partial) and the Layer 9 uniform pinned construction (partial).
- Serves defs: 11
- Evidence: README l.4976 "## Layer 9D: classification, relative groups and forms", l.4977 "The **isomorphism** and **existence theorems**: split reductive groups ↔ root data"; STATUS "remaining: isomorphism and existence theorems, relative center and derived group, forms, perfect-field pseudo-reductivity, nilradical filtration of the Weil example".

### 3A.5e The complex Lie group G(ℂ)
- Status: NOT-STARTED. Only the pinned inputs exist: point topology and topological group `TauCeti.PointTopology.isTopologicalGroup` (Topology/Algebra/PointTopology/Group.lean) and scheme point topology with charts (Topology/Algebra/PointTopology/Scheme/Charts.lean). No complex manifold or Lie-group structure on G(ℂ). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/38438 (Topology/Algebra/PointTopology/Scheme/Reduction.lean: reduction induces a homeomorphism on complex points, the 3A.5c item this one needs).
- Ready now: no: needs 3A.5b-3A.5d (open-chart embeddings, scheme-level fibre product, smooth complex charts). STATUS lists these as the 3A remainder ("complex-point comparison").
- Serves defs: 68
- Evidence: README l.1914 "**3A.5e The complex Lie group `G(ℂ)`.**" ("By 3A.5c–3A.5d, `G(ℂ)` is a Hausdorff, second-countable complex manifold"); STATUS 3A "remaining: complex-point comparison, restriction to O(1) sections and remaining worked tests"; supplier contract l.1058 "The library does not state that an affine open chart is an open embedding…".

## TauCetiRoadmap/RiemannianGeometry
STATUS.md snapshot: d9fbe7b 2026-11-11 (Tau Ceti checked at 91942aa9f, 2026-11-19)

### R5a Immersion geometry: pullback connection, normal bundle, B, S, ∇⊥
- Status: PARTIAL: the orthogonal normal bundle of an immersion into a manifold with a Riemannian metric, `ν_f` as a smooth subbundle of `f *ᵖ TN` indexed by the source point (`TauCeti.orthogonalNormalSpace`, `orthogonalNormalFiberBundle`, `orthogonalNormalVectorBundle`, `orthogonalNormalContMDiffVectorBundle`), with the smooth orthogonal projection `contMDiff_starProjection_orthogonalNormalSpace` and the formula `starProjection_orthogonalNormalSpace_eq_sub_mfderiv_inverse` (`v ↦ v − df((df*df)⁻¹ df* v)`) (Geometry/Manifold/Riemannian/Immersion/NormalBundle.lean, Tau Ceti PR #37236); covariant differentiation of fields along a map `CovariantDerivative.alongMap`, agreeing with `alongCurveWithin` on curves (`alongMap_curveVelocityWithin`) and with the ambient derivative on pulled-back fields (`alongMap_pullback`) (Geometry/Manifold/VectorBundle/CovariantDerivative/AlongMap/Basic.lean, #38120); the flat-ambient `TauCeti.secondFundamentalForm`, `shapeOperator`, `manifoldSecondFundamentalForm`, `manifoldShapeOperator` (Analysis/InnerProductSpace/{SecondFundamentalForm,ShapeOperator}.lean, Geometry/Manifold/Immersion/{SecondFundamentalForm,ShapeOperator}.lean), the tangent and normal projections (Riemannian/Immersion/Projection.lean), the Gauss formula along curves (CovariantDerivative/AlongCurve/Immersion.lean), embedding normal spaces (Geometry/Manifold/SmoothEmbedding/NormalSpace/) and the pullback metric (Riemannian/Pullback/Basic.lean). Missing: the comparison `ν_f ≅ f*TN/df(TM)`, the pullback ambient connection as a connection on `f *ᵖ TN`, the intrinsic B, S and ∇⊥ for a Riemannian ambient, and Gauss/Codazzi/Ricci. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/43723 (the quotient normal bundle `f*TN/df(TM)` of an immersion, Geometry/Manifold/Immersion/NormalSpace/) and https://github.com/TauCetiProject/TauCeti/pull/43720 (its identification with the orthogonal normal bundle, Riemannian/Immersion/NormalBundle.lean)
- Ready now: yes for the quotient comparison (`ν_f` and its projection are in code). B/S/∇⊥: the README lists "SmoothBundlesConnections B2–B4" (B3–B4 not started); the dependency looks soft, since R5a uses Tau Ceti's vector-bundle `CovariantDerivative`, `alongMap` gives the ambient derivative along `f`, and `ν_f` with its projection is in code
- Serves defs: 31, 49, 52, 65, 66
- Evidence: README l.3205 "### R5a. Immersion geometry and first variation" (l.3210 "construct the smooth bundle equivalence from ν_f={ (p,w) : w⊥range(df_p) } to f*TN/df(TM)"); *Needs* l.3231 "SmoothBundlesConnections B2.1 (smooth pullback and Hom bundles); GeometricTopology Layer 1 (embedding normal bundle)" and l.3300 "R1 curvature and tensor connections; R5a smooth normal comparison; SmoothBundlesConnections B2–B4"; grep `meanCurvature|principalCurvature` in Tau Ceti: no hits (the `normalConnection` in Analysis/PDE/SeibergWitten/FlatLimit.lean is a flat-model frame, unrelated)

### R5a.1 Orientation-free C² relative volume
- Status: PARTIAL: the relative density of two Riemannian metrics `Bundle.ContMDiffRiemannianMetric.relativeVolumeDensity` (Geometry/Manifold/Riemannian/VolumeDensity/Relative.lean): positive, `C^n`, basis/chart independent, `relativeVolumeDensity_self`; `dV_{g'} = J dV_g` (`riemannianVolume_eq_map_withDensity_relativeVolumeDensity`, `integral_riemannianVolume_eq_integral_relativeVolumeDensity_smul`), no orientation; pullback along local diffeomorphisms and restriction to open sets and time intervals (VolumeDensity/Restriction.lean); also `hasDerivAt_chartVolumeDensity`, `eventually_forall_injective_mfderiv_of_isCompact`. Missing: joint parameter dependence of `J_t` for a family `F_t`, and the C² functional `V(t) = ∫(J_t − 1) dvol_(g_0)` with its two derivatives. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43602 (the compact-source part of R5a.1: `Bundle.ContMDiffRiemannianMetric.relativeVolume` and its C² dependence along families of metrics and immersions, VolumeDensity/RelativeVolume.lean, ContMDiff/ParametricIntegralDeriv.lean).
- Ready now: yes (induced metric `ContMDiffRiemannianMetric.pullback`, `riemannianVolume` and the relative density exist; what remains is differentiation under the integral).
- Serves defs: 52
- Evidence: README l.3304 "#### R5a.1. Orientation-free C² relative volume" ("Define the positive relative density J_t ... and prove `dvol_(g_t)=J_t dvol_(g_0)`"); *Needs* l.3358.

### R5a.2 Principal curvatures, H, minimality, first variation, minimal cones
- Status: NOT-STARTED (only the flat-ambient B/S above)
- Ready now: no: needs R5a's B/S pairing; the first-variation part also needs R5a.1 and DG Layer 12 integration/divergence
- Serves defs: 49, 52, 65, 66
- Evidence: README l.3362 "#### R5a.2. First variation and immersion examples", l.3364 "Define principal curvatures as the eigenvalues of S_ν ... H=(tr B)/m ... minimality is H=0"; l.3399 "minimal cone equivalence away from the cone vertex"; *Needs* l.3387

### R5b Second variation, Jacobi operator, stability, Dirichlet index
- Status: PARTIAL, operator-theoretic part only: the Dirichlet operator of a form coercive after a shift along `J`, `IsCoercive.formOperator` (graph `{(J u, f) : Q(u, v) = ⟪f, J v⟫}`, `mem_graph_formOperator_iff`), self-adjoint (`isSelfAdjoint_formOperator`), bounded below by `−c` (`neg_mul_norm_sq_le_inner_formOperator`), with `(L_D + c)⁻¹ = S` (`resolvent_formOperator_neg`), compact resolvent (`hasCompactResolvent_formOperator`), independent of the shift (`formOperator_eq`) and with a Hilbert basis of eigenvectors (`exists_hilbertBasis_formOperator`) (Analysis/InnerProductSpace/Variational/FormOperator.lean, Tau Ceti PR #42856), on `IsCoercive.formSolutionOperator`, `IsCoercive.isLeast_rayleighQuotient` and the min–max principle `TauCeti.isLeast_minMax_of_hilbertBasis` (Variational/MinMax.lean). Missing: the index statement for negative-definite subspaces, the domain/regularity comparison, and all of the geometry: the second variation formula, the Jacobi operator on `ν_f`, stability.
- Ready now: no for the geometry: needs R5a, R5a.1, R5a.2. The abstract index statement needs only the code above.
- Serves defs: 52, 65
- Evidence: README l.3581 "### R5b. General normal second variation and hypersurface stability", l.3583 "consumes R5a's immersion geometry, R5a.1's ... relative-volume lemma and R5a.2's first variation"; l.3639 "Define the Dirichlet operator L_D of L, the Dirichlet Jacobi operator", l.3655 "Prove the index statement"

### R5c Schrödinger operators on compact manifolds: closed case, index on smooth sections, principal eigenfunction
- Status: NOT-STARTED: `TauCeti.Manifold.laplaceBeltrami`, `laplaceBeltrami_eq_sum_hessian` and `IsCoercive.formSolutionOperator` exist; no bundle Schrödinger operator `∇*∇ + K`, closed-manifold realization, min–max or principal eigenfunction
- Ready now: no: needs R5b's Dirichlet realization, ComplexKahlerGeometry K5a (closed case), PDE A4, A6 and E20, PseudodifferentialOperators P1.0's connection Laplacian, SBC B2–B4
- Serves defs: 52, 66 (through RiemannianManifoldsWithConvexBoundary §3.5), 38 (through ComplexHessianEquations §5.3 and Layer 6, for the paper's theorem)
- Evidence: README l.3715 "### R5c. Schrödinger operators on compact manifolds: spectrum, principal eigenfunction and Dirichlet problem"; *Needs* l.3807; roadmap PR #2222; MinimalSurfaces MS6.1 *Needs* "R5c (the closed case, the index on smooth sections and the smoothness of eigensections)"

### R7.9 Separating and two-sided hypersurfaces
- Status: NOT-STARTED: the inputs it names exist (`TauCeti.SmoothEmbedding.NormalSpace`, `normalExp` and the Riemannian tubular neighbourhood, `TauCeti.IsBicollar`, `TauCeti.periodHom`, regular sublevels, `TauCeti.VectorBundleOrientationCover`); no unit normal double cover `S(ν_f)`, two-sidedness predicate or separation theorem
- Ready now: no: needs DifferentialGeometry 12.5's outward unit normal (not in code). Its other input, R5a's normal bundle, is in code (`TauCeti.orthogonalNormalContMDiffVectorBundle`, Geometry/Manifold/Riemannian/Immersion/NormalBundle.lean)
- Serves defs: 52, 66 (through RiemannianManifoldsWithConvexBoundary §§3.1, 4.3) (one-sided index through the normal double cover, MinimalSurfaces MS6.3)
- Evidence: README l.4469 "### R7.9. Separating and two-sided hypersurfaces", "Call f *two-sided* when it has a unit normal field ν ... The unit vectors of `ν_f` form the *unit normal double cover*"; *Needs* l.4745; roadmap PR #2223

### R1.3 Normal homogeneous metrics on G/H
- Status: NOT-STARTED: Riemannian submersions have splitting, connection and O'Neill tensors with their symmetries, their transport under local isometries, and the integrability criterion for the horizontal distribution (Geometry/Manifold/Riemannian/Submersion/{Basic,Connection,Integrability}.lean, Submersion/ONeill/{Basic,Isometry}.lean); O'Neill's horizontal curvature formula `inner_curvatureTensor_of_mem_orthogonal_ker` with `sectionalCurvature_mfderiv` (Submersion/Curvature.lean); no homogeneous quotient metric. STATUS coverage Layer 1 remaining "... and the O'Neill curvature formulas" (STATUS predates Submersion/Curvature.lean)
- Ready now: no: needs SBC B1.4's smooth G/H (partial: the free proper quotient theorem and Cartan's closed-subgroup theorem are in code, G/H for a closed subgroup H is not assembled)
- Serves defs: 62, 15, 31 (through RealSemisimpleLieGroups §§5.3, 5.7)
- Evidence: README l.1205 "### 1.3 Metric changes, Lie groups and submersions", l.1310 "homogeneous metric on SBC B1.4's G/H with horizontal space h^perp and prove G→G/H is a Riemannian submersion"

### R4 item 4 Cartan–Hadamard
- Status: NOT-STARTED: both inputs are in code: the supplier `norm_le_norm_mfderiv_riemannianExp_of_sectionalCurvature_nonpos` (Geometry/Manifold/Riemannian/Jacobi/Comparison.lean) and R4 item 3's covering criterion, a local Riemannian isometry from a geodesically complete manifold is a covering map (`TauCeti.IsLocalRiemannianIsometry.isCoveringMap`, `surjective`), in the form the README names for Cartan–Hadamard, a local diffeomorphism from a complete manifold that does not decrease lengths is a covering map (`TauCeti.Manifold.isCoveringMap_of_norm_le_norm_mfderiv`, `surjective_of_norm_le_norm_mfderiv`) (Geometry/Manifold/Riemannian/Covering/Criterion.lean). No `cartanHadamard_isCoveringMap`
- Ready now: yes: R4 item 3 and HopfRinow L4 are in code
- Serves defs: 62, 15, 31 (through RealSemisimpleLieGroups §§5.3, 5.7)
- Evidence: README l.2565 "4. Cartan–Hadamard (`cartanHadamard_isCoveringMap`)", l.2569–2571 ("exp_p is a local diffeomorphism from the complete flat T_pM satisfying the hypothesis of the preceding covering criterion"), *Needs* l.2577 "R4.3 (covering criterion), HopfRinow (Completed) Layer 4"; STATUS "R4 has its models, the nonpositive-curvature exponential bound ... but no comparison theorem"

### R6 Euclidean ε-tube inversion and nearest-point retraction
- Status: NOT-STARTED: the Euclidean normal tube of a `C²` embedding of a compact manifold `TauCeti.exists_isTubularNeighborhood_normalBundle` (`TubularNeighborhood/Euclidean.lean`) and the squared-distance Hessian declarations R6 consumes are in code; no nearest-point retraction on main. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43523 (TubularNeighborhood/NearestPoint.lean) adds `TauCeti.nearestPointRetraction`, `image_normalTube_eq_thickening`, the inversion below the injectivity radius and a uniform radius for compact `C²` embedded submanifolds.
- Ready now: yes after #43523 for the `C¹`/smooth regularity of the retraction; the rest of R6 needs R5a.
- Serves defs: 37, 48 (through YangMillsConnectionsAndCaloricGauge §1.2)
- Evidence: README l.4081 "### R6. Focal geometry and squared-distance Morse functions", l.4199–4203 "R6 owns the ε-tube inversion for closed-image Euclidean embeddings ... a nearest-point retraction".

## TauCetiRoadmap/RiemannianGeometry/MinimalSurfaces
No STATUS.md; sub-roadmap from roadmap PR #2226 (Tau Ceti checked at 91942aa9f, 2026-11-19)

### MS6.1–MS6.3 Morse index and nullity of minimal submanifolds (compact, by exhaustion, hypersurfaces)
- Status: NOT-STARTED (grep for a Morse index of minimal immersions, Jacobi operator or nullity: no hits; the only index form is along curves, Geometry/Manifold/Riemannian/IndexForm/Basic.lean)
- Ready now: no: needs R5b (index form, Dirichlet realization of `−J^⊥`) and R5c (closed case, index on smooth sections); MS6.3's one-sided case needs R7.9's normal double cover
- Serves defs: 52
- Evidence: README l.1181 "### 6.1 Morse index on compact minimal submanifolds and negative eigenvalues of `−J^⊥`" ("the nullity `null(Σ) = dim ker(−J^⊥)`"), l.1217 "### 6.2 Morse index of minimal submanifolds in `ℝ^m` via exhaustions" ("independent of the choice of smooth exhaustion and equals the supremum of `dim E` over finite-dimensional subspaces `E ⊂ C^∞_c(Σ ∖ ∂Σ;ν_f)`"), l.1255 "### 6.3 Specialization to hypersurfaces and two-sided hypersurfaces"; *Needs* l.1214, l.1253, l.1296

## TauCetiRoadmap/EtaleCohomologyFoundations
STATUS.md snapshot: 53f4df3 2026-11-16, generated against Tau Ceti aa6e43e (Tau Ceti checked at 91942aa9f, 2026-11-19; README at roadmap 890b66d)

### §F.0.2 Finite étale Galois categories, `EtaleFundamentalGroup` and the étale fundamental groupoid
- Status: PARTIAL, and enough for def 84's use of π₁. In code: `PreGaloisCategory (FiniteEtaleScheme S)` for every S (AlgebraicGeometry/FiniteEtale/Quotient.lean); `FiberFunctor (fiber x)` and `GaloisCategory (FiniteEtaleScheme S)` for connected S, with any two geometric points joined by a path (FiniteEtale/Galois/Category.lean); `Aut (FiniteEtaleScheme.fiber x)` with functoriality `mapAutFiber`/`mapFiberIso` and change of basepoint `mapAutFiber_conjAut` (Galois/Functoriality.lean); paths on disconnected bases (Galois/Component.lean); `galContinuousMulEquivAutFiber : Gal(Ω/K) ≃ₜ* π₁(Spec K,x)` (Galois/FundamentalGroup.lean). Missing: the named `EtaleFundamentalGroup`, `EtalePath`, `EtaleFundamentalGroup.map` and `EtaleFundamentalGroup.small`; lisse monodromy; tensor/dual transport. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/37826 (`TauCeti.FiniteEtaleScheme.EtaleFundamentalGroup` and `EtalePath`, with paths a torsor, FiniteEtale/Fiber.lean), https://github.com/TauCetiProject/TauCeti/pull/37847 (the Galois action on stalks `AlgebraicGeometry.Scheme.galoisStalk`, Sites/Etale/GaloisStalk.lean) and https://github.com/TauCetiProject/TauCeti/pull/43299 (small étale restriction and effective étale descent for representability by finite étale schemes, toward lisse monodromy, FiniteEtale/RestrictSheaf.lean). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43620 (FiniteEtale/Galois/Functoriality.lean: `EtaleFundamentalGroup.map` for spectra of fields as Galois restriction).
- Ready now: yes: the named `EtaleFundamentalGroup` package needs only what is in code; lisse monodromy can use `CategoryTheory.Sheaf.IsFiniteLisse` and the fully faithful `TauCeti.FiniteEtaleScheme.toSheafFullyFaithful` (STATUS frontier).
- Serves defs: 84
- Evidence: README l.312 "## F.0.2 Finite étale Galois categories and the étale fundamental groupoid", l.380 (block "The canonical fundamental group", `EtaleFundamentalGroup`, EtalePath); STATUS "§F.0.2 is partial: the Galois category, paths, functoriality of `π₁` and the connected-component criterion are done, but lisse monodromy and tensor/dual transport are missing". `EtaleFundamentalGroup` absent from Tau Ceti.

### §F.0.1 Finite and constructible étale module sheaves (prerequisite of every cohomology item below)
- Status: PARTIAL. Geometric stalks with their module structure, `TauCeti.AlgebraicGeometry.Scheme.etaleStalk`, exactness `shortExact_map_etaleStalk`, joint conservativity `isIso_of_forall_isIso_etaleStalk`, stalkwise exactness criteria `exact_iff_forall_exact_map_etaleStalk`; finite lisse sheaves `CategoryTheory.Sheaf.IsFiniteLisse` with `isFiniteLisse_constantSheaf`, `IsFiniteLisse.finite_etaleStalk` (AlgebraicGeometry/Sites/Etale/ModuleSheaf.lean); coefficient-invertibility criteria (per STATUS); the tensor/coefficient structure: étale module sheaves form a symmetric monoidal category with monoidal geometric stalks (`TauCeti.AlgebraicGeometry.Scheme.monoidalCategorySheafModuleCat`, `symmetricCategorySheafModuleCat`, `monoidalEtaleStalk`, AlgebraicGeometry/Sites/Etale/Monoidal.lean, Tau Ceti PR #40921); the category `GeometricPoint S` with `toPointFunctor : GeometricPoint S ⥤ (Scheme.smallEtaleTopology S).Point` (Sites/Etale/GeometricPoint.lean); the localization of the small étale site at an étale `U`, `AlgebraicGeometry.Scheme.Etale.overEquivalence : Over U ≌ U.left.Etale` (Sites/Etale/Localization.lean, #39351). Missing: `VanishingCycles.constructibleEtale`: stratifications, constructibility, pullback and étale descent, extension by zero, closure under limits, colimits, extensions and tensor products, and the weak Serre class property. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/37149 (the constant étale sheaf as locally constant functions, `constantSheafIsoEtaleLocallyConstantSheaf`), https://github.com/TauCetiProject/TauCeti/pull/41266 and https://github.com/TauCetiProject/TauCeti/pull/41781 (overlapping: pullback of small étale sheaves, base change and étale descent of `IsFiniteLisse`, Sites/Etale/Pullback.lean) and https://github.com/TauCetiProject/TauCeti/pull/43084 (geometric point functoriality, Galois actions on stalks and the stalk Frobenius, Sites/Etale/GeometricPoint/); none defines constructible sheaves.
- Ready now: yes, mostly. The cited SchemeAndStackFoundations §1.1 (`sheaf_stack`) and §§2.1, 2.9 have only first definitions, so work may have to supply local substitutes.
- Serves defs: 18, 19, 69, 77, 84 (F.1, F.4.x and F.0.2's monodromy all need it)
- Evidence: README l.173 "## F.0.1 Finite and constructible étale module sheaves" (*Needs:* SchemeAndStackFoundations §1.1, §§2.1, 2.9); STATUS "§F.0.1 has stalks, finite lisse sheaves and coefficient-invertibility criteria, and nothing on constructibility"; frontier "Constructible étale sheaves ... Everything from §F.0.3 onward depends on this".

### §F.1 and §0.9 cup products: `finiteCoefficientCohomology` and classes as shifted morphisms
- Status: NOT-STARTED. Neither `constructibleDerivedCategory` nor `finiteCoefficientCohomology` exists, and no cup product on `Sheaf.H` or on étale cohomology exists in Tau Ceti or Mathlib (the cup files in Tau Ceti are for cochains, Hochschild cochains, Galois cohomology and Čech cochains of a presheaf of algebras, `TauCeti.CategoryTheory.cechCup` in CategoryTheory/Sites/SheafCohomology/Cech/Cup.lean, a cochain-level product with no passage to `Sheaf.H`).
- Ready now: no. §F.1 needs §§F.0.1–F.0.4, §0.7 (`supportLocalization`), EnhancedDerivedSheaves §§0.1–0.4 (`tensorHom`, `functorCoherence`) and SchemeAndStackFoundations §§2.1–2.2, 2.5, 2.7, 2.17. §0.9's `ShiftedHom` cup product needs §0.7 and Mathlib `ShiftedHom`; its plain (unsupported) form on `D(X,Λ)` could be built on Mathlib's `DerivedCategory` once a monoidal structure on `D(X,Λ)` is available.
- Serves defs: 18 (cup products), 69, 77 (étale cohomology with Z/ℓⁿ coefficients)
- Evidence: README l.827 "## F.1 Derived sheaves and coherent diagrams", l.874 "**Finite-coefficient cohomology and coherent actions.** ... Build cup products"; l.1838 "**Classes as shifted morphisms, cup products with supports and purity.** ... `Hⁿ(X,K) = ShiftedHom Λ_X K n` ... Define the cup product `Hᵃ(X,K) × Hᵇ(X,L) → Hᵃ⁺ᵇ(X,K⊗L)`" (*Needs:* §0.7); STATUS "§§F.0.3, F.0.4, F.0.A2, 0.5–0.11, F.1–F.3a ... are untouched".

### §F.2.1 Proper base change and §F.2.2 Smooth base change
- Status: NOT-STARTED. `VanishingCycles.properBaseChange` and `smoothBaseChange` are absent.
- Ready now: no. F.2.1 needs SchemeAndStackFoundations §§2.1–2.2 and EnhancedDerivedSheaves §§0.1–0.4. F.2.2 needs F.1 `finiteCoefficientCohomology` and SchemeAndStackFoundations §0.9.
- Serves defs: 69 (and 77 through the étale cohomology of modular curves)
- Evidence: README l.898 "## F.2.1 Proper base change for arbitrary torsion" (*Needs* l.907); l.916 "## F.2.2 Smooth base change in the rotated square" (*Needs* l.927); STATUS: F.2 untouched.

### §§F.4.1–F.4.2 Normalized adic systems and classical Z_ℓ realization
- Status: NOT-STARTED. `normalizedAdicSystems` and `classicalAdicRealization` are absent. Mathlib's pro-étale `Scheme.EllAdicCohomology` is the §F.4.3 comparison target, not this.
- Ready now: no. Needs §§F.0.1–F.0.4, F.1, F.2–F.3 and EnhancedDerivedSheaves §0.3 `inverseLimits`/`derivedCompletion`.
- Serves defs: 69 (Z_ℓ coefficients), 77
- Evidence: README l.1470 "## F.4.1 Normalized bounded constructible systems" (*Needs* l.1494: "§§F.0.1–F.0.4, F.1; EnhancedDerivedSheaves §0.3 inverseLimits and derivedCompletion"); l.1506 "## F.4.2 Classical realization and finite-level cohomology limits" (*Needs* l.1517); STATUS: F.4.1–F.4.6 untouched.

### §F.4.5 Rational realization and finite-dimensional cohomology (b₂)
- Status: NOT-STARTED. `VanishingCycles.rationalAdicRealization` is absent.
- Ready now: no. Its *Needs* line is "normalizedAdicSystems through adicFiniteness" (§§F.4.1–F.4.4, which need F.3 finiteness), §F.0.2, F.2 Künneth and §F.4.0 stable lattices (partial in code: `Subgroup.isCompact_closure_iff_exists_stable_lattice`, `TauCeti.GaloisLattice.IntegralModel.nonempty`). It is near the end of the ECF dependency chain.
- Serves defs: 19
- Evidence: README l.1665 "## F.4.5 Rational realization and finite-dimensional cohomology" (`RΓ_(c)(X,K_Qℓ)≅RΓ_(c)(X,K_Zℓ)⊗ᴸℚ_ℓ`, finite-dimensional `Hⁱ_(c)`, l.1690); *Needs* l.1696; STATUS: F.4.1–F.4.6 untouched.

### §F.0.A2 The arithmetic fundamental-group sequence and sections of rational points
- Status: NOT-STARTED. `arithmeticExactSequence` is absent. Its §F.0.A0 input is done for fields (`galContinuousMulEquivAutFiber`); §F.0.4 topological invariance (`universalHomeomorphismEtaleEquivalence`) is not started.
- Ready now: no: needs §F.0.4 (finite étale covers along the universal homeomorphism `X_{k̄} → X_{k^sep}`), descent of finite étale covers along limits from SchemeAndStackFoundations §0.9, and §F.0.2's named `EtaleFundamentalGroup.map`.
- Serves defs: 84
- Evidence: README l.613 "## F.0.A2 The arithmetic fundamental-group sequence" (`1 → π₁^ét(X_{k̄}) → π₁^ét(X) → π₁^ét(Spec k) → 1` for qcqs geometrically connected `X/k`; "A `k`-rational point `a` of `X` gives a continuous section `s_a`"; *Needs:* §F.0.A0, §F.0.2, §F.0.4, SchemeAndStackFoundations §0.9); STATUS lists §F.0.A2 among the untouched sections.

## TauCetiRoadmap/ArithmeticGaloisRepresentations
No STATUS.md (merged; Tau Ceti checked at 91942aa9f, 2026-11-19).

### Layer 1 (§§1.1, 1.6, 1.8–1.9) and Layer 5 Continuous representations, integral models, Brauer–Nesbitt, residual representations, recognition by Frobenius
- Status: PARTIAL: the carrier `TauCeti.ContinuousRep` with `Iso`, `ofCharacter`, `baseChange`, `toContRepresentation` (RepresentationTheory/Continuous/ContinuousRep.lean) and `GaloisLattice.IntegralModel` (Continuous/IntegralModel/Basic.lean), from EtaleCohomologyFoundations §F.4.0; for §1.6, integral models of subrepresentations and quotients `IntegralModel.submodel` with `submodelInclusion`, `quotientModel` with `quotientProjection`, and `range_submodelInclusion_eq_ker_quotientProjection` (Continuous/IntegralModel/Subquotient.lean, Tau Ceti PR #35600). Missing: `ContinuousRep.Hom`, `continuous_iff_matrixCoeff`, `ContinuousRep.charpoly` and the rest of Layer 1; all of Layer 5. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/42944 (§1.1 `ContinuousRep.Hom`, continuity criteria and `ContinuousRep.charpoly`, RepresentationTheory/Continuous/ContinuousRep/), https://github.com/TauCetiProject/TauCeti/pull/42907 (§1.1 orbit and matrix-entry criteria for joint continuity, RepresentationTheory/Continuous/JointContinuity.lean) and https://github.com/TauCetiProject/TauCeti/pull/43004 (§1.5 `ContinuousRep.baire_descent` and §1.6 `ContinuousRep.exists_integral_conj_GL`).
- Ready now: yes: §1.1 needs only Mathlib and the §F.4.0 carrier in code.
- Serves defs: 69
- Evidence: README l.767 "## Layer 1: continuous representations and integral models", l.779 "### 1.1 Continuous representations" (*Needs:* "EtaleCohomologyFoundations §F.4.0 (Tau Ceti `TauCeti.ContinuousRep`); Mathlib"), l.1124 "### 1.6 Lattices and integral models", l.1226 "### 1.8 Brauer–Nesbitt", l.3447 "## Layer 5: recognition by Frobenius polynomials".

### §1.11 Reductive quotients over fields and DVRs (`Conj_H = H//H`, `χ_H`)
- Status: NOT-STARTED. Inputs in code: `TauCeti.HopfAlgebra.conjugationAlgHom` (Algebra/AlgebraicGroup/Hopf/Conjugation.lean), `TauCeti.ComoduleAlgebra.finiteType_coinvariants` for linearly reductive Hopf algebras (Algebra/Bialgebra/ComoduleAlgebra/LinearlyReductive.lean), `reductiveCommHopfAlgProperty`. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43631 (AlgebraicGeometry/Quotient/{ComoduleAlgebra,Conjugation}.lean: the field case `X // G` and `Conj_H`).
- Ready now: yes over a field (ReductiveGroups Layer 6, Mathlib `AlgHom.equalizer`); the DVR case needs ReductiveGroupsPartII RG2.3.1 *reductive-model* (not started).
- Serves defs: 89
- Evidence: README l.1382 "### 1.11 Uniqueness of lattices and symplectic models", l.1436 "**Reductive quotients over fields and DVRs.**", `Conj_H` and the `GL_n` characteristic-polynomial instance l.1456–1475, *Needs* l.1476.

### §§2.1–2.2 Decomposition groups, inertia, unramifiedness and Frobenius
- Status: NOT-STARTED (no `GaloisRep.decompositionGroup`, `GaloisRep.inertiaGroup`, `IsArithFrobAtIntegralPrime` in Tau Ceti). Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/43514 (§2.1 decomposition, inertia and wild inertia groups at primes of the integral closure of `𝓞 F` in `F^alg` with the arithmetic Frobenius predicate, NumberField/AbsoluteGaloisGroup/Decomposition.lean, `TauCeti.GaloisRep.toIntegralClosure`) and https://github.com/TauCetiProject/TauCeti/pull/43510 (§2.1 global closure in the local closure, `IsSeparable.exists_isSeparable_adjoin_simple_eq_of_denseRange`, Analysis/Normed/Field/Dense.lean). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43604 (NumberTheory/NumberField/LocalGlobal/PlaceAction.lean: §2.1 *Finite-place Galois action*, stabilizers as decomposition subgroups).
- Ready now: yes for §2.1's local closure and decomposition and inertia groups: Mathlib `IsKrasner.krasner`, `AlgHom.IsArithFrobAt`, `ValuationSubring.decompositionSubgroup` and the completed LocalFieldsRamification. §2.2 follows §2.1.
- Serves defs: 69, 89
- Evidence: README l.1599 "## Layer 2: decomposition groups, inertia and Weil–Deligne representations", l.1616 "### 2.1 Decomposition groups" (*Needs* "Mathlib `IsKrasner.krasner`; `TauCetiRoadmap.LocalFieldsRamification`"), l.1796 "### 2.2 Ramification and Frobenius".

## TauCetiRoadmap/IntegralHeckeAndGaloisDeterminants
No STATUS.md (merged; Tau Ceti checked at 91942aa9f, 2026-11-19).

### §3a.1 GLₙ Hecke polynomials, Frobenius conventions and the rank-two modular-form normalization
- Status: NOT-STARTED (grep `heckePolynomial` in Tau Ceti: no hits; the rank-two input `HeckeRing.GL2.Newform.satakeParameters` is in code).
- Ready now: no: the integral GLₙ Hecke polynomial needs IHG.0 and SmoothRepresentationsOfLocalGroups SR.4.3 *gln-generators* (not started); the rank-two normalization needs it.
- Serves defs: 69 (the Frobenius-polynomial normalization of `ρ_{f,λ}`), 88 (through AutomorphicLFunctionsAndLocalFactors AL.4.1.1 and AL.R.4)
- Evidence: README l.1730 "### 3a.1 GLₙ Hecke polynomials and Frobenius conventions", l.1833 "**Rank-two classical modular-form normalization.**" (*Needs* "Integral GLn Hecke polynomial, Arithmetic and geometric Frobenius conversion, Tau Ceti `HeckeRing.GL2.Newform.satakeParameters`").

## TauCetiRoadmap/ComplexKahlerGeometry
STATUS.md snapshot: d9fbe7b 2026-11-11 (Tau Ceti checked at 91942aa9f, 2026-11-19)

### K1 + K2 type calculus, T^{1,0}, (1,1)-forms, Dolbeault, i∂∂̄
- Status: PARTIAL: the pieces def 38 needs are in place: eigenbundles T^{1,0}/T^{0,1} (Geometry/Symplectic/Manifold/AlmostComplex/Eigenbundle/), type projections and `IsOfType φ J p q` (Geometry/Manifold/DifferentialForm/AlmostComplexType.lean:205), ∂, ∂̄, d=∂+∂̄, ∂̄²=0 (Geometry/Manifold/DifferentialForm/Dolbeault/{Basic,ComplexManifold}.lean), `dC` with ddᶜ=2i∂∂̄ (Dolbeault/DC.lean), Dolbeault complex and cohomology with pullback, wedge product and `H^(p,0)` (Dolbeault/{Complex,Cohomology,Wedge}.lean), the `(0,q)` polydisc Dolbeault–Grothendieck lemma on smaller concentric polydiscs (`exists_contDiffOn_delBarCoeff_eq_of_polydisc`, Analysis/Complex/Wirtinger/Polydisc.lean). Missing: Newlander–Nirenberg, parametrized submanifolds, the whole-polydisc `(p,q)` lemma, Dolbeault theorem; i∂∂̄ only for smooth forms (no C² version, which is not a target either). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/39955 (K2 §2.1 Dolbeault coordinate formula for `∂̄` of arbitrary smooth `(p,q)`-forms, Dolbeault/ModelSpace.lean). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43526 (Geometry/Manifold/Complex/InverseFunction.lean: the holomorphic inverse function theorem of K1 §1.1).
- Ready now: yes (remaining K1/K2 work is not needed for def 38)
- Serves defs: 38
- Evidence: README l.370 "## Layer 1: complex structures and type calculus (K1)", l.558 "## Layer 2: Dolbeault calculus and the local lemmas (K2)"; STATUS "K1 is partial ... K2 is partial: ∂ and ∂̄ have their bidegrees ... `dᶜ = i(∂̄ − ∂)` satisfies `ddᶜ = 2i∂∂̄`"; grep confirms `typeProjection`, `IsOfType`, `dC`, `delBar_delBar_ofComplexManifold`

### §6.1 K6.0 Kähler predicate IsKahler and local Kähler identities
- Status: PARTIAL: the real-carrier predicate `TauCeti.SmoothTwoForm.IsKahler` (closed, `Compatible`, `J.nijenhuis = 0`) with `isKahler_iff`, `IsKahler.isSymplectic`, `isKahler_ofComplexManifold_iff` and the flat example (Geometry/Symplectic/Manifold/Kahler.lean, Tau Ceti PR #37267). Missing: the Hermitian-metric form of the predicate and its comparison with the real carrier, and the local Kähler and curvature identities of 6.1
- Ready now: no: the rest of 6.1 needs K4, 5.1's formal-adjoint comparison and K1 Newlander–Nirenberg for the complex-manifold comparison
- Serves defs: 38 (ComplexHessianEquations Layers 5–6 consume K6.0 for the theorem)
- Evidence: README l.2321 "### 6.1 Local Kähler and curvature identities (K6.0)", "The canonical predicate is a Hermitian metric on a complex manifold with closed fundamental form ... real-carrier condition `IsKahler form J`"; Dependencies l.2690 "6.1 uses Layers 1, 2 and 4 and 5.1's local formal-adjoint comparison"

### §5.7 K5a Hodge/Laplace self-adjoint H² realization, compact resolvent
- Status: NOT-STARTED: the smooth operators exist (`hodgeLaplacian` Geometry/Manifold/Riemannian/Codifferential.lean:246, `laplaceBeltrami` Geometry/Manifold/Riemannian/Laplacian.lean:274) and the abstract `LinearPMap.HasCompactResolvent` API exists (Analysis/InnerProductSpace/LinearPMap/CompactResolvent.lean), as do integer-order bundle Sobolev spaces `TauCeti.SobolevSection` over a finite bundle atlas (Geometry/Manifold/VectorBundle/Sobolev/), but there is no H² realization, real-order distributional Sobolev scale or Rellich on manifolds
- Ready now: no: needs PseudodifferentialOperators P1.0 (Layer 1 partial), 5.4 compact-bundle Sobolev scale (the distributional `BundleSobolev E s` is missing), 5.1 density/test layer (partial: the pointwise star, `DensityBundle` (Geometry/Manifold/VectorBundle/Density.lean) and the fixed-compact topology on compactly supported sections (Geometry/Manifold/VectorBundle/Section/CompactSupportTopology.lean) exist; the orientation line, `BundleTest` on density-twisted bundles and bundle distributions do not); HopfRinow L1 and DG 8.5 are in place
- Serves defs: 40, 38 (ComplexHessianEquations Layer 5 consumes K5a)
- Evidence: README l.1948 "### 5.7 Laplace-type estimates, spectral theory and the real Hodge theorem (K5a)", l.2013 "For every formally self-adjoint nonnegative Laplace-type system P on a compact boundaryless base, build its geometric H² realization", l.2038 "satisfies `LinearPMap.HasCompactResolvent`"; *Needs* l.2075; STATUS "K5a is partial: ... Hodge Laplacian ... chart `C^k` seminorms and the topology on smooth sections ... but not the orientation line, density bundle, bundle distributions or Sobolev scale"

### §4.2 K4 Chern connections
- Status: NOT-STARTED (no Chern connection; holomorphic line bundles exist, `Geometry/Manifold/Complex/StructureSheaf/LineBundle/Basic.lean`).
- Ready now: no: needs 4.1 and K1 §1.4's Newlander–Nirenberg theorem (missing).
- Serves defs: 38 (the Ricci form in ComplexHessianEquations Layer 6, for the paper's theorem)
- Evidence: README l.1134 "### 4.2 Chern connections and Koszul–Malgrange"; *Needs* l.1155.

## TauCetiRoadmap/HeegaardFloer
STATUS.md snapshot: 7b9b7c6 2026-11-16, generated against Tau Ceti aa6e43e (Tau Ceti checked at 91942aa9f, 2026-11-19)

### F0.5 (§2.7) finite-C^ℓ almost-complex parameter spaces and regularity-loss comparisons
- Status: PARTIAL: finite-regularity carriers `ContMDiffAlmostComplexStructure`, families `ContMDiffAlmostComplexStructureFamily`, chart reading/reconstruction `chartEquiv`, `inChart` (…/Manifold/AlmostComplex/{ContMDiff,Family,Chart,Family/Chart}.lean). Missing: the Banach manifold of C^ℓ tame/compatible J (conjugation charts, openness, Nemytskii estimates), universal CR section, derivative-budget comparisons.
- Ready now: no: needs F1.1–F1.2 `W^{1,p}`/bundle estimates (STATUS Layer 3 remaining) and F0.0 Banach-manifold floor (partial).
- Serves defs: 56, 60 (through F2.4/F2.6d)
- Evidence: README l.1873 "### 2.7 Regularity-loss comparisons for surface and strip Cauchy–Riemann sections (F0.5)"; STATUS Layer 3 remaining "W^{1,p} and bundle interior estimates, totally real boundary estimates, Sobolev spaces on strips, ..."; grep `universalCauchyRiemann` none.

### F2.2 (§4.2) local theory: unique continuation, isolated critical points, adapted coordinates
- Status: PARTIAL. F2.2a's point-preimage part (McDuff–Salamon Lemma 2.4.1 for point preimages) for a `C¹` solution `u` of `∂ₜu = J(u) ∂ₛu` with `J` Lipschitz near the value: unique continuation `TauCeti.eqOn_const_of_cauchyRiemann_of_eventually_eq`, `eqOn_const_of_cauchyRiemann_of_forall_isBigO`, discrete preimages `setOf_ne_mem_codiscreteWithin_of_cauchyRiemann`, finitely many on compacts `finite_inter_preimage_singleton_of_cauchyRiemann`, finite local order `exists_isTheta_pow_of_cauchyRiemann` (Geometry/Symplectic/JHolomorphic/UniqueContinuation.lean). F2.2b (Lemma 2.4.2): the adapted chart `TauCeti.exists_holomorphicAdaptedChart` built from `holomorphicNormalExtension` `Φ(a, w) = u a + Θ_a w`, standard structure along the disc `OpenPartialHomeomorph.pullbackEnd_of_coe_eq_holomorphicNormalExtension`, the normal Lipschitz control for `C²` `u` and `J` `exists_holomorphicAdaptedChart_norm_pullbackEnd_sub_le` and the resulting inequality `‖∂ₛb + i ∂ₜb‖ ≤ C ‖b‖ ‖∂ₜ(a, b)‖` for the normal component, `norm_snd_add_I_smul_snd_le` (JHolomorphic/AdaptedChart.lean). Linear inputs: the similarity principle for continuous weak solutions with `L^p_loc` coefficients, `p > 2`, for the structure `i`, `TauCeti.exists_similarity_of_hasWeakConjWirtingerDerivOn`, `hasSimilarityFactorizationAt_of_hasWeakConjWirtingerDerivOn` (Analysis/Complex/CauchyRiemann/Similarity.lean), the variable-structure unique continuation for `C¹` solutions (CauchyRiemann/UniqueContinuation/VariableStructure.lean) and the linearized Floer version (Geometry/Symplectic/Floer/UniqueContinuation.lean). Missing: the `W^{2,p}` regularity step of F2.2a, isolated critical points through the differentiated equation and finite critical sets, and F2.2c (Lemma 2.4.3, accumulation to factorization).
- Ready now: yes for F2.2c: its proof uses F2.2b's adapted coordinates and normal inequality and the similarity principle for a bounded coefficient, all in code. The isolated-critical-point step for `C¹` curves with `C²` J could begin on the variable-structure theorems; for `C¹` J it starts from PH5.1 `W^{2,p}` regularity.
- Serves defs: 60
- Evidence: README l.2592 "### 4.2 Local theory (F2.2)", items a (l.2597, "Prove local unique continuation and isolated point-preimages. Apply the similarity principle also to its differentiated CR equation ...; prove isolated critical points"), b (l.2604, "Straighten an embedded reference disc to (a,0) with J(a,0)=i", Lemma 2.4.2) and c (l.2613, "the local accumulation-to-factorization lemma (Lemma2.4.3)"), *Needs* l.2642; STATUS Layer 4 remaining "local theory". The Lemma 2.4.3 factorization is absent from Geometry/Symplectic/JHolomorphic/ (AdaptedChart.lean names it only as the consumer of `norm_snd_add_I_smul_snd_le`).

### F2.4 (§4.4) and F2.6d (§4.6d) universal moduli spaces, regular J
- Status: NOT-STARTED; local-coordinate linearization exists (`cauchyRiemannLinearization`, Geometry/Symplectic/JHolomorphic/Linearization.lean), the localized variation of a smooth J at an injective point (positive pairing with a cokernel covector, Geometry/Symplectic/Manifold/AlmostComplex/Variation.lean), and F0.0's transversality package: the Sard–Smale theorem `TauCeti.isMeagre_image_criticalPoints_of_isFredholm` for `C^k` Fredholm maps with `k > max(index, 0)` (Analysis/Fredholm/SardSmale.lean), universal level sets and parametric transversality (Analysis/Fredholm/{UniversalLevelSet,Parametric}.lean).
- Ready now: no: needs F0.5 parameter spaces, F2.2 somewhere-injectivity, F1.2 adjoint identification; F2.6d also F2.6b–c and PH5.2.
- Serves defs: 56, 60
- Evidence: README l.2688 "### 4.4 Transversality (F2.4)", *Needs* l.2711; l.2975 "### 4.6d Transversality and degree (F2.6d)", *Needs* l.3027; STATUS Layer 4 remaining "transversality and gluing"; STATUS prose "the abstract transversality package (sharp Sard, Sard–Smale, parametric transversality, the determinant line bundle) is in place".

### F2.6e (§4.6e) normal operator of embedded spheres, four-dimensional regularity
- Status: PARTIAL (local only): `normalCauchyRiemannLinearization` (JHolomorphic/Normal/Linearization.lean) with target covariance `normalFDerivMap` and source covariance `normalCauchyRiemannLinearization_comp_right`, `normalCauchyRiemannLinearization_comp_right_of_surjective` (Normal/Naturality.lean); normal rescaling (Normal/Rescaling.lean); the complex structure on the quotient by the image of a complex-linear map `AlmostComplexStructure.quotient`, `IsComplexLinearMap.quotientRange` (Geometry/Symplectic/AlmostComplex/Quotient.lean) and the pointwise ellipticity of the real Cauchy–Riemann symbol, bijective onto complex-antilinear maps for a nonzero covector (`cauchyRiemannSymbolAntilinear_bijective`, `cauchyRiemannSymbolEquiv`, JHolomorphic/Symbol.lean). Missing: the global normal-bundle real CR operator, intersection multiplicities, Micallef–White, adjunction, automatic surjectivity for d ≥ −1.
- Ready now: no: needs F2.2, F2.6b, F1.5, F1.2.
- Serves defs: 60
- Evidence: README l.3029 "### 4.6e Four-dimensional curves and regularity (F2.6e)", "For an embedded sphere construct the quotient real CR operator on its normal" (l.3140), *Needs* l.3172.

### F4.B (§6.2) Spin^c, Turaev model, grading carrier
- Status: NOT-STARTED for Spin^c: no Turaev vector-field model, no Spin^c torsor, no c₁. Adjacent combinatorial code only: `HeegaardRegionSystem.WeaklyAdmissibleAt` (spin^c read through Maslov index of periodic domains) and relative grading in TauCeti/LowDimTopology/Heegaard/{SpincAdmissibility,RelativeGrading}.lean; the group `CliffordAlgebra.spinCGroup` = (Spin × U(1))/(−1,−1) with `det`, `toSpecialOrthogonal` and charge conjugation `CliffordAlgebra.spinCGroup.chargeConj` (LinearAlgebra/CliffordAlgebra/Spin/SpinC.lean) and its Lie-group structure (Geometry/Lie/CliffordAlgebra/SpinC/Basic.lean). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43592 (Spinᶜ structures on a vector bundle as principal lifts of the orthonormal frame bundle, Topology/VectorBundle/SpinCStructure.lean; not Turaev's vector-field model).
- Ready now: no: needs F4.A geometric pointed diagrams (only combinatorial `HeegaardRegionSystem`, no handlebody-glued Y found) and F1.4–F1.5.
- Serves defs: 64
- Evidence: README l.3646 "### 6.2 Spinᶜ, periodic surfaces and the grading carrier (F4.B)", *Needs* l.3744; STATUS Layer 6 remaining "spin^c structures in general"; SpincAdmissibility.lean: "identification ... with the Chern class pairing is geometric and is not formalized here".

## TauCetiRoadmap/ModularCurves
STATUS.md snapshot: 7ca783d 2026-11-09, written against the layer numbering before the README reorganisation of roadmap PR #2140 (old 0G is §0.7, old 2B is §2.2, old Layer 9 coarse schemes is Layer 6; Tau Ceti checked at 91942aa9f, 2026-11-19)

### §0.7 relative finite-locally-free Grassmannian, Plücker
- Status: PARTIAL: affine case fully in Tau Ceti (TauCeti/AlgebraicGeometry/Grassmannian/*: `scheme`, `glueData`, `chartι`, `schemeHomEquiv`, `isProper_toSpec`, `schemeUniversalIdeal`, Hopf-ideal locus, `FiniteLocallyFree.lean`), with base change along `Spec R' → Spec R`, `G(k, R' ⊗[R] M) ≅ Spec R' ×_{Spec R} G(k, M)` (`Module.Grassmannian.isPullback_baseChangeHom`, `baseChangeHom`, Grassmannian/BaseChange.lean), the comparison used to glue over a non-affine base. Missing: gluing over a non-affine base with independence of trivialisations, universal quotient and kernel there, the universal property over arbitrary `S`, subbundle/dual comparisons, `Grass_1(F) ≅ Proj_S(Sym F)`, the Plücker closed immersion. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43522 (the isomorphism of Grassmannian schemes induced by a linear equivalence, `Module.Grassmannian.schemeIsoOfLinearEquiv` with its functoriality, the change-of-trivialisation step of the gluing; the gluing itself is not in it).
- Ready now: yes for gluing over a non-affine base. The rank-one identification and Plücker need StableReduction Layer 2's relative Proj and AlgebraicVectorBundles L0C/L2A (exterior powers, `gradedSymmetricAlgebra`).
- Serves defs: 25, 26 (through AlgebraicModuliForArithmeticGeometry §1.3, whose *Needs* is "ModularCurves §0G")
- Evidence: README l.1076 "### 0.7. Parameter spaces for subgroup schemes" ("This block owns the relative Grassmannian of a finite locally free `𝒪_S`-module"); STATUS Layer 0 remaining "0G over a non-affine base".

### Layer 10 compactified coarse X_H, X_0(N)
- Status: NOT-STARTED (TauCeti/AlgebraicGeometry/ModularCurve/ has `Y₁(N)`, Legendre and level-three lines, no coarse `Y₀(N)` or `X_H`)
- Ready now: no: needs §2.2 quotient isogenies (STATUS "2B quotients E/C" remaining), §3.2 naive `[Γ₀(N)]` (STATUS "naive Gamma0(N)" remaining), Layer 6 quotients, coarse schemes and the `j`-line (STATUS old Layer 9 "everything beyond the Legendre and level-three rings"), the formal-cusp package and a Riemann–Hurwitz package. It uses nothing from Layers 7–9
- Serves defs: 69, 71
- Evidence: README l.4030 "## Layer 10: compactified coarse curves over `ℤ[1/N]`, cusps, and the Shimura covering", Dependencies l.4266; README l.4399 "Dependency order and parallel work" ("Layer 10 uses nothing from Layers 7–9"); STATUS "Layer 10 has not begun".

## TauCetiRoadmap/AlgebraicModuliForArithmeticGeometry
No STATUS.md (merged as roadmap PR #853; Tau Ceti checked at 91942aa9f, 2026-11-19).

### §1.3 coherentGrassmannian, plucker (with §1.1 projectiveBundle for the P(E) and Plücker clauses)
- Status: NOT-STARTED (grep `coherentGrassmannian|projectiveBundle|ProjectiveBundles` empty; the affine `Module.Grassmannian.scheme` with base change is in code under ModularCurves §0.7)
- Ready now: no: `coherentGrassmannian` (classifying maps, base change, agreement with `Module.Grassmannian` on affines, properness over `Spec R`) needs ModularCurves §0.7 over a non-affine base (partial; that gluing is ready now). `Gr_1(E) ≅ P(E)` and `plucker` also need §1.1 `ProjectiveBundles.projectiveBundle`, whose Needs are SSF §0.3 (begun: TauCeti/AlgebraicGeometry/RelativeProj/), StableReduction Layer 2, AlgebraicVectorBundles L0C and SSF §5.4 (not started)
- Serves defs: 25, 26
- Evidence: README l.609 "### 1.3 Coherent quotients, Plücker and partial flags" ("Define `coherentGrassmannian`. For a quasi-coherent finite-type E on arbitrary S ..."; *Needs:* ModularCurves §0G, `ProjectiveBundles.projectiveBundle`, ...), l.313 "### 1.1 Projective quotients and all integer twists"; cited by NashBlowups §1.2 and its supplier contract (README l.51, l.342).

### §4.1 IsGerbe and relative gerbes
- Status: NOT-STARTED (grep `IsGerbe|relativeGerbe` empty; the `TrivialGerbe` files in Geometry/Manifold/Etale/ and Topology/CategoryTheory/Groupoid/Effective/ are topological groupoid gerbes, unrelated). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43615 (CategoryTheory/Sites/Descent/IsGerbe.lean: `Pseudofunctor.IsGerbe`).
- Ready now: yes (Needs only Mathlib `Pseudofunctor.IsStack`, `IsPrestack`, `Aut`)
- Serves defs: 29
- Evidence: README l.1862 "### 4.1 Gerbes and relative locality" ("Define `IsGerbe`. For `F : C`ᵒᵖ → Cat a pseudofunctor ..."); StackPointsAndResidualGerbes' supplier contract (README l.480) cites §4.1 `IsGerbe`, `IsGerbe.equivalence_iff`, `relativeGerbe`, `relativePullback`, ... for its Layer 2 (l.999 "## Layer 2: gerbes over algebraic stacks").

## TauCetiRoadmap/SmoothBundlesConnections
STATUS.md snapshot: d137fc6 2026-11-09 (to Tau Ceti d92acc5; Tau Ceti checked at 91942aa9f, 2026-11-19)

### B1.4 Slices, quotients and homogeneous spaces G/H
- Status: PARTIAL: the free proper quotient theorem is in code: for a finite-dimensional real Lie group acting smoothly, freely and properly on a boundaryless manifold, `M ⧸ G` is a manifold of dimension `dim M − dim G` (`ProperSMul.orbitRelQuotientChartedSpace`, `instIsManifoldOrbitRelQuotient`) and the orbit map is a smooth submersion (`isSubmersion_quotientMk`, `ker_mfderiv_quotientMk`), Geometry/Manifold/GroupAction/Quotient.lean. Its inputs: orbit-space charts from transverse slices (`TauCeti.MulAction.isOpenEmbedding_quotientMk_slice`, `TauCeti.exists_contMDiffAt_quotientMk_slice_eq_iff`, GroupAction/SliceChart.lean), transverse slice maps as local diffeomorphisms (`isLocalDiffeomorphAt_smul_slice_iff`, GroupAction/TransverseSlice.lean), orbit maps of free points as closed smooth embeddings (`isSmoothEmbedding_smul_const`, GroupAction/Orbit.lean), compact stabilizers and closed orbits of proper actions (Topology/Algebra/ProperAction/Orbit.lean), Haar-averaged invariant metrics (Geometry/Manifold/Riemannian/Invariant.lean), equivariant charts for finite groups (GroupAction/Linearization.lean), and smooth functions on orbit spaces (GroupAction/SmoothFunctions.lean, Geometry/Manifold/Quotient/). Missing: the principal-bundle clause `exists_principalBundle_orbitFiber` (the orbit projection as a `TauCeti.PrincipalBundle`), the compact-isotropy equivariant exponential chart and slice theorem `G ×_H B`, and smooth G/H for a closed subgroup H as a named construction (its inputs are in code: the free proper quotient theorem and Cartan's closed-subgroup theorem `isEmbeddedLieSubgroup_of_isClosed`, Geometry/Lie/Subgroup/Embedded.lean). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43518 (`G ⧸ K` for a closed subgroup as a smooth manifold of dimension `dim G - dim 𝔨`, `Subgroup.quotientChartedSpace`, `Subgroup.instIsManifoldQuotient`, `Subgroup.isSubmersion_quotientMk`, Geometry/Lie/Subgroup/Quotient.lean), https://github.com/TauCetiProject/TauCeti/pull/43721 (equivariant linear slices at points with compact stabilizer, GroupAction/EquivariantSlice.lean) and https://github.com/TauCetiProject/TauCeti/pull/43727 (twisted products `G ×_K B` as free proper quotients, GroupAction/TwistedProduct.lean); no open PR assembles the slice theorem from them.
- Ready now: yes for the slice theorem and for G/H, both on the free proper quotient theorem; the principal-bundle clauses consume B1.1's `TauCeti.PrincipalBundle` API, which is in Tau Ceti
- Serves defs: 62, 15, 31 (through RealSemisimpleLieGroups §§5.2, 5.7)
- Evidence: README l.578 "### B1.4 Slices, quotients and homogeneous spaces", l.589 "Prove the free proper quotient theorem first by transverse local charts and properness", l.608 headline `exists_principalBundle_orbitFiber`, l.642 "For a closed Lie subgroup H≤G ... construct G/H"; *Needs* l.735 ("B1.1, B1.2; LieGroups Layer 2; ...")

### B2 pullback connection (as cited)
- Status: B2.1 (pullback/Hom/associated bundles) is PARTIAL: smooth associated bundles and complexification exist. B2 has no connection content
- Ready now: n/a (see R5a)
- Serves defs: 49
- Evidence: README l.829 "### B2.1 Associated bundles and complex structures" constructs associated, tensor, dual, exterior-power, direct-sum and Hom bundles and pullback comparisons only; connection pullback is in B3.1 l.1209 ("smoothness, pullback, restriction") and B3.3 l.1267 for principal/associated connections

### B3–B4 Principal connections, curvature, gauge group
- Status: NOT-STARTED (Layers 3–7 "untouched"; no principal connections, curvature or gauge group in code; the gauge code is the U(1) vortex theory on ℂ, Analysis/PDE/Vortex/, unrelated). Inputs that exist: the orthonormal (unitary) frame bundle of a metric vector bundle as a topological principal `O(n)`/`U(n)` bundle `TauCeti.OrthonormalFrameBundle.Fiber` with proper projection (Topology/VectorBundle/OrthonormalFrame/{Principal,Basic}.lean), and the splitting of the first-jet sequence by a vector-bundle connection (Geometry/Manifold/VectorBundle/FirstJet/Connection.lean)
- Ready now: no: B3.1 needs B1.5 (Ehresmann connections, not in code) and B2.5 (smooth GL frame bundles, reductions and ad(P); only the topological orthonormal frame bundle exists); B4 needs B3.1–B3.3
- Serves defs: 37, 48 (consumed by YangMillsConnectionsAndCaloricGauge §1.3)
- Evidence: README l.1200 "### B3.1 Principal connections" (*Needs* l.1234 "B1.5, B2.5; Tau Ceti `TauCeti.SmoothBundleForm`, `TauCeti.bracketWedge`, `TauCeti.CurvatureForm`, `TauCeti.mextDeriv`, `TauCeti.fundamentalVectorField`; LieGroups Layer 1"), l.1311 "### B4.1 Curvature and the exterior covariant derivative", l.1343 "### B4.2 The gauge group"; STATUS coverage Layer 3/4 "state":"untouched"

## TauCetiRoadmap/YangMillsConnectionsAndCaloricGauge
No STATUS.md; Tau Ceti checked at 91942aa9f, 2026-11-19 (grep `caloric`, `instanton`: no hits; `YangMills` hits only Analysis/PDE/YangMills/StructureGroup.lean, §1.1). Its Tau Ceti suppliers are in code: `TauCeti.WeakDerivStep`, `TauCeti.D1p0` with `sobolevEmbeddingL`, `TauCeti.heatKernel`, the Mihlin–Hörmander theorem, the closed-subgroup theorem (`Geometry/Lie/Subgroup/`), `Ad`-invariant inner products (`TauCeti.Lie.exists_isSymm_bilinForm_Ad_invariant`, `Geometry/Lie/Adjoint/InvariantForm.lean`), `HomotopyGroup.bijective_hurewicz`, the smooth degree (`Geometry/Manifold/Degree/`).

### Layer 1 (§§1.1–1.6) Structure group, nearest-point retraction, gauge identities, invariant and Chern–Simons forms, self-duality
- Status: PARTIAL: §1.1 is in code except the tangent-space clause: `TauCeti.CompactMatrixStructureGroup n` (a closed subgroup of `U(n)` with an `Ad`-invariant inner product on its Lie algebra `ClosedSubgroup.matrixLieAlgebra`), `ofTraceForm`, `restrict`, `prod`, `innerForm_matrixAdjointRepresentation` (`Ad(g)` is an isometry), `innerForm_lie_left` (`ad X` is skew-adjoint) (Analysis/PDE/YangMills/StructureGroup.lean, on Geometry/Lie/Subgroup/Unitary/Matrix.lean, Tau Ceti PR #58). Missing: the tangent space `g𝔤 = 𝔤g` of §1.1, and §§1.2–1.6.
- Ready now: §1.1's tangent-space clause yes (its *Needs* are Mathlib and the pinned Tau Ceti closed-subgroup declarations); §1.5 yes (Tau Ceti `Orientation.formHodgeStar`); §1.2 no: needs RiemannianGeometry R6's Euclidean tube inversion; §1.3 no: needs SmoothBundlesConnections B3.1, B4.1–B4.2 (untouched); §1.4 no: needs CharacteristicClasses C4 item 1 and C5a.3 (untouched).
- Serves defs: 37, 48
- Evidence: README l.490 "## Layer 1: structure groups and pointwise gauge algebra", l.492 "### 1.1 The structure group" (l.498 "The tangent space of `G` at `g` ... is `g𝔤 = 𝔤g`"); *Needs* l.521 (§1.1), l.568 (§1.2 "RiemannianGeometry R6"), l.600 (§1.3 "SmoothBundlesConnections B3.1, B4.1, B4.2"), l.648 (§1.4 "CharacteristicClasses C4 item 1 and C5a.3").

### Layers 2–3 (§§2.1–2.5, 3.1–3.4) `G^{k,p}_loc`, rough connections, gauge invariance of finite energy
- Status: NOT-STARTED (order-one vector-valued `W^{1,p}` is `TauCeti.WeakDerivStep`; no `G`-valued classes).
- Ready now: no: §2.1 needs PDE gap `vector-valued-wkp` (orders `k ≥ 2` and local classes of `W^{k,p}(Ω; V)`, requested of PDE Layer 1 in the Exact supplier contracts) and §1.1; §2.2 needs §1.2; §3.2 needs §1.3.
- Serves defs: 48 (48.1), 37
- Evidence: README l.739 "## Layer 2: critical Sobolev maps into `G`", l.905 "## Layer 3: rough connections and gauge invariance"; *Needs* "Tau Ceti `TauCeti.WeakDerivStep`; gap `vector-valued-wkp` (PDE)", l.951 "1.3, 2.4, 3.1"; gap text l.394 "What PDE must provide (gap:vector-valued-wkp)".

### Layers 4–6 (§§4.1–4.4, 5.1–5.6, 6.1–6.4) Uhlenbeck gauges, good global gauge, `Top(d, G)`, characteristic numbers, `SU(2)` instanton number
- Status: NOT-STARTED.
- Ready now: no: §4.1 needs PDE gaps `lp-neumann-ball` and `lp-divcurl-normal-ball`; §§5.2, 5.3, 6.1 need PDE gap `hardy-inequality`; all need Layers 2–3; §6.4 also needs AlgebraicTopology §§6.5, 8.3 (Hurewicz in code).
- Serves defs: 48 (48.2–48.5), 37
- Evidence: README l.1020 "## Layer 4: Uhlenbeck's lemmas and the good gauge on a ball", l.1192 "## Layer 5: the good global gauge and the topological class", l.1294 "### 5.4 The topological class, the trivial class and `Top(4, G) ≅ π₃(G)`", l.1376 "## Layer 6: characteristic numbers and the instanton number", l.1452 "### 6.4 The instanton number for `SU(2)`"; *Needs* l.1057, l.1260, l.1334, l.1506.

### Layer 7 (§§7.1–7.7) Harmonic Yang–Mills connections, energy gap, BPST, ground state
- Status: NOT-STARTED.
- Ready now: no: needs Layers 4–6, Yamabe Y2 item 1 (sharp Sobolev inequality `sphereYamabeConstant_mul_le`, not in code; `TauCeti.Yamabe.sphereYamabeConstant` is) for §7.5, and the LieGroups gap `compact-su2-subalgebra` for §7.7.
- Serves defs: 37 (§§9.6–9.7 and §10.2 consume §7.7)
- Evidence: README l.1520 "## Layer 7: harmonic Yang–Mills connections and the ground state"; *Needs* l.1631 "Yamabe Y2 item 1; 6.3, 7.3, 7.4", l.1686 "gap `compact-su2-subalgebra` (LieGroups); 1.6, 7.5, 7.6".

### Layers 8–10 (§§8.1–8.4, 9.1–9.7, 10.1–10.5) Homogeneous spaces on `ℝ⁴`, Yang–Mills heat flow, caloric gauge and caloric manifold
- Status: NOT-STARTED (only inhomogeneous Littlewood–Paley blocks and Besov spaces in code; `TauCeti.D1p0` supplies `Ḣ¹(ℝ⁴)`).
- Ready now: no: §8.1 needs PDE §7.1–7.2's homogeneous blocks and homogeneous Besov spaces (PDE Layer 7 partial, not in code) on `TauCeti.D1p0` (in code); §9.1 needs §1.3; §§9.6–9.7 need Layers 4, 6–7; Layer 10 needs Layer 9 and Layers 3–4.
- Serves defs: 37
- Evidence: README l.1697 "## Layer 8: homogeneous spaces and linear covariant flows on `ℝ⁴`", l.2038 "## Layer 9: the Yang–Mills heat flow on `ℝ⁴`", l.2303 "## Layer 10: the caloric gauge and the caloric manifold"; *Needs* l.1880, l.2082, l.2390, l.2424, l.2526; build order l.486–488.

New items in other sections:

## TauCetiRoadmap/GeometricCurrents
STATUS.md snapshot: 941bb58 2026-11-12 (Tau Ceti checked at 91942aa9f, 2026-11-19)

### G1–G2 Mass and pushforward of Lipschitz images
- Status: PARTIAL, Euclidean only: mass/local mass (Analysis/Distribution/Mass/Basic.lean), the Radon mass measure (Mass/Measure.lean), L¹ extension and Borel restriction (Mass/Extension.lean), normal currents (Mass/Normal.lean), weak compactness (Mass/Compactness.lean), smooth pushforward of compactly supported currents (Analysis/Distribution/CutoffPushforward.lean), integration and simplex currents, the cone operator with mass bounds (Mass/Cone.lean), slicing of locally normal currents by a smooth function (Mass/Slice.lean). Missing: the manifold `TestForm`/`Current` carrier, integer-rectifiable currents, Lipschitz pushforward (G2)
- Ready now: no for the manifold carrier: G1 needs K5a's early `BundleTest` (CKG 5.1, missing), Calib C1 comass and HopfRinow L0. G2 needs GMT G2–6 (G2 lacks tangent-plane uniqueness and the tangential area formula) and CalibratedGeometry C2. A Euclidean Lipschitz pushforward could start on the existing Euclidean carrier
- Serves defs: 57
- Evidence: README l.137 "## G1. Test forms, currents and mass", l.240 "## G2. Integer rectifiability, integration, pushforward and slicing", l.298 "Extend pushforward to locally Lipschitz maps"; dependency graph l.964-966; STATUS "The Euclidean half of G1 is essentially complete ... Nothing yet lives on a manifold, there are no integer-rectifiable or integral currents, and G3 and G4b–G7 have not begun"

### G3 Lipschitz singular subcomplex
- Status: NOT-STARTED (grep for a Lipschitz singular complex: no hits)
- Ready now: no: needs G2, G4a, Calib C2, AT/GT
- Serves defs: 57
- Evidence: README l.406 "## G3. Ordinary integral-current homology and chain comparisons", l.434 "A Lipschitz singular ..."; dependency graph l.967 "`{G2, G4a, Calib C2, AT/GT, DGF0 adapter} → G3`"

### G6 Varifolds of currents, first variation, monotonicity
- Status: NOT-STARTED (no varifold or Grassmann-bundle code)
- Ready now: no: needs G4b, G5, R5a/R5b, GMT perimeter, PDE strong-solution upgrades, Calib C1/TopK T1.5
- Serves defs: 53, 65
- Evidence: README l.668 "## G6. First variation, normal stability and interior regularity", l.679 "Give the auxiliary rectifiable varifold's restriction, weight, integer multiplicity ...", l.688 "Develop density, monotonicity"; dependency graph l.973

## TauCetiRoadmap/GeometricMeasureTheory
STATUS.md snapshot: 59c8654 2026-11-16, generated against Tau Ceti aa6e43e (Tau Ceti checked at 91942aa9f, 2026-11-19)

### G2 Rectifiable sets, approximate tangents, area formula
- Status: PARTIAL: `CountablyRectifiable`, the density theorem, a.e. existence of approximate tangent planes (Geometry/MeasureTheory/Rectifiable/ApproximateTangent.lean) and a measurable choice of tangent projections (Rectifiable/MeasurableTangent.lean), and the cone condition for the classical tangent plane of a differentiable normal graph (Rectifiable/Graph.lean). The Lipschitz area formula ℝᵐ→ℝⁿ with multiplicity is in MeasureTheory/Function/AreaFormula/{Basic,Lipschitz,Multiplicity}.lean, and the coarea formula for locally Lipschitz maps with a.e. countably rectifiable fibres is in MeasureTheory/Function/Coarea/Lipschitz.lean and Geometry/MeasureTheory/Rectifiable/Coarea.lean. Missing: a.e. uniqueness of tangent planes, tangential differentiation, and the tangential area formula on rectifiable sets. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/37783 (a.e. uniqueness of approximate tangent planes, `CountablyRectifiable.ae_eq_of_tendsto_measure_outside_cone_div`), https://github.com/TauCetiProject/TauCeti/pull/41606 (a.e. uniqueness and measurability of approximate tangent planes, tangential differentiation and tangential Jacobians of Lipschitz maps), https://github.com/TauCetiProject/TauCeti/pull/41204 (tangential calculus and the weighted, counting and injective tangential area formulas, Rectifiable/AreaFormula.lean) and https://github.com/TauCetiProject/TauCeti/pull/39041 (tangential differentiation on Lipschitz normal graphs).
- Ready now: yes
- Serves defs: 53, 57
- Evidence: README l.148 "## G2: Rectifiability, area, and coarea"; STATUS coverage G2 remaining "a.e. uniqueness of approximate tangent planes, tangential differentiation of Lipschitz maps, the tangential area formula"

### G5 De Giorgi structure theorem
- Status: PARTIAL: perimeter API, essential and reduced boundaries, outer normal, density estimates, the `|Dχ| ≤ nω_n Hⁿ⁻¹` bound, blow-ups with the density of the perimeter measure at reduced-boundary points (`tendsto_perimeter_ball_div`, Analysis/BoundedVariation/BlowUp.lean), and slicing of perimeters. Missing: De Giorgi's theorem itself (rectifiability of ∂*E, `|Dχ_E| = Hⁿ⁻¹⌞∂*E`), the essential/reduced comparison, and the frontier criterion. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/41783 (De Giorgi's structure theorem, Analysis/BoundedVariation/DeGiorgi.lean, with the cone criteria for countable rectifiability `CountablyRectifiable.of_forall_infDist_le`), https://github.com/TauCetiProject/TauCeti/pull/40507 (countable rectifiability and Borel measurability of `reducedBoundary`), https://github.com/TauCetiProject/TauCeti/pull/39597 (`μHE[n - 1] ≤ |Dχ_s|` on the reduced boundary, `euclideanHausdorffMeasure_le_variationMeasure_preimage`) and https://github.com/TauCetiProject/TauCeti/pull/42749 (Federer's structure theorem: essential and reduced boundary differ by an `Hⁿ⁻¹`-null set, Analysis/BoundedVariation/Federer.lean).
- Ready now: yes (G3–G4 are essentially done; the needed G2 rectifiability API exists)
- Serves defs: 55
- Evidence: README l.248 "## G5: Finite perimeter and boundary structure", "Prove ... De Giorgi's structure theorem"; STATUS coverage G5 remaining "rectifiability of the reduced boundary, perimeter measure as Hn-1 on it, essential/reduced boundary comparison, frontier criterion"

## TauCetiRoadmap/CStarAlgebras
STATUS.md snapshot: 3930ad9 2026-11-11 (Tau Ceti checked at 91942aa9f, 2026-11-19; stale on C3.2 and C4.1). The CStarAlgebras items also feed merged AmenableTracesOnCStarAlgebras, which specifies #36.

### C2.1 State extension
- Status: PARTIAL: the unital case is in code: along an injective unital star homomorphism every state extends (`TauCeti.surjOn_pullbackFunctional_stateSpace`), and every state of a closed unital star subalgebra is the restriction of a state (`StarSubalgebra.exists_mem_stateSpace_forall_apply_coe_eq`), TauCeti/Analysis/CStarAlgebra/State/Extension.lean, on the state space API of TauCeti/Analysis/CStarAlgebra/State/Space.lean. Missing: pure extensions of pure states (the face of extensions), functorial restriction, the nonunital case. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43635 (Analysis/CStarAlgebra/State/Extension.lean: extension of pure states to pure states).
- Ready now: yes for pure extensions (Krein–Milman `closure_convexHull_extremePoints_stateSpace` exists); the nonunital case goes through C1.2 unitization, which STATUS lists as remaining in Layer 1.
- Serves defs: 36
- Evidence: README l.544 "### 2.1 State extension (C2.1)" ("Prove that every pure state has a pure extension ... Include functorial restriction and the nonunital case through the unitizations"), *Needs* "BanachSpaceTheory B1–B2; VonNeumannAlgebras V0"; Tau Ceti commit 4c2e91858 (#37569).

### C3.2 Completely bounded maps
- Status: PARTIAL: at the C*-algebra level (operator-space structure through `CStarMatrix`) `LinearMap.IsCompletelyBounded` and `LinearMap.cbNorm` with `norm_map_le_cbNorm_mul`, `cbNorm_le_iff`, the norm laws (`cbNorm_add_le`, `cbNorm_smul`, `cbNorm_eq_zero_iff`), `cbNorm_comp_le`, `cbNorm_id`, `NonUnitalStarAlgHom.cbNorm_le_one` and the transpose example `CStarMatrix.cbNorm_transposeₗ` (cb norm `n`), TauCeti/Analysis/CStarAlgebra/CompletelyBounded.lean (Tau Ceti #38429). Missing: abstract operator spaces (C3.1), `CB(E, F)` as a normed space with completeness, the matrix-norm structure on `CB(E, F)` and `E*`, `E → E**` completely isometric, Smith's lemma. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43618 (CompletelyBounded/{Basic,Maps}.lean: the Banach space `CB(A, B)` and `‖u‖_cb = ‖u‖` for functionals).
- Ready now: yes for the C*-level remainder (completeness of the cb maps between C*-algebras, Smith's lemma for C*-algebra domains, `‖u‖_cb = ‖u‖` for functionals); the operator-space parts need C3.1 (not started).
- Serves defs: 36, 46
- Evidence: README l.918 "### 3.2 Completely bounded maps (C3.2)" ("`Suggested.lean` defines complete boundedness of a linear map between C*-algebras as `IsCompletelyBounded`"), *Needs* "§3.1; BanachSpaceTheory B1"; PR #2421 §1.4 compares its Schatten amplification norm with C3.2.

### C3.3 / C5.3 Column/row, MIN/MAX; operator-space tensor products
- Status: NOT-STARTED.
- Ready now: no: C3.3 needs C3.1–3.2; C5.3 needs §3.1–3.3 and §4.4 (Wittstock).
- Serves defs: 36, 46
- Evidence: README l.948 "### 3.3 Column and row spaces, MIN and MAX, operator algebras (C3.3)"; l.1169 "### 5.3 Operator-space tensor products (C5.3)", *Needs* "§3.1–§3.3, §4.4"; grep `OperatorSpace|Ruan` only unrelated hits.

### C4.1 Completely positive maps, Schwarz, multiplicative domain
- Status: PARTIAL: `n`-positivity `TauCeti.IsNPositive` with `CompletelyPositiveMap.ofIsNPositive`; the Kadison–Schwarz inequality `IsNPositive.star_map_mul_map_le` (`φ(a)*φ(a) ≤ ‖φ 1‖ • φ(a*a)` for 2-positive maps) and `IsNPositive.star_map_mul_map_le_of_map_one` (unital), `CompletelyPositiveMapClass.star_map_mul_map_le`; `‖φ a‖ ≤ ‖φ 1‖‖a‖` and `‖φ‖ = ‖φ 1‖` (`IsNPositive.opNorm_eq_norm_map_one`, `CompletelyPositiveMapClass.opNorm_ofClass_eq_norm_map_one`), TauCeti/Analysis/CStarAlgebra/CompletelyPositiveMap.lean (Tau Ceti #38424). Missing: `‖φ‖_cb = ‖φ(1)‖`, the approximate-unit formula and unitization of c.p.c. maps, complete positivity of positive maps with commutative domain or range, the multiplicative domain and bimodularity. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43638 (CompletelyPositiveMap/CompletelyBounded.lean: `‖φ‖_cb = ‖φ‖ = ‖φ 1‖` for completely positive `φ` with unital domain).
- Ready now: yes for `‖φ‖_cb = ‖φ(1)‖` (C3.2's C*-level `cbNorm` exists), the unitization of c.p.c. maps (used by AmenableTracesOnCStarAlgebras §2.1) and the commutative domain/range theorems; the multiplicative domain by the README's dilation route needs C4.2 (not started).
- Serves defs: 36
- Evidence: README l.986 "### 4.1 Completely positive maps, Schwarz and the multiplicative domain (C4.1)", *Needs* "VonNeumannAlgebras V13a; Mathlib `CompletelyPositiveMap`, `CStarMatrix`; §4.2 for the dilation route"; grep `multiplicativeDomain` empty.

### C4.2 Stinespring dilation and Arveson's Radon–Nikodym theorem
- Status: NOT-STARTED (grep `Stinespring`: no hits). Inputs present: GNS and the Gelfand–Naimark faithful representation `exists_faithful_nondegenerate_representation` (TauCeti/Analysis/CStarAlgebra/Representation/GNS.lean), Mathlib `CStarAlgebra.approximateUnit`. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/41199 and https://github.com/TauCetiProject/TauCeti/pull/41244 (each proves nonunital and unital Stinespring dilation with unitary uniqueness of minimal dilations and Arveson's Radon–Nikodym theorem, Analysis/CStarAlgebra/Stinespring/ and CompletelyPositiveMap/{Stinespring,RadonNikodym}.lean respectively).
- Ready now: yes for unital domains (*Needs* VonNeumannAlgebras V0 GNS, in code); the nonunital approximate-unit step cites §1.4, not started.
- Serves defs: 36 (AmenableTracesOnCStarAlgebras §2.2 multiplicativity defects, §4.5, and C4.1's multiplicative domain)
- Evidence: CStarAlgebras README l.1021 "### 4.2 Stinespring dilation and the Radon–Nikodym theorem (C4.2)", *Needs* "VonNeumannAlgebras V0 (GNS); ... §1.4 (approximate units)"; AmenableTracesOnCStarAlgebras README l.985 (§2.2 *Needs* "CStarAlgebras C4.1 ..., C4.2").

### C5.1–C5.2 C*-tensor products: minimal and maximal norms, tensoring maps and functionals
- Status: NOT-STARTED.
- Ready now: no: C5.1 needs VonNeumannAlgebras V13b.SpatialNorm (Layer 13 untouched), V2 (partial) and §4.2; C5.2 needs §5.1 and V4.
- Serves defs: 36 (AmenableTracesOnCStarAlgebras §1.5 bimodule identification, §§3.5, 4.3–4.4)
- Evidence: CStarAlgebras README l.1112 "### 5.1 The maximal C*-norm and the comparison of C*-norms (C5.1)", l.1143 "### 5.2 Tensoring maps and functionals; concrete identifications (C5.2)"; AmenableTracesOnCStarAlgebras README l.1399 (§4.4 *Needs* "CStarAlgebras C4.1 (multiplicative domain), C5.1–C5.2").

### C5.4 Direct sums, products, inductive limits, C*(F_∞)
- Status: PARTIAL: bounded products and their `c₀` quotients are in code: `lp.inftyCStarAlgebra` (the bounded product of nonzero unital C*-algebras is a unital C*-algebra, TauCeti/Analysis/CStarAlgebra/BoundedProduct.lean), `lp.c0Ideal` closed and star-closed with quotient norm `limsup_i ‖a_i‖` (`lp.isClosed_c0Ideal`, `lp.star_mem_c0Ideal`, `lp.norm_mk_c0Ideal`, TauCeti/Analysis/Normed/Lp/C0Ideal.lean), so `∏ M_{k_n} / ⊕ M_{k_n}` is a C*-algebra. Missing: C*-inductive limits with their universal property and norm formula (needed for AF algebras), `c₀` direct sums as C*-algebras with universal properties, `C*(F_∞)`. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/39234 (C*-inductive limits of directed systems with the norm formula `‖of i a‖ = inf_{j ≥ i} ‖f i j a‖` and universal property `lift`, Analysis/CStarAlgebra/InductiveLimit.lean) and https://github.com/TauCetiProject/TauCeti/pull/43527 (`c₀` direct sums of C*-algebras and the universal property `lp.liftNonUnitalStarAlgHom` of the bounded product, Analysis/CStarAlgebra/C0DirectSum.lean).
- Ready now: yes (*Needs* "Mathlib `lp`; §1.3 (ideals and quotients)"; quotient by closed ideal present).
- Serves defs: 36
- Evidence: README l.1203 "### 5.4 Direct sums, products, inductive limits and the universal unitary algebra (C5.4)"; Tau Ceti commit dcb25a745 (#37764); grep for C*-algebra `DirectLimit`/inductive limit in TauCeti/Analysis/CStarAlgebra: only a comment in QuantumSpin/Interaction.lean.

### C6.1–C6.2 Nuclear maps and nuclearity characterizations
- Status: NOT-STARTED (no `IsNuclearContraction`).
- Ready now: no: C6.1 needs C4.1 (the definition alone is statable on Mathlib `→CP`); C6.2 needs §5.1–5.2, §6.1, V13b, V1, V4.
- Serves defs: 36
- Evidence: README l.1272 "### 6.1 Nuclear maps and nuclear algebras (C6.1)" (*Needs* "§4.1"), l.1297 "### 6.2 The equivalent characterizations of nuclearity (C6.2)"; grep `IsNuclear` empty.

### C7.1 Exactness
- Status: NOT-STARTED.
- Ready now: no: needs §5.1–5.2, §6.1–6.2, §3.2, VonNeumannAlgebras V13b.SpatialNorm.
- Serves defs: 36
- Evidence: README l.1455 "### 7.1 Exactness (C7.1)"; grep empty.

## TauCetiRoadmap/AmenableTracesOnCStarAlgebras
No STATUS.md (merged as roadmap PR #2260; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `IsTracialState`, `matrixTwoNorm`, `IsAmenableTrace`, `IsHypertrace` in Tau Ceti: no hits.

### §§1.1–1.2 Tracial states, `T(A)`, the trace kernel and faithfulness
- Status: NOT-STARTED. Inputs present: `TauCeti.CStarAction.trivial`, `isKMSState_zero_iff`, `kmsStates` with `convex_kmsStates`, `isCompact_kmsStates` (TauCeti/Analysis/CStarAlgebra/Action/{Basic,KMS/Basic,KMS/StateSpace}.lean), `LinearMap.traceRadical`, Mathlib `PositiveLinearMap.GNS`. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43146 implements §§1.1–1.2 (`PositiveContinuousLinearMap.IsTracialState`, `TauCeti.tracialStateSpace`, `traceKernel`, `IsFaithful`, State/Tracial/). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/38432 (Analysis/CStarAlgebra/TracialFunctional.lean: `PositiveTracialFunctional` and tracial states).
- Ready now: yes (*Needs* VonNeumannAlgebras V0 states, whose state space and GNS are in code); §1.3 follows #43146.
- Serves defs: 36
- Evidence: README l.503 "### 1.1 Tracial states and the tracial state space" (`IsTracialState` as the `0`-KMS condition of the trivial action), l.562 "### 1.2 The trace kernel, faithfulness and simplicity".

### §1.5 The normalized trace and 2-norm on matrix algebras
- Status: NOT-STARTED. Inputs present: `Matrix.frobeniusInnerProductSpace`, `Matrix.frobenius_inner_eq_trace_conjTranspose_mul` (TauCeti/Analysis/Matrix/Frobenius.lean), `LinearMap.existsUnique_trace_mul_eq`, `Matrix.mem_range_scalar_iff_trace_mul_mul_comm` (TauCeti/LinearAlgebra/Matrix/Trace/Duality.lean). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43495 (`CStarMatrix.normalizedTrace` and `CStarMatrix.normalizedTwoNorm` on `CStarMatrix n n ℂ`, Analysis/CStarAlgebra/Matrix/Trace.lean).
- Ready now: yes for `tr_k`, `matrixTwoNorm` and its inequalities, block and tensor laws; the bimodule identification `M_k ⊗ M_kᵒᵖ ≅ B(L²(M_k, tr_k))` needs CStarAlgebras C5.1 (not started).
- Serves defs: 36
- Evidence: README l.751 "### 1.5 The normalized trace and 2-norm on matrix algebras", *Needs* "§1.1; VonNeumannAlgebras V0, V3; CStarAlgebras C5.1 (uniqueness of the C*-norm on `M_n ⊙ A`)".

### §§2.1–2.2 Completely positive contractions into matrices, multiplicativity defects
- Status: NOT-STARTED.
- Ready now: no: §2.1 needs §1.5 and CStarAlgebras C4.1's unital extension of c.p.c. maps (missing; ready); §2.2 needs §2.1 and C4.2 Stinespring (not started).
- Serves defs: 36
- Evidence: README l.895 "### 2.1 Operations on completely positive contractions into matrices", *Needs* "§1.5; CStarAlgebras C4.1 (composition, unital extension, Kadison–Schwarz)"; l.963 "### 2.2 Multiplicativity defects and asymptotic multiplicative domains", *Needs* "§1.5, §2.1; CStarAlgebras C4.1, C4.2".

### §3.1, §3.2, §3.4 Amenable traces (Definition 36.3), nets, sequences and u.c.p. forms, pullback
- Status: NOT-STARTED.
- Ready now: no: §3.1 needs §§1.1–1.2 and §1.5 only; §3.2 needs §1.3, §1.6, §2.1 and C4.1's unital extension; §3.4 needs §§1.1–1.2, §3.1.
- Serves defs: 36 (§3.1 is the definition)
- Evidence: README l.1122 "### 3.1 The three approximation properties" (`IsAmenableTrace`, `AdmitsFaithfulAmenableTrace`), *Needs* "§1.1–§1.2, §1.5; Mathlib `CompletelyPositiveMap`, `CStarMatrix`"; l.1179 "### 3.2 Nets, sequences, unital maps and finite-dimensional approximants"; l.1248 "### 3.4 Pullback along star homomorphisms".

### §§4.1–4.4 Hypertraces and the Connes–Kirchberg theorem
- Status: NOT-STARTED.
- Ready now: no: §4.1 needs VonNeumannAlgebras V13a and CStarAlgebras C4.1's multiplicative domain; §4.4 needs §§1.4–1.5, 3.2, 4.1–4.3, CStarAlgebras C5.1–C5.2, VonNeumannAlgebras V13b.SpatialNorm.
- Serves defs: 36 (Prop 36.4(ii))
- Evidence: README l.1310 "### 4.1 Hypertraces and representation independence", l.1422 "### 4.4 The Connes–Kirchberg theorem", *Needs* l.1399 and l.1446.

### §§5.1–5.4 Nuclear maps, uniform amenable traces, nuclear and exact algebras
- Status: NOT-STARTED.
- Ready now: no: needs CStarAlgebras C6.1, C6.5, C7.1, C2.8, VonNeumannAlgebras V13a and §4.4, §4.6.
- Serves defs: 36 (Prop 36.4(iii))
- Evidence: README l.1702 "### 5.3 Nuclear C*-algebras", *Needs* "§3.2–§3.3, §5.1–§5.2; CStarAlgebras C6.1, C6.5"; l.1723 "### 5.4 Exact C*-algebras", *Needs* "§3.3, §4.4, §5.1–§5.2; CStarAlgebras C6.1, C7.1; VonNeumannAlgebras V13a".

### §7.2, §8.5 AF and UHF traces; subalgebras of simple unital AF algebras (Schafhauser)
- Status: NOT-STARTED.
- Ready now: no: §8.5 needs §1.2, §3.4, §6.3, §7.2, CStarAlgebras C6.5, C7.1, CStarClassification CL2; §7.2 needs CStarAlgebras C2.1 and CL2 (C*-inductive limits of C5.4 not in code).
- Serves defs: 36 (the cited paper's application)
- Evidence: README l.1981 "### 7.2 AF and UHF algebras", l.2272 "### 8.5 Subalgebras of simple unital AF algebras" (`subalgebra_isAF_simple`).

## TauCetiRoadmap/DerivedModuleAlgebra
STATUS.md snapshot: d9fbe7b 2026-11-11 (Tau Ceti checked at 91942aa9f, 2026-11-19)

### §0.4 The full cotangent complex and §0.8 transitivity triangle
- Status: NOT-STARTED. `Algebra.CotangentComplex` is absent. Only Mathlib's naive `Extension.cotangentComplex` is used. Inputs: the standard polynomial resolution stages and their varying-base maps exist (Algebra/Category/CommAlgCat/PolynomialResolution/{Basic,Map,Simplicial}.lean), but the resolution property does not.
- Ready now: no. §0.4 needs §0.1 (resolution property and the Lπ_! comparison missing) and §0.2 (derived tensor bifunctor and base-change adjunction missing; K-flat models exist). §0.8 needs §§0.4, 0.6 and 0.2.
- Serves defs: 27
- Evidence: README l.1271 "### 0.4 The full cotangent complex" (signature `Algebra.CotangentComplex (A B) : DerivedCategory (ModuleCat B)`); l.1463 "### 0.8 The cotangent transitivity triangle". STATUS Layer 2 remaining: "the full cotangent complex (§0.4) and everything built on it, §§0.6–0.25". Layer 1 remaining: "the derived tensor bifunctor and base-change adjunction, resolution comparison of §0.1 ...".

### §1.3 derived completion; §1.7 I-completely flat
- Status: NOT-STARTED for these sections; their input §1.2 is done. §1.2 in code: `TauCeti.derivedComplete` in D(A), the radical ideal `derivedCompleteIdeal`, generator and radical invariance, the module telescope criterion `TauCeti.IsDerivedComplete`, and the cohomology criterion `TauCeti.derivedComplete_iff_isDerivedComplete_homology` (every `Hⁿ(M)` derived complete, Stacks 091T), with closure under products, shifts and cones (RingTheory/AdicCompletion/DerivedComplete.lean, .../DerivedComplete/Module.lean). No `derivedCompletion` or `completeFlatness` in code.
- Ready now: §1.3: no, needs §1.1.1 derived Hom with the tensor–Hom adjunction (`derivedHom` exists, adjunction remaining). §1.7: no, needs §0.2's derived tensor bifunctor.
- Serves defs: 81
- Evidence: README l.2024 "### 1.2 Derived ideal completeness", l.2064 "### 1.3 The derived completion reflector", l.2359 "### 1.7 Complete flatness and complete faithful flatness". STATUS Layer 3 remaining (stale on the cohomology criterion, which is in code): "exactness of the derived limit, tensor–Hom adjunction, cohomology criterion for completeness, §§1.3–1.9".

## TauCetiRoadmap/DerivedDeRhamCohomology
Checked against the README at roadmap 890b66d (Tau Ceti checked at 91942aa9f, 2026-11-19).

### §5.8 the scheme cotangent complex `L_(X/A)` and derived de Rham on schemes
- Status: NOT-STARTED (grep `DerivedDeRham|deRhamSheaves` in TauCeti empty)
- Ready now: no: needs DerivedModuleAlgebra §0.4 (the full cotangent complex, not started), §0.11 and §0.2, and Layers 1–2 of this roadmap
- Serves defs: 27 (VirtualFundamentalClass §§3.1–3.4 consume it)
- Evidence: README l.4513 "### 5.8 Derived de Rham on schemes and formal schemes" ("let `L_(X/A)` be the complex of quasi-coherent sheaves with value `L_(B/A)` on affine opens"); VirtualFundamentalClass README "DerivedDeRhamCohomology §5.8 supplies the scheme cotangent complex".

## TauCetiRoadmap/EnhancedDerivedSheaves
STATUS.md snapshot: 385ec2d 2026-11-06 (Tau Ceti checked at 91942aa9f, 2026-11-19)

### §0.3 Derived tensor and internal Hom `ClassicalDerived.tensorHom` (with §0.4 functorCoherence)
- Status: PARTIAL, inputs only. The K-flat half of §0.2 exists: every unbounded complex of sheaves of modules has a K-flat resolution by flat terms (`CochainComplex.exists_quasiIso_isKFlat_sheafOfModules`, Algebra/Category/ModuleCat/Sheaf/TensorProduct/KFlat.lean). Tensoring with a fixed K-flat complex descends to the derived category (`CochainComplex.kFlatTensor`, Algebra/Homology/Monoidal/KFlat/DerivedTensor.lean). Missing: the derived tensor bifunctor on sheaves, internal RHom, the tensor–Hom adjunction, K-injective replacement on ringed sites, the enhanced category (§0.1) and all of §0.4.
- Ready now: no, as the README specifies it. §0.3 needs §§0.1–0.2, i.e. the enhanced category via the dg nerve, which needs E0.6 shift/cone comparison and E0.8 presentability, both remaining. A homotopy-category-level ⊗ᴸ on `DerivedCategory (SheafOfModules R)` from the existing K-flat resolutions could start now as a substep.
- Serves defs: 18, 27 (VirtualFundamentalClass §3.1 instantiates the ringed-site tensor and internal Hom on stack sites)
- Evidence: README l.455 "### 0.3 Tensor, internal Hom and derived limits" ("provide `ClassicalDerived.tensorHom`: K-flat replacement defines `⊗ᴸ_R` ..."). README l.492 "### 0.4 Coherent derived functors". STATUS Layer 0 remaining: "K-injective replacement on ringed sites, the enhanced module-sheaf category, derived tensor-Hom, derived limits, completion comparison, functor coherence".

## TauCetiRoadmap/GeometricTopology
STATUS.md snapshot: 7bb61fc 2026-11-16, generated against Tau Ceti aa6e43e (Tau Ceti checked at 91942aa9f, 2026-11-19)

### Layer 1.1 Smooth collars
- Status: PARTIAL: `TauCeti.SmoothCollar` (a `C^k` injective local diffeomorphism `∂M × [0, 1) → M` with zero slice the boundary inclusion) with `isOpenEmbedding`, `opensRange`, `diffeomorphOpensRange`, `reparam`, `isCollar`/`isCollared`, `ofIsEmpty` (Geometry/Manifold/Boundary/Collar/Smooth.lean); local smooth product collars `IsProductCollarChart.diffeomorphProd` (Collar/Diffeomorph.lean); topological collars. Missing: the existence theorem (Collar/Diffeomorph.lean's docstring: the global theorem "still requires patching these local diffeomorphisms along the whole boundary"), uniqueness up to isotopy, the interior as a boundaryless manifold.
- Ready now: no for existence: the flow route needs semiflows starting at boundary points (Mathlib integral curves exist only at interior points), which open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/40499 (forward semiflow of strictly inward vector fields in convex sets) supplies in charts. Open PRs https://github.com/TauCetiProject/TauCeti/pull/43621 (`SmoothCollar.shrink` to depth ε) and https://github.com/TauCetiProject/TauCeti/pull/38769 (the interior as a boundaryless manifold) cover two other 1.1 items.
- Serves defs: 66 (through RiemannianManifoldsWithConvexBoundary §§3.3–3.5, 4.4)
- Evidence: README l.788 "### 1.1 Smooth collars"; STATUS coverage Layer 1 remaining "general boundary collars, gluing along boundary pieces, handle attachment and embeddings of all compact surfaces in R^4"; grep `SmoothCollar`: only Collar/Smooth.lean, no existence statement.

### 1.3 Gluing along the boundary, the double, handle attachment
- Status: NOT-STARTED. Inputs in code: compatible open gluing of manifolds (`TopCat.GlueData.IsCompatible.isManifold`, Geometry/Manifold/Gluing/GlueData.lean) and the double of a charted space along an open subset (`TauCeti.isCompatible_doubleGlueData`, Gluing/Double.lean). No gluing of manifolds with boundary through collars, no double `M ∪_id M`, no handle attachment.
- Ready now: no: needs 1.1's smooth collar existence (partial) and 1.2 (complements of embedded balls).
- Serves defs: 66 (the collar extension and the double, through RiemannianManifoldsWithConvexBoundary §§3.3, 3.5), 59 (1.7 needs 1.3)
- Evidence: README l.851 "### 1.3 Gluing along the boundary and handle attachment" ("The double `M ∪_id M` is a boundaryless manifold containing `M` ..."; *Needs* "Tau Ceti `TauCeti.chartedSpaceOfIsOpenEmbedding`, `TauCeti.SmoothEmbedding`; Layer 1.1, Layer 1.2; DifferentialGeometry *Boundary and corners*"); STATUS coverage Layer 1 remaining "... gluing along boundary pieces, handle attachment ...".

### 1.7 / 1.7.2 Compact smooth surfaces, Mod(F)
- Status: PARTIAL: the mapping class group is in code, in every dimension: `TauCeti.MappingClassGroup I M` = `Diff(M, ∂M)` modulo the path component of the identity for compact `M`, with `mk`, `mk_eq_mk_iff`, `lift`, `mk_final_eq_one` and `Mod⁺` as `MappingClassGroup.orientationPreserving` (Geometry/Diffeomorphism/MappingClassGroup.lean), on `TauCeti.RelativeDiff` (Geometry/Diffeomorphism/FixingSubgroup/Basic.lean) and `TauCeti.Diffeotopy`. Missing: compact smooth surfaces (1.7), Dehn twists (the `DehnTwist` hits are group-theoretic HNN/pushout and limit-group files), `Mod(T²) ≅ GL₂(ℤ)`, Lickorish generation
- Ready now: no: the 1.7.2 theorems need 1.7, and 1.7 needs Layer 11.2.1 (partial), 1.2, 1.3 (missing), 1.3.1, 1.4 and 11.3
- Serves defs: 59
- Evidence: README l.1049 "### 1.7 Compact smooth surfaces" (*Needs* l.1096), l.1212 "### 1.7.2 Mapping class groups of compact surfaces and Dehn twists" (*Needs* l.1279 "Layer 1.5 ..., Layer 1.7 ..., Layer 3.1 ..., Layer 3.3 ..., Layer 3.4")

## TauCetiRoadmap/OperatorTheory/SelfAdjointSpectralTheory
STATUS.md snapshot: ad0502e 2026-11-16 (umbrella OperatorTheory/STATUS.md, generated against Tau Ceti aa6e43e; Tau Ceti checked at 91942aa9f, 2026-11-19)

### SA-E01, SA-E03–E07 Spectral PVM of an unbounded self-adjoint operator, projections, resolvent formula
- Status: NOT-STARTED (no `ProjValMeasure ℝ` built from a `LinearPMap`). Inputs present: unitary Cayley transform `IsSelfAdjoint.cayley_mem_unitary` (Analysis/InnerProductSpace/LinearPMap/Cayley.lean), bounded normal `ContinuousLinearMap.spectralPVM` (Analysis/InnerProductSpace/BorelCalculus/Basic.lean), reindexing `ProjValMeasure.map` (ProjValMeasure/Map.lean), resolvent API (LinearPMap/Resolvent.lean). Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/41596 (SA-E01 `LinearPMap.spectralPVM A hA : ProjValMeasure ℝ H` as the pushforward of the Cayley transform's spectral measure, with its characterising properties), https://github.com/TauCetiProject/TauCeti/pull/29129 (an earlier construction of the same Cayley spectral measure, Analysis/InnerProductSpace/LinearPMap/Spectral/Measure.lean) and https://github.com/TauCetiProject/TauCeti/pull/37560 (SA-E02 zero mass at `1`, `spectralPVM_proj_preimage_singleton_eq_zero`, LinearPMap/Cayley/Spectral.lean).
- Ready now: yes (Part D done, Part B PVM/Borel calculus and SA-B25 present; SA-E02 zero mass at 1 must be proved first). SA-E09 later needs Part C SA-C12–19 (Part C partial).
- Serves defs: 35, 45
- Evidence: README l.1202 "SA-E01: Spectral PVM of an unbounded self-adjoint operator", l.1208–1215 SA-E03..E07; STATUS Part E remaining "the unbounded spectral PVM, resolvent formula, generated group and Stone uniqueness"; Suggested.lean l.692 `spectralPVM (hA : IsSelfAdjoint A) : ProjValMeasure ℝ H := sorry`.

## TauCetiRoadmap/OperatorTheory/UnboundedOperators
Umbrella OperatorTheory/STATUS.md ad0502e 2026-11-16 lists all six UnboundedOperators layers as untouched; Tau Ceti checked at 91942aa9f, 2026-11-19. Only the scalar-measure step of UO-C03 and the real-scalar case of the UO-D06 representation theorem are in code (below): grep for `exists_spectralType_decomposition`, `essentialSpectrum`, `discreteSpectrum`, `existsUnique_maximal_multiplier`, `friedrichs` in TauCeti: no hits.

### UO-A01 (§1.1) Unbounded spectral integral
- Status: NOT-STARTED. Inputs present: `TauCeti.ProjValMeasure` with integral and diagonal measures (Analysis/InnerProductSpace/ProjValMeasure/, BorelCalculus/DiagonalMeasure.lean). Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/43205 and https://github.com/TauCetiProject/TauCeti/pull/40748 each implement `ProjValMeasure.spectralIntegral` with `existsUnique_spectralIntegral` (§§1.1–1.2); they duplicate each other.
- Ready now: partly: the PVM-side construction uses only Tau Ceti's `ProjValMeasure` API; the cited HilbertModules H6 graph-closure API is not started (Mathlib's `LinearPMap.closure` covers the Hilbert-space case).
- Serves defs: 35
- Evidence: README l.241 "### 1.1 Spectral-integral domain and action (UO-A01)", *Needs* l.245 "Tau Ceti's `TauCeti.ProjValMeasure` API ...; HilbertModules H6 graph closure".

### UO-C01, UO-C03 (§3.1, §3.3) Spectral projections and the pp/ac/sc decomposition
- Status: PARTIAL: UO-C03's scalar-measure step is in code: the unique split of an s-finite measure into atomic, absolutely continuous and singular continuous parts relative to a reference measure without atoms, `MeasureTheory.Measure.atomicPart_add_withDensity_rnDeriv_add_singularContinuousPart`, its uniqueness, and `not_isAtom_singularContinuousPart` (MeasureTheory/Measure/Decomposition/SingularContinuous.lean, on `atomicPart` in Decomposition/Atomic.lean). Missing: UO-C01, and the subspaces `H_pp`, `H_ac`, `H_sc` of a PVM with `exists_spectralType_decomposition`.
- Ready now: no: §3.1 needs §1.1, §1.5, §1.6; §3.3 needs §1.1, §3.1, SelfAdjointSpectralTheory SA-E06–E07 (not started, after SA-E01) and VonNeumannAlgebras V2.
- Serves defs: 35 (UO-C03 is its target), 45 (to state the paper's a.c. spectrum)
- Evidence: README l.523 "### 3.1 Approximate eigenvectors and spectral projections (UO-C01)", l.552 "### 3.3 Pure-point/absolutely-continuous/singular decomposition (UO-C03)" (headline `exists_spectralType_decomposition`).

### UO-C02 (§3.2) Essential and discrete spectrum
- Status: NOT-STARTED.
- Ready now: no: needs §3.1, HilbertModules H6 closed range (not started), OperatorKTheory §8.4 for the bounded comparison.
- Serves defs: 40
- Evidence: README l.533 "### 3.2 Essential spectrum (UO-C02)" (`discreteSpectrum`, `essentialSpectrum`, `notMem_essentialSpectrum_iff`).

### UO-D06 (§4.7) Closed forms and the Friedrichs extension
- Status: PARTIAL: the real-scalar representation theorem is in code for a bounded symmetric form on a real Hilbert space `V` that is coercive after a shift along a continuous dense-range `J : V → H`: the represented operator `IsCoercive.formOperator` with its graph characterization `mem_graph_formOperator_iff`, domain `mem_domain_formOperator_iff`, independence of the shift `formOperator_eq`, self-adjointness `isSelfAdjoint_formOperator`, the lower bound `neg_mul_norm_sq_le_inner_formOperator` and the resolvent `resolvent_formOperator_neg` (Analysis/InnerProductSpace/Variational/FormOperator.lean, Tau Ceti PR #42856), on the real coercive solution map `IsCoercive.formSolutionOperator`. Missing: the closed-form carrier and the coercive solution map over `[RCLike 𝕜]`, `existsUnique_selfAdjoint_of_closed_form`, the square-root form domain, the real spectral restriction, the Friedrichs extension `friedrichs_extension_extremal` and the sum-form theorem. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/41886 (the form representation theorem over `[RCLike 𝕜]`, `TauCeti.existsUnique_selfAdjoint_of_closed_form`, LinearPMap/ClosedForm.lean, with sesquilinear Lax–Milgram maps).
- Ready now: yes for the form representation theorem over `RCLike` (its *Needs* are Mathlib and Tau Ceti's complexification; the real case is in code); square roots need §1.1–§1.3 and SA-E01, and the real case GeneralizedCohomology G5.5-RealHilbert.
- Serves defs: 40 (and VariationalMethods Layer 2, on the chain of 34)
- Evidence: README l.703 "### 4.7 Closed forms and the Friedrichs extension (UO-D06)" ("Work uniformly over `[RCLike 𝕜]`", headline `existsUnique_selfAdjoint_of_closed_form`), *Needs* l.819.

### UO-A07, UO-E04–E06 (§1.7, §§5.4–5.7) Maximal multipliers, Kato–Rellich, cores, the free Laplacian on ℝ³
- Status: NOT-STARTED. Inputs present: Kato–Rellich `IsSelfAdjoint.add_of_isRelativelyBounded` (SA-C55), bounded multiplication operators on `Lᵖ` (MeasureTheory/Function/Lp/Multiplication.lean, Analysis/Semigroups/Multiplication/). Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/42114 (UO-A07 maximal unbounded multiplication operators on `Lp`, `existsUnique_maximalMultiplication`, MeasureTheory/Function/Lp/MaximalMultiplication/) and https://github.com/TauCetiProject/TauCeti/pull/43512 (the relatively compact half of UO-E04, `LinearPMap.IsRelativelyCompact`, `isRelativelyCompact_iff_isCompactOperator_compResolvent`).
- Ready now: yes for UO-A07's existence and self-adjointness headline `existsUnique_maximal_multiplier` (Mathlib `Lp`, `MemLp`; the V10 cyclic-model comparison and intertwining identities wait on V10 and §1.1–§1.3); UO-E06 needs §5.4 and §5.6, which need §3.2 and §5.1–§5.3.
- Serves defs: 45 (UO-E06 specifies it for d = 3 only; the free Laplacian on ℝ^d is UO-A07 conjugated by the Fourier transform)
- Evidence: README l.309 "### 1.7 Multiplier model (UO-A07)", l.983 "### 5.4 Kato–Rellich and relatively compact perturbations (UO-E04)", l.1033 "### 5.7 Three-dimensional L²+L∞ potentials (UO-E06)" ("This is an ℝ³ theorem ... the statement is not extended to ℝⁿ").

## TauCetiRoadmap/VariationalMethods
STATUS.md snapshot: fac70b1 2026-11-14, generated against Tau Ceti aa6e43e (Tau Ceti checked at 91942aa9f, 2026-11-19; grep `CompactFormPair`, `rayleighMinMax`: no hits). STATUS lists Layer 1 as partial and Layers 2–6 as untouched.

### §3.1, §§4.1–4.4 Compact form pairs, successive minima, Courant–Fischer on the form domain
- Status: NOT-STARTED. Inputs present: Courant–Fischer for compact self-adjoint operators (Analysis/InnerProductSpace/CourantFischer.lean), Rayleigh quotients and variational spectrum (Analysis/InnerProductSpace/Variational/{Rayleigh,Spectrum}.lean), direct method (Analysis/Variational/DirectMethod.lean), and §1.3's weak-to-norm continuity of a compact operator on bounded sets (`IsCompactOperator.continuousOn_comp_toWeakSpace_symm_of_isBounded`, `IsCompactOperator.isSeqClosed_toWeakSpace_preimage`, Analysis/Normed/Operator/Compact/WeakSpace.lean) with the non-closedness of the unit sphere in the weak topology (`TauCeti.not_isClosed_toWeakSpace_setOf_norm_eq`, Analysis/Normed/Module/WeakSpace/Sphere.lean).
- Ready now: no: Layer 3 needs Layers 1–2, and Layer 2 consumes UnboundedOperators UO-D06's coercive solution map over `[RCLike 𝕜]` (UO-D06 is partial: only the real `IsCoercive.formSolutionOperator` and `IsCoercive.formOperator` are in code); Layer 1 (direct method) is ready.
- Serves defs: 34 (min–max formula of Thm 34.2, 34.4(c); the Neumann spectrum itself is PR #1614)
- Evidence: README l.562 "### 3.1 Compact form pairs", l.782 "### 4.4 Courant–Fischer on the form domain" (`CompactFormPair.eigenvalue_eq_rayleighMinMax`); Layer 2 Dependencies "UnboundedOperators UO-D06 (coercive solution over `𝕜`)".

## TauCetiRoadmap/PseudodifferentialOperators
STATUS.md snapshot: 49adf64 2026-11-16, generated against Tau Ceti aa6e43e (Tau Ceti checked at 91942aa9f, 2026-11-19)

### §5.4 Compact-base C^{k,α} Hölder spaces
- Status: PARTIAL: for a fixed compact chart atlas `A : TauCeti.CompactChartAtlas I M`, the vector-valued space `TauCeti.CompactChartAtlas.CkHolderSpace A k α F` with norm = finite-atlas `C^k` norm + chart Hölder seminorms of the `k`th coordinate derivatives (`CkHolderSpace.norm_def`, `ContMDiffMap.chartHolderNorm`), and its completeness on boundaryless `M` (`CkHolderSpace.instCompleteSpace`), TauCeti/Geometry/Manifold/ContMDiffMap/Chart/Holder.lean. Euclidean inputs: the Hölder spaces `C^{k,α}(Ω)` on an open set, `TauCeti.CkHolderSpaceOn`, Banach for a Banach codomain (Analysis/Holder/OpenSet.lean), and the identification of the non-integer-order Hölder–Zygmund space with the bounded Hölder space `TauCeti.BesovSpace.ckHolderSpaceEquiv` (Analysis/Holder/Zygmund.lean). Missing: the comparison of two atlases (the file says it is not included), bundle `C^(k,α)` norms by connection comparisons, Zygmund `C^r_*`, the mapping theorems and the identification `C^(k+α)_* = C^(k,α)`. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/40847 (atlas independence of `C^{k,α}(M, F)` on a compact boundaryless manifold, Chart/Holder/Atlas.lean, with the Hölder chain rule `exists_holderOnWith_iteratedFDerivWithin_comp`).
- Ready now: yes for the atlas comparison (finite-atlas `C^k` comparison `ContMDiffMap.exists_finiteAtlasSeminorm_le` and the Hölder file exist); the Zygmund and mapping parts: no, they need P2–P4 (partial) and §5.3 Besov estimates.
- Serves defs: 32
- Evidence: README l.1337 "### 5.4 Hölder, Zygmund and little Hölder spaces", "Supply the compact-base bundle C^(k,α) norms by chart/connection comparisons"; *Needs* l.1428; Tau Ceti commit 97ec502a0 (#37238); STATUS coverage Layer 5 remaining "... Zygmund mapping ..."

### P7 §7.1 and P7a §8.1 Scalar self-adjoint Laplacian realization on closed manifolds
- Status: NOT-STARTED. Layer 6 has ellipticity, parametrix symbols, interior regularity and estimates for localized operators on Sobolev data, and interior elliptic regularity of differential operators on arbitrary distributions on open subsets of `ℝⁿ` (`Distribution.IsLocallySobolevAt.of_sum_smul_smulLeftCLM_iteratedLineDerivOp`, Analysis/Pseudodifferential/DistributionalRegularity.lean); Layers 7 and 8 are preparatory (polar decomposition and normalization of elliptic symbols, equivariant Fredholm multiplicities, parameter-dependent symbols; equal eigenspace multiplicities for almost-conjugate subgroups). No closed-manifold Laplacian `LinearPMap` in TauCeti/Geometry
- Ready now: no: §7.1 needs P6's patched global parametrix and Fredholm theory on compact bases (missing) and K5a's realization (CKG §5.7, not started). §8.1 needs RiemannianGeometry R4.7, P5 density, P6 and P7
- Serves defs: 40
- Evidence: README l.1600 "### 7.1 Powers and their Sobolev domains" ("Consume K5a's generic nonnegative Laplace-system self-adjoint H² realization"), l.1935 "### 8.1 Quotients and the scalar realization" (*Needs* l.1981); STATUS coverage Layer 6 remaining "regularity for arbitrary distributions, patched global parametrix, Fredholm theory on compact bases", Layer 8 remaining "scalar Laplacian H^2 realization, normalized pullback on H^2, isospectrality"; prose "Layers 7 and 8 are preparatory"

## TauCetiRoadmap/SobolevMapsBetweenManifolds
No STATUS.md; Tau Ceti checked at 91942aa9f, 2026-11-19 (grep `IsSobolevMap`, `HasWeakMFDeriv`, `orientedJacobian`, `MemW1pLocM`: no hits). Its inputs in code: Euclidean `TauCeti.HasWeakFDerivOn` with chain rule and change of variables, planar `MemLpLoc`/`MemWkpLoc` (Analysis/Sobolev/Local/), chartwise null sets `TauCeti.IsNullSet`, Riemannian volume, orientations, and the two-dimensional-source class `TauCeti.MemWkpLocMap` of PseudoholomorphicCurveAnalysis PH4.1 (Geometry/Manifold/Sobolev/LocalMap.lean, chart independence for `k ≤ 1` in LocalMap/Atlas.lean, locality `TauCeti.memWkpLocMapOnGroupoid_iff_locally` in LocalMap/Locality.lean).

### Layer 1 (§§1.1–1.2) `MemLpLoc`, `W^{1,p}_loc(Ω; F)` on open subsets of finite-dimensional real normed spaces
- Status: NOT-STARTED (`MemLpLoc`, `MemWkpLoc` take `U : Set ℂ`, Analysis/Sobolev/Local/Basic.lean). Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/43530, https://github.com/TauCetiProject/TauCeti/pull/43087, https://github.com/TauCetiProject/TauCeti/pull/41136 and https://github.com/TauCetiProject/TauCeti/pull/40283 (competing implementations of §§1.1–1.2: `MemLpLoc` and `MemWkpLoc`, or `MemW1pLoc` in #41136, on finite-dimensional real normed spaces, Analysis/Sobolev/Local/).
- Ready now: yes (*Needs* Tau Ceti `TauCeti.HasWeakFDerivOn` and its a.e. uniqueness, present).
- Serves defs: 47 (and 41, 42 through it)
- Evidence: README l.344 "### 1.1 Local Lebesgue and Sobolev classes", l.386 "### 1.2 The first-order class `W^{1,p}_loc(Ω; F)`".

### Layer 2 (§§2.1–2.3) chain rules, change of variables, local mollification
- Status: NOT-STARTED in every dimension; the planar `MemWkpLoc.contDiffOn_comp`, `MemWkpLoc.comp_contDiffOn_diffeo` and the Euclidean `HasWeakFDerivOn.contDiffOn_comp`, `HasWeakFDerivOn.comp_contDiffOn_diffeo` exist.
- Ready now: no: needs §1.2 (§2.3 first, then §2.1–§2.2).
- Serves defs: 47 (Proposition 47.1), 41, 42
- Evidence: README l.438 "### 2.1 Chain rules and the composition operator", l.489 "### 2.2 Change of variables", l.518 "### 2.3 Local mollification"; *Needs* l.486, l.513 "§1.2, §2.3".

### Layer 3 (§§3.1–3.2) the almost-everywhere filter, measurability and `L^p_loc` on a manifold
- Status: NOT-STARTED. `TauCeti.IsNullSet` and `TauCeti.isNullSet_iff_riemannianVolume_eq_zero` exist; images of null sets under differentiable maps `TauCeti.IsNullSet.image_of_mdifferentiableOn` (Geometry/Manifold/Measure/Differentiable.lean) cover the first claim of §3.3. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/40842 (Geometry/Manifold/Measure/AE.lean: §3.1 the almost-everywhere filter `ae` on a manifold).
- Ready now: no: §3.1 needs §2.2; §3.2 needs §1.1, §2.2, §3.1.
- Serves defs: 47, 41, 42
- Evidence: README l.634 "### 3.1 Null sets, positive densities and the almost-everywhere filter" (*Needs* l.675 "§2.2; Tau Ceti `TauCeti.IsNullSet`"), l.679 "### 3.2 Measurability and local `Lᵖ`", l.722 "### 3.3 Null sets under `C¹` maps".

### Layer 4 (§§4.1–4.3) Sobolev functions on `M`, the class `IsSobolevMap`, the weak differential `HasWeakMFDeriv`
- Status: NOT-STARTED for finite-dimensional sources in general; for Riemann-surface sources the class (without `Df`) is `TauCeti.MemWkpLocMap`.
- Ready now: no: needs §1.2, §2.1, §2.2, §3.1, §3.2.
- Serves defs: 47 (47.3(a)–(b), Proposition 47.2), 41, 42
- Evidence: README l.755 "### 4.1 Sobolev functions on a manifold", l.779 "### 4.2 The class `W^{1,p}_loc(M, N)`" (*Needs* l.809), l.811 "### 4.3 The weak differential" (*Needs* l.837).

### §5.1, §§6.1–6.2 `‖Df‖` and the Jacobian `J_f`
- Status: NOT-STARTED.
- Ready now: §6.1 (`orientedJacobian` of a linear map between oriented inner product spaces): yes (*Needs* only Mathlib `Orientation.volumeForm`, `LinearMap.normDet`); §5.1 and §6.2: no, they need §3.2 and §4.3.
- Serves defs: 47 (47.3(c)–(d)), 41, 42
- Evidence: README l.1009 "### 5.1 The norm `‖Df‖`" (*Needs* l.1048 "§3.2, §4.3"), l.1173 "### 6.1 The oriented Jacobian of a linear map" (*Needs* l.1197), l.1201 "### 6.2 The Jacobian of a Sobolev map" (*Needs* l.1227).

## TauCetiRoadmap/PseudoholomorphicCurveAnalysis
STATUS.md snapshot: 1928c2e 2026-11-14, describing Tau Ceti to aa6e43e 2026-11-13 (Tau Ceti checked at 91942aa9f, 2026-11-19; the Schottky double, which STATUS lists as remaining, is in code)

### PH6.1 Sobolev sections over compact surfaces with boundary
- Status: PARTIAL: a generic boundaryless bundle carrier `TauCeti.SobolevSection A μ p k` (`W^{k,p}(V)` over a `FiniteBundleAtlas`, closedness/completeness, `lowerOrderL`) exists in TauCeti/Geometry/Manifold/VectorBundle/Sobolev/{Basic,ContMDiffSection,SMul}.lean, and for surfaces modelled on `ℂ` its chart readings are the local classes `MemWkpLoc` and conversely (`TauCeti.SobolevSection.memWkpLoc_coord`, `exists_ae_eq_coord_of_memWkpLoc`, Sobolev/Local.lean), in arbitrary bundle charts rather than isothermal ones, with Morrey's embedding for `p > 2` (Sobolev/Morrey.lean), Rellich compactness for the boundaryless carrier `TauCeti.SobolevSection.isCompactOperator_lowerOrderL` (Sobolev/Rellich.lean) and chart transfer `FiniteBundleAtlas.transferL`, `restrictL_eq_transferL` (Sobolev/Transfer.lean). For `∂Σ ≠ ∅`, `TauCeti.BorderedSobolevSection` over a half-plane `FiniteBundleAtlas` (FiniteBundleAtlas/HalfPlane.lean) is complete, contains the `Cᵏ` sections and is closed under multiplication by smooth functions (Sobolev/Bordered/{Basic,SMul}.lean). First-order Morrey up to the boundary is in code: for `2 < p`, every element of `W^{1,p}(V)` has a unique continuous representative `TauCeti.BorderedSobolevSection.toSection` (`existsUnique_continuous_ae_eq_halfCoord`), with Hölder chart expressions up to the real axis (`exists_holderOnWith_halfCoord_toSection`) (Sobolev/Bordered/Morrey.lean, Tau Ceti PR #39414). Missing: norm independence of the atlas, density of smooth sections, Rellich up to the boundary, higher-order Morrey and multiplication by `W^{k,p}` coefficients for kp>2, the totally real boundary subspace `W^{k,p}_F`, comparison with P5.2 on interior subsurfaces.
- Ready now: no: needs PH2.4 isothermal coordinates/bordered atlas (partial: planar isothermal charts from the Beltrami solution with holomorphic transitions, Analysis/Complex/Beltrami/Transition.lean and Geometry/Manifold/Complex/Isothermal.lean, but no bordered isothermal atlas), PH1.2 Morrey/algebra/composition at higher order (partial: first-order chain rule and multiplication in Analysis/Sobolev/Local/{ChainRule,Multiplication}.lean; the half-disc higher-order reflection with its weak derivative `HasWeakFDerivOn.planarReflection` is in Local/Reflection.lean), PDE Lane A item 6 trace; the boundaryless sub-case could start against the existing carrier.
- Serves defs: 56, 60
- Evidence: README l.1045 "### 6.1 Sobolev sections over compact surfaces with boundary"; STATUS Layer 6 remaining "Fredholm property, duality and agreement with the smooth theory for real Cauchy–Riemann operators", Layer 1 remaining "higher-order Morrey and Rellich up to the half-disc boundary; continuity of composition above order one"; grep `SobolevSection` hits the bundle files above (Sobolev/ and Sobolev/Bordered/).

### PH6.2 Real Cauchy–Riemann operators
- Status: PARTIAL: the smooth half is in code: `TauCeti.IsRealCauchyRiemannOperator` (Leibniz-rule definition), `difference`/`isZeroOneForm_difference` (two operators differ by a zeroth-order (0,1)-form), `add_zeroOrder`, complex-linear part `sectionComplexLinearPart` + `antilinearPart` with uniqueness (MS Ex. C.1.7), and `IsCovariantDerivativeOn.isRealCauchyRiemannOperator_zeroOnePart` (a complex connection gives `(∇)^{0,1}`), in TauCeti/Geometry/Manifold/VectorBundle/CauchyRiemann/{Basic,Connection}.lean, with local-frame readings, direct sums, transport, straight lines and holomorphic frames (CauchyRiemann/{LocalFrame,Constructions,HolomorphicFrame}.lean); the boundaryless target space of Sobolev `(0,1)`-forms `TauCeti.zeroOneSobolevSections` with its projection (Sobolev/ZeroOneForm.lean); weak real CR equations with Sobolev coefficients (Analysis/Complex/CauchyRiemann/RoughCoefficients/Weak.lean) and the formal adjoint of such an operator as a reflected real CR operator (`TauCeti.crFormalAdjoint_crReflectedAdjoint`, RoughCoefficients/Adjoint.lean). The chart calculus `(D s)ᵢ = ∂̄ sᵢ + Zᵢ sᵢ` with `TauCeti.FiniteBundleAtlas.chartZeroOrder`: `coord_tangentHom_eq_complexAntilinearPartL_fderiv_add_chartZeroOrder`, overlap law `complexAntilinearPartL_fderiv_coordChangeL_add_chartZeroOrder`, `contDiffOn_chartZeroOrder`, `exists_norm_chartZeroOrder_apply_le` (Geometry/Manifold/VectorBundle/CauchyRiemann/Chart.lean). Missing: operators of class `W^{ℓ−1,p}` (`D = D₀ + α`), the realizations `W^{ℓ,p} → W^{ℓ−1,p}`, the totally real boundary condition `F`. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/42721 (the boundaryless realization `IsRealCauchyRiemannOperator.sobolevL : SobolevSection A μ p 1 →L[ℝ] zeroOneSobolevSections A μ p 0`, VectorBundle/Sobolev/CauchyRiemann.lean) and https://github.com/TauCetiProject/TauCeti/pull/35116 (the planar Checks of PH6.2).
- Ready now: yes for the boundaryless realization of a smooth operator (`SobolevSection`, `zeroOneSobolevSections` and the chart calculus exist); no for the bordered case and `F`, which need PH6.1.
- Serves defs: 56, 60
- Evidence: README l.1083 "### 6.2 Real Cauchy–Riemann operators"; STATUS Layer 6 "partial"; grep `IsRealCauchyRiemannOperator` -> CauchyRiemann/Basic.lean (496 lines), Connection.lean.

### PH6.3 Fredholm property, kernel and cokernel
- Status: NOT-STARTED (generic Fredholm library exists: TauCeti/Analysis/Fredholm/*, incl. Adjoint, CompactPerturbation, DeterminantLine with its bundle and path transport of orientations, and two-out-of-three with index additivity along maps of short exact sequences, Analysis/Fredholm/Snake.lean; the vector similarity principle with the constant structure `i` for continuous weak solutions with locally `Lᵖ` coefficients, `p > 2`, `TauCeti.exists_similarity_of_hasWeakConjWirtingerDerivOn`, with unique continuation and isolated zeros, Analysis/Complex/CauchyRiemann/Similarity.lean; nothing CR-specific on bundles).
- Ready now: no: needs PH6.1–6.2 Sobolev realizations, PH3.3–3.5 (Sobolev-coefficient and boundary estimates, the `W^{1,p}` vector similarity principle with variable `J`; only the constant-`i` similarity principle is in code), PH4.1, PH2.4.
- Serves defs: 56, 60
- Evidence: README l.1128 "### 6.3 Fredholm property, kernel and cokernel"; deps l.1215 "PH1 (through PH6.1's localizations), PH2.4, PH3.3–PH3.5, PH4.1"; STATUS Layer 3 remaining "Sobolev-coefficient estimates (3.3), boundary estimates (3.4), vector similarity principle (3.5)".

### PH7 (7.1 Maslov index of a bundle pair, 7.2 Riemann–Roch)
- Status: PARTIAL (ingredients only): loop Maslov index `TotallyRealLoop.maslovIndex`, `maslovIndex_map/_prod/_rotation`, loop concatenation and base-point invariance in TauCeti/LinearAlgebra/TotallyReal/Maslov/*.lean, with its agreement with Souriau's Robbin–Salamon index of a path of unitary frames, `Matrix.UnitaryGroup.maslovIndex_realImageLoop` (Analysis/Matrix/UnitaryGroup/Maslov/Loop.lean); the Robbin–Salamon crossing-form formula for paths of Lagrangian graphs (`Matrix.UnitaryGroup.maslovIndex_eq_crossingForm_add_finsum_of_souriau_eq_cayley`, Analysis/Matrix/UnitaryGroup/Maslov/Crossing.lean); the zero axiom for paths `Matrix.UnitaryGroup.maslovIndex_eq_zero_of_rootMultiplicity_eq`, `maslovIndex_eq_zero_of_forall_not_isRoot`, `Matrix.det_eq_neg_one_pow_mul_exp_spectralAngleSum` (Analysis/Matrix/UnitaryGroup/Maslov.lean); the disc model of 7.2, the cokernel of `∂̄` with rotating-line boundary of Maslov index `k` of real dimension `max (−1 − k) 0`, `TauCeti.exists_conjWirtingerDeriv_eq_and_eq_zpow_mul_conj_iff` (Analysis/Complex/UnitDisc/Cokernel.lean); STATUS also cites nowhere-vanishing sections in high rank and Hermitian metrics. No doubled bundle `E_F`, no `μ(E,F)`, no index formula.
- Ready now: no: 7.1 needs CharacteristicClasses C3.2's `c₁` (its other input, PH2.4's Schottky double as a compact Riemann surface with the antiholomorphic involution, is in code: `TauCeti.SchottkyDouble`, `SchottkyDouble.doubleChart`, Geometry/Manifold/Complex/BorderedHolomorphic/SchottkyDouble.lean); 7.2 needs PH6 (incl. 6.3) and PH3.5, plus CharacteristicClasses C2.3/C3.2 and AlgebraicTopology Stage 6/7.1/8.7.
- Serves defs: 56, 60
- Evidence: README l.1223 "### 7.1 Maslov index of a bundle pair", l.1271 "### 7.2 Riemann–Roch" ("prove `ind_ℝ D = nχ(Σ) + μ(E, F)`"); STATUS Layer 7 remaining "Maslov index of a bundle pair and Riemann–Roch; only model-case index computations exist".

## TauCetiRoadmap/AnalyticStableMaps
No STATUS.md (merged as roadmap PR #987; Tau Ceti checked at 91942aa9f, 2026-11-19).

### §§0.1–0.2 The Cauchy–Riemann section, energy and virtual dimension; the linearized operator D_u and the closed index
- Status: NOT-STARTED (inputs only: the local CR linearization `cauchyRiemannLinearization` with coordinate covariance, Geometry/Symplectic/JHolomorphic/{Linearization,Naturality}.lean; `IsPseudoholomorphic`, `stdComplexLineEnergy`, `SmoothTwoForm.Tames`; chart-level invariance of `stdComplexLineEnergy` under holomorphic changes of coordinate and its scaling by `d` under `z ↦ z ^ d`, `SymplecticForm.stdComplexLineEnergy_restrict_image`, `SymplecticForm.stdComplexLineEnergy_restrict_preimage_realChart_pow`, JHolomorphic/Energy/Conformal.lean).
- Ready now: no: §0.1 needs HeegaardFloer F2.6c, DifferentialGeometry 8.3–8.5 and CharacteristicClasses C3; §0.2 needs §0.1 and PseudoholomorphicCurveAnalysis PH6.2–PH6.3, PH7.2.
- Serves defs: 56 (target: §0.2 is Definition 56.3), 60
- Evidence: README l.120 "### 0.1 The Cauchy–Riemann section, energy, area and the virtual dimension", l.138 "### 0.2 The linearized operator and the closed index" (*Needs* "§0.1; PseudoholomorphicCurveAnalysis PH6.2–PH6.3, PH7.2; CharacteristicClasses C3; ...").

### §0.4 Finite exceptional sets of a nonconstant closed curve (with §0.5 normalization)
- Status: NOT-STARTED. Input present: the point-preimage half of McDuff–Salamon Lemma 2.4.1 for a `C¹` solution of `∂ₜu = J(u) ∂ₛu` on an open subset of `ℂ`: unique continuation, discrete preimages of points with finitely many in each compact set, and finite positive local orders (`TauCeti.eqOn_const_of_cauchyRiemann_of_forall_isBigO`, `TauCeti.finite_inter_preimage_singleton_of_cauchyRiemann`, `TauCeti.exists_isTheta_pow_of_cauchyRiemann`, Geometry/Symplectic/JHolomorphic/UniqueContinuation.lean); the file states that the corresponding result for critical points is not proved.
- Ready now: no: needs HeegaardFloer F2.2a (finiteness of `Crit(u)` and of fibres on a closed source) and F2.3.
- Serves defs: 60 (60.1)
- Evidence: README l.170 "### 0.4 Finite exceptional sets and compact-image localization", l.182 "### 0.5 Normalization of a nonconstant closed curve through a simple curve".

### §2.1 Completely metrizable smooth-J topology, Baire property, density in J^ℓ
- Status: PARTIAL: for sections of a smooth vector bundle over a Lindelöf boundaryless base, the compact derivative topology is completely metrizable and Baire (`ContMDiffSection.isCompletelyMetrizableSpace_frameTopology`, `baireSpace_frameTopology`, Geometry/Manifold/VectorBundle/Section/CompletelyMetrizable.lean, Tau Ceti PR #38626), on `ContMDiffSection.completeSpace_frameTopology` (Section/Complete.lean); `SmoothAlmostComplexStructure.frameTopology` with `isClosedEmbedding_toEndomorphism_frameTopology`, `isClosed_setOf_invariant_tames_frameTopology`, `secondCountableTopology_frameTopology_of_sigmaCompactDomains` (Section/SecondCountable.lean). Missing: the Baire property of the spaces of smooth tame and compatible J themselves, density in `J^ℓ`, and the tangent spaces. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43517 (smooth, tame and compatible almost complex structures with `SmoothAlmostComplexStructure.frameTopology` are completely metrizable and Baire, AlmostComplex/CompletelyMetrizable.lean).
- Ready now: yes for the Baire property of smooth tame and compatible J (a closed subspace of the completely metrizable section space); no for density in `J^ℓ` and tangent-space statements (need HeegaardFloer F0.5, partial).
- Serves defs: 63 (63.4(b))
- Evidence: README l.266 "### 2.1 Finite-regularity parameter spaces and the smooth-J topology".

## TauCetiRoadmap/FukayaTheory
No STATUS.md (merged as roadmap PR #1045; Tau Ceti checked at 91942aa9f, 2026-11-19).

### FK2.2 Nonlinear CR section and linearization (polygons with Lagrangian boundary)
- Status: NOT-STARTED (inputs only: local `cauchyRiemannLinearization` with coordinate covariance, JHolomorphic/{Linearization,Naturality}.lean; cylinder Floer operator `floerSobolevOperator`, Floer/SobolevRealization.lean).
- Ready now: no: needs PH6.1, PH6.3, PH7.2, PH3, HeegaardFloer F0.0, F1.1–F1.5.
- Serves defs: 56 (bordered analogue of D_u; implicit)
- Evidence: README l.354 "### 2.2 Nonlinear CR section and linearization (FK2.2)"; *Needs* l.376.

## TauCetiRoadmap/AdicEtaleGeometry
STATUS.md snapshot: 39df4ea 2026-11-16, generated against Tau Ceti aa6e43e (Tau Ceti checked at 91942aa9f, 2026-11-19)

### Layer A0 Completed tensor products and fibre products
- Status: PARTIAL. In code: `Huber.IsCompletedPushout` and the Huber-pair `completedTensor` (RingTheory/Huber/TensorProduct/{Pushout,Pair,Plus,UniversalProperty}.lean). Ring-level associativity, symmetry and unit (TensorProduct/{Associator,Symmetry,Unit}.lean; A0.7 at ring level). Rational localisation (TensorProduct/Rational.lean; A0.4 algebra). Finite étale base change (TensorProduct/FiniteEtale.lean; A0.5 algebra). Transitivity (BaseChange.lean). Affinoid fibre products `AdicSpace.affinoid_isPullback`, `affinoid_isPullback_of_isStablySheafyRing_left/right`, and Tate point lifting `exists_ofPair_completedTensor_point` (AlgebraicGeometry/AdicSpace/Pullback/Affinoid.lean). A0.8 in full: analytic points, the analytic locus `PreAdicSpace.analyticLocus` with `analyticLocus.ι`, `analyticLocus.lift`, `analyticLocus.range_ι` (AlgebraicGeometry/AdicSpace/PreAdicSpace/Analytic.lean), the cartesian restriction square for adic morphisms `IsAdic.isPullback_analyticLocusMap` (Morphisms/AnalyticLocus.lean), and `isAdic_iff_mapsTo_analyticPoints` (Morphisms/Adic.lean). Fibre products are local on the source, `TauCeti.AdicSpace.hasPullback_of_cover` (AlgebraicGeometry/AdicSpace/Pullback/Cover.lean). Missing: global fibre products for morphisms locally of finite type, `AdicSpace.FibreProduct.lift`/`ofPairPushout`, chart independence (A0.6), and the adic-space-level A0.4/A0.5/A0.7 comparisons. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/37807 (A0.4 at adic-space level: `PreAdicSpace.IsOpenImmersion.isPullback`, `PreAdicSpace.Hom.isPullback_restrictPreimage`, pullback along an open subspace is restriction) and https://github.com/TauCetiProject/TauCeti/pull/42605 (existence and base-change stability of fibre products of adic spaces in the adic case, AdicSpace/Pullback/).
- Ready now: yes for the A0.4/A0.5/A0.7 adic-space packaging. The glued fibre product depends on AdicSpacesPartII R0.7 existence (below).
- Serves defs: 22
- Evidence: README l.747 "## Layer A0: completed tensor products and the fibre products actually used". STATUS coverage Layer A0 remaining "geometric fibre product and maps into affinoids in A0.1, A0.2, A0.4, A0.6, symmetry and unit in A0.7, base change of the analytic locus"; prose "A0.8 is done apart from its base-change clause".

### A1.6 étale/finite étale sites, A1.7 geometric points, A1.14 change of base field
- Status: NOT-STARTED. No `AdicSpace.IsEtaleLocalDescription`, `AdicSpace.smallEtale` or `smallEtaleTopology` for adic spaces. What exists in A1: A1.0.0, A1.0.1, the morphism half of A1.0.3, and part of A1.2 (`finiteAlgebra.homEquiv`).
- Ready now: no. A1.6 needs *strongly-sheafy-huber-pair* (A1.1), *etale-morphism* and *etale-base-change* (A1.3–A1.5) and A0 pullbacks. A1.7 needs A1.6. A1.14 needs the pro-étale site (A1.10–A1.12, *proetale-coherence*), the etale-descent targets and AdicSpacesPartII R0.7/R0.19.
- Serves defs: 22
- Evidence: README l.3259 "### A1.6 the étale and finite étale sites" (*etale-site*, `AdicSpace.smallEtale X`); l.3670 "### A1.7 geometric points, enough points, strict localisations"; l.5511 "### A1.14 coherence and change of base field" (*etale-descent-along-algebraic-extension* l.5539, *proetale-field-extension-slice* l.5565). STATUS coverage Layer A1 remaining "A1.0.3a, Elkik A1.0.4 and A1.0.5, A1.1, finiteness and strong sheafiness in A1.2, A1.3 onward".

## TauCetiRoadmap/AdicSpacesPartII
STATUS.md snapshot: 1c6a1a4 2026-11-11 (Tau Ceti checked at 91942aa9f, 2026-11-19)

### R0.7 Fibre products (and R0.6 lft for rigid spaces)
- Status: PARTIAL. *valuation-amalgamation* (`ValuationSpectrum.exists_amalgamation`) is done. *affinoid-fibre-product* is in code (`TauCeti.AdicSpace.affinoid_isPullback`, `isPullback_ofPair_of_isCompletedPushout`, the unconditional version when one factor is stably sheafy and the other is topologically of finite type; AlgebraicGeometry/AdicSpace/Pullback/Affinoid.lean). The reduction of existence to an affinoid source is in code: fibre products exist once they exist over the members of an open cover of the source (`TauCeti.AdicSpace.hasPullback_of_cover`, AdicSpace/Pullback/Cover.lean). Missing: *fibre-product-along-finite-type* (the non-adic ascending-union case), the reduction on the base and target, *fibre-products-existence* (`hasPullback_of_finiteType`), `exists_pullback_point` and base-change stability. For "rigid space lft" (R0.6): `IsAdic`, `LocallyOfWeaklyFiniteType`, `LocallyOfPlusWeaklyFiniteType` and `QuasiCompact` exist (AdicSpace/Morphisms/), as does `TauCeti.AdicSpace.IsLocallyHuberStandard` (AdicSpace/PreAdicSpace/LocallyHuberStandard.lean, with Huber's standing class stable under rational localisation); finite presentation is missing. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/42605 (the adic branch of *fibre-products-existence* and base-change stability, AdicSpace/Pullback/{OpenImmersion,WeaklyFiniteType}.lean), https://github.com/TauCetiProject/TauCeti/pull/40900 (R0.3 *completed-tensor-rational-localisation*: completed rational localisation commutes with completed tensor products, Spa/TensorProduct/Rational.lean) and https://github.com/TauCetiProject/TauCeti/pull/41312 (R0.6 `TauCeti.AdicSpace.LocallyOfFiniteType`, `LocallyOfFinitePresentation`, AdicSpace/Morphisms/FinitePresentation/).
- Ready now: yes for gluing affinoid fibre products to *fibre-products-existence* in the lft-over-stably-sheafy case (the gluing step uses the Huber-pair rational-localisation comparison of R0.3, whose ring-level form is RingTheory/Huber/TensorProduct/Rational.lean). The non-adic case needs R0.6 completion. R0.2 sheafiness for noetherian rings of definition (*noetherian-type-stably-sheafy*, partial) remains a prerequisite for the noetherian-type charts.
- Serves defs: 22
- Evidence: README l.3557 "### R0.7 fibre products" (*affinoid-fibre-product* at ~l.3622, *fibre-products-existence* at ~l.3702). *fibre-products-existence* Needs l.3736 (*affinoid-fibre-product*, *fibre-product-along-finite-type*, *adic-iff-analytic-locus*, *noetherian-type-stably-sheafy*, ...). STATUS remaining: "non-affinoid fibre products (R0.7)", with "The Huber-pair form of the rational-localisation comparison (R0.3) is a prerequisite".

## TauCetiRoadmap/AdicSpacesPartIV
STATUS.md snapshot: 7ca783d 2026-11-09 (Tau Ceti checked at 91942aa9f, 2026-11-19)

### R4.1–R4.6 étale sites on analytic adic spaces, rigid comparison, geometric points
- Status: NOT-STARTED for the site theory. Only R4.7 algebraic normal-crossings charts and the punctured-disc noncompactness check exist.
- Ready now: no. R4 re-exports AdicEtaleGeometry A1's *etale-site* (not started) onto R0/R1 carriers. R4.4's rigid comparison also needs AdicSpacesPartII R1 (untouched).
- Serves defs: 22
- Evidence: README l.562 "## Layer R4: étale and pro-étale sites"; l.583 "### R4.1 the étale site on the analytic carriers"; l.727 "### R4.4 rigid comparison"; l.827 "### R4.6 geometric points and pullback". The Checks at l.1712 have Sh(X_ét) ≃ continuous Gal(K^sep/K)-sets via ξ. STATUS remaining: "the étale and pro-étale sites, nu, rigid comparison and geometric points".

## TauCetiRoadmap/CharacteristicClasses
STATUS.md snapshot: 2bec3fc 2026-11-09 (to Tau Ceti d92acc5; Tau Ceti checked at 91942aa9f, 2026-11-19)

### C4 Chern–Weil forms
- Status: NOT-STARTED (no Chern–Weil code; grep `ChernWeil`: no hits)
- Ready now: no: C4.1 applies invariant polynomials to "SBC's principal curvature" (SBC B4.1, untouched); comparisons need C1–C3 (C1 partial, C3 untouched)
- Serves defs: 37, 48 (YangMillsConnectionsAndCaloricGauge §1.4 and Layer 6 consume C4 item 1; §§9.6–9.7 and §10.2 reach Layer 6)
- Evidence: README l.1321 "## C4. Curvature classes and their integral comparison", item 1 "Apply them to curvature using DG's value-bundle wedge/composition and SBC's principal curvature"; l.1996 "C4's invariant-form construction and line comparison use C1–C3 and the smooth suppliers"; STATUS "C3, C4, C5, C5a and C7 are untouched"

### C5a.3 Weil algebra and normalized Chern–Simons forms
- Status: NOT-STARTED (grep `WeilAlgebra`, `ChernSimons`: no hits).
- Ready now: no: "C5a.3 builds the Weil algebra and finite universal connection maps from C4" (C4 untouched).
- Serves defs: 37, 48 (through YangMillsConnectionsAndCaloricGauge §1.4)
- Evidence: README l.1530 "**C5a.3. The Weil differential and normalized transgression forms.**", l.2011.

## TauCetiRoadmap/DGAInfinity
STATUS.md snapshot: bf232a2 2026-11-16, generated against Tau Ceti aa6e43e (Tau Ceti checked at 91942aa9f, 2026-11-19)

### Layer 8 Hochschild cochains (ordinary algebras, normalized, HH²)
- Status: PARTIAL. Positive-arity Hochschild cochains of an A∞ algebra, with the Hochschild differential `[m,-]`, braces, the Gerstenhaber bracket and cohomology (Algebra/Homology/AInfinity/Algebra/Hochschild/{Basic,Complex,Cohomology}.lean). Normalized cochains for a strict unit, `PositiveHochschild.normalizedComplex` (Hochschild/Normalized.lean); whether the inclusion is a quasi-isomorphism is not addressed. Formal deformations and obstruction classes in Hochschild degree two (Deformation.lean); first-order deformations are degree-one cocycles. An ordinary or DG algebra becomes an A∞ algebra via `IsNonUnitalDGAlgebra.toAInfinityAlgebra` (DG.lean). For an ordinary algebra `A` and an `A`-bimodule `M` (so `M = A` gives Cⁿ(A,A)), the multilinear cochains `Aⁿ → M` in every arity including zero carry the Hochschild coboundary `TauCeti.hochschildBimoduleCoboundary` with `δ ∘ δ = 0`, degree-zero cocycles the centre and degree-one cocycles the derivations (RingTheory/HochschildCohomology/Coboundary.lean); the packaged cochain complex and cohomology there, `hochschildCochainComplex`/`hochschildCohomology` (Complex.lean), have coefficients in `Hom_R(A, M)`, not in `M`. Missing: the cochain complex and cohomology HHⁿ(A, M) with bimodule coefficients, HH² ↔ infinitesimal deformations and HH³ ↔ obstructions for ordinary algebras, normalization comparison, and quasi-equivalence/Morita invariance. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/37750 (Hochschild cohomology of an ordinary algebra with bimodule coefficients: `TauCeti.hochschildBimoduleCochainComplex`, `hochschildBimoduleCohomology`, RingTheory/HochschildCohomology/Bimodule.lean).
- Ready now: yes. The README names no blocking prerequisites for the ordinary-algebra HH²/HH³ clause, and both the A∞ machinery it specializes and the bimodule-coefficient coboundary are present.
- Serves defs: 10
- Evidence: README l.520 "### Layer 8: Hochschild cochains, deformations, Massey products, and formality" ("For an ordinary associative algebra, recover `HH²` for infinitesimal deformations and `HH³` for obstructions"). STATUS Layer 8 remaining "normalization and Morita invariance comparisons, Deligne groupoids over Q-algebras, higher m_n encoding Massey defining systems".

## TauCetiRoadmap/DifferentialGeometry
STATUS.md snapshot: 53c246b 2026-11-16, generated against Tau Ceti aa6e43e (Tau Ceti checked at 91942aa9f, 2026-11-19)

### Layer 12 (12.4 density, 12.5 divergence theorem)
- Status: PARTIAL: `riemannianVolume`, the gradient, divergence and Laplacian, the boundaryless compactly supported divergence theorem `integral_divergence_eq_zero` (Geometry/Manifold/Riemannian/DivergenceTheorem.lean:225), and, on oriented manifolds, `measure_riemannianVolumeForm` (`|dV| = riemannianVolume`) with the agreement of `integralTopForm` of `f dV` and the integral against `riemannianVolume` for continuous compactly supported `f` (Geometry/Manifold/Riemannian/VolumeForm/Measure.lean) exist. Missing: the 12.4 Riemannian density and its `integralDensity` link, and the 12.5 boundary divergence theorem `integral_divergence_eq_boundaryFlux`. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/38427 (Geometry/Manifold/Density/Integral.lean: `integralDensity` (DifferentialGeometry 5.5a), the input 12.4 waits on).
- Ready now: no: 12.4 needs 5.5a's `integralDensity` and its agreement with top-form integration. The rest of 5.5a is in code: `Density`, `RoughDensity` and the density `toDensity` of a top form and an orientation (LinearAlgebra/Density/{Basic,Orientation}.lean, Geometry/Manifold/Density/Basic.lean), and the smooth `DensityBundle` (Geometry/Manifold/VectorBundle/Density.lean). `integralDensity` itself needs only 5.2 (form integration, in code), so it can start now. 12.5 needs 12.4. Compactly supported variations on boundaryless sources can already use `integral_divergence_eq_zero`
- Serves defs: 52
- Evidence: README l.2796 "### Layer 12: Riemannian metrics and the Laplace–Beltrami operator", l.2936 "**12.5 Divergence theorem and Green.**"; STATUS coverage Layer 12 remaining names the Riemannian density with its `integralDensity` comparison (12.4) and the divergence theorem with boundary (12.5); Layer 5 remaining "densities on manifolds, integralDensity and Stokes with corners (5.5)"; grep `integralDensity` in Tau Ceti: no hits

## TauCetiRoadmap/FlagVarieties
STATUS.md snapshot: 7ca783d 2026-11-09 (Tau Ceti checked at 91942aa9f, 2026-11-19; README at roadmap 890b66d)

### Layer 2 Standard algebraic parabolics P_J
- Status: NOT-STARTED for general G. The GL_n case is done in Layer 1 (`standardWeight`, weight parabolics; Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/). Abstract Tits-system standard parabolics exist (GroupTheory/TitsSystem/Parabolic/).
- Ready now: no: STATUS says "blocked on ReductiveGroups 7/7b" (needs the Tits system on G(k), B W_J B and the BN-pair comparison with algebraic parabolics).
- Serves defs: 79
- Evidence: README l.156 "## Layer 2: standard algebraic parabolics and the BN-pair bridge" (inputs: "ReductiveGroups Layer 7's actual algebraic-group Tits system on G(k)"); STATUS Layer 2 "untouched", "remaining: standard parabolics P_J and their order classification; blocked on ReductiveGroups 7/7b".

## TauCetiRoadmap/NoncommutativeIntegration
STATUS.md snapshot: 2cc438a 2026-11-11 (Tau Ceti checked at 91942aa9f, 2026-11-19)

### §1.5 Finite-trace inclusions; Lp(B(H),Tr) = S_p
- Status: NOT-STARTED (no generalized singular numbers / τ-measurable operators). Supporting: approximation numbers (TauCeti/Analysis/OperatorIdeal/ApproximationNumber/), operator-ideal Schatten families (Analysis/OperatorIdeal/Family*), finite-dimensional Schatten seminorm (Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Schatten.lean).
- Ready now: no: needs §1.1, §1.3, §1.4 (not started) and VonNeumannAlgebras V10.Affiliation/V10.TracialLp (Layer 10 untouched).
- Serves defs: 46 (weak link)
- Evidence: README l.360 "### 1.5 Finite-trace inclusions and the commutative and Schatten identifications", *Needs* "§1.1, §1.3, §1.4; OperatorTheory/OperatorIdeals Parts A–B"; grep `generalizedSingularNumber|tauMeasurable` empty.

## TauCetiRoadmap/PerfectoidSpaces
STATUS.md snapshot: b885423 2026-11-16, generated against Tau Ceti aa6e43e (Tau Ceti checked at 91942aa9f, 2026-11-19); STATUS lists Layer P4 as untouched

### P4.15.2 universal prisms and perfection; P4.15.3 the affine Hodge–Tate input (Čech–Alexander Δ_{C/B})
- Status: PARTIAL, δ-rings only: `TauCeti.DeltaRing` (a `δ`-structure for a fixed prime `p`, with the polynomial `DeltaRing.addCorrection`), its Frobenius lift `DeltaRing.frobenius`, the `δ`-structure of a Frobenius lift on a `p`-torsion-free ring `DeltaRing.ofFrobeniusLift` with uniqueness `DeltaRing.ext_of_frobenius`, and the unique `δ`-structure on `ℤ` (RingTheory/DeltaRing/Basic.lean). Missing: free `δ`-algebras, distinguished elements, prisms (bounded, perfect), rigidity, prismatic envelopes, perfection of prisms, the perfect-prism/perfectoid equivalence, `A_inf` initiality, `Δ_init`, and all of P4.15.3. The "prism" hits elsewhere in TauCeti are simplicial/cubical topology.
- Ready now: no for the sections as written. P4.15.2 needs P4.15.1, which needs DerivedModuleAlgebra §§0.1–0.4, 0.14 and 1.1–1.9 (largely unstarted), plus P1.16–P1.18, P1.24 and P0.19 cotangent. P4.15.3 additionally needs P0.19's full cotangent complex. Distinguished elements, prisms and rigidity have no derived prerequisites beyond `TauCeti.DeltaRing` and the derived (p,J)-completeness predicate (both exist) and could start now as a substep.
- Serves defs: 81
- Evidence: README l.11053 "#### P4.15.2 universal prisms and perfection" (*semiperfectoid-universal-prism*); l.11090 "#### P4.15.3 the affine Hodge–Tate input" (*semiperfectoid-affine-hodge-tate*, which states "No global prismatic-cohomology output is required"). l.10959 "#### P4.15.1 derived completion and complete flat descent" is the prerequisite.

## TauCetiRoadmap/SpinGeometry
STATUS.md snapshot: 8f0def6 2026-11-11 (describes Tau Ceti to a6027b1; Tau Ceti checked at 91942aa9f, 2026-11-19)

### G4.2 Principal spin lifts
- Status: PARTIAL: the structure, its equivalences and pullback are in code: `TauCeti.SpinStructure` for rank `n ≥ 1` (a `TauCeti.PrincipalBundle` for `realCliffordSpinGroupZero n` with a continuous frame map to `TauCeti.OrthonormalFrameBundle`, equivariant along `CliffordAlgebra.spinVectorAction`, no numerability field, as the README's `Suggested.lean` specifies), `SpinStructure.Equiv` (`refl`, `symm`, `trans`, `toHomeomorph`), `SpinStructure.pullback`, `Equiv.pullback` (Topology/VectorBundle/SpinStructure.lean). Missing: descent, metric-change independence, smooth structures on lifts, and G4.3 onward. G4.1a–b frame adapters are done. The carriers the section names exist: `TauCeti.PrincipalBundle` with `PrincipalBundle.pullback` (Topology/FiberBundle/Principal/Basic.lean, Geometry/Manifold/FiberBundle/Pullback.lean), cocycle gluing `TauCeti.fiberBundleCoreOfGroupCocycle` (Geometry/Manifold/FiberBundle/GroupCocycle.lean), `TauCeti.OrthonormalFrameBundle` with `toOrientationCover` (Topology/VectorBundle/Orientation/OrthonormalFrame.lean) and its presentation as a principal `O(n)`-bundle `TauCeti.OrthonormalFrameBundle.Fiber` with proper projection (Topology/VectorBundle/OrthonormalFrame/Principal.lean), the structure group `CliffordAlgebra.realCliffordSpinGroupZero` (LinearAlgebra/CliffordAlgebra/Spin/Real/Basic.lean).
- Ready now: no for the rest: descent and metric-change independence need TopologicalKTheory T6.4's numerable principal-bundle category and CharacteristicClasses C1.0's oriented frames and metric-change transport (neither in code). G4 has no Spin^c content; FourManifolds §4.1, the target for def 64, builds its Spin^c lifts on G4's frame lifts and covering adapters (FourManifolds README l.1907).
- Serves defs: 64
- Evidence: README l.1461 "## Layer 4: Spin lifts, obstruction and classification", l.1585 "### 4.2 Principal spin lifts (G4.2)" ("A spin structure on an oriented metric V of rank n is a numerable principal Spin(n)-bundle P with an equivariant map P→Fr⁺_SO(V)"), *Needs* l.1652; STATUS "The topological and smooth frame adapters of G4.1 are done ... there are no Clifford bundles (G3), spin structures (G4.2–G4.4)", which predates Topology/VectorBundle/SpinStructure.lean.

## TauCetiRoadmap/StableReduction
STATUS.md snapshot: 1b19ebb 2026-11-11 (Tau Ceti checked at 91942aa9f, 2026-11-19)

### Layer 10 PrestableMap, IsStableMap, openness
- Status: PARTIAL: `PrestableMap`, isomorphisms/category, automorphisms with `infinitesimalAut`, contracted components with the closed-point, dimension and field-extension characterizations (TauCeti/AlgebraicGeometry/Curves/StableMaps/{Basic,Category,Automorphism,Contracted}.lean). Missing: `IsStableMap`, base-change invariance, openness for projective targets, the finite-automorphism and ampleness characterizations, and the constant-map/source-stability theorem. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/37797 (the normalization genus of a curve and the normalization of a curve is a curve, Curves/Genus/Normalization.lean) and https://github.com/TauCetiProject/TauCeti/pull/43507 (Layer 10's fibre automorphism groups `PrestableMap.fiberAut`, `fiberAutCongr`, `fiberAutPullback`, `fiberAutPostcomp`, StableMaps/FiberAutomorphism.lean).
- Ready now: yes for `IsStableMap` (needs the Layer 3 pointed-prestable core, which exists, plus a normalization genus of components; no `normalizationGenus` is in Tau Ceti yet, so build it from Normalization/ and `Scheme.genus`). Openness and the ampleness criterion need Layer 2's openness of ampleness (remaining).
- Serves defs: 24
- Evidence: README l.732 "### Layer 10: stable maps and their stability condition"; STATUS l.32 "Layer 10 has prestable maps, automorphisms and contracted components, but no `IsStableMap`"; grep `IsStableMap` empty.

### Layer 11 stable-map API and map-aware stabilization
- Status: PARTIAL: evaluation maps and polarization degree (StableMaps/Degree.lean); decorated dual graphs, clutching, contraction, cutting, forgetting, stabilization files exist in StableMaps/DualGraph/; descent of a prestable map along a contraction of its source curve, `PrestableMap.descend` with `toDescend` and uniqueness `descend_eq`, compatible with postcomposition, reindexing and base change (StableMaps/Descent.lean). STATUS remaining: "additivity and local constancy of degree, single-marking contraction, gluing of stable maps, map-aware stabilization in families".
- Ready now: no: needs Layer 10 `IsStableMap`, Layer 2 polarized descent and contraction descent, and Layer 3 single-marking contraction (all remaining)
- Serves defs: 24
- Evidence: README l.778 "### Layer 11: basic stable-map API and map-aware stabilization"; STATUS l.32 "Layer 11 has evaluation maps, the polarization degree of a map over a field, and decorated dual graphs".

## TauCetiRoadmap/SymplecticGeometry/CotangentLagrangian
STATUS.md snapshot: 62acfe6 2026-11-16 (umbrella SymplecticGeometry/STATUS.md, generated against Tau Ceti aa6e43e; Tau Ceti checked at 91942aa9f, 2026-11-19)

### C3.1 Discrete action, iterates and convex billiards
- Status: PARTIAL. Exists: the lifted next-collision map β̃ on `ℝ × (−1, 1)`, `TauCeti.StrictConvexBilliardTable.nextCollision`, with existence and uniqueness of the exit parameter (`exists_collision`, `eq_nextParam_of_areaForm_eq_zero`), `nextTangential_mem_Ioo`, the reflection law `outgoingDir_nextCollision` and τ-equivariance `nextCollision_add_period`, for any unit-speed table, not only smooth ones (TauCeti/Dynamics/Billiard/NextCollision.lean); periodic billiard polygons `TauCeti.exists_billiard_periodic_reflection` (Dynamics/Billiard/PeriodicPolygon.lean); the inverse of β̃ by time reversal, `nextCollisionEquiv`, and its descent to a bijection β of `AddCircle L × (−1, 1)`, `billiardMap` with `billiardMap_symm_coe` (Dynamics/Billiard/Inverse.lean); the generating function `S(s, t) = −‖χ(t) − χ(s)‖` (`generatingFunction`, `generatingFunction_add_period`) with `v = ∂_sS`, `w = −∂_tS` at the next collision (`deriv_generatingFunction_left_nextParam`, `deriv_generatingFunction_right_nextParam`, `nextParam_eq_iff_deriv_generatingFunction_left_eq`), the twist `∂_s∂_tS < 0` (`deriv_deriv_generatingFunction_left_neg`, `_right_neg`) and, for fixed `s`, `∂t/∂v < 0` with continuity of `v ↦ t` (`hasDerivAt_nextParam`, `deriv_nextParam_neg`, `continuousOn_nextParam`, `strictAntiOn_nextParam`) (Dynamics/Billiard/GeneratingFunction.lean); the chain dictionary `TauCeti.CotangentBundle.exists_equiv_periodic_of_generating` with `TauCeti.cyclicAction` (Geometry/Symplectic/Cotangent/GeneratingFunction/Chain.lean); the circular table `TauCeti.StrictConvexBilliardTable.circle` with the rotation formula `billiardMap_circle_coe`, the periodicity criterion `isPeriodicPt_billiardMap_circle_iff` and `exists_isPeriodicPt_billiardMap_circle_iff` (periodic exactly when `arccos v` is a rational multiple of `π`), the chord-length primitive identity `dℓ = w dt − v ds` for the circle `hasFDerivAt_norm_circle_nextParam_sub`, and the perimeter maximizers among inscribed `N`-gons (`isMaxOn_inscribedPerimeter_circle_iff_of_even`, `isMaxOn_inscribedPerimeter_circle_iff_add_add_eq_zero`) (Dynamics/Billiard/Circle.lean, with the perimeter bounds `TauCeti.inscribedPerimeter_le_of_forall_norm_le`, `inscribedPerimeter_eq_iff_of_forall_norm_eq` in Dynamics/Billiard/PeriodicPolygon.lean). Missing: joint continuity and smoothness of β̃ and its inverse in `(s, v)` (so β as a homeomorphism), the primitive identity `β̃*λ − λ = dℓ` and `β̃*ω = ω` for a general table, `MeasurePreserving` for β, the application of the chain dictionary to billiards (critical inscribed N-gons ↔ periodic states), and finite-volume recurrence. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/38890 (smoothness of β̃: `contDiffAt_nextCollision`, `contDiffOn_nextCollision`, Dynamics/Billiard/Smooth.lean), https://github.com/TauCetiProject/TauCeti/pull/42657 (joint continuity of β̃ and β as a homeomorphism: `continuousOn_nextCollision`, `nextCollisionHomeomorph`, Dynamics/Billiard/Continuous.lean) and https://github.com/TauCetiProject/TauCeti/pull/41537 (the circular table: its billiard maps, chord-length primitive identity, invariant measure, rational-rotation periodicity and inscribed `N`-gon maximizers, Dynamics/Billiard/Circle/).
- Ready now: yes: consumes C3's generating relations (TauCeti/Geometry/Symplectic/Cotangent/GeneratingFunction/{Correspondence,Composition,MixedHessian,Family,...}.lean), the carrier, β̃ and the generating function above, plus Mathlib `AddCircle` measure and `MeasurePreserving.conservative`. The merged MathematicalBilliards restates these properties at regularity `C^k` on its own carrier `ConvexTable` (§§2.1–2.2, 3.1–3.3), consumes C3.1's map and circular formula (§§1.5, 2.5, 5.6) and its finite-volume recurrence (§4.4), and does not cite the Tau Ceti carrier.
- Serves defs: 92
- Evidence: CotangentLagrangian/README l.471 "### C3.1. Discrete action, iterates and convex billiards", paragraph "Convex planar billiards" (l.527), l.728 "C3.1 consumes C3's generating relations, Mathlib's `AddCircle` measure ..."; SymplecticGeometry STATUS "C3 is partial: generating functions, their composition, and the next-collision map of a convex billiard are in"; grep `measurePreserving_billiardMap|continuous_billiardMap` in TauCeti/Dynamics/Billiard empty, and `primitive` there hits only the circle (Dynamics/Billiard/Circle.lean).

## TauCetiRoadmap/MathematicalBilliards
No STATUS.md (merged as roadmap PR #2255; Tau Ceti checked at 91942aa9f, 2026-11-19).

### Layer 1 Convex billiard tables (`ConvexTable`, curvature criterion, exit points, oriented lines)
- Status: NOT-STARTED on the roadmap's carrier (grep `ConvexTable` empty). Tau Ceti's `TauCeti.StrictConvexBilliardTable` (TauCeti/Dynamics/Billiard/NextCollision.lean) is the same strict-convexity and orientation condition for `C¹` unit-speed tables in an oriented Euclidean plane, with exit parameters (`exists_collision`, `nextParam`); the roadmap works in `ℂ` with a regularity index `k` and does not cite it. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43506 (§1.1 carrier `TauCeti.ConvexTable k ℓ` with `ConvexTable.apply_eq_apply_iff`, `injOn_Ico`, Dynamics/Billiard/ConvexTable.lean).
- Ready now: yes for §§1.1, 1.3–1.5 (Mathlib `StrictConvex`, `convexHull`; Tau Ceti `TauCeti.IsJordanCurve`, `isJordanCurve_frontier_of_convex`); §1.2 (curvature criterion) needs RiemannianGeometry/Surfaces §3.1 `integral_signedCurvature_add_sum_exteriorAngle_eq_two_pi` (not in code).
- Serves defs: 92
- Evidence: README l.96 "## Layer 1: Convex billiard tables", l.100 (§1.1 carrier), l.120 (§1.2), Dependencies l.172.

### Layers 2–3 The billiard ball map, its regularity and closed-cylinder extension; generating function and invariant measure
- Status: NOT-STARTED on `ConvexTable`. Tau Ceti analogues in the coordinates `(s, cos δ)`: the lift and the bijection of the open cylinder with time reversal (`nextCollision`, `nextCollisionEquiv`, `billiardMap`, `billiardMap_symm_coe`; cf. §§2.1, 2.4) and the chord-length derivatives and twist (`generatingFunction`, `deriv_deriv_generatingFunction_left_neg`; cf. §3.1); for the circle, the explicit billiard map and the chord-length primitive identity (`StrictConvexBilliardTable.billiardMap_circle_coe`, `hasFDerivAt_norm_circle_nextParam_sub`, Dynamics/Billiard/Circle.lean; cf. the circle Checks of §§2.1, 3.2). Missing: homeomorphism and `C^{k−1}` regularity (§2.2), the closed cylinder (§2.3), the comparison with C3.1 (§2.5), exactness and the Jacobian (§3.2), `phaseMeasure` and `ConvexTable.measurePreserving_billiardMap` (§3.3). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/38024 (Dynamics/Billiard/GeneratingFunction.lean: `billiardGeneratingFunction` of a periodic plane curve, its derivative and the twist condition).
- Ready now: no: needs Layer 1 (§2.1 needs §1.3; Layer 3 needs Layers 1–2; §2.5 also needs C3.1's map).
- Serves defs: 92
- Evidence: README l.174 "## Layer 2: The billiard ball map", l.251 "## Layer 3: Generating function and invariant measure", Dependencies l.249, l.304.

### Layers 4–5 Twist maps of the annulus; rotational invariant curves, Birkhoff's graph theorem and rotation numbers
- Status: NOT-STARTED (grep `IsTwistLift|IsRotationalInvariantCurve|nonwanderingSet` empty). A Tau Ceti analogue of §4.2's endpoint-coordinate construction exists for a `C²` map of a strip `ℝ × J` with `∂_y X ≠ 0`: the twist coordinates `TauCeti.stripTwistCoord` `(x, y) ↦ (x, X(x, y))` are injective and a `C^n` local diffeomorphism onto a band (`injOn_stripTwistCoord`, `isLocalDiffeomorphOn_stripTwistCoord`), and for an area-preserving map the band generating function `TauCeti.stripBandGeneratingFunction` satisfies the generating equations, is invariant under diagonal translation and has mixed derivative `−1/∂_y X` (`hasFDerivAt_stripBandGeneratingFunction`, `stripBandGeneratingFunction_add_diag`, `fderiv_fderiv_stripBandGeneratingFunction_apply`), Geometry/Symplectic/Annulus/TwistBand.lean; it is stated for Tau Ceti's `stripGeneratingFunction` (Annulus/GeneratingFunction.lean), not for `IsTwistLift` or the primitive `λ = g dx`. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/43497 (§4.1 `TauCeti.IsTwistLift`, Dynamics/TwistMap/TwistLift.lean) and https://github.com/TauCetiProject/TauCeti/pull/43500 (§4.4 `nonwanderingSet` with `isClosed_nonwanderingSet`, `nonwanderingSet_eq_univ_of_dense`, Dynamics/NonwanderingSet.lean).
- Ready now: yes for §§4.1–4.2 (twist lifts, monotone and exact twist maps; Mathlib only) and §5.1 (`IsRotationalInvariantCurve`, Definition 92.5; Mathlib `ContinuousMap.Nullhomotopic`, Tau Ceti Jordan curve theorem). No for the rest: §4.3 needs Layers 2–3; §4.4 needs C3.1's finite-volume recurrence (not in code); §5.2 needs GeometricTopology §2.3, the annulus theorem in dimension two (not in code); §§5.3–5.6 need §§2.3, 3.3, 4.3–4.4.
- Serves defs: 92
- Evidence: README l.306 "## Layer 4: Twist maps of the annulus", l.383 "## Layer 5: Rotational invariant curves" (§5.1 l.385, §5.3 l.416, §5.4 l.433), Dependencies l.381, l.479.

### Layers 7–8 Polygonal tables, phase space, trajectories, singular set, billiard flow and Liouville measure
- Status: NOT-STARTED (grep `billiardFlow|polygonalTable` empty). Supplier pieces exist: `TauCeti.SimplePolygon`, `Polygon.boundaryParamCircle`, `Polygon.IsSimple.isJordanCurve_boundary` (TauCeti/Geometry/Polygon/Simple.lean). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43494 (§7.1 `TauCeti.PolygonalTable` with `vertexSet`, `Side`, Dynamics/Billiard/PolygonalTable.lean).
- Ready now: yes for Layer 7 (Mathlib, Tau Ceti polygons); Layer 8 needs Layer 7.
- Serves defs: 93
- Evidence: README l.554 "## Layer 7: Polygonal tables" (§7.1 l.556, §7.2 l.576, §7.3 l.594), l.620 "## Layer 8: The singular set and the billiard flow" (§8.2 l.632, §8.3 l.648), Dependencies l.618, l.664.

### Layer 12 (§§12.1–12.5) Weak mixing of flows
- Status: NOT-STARTED (grep `IsWeaklyMixing|WeakMixing` in TauCeti empty). Supplier pieces exist: `TauCeti.bochner_charFun_real` (Analysis/Bochner/CharFun/Bochner.lean), `TauCeti.Semigroups.StronglyContinuousGroup` and `.IsUnitary` (Analysis/Semigroups/Group/). Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/42865 (§12.4 Wiener's lemma `TauCeti.tendsto_average_norm_charFun_sq`), https://github.com/TauCetiProject/TauCeti/pull/43173 (§§12.4, 12.4.1: Wiener's lemma and the continuous-time mean ergodic projection with the spectral atomic-mass identity) and https://github.com/TauCetiProject/TauCeti/pull/43158 (§12.4.1 `exists_tendsto_twistedAverage`, the mean ergodic theorem and Bochner spectral measure for `StronglyContinuousGroup`, Analysis/Semigroups/Group/MeanErgodic.lean).
- Ready now: yes for §§12.1–12.5 (Mathlib measure theory, `charFun`, `Lp.compMeasurePreserving`; Tau Ceti Bochner and strongly continuous groups); §12.6 needs Layers 9–11.
- Serves defs: 93
- Evidence: README l.866 "## Layer 12: Weak mixing of flows" (§12.1 l.868, §12.5 l.929), Dependencies l.963.

## TauCetiRoadmap/TaubesGromov
STATUS.md snapshot: af2393b 2026-11-16, generated against Tau Ceti aa6e43e (Tau Ceti checked at 91942aa9f, 2026-11-19)

### TG1 Embedded normal operators and application regularity
- Status: NOT-STARTED (only the local normal linearization of HF, Geometry/Symplectic/JHolomorphic/Normal/Linearization.lean, the normal rescaling of J along a curve, Normal/Rescaling.lean, taming forms `K π^* ω_C + dλ` for the normal linearization on disc bundles and under small normal dilations, `TauCeti.exists_forall_div_two_mul_norm_sq_le_normalLinearization` (Normal/Taming.lean), the fibrewise real Cauchy–Riemann symbol `TauCeti.cauchyRiemannSymbol` with its bijectivity onto antilinear maps over a complex line (JHolomorphic/Symbol.lean), and the generic Fredholm determinant line bundle with orientation transport, Analysis/Fredholm/DeterminantLine/).
- Ready now: no: needs PH6.2–6.3 realizations, HF F1.4 determinant orientation, GT tube, HF/M simple-curve transversality (F2.4/F2.6d).
- Serves defs: 60
- Evidence: README l.40 "## TG1. Embedded normal operators and application regularity"; STATUS prose "TG1 has only the normal linearization of J along a holomorphic section".

## TauCetiRoadmap/VonNeumannAlgebras
STATUS.md snapshot: 5be5068 2026-11-11 (Tau Ceti checked at 91942aa9f, 2026-11-19; README at roadmap 890b66d, which includes the #2242 revision on Jones 2015 and bounded Tomita–Takesaki)

### Layer 13 (V13b) injective = hyperfinite
- Status: NOT-STARTED.
- Ready now: no: needs V13a and V11 standard form, V12 ultrapowers, V5/V6 traces; Layers 3–7 and 9–13 are all untouched.
- Serves defs: 36
- Evidence: README l.4792 "## Layer 13: Hyperfiniteness and injective classification", l.4851 "### 13.2 Semidiscreteness, approximation and classification (V13b)"; STATUS `{"id":"Layer 13","state":"untouched"}`; grep `Hyperfinite|Semidiscrete` empty.

### V13a Tensor-independent CP maps, Arveson extension, Tomiyama, injectivity
- Status: NOT-STARTED.
- Ready now: no: needs V0–V3, V4.Core, V4.Normality; Layers 3–4 are untouched.
- Serves defs: 36 (AmenableTracesOnCStarAlgebras §4.1 hypertraces, §4.4, §5.4)
- Evidence: VonNeumannAlgebras README l.4794 "### 13.1 Tensor-independent CP and extension foundations (V13a)", *Needs* "V0–V3, V4.Core, V4.Normality"; AmenableTracesOnCStarAlgebras README l.1321 (§4.1 *Needs* "VonNeumannAlgebras V13a (Arveson's extension theorem)").

### Layer 9 (lattice part) Lattices in unimodular locally compact groups, Weil's formula, uniform lattices
- Status: NOT-STARTED (no lattice-subgroup predicate in Tau Ceti; Mathlib has `IsFundamentalDomain`, `covolume`, `QuotientGroup.integral_eq_integral_automorphize`). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43511 (`Subgroup.IsLattice`, Weil's formula for nonnegative functions and uniform lattices, MeasureTheory/Group/Lattice.lean).
- Ready now: yes for the lattice notion and Weil's formula (Mathlib inputs only); the lattice-module part of Layer 9 needs V7 and V8.
- Serves defs: 15, 31 (lattices in `PU(1,n)`, read in open PR #2425 §5.1)
- Evidence: README l.2882 "## Layer 9: Lattice modules and discrete series", l.2893 "Define a lattice as a discrete subgroup of finite covolume in a unimodular second-countable locally compact group".

## TauCetiRoadmap/SpectralSequencesAndConvergence
No STATUS.md (merged as roadmap PR #2302; Tau Ceti checked at 91942aa9f, 2026-11-19).

### Layer 1 and §2.1 Cycle and boundary towers, stabilisation, the limit page; bidegree assignments
- Status: NOT-STARTED for an arbitrary spectral sequence (grep `limitPage|HasLimitPage|infiniteCycles` empty). Tau Ceti has `E∞` and stabilisation only for spectral objects and filtered complexes (`Abelian.SpectralObject.EInftyIsoCokernel`, `spectralSequencePageXIsoEInfty`, Algebra/Homology/SpectralObject/{Abutment,Stabilization}.lean; `filtrationSpectralSequencePageXIsoEInftyOfFinite`, .../SpectralSequence/Filtered/Stabilization.lean). Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/43085 and https://github.com/TauCetiProject/TauCeti/pull/43118 (Layer 1: cycle and boundary towers, stabilisation and the limit page `E_∞ = Z_∞ / B_∞`, Algebra/Homology/SpectralSequence/{Tower,Stabilization,LimitPage}.lean) and https://github.com/TauCetiProject/TauCeti/pull/43181 (§2.1 `SpectralSequence.BidegreeAssignment` with boundedness and page Euler characteristics, SpectralSequence/Bidegree.lean).
- Ready now: yes (Mathlib `Subobject`, `kernelSubobject`, `imageSubobject`, `SpectralSequence`; countable products for §1.4 in general).
- Serves defs: 6
- Evidence: README l.404 "## Layer 1: cycle and boundary towers and the limit page" (§1.4 l.513), l.564 "### 2.1 Bidegree assignments".

### Layer 3 (§§3.1–3.2, 3.4) Filtered abutments, convergence structures, finite filtrations
- Status: NOT-STARTED (no convergence structure for an arbitrary spectral sequence; the filtered-complex convergence results in Tau Ceti, `filtrationSpectralSequencePageXIsoGradedOfFinite` and the exhaustive and complete variants in .../SpectralSequence/Filtered/{Convergence,Exhaustive,Complete}.lean, are instances in Layer 5's setting).
- Ready now: no: §3.2 needs §§1.4, 2.1, 3.1; §3.4 needs §3.2 and §2.3 for its Serre-class clause.
- Serves defs: 6
- Evidence: README l.703 "## Layer 3: filtered abutments and convergence", l.738 "### 3.2 Convergence structures" (*Needs:* 1.4, 2.1, 3.1), l.805 "### 3.4 Finite filtrations".

### §4.4 Convergence in a range of degrees (with §§4.1–4.3)
- Status: NOT-STARTED (grep `HasConvergenceBounds` empty). Supplier pieces exist: Tau Ceti `abutment`, `abutmentFiltration`, `isZero_abutmentFiltration`, `isIso_abutmentFiltrationι`, `EInfty`, `spectralSequencePageXIsoEInfty`.
- Ready now: no: needs §§3.2, 3.4, 4.2, 4.3 (and §4.1 on §1.2).
- Serves defs: 6
- Evidence: README l.961 "## Layer 4: spectral objects indexed by `EInt`", l.1114 "### 4.4 Convergence in a range of degrees" (*Needs:* 3.2, 3.4, 4.2, 4.3).

## TauCetiRoadmap/AlgebraicModuliForArithmeticGeometryPartII
No STATUS.md (merged as roadmap PR #1754; Tau Ceti checked at 91942aa9f, 2026-11-19).

### Layer 1 (§§1.1, 1.5, 1.7(ii)) `Num(X/S)`, `N¹(X/S)_ℝ`, nef classes and Kleiman's nonnegativity
- Status: NOT-STARTED (grep `numericallyTrivialClasses|relNumericallyTrivialClasses|IsNef` empty). Supplier pieces exist: `TauCeti.AlgebraicGeometry.LineBundleClass` and `LineBundleClass.IsAmple` (AlgebraicGeometry/LineBundle/Ample.lean), `LineBundleClass.intersectionNumber` with curves (AlgebraicGeometry/IntersectionNumber/Basic.lean), `Chow.intersectionNumber` and `Chow.Num` on surfaces (AlgebraicGeometry/Chow/SurfaceIntersection.lean).
- Ready now: no: §1.1 needs Layer 0 (§0.4 `Pic^τ(X/S)`, §§0.6–0.7); §1.5 needs §1.4; §1.7(ii) needs SchemeAndStackFoundations §§5.2–5.3 (§5.2 partial, §5.3 not started).
- Serves defs: 95 (through open PR #2431, which imports §§0.1, 1.1, 1.5–1.7)
- Evidence: README l.244 "## Layer 1: numerical groups, cones, nefness and bigness", l.246 "### 1.1 The relative numerical group Num(X/S)", l.335 "### 1.5 Relatively nef invertible sheaves", l.387 "### 1.7 Ampleness, the Nakai–Moishezon criterion and Kleiman's criterion"; Dependencies l.442.

## TauCetiRoadmap/NashBlowups
No STATUS.md (merged as roadmap PR #2413; Tau Ceti checked at 91942aa9f, 2026-11-19). Neither Suggested.lean declaration (`HasLocallyFreeQuotientOfDifferentials`, `smooth_iff_hasLocallyFreeQuotientOfDifferentials_of_charZero`, `..._of_isNormalScheme`) nor any italic target name of the README (`nashModification`, `nashBlowup`, `nashCotangent`, `nashIterate`, `normalizedNashBlowup`, `gaussMap`, `smoothLocusOfDim`, ...) exists in Tau Ceti. Every Tau Ceti supplier declaration it lists is in code (`relativeDifferentialsHomEquiv`, `pushforwardDerivation`, `relativeDifferentialsSpecIso`, `relativeDifferentialsStalkEquiv`, `FiniteLocallyFreeSheaf.FixedRank`, `Scheme.Hom.isReduced_image`, `isIso_normalizationDesc_iff`, `kerCotangentToTensor_bijective_of_formallyEtale`, `powRingHom_finite`, ...).

### §§0.1–0.2 the comparison map `c_f : f*Ω_{Y/R} → Ω_{X/R}`, base change and closed immersions
- Status: NOT-STARTED in code (grep `pullbackMap|relativeDifferentials.*baseChange` in TauCeti/AlgebraicGeometry/Modules/Differentials/ empty). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/40905 (`Roadmap: AlgebraicCurves` 12B.0d) adds Modules/Differentials/Pullback.lean with the §0.1 map under other names (`relativeDifferentialsPullbackHom`, `cotangentMap` with functoriality and open-immersion lemmas) and §0.2's base change (`relativeDifferentialsBaseChangeIso`); `pullbackMap_surjective_of_isClosedImmersion` is not in it.
- Ready now: yes, after #40905 for the closed-immersion clause (§0.1 needs only Tau Ceti `relativeDifferentialsHomEquiv`, `pushforwardDerivation`, `relativeDifferentialsRestrictIso`, `relativeDifferentialsSpecIso` and Mathlib `Scheme.Modules.pullbackPushforwardAdjunction`, all in code; §0.2 needs §0.1 and Mathlib `KaehlerDifferential.tensorKaehlerEquiv`)
- Serves defs: 25, 26 (through §2.6 locality and field base change, 25.5(c), and §3.1)
- Evidence: README l.419 "### 0.1 The comparison map of differentials" (*relativeDifferentials.pullbackMap*, Needs l.448), l.452 "### 0.2 Base change and closed immersions" (*relativeDifferentials.baseChangeIso*, *pullbackMap_surjective_of_isClosedImmersion*, Needs l.487 "§0.1; Tau Ceti ...").

### §0.3 the smooth locus of dimension `d`
- Status: NOT-STARTED (grep `smoothLocusOfDim` empty). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43574 (`TauCeti.AlgebraicGeometry.smoothLocusOfDim` with every bullet of §0.3, Modules/Differentials/SmoothLocusOfDim.lean).
- Ready now: yes (Needs Mathlib `Scheme.Hom.smoothLocus`, Tau Ceti `isFiniteLocallyFree_relativeDifferentials`, `rank_relativeDifferentials_apply`, `smoothOfRelativeDimension_iff_ringKrullDim_stalk_eq` (Morphisms/Smooth/RelativeDimension.lean), `smooth_smoothLocus_ι_comp` and SchemeAndStackFoundations §0.7, whose recorded local-dimension declarations are in Scheme/LocalDimension.lean)
- Serves defs: 25, 26 (`X_sm^{(d)}` is the open in §2.1's definition `N(X, Ω_{X/k}, d, X_sm^{(d)})`)
- Evidence: README l.490 "### 0.3 The smooth locus of dimension d", Needs l.515.

### §0.4 Grassmannians along a surjection
- Status: NOT-STARTED (grep `coherentGrassmannian` empty)
- Ready now: no: needs AlgebraicModuliForArithmeticGeometry §1.3 `coherentGrassmannian` (NOT-STARTED; it needs ModularCurves §0.7 over a non-affine base, PARTIAL)
- Serves defs: 25 (through §3.1, the Gauss-map description 25.5(d))
- Evidence: README l.519 "### 0.4 Grassmannians along a surjection" (*coherentGrassmannian.mapOfSurjective*, Needs l.553 "AlgebraicModuliForArithmeticGeometry §1.3").

### §0.5 smoothness at closed points over a perfect field
- Status: NOT-STARTED (*smooth_iff_isRegularLocalRing_closedPoints* absent). Tau Ceti has the global halves: `TauCeti.AlgebraicGeometry.isRegularLocalRing_stalk_of_smooth` and `Scheme.Hom.smooth_of_isRegularLocalRing_stalk` (regular everywhere over a perfect field implies smooth), both in Morphisms/Smooth/Regular.lean.
- Ready now: no: needs SchemeAndStackFoundations §4.13 `regularLocus_eq_smoothLocus` (absent: grep `regularLocus` in TauCeti/AlgebraicGeometry empty; the ring-level `TauCeti.Excellence.regularLocus` is in RingTheory/RegularLocalRing/Locus.lean). That §4.13 clause needs only existing Tau Ceti and Mathlib, so it can start now.
- Serves defs: 25, 26 (census 025 chain step 2)
- Evidence: README l.555 "### 0.5 Smoothness at closed points over a perfect field", Needs l.572 "SchemeAndStackFoundations §4.13 (`regularLocus_eq_smoothLocus`)"; SchemeAndStackFoundations README l.6986 "Define *Scheme.regularLocus X* ... prove *regularLocus_eq_smoothLocus*".

### §0.6 normality under separable extension of the ground field
- Status: NOT-STARTED (grep `IsGeometricallyNormal|isNormal_directLimit|isNormal_tensorProduct|isNormalScheme_pullback` empty). Its inputs are in code: `TauCeti.MvPolynomial.isIntegrallyClosed` (RingTheory/MvPolynomial/IntegrallyClosed.lean), `TauCeti.Algebra.Etale.isIntegrallyClosed_localization_atPrime_of_localization_under` (RingTheory/Etale/Normal.lean), `isNormalScheme_Spec_iff_forall_localization`. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43626 (RingTheory/Etale/Normal.lean, Localization/Normal.lean: normality under localization, polynomial rings and étale base change, and the finite separable case).
- Ready now: yes (Needs only Mathlib and those Tau Ceti declarations)
- Serves defs: 26 (through §6.3 `normalizedNashBlowup.baseChange`)
- Evidence: README l.575 "### 0.6 Normality under separable extension of the ground field" (*isNormal_directLimit*, *Algebra.IsGeometricallyNormal*, *isNormalScheme_pullback_of_isTranscendentalSeparable*), Needs l.661.

### §0.7 `HasLocallyFreeQuotientOfDifferentials`
- Status: NOT-STARTED (grep `HasLocallyFreeQuotient` empty; the predicate is stated in the roadmap's Suggested.lean). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43610 (Modules/Differentials/LocallyFreeQuotient.lean: `HasLocallyFreeQuotientOfDifferentials` with the restriction and smooth-scheme bullets).
- Ready now: yes for the definition and the restriction and smooth-scheme bullets (Tau Ceti `FiniteLocallyFreeSheaf.FixedRank`, `relativeDifferentialsRestrictIso`, `isFiniteLocallyFree_relativeDifferentials`); the uniqueness, glueing and stalk-criterion bullets need §0.3 (not started)
- Serves defs: 25, 26 (hypothesis of the triviality criterion §2.5, hence §2.7 and §§6.4, 7.1)
- Evidence: README l.671 "### 0.7 Locally free quotients of the differentials", Needs l.728 "... §0.3 for the uniqueness, glueing and stalk bullets".

### §1.1 the setting lemma
- Status: NOT-STARTED
- Ready now: no: needs §0.3 (not started). Its other inputs are in code: SchemeAndStackFoundations §0.11's smoothness descent along `Spec k' → Spec k` is Mathlib's `DescendsAlong @Smooth (@Surjective ⊓ @Flat ⊓ @QuasiCompact)` (AlgebraicGeometry/Morphisms/LocalFlatDescent.lean), §0.23 is Tau Ceti `isUniversalHomeomorphism_iff_isIntegralHom_universallyInjective_surjective`, and `Smooth.geometricallyReduced` is in Morphisms/Smooth/GeometricallyReduced.lean
- Serves defs: 25, 26 (§2.1 needs it)
- Evidence: README l.766 "### 1.1 The setting", Needs l.802 "§0.3; Mathlib ...; SchemeAndStackFoundations §§0.11, 0.23".

### §§1.2–1.5 the Nash modification `N(X, F, r, U)`, universal property, Plücker form, locality and flat base change
- Status: NOT-STARTED (grep `nashModification` empty)
- Ready now: no: §1.2 needs AlgebraicModuliForArithmeticGeometry §1.3 `coherentGrassmannian` (NOT-STARTED); §1.3 needs §1.2; §1.4 needs §§1.2–1.3 and AlgebraicModuliForArithmeticGeometry §1.3 `plucker` (which also needs §1.1 `ProjectiveBundles.projectiveBundle`, not started); §1.5 needs §1.2 and AlgebraicModuliForArithmeticGeometry §5.4 `ArithmeticModuli.DMSchematicClosure.stack` (not started; its Needs are SchemeAndStackFoundations §§1.18, 1.20, 1.22, and the scheme case it supplies, flat base change of `Scheme.Hom.image`, is not in Tau Ceti or Mathlib)
- Serves defs: 25, 26 (§1.2 is the construction §2.1 specialises; §2.2 needs §1.4, §2.4 needs §1.3, §2.6 needs §1.5)
- Evidence: README l.807 "### 1.2 The Nash modification of a sheaf" (Needs l.837), l.840 "### 1.3 Universal property" (Needs l.867), l.870 "### 1.4 The Plücker form" (Needs l.879), l.881 "### 1.5 Locality and flat base change" (Needs l.906 "§1.2; AlgebraicModuliForArithmeticGeometry §§1.3, 5.4").

### §§2.1–2.7 `nashBlowup`, `nashBlowupHom`, `nashCotangent`, properness and modification, universal property, triviality criterion, locality and field base change, `nashIterate`
- Status: NOT-STARTED (grep `nashBlowup|nashCotangent|nashIterate|NashIteration` empty)
- Ready now: no: §2.1 needs §§0.3, 1.1, 1.2 (not started, §1.2 waiting on AlgebraicModuliForArithmeticGeometry §1.3). §2.2 also needs §1.4 and SchemeAndStackFoundations §4.11 `IsModification.Witness` (§4.11 PARTIAL: `IsModification` and the centre are in code, `Witness` is not); §2.3 needs SchemeAndStackFoundations §0.7 (in code); §2.5 needs §0.7; §2.6 needs §§0.1, 0.2, 1.5; §2.7 needs §§2.3, 2.5
- Serves defs: 25 (target: 25.2–25.5(c)), 26 (Layer 6 is built on it)
- Evidence: README l.918 "## Layer 2: the Nash blowup"; l.920 "### 2.1 Definition" (Needs l.946), l.949 "### 2.2 Properness and the modification property" (Needs l.968 "§§1.2, 1.4, 2.1; SchemeAndStackFoundations §4.11; ..."), l.989 "### 2.4 Universal property", l.1021 "### 2.5 When the Nash blowup is trivial", l.1051 "### 2.6 Locality and field base change" (Needs l.1074), l.1077 "### 2.7 The Nash iteration" (Needs l.1105).

### §3.1 the Gauss map `nashBlowup_eq_closure_graph_gaussMap`
- Status: NOT-STARTED (grep `gaussMap` empty)
- Ready now: no: needs §§0.2, 0.4, 1.2, 2.1 and AlgebraicModuliForArithmeticGeometry §1.3 (all not started)
- Serves defs: 25 (25.5(d), census 025 chain step 7)
- Evidence: README l.1121 "### 3.1 The Gauss map", Needs l.1145.

### §§6.1–6.4 `normalizedNashBlowup`, universal property, locality and separable base change, isomorphism criteria
- Status: NOT-STARTED (grep `normalizedNash` empty). The scheme-level normalisation inputs are in code: Mathlib `Scheme.Hom.normalization`, `normalizationDesc`; Tau Ceti `isFinite_fromNormalization_of_isJapanese` (Normalization/Finite.lean) with `IsUniversallyJapanese.of_field`, and `Scheme.Hom.isIso_normalizationDesc_iff` (Normalization/IsIso.lean).
- Ready now: no: §6.1 needs §§2.1–2.3 (not started), AlgebraicModuliForArithmeticGeometry §5.4 `DMNormalization` (not started; its stack construction needs SchemeAndStackFoundations §§0.20, 1.14, 1.19–1.21, but the scheme case §6.1 uses is the Mathlib and Tau Ceti code above) and SchemeAndStackFoundations §0.30 (in code: `IsNormalScheme`); §6.2 needs §2.4; §6.3 needs §§0.6, 2.6; §6.4's main statement needs §§2.5, 6.1, and its corollaries need §§4.5, 5.4
- Serves defs: 26 (target: 26.1–26.2)
- Evidence: README l.1530 "## Layer 6: the normalised Nash blowup"; l.1532 "### 6.1 Definition and basic properties" (Needs l.1556 "§§2.1–2.3; AlgebraicModuliForArithmeticGeometry §5.4; SchemeAndStackFoundations §0.30"), l.1558 "### 6.2 Universal property", l.1585 "### 6.3 Locality and separable base change" (Needs l.1625 "§§0.6, 2.6, 6.1; ..."), l.1629 "### 6.4 Isomorphism criteria" (Needs l.1648).

### Layer 7 (§§7.1–7.3) `normalizedNashIterate`, `NormalizedNashIterationResolves`, open subschemes propagate, the never-resolves principle
- Status: NOT-STARTED (grep `normalizedNashIterate|NormalizedNashIterationResolves|iterate_openSubscheme` empty)
- Ready now: no: §7.1 needs §§0.3, 2.5, 2.7, 6.1, 6.4; §7.2 needs §§2.4, 2.6, 2.7, 6.3, 7.1; §7.3 needs §§7.1–7.2
- Serves defs: 26 (target: 26.3, and §7.3 is the form in which the paper's theorem is applied)
- Evidence: README l.1661 "## Layer 7: iteration and the never-resolves principle"; l.1663 "### 7.1 The normalised iteration" (Needs "§§0.3, 2.5, 2.7, 6.1, 6.4"), l.1693 "### 7.2 Open subschemes propagate", l.1716 "### 7.3 The never-resolves principle"; Dependencies "Layers 2 and 6".

## TauCetiRoadmap/StackPointsAndResidualGerbes
No STATUS.md (merged as roadmap PR #2429; Tau Ceti checked at 91942aa9f, 2026-11-19). No target of the roadmap exists in Tau Ceti: grep `Stacks\.|IsMonomorphism|IsFiniteTypePoint|automorphismGroupSpace|IsGerbeOver|residualGerbe|ResidualGerbe|residueField.*Stack|normalSpace|tangentToNormal` in TauCeti/AlgebraicGeometry empty. Every section rests on SchemeAndStackFoundations Layer 1, of which Tau Ceti has §1.3, the core of §1.4, §1.5's `EtaleEquivRel` and §1.18's `StackInGroupoids` carrier; §1.19 (algebraic stacks) and §1.20 (`Stacks.points`, `inertia`) are not started, so no item is ready. The README also names unowned "gap:" requests to its suppliers (most often gap:stack-morphism-permanence, gap:flat-groupoid-quotients, gap:stack-separation-axioms, gap:inertia-of-presentations, gap:reduced-regular-smooth-local, gap:qcoh-stacks-abelian-tensor; l.364–l.520 "What SchemeAndStackFoundations must provide (gap:...)"), which SchemeAndStackFoundations §§1.7–1.9, 1.13, 1.19–1.22, 4.12–4.13, AlgebraicModuliForArithmeticGeometry §8.1 and ReductiveGroups Layer 3 must add.

### Layer 0 (§§0.1–0.5) reduced and regular stacks, monomorphisms, immersions and substacks, closed substacks and infinitesimal neighbourhoods, reduced induced closed substack
- Status: NOT-STARTED
- Ready now: no: §0.1 needs SchemeAndStackFoundations §1.19 `IsAlgebraicStack` and §1.20 (both NOT-STARTED); §0.2 needs SSF §1.18 `twoFiberProduct` (§1.18 PARTIAL: carrier only), §§1.7, 1.8 (NOT-STARTED), §1.19, §1.20; §0.3 needs §§0.1–0.2, SSF §1.14 `Groupoid.restrict` (NOT-STARTED); §0.4 needs §0.3, SSF §1.22 `Stacks.QCoh` (NOT-STARTED) and §4.8 `Scheme.formalCompletion` (in code, AdicThickeningSystem/FormalCompletion.lean); §0.5 needs §§0.1, 0.3, SSF §1.20
- Serves defs: 28 (§0.3 open substacks ↔ open subsets of `|𝒳|`, 28.2(c); §§0.1, 0.2, 0.5 on its chain), 29, 16 (§§0.1–0.3, 0.5, through §§1.3, 3.3, 5.3), 17 (through Layer 7; §0.4 serves only 17 and 29)
- Evidence: README l.542 "## Layer 0: monomorphisms, immersions and reduced substacks"; l.544 "### 0.1" (Needs l.554 "SchemeAndStackFoundations §1.19 ..., §1.20"), l.586 "### 0.2 Monomorphisms" (Needs l.603 "§1.18 (`twoFiberProduct`), §1.19 ..., §1.7 ..., §1.8 ..., §1.20"), l.643 "### 0.3 Immersions and substacks" (Needs l.676), l.700 "### 0.4 Closed substacks, quasi-coherent ideals and infinitesimal neighbourhoods" (Needs l.732), l.773 "### 0.5 The reduced induced closed substack" (Needs l.784).

### Layer 1 (§§1.1–1.4) finite type points, closed and field-valued points, `Stacks.automorphismGroupSpace` `G_x`, when `G_x` is a scheme
- Status: NOT-STARTED (grep `IsFiniteTypePoint|pointOfObject|automorphismGroupSpace` empty)
- Ready now: no: §1.1 needs §0.5 and SSF §1.20 `Stacks.points` (NOT-STARTED); §1.2 needs §1.1, SSF §§1.18, 1.20; §1.3 needs §0.2, SSF §1.20 `inertia`, `automorphismGroup`, §1.13 `Groups.GroupSpace` and §1.14 `stabilizerAt` (NOT-STARTED); §1.4 needs §1.3 and SSF §1.9 (NOT-STARTED)
- Serves defs: 28 (target: 28.4(a)–(b), and `G_x`), 29, 16 (§§1.1, 1.3), 17 (through Layer 7)
- Evidence: README l.829 "## Layer 1: points of finite type and automorphism groups"; l.831 "### 1.1 Finite type points" (Needs l.838), l.877 "### 1.2 Closed points and field-valued points" (Needs l.883), l.914 "### 1.3 The automorphism group algebraic space" (Needs l.925 "SchemeAndStackFoundations §1.20 (`inertia`, ...), §1.13 (`Groups.GroupSpace`), §1.14"), l.955 "### 1.4 When the automorphism group is a scheme" (Needs l.962).

### Layer 2 (§§2.1–2.6) gerbes over an algebraic stack, gerbes with a section are classifying stacks, the inertia and diagonal criteria, the dense open gerbe
- Status: NOT-STARTED (grep `IsGerbe|relativeGerbe|classifyingEquiv` empty)
- Ready now: no: §2.1 needs AlgebraicModuliForArithmeticGeometry §4.1 `relativeGerbe` (NOT-STARTED, ready now), SSF §§1.18, 1.23 (NOT-STARTED) and, for its comparison bullet, AlgebraicModuliForArithmeticGeometry §5.1 rigidification (not started) and SSF §1.20; §§2.2–2.3 need SSF §1.21 `Stack.quotient`, `actionQuotient` (NOT-STARTED); §2.4 needs SSF §§1.14, 1.17 `artinBootstrap`, 1.20; §2.5 needs SSF §1.20; §2.6 needs §§0.3, 0.5, 2.4
- Serves defs: 29 (gerbes, census 029 chain step 4), 16 (through §§3.4, 5.3), 17 (through Layer 7)
- Evidence: README l.999 "## Layer 2: gerbes over algebraic stacks"; l.1001 "### 2.1" (Needs l.1016 "AlgebraicModuliForArithmeticGeometry §4.1 (`relativeGerbe`, ...); SchemeAndStackFoundations §1.18, §1.23 ..."), l.1061 "### 2.2 Gerbes with a section are classifying stacks" (Needs l.1070), l.1084 "### 2.3", l.1109 "### 2.4 The inertia criterion" (Needs l.1121), l.1136 "### 2.5", l.1158 "### 2.6 The dense open gerbe".

### Layer 3 (§§3.1–3.5) reduced one-point stacks, rigidity of monomorphisms, `Stacks.residualGerbe`, its properties and functoriality
- Status: NOT-STARTED (grep `residualGerbe|ResidualGerbeExists|residualGerbeMap` empty)
- Ready now: no: §3.1 needs §0.1, SSF §§1.19–1.20; §3.2 needs §§0.2, 3.1, SSF §1.21 and §1.8 (NOT-STARTED); §3.3 needs §§0.2, 0.5, 3.1, 3.2, SSF §1.18; §3.4 needs Layer 2 and §§3.1–3.3; §3.5 needs §§3.2–3.4
- Serves defs: 29 (target: §3.3 is 29.1–29.2), 16 (§3.3 residual gerbes, cited by census 016), 17 (through Layer 7)
- Evidence: README l.1192 "## Layer 3: reduced one-point stacks and residual gerbes"; l.1194 "### 3.1", l.1221 "### 3.2 Rigidity of monomorphisms" (Needs l.1232), l.1252 "### 3.3 Residual gerbes" (Needs l.1261 "0.2, 0.5, 3.1, 3.2; SchemeAndStackFoundations §1.18"), l.1283 "### 3.4 Properties of residual gerbes" (Needs l.1294), l.1316 "### 3.5 Functoriality".

### Layer 4 (§§4.1–4.5) existence of residual gerbes: finite type points, flat locally quasi-finite presentations, quasi-compact inertia, locally Noetherian stacks, closed points
- Status: NOT-STARTED
- Ready now: no: needs Layer 3 and §§0.2–0.5, 1.1–1.2, 2.1–2.6, with SSF §§1.8, 1.19 `IsDeligneMumford`, 1.20, 1.21 (all NOT-STARTED)
- Serves defs: 29 (29.3(a), and §4.5 the closed-immersion criterion), 16 (§§4.1–4.4, through §5.3; census 016 cites existence at closed points, quasi-compact inertia and locally Noetherian stacks), 17 (§4.5 is needed by §§7.1–7.4)
- Evidence: README l.1347 "## Layer 4: existence of residual gerbes"; l.1349 "### 4.1 Finite type points" (Needs l.1361), l.1377 "### 4.2" (Needs l.1387), l.1407 "### 4.3" (Needs l.1415), l.1430 "### 4.4 Locally Noetherian stacks" (Needs l.1437), l.1453 "### 4.5 Closed points" (Needs l.1457 "0.3, 0.5, 1.2, 3.3, 4.1, 4.4").

### §§5.1, 5.3 decent algebraic stacks and the residue field `Stacks.residueField` `κ(x)`
- Status: NOT-STARTED
- Ready now: no: §5.1 needs §§0.2, 0.3, 2.5 and SSF §§1.19, 1.20 `QuasiCompactStack` (NOT-STARTED); §5.3 needs §§2.1, 2.5, 3.1–3.5, 4.1, 4.3, 4.4, 5.1
- Serves defs: 16 (§5.3 `κ(x)`, cited by census 016 for the degree `[κ(x):k]/|Aut(x̄)|`), 29 (§6.3 needs §5.3), 17 (through Layer 7)
- Evidence: README l.1492 "## Layer 5: decent stacks and the residue field"; l.1494 "### 5.1 Decent algebraic stacks" (Needs l.1508), l.1577 "### 5.3 The residue field" (Needs l.1589 "0.2, 2.1, 2.5, 3.1, 3.2, 3.4, 5.1; 3.5 (for the functoriality bullet); 4.1, 4.3, 4.4 ...").

### Layer 6 (§§6.1–6.4) the presentation by a representative, base change to a representative, neutral residual gerbes `𝒵_x ≃ BG_x`, rational points
- Status: NOT-STARTED (grep `ResidualGerbe.IsNeutral|residualGerbe_rationalPoint` empty)
- Ready now: no: §6.1 needs §§0.2, 1.3, 2.4, 3.2, 3.4, 4.1, 5.3 and SSF §§1.14, 1.21; §6.2 needs §§2.1, 2.2, 3.4, 5.3 and SSF §1.20; §6.3 needs §§2.1–2.3, 3.4, 5.3, 6.1, 6.2; §6.4 needs §§3.1–3.4, 4.1, 4.5, 6.3 (and §§1.2, 1.4 for its API bullet)
- Serves defs: 29 (target: 29.4), 17 (§6.4 is needed by §§7.2–7.4)
- Evidence: README l.1722 "## Layer 6: residual gerbes at representatives and rational points"; l.1724 "### 6.1" (Needs l.1732), l.1759 "### 6.2", l.1796 "### 6.3 Neutral residual gerbes and `BG_x`" (Needs l.1818), l.1843 "### 6.4 Rational points of stacks over a field" (Needs l.1858).

### Layer 7 (§§7.1–7.4) infinitesimal neighbourhoods, `Stacks.normalSpace` `N_x` as a `G_x`-representation, `Stacks.tangentToNormal`, quotient stacks
- Status: NOT-STARTED (grep `normalSpace|tangentToNormal` empty)
- Ready now: no: §7.1 needs §§0.4, 3.4, 4.5 and SSF §4.8 (in code); §7.2 needs §§0.1, 0.4, 1.3, 4.5, 6.4, SSF §1.22 `Stacks.QCoh` (NOT-STARTED), Tau Ceti `TauCeti.Comodule` (in code) and ReductiveGroups Layer 1; §7.3 needs §§7.1–7.2, 2.2, 2.3, 6.4, AlgebraicModuliForArithmeticGeometry §§8.1, 8.3 (not started) and SSF §1.21; §7.4 needs §§7.2–7.3, SSF §§1.20–1.22
- Serves defs: 29 (target: 29.5, `N_x`), 17 (census 017 chain step 6: the local data `N_x`, `G_x` and the tangent comparison of the Luna slice statement)
- Evidence: README l.1915 "## Layer 7: infinitesimal neighbourhoods, normal and tangent spaces"; l.1926 "### 7.1" (Needs l.1930), l.1949 "### 7.2 The normal space" (Needs l.1956), l.1987 "### 7.3 The tangent space and the comparison map" (Needs l.2031), l.2063 "### 7.4 Quotient stacks" (Needs l.2094).

## TauCetiRoadmap/VirtualFundamentalClass
No STATUS.md (merged as roadmap PR #1996; Tau Ceti checked at 91942aa9f, 2026-11-19). No target of the roadmap exists in Tau Ceti: grep `normalCone|IsDeligneMumford|ObstructionTheory|virtualClass|intrinsicNormal` in TauCeti empty, and TauCeti/AlgebraicGeometry/Stack/ has only `SchPseudofunctor` and `StackInGroupoids`. Its Tau Ceti suppliers are in code: `Chow.ChowGroup.pushforward` (Chow/ClosedImmersion.lean), `relativeSpec`, `relativeSpecHomIso`, `relativeSpecBaseChangeIso`, `gradedRelativeSpecEquiv` (RelativeSpec/), `gradedSymmetricAlgebra`, `FiniteLocallyFreeSheaf`, `GeometricVectorBundle`, `Scheme.IdealSheafData.blowup`. Every layer rests on SchemeAndStackFoundations Layer 1 (DM stacks §1.19, quotient stacks §1.21, `QCoh` §1.22, not started), so no item is ready.

### Layer 0 (§§0.2–0.3) dimension of algebraic stacks, `dim [U/G] = dim U − dim G`
- Status: NOT-STARTED
- Ready now: no: §0.2 needs SSF Layer 1 (algebraic stacks, §1.19, not started); §0.3 needs §0.2 and SSF §1.21 quotient stacks (not started)
- Serves defs: 16 (§2.1 needs §§0.2–0.3), 27
- Evidence: README l.266 "## Layer 0: shared stack foundations and stack dimension", l.277 "### 0.2 Dimension and pure dimension" (*Needs* "SchemeAndStackFoundations Layer 1").

### Layer 1 (§§1.1–1.6) ringed sites of DM stacks, locally free sheaves, relative spectra, cones, normal cones and deformation to the normal cone over stacks
- Status: NOT-STARTED (the scheme-level `relativeSpec` and `gradedSymmetricAlgebra` suppliers are in code)
- Ready now: no: §1.1 needs §0.1 and SSF §§1.10, 1.22 (not started); §1.5 needs SSF §5.5 (not started)
- Serves defs: 27
- Evidence: README l.324 "## Layer 1: stack sites, representable cones, and normal cones"; l.326 "### 1.1 Ringed sites and comparison" (*Needs* "§0.1, SchemeAndStackFoundations §§1.10, 1.22 and AlgebraicVectorBundles L1A–L2B"); l.409 "### 1.5 Normal cones and deformation" (*Needs* "§§1.1–1.4 and SchemeAndStackFoundations §5.5").

### §§2.1–2.2 Vistoli's rational Chow groups of separated DM stacks, degree of proper zero-cycles, flat pullback and proper pushforward
- Status: NOT-STARTED
- Ready now: no: §2.1 needs §§0.2–0.3 (not started) and SSF §5.1 (partial: `Chow.ChowGroup` in code); §2.2 needs §2.1 and SSF Layer 5 (§5.2 partial). §2.1's cycles are "on integral closed substacks", which no merged roadmap defines (PR #2446's `gap:closed-substacks-of-stacks`; closed and reduced closed substacks are StackPointsAndResidualGerbes §§0.3–0.5, not started)
- Serves defs: 16 (target: 16.1–16.3, degree of 16.6), 27
- Evidence: README l.464 "## Layer 2: rational Chow theory and Gysin maps for Deligne–Mumford stacks"; l.469 "### 2.1 Rational Chow groups" ("Build Vistoli's dimension-graded rational Chow groups for separated Deligne–Mumford stacks ..."; API "Compute degrees of proper zero-cycles, with the generic stabilizer weight"); l.497 "### 2.2 Chow operations".

### §§2.3–2.5 Chern classes, refined Gysin maps, bivariant orientations for DM stacks
- Status: NOT-STARTED
- Ready now: no: needs §§1.2, 1.5, 2.1–2.2 and SSF Layer 5 (§§5.4–5.5 not started)
- Serves defs: 27 (the zero-section Gysin map `0_E^!` of the Layer 2 milestone)
- Evidence: README l.519 "### 2.3 Homotopy invariance and Chern classes", l.555 "### 2.4 Refined Gysin maps" (*Needs* "§§1.5, 2.2–2.3 and SchemeAndStackFoundations Layer 5"), l.573 "### 2.5 Bivariant orientations and comparison".

### Layer 3 (§§3.1–3.4) derived operations on stack sites, perfect complexes and global resolutions, cotangent complexes of morphisms of stacks, local presentation
- Status: NOT-STARTED
- Ready now: no: §3.1 needs Layer 1, DerivedModuleAlgebra, EnhancedDerivedSheaves (§0.3 partial) and DerivedDeRhamCohomology §5.8 (not started); §3.3 also needs SSF §1.10 (not started)
- Serves defs: 27
- Evidence: README l.622 "## Layer 3: geometric cotangent complexes and perfect complexes on stacks"; l.659 "### 3.3 Relative cotangent complexes" ("Consume the scheme cotangent complex from DerivedDeRhamCohomology §5.8 ...").

### Layers 4–5 cone stacks, `h¹/h⁰`, the intrinsic normal sheaf and cone
- Status: NOT-STARTED
- Ready now: no: §4.1 needs §§0.1, 1.4; §4.3 needs §§3.1–3.2; §5.1 needs §§1.5–1.6, 3.3–3.4, 4.4
- Serves defs: 27 (27.2, 27.3)
- Evidence: README l.731 "## Layer 4: cone stacks and the `h¹/h⁰` construction", l.846 "## Layer 5: the intrinsic normal sheaf and cone", l.882 "### 5.3 Intrinsic normal cone".

### Layers 6–7 obstruction theories, perfect obstruction theories, global resolutions, the virtual class and its degree
- Status: NOT-STARTED
- Ready now: no: §6.1 needs §§3.1–3.4, 4.4–4.5, 5.1; §7.4 needs §§7.1–7.3, which need Layer 2 Gysin maps (§2.4) and §6.5
- Serves defs: 27 (target: 27.4–27.6)
- Evidence: README l.944 "### 6.1 Obstruction theories", l.997 "### 6.4 Perfect obstruction theories", l.1018 "### 6.5 Global two-term resolutions", l.1141 "### 7.4 Public construction", l.1187 "### 7.7 Virtual degree".

### Layer 9 (§§9.1–9.2) relative intrinsic cone and relative virtual class over a pure-dimensional algebraic stack
- Status: NOT-STARTED
- Ready now: no: §9.1 needs §§0.2, 1.5–1.6, 3.3, 4.4, 5.1–5.3; §9.2 needs §§6.1–6.5, 7.1–7.4, 9.1
- Serves defs: 27 (27.3–27.6 relative; open roadmap PR #1998 Layer 4 builds 27.7 on §9.2)
- Evidence: README l.1325 "## Layer 9: the relative intrinsic cone and virtual class", l.1327 "### 9.1 Relative intrinsic cone", l.1348 "### 9.2 Relative virtual class".

## TauCetiRoadmap/ComplexHessianEquations
No STATUS.md (merged as roadmap PR #2440; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `spectralFunction`, `eigenvalueVector`, `gardingCone`, `hessianCone`, `AdmissiblePair`, `IsHyperbolic`, `ddbarHermitianForm`, `formPow`, `IsNormalizedSolution`, `Maclaurin`: no hits. Its Tau Ceti suppliers are in code: Courant–Fischer `LinearMap.IsSymmetric.eigenvalue_mono`, `abs_eigenvalue_sub_eigenvalue_le` (Analysis/InnerProductSpace/CourantFischer.lean), von Neumann's trace inequality `re_trace_comp_le_sum_eigenvalues_mul_eigenvalues` (HoffmanWielandt/Basic.lean), Ky Fan `sum_re_inner_apply_self_le_sum_eigenvalues` (KyFan.lean), `Convex.robinHood_mem` and `TauCeti.mem_of_prefixSum_le_of_sum_eq` (Analysis/Convex/Majorization.lean), `Real.prod_rpow_add_prod_rpow_le_prod_add_rpow` (Analysis/MeanInequalities.lean), the Levi form `TauCeti.manifoldLeviForm` with `isSymm_manifoldLeviForm`, `leviForm_comp_symm_apply_of_mem_maximalAtlas`, `toMatrix₂_leviForm`, `re_leviForm_nonpos_of_isLocalMax`, `integralTopForm_mextDeriv_eq_zero` (DifferentialForm/Integration/BoundarylessStokes.lean), `riemannianVolume`, and ComplexManifolds Milestone 2's canonical orientation (Geometry/Manifold/Complex/Orientation.lean).

### Layer 1 (§§1.1–1.5) Relative eigenvalues, Ky Fan sums, spectral functions and Lewis's formula, concavity and ellipticity, determinant and Euler identities
- Status: NOT-STARTED (the eigenvalue inequalities it consumes are in code; no relative eigenvalue vector, spectral function or `eigenvalueVector`). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43573 (§1.1 relative eigenvalue vector `LinearMap.IsSymm.relEigenvalues` via `LinearMap.toSesqForm`, Analysis/InnerProductSpace/RelativeEigenvalues.lean).
- Ready now: yes for §§1.1–1.2 (their *Needs* are Mathlib `LinearMap.IsSymmetric.eigenvalues`, `eigenvectorBasis` and the Tau Ceti eigenvalue inequalities above, all in code); §1.3 needs §1.2, §1.4 needs §§1.2–1.3, §1.5 needs §1.3.
- Serves defs: 38
- Evidence: README l.115 "## Layer 1: Eigenvalues and spectral functions", l.119 "### 1.1 Eigenvalues relative to an inner product" (*Needs* l.121), l.157 "### 1.2 Ky Fan sums and their derivative" (*Needs* l.163), l.177 "### 1.3 Spectral functions and their derivative" (*Needs* l.183 "§1.2"), l.197 "### 1.4" (*Needs* l.206 "§§1.2–1.3"), l.218 "### 1.5" (*Needs* l.226 "§1.3"); `Suggested.lean` `eigenvalueVector`, `differentiableAt_spectralFunction_iff`, `concaveOn_spectralFunction`.

### Layer 2 (§§2.1–2.5) Newton–Maclaurin, Gårding cones `Γ_k`, Hessian quotients, admissible cones and pairs, structural condition, examples
- Status: NOT-STARTED (Tau Ceti uses `esymm` only for Hecke algebras, Newton identities and Weierstrass polynomials; no Newton–Maclaurin inequalities, hyperbolic polynomials, `Γ_k` or `AdmissiblePair`). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43590 (§2.1 Newton–Maclaurin inequalities with `eval_esymm_succ`, `sum_mul_eval_update_zero_esymm`, Analysis/MvPolynomial/NewtonMaclaurin.lean).
- Ready now: yes for §2.1 (*Needs* Mathlib `MvPolynomial.esymm`, `Polynomial.card_roots_le_derivative`); §2.2 needs §2.1 (and §1.4 for the operator version); §2.3 needs §§2.1–2.2; §2.4 needs §§1.3–1.5, 2.2–2.3; §2.5 needs §§2.1–2.4.
- Serves defs: 38 (38.2 is §2.4, 38.4 is §2.5)
- Evidence: README l.242 "## Layer 2: Gårding cones and admissible pairs", l.244 "### 2.1 Elementary symmetric functions and the Newton–Maclaurin inequalities" (*Needs* l.246), l.258 "### 2.2 Hyperbolic polynomials and the Gårding cones" (*Needs* l.264), l.288 "### 2.3" (*Needs* l.290), l.299 "### 2.4 Admissible cones, admissible pairs and the structural condition" (*Needs* l.310 "§§1.3–1.5, 2.2–2.3"), l.331 "### 2.5 Examples and structural constants" (*Needs* l.341); `Suggested.lean` `AdmissiblePair`, `AdmissiblePair.IsStructural`, `exists_hessianPair`.

### §3.1 Eigenvalue functions, `i∂∂̄u` of a `C²` function on the Levi form, complex Laplacian
- Status: NOT-STARTED (its Levi-form inputs are in code: `TauCeti.manifoldLeviForm` and the lemmas above, `TauCeti.SmoothTwoForm.Invariant`, `Compatible`; no `hermitianForm`, `ddbarHermitianForm`, `IsRelEigenvalueVector` or comparison with K2's `i∂∂̄`).
- Ready now: no: needs §1.1 (not started). Its other *Needs*, ComplexKahlerGeometry K1–K2, are partial with the parts §3.1 uses (type projections, `∂`, `∂̄`, `dC`) in code.
- Serves defs: 38 (38.1)
- Evidence: README l.359 "### 3.1 Eigenvalue functions, `i∂∂̄` and the complex Laplacian"; *Needs* l.361 "Layer 1 §1.1; ComplexKahlerGeometry K1–K2; Tau Ceti `TauCeti.manifoldLeviForm`, ..."; `Suggested.lean` `hermitianForm`, `ddbarHermitianForm`, `IsRelEigenvalueVector`.

### §3.2 Form identities `α^k ∧ ω^{n−k} = c·σ_k(λ[α])·ω^n`, `ω^n = n!·dvol_g`, integration identities, Kähler invariance
- Status: NOT-STARTED (`TauCeti.SmoothTwoForm.volumeForm` and `liouvilleMeasure` give `ωⁿ/n!` and its measure; no comparison with `riemannianVolume`, no `formPow` or `formPowIntegral`).
- Ready now: no: needs §3.1 and §§2.2–2.3 (not started). Its other *Needs* are in code: DifferentialGeometry Layers 0–1, 5, 12 through `TauCeti.RoughForm.wedge`, `integralTopForm`, `integralTopForm_mextDeriv_eq_zero`, `riemannianVolume`, and ComplexManifolds Milestone 2 (canonical orientation, Geometry/Manifold/Complex/Orientation.lean; ComplexManifolds STATUS "Milestone 2" done).
- Serves defs: 38 (also states Proposition 14.2's comparison `ωⁿ/n! = dvol_g` and Proposition 14.4's invariance for Definition 14, which is in code)
- Evidence: README l.390 "### 3.2 Form identities and integration identities"; *Needs* l.400 "§3.1; Layer 2 §§2.2–2.3; DifferentialGeometry Layers 0–1, 5 and 12 ...; ComplexManifolds Milestone 2"; Conventions l.36 "`ω^n = n!·dvol_g`"; `Suggested.lean` `formPow`, `formPowIntegral`.

### §3.3 Admissible functions, the equation `f(λ_ω[χ_φ]) = c·e^F` with `sup φ = 0`, normalisation
- Status: NOT-STARTED (no `IsNormalizedSolution`).
- Ready now: no: needs §§3.1–3.2 and §§2.4–2.5 (not started).
- Serves defs: 38 (38.3, Examples 38.4)
- Evidence: README l.422 "### 3.3 Admissible functions and the equation" ("a solution is a pair `(c, φ)` ... with `f(λ_ω[χ_φ]) = c·e^F` on `X` and `sup_X φ = 0`"); *Needs* l.436 "§§3.1–3.2; Layer 2 §§2.4–2.5"; `Suggested.lean` `IsNormalizedSolution`.

### §3.4 Degenerating backgrounds `ω_t = χ + tω_X`, energy and entropy
- Status: NOT-STARTED.
- Ready now: no: needs §§3.2–3.3 and §2.4 (not started).
- Serves defs: 38 (for the paper's theorem: Layer 8's `L^∞` estimates consume it; not part of Definitions 38.1–38.3)
- Evidence: README l.450 "### 3.4 Degenerating backgrounds, energy and entropy"; *Needs* l.452 "§§3.2–3.3; Layer 2 §2.4"; consumed by §§8.1–8.6 (*Needs* l.708, l.720, l.734, l.752, l.782).

## TauCetiRoadmap/Varifolds
No STATUS.md (merged as roadmap PR #2443; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `varifold`, `grassmannBundle`, `Euclidean.grassmannian`, `VarifoldTendsto`, `IsVarifoldTangent`: no hits. Suppliers in code: `TauCeti.finiteGrassmannian` with `toEuclidean`, `toEuclidean_injective`, `continuous_starProjection_toEuclidean` (Topology/Grassmannian/{Basic,Tautological}.lean), `TauCeti.CountablyRectifiable`, `Distribution.massMeasure` (Analysis/Distribution/Mass/Measure.lean), `TauCeti.RealRMK.posPart`/`negPart` (MeasureTheory/Integral/RieszMarkovKakutani/Signed.lean), `TauCeti.isCompact_closure_of_isTightMeasureSet_of_mass_le` (MeasureTheory/Measure/Prokhorov.lean), `TauCeti.globalFlow`, `TauCeti.Manifold.divergence`, `integral_divergence_eq_zero`, `TauCeti.inducedRiemannianMetric`, `TauCeti.Manifold.IsNormalDomain`, `exists_isNormalDomain_ball`, `eq_riemannianVolume_iff`, `IsLocalRiemannianIsometry.mfderiv_leviCivitaConnection_mpullback`. Supplier roadmap items not in code: GeometricCurrents G6's Grassmann bundle and Radon compactness (G6 not started), GeometricCurrents G2's manifold chart comparison (GeometricCurrents STATUS 941bb58: "Nothing yet lives on a manifold"), GeometricMeasureTheory G2 (partial: a.e. uniqueness of tangent planes, tangential differentiation and the tangential area formula missing), RiemannianGeometry R5a (partial), R5a.2 (not started). HopfRinow Layers 0–2 are complete.

### §1.1 The Grassmannian `G(E, k)` of a Euclidean space in projection form
- Status: NOT-STARTED (`TauCeti.finiteGrassmannian` and its projection map exist; no `Euclidean.grassmannian` of star projections, complement map, image-plane map or comparison homeomorphism). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43572 (`Euclidean.grassmannian E k` of star projections with `finiteDimensional_range`, `finrank_range` and the bijection with `k`-dimensional subspaces, Topology/Grassmannian/StarProjection.lean).
- Ready now: yes (*Needs* are Mathlib `IsStarProjection`, `Submodule.starProjection`, `isStarProjection_iff_eq_starProjection_range`, `Continuous.homeoOfEquivCompactToT2` and the Tau Ceti `finiteGrassmannian` declarations, all present).
- Serves defs: 53, 65; 52 (through §5.1)
- Evidence: README l.421 "### 1.1 The Grassmannian of a Euclidean space" ("define the Grassmannian G(E, k) = `Euclidean.grassmannian E k` as the set of continuous linear maps P : E → E that are self-adjoint idempotents"); *Needs* l.497; `Suggested.lean` `grassmannian`.

### §§1.2–1.4 Grassmann bundle `G_k(M)`, varifolds with weight, mass, support and restriction, varifold convergence and compactness
- Status: NOT-STARTED.
- Ready now: no: §1.2 needs §1.1 and GeometricCurrents G6 (Grassmann bundle, compactness over compact base regions, Radon compactness; not started); §1.3 needs §1.2; §1.4 needs §1.3 and G6's Radon compactness (the README's route goes through Tau Ceti `isCompact_closure_of_isTightMeasureSet_of_mass_le`, in code).
- Serves defs: 53 (53.1), 65; 52 (through §5.1)
- Evidence: README l.503 "### 1.2 The Grassmann bundle of a Riemannian manifold" (*Needs* l.537 "Layer 1.1; GeometricCurrents G6"), l.541 "### 1.3 Varifolds, weight, mass, support and restriction" (*Needs* l.572), l.576 "### 1.4 Varifold convergence and compactness" (*Needs* l.603); `Suggested.lean` `grassmannBundle`, `weight`, `VarifoldTendsto`.

### Layer 2 (§§2.1–2.3) Approximate tangent spaces and the rectifiability criterion, rectifiable and integral varifolds `v(Γ, θ)`, the varifold `[Σ]` of a `C¹` submanifold
- Status: NOT-STARTED (`CountablyRectifiable`, a.e. existence and a measurable choice of Euclidean approximate tangent planes are in code, from GeometricMeasureTheory G2).
- Ready now: no: §2.1 needs GeometricMeasureTheory G2 (partial: a.e. uniqueness and the tangential area formula missing) and GeometricCurrents G2's chart comparison of rectifiable sets and Hᵏ on a Riemannian manifold (not in code); §2.2 also needs §1.3; §2.3 needs §2.2.
- Serves defs: 53 (53.2), 65 (`[Σ]`); 52 (through §5.1)
- Evidence: README l.619 "## Layer 2: rectifiable and integral varifolds", l.621 "### 2.1" (*Needs* l.658 "GeometricMeasureTheory G2 ...; GeometricCurrents G2 ...; HopfRinow Layer 2"), l.663 "### 2.2 Rectifiable and integral varifolds" (*Needs* l.719), l.723 "### 2.3 The varifold of a C¹ submanifold" (*Needs* l.762); `Suggested.lean` `IsRectifiable`, `IsIntegral`.

### Layer 3 (§§3.1–3.3) Push-forward, dilations and normal-coordinate blow-ups, tangent spaces with multiplicity
- Status: NOT-STARTED.
- Ready now: no: §3.1 needs Layers 1.1–1.4, 2.2 and GeometricMeasureTheory G2's area formula, GeometricCurrents G2; §3.2 needs §3.1 (HopfRinow Layers 1–2 complete); §3.3 needs §§2.1–2.2, 3.2.
- Serves defs: 53 (53.3), 65; 52 (through §5.1)
- Evidence: README l.779 "## Layer 3: push-forward, blow-ups and tangent spaces", l.781 "### 3.1 Push-forward" (*Needs* l.831), l.835 "### 3.2 Dilations and normal-coordinate blow-ups" (*Needs* l.861), l.864 "### 3.3" (*Needs* l.915); `Suggested.lean` `blowUp`.

### §4.2 Riesz representation for vector fields
- Status: NOT-STARTED (Tau Ceti's Euclidean mass measure and polar density of a current, `Distribution.massMeasure`, `Distribution.apply_eq_integral_polarDensity`, are in code; no vector-field Riesz theorem on a Riemannian manifold, and no gluing of local measures over a cover). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43591 (the Euclidean case of §4.2: `Distribution.polarVector`, `Distribution.apply_eq_integral_inner_polarVector`, `ae_norm_polarVector_eq_one`, `ae_eq_polarVector`, `massMeasure_eq_of_apply_eq_integral_inner` in Analysis/Distribution/Mass/PolarVector.lean; the Riemannian form and the gluing over a cover are not in it).
- Ready now: yes (*Needs* are Tau Ceti `Distribution.massMeasure`, `massMeasure_preimage_coe`, `enorm_apply_le_lintegral_massMeasure`, `TauCeti.RealRMK.posPart`, `negPart`, `integral_rieszMeasure_posPart_sub_integral_rieszMeasure_negPart` and Mathlib `RealRMK.rieszMeasure`, `Measure.rnDeriv`, all present).
- Serves defs: 53 (53.4), 65; 52 (through §5.1)
- Evidence: README l.983 "### 4.2 Riesz representation for vector fields" ("What Tau Ceti's mass measure does not provide is built here: the polar field η and the gluing of the local measures and fields over a countable cover of W"); *Needs* l.1019.

### §§4.1, 4.3–4.5 First variation, stationarity, locally bounded first variation, Riesz decomposition with generalized mean curvature, two metrics and blow-ups
- Status: NOT-STARTED (`TauCeti.Manifold.divergence`, `globalFlow` and the length/energy first variations of curves exist; no `firstVariation` of a varifold).
- Ready now: no: §4.1 needs §§1.3, 3.1; §4.3 needs §§4.1–4.2; §4.4 needs §§3.1–3.2, 4.2–4.3; §4.5 needs §§3.1–3.2, 4.1, 4.3–4.4.
- Serves defs: 53 (53.4, 53.5(a)), 65 (stationarity, §4.3); 52 (through §5.1)
- Evidence: README l.932 "## Layer 4: the first variation", l.934 "### 4.1 Tangential divergence and the first variation" (*Needs* l.978), l.1025 "### 4.3 Stationary varifolds and locally bounded first variation" (*Needs* l.1058), l.1060 "### 4.4 The Riesz decomposition of the first variation" (*Needs* l.1115), l.1121 "### 4.5" (*Needs* l.1167); `Suggested.lean` `firstVariation`, `IsStationary`, `HasLocallyBoundedFirstVariation`, `exists_firstVariation_eq_riesz`.

### Layer 5 (§§5.1–5.2) First variation of a `C²` submanifold (`δ[Σ] = −k ∫ ⟨H_Σ, X⟩`, stationary iff minimal), varifolds on an embedded submanifold of Euclidean space
- Status: NOT-STARTED (the flat-ambient `TauCeti.secondFundamentalForm` and `inducedRiemannianMetric` it names are in code).
- Ready now: no: §5.1 needs §§2.3, 4.1–4.4 and RiemannianGeometry R5a (partial: normal bundle `orthogonalNormalContMDiffVectorBundle` in code, no intrinsic B for a Riemannian ambient) and R5a.2 (not started); §5.2 needs §§3.1, 3.3, 4.1–4.4, R5a and GeometricCurrents G2.
- Serves defs: §5.1: 53 (53.5(b)), 65, 52 (the varifold reading of 52.1); §5.2: 53
- Evidence: README l.1188 "## Layer 5: smooth submanifolds and embedded ambient manifolds", l.1190 "### 5.1 The first variation of a C² submanifold" (*Needs* l.1231 "Layer 2.3, Layer 4.1–4.4; RiemannianGeometry R5a, R5a.2"), l.1235 "### 5.2 Varifolds on an embedded submanifold of Euclidean space" (*Needs* l.1286).

### §§6.1–6.4 Euclidean and Riemannian monotonicity, densities, constancy
- Status: NOT-STARTED.
- Ready now: no: §6.1 needs Layer 4; §6.2 also needs RiemannianGeometry R4 item 1 (partial: `rauch_norm_ge_of_sectional_le`, Geometry/Manifold/Riemannian/Jacobi/Comparison.lean, and `hessian_dist_sq_self`, Riemannian/Hessian/SquaredDistance.lean, are in code; the transverse Hessian comparison of the distance function `r` is not); §6.3 needs §§1.4, 3.3, 4.4, 6.1–6.2; §6.4 needs §§2.3, 3.3, 4.3, 6.3 and GeometricCurrents G1's constancy criterion (in code, `existsUnique_eq_ofFun_const_of_forall_lineDerivOp_eq_zero`).
- Serves defs: 53 (53.6), 65
- Evidence: README l.1302 "## Layer 6: monotonicity, densities and constancy", l.1306 "### 6.1" (*Needs* l.1350), l.1352 "### 6.2 The Riemannian monotonicity formula" (*Needs* l.1395 "Layer 4.1–4.4; RiemannianGeometry R4 item 1; HopfRinow Layer 2"), l.1399 "### 6.3 Densities" (*Needs* l.1468), l.1472 "### 6.4 The constancy theorem" (*Needs* l.1539); `Suggested.lean` `monotonicity_identity`, `densityRatio`, `constancy`.

### Layers 7–8 (§§7.1–7.6, 8.1–8.2) Varifold tangents, Allard's rectifiability theorem, rectifiable and integral compactness, tangent cones
- Status: NOT-STARTED.
- Ready now: no: Layer 7 needs Layers 1–4 and 6 (§7.1 *Needs* §§1.2, 1.4, 4.3, 4.5, 6.2–6.3); §8.1 needs §§4.5, 7.1–7.3; §8.2 needs §§6.3, 7.2, 7.6, 8.1.
- Serves defs: 53 (53.6), 65 (tangent cones)
- Evidence: README l.1592 "## Layer 7: varifold tangents, rectifiability and compactness" (*Needs* l.1631, l.1704, l.1739, l.1778, l.1890, l.1935), l.1949 "## Layer 8: tangent cones", l.1951 "### 8.1 Rectifiable tangent cones" (*Needs* l.1974), l.1976 "### 8.2 Integral tangent cones" (*Needs* l.1997); `Suggested.lean` `IsVarifoldTangent`, `isRectifiable_of_ae_density_pos`, `integral_compactness`, `IsVarifoldTangent.isIntegral`.

### §§9.1, 9.3, 9.4 Regular and singular sets, comparison with GeometricCurrents G6, statement-level acceptance tests (Simon, Edelen–Spolaor)
- Status: NOT-STARTED.
- Ready now: no: §9.1 needs §§1.3, 3.1, 4.1, 6.4; §9.3 needs Layers 1–8 and GeometricCurrents G1, G2, G5, G6 (G2 partial, G5 and G6 not started); §9.4 needs §§1.4, 2.2–2.3, 3.1, 4.3, 6.3, 7.2, 8.2, 9.1.
- Serves defs: 53, 65 (`sing^∞`, the cones `C_{p,q}`, Simon's theorem without its strict-stability clause)
- Evidence: README l.2008 "## Layer 9: regular sets, invariance, currents and acceptance statements", l.2010 "### 9.1 Regular and singular sets" (*Needs* l.2041), l.2074 "### 9.3 Comparison with GeometricCurrents G6" (*Needs* l.2098), l.2101 "### 9.4 Statement-level acceptance tests" (*Needs* l.2139).

## TauCetiRoadmap/GaussianIsoperimetryAndClusters
No STATUS.md (merged as roadmap PR #2420; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `weightedPerimeter`, `gaussianPerimeter`, `weightedVariation`, `isoperimetricProfile`, `modelProfile`, `gaussianSymmetral`: no hits. Every Tau Ceti declaration named in the *Needs* of Layers 1–4 is in code: the Gaussian distribution function and quantile (`TauCeti.Probability.cdf_gaussianReal_zero_one`, `strictMono_cdf_gaussianReal`, `hasDerivAt_cdf_gaussianReal`, `quantile_gaussianReal_zero_one`, `Real.hasDerivAt_erfInv`), projection laws (`TauCeti.Probability.map_orthogonalProjectionOnto_stdGaussian_pi`, `Submodule.map_orthogonalProjectionOnto_stdGaussian`, `stdGaussian_eq_withDensity_norm`), Euclidean BV and perimeter (`TauCeti.totalVariationOn`, `TauCeti.perimeter`, `variationMeasure`, `polarDensity`, `reducedBoundary`, `outerNormal`, `essentialBoundary`, `Convex.perimeter_lt_top`, `exists_subseq_tendsto_measure_symmDiff_inter_of_perimeter_le`, `integral_trace_fderiv_mul_indicator_eq_integral_inner_outerNormal`, `totalVariationOn_eq_lintegral_perimeter`, `reducedBoundary_congr_ae`, BV Poincaré `setLIntegral_enorm_sub_setAverage_le_mul_totalVariationOn_of_eq_ball`), `TestFunction.divergenceCLM`, `euclideanHausdorffMeasure_sphere`. Supplier roadmap items not in code: GeometricMeasureTheory G5's De Giorgi structure theorem and essential/reduced comparison (G5 partial), G6's bounded Lipschitz domains (G6 partial), G2's tangential area formula (G2 partial).

### Layer 1 (§§1.1–1.3) Gaussian isoperimetric function `I = φ ∘ Φ⁻¹`, Gaussian tails, orthogonal splitting
- Status: NOT-STARTED (no `gaussianIsoperimetricProfile`; the joint projection law is in code, the binary product form on `F × F^⊥` is not). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43577 (§1.1: `TauCeti.Probability.gaussianIsoperimetricProfile` with `gaussianIsoperimetricProfile_cdf`, `_one_sub`, `continuous_gaussianIsoperimetricProfile` and its derivatives, in Probability/Distributions/Gaussian/IsoperimetricProfile.lean; §§1.2–1.3 are not in it). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43645 (Probability/Distributions/Gaussian/OrthogonalSplitting.lean: §1.3 orthogonal splitting).
- Ready now: yes (*Needs* are the Mathlib and Tau Ceti Gaussian declarations above, all present; §1.2 needs §1.1).
- Serves defs: 55
- Evidence: README l.124 "## Layer 1: the standard Gaussian on the line and on Euclidean spaces", l.126 "### 1.1 The Gaussian isoperimetric function" (*Needs* l.135), l.143 "### 1.2 Gaussian tails" (*Needs* l.145 "§1.1"), l.152 "### 1.3 Orthogonal splitting" (*Needs* l.154); `Suggested.lean` `gaussianIsoperimetricProfile`.

### §§2.1, 2.4 Weighted variation and perimeter `P_μ`, `gaussianPerimeter`; lower semicontinuity and compactness
- Status: NOT-STARTED (`TauCeti.perimeter` with the Gaussian measure is not the Gaussian perimeter; no `weightedVariation`, `weightedPerimeter`, `gaussianPerimeter`). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43588 (§2.1: `TauCeti.weightedVariation`, `weightedPerimeter`, `gaussianWeight`, `gaussianPerimeter` with the weighted divergence theorem and elementary laws, in Analysis/BoundedVariation/Weighted.lean; the density-bounded form, the local comparison with `|Du|` and §2.4 are not in it).
- Ready now: yes for §2.1 (*Needs* Tau Ceti `TestFunction.divergenceCLM`, `TauCeti.totalVariationOn`, `TauCeti.perimeter`, Mathlib `TestFunction`, `ContDiffBump`); §2.4 needs §2.1 and Tau Ceti `exists_subseq_tendsto_measure_symmDiff_inter_of_perimeter_le` (in code).
- Serves defs: 55 (55.1)
- Evidence: README l.174 "### 2.1 Weighted variation and weighted perimeter" (*Needs* l.184), l.214 "### 2.4 Lower semicontinuity and compactness" (*Needs* l.216 "§2.1"); `Suggested.lean` `weightedVariation`, `weightedPerimeter`, `gaussianPerimeter`.

### §§2.2–2.3, 2.5–2.7 Weighted variation measure on the reduced boundary, explicit perimeters, weighted Gauss–Green, coarea, Gaussian invariance and cylinders
- Status: NOT-STARTED.
- Ready now: no: §2.2 needs §2.1 and GeometricMeasureTheory G5 (De Giorgi's theorem, essential versus reduced boundary; partial, the structure theorem is missing); §2.3 needs §2.2, G5's boundary criterion and G6 (bounded Lipschitz domains; partial); §2.5 needs §§1.3, 2.2 and G5; §2.6 needs §§2.1–2.2 and G2's coarea (partial); §2.7 needs §§1.3, 2.1, 2.5.
- Serves defs: 55 (55.2 is §2.2; §§2.3, 2.7 are on the chain to §§3.1, 3.4, 4.1–4.2)
- Evidence: README l.192 "### 2.2 Weighted variation is the weighted variation measure" (*Needs* l.194 "GeometricMeasureTheory G5 (De Giorgi's theorem, essential versus reduced boundary)"), l.201 "### 2.3" (*Needs* l.203), l.224 "### 2.5 Weighted Gauss–Green formula" (*Needs* l.226), l.234 "### 2.6 Weighted coarea formulas" (*Needs* l.236), l.244 "### 2.7 Gaussian invariance and cylinders" (*Needs* l.246); `Suggested.lean` `weightedPerimeter_eq_lintegral_reducedBoundary`.

### Layer 3 (§§3.1–3.5) Clusters, interfaces `Σ_ij`, interface quadratic form, isoperimetric profiles, existence of minimizing clusters
- Status: NOT-STARTED (the `Cluster` hits in Tau Ceti are cluster algebras).
- Ready now: no: §3.1 needs §§2.1, 2.7; §3.2 needs §§2.2, 3.1 and G5 (density one-half on the reduced boundary); §3.3 needs §§2.1, 3.2; §3.4 needs §§2.3, 3.1; §3.5 needs §§2.4, 3.1, 3.4.
- Serves defs: 55 (55.3 is §3.1, 55.4 is §3.2, the profile of 55.5 is §3.4)
- Evidence: README l.262 "## Layer 3: clusters and their interfaces", l.266 "### 3.1 Clusters" (*Needs* l.276 "§2.1, §2.7"), l.285 "### 3.2 The interface decomposition" (*Needs* l.287), l.296 "### 3.3" (*Needs* l.298), l.305 "### 3.4 Isoperimetric profiles and minimizing clusters" (*Needs* l.314), l.322 "### 3.5" (*Needs* l.324); `Suggested.lean` `Cluster`, `Cluster.perimeter`, `isoperimetricProfile`.

### Layer 4 (§§4.1–4.7) Model simplicial cluster, simplicial clusters in `E`, measure map, model profile, its boundary behaviour and differential identities, `I^{(q−1)} ≤ I_m^{(q−1)}`
- Status: NOT-STARTED.
- Ready now: no: §4.1 needs §§1.3, 2.3, 3.2; §4.2 needs §§2.7, 4.1; §§4.3–4.7 need §§4.1–4.2 with §§1.2, 2.5, 3.4.
- Serves defs: 55 (55.5 is §§4.1–4.2)
- Evidence: README l.340 "## Layer 4: model simplicial clusters and the model profile", l.344 "### 4.1 The canonical model cluster" (*Needs* l.353), l.363 "### 4.2 Simplicial clusters in a Euclidean space" (*Needs* l.371), l.380–425 §§4.3–4.7 (*Needs* l.382, l.393, l.407, l.417, l.427); `Suggested.lean` `modelCell`, `modelMeasureMap`, `modelProfile`, `isoperimetricProfile_le_modelProfile`.

## TauCetiRoadmap/RiemannianManifoldsWithConvexBoundary
No STATUS.md (merged as roadmap PR #2451; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `boundaryTangentSpace`, `IsBoundaryDefiningFunctionOn`, `IsStrictlyConvexAt`, `exitTime`, `exists_halfSpaceOutwardUnitNormal`: no hits. Its Tau Ceti suppliers are in code: boundary charts and outward vectors (`TauCeti.boundaryChartedSpace`, `mfderiv_subtypeVal_boundary`, `TauCeti.IsOutwardPointing`, `isOutwardPointing_iff_tangentCoordChange`, `tangentCoordChange_normal_pos`, `isManifold_boundary`), `TauCeti.Manifold.mgradient`, `TauCeti.Manifold.hessian` with `hessian_symm`, `hessian_apply_eq_mvfderiv_sub`, `Bundle.ContMDiffRiemannianMetric.restrictBoundaryTangentSpace`, `rescale`, `hessian_rescale`, `leviCivitaConnection_rescale_apply`, `ContMDiffNondegenerateMetricFamily`, regular sublevels (`scalarRegularSublevelChartedSpace`, `isManifold_scalarRegularSublevel`, `boundary_scalarRegularSublevel`), `TauCeti.EuclideanHalfSpace.collarDiffeomorph`, `TauCeti.SmoothEmbedding.normalExp`, `IsGeodesicCurveOn`, `IsGeodesicCurveOnFrom`, `geodesicInterval`. Supplier roadmap items not in code: DifferentialGeometry 12.5's outward unit normal `exists_halfSpaceOutwardUnitNormal`, RiemannianGeometry R7.9 and R5c (not started), GeometricTopology 1.1 (partial: `SmoothCollar` without existence) and 1.3 (not started), ComplexKahlerGeometry K5a's smooth half-space extension (the finite-order `exists_contDiff_extension_halfSpace`, Analysis/Sobolev/Trace/Reflection/HalfSpace.lean, is in code; the `C^∞` Seeley extension is not).

### §1.1 Tangent, inward and outward directions at the boundary (`boundaryTangentSpace`)
- Status: NOT-STARTED (`TauCeti.IsOutwardPointing` and the boundary charts exist; no `boundaryTangentSpace` or trichotomy). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43579 (§1.1: `TauCeti.boundaryTangentSpace`, `boundaryTangentSpace_eq_euclideanHalfSpaceBoundary`, `finrank_boundaryTangentSpace`, the trichotomy `isOutwardPointing_or_mem_boundaryTangentSpace_or_isOutwardPointing_neg`, in Geometry/Manifold/Boundary/TangentSpace.lean).
- Ready now: yes (*Needs* are the Tau Ceti boundary-chart declarations above and DifferentialGeometry 5.1's outward-pointing interface, `TauCeti.IsOutwardPointing`, all present).
- Serves defs: 66, 49
- Evidence: README l.457 "### 1.1 Tangent, inward and outward directions" ("Define the tangent space of the boundary at `q ∈ ∂M`, `boundaryTangentSpace q`"); *Needs* l.487; `Suggested.lean` `boundaryTangentSpace`.

### §§1.2–1.6 Unit normals, boundary defining functions, second fundamental form `II`, Weingarten map, principal and mean curvature, conformal change
- Status: NOT-STARTED (flat-ambient `TauCeti.secondFundamentalForm`/`shapeOperator` only; no boundary `II`, `IsBoundaryDefiningFunctionOn` or Weingarten map).
- Ready now: no: §1.2 needs §1.1 and DifferentialGeometry 12.5 `exists_halfSpaceOutwardUnitNormal` (not in code; DifferentialGeometry STATUS 53c246b Layer 12 remaining "the divergence theorem with boundary (12.5)"); §1.3 needs §§1.1–1.2; §1.4 needs §§1.1–1.3 and DifferentialGeometry 12.3 (`hessian`, in code); §1.5 needs §1.4; §1.6 needs §§1.2, 1.4–1.5.
- Serves defs: 66 (66.1, 66.2(a)), 49 (§§1.4–1.5: II, Weingarten map, principal curvatures, `H = tr S / n` for a boundary)
- Evidence: README l.491 "### 1.2 The outward and inward unit normal" (*Needs* l.525 "DifferentialGeometry 12.5 (`exists_halfSpaceOutwardUnitNormal`) and 12.2"), l.528 "### 1.3 Boundary defining functions" (*Needs* l.558), l.563 "### 1.4 The second fundamental form" (*Needs* l.598), l.603 "### 1.5 Weingarten map, principal curvatures and mean curvature" (*Needs* l.625), l.627 "### 1.6 Conformal change and scaling" (*Needs* l.654); `Suggested.lean` `IsBoundaryDefiningFunctionOn`, `secondFundamentalForm`.

### §§2.1–2.3 Convexity predicates, Hessian characterisation, openness, uniform bounds and families of metrics
- Status: NOT-STARTED.
- Ready now: no: §2.1 needs §§1.4–1.6; §2.2 needs §§1.3–1.4, 2.1; §2.3 needs §§1.4–1.6, 2.1 and Tau Ceti `ContMDiffNondegenerateMetricFamily.contMDiffAt_christoffelSymbol` (in code).
- Serves defs: 66 (66.3 and Remarks), 49 (§2.1, strict convexity iff all principal curvatures are positive)
- Evidence: README l.673 "## Layer 2: Convexity of the boundary", l.675 "### 2.1 Convexity predicates" (*Needs* l.708 "1.4, 1.5, 1.6"), l.710 "### 2.2 Hessian characterisation" (*Needs* l.728), l.730 "### 2.3" (*Needs* l.760); `Suggested.lean` `IsStrictlyConvexAt`, `IsStrictlyConvexBoundary`, `isStrictlyConvexAt_iff_hessian_neg`.

### §§3.1, 3.3–3.5 Regular domains, defining functions on the collar extension and the double, extension of metrics across the boundary, realisation as `{ρ̃ ≥ 0}` in a boundaryless manifold
- Status: NOT-STARTED (inputs in code: regular sublevels as manifolds with boundary, `TauCeti.SmoothCollar`, `EuclideanHalfSpace.collarDiffeomorph`, the finite-order half-space extension; no regular-domain structure, collar extension, double or realisation theorem).
- Ready now: no: §3.1 needs §§1.1–1.4 and RiemannianGeometry R7.9 (not started); §3.3 needs §3.1 and GeometricTopology 1.1 (partial: collar existence missing) and 1.3 (not started); §3.4 needs §3.1 and ComplexKahlerGeometry K5a's `C^∞` half-space extension (not in code); §3.5 needs §§3.1, 3.3–3.4, GeometricTopology 1.1, 1.3 and RiemannianGeometry R5c (not started).
- Serves defs: 66 (the boundaryless extension used by §§4.1–4.4)
- Evidence: README l.775 "### 3.1 Regular domains" (*Needs* l.836 "1.1–1.4; RiemannianGeometry R7.9 ..."), l.883 "### 3.3 Defining functions on the collar extension and the double" (*Needs* l.945), l.950 "### 3.4 Extension of functions and metrics across the boundary" (*Needs* l.975), l.979 "### 3.5 The realisation theorem" (*Needs* l.1027); `Suggested.lean` `exists_isSmoothEmbedding_regularDomain`.

### §§4.1–4.2 Geodesics of a regular domain, second-order contact with the boundary
- Status: NOT-STARTED (`TauCeti.Manifold.IsGeodesicCurveOn`, `IsGeodesicCurveOnFrom`, `geodesicInterval` and `RiemannianIsometry.isGeodesicCurveOn_comp_iff` exist; no boundary-contact formula).
- Ready now: no: §4.1 needs §§3.1, 3.5 (HopfRinow Layer 1 complete); §4.2 needs §§1.1, 1.3–1.4, 2.1–2.2, 3.1, 4.1.
- Serves defs: 66 (66.2(c): `(ρ∘γ)''(0) = −|dρ| II(u,u)`, tangent geodesics leave)
- Evidence: README l.1080 "### 4.1 Geodesics of a regular domain" (*Needs* l.1111), l.1116 "### 4.2 Second-order contact with the boundary" (*Needs* l.1156); `Suggested.lean` `not_exists_isGeodesicCurveOnFrom_of_isStrictlyConvexAt`, `mem_interior_of_isGeodesicCurveOn`.

### §§4.3–4.4 Normal exponential and signed distance of a hypersurface, boundary normal coordinates
- Status: NOT-STARTED (`TauCeti.SmoothEmbedding.normalExp` with `exists_partialDiffeomorph_normalExp_subset`, `exists_isClosedEmbedding_normalExp_norm_le_subset`, and `isSmoothEmbedding_coe_regularLevel` exist; no signed distance or boundary normal coordinates `g = dr² + h_r`).
- Ready now: no: §4.3 needs §§1.3, 3.1 and RiemannianGeometry R7.9 (normal collar, not started); §4.4 needs §§1.4, 4.3 and GeometricTopology 1.1 (partial: collar existence missing).
- Serves defs: 66 (66.2(b): `II = −½ ∂_r h_r|₀`)
- Evidence: README l.1160 "### 4.3 The normal exponential and signed distance of a hypersurface" (*Needs* l.1229), l.1236 "### 4.4 Boundary normal coordinates" (*Needs* l.1290 "1.4, 4.3; GeometricTopology 1.1 (smooth collars)").

## TauCetiRoadmap/AlgebraicModularFormsAndSerreWeights
No STATUS.md (merged as roadmap PR #928; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `higherWeight_attachment|ClassicalModularGalois`, `KodairaSpencer`, `GaussManin|logDeRham`, `GeometricModularForm|KatzModularForm`, `hodgeFricke` in TauCeti/: empty. Its Tau Ceti suppliers are in code: `HeckeRing.GL2.EigenformAwayFromLevel` with `qExpansion_coeff_eq_eigenvalue_mul_coeff_one` (NumberTheory/ModularForms/Newforms/Eigenform.lean), `TauCeti.frickeGL` (ModularForms/Fricke/Matrix.lean), `TauCeti.symPowerRep` (RepresentationTheory/ClassicalGroups/SymmetricPower/Basic.lean), `TauCeti.ContinuousRep`.

### §§1.1–1.3, 1.6 Geometric modular forms, cusp forms, coefficient maps, integral logarithmic de Rham extension
- Status: NOT-STARTED.
- Ready now: no: §1.1 needs ModularCurvesPartII §§4.1–4.4, 7.1–7.1a, 5.21 (not started); §1.2 needs §1.1 and ModularCurvesPartII §§4.1–4.4; §1.3 needs §§1.1–1.2; §1.6 needs §1.1, AbelianSchemesAndArithmeticModuli §A4.3 (not started), ModularCurvesPartII §§4.4, 7.1–7.1a and ComplexComparisonPartII C5.6 (not started).
- Serves defs: 69 (§1.6 is the de Rham input of §6.1; §§1.1–1.3 are inputs of §1.6 and §3.11)
- Evidence: README l.110 "## Layer 1: Geometric forms and comparison"; l.114 "### 1.1 Geometric modular forms" (*Needs* l.138), l.142 "### 1.2 Cusp forms and the cusp ideal" (*Needs* l.162), l.166 "### 1.3 Functorial coefficient maps" (*Needs* l.186), l.226 "### 1.6 Integral elliptic logarithmic de Rham extension" (*Needs* l.238 "§1.1 Geometric modular forms; AbelianSchemesAndArithmeticModuli §A4.3; ModularCurvesPartII §§4.4, 7.1–7.1a; ComplexComparisonPartII C5.6").

### §§2.10, 2.13–2.14, 3.11 Diamonds on coherent cohomology, auxiliary Fricke map, Fricke on Hodge powers, root-dependent Hodge Fricke operator
- Status: NOT-STARTED (only the analytic `TauCeti.frickeGL` and Atkin–Lehner operators on analytic forms are in code).
- Ready now: no: §3.11 needs ModularCurvesPartII §9.3 (not started), §1.3 and §2.14; §2.14 needs §§2.10, 2.13; §2.10 needs §§1.1–1.2 and ModularCurvesPartII §9.2; §2.13 needs ModularCurvesPartII §§9.1–9.2, 2.6–2.7, 3.7, 3.1–3.2, 3.9 (none started).
- Serves defs: 69
- Evidence: README l.432 "### 2.10 Diamonds on coherent cohomology" (*Needs* l.452), l.503 "### 2.13 The auxiliary curve Fricke map" (*Needs* l.527), l.531 "### 2.14 Fricke on Hodge powers" (*Needs* l.555 "§2.10 ...; §2.13 ..."), l.825 "### 3.11 The root-dependent Hodge Fricke operator" (*Needs* l.847 "ModularCurvesPartII §9.3; §1.3 Functorial coefficient maps; §2.14 Fricke on Hodge powers").

### §§6.1–6.2 Classical rank-two cohomological summand, λ-adic attachment `higherWeight_attachment`
- Status: NOT-STARTED (the milestone is stated in the roadmap's Suggested.lean l.101; no Tau Ceti counterpart).
- Ready now: no: §6.1 needs §1.6, ModularCurvesPartII §§14.1–14.4a, 14.11, ModularCurves Layers 5 and 10 (Layer 10 untouched), EtaleCohomologyFoundations §§0.6, 0.8, 0.11, F.0–F.6 (§F.0.1 partial, the rest not started), ComplexComparisonPartII §§C6.3–C6.6, JacobianChallenge Layers A–B (partial), SchemeAndStackFoundations §§2.19–2.21, 3.3; §6.2 needs §6.1, §3.11, ModularCurvesPartII §9.3, ArithmeticGaloisRepresentations Layers 1 and 5 and §2.3 (partial: `ContinuousRep` carrier and integral models in code).
- Serves defs: 69 (§6.2 is Definition 69.1 with its existence theorem)
- Evidence: README l.1389 "## Layer 6: Classical Galois attachments"; l.1395 "### 6.1 The classical rank-two cohomological summand" (*Needs* l.1426); l.1430 "### 6.2 Classical eigenforms of weight at least two" (`TauCetiRoadmap.AlgebraicModularFormsAndSerreWeights.ClassicalModularGalois.higherWeight_attachment`; *Needs* l.1456 "§6.1 ...; §3.11 ...; ModularCurvesPartII §9.3 ..."); Dependencies l.1521.

## TauCetiRoadmap/ModularCurvesPartII
No STATUS.md (merged as roadmap PR #913; Tau Ceti checked at 91942aa9f, 2026-11-19). Tau Ceti's TauCeti/AlgebraicGeometry/ModularCurve/ has the moduli problems `[Γ₁(N)]`, `[Γ₀(N)]` (`ModuliProblem.gammaZero`, Gamma/Zero.lean), naive levels, `Y₁(N)`, the Legendre and level-three lines and rigidifier quotients (the merged ModularCurves layers); grep `levelStack`, `levelGamma0`, `projectiveIndex`, `integralCoarseCurve`, `modularJacobian`, `jacobianNorm`, `heckeUpper`, `heckeAlgebraUpper`, `weightCoefficients`, `relativeEtaleH1`, `modularBorelSerreComparison`, `perfectHeckePairing`, `atkinLehnerExact`, `jacobianTateModule` in TauCeti/: empty. The analytic map `Γ₁(N)\ℍ → Y₁(N)(ℂ)` in Tate normal form coordinates is in code: `TauCeti.gamma1QuotientEquivTateNormalForm` (`Γ₁(N)\ℍ` in bijection with the Tate normal forms with `(0, 0)` of exact order `N ≥ 4`) with the holomorphy of its coefficients, `UpperHalfPlane.tateNormalFormCoeffs_pointedWeierstrassCurve_eq_iff` (Analysis/SpecialFunctions/Elliptic/Gamma1/TateNormalForm.lean); it does not enter the items below.

### §3.8 Open level subgroups and the standard levels
- Status: NOT-STARTED (no `levelGamma0`, `levelGamma1`, `splitCartanNormalizer`, `nonsplitCartan`, `projectiveIndex`, `levelDet`, `levelPullback` in Tau Ceti; `levelConjEquiv` in NumberTheory/ClassFieldTheory/Formation/Conjugation.lean is unrelated). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43611 (NumberTheory/ModularForms/CongruenceSubgroups/LevelSubgroup.lean: the standard level subgroups of `GL₂(ℤ/N)`, projective index and determinant image).
- Ready now: yes: every listed declaration is a finite-group statement over Mathlib `Matrix.GeneralLinearGroup`, `Subgroup.index`, `Subgroup.normalizer`, `CongruenceSubgroup.Gamma0/Gamma1/Gamma`. The *Needs* line also cites ModularCurves Layer 9B (Layers 6.2 and 9.5, the standard quotient problems; STATUS "quotient problems" remaining), which fixes the right-action convention and does not enter these declarations.
- Serves defs: 77 (the levels `H ⊆ GL₂(Ẑ)` of the tower); 69, 71 through §3.9, §3.12 and §5.2
- Evidence: README l.1110 "### 3.8 Open level subgroups and the standard levels" (interface `levelGamma0`, `levelGamma1`, `levelGamma1Mu`, `splitCartan`, `nonsplitCartan`, `projectiveIndex`, `levelDet`, `levelPullback`, `levelGamma0_comap`, `levelConj`; *Needs* l.1146 "Mathlib `Matrix.GeneralLinearGroup` ...; ModularCurves Layer 9B"); ModularCurves README l.4546 label table "Layer 9B | Layer 6.2 (after inverting `N`) and Layer 9.5 (over `ℤ`)".

### §3.12 The Deligne–Rapoport level-H stack `levelStack`
- Status: NOT-STARTED.
- Ready now: no: needs §2.11 (polygon-count stacks), §3.9 (which needs §3.8, §2.11, ModularCurves Layers 0C, 0D, 3N, 5B, 9A, 9D), AlgebraicModuliForArithmeticGeometry §5.4 `DMNormalization`, SchemeAndStackFoundations §§0.20, 1.1, 1.19, 1.22 (not started; §1.18 partial) and the finite-normal recognition contract of ModularCurves Layer 10 (untouched).
- Serves defs: 77 (finite-level terms `Y(K_pK^p)` with level maps and conjugation isomorphisms); 69, 71 through §5.2
- Evidence: README l.1220 "### 3.12 The Deligne–Rapoport level-H stack" (`levelStack`, `levelStack.map`, `levelStack.conj`, `levelStack.ellipticOpen`; *Needs* l.1251); §3.9 *Needs* l.1183.

### §§5.2–5.3 Integral coarse modular curves and their base change
- Status: NOT-STARTED (no `integralCoarseCurve`; merged ModularCurves Layer 6 coarse moduli schemes are also not in code, STATUS Layer 6 "coarse moduli schemes, the curves Y_H" remaining).
- Ready now: no: §5.2 needs §§3.2, 3.4, 3.9, 3.12, 4.1, 5.1, SchemeAndStackFoundations §1.23 `keel_mori` and AlgebraicModuliForArithmeticGeometry §7.5; §5.3 needs §5.2 and AlgebraicModuliForArithmeticGeometry §5.1.
- Serves defs: 71 (`X₀(N)` over `ℚ`; §13.1 needs §§5.2–5.3); 69 through §9.3
- Evidence: README l.1644 "## Layer 5: Integral coarse modular curves"; l.1665 "### 5.2 Integral coarse modular curves" (`integralCoarseCurve`, `integralCoarseCurve_levelMap`; *Needs* l.1687), l.1691 "### 5.3 Base change for coarse modular curves" (*Needs* l.1702).

### §9.3 Cyclotomic Fricke involution
- Status: NOT-STARTED (the analytic `TauCeti.frickeGL` and Atkin–Lehner operators on forms are in code; no curve involution or universal isogeny).
- Ready now: no: needs §4.1, §5.2, §9.2 (not started), ModularCurves Layers 2B (partial: "2.2 quotients E/C" remaining), 2E (Cartier–Nishi duality and the Weil pairing, remaining) and 10 (untouched), ModularForms Layer 6.
- Serves defs: 69 (curve map and universal isogeny for AlgebraicModularFormsAndSerreWeights §§3.11, 6.2); 71 through §§9.4, 13.4
- Evidence: README l.2616 "### 9.3 Cyclotomic Fricke involution" (`atkinLehner`, `atkinLehner_sq`, `atkinLehner_changeRoot`; *Needs* l.2643 "§4.1; §5.2; §9.2; Tau Ceti `TauCeti.frickeGL`; ...; ModularCurves Layer 2B; ModularCurves Layer 2E; ModularCurves Layer 10").

### §§13.1–13.3 Modular Jacobians and norms, upper and lower Jacobian Hecke operators, geometric integral Hecke algebra
- Status: NOT-STARTED (Tau Ceti inputs in code: `Divisor.conorm`, `Divisor.conorm_principal`, `Divisor.finrank_mul_degree_conorm`, cited by §13.2's function-field step; no `modularJacobian`, `jacobianNorm`, `heckeUpper`, `heckeLower`, `heckeAlgebraUpper`).
- Ready now: no: §13.1 needs JacobianChallengePartII §§1.2–1.4 (not started), JacobianChallenge Layers D–E (partial; no Jacobian scheme), SchemeAndStackFoundations §3.5 `lineBundleNorm` (not in code), §§5.2–5.3, StableReduction Layer 2, AbelianSchemesAndArithmeticModuli A2.2–A2.5, A6.25; §13.2 needs §§7.2–7.4, 9.1, 9.2, 9.10, 9.12, 10.2, 13.1, JacobianChallenge Layers B, E, F; §13.3 needs §13.2 and AbelianSchemesAndArithmeticModuli A4.1, A6.7.
- Serves defs: 71
- Evidence: README l.3236 "## Layer 13: Jacobian functoriality and the integral Hecke action"; l.3238 "### 13.1 Modular Jacobians and norms" (*Needs* l.3280 "`JacobianChallengePartII` §§1.2–1.4 ..."), l.3286 "### 13.2 Upper and lower Jacobian Hecke operators" (*Needs* l.3299, l.3325), l.3329 "### 13.3 The geometric integral Hecke algebra" (*Needs* l.3360).

### §§14.1–14.4a, 14.11 Geometric weight coefficient systems, finite and adic parabolic cohomology, integral comparison and change of level, parabolic Poincaré pairing
- Status: NOT-STARTED (Tau Ceti has the topological `TauCeti.LocalCoefficientSystem` with `pullback` and `SymmetricPower.finrank_eq`, cited by §14.1; no `weightCoefficients`, `relativeEtaleH1`, `relativeBettiH1`, `modularBorelSerreComparison`).
- Ready now: no: §14.1 needs §§3.2, 3.5, 4.12, AbelianSchemesAndArithmeticModuli §A4 and EtaleCohomologyFoundations §§F.1–F.4 (not started); §§14.2–14.3 need §14.1 and AlgebraicTopology Stages 2, 6; §14.4a needs FuchsianOrbifolds Layers 2–4, ArithmeticLocallySymmetricSpaces §§ALS.F.3, ALS.1.4, ALS.2.1–ALS.2.4, ALS.5a.3–ALS.5a.5, ComplexComparisonPartII §§C6.1, C6.3–C6.6; §14.4 needs §14.4a and ALS.1.1–ALS.1.8 (not started); §14.11 needs §§14.4, 14.7–14.10 and EtaleCohomologyFoundations §0.11 `curveDuality`.
- Serves defs: 69 (via AlgebraicModularFormsAndSerreWeights §6.1), 77 (finite and adic étale cohomology with change of level); 71 through §§14.5, 14.13–14.14
- Evidence: README l.3496 "## Layer 14: Cohomological realizations and parabolic lattices"; l.3498 "### 14.1 Geometric weight coefficient systems" (*Needs* l.3525), l.3529 "### 14.2 Finite and adic parabolic cohomology" (*Needs* l.3550), l.3554 "### 14.3 Boundary and interior cohomology" (*Needs* l.3571), l.3575 "### 14.4 Integral comparison and change of level" (*Needs* l.3595), l.3599 "### 14.4a The modular Borel–Serre pair and adic adapter" (*Needs* l.3620), l.3754 "### 14.11 Parabolic Poincaré pairing" (*Needs* l.3778).

### §§7.6, 9.1, 9.2, 9.4, 13.4, 14.5, 14.13–14.14 Further inputs of §16.5
- Status: NOT-STARTED (no `perfectHeckePairing`, `heckeLevelStack`, `atkinLehnerExact`, `jacobianTateModule` in Tau Ceti).
- Ready now: no: §7.6 needs §7.5; §§9.1, 9.2, 9.4 need §§4.1, 5.2 (and §9.4 needs §9.3); §13.4 needs §§9.2, 9.3, 9.12, 13.2 and AbelianSchemesAndArithmeticModuli A3.7; §14.5 needs §§7.1–7.4, 9.11, 13.1, 13.2, 14.4; §14.13 needs §§13.4, 13.5, 14.4 and JacobianChallenge Layer F (partial); §14.14 needs §§14.5, 14.7, 14.13.
- Serves defs: 71
- Evidence: README l.2396 "### 7.6 Perfection of the full Hecke pairing" (*Needs* l.2416), l.2560 "### 9.1 Compactified Hecke degeneracy maps" (*Needs* l.2586), l.2590 "### 9.2 Diamond operators" (*Needs* l.2612), l.2647 "### 9.4 Exact-divisor Atkin–Lehner operators" (*Needs* l.2670), l.3366 "### 13.4 Polarization and Hecke adjoints" (*Needs* l.3377), l.3624 "### 14.5 The weight-two Shimura isomorphism is Hecke-equivariant" (*Needs* l.3638), l.3803 "### 14.13 The actual Jacobian Tate realization" (*Needs* l.3817), l.3821 "### 14.14 `H¹` is free of rank two over the Hecke algebra" (*Needs* l.3835); all cited by §16.5's *Needs* l.4196.

### §§16.1–16.3, 16.5 Hecke prime, `A_f = J₁(N)/B_f`, Shimura's dimension theorem, `A_f⁰ := J₀(N)/B_f⁰`
- Status: NOT-STARTED (Tau Ceti has the field carrier `TauCeti.AlgebraicGeometry.AbelianVariety` with `IsIsogeny` and the Hecke algebra on newforms, NumberTheory/ModularForms/Newforms/Hecke/; no Hecke prime `p_f` or modular quotient).
- Ready now: no: §16.1 needs §13.3; §16.2 needs §§13.1–13.3, 16.1, CyclotomicClassGroupsAndStickelberger §4.3 (not started) and NeronModelsAndSemistableAbelianVarieties §5.1 (not started); §16.3 needs §§14.14, 16.1–16.2 and AbelianSchemesAndArithmeticModuli A4, A6.5; §16.5 needs §§7.6, 9.1, 9.2, 9.4, 13.1, 13.2, 13.4, 14.5, 14.13, 14.14, 16.1–16.3, CyclotomicClassGroupsAndStickelberger §4.3, AbelianSchemesAndArithmeticModuli A3.2, A4, A6.5, SchemeAndStackFoundations §0.7.
- Serves defs: 71 (§16.5 is the definition as stated; §16.2 is its Remark 4 version)
- Evidence: README l.4096 "## Layer 16: Weight-two modular abelian quotients"; l.4098 "### 16.1 The Hecke prime and coefficient field of a newform" (*Needs* l.4115), l.4119 "### 16.2 The modular abelian variety `A_f`" (*Needs* l.4134), l.4138 "### 16.3 Tate module and Shimura's dimension theorem" (*Needs* l.4153), l.4174 "### 16.5 Trivial character: the quotient of `J₀(N)`" (`modularQuotientGamma0_norm_pull`; *Needs* l.4196).

## TauCetiRoadmap/JacobianChallengePartII
No STATUS.md (merged as roadmap PR #1225; Tau Ceti checked at 91942aa9f, 2026-11-19). Its Tau Ceti suppliers are in code: `relativePicardFppfSheaf`, `relativePicardFiberDegree`, `relativePicardDegreeZeroFppfSheaf`, `relativePicardPresheafBaseChangeIso`, `graphDivisor`, `graphDivisorDegreeOne`, `abelMap`, `abelJacobiMapOfDegree` (TauCeti/AlgebraicGeometry/PicardFunctor/, EffectiveCartierDivisor/), `InvertibleSheaf.pullback`, `LineBundleClass.IsAmple`. Grep `RelativeJacobian`, `invertibleSheafDescends`, `exists_locallyConstant_relativePicardFiberDegree`, `picardComponent`, `AbelianScheme`, `normalizedPoincare`, `thetaDivisor|twiceTheta` in TauCeti/: empty.

### Layer 0 (§§0.0–0.4) Finite-stage descent of line bundles, relative degree components, relative curve Picard scheme, degree torsors
- Status: NOT-STARTED.
- Ready now: no: §0.0 needs SchemeAndStackFoundations §0.9 (partial: limits with affine transitions and affine noetherian approximation in TauCeti/AlgebraicGeometry/Limits/AffineTransition.lean and NoetherianApproximation.lean; STATUS "0.9 non-affine approximation" remaining) and JacobianChallenge Layers A and C (partial); §§0.1–0.2 need §0.0 and JacobianChallenge Layers A–C; §0.3 needs SchemeAndStackFoundations §4.14 (not started), JacobianChallenge Layer D (partial), ComplexComparisonPartII §§C3.2d.2–C3.2d.3, C3.2f.1–C3.2f.2 and AlgebraicModuliForArithmeticGeometry §7.3; §0.4 needs §0.3.
- Serves defs: 30, 71, 80 (inputs of §§1.1–1.2 and 2.1–2.2)
- Evidence: README l.120 "## Layer 0: Relative Picard degree components and torsors"; l.126 "### 0.0 Finite-stage descent of line bundles" (`RelativeJacobian.invertibleSheafDescends`; *Needs* l.141 "SchemeAndStackFoundations §0.9 ...; JacobianChallenge, Layers A and C"), l.143 "### 0.1" (*Needs* l.151), l.153 "### 0.2" (*Needs* l.172), l.174 "### 0.3 Relative curve Picard scheme" (*Needs* l.196 "... SchemeAndStackFoundations §4.14 (`hilbert_quot_schemes`) ..."), l.198 "### 0.4 Picard degree torsors" (*Needs* l.217).

### Layer 1 (§§1.1–1.4, 1.3a) Relative Jacobian `J(X/S)`, base change, curve determinant, canonical principal polarization
- Status: NOT-STARTED.
- Ready now: no: §§1.1–1.2 need §0.3, JacobianChallenge Layers D–E (partial; no Jacobian scheme, no Layer E milestone) and AbelianSchemesAndArithmeticModuli A0.1 (not started); §1.3 needs §§1.2, 0.2 and AlgebraicModuliForArithmeticGeometry §7.6.1; §1.3a needs §0.0, PadicMeasuresIwasawaAlgebras §5.1 `detLine`, AlgebraicVectorBundles L0C, SchemeAndStackFoundations §1.1; §1.4 needs §§1.2, 1.3, 1.3a, 2.1, 2.2 and AbelianSchemesAndArithmeticModuli A2.2, A2.3, A2.5.
- Serves defs: 30 (Remark 3: `λ_X`), 71 (through ModularCurvesPartII §13.1), 80
- Evidence: README l.227 "## Layer 1: Relative Jacobians and principal polarization"; l.233 "### 1.1 Properness of the relative Jacobian" (*Needs* l.239), l.241 "### 1.2 Relative Jacobian" (*Needs* l.263), l.265 "### 1.3 Base change of the relative Jacobian" (*Needs* l.271), l.273 "### 1.3a Determinant of curve cohomology" (*Needs* l.288), l.290 "### 1.4 Canonical principal polarization" (*Needs* l.311).

### Layer 2 (§§2.1–2.2) Section-free Abel map, degree-`d` Abel–Jacobi morphisms `i_α`
- Status: NOT-STARTED (the Abel maps on functors of points `abelMap`, `abelJacobiMapOfDegree` are in code, PicardFunctor/Abel/; no morphism to a represented Jacobian).
- Ready now: no: §2.1 needs §§0.3–0.4; §2.2 needs §§2.1, 0.4, 1.2.
- Serves defs: 30 (§2.2); 71, 80 through §1.4
- Evidence: README l.321 "## Layer 2: Abel maps and section-free differences"; l.327 "### 2.1 Section-free Abel map" (*Needs* l.345 "§0.3; §0.4; Tau Ceti `graphDivisor`, ..."), l.347 "### 2.2 Degree-d Abel–Jacobi morphism" (*Needs* l.366 "§2.1; §0.4; §1.2").

### §§3.1–3.3 Normalized Poincaré bundle, theta divisor `θ_α` for a degree-one class, canonical twice-theta bundle `Θ_X`
- Status: NOT-STARTED.
- Ready now: no: §3.1 needs §1.4 and AbelianSchemesAndArithmeticModuli A2.2–A2.3; §3.2 needs §2.2 and JacobianChallenge Layers C and E (partial; §E.5 theta not started); §3.3 needs §3.1 and AbelianSchemesAndArithmeticModuli A2.6 `Polarization.graphBundle`.
- Serves defs: 30 (`θ_α`, `Θ = Δ^*(P^∨)`), 80 (`Θ_X` for `ĥ = ½ĥ_Θ`)
- Evidence: README l.455 "## Layer 3: Poincaré normalization and twice-theta"; l.463 "### 3.1 Normalized Jacobian Poincaré bundle" (*Needs* l.481), l.483 "### 3.2 Theta divisor with a degree-one class" (*Needs* l.503 "§2.2; JacobianChallenge, Layer C; JacobianChallenge, Layer E"), l.505 "### 3.3 Canonical twice-theta bundle" (*Needs* l.524).

### §§3.4–3.6, 3.9 Theta pullbacks, Poincaré addition and diagonal identities
- Status: NOT-STARTED.
- Ready now: no: §3.4 needs §§3.2, 2.2 and JacobianChallenge Layer B (partial); §3.5 needs §§3.2, 3.4 and JacobianChallenge Layer B; §3.6 needs §§3.1, 3.2, 1.4 and AbelianSchemesAndArithmeticModuli A2.3 `mumfordMap`; §3.9 needs §3.6 and AbelianSchemesAndArithmeticModuli §A1.5 `relativeCube` (not started).
- Serves defs: 30 (§3.5 `[−1]^*θ_α = t_κ^*θ_α`, on §3.4); 30, 80 through §3.10, which needs §3.9 and so §3.6
- Evidence: README l.526 "### 3.4 Pullback of inverse theta" (*Needs* l.540, l.554), l.556 "### 3.5 Pullback of theta" (*Needs* l.568), l.570 "### 3.6 Poincaré addition identity" (*Needs* l.578), l.594 "### 3.9 Poincaré diagonal identity" (*Needs* l.608 "§3.6; AbelianSchemesAndArithmeticModuli §A1.5 (`relativeCube` ...)").

### §§3.10–3.13 Geometric-fibre twice-theta class, symmetry, zero rigidification, relative ampleness
- Status: NOT-STARTED.
- Ready now: no: §3.10 needs §§3.3, 3.9, 1.3 and AbelianSchemesAndArithmeticModuli A2.6; §§3.11–3.12 need §§3.1, 3.3; §3.13 needs §§3.10, 3.3, 1.1 and StableReduction Layer 2.
- Serves defs: 30, 80
- Evidence: README l.610 "### 3.10 Geometric fibre twice-theta class" (*Needs* l.616), l.618 "### 3.11 Symmetry of twice-theta" (*Needs* l.624), l.626 "### 3.12 Zero rigidification of twice-theta" (*Needs* l.632), l.634 "### 3.13 Relative ampleness of twice-theta" (*Needs* l.640).

## TauCetiRoadmap/NeronModelsAndSemistableAbelianVarieties
No STATUS.md (merged as roadmap PR #852; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `NeronMappingProperty`, `NeronModel`, `WeakNeronModel`, `HasGoodModel`, `DifferentialLattice`, `SemistableReduction`, `FiniteSeparableSemistableExtension`, `NeronOggShafarevich`, `ConnectedNeronLocalization`, `AbelianScheme` in TauCeti/: empty. Tau Ceti inputs in code: the field carrier `TauCeti.AlgebraicGeometry.AbelianVariety`, `IdealSheafData.IsEffectiveCartier` (EffectiveCartierDivisor/Basic.lean), `FiniteTypeCommHopfAlgCat.identityComponentSpec` (Algebra/AlgebraicGroup/Connected/GroupScheme.lean), `componentGroupScheme` (Connected/ComponentGroup/FiniteEtale.lean).

### §§1.1–1.4, 1.6, 1.10 Néron mapping property, marked models, extension of generic morphisms, uniqueness, weak Néron models, étale base change
- Status: NOT-STARTED. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43593 (§§1.1–1.4: `NeronMappingProperty`, `NeronModel`, `NeronModel.extend`, `NeronModel.unique_iso`, in AlgebraicGeometry/NeronModel/; §§1.6 and 1.10 are not in it).
- Ready now: yes: §1.1 needs only Mathlib `AlgebraicGeometry.Smooth` and `CategoryTheory.Over.pullback`; §§1.2–1.4, 1.6 and 1.10 need only earlier sections of this group and Mathlib (`IsSeparated`, `QuasiCompact`, `Etale`, `Smooth`).
- Serves defs: 78 (§1.4 uniqueness), 85 (§§1.1–1.4); 87, 89 through §§1.8–1.9; §1.10 feeds §3.1 for 85
- Evidence: README l.724 "## Layer 1: Néron models and their uniqueness"; l.737 "### 1.1 The Néron mapping property" (*Needs* l.757 "Mathlib `AlgebraicGeometry.Smooth`, `CategoryTheory.Over.pullback`"), l.785 "### 1.2 Marked finite-type Néron models" (`NeronModel`; *Needs* l.805 "1.1; Mathlib `IsSeparated`, `QuasiCompact`"), l.818 "### 1.3 Extension of generic morphisms" (*Needs* l.831 "1.1, 1.2"), l.850 "### 1.4 Uniqueness of marked Néron models" (`NeronModel.unique_iso`; *Needs* l.862 "1.3"), l.887 "### 1.6 Weak Néron models" (*Needs* l.902 "1.2; Mathlib `Etale`"), l.1113 "### 1.10 Étale and unramified base change" (*Needs* l.1124 "1.2, 1.4; Mathlib ...").

### §§1.5, 1.7–1.9 Group law, smoothening and local existence, abelian schemes are Néron models, Dedekind local-to-global construction
- Status: NOT-STARTED.
- Ready now: no: §1.5 needs §§1.3–1.4 and AbelianSchemesAndArithmeticModuli A0.1–A1 (not started; §A0.1 ready); §1.7 needs §§1.5–1.6 and SchemeAndStackFoundations §§0.16, 0.20–0.21 (STATUS "0.20-0.21" remaining) and §§4.11–4.13 (§4.11 partial, §4.12 partial: graph closure only, §4.13 Bertini remaining); §1.8 needs §1.4 and AbelianSchemesAndArithmeticModuli A0.1–A1.2, A1.8; §1.9 needs §§1.4, 1.7, 1.8.
- Serves defs: 78 (§§1.8–1.9), 85 (§1.9 global Néron model), 87 (§1.9, through §6.4b), 89 (§1.8, through §5.1)
- Evidence: README l.864 "### 1.5 The group law and extension of homomorphisms" (*Needs* l.876), l.926 "### 1.7 Smoothening and local existence" (`LocalExistence`; *Needs* l.949), l.970 "### 1.8 Abelian schemes are Néron models" (`HasGoodModel`; *Needs* l.981), l.997 "### 1.9 Spreading out and the Dedekind local-to-global construction" (`DedekindExistence`; *Needs* l.1012).

### §1.9a Closures of generic subschemes and good reduction of subvarieties
- Status: NOT-STARTED (its inputs Mathlib `Scheme.Hom.image`, `Scheme.Hom.smoothLocus` and Tau Ceti `IdealSheafData.IsEffectiveCartier` exist).
- Ready now: no: needs §§1.4, 1.8, 1.9, AbelianSchemesAndArithmeticModuli A0.1–A1, FiniteFlatGroupsAndIntegralPadicHodgeTheory §R07.1.20 and AlgebraicModuliForArithmeticGeometry §5.4.
- Serves defs: 78 (Definitions 78.2–78.4 with their equivalences)
- Evidence: README l.1032 "### 1.9a Closures of generic subschemes and good reduction of subvarieties" (*Needs* l.1065 "1.4, 1.8, 1.9; `AbelianSchemesAndArithmeticModuli:A0.1–A1`; FiniteFlatGroupsAndIntegralPadicHodgeTheory §R07.1.20; AlgebraicModuliForArithmeticGeometry §5.4; ...").

### §1.11 The invariant-differential lattice `DifferentialLattice`
- Status: NOT-STARTED.
- Ready now: no: needs §§1.5, 1.9 and SchemeAndStackFoundations §3.8 (invariant differentials; STATUS Layer 3 "Picard groups (3.4) onward" remaining).
- Serves defs: 85 (the Hodge bundle `e^*Ω^g` on a Néron model)
- Evidence: README l.1136 "### 1.11 The invariant-differential lattice" (`DifferentialLattice`, `det`, `localize`, `etale_basechange`; *Needs* l.1152 "1.5, 1.9; SchemeAndStackFoundations §3.8; Mathlib `KaehlerDifferential`").

### §§2.1–2.2 Identity component and component group
- Status: NOT-STARTED (the affine `identityComponentSpec` and `componentGroupScheme` are in code; no `NeronIdentity`, `NeronComponents`).
- Ready now: no: §2.1 needs §§1.5, 1.9, AlgebraicModuliForArithmeticGeometry §7.9 and ReductiveGroups Layer 3; §2.2 needs §2.1.
- Serves defs: 85 (§2.1), 87 (§§2.1–2.2, through §6.4b)
- Evidence: README l.1182 "## Layer 2: special fibres and component groups"; l.1197 "### 2.1 The identity component" (*Needs* l.1226), l.1244 "### 2.2 The component group" (*Needs* l.1289).

### §§3.1, 3.3, 3.10 Semistable reduction predicate, semistable identity models and finite base change, semistable reduction after a finite separable extension
- Status: NOT-STARTED.
- Ready now: no: §3.1 needs §§1.10, 2.1, 2.3, 2.4, SchemeAndStackFoundations §§0.12–0.14 (STATUS remaining) and AbelianSchemesAndArithmeticModuli A2.2; §3.3 needs §§2.1, 3.1 and SchemeAndStackFoundations §0.14; §3.10 needs §§3.1, 3.2, 3.8, 3.9, StableReduction Layers 4 and 7, JacobianChallenge Layers D–F (partial) and AbelianSchemesAndArithmeticModuli A3, A6.5.
- Serves defs: 85 (the local form of 85.4 over a discrete valuation ring, and the stable height's base change; the global choice of `K'` is merged ArakelovGeometryAndAbelianHeights §3.4, through §3.12)
- Evidence: README l.1528 "## Layer 3: semistable reduction and uniformisation"; l.1539 "### 3.1 The semistable reduction predicate" (*Needs* l.1562), l.1606 "### 3.3 Semistable identity models and finite base change" (`SemistableIdentityBasechange`; *Needs* l.1623), l.1895 "### 3.10 Semistable reduction after a finite separable extension" (`FiniteSeparableSemistableExtension`; *Needs* l.1924).

### §5.1 Néron–Ogg–Shafarevich for abelian varieties
- Status: NOT-STARTED (the elliptic-curve criterion over a local field, `hasGoodReduction_iff_forall_mem_inertiaSubgroup_tateModuleGaloisRepresentation_eq_one` in TauCeti/AlgebraicGeometry/EllipticCurve/TateModule/GoodReduction.lean, is in code; the abelian-variety statement is not).
- Ready now: no: needs §1.8, §3.11 (Grothendieck's monodromy criterion), §4.3 (monodromy pairing), ArithmeticGaloisRepresentations §§6.1–6.2 and EtaleCohomologyFoundations §F.3a.
- Serves defs: 89 (unramifiedness of `ρ_ℓ` at good-reduction places)
- Evidence: README l.3109 "### 5.1 Néron–Ogg–Shafarevich" (`NeronOggShafarevich`; *Needs* l.3127 "1.8, 3.11, 4.3; `ArithmeticGaloisRepresentations:§§6.1–6.2`; EtaleCohomologyFoundations §F.3a").

### §6.4b Connected Néron torsors and localization `ConnectedNeronLocalization`
- Status: NOT-STARTED.
- Ready now: no: needs §§1.9, 2.1–2.2, ReductiveGroupsPartII RG2.3.7 (Lang's theorem) and SchemeAndStackFoundations §§0.12–0.14, 1.15–1.16, 2.1–2.4, 2.10, 2.15.
- Serves defs: 87 (`Ш(A/F)` and its identification with Mathlib's `ContinuousCohomology.tateShafarevich`)
- Evidence: README l.4024 "### 6.4b Connected Néron torsors and localization" (*Needs* l.4061 "1.9, 2.1–2.2; ReductiveGroupsPartII RG2.3.7 ...; SchemeAndStackFoundations §§0.12–0.14, 1.15–1.16, 2.1–2.4, 2.10, 2.15 ...").

## TauCetiRoadmap/SelmerIwasawaCohomology
No STATUS.md (merged as roadmap PR #869; Tau Ceti checked at 91942aa9f, 2026-11-19). The discrete Selmer interface it extends is EllipticCurves Layer 7, in code as `TauCeti.ContCohomology.SelmerStructure` with `selmerGroup`, `mem_selmerGroup_iff`, `withLocalConditions`, `localConditionComparison`, `finite_selmerGroup_of_finite_quotient` (RepresentationTheory/Homological/ContCohomology/SelmerStructure/{Basic,Comparison}.lean).

### §§2.1–2.2 Compact and rational Selmer data and the Selmer kernel
- Status: NOT-STARTED. The discrete case is in code as above; the module-theoretic data over a ring `R` with relaxed and strict conditions and `Sel = ker(H → ∏_v H_v/L_v)` for compact and rational coefficients are not. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43653 (`TauCeti.SelmerData R ι H Hloc` with `selmerModule`, `ker_singularLocalization`, `withLocalConditions`, `relax`, `strict`; LinearAlgebra/SelmerData.lean).
- Ready now: yes (*Needs* lists only Mathlib `Submodule.map_le_iff_le_comap` and EllipticCurves Layer 7, which is in code; the compact and rational instances use ArithmeticGaloisDuality Layer R02.1, which §2.12a does not need)
- Serves defs: 87 (formal *Needs* of §2.12a)
- Evidence: README l.345 "### 2.1 Compact and rational Selmer data" (*Needs* l.372), l.374 "### 2.2 Compact and rational Selmer kernel" (*Needs* l.411).

### §2.12a Abelian Kummer and Sha interfaces (`AbelianVariety.Points`, `Sel_φ(A/K)`, `Ш(A/K)`, finiteness)
- Status: NOT-STARTED. Tau Ceti has `TauCeti.AlgebraicGeometry.AbelianVariety` with its homomorphism group and isogenies `AbelianVariety.IsIsogeny` (AlgebraicGeometry/AbelianVariety/{Basic,MorphismGroup,Isogeny}.lean) and the elliptic-curve Selmer and Sha groups; no point group `AbelianVariety.Points`, torsion, Galois cohomology of `A(Kˢ)` or abelian `Ш` (grep `AbelianVariety.Points`, `tateShafarevich` in TauCeti/AlgebraicGeometry/AbelianVariety/ empty).
- Ready now: no: needs §§2.1–2.2 (ready), AbelianSchemesAndArithmeticModuli §§A2.2–A2.3, A3.1–A3.5, A3.7, A5.1 (not started), SchemeAndStackFoundations §§0.12, 2.1, 2.15 and ArithmeticGaloisDuality §R02.3.1 (finiteness, not started). The annihilator part also needs ArithmeticGaloisDuality §§R02.1.2, R02.4.3, D7.6; the definition does not.
- Serves defs: 87 (the target: 87.1–87.4(iii))
- Evidence: README l.677 "### 2.12a Abelian Kummer and Sha interfaces", l.679 "**Abelian Kummer, Selmer and Sha carriers.**", l.692 "**Finite Selmer and reduced primary groups.**", l.704 "**All-place Kummer annihilators.**", *Needs* l.717.

## TauCetiRoadmap/ArithmeticGaloisDuality
No STATUS.md (Tau Ceti checked at 91942aa9f, 2026-11-19).

### §R02.3.1 The group `G_{K,S}`, Hermite's finiteness and finiteness of `H¹(G_{K,S}, M)`
- Status: NOT-STARTED (grep `maxUnramifiedOutside`, `galoisGroupS`, `RestrictedRamification` empty). The Hermite input is in code in the form the roadmap asks for: `finite_of_finrank_le_of_ramifiedSupport_subset` (NumberTheory/NumberField/Discriminant/RamifiedSupport/Hermite.lean); inflation–restriction is in code (FieldTheory/GaloisCohomology/Inflation.lean). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43656 (`TauCeti.RestrictedRamification.maxUnramifiedOutside`, `galoisGroupS`, `finite_H1_galoisGroupS`; NumberTheory/NumberField/RestrictedRamification/).
- Ready now: yes (NumberFieldArithmetic is completed; ProfiniteCohomology Layer 5 supplies inflation–restriction)
- Serves defs: 87 (finiteness of `Sel_φ(A/K)` in SelmerIwasawaCohomology §2.12a)
- Evidence: README l.1841 "### R02.3.1 The group `G_{K,S}`, finiteness and localisation", l.1954 "**Hermite: finitely many extensions of bounded degree unramified outside a finite set.**", l.1980 "**Finiteness of `H¹(G_{K,S}, M)`.**" (*Needs* l.1996).

## TauCetiRoadmap/FourManifolds
No STATUS.md (merged as roadmap PR #936; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `SpinCStructure`, `spinCStructure`, `stiefelWhitneyClass`, `chernClass`: no hits.

### §4.1 (group and lift part) Spinᶜ(n), its maps to SO(n) and U(1), Spinᶜ structures as principal lifts with their isomorphisms and pullback
- Status: PARTIAL: the group is in code: `CliffordAlgebra.spinCGroup Q hQ` = (Spin(Q) × `Circle`)/`spinCKernel` with `mk`, `lift`, `ofSpin`, `ofCircle`, the determinant character `det` (`det_mk : det [s, z] = z²`), `toSpecialOrthogonal`, `mem_ker_toSpecialOrthogonal_prod_det_iff`, `finite_ker_toSpecialOrthogonal_prod_det` (LinearAlgebra/CliffordAlgebra/Spin/SpinC.lean); continuity of `det` and `toSpecialOrthogonal`, `detContinuousMonoidHom`, `ofCircleContinuousMonoidHom`, `isQuotientCoveringMap_mk` and `isQuotientCoveringMap_toSpecialOrthogonal_prod_det` (Topology/Algebra/CliffordAlgebra/Spin/SpinC.lean); the smooth compact Lie-group structure, `isLocalDiffeomorph_realMk`, `contMDiff_realDet` (Geometry/Lie/CliffordAlgebra/SpinC/Basic.lean); the infinitesimal determinant splitting `realDetLieLift`, `realDetLieLinearEquiv` (SpinC/Determinant.lean); half-spin actions (SpinC/HalfSpin.lean); charge conjugation `CliffordAlgebra.spinCGroup.chargeConj` with `chargeConj_mk`, `chargeConj_chargeConj`, `det_chargeConj`, `toSpecialOrthogonal_chargeConj` (Spin/SpinC.lean), `chargeConjContinuousMulEquiv` (Topology/Algebra/CliffordAlgebra/Spin/SpinC.lean) and `contMDiff_realChargeConj` (Geometry/Lie/CliffordAlgebra/SpinC/Basic.lean); the canonical lift `TauCeti.SeibergWitten.unitaryLift : U(V, J) → Spinᶜ(4)` with `det_unitaryLift` (Analysis/PDE/SeibergWitten/UnitaryLift.lean). The Spin analogue of the lift is `TauCeti.SpinStructure` with `Equiv` and `pullback` (Topology/VectorBundle/SpinStructure.lean). Missing: the Spinᶜ structure itself (a principal Spinᶜ(n)-bundle with a map to the fixed SO frame bundle, isomorphisms covering its identity), its associated-bundle and determinant-line constructions, pullback, sums, orientation change and boundary restriction, compatibility with Spin structures. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43592 (the lift part: `TauCeti.SpinCStructure` as a principal lift of `TauCeti.OrthonormalFrameBundle` along `spinCGroup.toSpecialOrthogonal`, `SpinCStructure.Equiv`, `SpinCStructure.pullback`, in Topology/VectorBundle/SpinCStructure.lean; determinant line, Spin-induced structures, sums and orientation change are not in it).
- Ready now: yes: the *Needs* item it uses is SpinGeometry G4's frame lifts and covering adapters (G4.1 adapters done; G4.2's `SpinStructure` in code as the template), on `TauCeti.PrincipalBundle`, `TauCeti.OrthonormalFrameBundle` and its `toOrientationCover`.
- Serves defs: 64
- Evidence: README l.1859 "## Layer 4: Spinᶜ, Wu and torsion", l.1861 "### 4.1 Spinᶜ, Wu and torsion" ("Spinᶜ structures are principal lifts with a specified map to that same SO frame bundle; isomorphisms cover its identity"); *Needs* l.1907 "SpinGeometry G4's frame lifts and covering adapters; CharacteristicClasses C2–C3's Chern and Stiefel–Whitney classes; AlgebraicTopology Stage 8's obstruction theory and Bockstein sequence"; grep `spinCGroup` in TauCeti/Topology/VectorBundle and TauCeti/Geometry/Manifold: no hits.

### §4.1 (classification part) Existence iff W₃ = β(w₂) = 0, the H²(−; ℤ) torsor of lifts, c₁(L) ≡ w₂ mod 2, integral lifts of w₂ on closed oriented four-manifolds
- Status: NOT-STARTED (no Stiefel–Whitney or Chern classes of bundles in code; Bockstein maps exist: AlgebraicTopology/Cohomology/Bockstein.lean, Singular/Coefficients/Bockstein.lean).
- Ready now: no: needs the lift part above, CharacteristicClasses C2 (partial: Thom and Euler classes) and C3 (untouched, the source of w₂ and c₁), and AlgebraicTopology Stage 8's obstruction theory (§§8.8–8.16 unassessed per AlgebraicTopology STATUS).
- Serves defs: 64
- Evidence: README l.1874 "Prove existence iff W₃=β(w₂)=0 and the H²(−;ℤ) torsor of lifts on paracompact Hausdorff CW-type bases. Compare determinant lines: c₁(L) mod 2=w₂ ..."; *Needs* l.1907; CharacteristicClasses STATUS "C3, C4, C5, C5a and C7 are untouched", which names C3 (Leray–Hirsch and projective splitting) as the source of Stiefel–Whitney, Chern and Pontryagin classes.

## TauCetiRoadmap/DimerModelsAndLozengeTilings
No STATUS.md (merged as roadmap PR #2422; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `lozenge`, `Kasteleyn`, `hexGraph`, `TriEdge`, `IsGibbs`, `dimer`: no hits. Its Tau Ceti suppliers are in code: `ErgodicSMul.iff_mem_extremePoints` and `invariantMeasuresOfMeasureUnivEq` (MeasureTheory/Group/ErgodicExtreme.lean), `TauCeti.MeasureTheory.ergodicSMul_iff_forall_smul_invariant` and `exists_smul_invariant_ae_eq` (MeasureTheory/Group/CountableAction.lean), `isExtreme_setOf_measure_eq_zero` (MeasureTheory/Measure/Face.lean), `TauCeti.Probability.tailProcess` (Probability/Process/Tail/Basic.lean), `Matrix.det_submatrix_comp_inr_eq_sign_mul_det_mul_det_submatrix_comp_inl_nonsing_inv` (LinearAlgebra/Matrix/Determinant/ComplementaryMinor.lean), `TauCeti.Contour.homologyCauchyTheorem` (Analysis/Contour/HomologyCauchy.lean) and `intervalIntegral_deriv_smul_segment_eq_curveIntegral` (Analysis/Contour/Primitive.lean). No other roadmap supplies it ("From other roadmaps: None").

### Layer 1 (§§1.1–1.6) Triangular lattice, dual hexagonal graph, regions, tilings, tilings as perfect matchings, row tilings
- Status: NOT-STARTED (`TauCeti.PerfectMatching` in Combinatorics/Enumerative/PerfectMatching is the complete-graph matching of a finite type, not a graph matching). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43575 (§§1.1–1.2: `TriEdge`, `TriFace`, `latticeRotation`, `hexGraph` with regularity and bipartiteness, in Combinatorics/Lozenge/; §§1.3–1.6 are not in it).
- Ready now: yes (its *Needs* are Mathlib only: `SimpleGraph.fromRel`, `SimpleGraph.Subgraph.IsPerfectMatching`, `DiscreteTiling.Protoset`, `arrowAddAction`).
- Serves defs: 100 (100.1)
- Evidence: README l.566 "## Layer 1: the triangular lattice and lozenge tilings", l.702 "### 1.5 Tilings are perfect matchings"; *Needs* l.575, l.604, l.637, l.665, l.712, l.738.

### Layer 2 (§§2.1, 2.2, 2.5, 2.10) Edge cochains, simple connectivity of the plane, heights of plane tilings, lozenge counts
- Status: NOT-STARTED.
- Ready now: no: needs Layer 1 (§§1.3–1.4).
- Serves defs: 100 (100.2 is §2.5; §2.10 feeds §5.4)
- Evidence: README l.771 "## Layer 2: height functions, simple connectivity and Thurston's criterion", l.863 "### 2.5 Heights of plane tilings", l.1043 "### 2.10 Finite changes preserve lozenge counts"; *Needs* l.783 (1.3), l.813 (2.1), l.877 (1.4, 2.2), l.1049 (2.5).

### Layer 4 (§§4.1–4.6) Outside and tail σ-algebras, Bernoulli measures, weak topology on a finite-alphabet subshift, specifications and Gibbs measures, face property
- Status: NOT-STARTED (Tau Ceti's tail σ-algebras are indexed by `ℕ` or `ℕ × ℕ` with no group action, per the README's supplier note). Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/43578 (§4.1: `TauCeti.Probability.cylinderEventsTail` with `cylinderEventsTail_eq_tailProcess` and the group-action lemmas, in Probability/Gibbs/Tail.lean) and https://github.com/TauCetiProject/TauCeti/pull/43581 (§4.5 and the carrier of §4.4: `TauCeti.Subshift`, `TauCeti.Specification`, `Specification.IsGibbs`, `isGibbs_iff_forall_ae_eq_condExp`, `convex_setOf_isGibbs`, in Probability/Gibbs/); §§4.2–4.3, the weak topology of §4.4 and §4.6 are in neither.
- Ready now: yes (its *Needs* are Mathlib `cylinderEvents`, `ProbabilityTheory.Kernel`, `Measure.infinitePi` and the Tau Ceti suppliers listed above, all in code; Layer 4 "depends on no earlier layer").
- Serves defs: 100 (100.3.1–100.3.2)
- Evidence: README l.1180 "## Layer 4: Gibbs specifications on configuration spaces", l.1347 "### 4.5 Specifications and Gibbs measures", l.1423 "### 4.6 The face property and closedness"; *Needs* l.1213, l.1251, l.1275, l.1307, l.1377, l.1453; build order l.548–564.

### Layer 5 (§§5.1–5.4) Dimer specification on periodic graphs, ergodic dimer measures, the lozenge instance `IsLozengeGibbs`
- Status: NOT-STARTED.
- Ready now: no: §§5.1–5.3 need Layer 4; §5.4 also needs §§1.2, 1.5, 2.10.
- Serves defs: 100 (100.3.1–100.3.2: `IsLozengeGibbs`, `lozengeGibbsInvariant`, `lozengeGibbs_extreme_iff_ergodic`)
- Evidence: README l.1496 "## Layer 5: dimer models on periodic graphs", l.1623 "### 5.4 The lozenge instance"; *Needs* l.1509, l.1545, l.1604, l.1653.

### Layer 6 (§§6.1–6.3) Slope, corners, edges of the slope triangle
- Status: NOT-STARTED.
- Ready now: no: needs §2.5 and §5.4 (§6.3 also §§1.6, 4.3, 5.3).
- Serves defs: 100 (100.3.3 is §6.1; §9.5 needs §§6.2–6.3)
- Evidence: README l.1693 "## Layer 6: slopes and the boundary of the slope triangle", l.1695 "### 6.1 The slope"; *Needs* l.1701, l.1727, l.1761.

### Layers 7–8 (§§7.1–7.3, 8.1–8.5) Torus tilings and torus limits; Kasteleyn theory on the torus
- Status: NOT-STARTED.
- Ready now: no: §7.1 needs §§1.5, 2.5; §7.3 needs Layers 4–6; Layer 8 needs §7.1.
- Serves defs: 100 (through §§9.1–9.5)
- Evidence: README l.1817 "## Layer 7: torus tilings and torus limits", l.1909 "## Layer 8: Kasteleyn theory on the torus"; *Needs* l.1829, l.1857, l.1888, l.1921, l.1960, l.1983, l.2018, l.2048.

### §§9.1–9.5, 9.7 Infinite inverse Kasteleyn kernel, determinantal Gibbs measures, ergodic Gibbs measures of every slope, the incomplete beta process
- Status: NOT-STARTED.
- Ready now: no: needs Layers 4, 6–8 and §9.6.
- Serves defs: 100 (existence in 100.4 is `exists_ergodicGibbs_of_slope`, §9.5; the measure `μ_{s,t}` of 100.5 is `incompleteBetaProcess_exists_unique`, §9.7)
- Evidence: README l.2068 "## Layer 9: the explicit kernel and ergodic Gibbs measures of interior slopes", l.2180 "### 9.5 Ergodic Gibbs measures of every slope", l.2240 "### 9.7 The incomplete beta process"; *Needs* l.2074, l.2124, l.2149, l.2167, l.2188, l.2270.

### §9.6 The complex slope and the incomplete beta kernel
- Status: NOT-STARTED. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43636 (Analysis/SpecialFunctions/IncompleteBeta/Kernel.lean: `complexSlope` and `incompleteBetaKernel`).
- Ready now: yes (its *Needs* are Mathlib `curveIntegral`, `Path.segment`, `curveIntegral_trans`, `Complex.arg` and Tau Ceti `TauCeti.Contour.homologyCauchyTheorem`, `intervalIntegral_deriv_smul_segment_eq_curveIntegral`, all in code).
- Serves defs: 100 (the kernel `K_ξ` of 100.5's explicit description)
- Evidence: README l.2196 "### 9.6 The complex slope and the incomplete beta kernel"; *Needs* l.2207.

## TauCetiRoadmap/LieGroupsPartII
No STATUS.md (merged as roadmap PR #2427; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `CartanInvolution`, `IwasawaData`, `ReductiveCartanDatum`, `MinimalParabolicDatum`, `IsSelfAdjointLinearGroup`, `linearLieAlgebra`, `conj_standardParabolic`: no hits. Its base carrier, LieGroups Layer 9's `CartanInvolution` and `IwasawaData`, is not in code (Layer 9 partial: matrix cases only).

### Layers 1–2 (§§1.1–1.2, 2.1–2.6) Reductive Cartan data and their conjugacy; restricted roots, conjugacy of maximal abelian `𝔞 ⊆ 𝔭` under `K⁰`, the two Weyl groups, component condition, conjugacy of Iwasawa triples
- Status: NOT-STARTED.
- Ready now: no: needs LieGroups Layer 9 (`CartanInvolution`, `FiniteCartanMatrixModel`, `cartan_polar_decomposition`, `IwasawaData`, restricted root system; partial, `GL n` only) and RealSemisimpleLieGroups §§0.2, 1.2, 2.3 (not started).
- Serves defs: 1 (§2.2), 4, 79 (through Layer 3), 54 (§§1.1, 2.5 through §§7.1, 8.1)
- Evidence: README l.143 "## Layer 1: Reductive Cartan data and their conjugacy", l.208 "## Layer 2: Restricted roots, positive systems and the two Weyl groups", l.228 "### 2.2 Conjugacy of maximal abelian subspaces of 𝔭", l.341 "### 2.6 Conjugacy of Iwasawa triples"; *Needs* l.147, l.187, l.219, l.248, l.281, l.304, l.330, l.343.

### Layer 3 (§§3.1–3.5) Minimal parabolic subgroup: `Z_G(𝔰)`, `M = Z_K(𝔞)`, `N`, `P = MAN`, Langlands decomposition, one conjugacy class, minimal parabolic datum
- Status: NOT-STARTED (inputs in code: `lieExp`, `TauCeti.Lie.conj_lieExp`, `LeftInvariantDerivation.Ad_lieExp`, `TauCeti.Lie.isEmbeddedLieSubgroup_of_isClosed`).
- Ready now: no: needs Layers 1–2, LieGroups Layer 9 (`iwasawaDecomposition`, partial) and, for §3.5, RealSemisimpleLieGroups §3.1 (not started).
- Serves defs: 4, 79
- Evidence: README l.359 "## Layer 3: The minimal parabolic subgroup", l.383 "### 3.2 The groups M, N and P", l.408 "### 3.3 The Langlands decomposition of P", l.436 "### 3.4 Minimal parabolic subgroups form one conjugacy class", l.446 "### 3.5 The minimal parabolic datum"; *Needs* l.375, l.391, l.427, l.438, l.453.

### §6.1 Conjugate standard parabolics of a Tits system (`conj_standardParabolic_le_iff`)
- Status: PARTIAL: the case `J = J'` of its second statement is in code as self-normalization, `TauCeti.TitsSystem.normalizer_standardParabolic`, `normalizer_eq_of_subgroupB_le`, `normalizer_subgroupB` (GroupTheory/TitsSystem/Parabolic/Normalizer.lean). Missing: `conj_standardParabolic_le_iff` (`g P_J g⁻¹ ⊆ P_{J'}` iff `J ⊆ J'` and `g ∈ P_{J'}`). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43633 (GroupTheory/TitsSystem/Parabolic/Conjugate.lean: `conj_standardParabolic_le_iff`, `conj_standardParabolic_eq_iff`).
- Ready now: yes (its *Needs* are Tau Ceti declarations, all in code: `standardParabolic_empty`, `mem_standardParabolic_iff` (Parabolic/Basic.lean), `existsUnique_mem_bruhatCell` (Bruhat/Uniqueness.lean), `bruhatCell_mul_eq_of_wordLength_le` and `_right` (Bruhat/Length.lean), `bruhatCell_mul_self_eq_union_of_mem_simple` (Bruhat/Basic.lean), `bruhatCell_subset_standardParabolic_iff`, `standardParabolic_le_standardParabolic_iff` (Parabolic/Classification.lean)).
- Serves defs: 4 (uniqueness of the type of a parabolic subgroup, abstractly)
- Evidence: README l.559 "## Layer 6: Parabolic subgroups and subalgebras in general", l.561 "### 6.1 Conjugate standard parabolics of a Tits system"; *Needs* l.577.

### §§7.1, 8.1 Self-adjoint linear groups; real points of connected reductive `ℝ`-groups as self-adjoint linear groups
- Status: NOT-STARTED (matrix inputs in code: `Matrix.GeneralLinearGroup.existsUnique_posDef_mul_unitary` (Analysis/Matrix/Polar.lean), `TauCeti.Lie.unitsLieAlgebraEquiv_Ad`, `lieExp_eq_expUnit`).
- Ready now: no: §7.1 needs §1.1 and LieGroups Layer 9's identity-cover Cartan and polar theorem (partial); §8.1 needs §§2.5, 7.1, RealSemisimpleLieGroups §2.3 and ArithmeticLocallySymmetricSpaces ALS.F.1, ALS.0.1, ALS.0.2 (not started).
- Serves defs: 54 (through open PR #2430, which consumes `IsSelfAdjointLinearGroup` and `isSelfAdjointLinearGroup_of_zeroLocus` for real reductive data)
- Evidence: README l.641 "## Layer 7: The self-adjoint linear model", l.645 "### 7.1 Self-adjoint linear groups", l.787 "## Layer 8: Real points of connected reductive groups over ℝ", l.796 "### 8.1 Real points as self-adjoint linear groups"; *Needs* l.647, l.798, l.800.

## TauCetiRoadmap/CountableStructureSpaces
No STATUS.md (merged as roadmap PR #1316; Tau Ceti checked at 91942aa9f, 2026-11-19). Most of its Layers 0, 1.1, 1.2, 2 and 4.1 is Tau Ceti's `ModelTheory/RelationalConfiguration/` at the pin; Layer 1.1 is done (`Topology/Algebra/Group/Perm.lean`). Its one roadmap supplier, InfinitaryModelExistence's `pcSeparation`, is in code (`FirstOrder.Language.pcSeparation`, ModelTheory/Interpolation/Craig.lean, with `LHom.PCMem` in ModelTheory/Interpolation/PCClass.lean).

### Layer 0 The coding space: finite-cylinder basis, `queryCode`, continuum equality, graph coding
- Status: PARTIAL: `RelationalConfiguration` with decoding, encoding, `Equiv.encodeVia`, topology and σ-algebra, `isClopen_setOf_eval`, `continuous_eval`, `continuous_iff`, compactness, Polish and Borel instances, `mk_le_continuum` (ModelTheory/RelationalConfiguration/Basic.lean, Topology.lean), and the decoded graph coding `SimpleGraph.toStructure_toRelationalConfiguration` with `range_toRelationalConfiguration` (Combinatorics/SimpleGraph/RelationalConfiguration.lean). Missing: the finite cylinders as a basis of clopen sets, `queryCode` with `isClosedEmbedding_queryCode`, the equality case of the cardinality bound, closedness of the range of the graph coding. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43619 (ModelTheory/RelationalConfiguration/Coding.lean: the finite-cylinder basis, the query code and the size of the coding space).
- Ready now: yes ("Mathlib and Tau Ceti only; no earlier layer and no other roadmap").
- Serves defs: 98 (Layer 5 consumes `queryCode`)
- Evidence: README l.234 "## Layer 0: The coding space" ("Still to build: the finite-cylinder basis, the query code, the equality case of the cardinality bound, closedness of the range of the graph coding and the decoded structure of the graph coding"; the last is in code); *Needs* l.292; grep `queryCode`: no hits.

### §1.2 The logic action: `ContinuousSMul`, stabilizers, saturations for every language
- Status: PARTIAL: the relabelling action with `eval_perm_smul` (RelationalConfiguration/Basic.lean), `continuous_uncurry_restrict` (Topology.lean), `isoSetoid_eq_orbitRel`, `isomorphismInvariant_iff_isInvariantBlock`, the `IsomorphismInvariant` closure lemmas and `analyticSet_iUnion_smul` for relational `L` with countably many relation symbols (Isomorphism.lean); `AnalyticSet.prod` (MeasureTheory/Constructions/Polish/Analytic.lean). Missing: the `ContinuousSMul` instance (98.3's joint continuity), `mem_stabilizer_iff` and closedness of stabilizers, `analyticSet_iUnion_smul` and analyticity of the isomorphism relation for languages with function symbols or uncountably many relation symbols. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43612 (ModelTheory/RelationalConfiguration/{Topology,Isomorphism}.lean: `ContinuousSMul`, stabilizers and saturations, completing §1.2).
- Ready now: yes (*Needs* L0's coding space and L1.1, both in code for this use; `continuous_uncurry_restrict` with `Equiv.Perm.continuous_inv_apply` gives the instance).
- Serves defs: 98 (98.3), 94 (its census chain item 3 cites §1.2's joint continuity and saturations; 94 is specified only by open PR #2418)
- Evidence: README l.344 "### 1.2 The logic action" ("Still to build: `mem_stabilizer_iff` and closedness of stabilizers, the two saturation results for languages with function symbols, and `analyticSet_iUnion_smul` for uncountably many relation symbols"; the `ContinuousSMul` bullet); *Needs* l.390; grep `ContinuousSMul` in TauCeti/ModelTheory: no hits.

### Layer 3 Trees, boundedness and the tree representation of analytic sets
- Status: PARTIAL: well-founded descriptive trees and their ranks with the boundedness theorem, under Tau Ceti names: `Descriptive.Tree.IsWellFounded`, `Descriptive.Tree.rank`, `IsWellFounded.rank_lt_omega_one`, `MeasureTheory.AnalyticSet.exists_treeRank_lt_omega_one_of_isClosed` (SetTheory/Descriptive/Tree.lean), which is the README's `treeHeight_lt_omega_one` and `analytic_treeHeight_bounded` in content. Missing: `initialSegment`, `body` and closedness of bodies, `StrictExt` with `wellFounded_strictExt_iff`, the Kleene–Brouwer order `KBLT` with `wellFounded_kbLT_iff`, and the tree representation `exists_tree_of_analyticSet_cantor` and `exists_tree_of_analyticSet`. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43637 (SetTheory/Descriptive/{Tree,KleeneBrouwer}.lean: tree bodies, the Kleene–Brouwer order and Layer 3 except `exists_tree_of_analyticSet`).
- Ready now: yes for everything but `exists_tree_of_analyticSet`, which needs Layer 0's `queryCode` (not in code).
- Serves defs: 98 (Layer 5 consumes `body` and `exists_tree_of_analyticSet`)
- Evidence: README l.475 "## Layer 3: Trees, boundedness and the tree representation"; *Needs* l.521 "L0 (`queryCode`, for `exists_tree_of_analyticSet`); M `Descriptive.tree`, `WellFounded.rank`, `MeasureTheory.AnalyticSet`, `Ordinal.omega`; the shape of Mathlib #41946"; grep `exists_tree_of_analyticSet`, `KBLT`, `def body`: no hits.

### Layer 5 (§§5.1–5.4) The López–Escobar theorem: PC sentence of a tree, `lopez_escobar`, `lopezEscobar_iff`, `lopezEscobar_action_iff`, `analyticSet_iff_exists_pc`
- Status: NOT-STARTED (§5.1's content is in code apart from the name `isomorphismInvariant_modelsOf`: `measurableSet_modelsOf` and `FirstOrder.Language.Equiv.mem_modelsOf_iff`, ModelTheory/RelationalConfiguration/ModelsOf.lean; the reduction of §5.3 step 0 has its inputs `symbSublang`, `LHom.reductConfiguration`, and step 3 has `pcSeparation`).
- Ready now: no: §§5.2–5.3 need Layer 0's `queryCode` and Layer 3's `body` and `exists_tree_of_analyticSet` (both partial, those parts not in code); §5.4 also needs §1.2's invariant σ-algebra (in Mathlib and code). §5.1 alone is ready.
- Serves defs: 98 (98.5)
- Evidence: README l.743 "## Layer 5: The López–Escobar theorem", l.754 "### 5.2 The PC sentence of a tree", l.792 "### 5.3 The hard direction", l.838 "### 5.4 Packaging"; *Needs* l.752, l.789, l.832, l.869; grep `lopezEscobar`, `lopez_escobar`, `pcSentence`: no hits.

## TauCetiRoadmap/AutomorphicLFunctionsAndLocalFactors
No STATUS.md (merged as roadmap PR #924; Tau Ceti checked at 91942aa9f, 2026-11-19). No target is in Tau Ceti (grep `isobaric`, `charpolyRev` against an L-group in TauCeti/: no hits).

### AL.4.1.1 The unramified L-group Euler factor `det(1 − T r(t))`
- Status: NOT-STARTED.
- Ready now: no: needs ReductiveGroupsPartII RG2.5.2 (the L-group; not started), IntegralHeckeAndGaloisDeterminants §3a.1 (not started) and SmoothRepresentationsOfLocalGroups SR.4 (not started); the polynomial itself is Mathlib `Matrix.charpolyRev`.
- Serves defs: 88 (the Euler factor of the unramified transfer along an arbitrary L-representation `r`, 88.1)
- Evidence: README l.2282 "#### AL.4.1.1 The unramified L-group Euler factor" (*Needs* l.2303 "**IntegralHeckeAndGaloisDeterminants**, §3a.1 ...; Mathlib `Matrix.charpolyRev`; ... **ReductiveGroupsPartII**, RG2.5.2 ...; **SmoothRepresentationsOfLocalGroups**, SR.4").

### AL.R.4, AL.3.7.2 `GLₙ` isobaric sums and strong multiplicity one for isobaric sums
- Status: NOT-STARTED.
- Ready now: no: AL.R.4 needs AL.R.1, AL.R.3, SmoothRepresentationsOfLocalGroups SR.2–SR.4 and IntegralHeckeAndGaloisDeterminants §3a.1 (not started); AL.3.7.2 needs AL.3.7.1, AL.3.6.1, AL.R.4 and ArithmeticLocallySymmetricSpaces ALS.F.6–F.7 (not started).
- Serves defs: 88 (merged AutomorphicLFunctionsAndLocalFactorsPartII §10.1, README l.1670, imports AL.R.4 for weak transfers (l.1672); §10.6, l.1784, imports AL.3.7.2 (*Needs* l.1801))
- Evidence: README l.625 "### AL.R.4 `GLₙ` isobaric sums" (*Needs* l.633), l.1794 "#### AL.3.7.2 Strong multiplicity one for isobaric sums" (*Needs* l.1802).

### AL.R.3, AL.3 Restricted tensor realizations and Rankin–Selberg theory (cited by GL2AutomorphicRepresentationsAndTransfer R16.4.1, R16.4.6)
- Status: NOT-STARTED.
- Ready now: no: AL.R.3 needs AutomorphicFormsOnReductiveGroups §§3.4–3.5 (open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43596 for `RestrictedTensor`), ALS.F.6, SmoothRepresentationsOfLocalGroups SR.1–SR.4 and AdelicAlgebraicGroups §§0.1–0.4, 2.2–2.3; AL.3.4.2–AL.3.4.3 need AL.3.4.1 and ALS.F.6 (none started).
- Serves defs: 72 (through R16.4.1 and R16.4.6)
- Evidence: README l.615 "### AL.R.3 Restricted tensor realizations" (*Needs* l.623), l.1430 "## Layer AL.3: Rankin–Selberg theory and function-field factors", l.1653 "#### AL.3.4.2 Global Whittaker factorization" (*Needs* l.1668), l.1670 "#### AL.3.4.3 Ordinary global multiplicity one for `GL(n)`" (*Needs* l.1689).

## TauCetiRoadmap/KTheoryFiniteLocalFields
No STATUS.md (merged as roadmap PR #1281; Tau Ceti checked at 91942aa9f, 2026-11-19).

### §4.0 Cyclic homology foundations (`HH_n(A/k)`, Connes mixed complex, smooth HKR comparison)
- Status: NOT-STARTED (grep `cyclicBar`, `CyclicHomology`, `connesOperator` in TauCeti/: no hits; the Hochschild cochains of DGAInfinity Layer 8 are in code, the derived Hochschild chains are not).
- Ready now: no: needs DGAInfinity Layer 8's derived Hochschild chains, normalized comparison and derived Morita invariance (partial), and derived tensor products and realization from GeneralizedCohomology and DerivedModuleAlgebra.
- Serves defs: 10 (open PR #2447 consumes `HH_n(A/k)` and the smooth HKR comparison; its §6.4(d), on which Theorem 10.5 rests, needs the comparison realized by antisymmetrisation)
- Evidence: README l.662 "### 4.0 Genuine equivariant and cyclic foundations", l.674 "**Cyclic homology foundations.**" ("the HKR comparison HHₙ(A/k)≃Ωⁿ_(A/k) for smooth commutative k-algebras"), *Needs* l.682.

## TauCetiRoadmap/EulerSystemsAndKolyvaginSystems
No STATUS.md (merged as roadmap PR #1272; Tau Ceti checked at 91942aa9f, 2026-11-19).

### §6.1 Exterior biduals (evaluation `⋀^r X → Hom_R(⋀^r Hom_R(X,R), R)` an isomorphism for finite projective `X`)
- Status: NOT-STARTED (grep `toExteriorBidual`, `exteriorBidual` in TauCeti/: no hits).
- Ready now: no: needs IntegralIwasawaTheory §12.6 (the carrier `TauCeti.StarkSystems.toExteriorBidual`), PadicMeasuresIwasawaAlgebras Layer 6 and SelmerIwasawaCohomology Layer 2; the finite-projective statement that PR #2447 uses needs only the §12.6 carrier.
- Serves defs: 10 (open PR #2447 Layer 7 uses it for `τ_n : T^n_{R/k} → Hom_R(Ω^n_{R/k}, R)`)
- Evidence: README l.3942 "### 6.1 Exterior biduals of Selmer modules", *Needs* l.3978 "`IntegralIwasawaTheory §12.6`; `PadicMeasuresIwasawaAlgebras Layer 6`; `SelmerIwasawaCohomology Layer 2`".

## TauCetiRoadmap/GL2AutomorphicRepresentationsAndTransfer
No STATUS.md (merged as roadmap PR #931; Tau Ceti checked at 91942aa9f, 2026-11-19). No target is in Tau Ceti (grep `nonCM`, `selfTwist`, `quadraticInduction`, `automorphicInduction`, `RestrictedTensor`, `IsAutomorphicRepresentation` in TauCeti/: only the private `mackeySelfTwistIso` of finite-group Mackey theory).

### R16.4.1, R16.4.6 Cuspidal restricted tensor factorization and the non-CM self-twist condition
- Status: NOT-STARTED.
- Ready now: no: R16.4.6 needs R16.4.1, ArithmeticLocallySymmetricSpaces ALS.F.6 and AutomorphicLFunctionsAndLocalFactors AL.3 (not started), and the `twist` and `centralCharacter` of AutomorphicFormsOnReductiveGroups §3.2 (not started); R16.4.1 needs R16.1.5–R16.1.6, AutomorphicLFunctionsAndLocalFactors AL.2.2, AL.R.3, AL.3.4.2 and AutomorphicSpectralTheory Layer 4 (not started).
- Serves defs: 72 (target: R16.4.6; CM is the complement of non-CM)
- Evidence: README l.1112 "## Layer R16.4: Global cuspidal representations", l.1114 "### R16.4.1 The cuspidal restricted tensor factorization" (*Needs* l.1120), l.1235 "### R16.4.6 The non-CM self-twist condition" (*Needs* l.1251), l.1261 Dependencies.

### R17.4.16 Quadratic automorphic induction
- Status: NOT-STARTED (the finite-group input `TauCeti.simple_indFDRep_ofLinearCharacter_iff` is in code, RepresentationTheory/Induction/Clifford/).
- Ready now: no: needs R17.4 cyclic base change, R16.3, R16.5, AutomorphicLFunctionsAndLocalFactors AL.1.6.2 and ArithmeticGaloisRepresentations §2.7 (not started).
- Serves defs: 72 (`AI_{E/F}(θ)`, the converse direction of Proposition 72.3(b); the Labesse–Langlands direction is not a target)
- Evidence: README l.2708 "### R17.4.16 Quadratic automorphic induction" (*Needs* l.2725).

## TauCetiRoadmap/ShimuraVarieties
No STATUS.md (merged as roadmap PR #933; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `CMType`, `mumfordTate`, `MumfordTate`, `PureDatum`, `Shimura.`: no hits.

### §P.3 Hodge filtrations and reflex fields (the representation–Hodge dictionary)
- Status: NOT-STARTED. Inputs in code: `TauCeti.DeligneTorus.S` with `complexSplitting`, `mu`, `characterGroup` (Algebra/AlgebraicGroup/DeligneTorus/{Basic,Splitting}.lean), `TauCeti.Hodge.HodgeStructureOn` with tensor products, duals and Tate twists (Geometry/Hodge/). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43695 (the action of the Deligne torus on a pure Hodge structure, the first slice of the representation–Hodge dictionary, Geometry/Hodge/DeligneTorus.lean).
- Ready now: yes for the dictionary between rational Hodge structures and homomorphisms `h : S → GL(V)_ℝ` with its tensor, dual and Tate compatibilities (split `S`-characters in code). The datum-dependent parts (holomorphic variations, Borel embedding, reflex field `E(D)`) need §§P.1–P.2.
- Serves defs: 13, 23, 89
- Evidence: README l.151 "## Prerequisites constructed here", l.177 "### P.3 Hodge filtrations and reflex fields".

### §P.3a Mumford–Tate groups of rational Hodge structures
- Status: NOT-STARTED. Inputs in code: `TauCeti.HopfIdeal.sSup_toIdeal` (Algebra/HopfAlgebra/HopfIdeal/Basic.lean), `TauCeti.Hodge.exists_isCompl_of_isPolarizable` (Geometry/Hodge/Orthogonal.lean), identity components (Algebra/AlgebraicGroup/HopfIdeal/IdentityComponent.lean), the unipotent radical (Algebra/AlgebraicGroup/Borel/Radical.lean), `CommHopfAlgCat.hopfIdealOrderIsoClosedSubgroup`.
- Ready now: no: needs §P.3's dictionary (ready, not started); every other input it names is in code.
- Serves defs: 13 (target), 23, 89
- Evidence: README l.189 "### P.3a Mumford–Tate groups of rational Hodge structures", l.210 "This uses ... `TauCeti.HopfIdeal.sSup_toIdeal`; `TauCeti.Hodge.exists_isCompl_of_isPolarizable`".

### §5.1 CM types, reflex fields and reflex norms
- Status: NOT-STARTED (no `CMType` on Tau Ceti `main`; `Suggested.lean` states `CMType`, `CMType.typeTrace`, `CMType.reflexField`, `CMType.reflexField_isCMField`, `CMType.reflexField_representation`). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43696 (`TauCeti.CMType` with `typeTrace` and `reflexField`, NumberTheory/NumberField/CMType/Basic.lean; not the reflex norm).
- Ready now: yes for `CMType`, induced and primitive types, `typeTrace`, `reflexField` and the reflex norm `N_{k,Φ}` with identities (a)–(d) (Mathlib `NumberField.IsCMField`, `ComplexEmbedding.conjugate`, `IntermediateField.adjoin`, `LinearMap.det`). `TauCeti.Shimura.ReflexNorm.cm_type` needs §4.2 and §§P.1–P.4.
- Serves defs: 70 (70.1(a); §5.3 `CMAbelianVariety` over `ℂ`), 75 (75.1)
- Evidence: README l.1445 "### 5.1 CM types, reflex fields and reflex norms", l.1504 "This uses `NumberField.IsCMField`; ...", l.1525 "### 5.3 CM abelian varieties with their algebra action".

### §§7.0i–7.0i.1 Absolute Hodge tensors on abelian varieties; Mumford–Tate-valued ℓ-adic representations and Frobenius classes
- Status: NOT-STARTED.
- Ready now: no: needs §P.3a, §5.7, AbelianSchemesAndArithmeticModuli §§A4.1, A4.3–A4.4, A5.6–A5.7, A6.11, ComplexComparisonPartII §§C5.1–C5.3, C6.6, ArithmeticGaloisRepresentations §1.11 and §§2.1–2.2, NeronModelsAndSemistableAbelianVarieties §5.1 (none implemented).
- Serves defs: 89 (target: §7.0i.1; 89.1 is §7.0i)
- Evidence: README l.2014 "### 7.0i Absolute Hodge tensors on abelian varieties" (`TauCeti.Shimura.abelian_absolute_hodge`), l.2029 "### 7.0i.1 Mumford–Tate-valued ℓ-adic Galois representations and Frobenius classes".

### §§2.5–2.7, 3.1 Normal analytic Baily–Borel quotient, finite generation, Baily–Borel algebraization, Borel extension
- Status: NOT-STARTED.
- Ready now: no: needs §§2.1–2.4, Layers 0–1, §P.6, ComplexComparisonPartII §C−1.1 and Layers C2, C4 (not started).
- Serves defs: 15, 31 (arithmetic lattices only: merged BallQuotientsAndComplexHyperbolicLattices §11.4, README l.877 "### 11.4 Comparison with the Baily–Borel compactification", *Needs* l.879 "ShimuraVarieties §§1.2, 2.1–2.2, 2.7, 3.3, 3.5")
- Evidence: README l.625 "### 2.5 Normal analytic Baily–Borel quotient", l.659 "### 2.7 Baily–Borel algebraization" (`TauCeti.Shimura.baily_borel`), l.733 "### 3.1 Borel extension across punctured polydisks".

## TauCetiRoadmap/PELModuli
No STATUS.md (merged as roadmap PR #966; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `PositiveInvolution`, `SymplecticOLattice`, `IntegralPELDatum`, `PELDatum`: no hits. Its cited Tau Ceti inputs are in code: `TauCeti.ConstantForm.groupScheme`, `Symplectic.groupScheme`, `Matrix.transpose_mul_J_mul_eq_det_smul`, `LinearMap.BilinForm.dualSubmodule_dualSubmodule_flip`, `TauCeti.IntegralOrder.IsOrder`/`IsMaximalOrder`, `SymplecticForm.Compatible`.

### M0.1 Positive involutions and star orders
- Status: NOT-STARTED. Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/43701 (`TauCeti.StarOrder`, star-orders in a `ℚ`-algebra with involution, RingTheory/IntegralOrder/StarOrder.lean) and https://github.com/TauCetiProject/TauCeti/pull/43709 (the reduced trace `TauCeti.Algebra.reducedTrace` of a semisimple algebra, the `Trd_{B/ℚ}` input of `PositiveInvolution`, RingTheory/Semisimple/Trace/Reduced.lean).
- Ready now: yes (Mathlib `StarRing`, `IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing`, `Algebra.trace`, `Submodule.IsLattice`; ClassicalArithmeticCompletion §7.4's `IntegralOrder.IsOrder`, in code at RingTheory/IntegralOrder/Basic.lean)
- Serves defs: 82
- Evidence: README l.430 "### M0.1 Positive involutions", *Needs* l.468.

### M0.4–M0.5, M0.7 Symplectic O-lattices and their duals, integral PEL data, the similitude group
- Status: NOT-STARTED.
- Ready now: no: M0.4 needs M0.1 (ready); its `polarizationType` also needs AbelianSchemesAndArithmeticModuli A5.4 (not started). M0.5 needs M0.1, M0.4. M0.7's Hopf algebra `IntegralPELDatum.coordinate` and `isometryGroup` need only M0.5 and Tau Ceti `ConstantForm.groupScheme`; its adelic points need AdelicAlgebraicGroups §§1.2–1.3 and ProfiniteArithmetic Layer 0.
- Serves defs: 82 (targets: `SymplecticOLattice.dual` for 82.2, `PELDatum.isometryGroup` for 82.4), 23 (`GSp(V,ψ)` as the Siegel similitude group)
- Evidence: README l.583 "### M0.4 Symplectic O-lattices and their duals" (*Needs* l.611), l.630 "### M0.5 Integral PEL data" (*Needs* l.657), l.712 "### M0.7 The similitude group" (*Needs* l.744).

### M0.20, M5.5 Self-dual lattices at good primes; unitary PEL data with prescribed signatures
- Status: NOT-STARTED.
- Ready now: no: M0.20 needs M0.3, M0.4, M0.6, M0.8, M0.9; M5.5 needs M0.5, M0.10, M0.13, M0.22, M0.23, M0.25, M2.10, M3.2.
- Serves defs: 82 (M0.20(3): lattice independence in 82.5(e); M5.5: the unitary datum over a CM field)
- Evidence: README l.1233 "### M0.20 Self-dual lattices at good primes" (*Needs* l.1252), l.3662 "### M5.5 Unitary PEL data with prescribed signatures" (*Needs* l.3687).

### M1.3 Unitary O_F-abelian schemes and signature type
- Status: NOT-STARTED.
- Ready now: no: needs M0.22, M0.23, M0.25, M0.27, M1.2 and AbelianSchemesAndArithmeticModuli A4.3 (not started).
- Serves defs: 70 (70.3 for `L` a CM field, in determinant form)
- Evidence: README l.1638 "### M1.3 Unitary `O_F`-abelian schemes and signature type" (*Needs* l.1669).

## TauCetiRoadmap/DiracScatteringAndNonlinearFourierTransform
No STATUS.md (merged as roadmap PR #2444; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `DiracFundamentalSystem`, `diracCoeff`, `scatteringA`, `nonlinearFourier`, `PoissonFinite` in TauCeti/: no hits.

### Layer 1 (§§1.1–1.6) Integral Grönwall, the linear Carathéodory theorem with an integrable coefficient, the propagator, Liouville's formula, continuous and holomorphic dependence on a parameter
- Status: NOT-STARTED. Inputs in code: Carathéodory existence and uniqueness for essentially bounded coefficients `TauCeti.exists_continuousOn_eq_forall_mem_Icc_eq_picard`, `TauCeti.eqOn_of_forall_mem_Icc_eq_picard` (Analysis/ODE/Caratheodory.lean), the constant-kernel Grönwall `TauCeti.le_mul_exp_of_le_add_mul_integral` (Analysis/ODE/Gronwall.lean), Jacobi's formula (Analysis/Calculus/FDeriv/Det.lean). Open Tau Ceti PRs https://github.com/TauCetiProject/TauCeti/pull/43694 (§1.1 integral Grönwall with a nonnegative integrable kernel, `TauCeti.le_mul_exp_integral_of_le_add_integral_mul`, Analysis/ODE/Gronwall/Integrable.lean) and https://github.com/TauCetiProject/TauCeti/pull/43702 (§1.2 `linear_caratheodory` with an integrable coefficient, Analysis/ODE/Caratheodory/Integrable.lean).
- Ready now: yes (Layer 1 *Needs* only Mathlib and Tau Ceti: absolute continuity, Lebesgue differentiation, `ContractingWith`, parametric integrals).
- Serves defs: 44 (target: Prop 44.1, §1.6), 43
- Evidence: README l.509 "## Layer 1: Carathéodory linear systems with a holomorphic parameter", l.515 "### 1.1", l.539 "### 1.2 The linear Carathéodory theorem" (`linear_caratheodory` in Suggested.lean), l.581 "### 1.3 The propagator", l.610 "### 1.4 Liouville's formula", l.647 "### 1.5", l.663 "### 1.6 Holomorphic dependence on a parameter"; Dependencies l.743.

### Layer 2 (§§2.1–2.8) Function theory of the upper half-plane: Poisson integrals, positive harmonic functions, Fatou, bounded holomorphic functions, H^p(ℂ₊), Paley–Wiener, outer functions
- Status: NOT-STARTED. Inputs in code: `TauCeti.halfSpacePoissonKernel`, `halfSpacePoissonKernel_pos`, `integral_halfSpacePoissonKernel` (Analysis/PDE/GreenFunction/HalfSpace.lean, PoissonIntegral/HalfSpace.lean), `TauCeti.boundaryCayley` (Analysis/Complex/Pick/Nevanlinna.lean), `DifferentiableOn.hasDerivAt_wedgeIntegral_upperHalfPlane`. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43708 (§2.1 Poisson and Schwarz integrals of measures on the upper half-plane, `TauCeti.upperHalfPlanePoissonKernel`, Analysis/Complex/UpperHalfPlane/Poisson.lean).
- Ready now: yes for §2.1 (Mathlib and the Tau Ceti half-space Poisson kernel); §2.2 needs AutomorphicSpectralTheory §0.5 (ready, not started); §§2.3–2.8 follow §§2.1–2.2.
- Serves defs: 43
- Evidence: README l.755 "## Layer 2: Function theory of the upper half-plane", l.757 "### 2.1" (*Needs* l.789), l.815 "### 2.2 Positive harmonic functions on the half-plane" (*Needs* l.836 "§2.1; AutomorphicSpectralTheory §0.5"), l.937 "### 2.5", l.990 "### 2.6", l.1087 "### 2.8 Outer functions"; Dependencies l.1139.

### Layers 3–4 (§§3.1–3.3, 4.1–4.5) The Dirac system, Hermite–Biehler functions, the scattering matrix and scattering functions, Dyson and half-plane bounds, outerness and the finite Plancherel identity
- Status: NOT-STARTED.
- Ready now: no: §3.1 needs §§1.2–1.4, 1.6; §4.1 needs §§1.3, 1.6, 3.1, 3.2; §4.3 needs §§3.1, 3.3, 4.1; §4.4 also needs Layer 2 (§§2.2, 2.5, 2.8).
- Serves defs: 44 (target: §4.1 `a`, `b`; §4.3), 43
- Evidence: README l.1150 "## Layer 3", l.1154 "### 3.1 The Dirac system and its fundamental matrix" (*Needs* l.1196), l.1217 "### 3.2", l.1250 "### 3.3"; l.1286 "## Layer 4", l.1290 "### 4.1 The scattering matrix and the scattering functions" (*Needs* l.1319), l.1362 "### 4.3 The half-plane inequality" (*Needs* l.1373), l.1383 "### 4.4" (*Needs* l.1398).

### Layer 5 (§§5.1–5.5) The square-integrable scattering limit, the non-linear Fourier transform, boundary values, Plancherel, convergence of truncations
- Status: NOT-STARTED.
- Ready now: no: §5.1 needs §§4.3, 4.5; §5.2 needs §§2.5, 5.1; §5.5 needs §§2.5, 4.4, 5.1, 5.3, 5.4.
- Serves defs: 43 (target: §§5.1–5.5)
- Evidence: README l.1441 "## Layer 5", l.1446 "### 5.1" (*Needs* l.1461), l.1472 "### 5.2 The non-linear Fourier transform" (*Needs* l.1483), l.1558 "### 5.5 Convergence of truncations" (*Needs* l.1576).

## TauCetiRoadmap/AutomorphicSpectralTheory
No STATUS.md (Tau Ceti checked at 91942aa9f, 2026-11-19).

### §0.5 Herglotz representation on the upper half-plane
- Status: NOT-STARTED. Input in code: the finite-measure Nevanlinna representation `TauCeti.exists_isFiniteMeasure_eq_nevanlinnaKernel_add` (Analysis/Complex/Pick/), disc Herglotz `exists_isFiniteMeasure_eq_herglotzTransform_add` (Analysis/Complex/Herglotz.lean); the density conversion `dν = (1+t²)dρ` and uniqueness are not in code. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43704 (the Herglotz representation of Pick functions in the resolvent convention, `TauCeti.exists_eq_subtractedResolventKernel_add`, Analysis/Complex/Pick/Herglotz.lean).
- Ready now: yes (*Needs*: Tau Ceti `Analysis.Complex.Pick.Nevanlinna`, Mathlib `Measure.withDensity`)
- Serves defs: 43 (through DiracScatteringAndNonlinearFourierTransform §2.2)
- Evidence: README l.181 "### 0.5 Herglotz representation", *Needs* l.197.

## TauCetiRoadmap/ArakelovGeometryAndAbelianHeights
No STATUS.md (merged as roadmap PR #1000; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `HermitianVectorBundle`, `arakelovDegree`, `faltingsHeight`, `weilClass` in TauCeti/: no hits (Tau Ceti's `arakelovMulHeight` is a Euclidean point height).

### §§1.1–1.6 Hermitian vector bundles over O_K, their operations, the Arakelov degree, the product formula, additivity, finite extension
- Status: NOT-STARTED. Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43697 (§1.1 `HermitianVectorBundle K` over `𝓞 K` and the §1.3 degree computed with a chosen section, NumberTheory/Arakelov/HermitianVectorBundle.lean).
- Ready now: yes (*Needs* of §§1.1–1.6 are Mathlib only: `NumberField.RingOfIntegers`, `Module.Projective`, `InnerProductSpace`, `NumberField.InfinitePlace.mult`, `FractionalIdeal.absNorm`, `NumberField.prod_abs_eq_one`, `Algebra.norm`, `Ideal.absNorm_algebraMap`)
- Serves defs: 85 (target: 85.1–85.2), 80 (through §1.12)
- Evidence: README l.167 "## Layer 1", l.171 "### 1.1 Hermitian vector bundles over the ring of integers", l.243 "### 1.3 The Arakelov degree of a hermitian bundle", l.281 "### 1.4 Independence of the section: the product formula", l.327 "### 1.6 Arakelov degree under finite extension"; *Needs* after each.

### §§1.12–1.14 Heights of points for metrized line bundles, the Weil height class and Northcott, the projective-space comparison
- Status: NOT-STARTED. Inputs in code: `TauCeti.absoluteProjectiveTupleHeight`, `TauCeti.finite_setOf_absMulHeight₁_le`, `TauCeti.arakelovLogHeight` (NumberTheory/Height/).
- Ready now: no: §1.12 needs §§1.3, 1.6, 1.10 (on §§1.8–1.9: SchemeAndStackFoundations §§3.4–3.5, 5.1 and ComplexComparisonPartII §C5.4) and ComplexComparisonPartII §§C−1.1, C0.4, C5.1 (not started).
- Serves defs: 80 (open PR #1017 §§0.16, 0.20 take the number-field Weil height class and Northcott from §1.13)
- Evidence: README l.537 "### 1.12", l.573 "### 1.13 Metrized heights represent Weil heights; Northcott for ample bundles" (*Needs* l.591), l.600 "### 1.14".

### §§2.1, 2.4 The Faltings metric and the metrized Néron Hodge line
- Status: NOT-STARTED.
- Ready now: no: §2.1 needs AbelianSchemesAndArithmeticModuli §A5.1 and ComplexComparisonPartII §§C−1.1, C0.4, C5.1 (not started); §2.4 needs §§1.1, 2.1 and NeronModelsAndSemistableAbelianVarieties §§1.1, 1.7, 1.9, 1.11.
- Serves defs: 85 (target: 85.5)
- Evidence: README l.700 "### 2.1 The Faltings metric on top differential forms" (*Needs* l.726), l.777 "### 2.4 The metrized Hodge line bundle over `O_K`"; Layer 2 Dependencies l.966.

### §§3.1, 3.3, 3.4 Relative Faltings height, finite extension, the stable Faltings height
- Status: NOT-STARTED.
- Ready now: no: §3.1 needs §§1.3, 1.4, 2.4; §3.3 needs NeronModelsAndSemistableAbelianVarieties §3.3; §3.4 needs §§3.1, 3.3 and NeronModelsAndSemistableAbelianVarieties §3.12.
- Serves defs: 85 (target: 85.6 over number fields, global 85.4(i) via `K(A[12])`)
- Evidence: README l.970 "## Layer 3", l.974 "### 3.1", l.1023 "### 3.3", l.1043 "### 3.4 The stable Faltings height" (*Needs* "§3.1; §3.3; NeronModelsAndSemistableAbelianVarieties §3.12"); Dependencies l.1122.

## TauCetiRoadmap/PadicDifferentialEquationsAndRigidCohomology
No STATUS.md (merged as roadmap PR #1002; Tau Ceti checked at 91942aa9f, 2026-11-19).

### §RD.0.33 The completion of an algebraically closed nonarchimedean field is algebraically closed, in every characteristic
- Status: NOT-STARTED (no `IsAlgClosed` instance for a completion in TauCeti/; Mathlib's `IsAlgClosed.of_denseRange` is characteristic 0 only). Open Tau Ceti PR https://github.com/TauCetiProject/TauCeti/pull/43699 (`IsAlgClosed.of_isAlgClosed_of_denseRange` in every characteristic, Analysis/Normed/Field/IsAlgClosed.lean).
- Ready now: yes (*Needs* are Mathlib only: `IsAlgClosed.of_exists_root`, `Polynomial.exists_monic_and_natDegree_eq_and_norm_map_algebraMap_coeff_sub_lt`, `Polynomial.exists_aroots_norm_sub_lt_of_norm_coeff_sub_lt`, `spectralNorm.normedField`, `UniformSpace.Completion`, all present)
- Serves defs: 22 (merged GaloisActionOnEtaleCohomology §0.1 "The completed algebraic closure", README l.126, *Needs* l.141, characteristic `p`)
- Evidence: README l.1578 "### RD.0.33", Mathlib supplier list l.328–412.

## TauCetiRoadmap/CongruenceSpectralGap
No STATUS.md (merged as roadmap PR #1504; Tau Ceti checked at 91942aa9f, 2026-11-19).

### §§0.1–0.2 Hyperbolic quotient measure and the positive orbifold Laplacian of a congruence quotient
- Status: NOT-STARTED.
- Ready now: no: §0.2 needs UnboundedOperators UO-D06 over `RCLike` (partial), AutomorphicSpectralTheory §§0.6–0.7, 1.16a (not started), FuchsianOrbifolds Layers 0–6 items (Layer 0 and part of Layer 2 not done per its STATUS), PDE Lane A/E and DifferentialGeometry Layer 12.
- Serves defs: 40 (Definition 40.3 for congruence `Γ` only; §0.6 gives `σ_ac = [1/4, ∞)` there)
- Evidence: README l.150 "### 0.1 Hyperbolic quotient measure" (*Needs* l.170), l.172 "### 0.2 Positive orbifold Laplacian" (*Needs* l.195), l.326 "### 0.6 Congruence spectral description".

## TauCetiRoadmap/RepresentationTheory/ModularCharactersAndBlocks
No STATUS.md (merged as roadmap PR #1775; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `blockIdempotent|IsBlockIdempotent|brauerCharacter|brauerProjection|IsDefectGroup|SameBlock` in TauCeti empty.

### §0.2 Block idempotents
- Status: NOT-STARTED. Inputs in code: `TauCeti.IsPrimitiveIdempotent`, `TauCeti.exists_completeOrthogonalIdempotents_isPrimitiveIdempotent` (RingTheory/Idempotents/Primitive/Decomposition.lean).
- Ready now: yes (Mathlib `MonoidAlgebra`, `Subalgebra.center`, `CompleteOrthogonalIdempotents`)
- Serves defs: 2 (target), 3, 9
- Evidence: README l.323 "### 0.2 Block idempotents" (`IsBlockIdempotent`, `complete_blockIdempotents_unique`).

### §§1.1, 1.3 Splitting modular system; lifting idempotents over `O[G]`
- Status: NOT-STARTED. Inputs in code: `IsAdicComplete.exists_isIdempotentElem_eq` (RingTheory/AdicCompletion/Idempotent.lean), `TauCeti.exists_projective_quotient_smul_top_linearEquiv`, `TauCeti.Cyclotomic.complexRoot`, `FDRep.exists_simple_nonempty_iso_baseChange_adjoin_of_isPrimitiveRoot`.
- Ready now: no: §1.3 needs §0.2; §1.1 consumes CharacterTheory §4.5, whose universe adapter is the remaining piece of CharacterTheory Layer 4 (RepresentationTheory/STATUS.md)
- Serves defs: 2 (target), 3, 9
- Evidence: README l.413 "### 1.1 A splitting modular system", l.461 "### 1.3 Lifting idempotents and projectives over `O[G]`" (`existsUnique_blockIdempotent_map_residue`, l.474).

### §§4.2–4.3 Block partitions and the principal block
- Status: NOT-STARTED
- Ready now: no: needs §§1.3, 2.4, 4.1 (not started)
- Serves defs: 2 (target), 9
- Evidence: README l.811 "### 4.2 The block partitions" (`exists_blockIdempotent_iff_centralCharacter_congr`, `SameBlock`, l.845–862), l.890 "### 4.3 The principal block".

### §§6.1–6.2 Relative traces, Brauer homomorphism, defect groups
- Status: NOT-STARTED. Input in code: `Representation.relNormInvariants`, `relNorm_comp_norm` (RepresentationTheory/RelativeNorm.lean).
- Ready now: yes for §6.1 (Mathlib `MonoidAlgebra`, `Subgroup.centralizer`, `IsPGroup`); §6.2 needs §§0.2, 0.3, 6.1
- Serves defs: 3 (target), 9
- Evidence: README l.966 "### 6.1 Relative traces and the Brauer homomorphism", l.1010 "### 6.2 Defect groups" (`IsDefectGroup`, `isDefectGroup_conj`, `isDefectGroup_iff_sylow_of_augmentation_ne_zero`).

### §7.1 Block induction and the first main theorem
- Status: NOT-STARTED
- Ready now: no: needs §§6.1–6.2 and §2.3
- Serves defs: 3 (target, Remark (3)), 9
- Evidence: README l.1178 "### 7.1 Block induction and the first main theorem" (`brauer_first_main`, l.1193).

## TauCetiRoadmap/ShimuraData
No STATUS.md (merged as roadmap PR #1038; Tau Ceti checked at 91942aa9f, 2026-11-19). Grep `mumfordTate|MumfordTate|hodgeGeneric` in TauCeti empty.

### Layer 1 §§1.1–1.5 Rational weight criterion, Mumford–Tate group, connectedness, reductivity, Hodge genericity
- Status: NOT-STARTED. Inputs in code: `TauCeti.HopfIdeal.sSup_toIdeal`, `TauCeti.GeneralLinear.coordinateHopfAlgebra`, `TauCeti.DeligneTorus.S`, `TauCeti.geometricallyConnectedCommHopfAlgProperty`, `TauCeti.reductiveCommHopfAlgProperty`.
- Ready now: no: §1.1 needs ShimuraVarieties §§P.1–P.5 (not started) and ReductiveGroupsPartII RG2.0a; §§1.2–1.5 follow §1.1
- Serves defs: 13 (target, beside ShimuraVarieties §P.3a), 23 (target: §1.5 `hodgeGeneric`), 89
- Evidence: README l.162 "## Layer 1", §1.1 *Needs* l.183, l.185 "### 1.2 Mumford–Tate group" (*Needs* l.224), l.226 §1.3 (*Needs* l.243), l.245 §1.4 (*Needs* l.261), l.263 §1.5 (*Needs* l.287).

## TauCetiRoadmap/BallQuotientsAndComplexHyperbolicLattices
No STATUS.md (merged as roadmap PR #2425; Tau Ceti checked at 91942aa9f, 2026-11-19). No `PU(1,n)` or ball in Tau Ceti; only the `n = 1` Fuchsian theory.

### Layers 1–2, §5.1 The ball and `PU(1,n)`; biholomorphisms and `ω`; lattices
- Status: NOT-STARTED
- Ready now: no: §1.1 needs RealSemisimpleLieGroups §5.7 (not started); §5.1 needs VonNeumannAlgebras Layer 9
- Serves defs: 15, 31
- Evidence: README l.160 "### 1.1", l.262 "### 2.1 Cartan's theorem", l.450 "### 5.1 Lattices".

### §§7.1, 9.3–9.5, 10.2–10.4 Analytic quotient, minimal compactification, uniqueness and `(S_Γ, φ_Γ)`
- Status: NOT-STARTED
- Ready now: no: needs ComplexComparisonPartII §C-1.1 (not started), ShimuraVarieties §P.6, and Layers 5–6 and 8
- Serves defs: 15 (target: Theorem 15.4, Proposition 15.5, Definition 15.6), 31
- Evidence: README l.560 §7.1, l.705 §9.3, l.715 §9.4, l.725 §9.5, l.785 §10.4.

### §3.3, §§12.1–12.3 Totally geodesic subvarieties, strict and maximal sub-ball quotients
- Status: NOT-STARTED
- Ready now: no: §12.1 needs §§3.1 and 10.4; §3.3 needs RiemannianGeometry R5a (not started) and RealSemisimpleLieGroups §5.7
- Serves defs: 31 (target: Definition 31.4)
- Evidence: README l.358 §3.3, l.910 "### 12.1", §§12.2–12.3.

## TauCetiRoadmap/NoncompactQuantumSymmetry
No STATUS.md (merged as roadmap PR #1015; Tau Ceti checked at 91942aa9f, 2026-11-19).

### Layer 3 (M0) item 2 Cartan involution and conjugacy of maximal compact subgroups
- Status: NOT-STARTED (grep `CartanInvolution|IwasawaData` empty; only `serreCompactInvolution` and the symplectic special cases exist)
- Ready now: no: needs LieGroups Layers 7 and 9 (partial)
- Serves defs: 1, 4 (a second route to LieGroups Layer 9's θ)
- Evidence: README l.840 "## Layer 3: M0", l.991–1003, l.1073.

## TauCetiRoadmap/GaloisActionOnEtaleCohomology
No STATUS.md (merged as roadmap PR #2271; Tau Ceti checked at 91942aa9f, 2026-11-19).

### §§0.1–0.2 The completed algebraic closure; Galois automorphisms extend to `C`
- Status: NOT-STARTED
- Ready now: yes for `CompletedAlgClosure K`, its density and §0.2, which need only Mathlib; algebraic closedness waits on PadicDifferentialEquationsAndRigidCohomology §RD.0.33 (not implemented), and the geometric-point clause on AdicEtaleGeometry A1.7
- Serves defs: 22
- Evidence: README l.126 "### 0.1" (*Needs* l.141), l.143 "### 0.2" (*Needs* l.162).

### §1.1 Automorphisms of a cover act on cohomology (with cup products)
- Status: NOT-STARTED. Tau Ceti has only the cochain-level Čech cup product `TauCeti.CategoryTheory.cechCup` (CategoryTheory/Sites/SheafCohomology/Cech/Cup.lean).
- Ready now: no: needs AdicEtaleGeometry A1.6, AdicSpacesPartIV R4, ClassicalAdicEtaleCohomology §§1.1, 1.3 and EnhancedDerivedSheaves §§0.1–0.4 (*Needs* l.218)
- Serves defs: 18, 22
- Evidence: README l.193 "### 1.1", cup products l.204.

### §§1.2–1.3, 2.1, 2.3, Layer 3 Continuity, discreteness, Hochschild–Serre, ℓ-adic representations
- Status: NOT-STARTED
- Ready now: no: they follow §1.1
- Serves defs: 22
- Evidence: README l.220, l.238, l.287, l.319, l.394.

## TauCetiRoadmap/WeilConjectures
No STATUS.md (merged as roadmap PR #1208; Tau Ceti checked at 91942aa9f, 2026-11-19).

### §7.12 Numerical divisor descent and surface invariant comparisons (the Enriques condition)
- Status: NOT-STARTED. Inputs in code: χ(O), `Chow.NumericallyEquivalent`, Ω¹ and exterior powers.
- Ready now: no: ω_Y as a line bundle on a smooth surface (SchemeAndStackFoundations §2.20) is missing, and the b₂ comparison needs EtaleCohomologyFoundations §§F.5–F.7
- Serves defs: 19 (target), 20
- Evidence: README l.1806, l.1848–1862 (Enriques condition and its API), *Needs* l.1911.

## TauCetiRoadmap/CompletedCohomologyPartII
No STATUS.md (merged as roadmap PR #1035; Tau Ceti checked at 91942aa9f, 2026-11-19).

### §0.5 Modular and compact tower tests
- Status: NOT-STARTED
- Ready now: no: needs ArithmeticLocallySymmetricSpaces §§0.1–0.7 and ModularCurvesPartII §§14.1–14.4a, not implemented (*Needs* l.379)
- Serves defs: 77
- Evidence: README l.365 "### 0.5".

### §§1.1–1.3 Fixed-exponent cohomology, smooth local-group action, tame Hecke operators
- Status: NOT-STARTED
- Ready now: no: needs Layer 0 and the ArithmeticLocallySymmetricSpaces Hecke correspondences
- Serves defs: 77 (target)
- Evidence: README l.424 §1.1, l.451 §1.2, l.467 §1.3.

### §2.1 Completed cohomology
- Status: NOT-STARTED
- Ready now: no: needs §1.1 (the limit itself uses only Mathlib `TopModuleCat.isLimit`, *Needs* l.564)
- Serves defs: 77 (target)
- Evidence: README l.539 "### 2.1".

### §§8.2, 8.4, 8.7 Canonical tower input; realisation comparisons; transported Galois and Hecke actions
- Status: NOT-STARTED
- Ready now: no: needs ShimuraVarieties canonical models, ModularCurvesPartII §§14.1–14.4a, §8.3 (on HilbertModularVarietiesAndShimuraCurves §§R18.4.12–R18.4.13) and the étale input of §F.4 (l.241)
- Serves defs: 77 (target: the `G_ℚ` action)
- Evidence: README l.1744 §8.2, l.1761 §8.3, l.1777 §8.4, l.1832 §8.7.

## TauCetiRoadmap/PrismaticCohomology
No STATUS.md (merged as roadmap PR #1057; Tau Ceti checked at 91942aa9f, 2026-11-19).

### §§0.1–0.7 Integral delta algebra
- Status: PARTIAL: `TauCeti.DeltaRing p A` with `DeltaRing.addCorrection`, `DeltaRing.frobenius`, `ofFrobeniusLift`, `ext_of_frobenius`, `delta_int` (RingTheory/DeltaRing/Basic.lean). Missing: `Delta.Structure`, `Delta.IsDeltaMap` over arbitrary rings and the rest of §§0.1–0.7.
- Ready now: yes (*Needs* are Mathlib `Nat.Prime.dvd_choose_self`, `add_pow`, `Ideal.Quotient.mk`, `Ideal.span` and earlier subsections)
- Serves defs: 81
- Evidence: README l.280 "### 0.1–0.7 Integral delta algebra"; *Needs* l.288, l.308, l.318, l.337, l.357, l.377, l.397, l.407.

### §0.73 maps of prisms, §0.79 rigidity, §0.81 bounded prisms
- Status: NOT-STARTED (no prism structure in Tau Ceti)
- Ready now: no: needs §0.72 (imported from PerfectoidSpaces P4.15.2), DerivedModuleAlgebra §§1.1–1.9 (only §1.2 in code) and DerivedDeRhamCohomology §§1.10–1.23
- Serves defs: 81
- Evidence: README l.1336 (*Needs* l.1344), l.1465 (*Needs* l.1475), l.1493 (*Needs* l.1501).

### §§1.0–1.9 Bounded formal sites, the relative prismatic site, `Δ_{X/A}`, Hodge–Tate comparison, Frobenius
- Status: NOT-STARTED
- Ready now: no: §1.0 needs SchemeAndStackFoundations §§4.7–4.8, DerivedDeRhamCohomology §§5.1–5.7, 5.26 and EnhancedDerivedSheaves E2–E3; §1.1 needs §§0.56, 0.60, 0.72–0.81, DerivedModuleAlgebra §§1.1–1.9 and EnhancedDerivedSheaves E2
- Serves defs: 81 (target)
- Evidence: README l.1726 (*Needs* l.1732), l.1738 (*Needs* l.1746), l.1769 (*Needs* l.1779), l.1818 (*Needs* l.1826), l.1846, l.1873, l.1885, l.1913, l.1927 (*Needs* l.1935).

## TauCetiRoadmap/AutomorphicLFunctionsAndLocalFactorsPartII
No STATUS.md (merged as roadmap PR #1756; Tau Ceti checked at 91942aa9f, 2026-11-19).

### §§0.0, 0.3, 0.4, 10.1 Split classical and GSpin groups, standard transfer degree, archimedean transfer, weak functorial transfer
- Status: NOT-STARTED
- Ready now: no: §0.0 needs ReductiveGroupsPartII RG2.0a and RG2.5, OrthogonalSpinGroups Layers 0–1, GeometryOfNumbersAndQuadraticArithmetic §2.9 and MetaplecticAutomorphicForms §3.2a (only in open roadmap PR #1063); §10.1 needs SmoothRepresentationsOfLocalGroups SR.4, AutomorphicFormsOnReductiveGroups §§2.1–2.7, AutomorphicSpectralTheory §§2.1–2.6 and AutomorphicLFunctionsAndLocalFactors AL.3, none started
- Serves defs: 88 (target: §10.1), 11
- Evidence: README l.107 §0.0 (*Needs* l.125), l.201 §0.3 (*Needs* l.238), l.240 §0.4 (*Needs* l.254), l.1670 §10.1 (*Needs* l.1702).

## TauCetiRoadmap/AnabelianGeometryAndNonabelianChabauty
No STATUS.md (merged as roadmap PR #1021; Tau Ceti checked at 91942aa9f, 2026-11-19).

### §7.1 Sections, the section map `κ_X` and its injectivity
- Status: NOT-STARTED
- Ready now: no: uses EtaleCohomologyFoundations §F.0.A2 (not implemented), the roadmap's Layer 0 nonabelian H¹, SelmerIwasawaCohomology §2.12a and JacobianChallenge Layer F
- Serves defs: 84
- Evidence: README l.8505 "### 7.1"; "Use" lines l.8539, l.8569, l.8588, l.8606.
