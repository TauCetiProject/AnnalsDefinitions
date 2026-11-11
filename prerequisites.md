# Merged-roadmap work on the prerequisite chains of the 100 Annals definitions

Specified in a merged roadmap (`TauCetiRoadmap/<Name>/` at roadmap commit 5f7befb, 2026-11-11), not
yet (fully) implemented in Tau Ceti main (a6027b1, 2026-11-11), and on the prerequisite chain of at
least one definition. Each item was checked against the README section, STATUS.md (snapshot date
given per roadmap; several are stale) and a grep of Tau Ceti code. Item format: status
(NOT-STARTED / PARTIAL with what exists), ready now (yes / no: needs X), definitions served,
evidence. Section and layer ids are the roadmap's own.

## Summary: roadmaps ranked by number of the 100 definitions served

Counts exclude items found DONE. "Ready now" counts items whose verdict begins "yes" (some are "yes for a named sub-part"; see the item).

| Roadmap | # defs served | Items (not-started / partial) | Ready now | Definitions served |
|---|---|---|---|---|
| SchemeAndStackFoundations | 16 | 28 (20 / 8) | 12 | 16, 17, 19, 20, 21, 24, 25, 26, 27, 28, 29, 30, 71, 80, 84, 85 |
| ReductiveGroupsPartII | 10 | 4 (2 / 2) | 3 | 11, 13, 23, 67, 68, 73, 82, 83, 88, 90 |
| RepresentationTheory/LieGroups | 7 | 4 (2 / 2) | 2 | 1, 4, 5, 54, 62, 79, 83 |
| JacobianChallenge | 6 | 4 (0 / 4) | 0 | 19, 30, 71, 80, 84, 85 |
| ReductiveGroups | 6 | 5 (3 / 2) | 1 | 1, 4, 11, 23, 68, 79 |
| RiemannianGeometry | 6 | 6 (5 / 1) | 0 | 31, 49, 52, 62, 65, 66 |
| EtaleCohomologyFoundations | 5 | 6 (4 / 2) | 2 | 18, 19, 69, 77, 84 |
| ComplexKahlerGeometry | 4 | 5 (3 / 2) | 1 | 14, 38, 40, 63 |
| HeegaardFloer | 4 | 6 (3 / 3) | 1 | 56, 60, 63, 64 |
| ModularCurves | 4 | 2 (1 / 1) | 1 | 25, 26, 69, 71 |
| SmoothBundlesConnections | 4 | 3 (1 / 2) | 1 | 37, 48, 49, 62 |
| GeometricCurrents | 3 | 3 (2 / 1) | 0 | 53, 57, 65 |
| GeometricMeasureTheory | 3 | 2 (0 / 2) | 2 | 53, 55, 57 |
| CStarAlgebras | 2 | 7 (7 / 0) | 2 | 36, 46 |
| DerivedModuleAlgebra | 2 | 2 (1 / 1) | 0 | 27, 81 |
| EnhancedDerivedSheaves | 2 | 2 (1 / 1) | 0 | 18, 27 |
| GeometricTopology | 2 | 2 (2 / 0) | 1 | 59, 66 |
| OperatorTheory/SelfAdjointSpectralTheory | 2 | 1 (1 / 0) | 1 | 35, 45 |
| PseudodifferentialOperators | 2 | 2 (2 / 0) | 0 | 32, 40 |
| PseudoholomorphicCurveAnalysis | 2 | 4 (1 / 3) | 0 | 56, 60 |
| AdicEtaleGeometry | 1 | 2 (1 / 1) | 1 | 22 |
| AdicSpacesPartII | 1 | 1 (0 / 1) | 1 | 22 |
| AdicSpacesPartIV | 1 | 1 (1 / 0) | 0 | 22 |
| CharacteristicClasses | 1 | 1 (1 / 0) | 0 | 48 |
| DGAInfinity | 1 | 1 (0 / 1) | 1 | 10 |
| DifferentialGeometry | 1 | 1 (0 / 1) | 0 | 52 |
| FlagVarieties | 1 | 1 (1 / 0) | 0 | 79 |
| NoncommutativeIntegration | 1 | 1 (1 / 0) | 0 | 46 |
| PerfectoidSpaces | 1 | 1 (1 / 0) | 0 | 81 |
| SpinGeometry | 1 | 1 (1 / 0) | 0 | 64 |
| StableReduction | 1 | 2 (0 / 2) | 1 | 24 |
| SymplecticGeometry/CotangentLagrangian | 1 | 1 (1 / 0) | 1 | 92 |
| TaubesGromov | 1 | 1 (1 / 0) | 0 | 60 |
| VonNeumannAlgebras | 1 | 1 (1 / 0) | 0 | 36 |

Distinct definitions served: 62. Items: see per-roadmap sections.

## Key ordering facts across items

- SchemeAndStackFoundations §4.14 (Hilbert/Quot) is the choke point for the whole Jacobian cluster
  (defs 19, 24, 30, 71, 80, 84, 85). Required order: JacobianChallenge Layer C coherence and base
  change, then §4.12 (generic flatness), then §4.14, then Layer C `Sym^d`, then Layer D Picard scheme.
- SSF Layer 1 is a linear chain: §1.3 lemmas, then §1.5, §1.6, §1.7/§1.8, §1.9, then §1.19, §1.20,
  §1.21, §1.22, §1.23. §1.18 (`StackInGroupoids`) can start now in parallel.
- LieGroups Layer 7 (compact real form, Cartan involution θ) unblocks Layer 9 beyond `GL n`, and
  with it defs 1, 4, 54, 62, 79. It is ready now.
- EtaleCohomologyFoundations §F.0.1 (étale module sheaves) precedes every étale cohomology item
  (§F.1, §F.2.x, §F.4.x) and is ready now.
- RiemannianGeometry R5a (B, S, normal connection) is formally blocked on SmoothBundlesConnections
  B3–B4 per its README, though that dependency looks soft.

## TauCetiRoadmap/SchemeAndStackFoundations
STATUS.md snapshot: 22c431a3 2026-11-11, generated against Tau Ceti d9fbe7b (Tau Ceti checked at a6027b1d24, 2026-11-11)

### §1.3–§1.4 algebraic-space predicates and the category AlgSpace
- Status: PARTIAL: §1.3 predicates `SchemePresheaf`, `Spaces.RepresentableDiagonal`, `Spaces.EtaleAtlas`, `Spaces.IsAlgebraicSpace` with API in TauCeti/AlgebraicGeometry/AlgebraicSpace/Basic.lean. §1.4 `Spaces.AlgSpace`, `toPresheaf`, `ofScheme` (Full/Faithful), terminal `Spec ℤ`, initial `∅` in AlgebraicSpace/Category.lean. Missing: `IsAlgebraicSpace.diagonal_locallyQuasiFinite`, `isAlgebraicSpace_of_etale_cover` (§1.3), `AlgSpace.overEquiv` (§1.4).
- Ready now: yes (needs only Mathlib plus the existing Basic.lean)
- Serves defs: 16, 20, 28
- Evidence: README l.2180 "### 1.3 Representable diagonals, étale atlases and the algebraic-space predicate", l.2236 "### 1.4 The category of algebraic spaces"; STATUS Layer 1 remaining "atlas API for algebraic spaces (1.3), algebraic spaces over a base (overEquiv, 1.4), 1.5 onward"; grep finds no `diagonal_locallyQuasiFinite`, `isAlgebraicSpace_of_etale_cover`, `overEquiv` in AlgebraicSpace/.

### §1.2 fppf descent of quasi-finite morphisms and of algebraic spaces
- Status: NOT-STARTED
- Ready now: yes (README needs §1.3, whose predicates exist; it uses `isAlgebraicSpace_of_etale_cover`, so do that §1.3 lemma first)
- Serves defs: 20 ("fppf descent for alg spaces")
- Evidence: README l.2166 "### 1.2 Fppf descent of quasi-finite morphisms and of algebraic spaces", Needs l.2177 "§1.3; Mathlib `Presheaf.IsSheaf`, `MorphismProperty.presheaf`, `LocallyQuasiFinite`"; STATUS does not mention §1.2; no matching declarations in Tau Ceti.

### §1.5 étale equivalence relations and the quotient sheaf
- Status: NOT-STARTED (no `EtaleEquivRel`, `quotientSheaf.*`; TauCeti/AlgebraicGeometry/Quotient/EquivalenceRelation.lean is unrelated scheme quotient machinery)
- Ready now: yes (needs §1.3 only)
- Serves defs: 16, 20, 28 (as the start of the §1.6–§1.9 chain)
- Evidence: README l.2254 "### 1.5 Étale equivalence relations and the quotient sheaf", Needs l.2265 "§1.3; Mathlib `Etale`, `Presheaf.IsLocallySurjective`, `sheafify`, `pullback`"; grep `EtaleEquivRel` returns nothing.

### §1.6–§1.9 presentations, points |X|, fibre products and étale-local properties, separation and properness
- Status: NOT-STARTED (no `etaleQuotientTheorem`, `spacePresentation`, `points`, `isAlgebraicSpace_pullback`, `EtaleLocal`, `IsSeparatedSpace`, `IsProperSpace`)
- Ready now: no: §1.6 needs §1.5; §1.7 and §1.8 need §1.6; §1.9 needs §1.7 and §1.8
- Serves defs: 16, 20, 28 (§1.7 `points F` for 28; §1.9 `IsProperSpace` for 16/20)
- Evidence: README l.2292 "### 1.6 Quotients by étale equivalence relations and presentations" (Needs §1.3, §1.5), l.2306 "### 1.7 Points of an algebraic space" (Needs §1.3, §1.6), l.2333 "### 1.8 Fibre products and étale-local properties of morphisms" (Needs §1.3, §1.6), l.2401 "### 1.9 Separation and properness" (Needs §1.3, §1.7, §1.8); every named declaration greps empty.

### §1.14 groupoids in algebraic spaces, stabilizer, stabilizerAt
- Status: NOT-STARTED (TauCeti/AlgebraicGeometry/Inertia/Basic.lean is decomposition/inertia groups of a point under a group acting on a scheme, unrelated)
- Ready now: no: needs §1.5, §1.8, §1.13 (group spaces, which needs §1.4, §1.8)
- Serves defs: 28, 29
- Evidence: README l.2561 "### 1.14 Groupoids in algebraic spaces and stabilizers", l.2581 "`stabilizerAt` for a field-valued point. *Needs:* §1.5, §1.8, §1.13"; grep `stabilizerAt` returns nothing.

### §1.18 StackInGroupoids, stackification, 2-fibre products
- Status: NOT-STARTED (only the carrier `SchPseudofunctor` in TauCeti/AlgebraicGeometry/Stack/Basic.lean; §1.1's `Descent.qcohPseudofunctor`, affine comonadicity, and fpqc uniqueness of descended morphisms (`Scheme.Modules.Hom.ext_of_fpqc`, `Hom.isIso_of_fpqc`, `Descent.qcohPseudofunctor_faithful_toDescentData` in Descent/QuasicoherentSheaf/Separated.lean) are prerequisites, not §1.18)
- Ready now: yes in practice: README lists §1.1, which is PARTIAL (effectivity, i.e. `qcoh_fpqc_descent` itself, and `sheaf_stack` missing), but the §1.18 definitions themselves use only Mathlib `Pseudofunctor`, `IsStack`, `DescentData`, `CategoricalPullback`
- Serves defs: 20, 24, 27, 28, 29
- Evidence: README l.2849 "### 1.18 Stacks in groupoids, stackification and 2-fibre products", Needs l.2891 "§1.1; Mathlib `Pseudofunctor`, `IsStack`, ..."; grep `StackInGroupoids|twoFiberProduct|stackification` empty.

### §1.19 IsRepresentableBySpaces, IsAlgebraicStack, IsDeligneMumford
- Status: NOT-STARTED
- Ready now: no: needs §1.4 (partial), §1.9, §1.18
- Serves defs: 16, 17, 20, 24, 27, 28, 29
- Evidence: README l.2923 "### 1.19 Representable morphisms, algebraic stacks and Deligne–Mumford stacks", Needs l.2936 "§1.4, §1.9, §1.18"; grep `AlgebraicStack|DeligneMumford` empty.

### §1.20 inertia, automorphismGroup, Stacks.points, IsProperStack
- Status: NOT-STARTED
- Ready now: no: needs §1.7, §1.8, §1.9, §1.14, §1.18, §1.19
- Serves defs: 16, 24, 28, 29
- Evidence: README l.2949 "### 1.20 Inertia, the setoid criterion, properties of morphisms and presentations" (`automorphismGroup x` l.2952, `Stacks.points` l.2972, `IsProperStack` l.2990), Needs l.2972 and l.2995; grep `automorphismGroup` hits only unrelated algebra/topology files; `IsProperStack`, `Stacks.points` empty.

### §1.21 quotient stacks, BG, root stacks
- Status: NOT-STARTED
- Ready now: no: needs §1.13, §1.14, §1.15, §1.19, §1.20
- Serves defs: 17, 29
- Evidence: README l.3055 "### 1.21 Quotient stacks, line bundles with a section, root stacks", Needs l.3081; grep `QuotientStack|classifyingStack` empty.

### §1.22 Stacks.QCoh, QCoh.pushforward
- Status: NOT-STARTED
- Ready now: no: needs §1.1 (partial), §1.11, §1.18, §1.21
- Serves defs: 17, 27, 29
- Evidence: README l.3092 "### 1.22 Quasi-coherent modules on stacks", Needs l.3107 "§1.1, §1.11, §1.18, §1.21; Mathlib `CoGrothendieck`"; grep `Stacks.QCoh` empty.

### §1.23 moduli functors, coarse moduli, Keel–Mori, IsTame
- Status: NOT-STARTED (the existing `IsTame` hits are tame ramification, unrelated)
- Ready now: no: needs §1.17, §1.19, §1.20, §1.22
- Serves defs: 16, 17, 24
- Evidence: README l.3124 "### 1.23 Moduli functors, fine and coarse moduli spaces, Keel–Mori, tame stacks", Needs l.3155; grep `CoarseModuli|KeelMori` empty.

### §2.6 quasi-coherent cohomology (cited for 20)
- Status: PARTIAL: higher direct images and qcqs vanishing (AlgebraicGeometry/Cohomology/HigherDirectImage/*, QuasiSeparated.lean), the module presheaf `U ↦ Hⁿ(f⁻¹U, M)` with sheafification `Rⁿf_* M` as an `𝒪_Y`-module (`Scheme.Hom.higherDirectImagePresheaf`, `higherDirectImagePresheafSheafificationIso` in HigherDirectImage/Presheaf.lean), cohomology of `𝒪(m)` on `ℙⁿ_R` (Cohomology/ProjectiveSpace/*). The names `qcoh_higherDirectImages`, `projectiveSpace_cohomology`, `ample_serre_vanishing`, `QCoh.isAffine_of_H1_vanishing` are not present; quasi-coherence of `Rⁿf_*`, the affine computation, flat base change and filtered colimits are missing.
- Ready now: yes (needs §0.3, §0.4, both begun, plus existing Tau Ceti cohomology)
- Serves defs: 20, 21 (via §2.7, §2.10)
- Evidence: README l.3554 "### 2.6 Quasi-coherent cohomology", Needs "§0.3, §0.4; Tau Ceti `Scheme.Modules.Cohomology`"; STATUS does not list §2.6 among Layer 2's started sections; JacobianChallenge STATUS confirms the ℙⁿ computation exists.

### §2.7 cohomology with supports and local cohomology
- Status: NOT-STARTED
- Ready now: no: needs §0.17, §2.1, §2.6 (§2.6 partial; README's *Lean:* line says "nothing of this subsection")
- Serves defs: 21
- Evidence: README l.3613 "### 2.7 Cohomology with supports and local cohomology" (defines `sectionsWithSupport`, `cohomologyWithSupport` on the Zariski site for modules); grep `sectionsWithSupport|cohomologyWithSupport` empty.

### §2.10 comparisons between the fppf, étale, Nisnevich and Zariski topologies
- Status: NOT-STARTED (Nisnevich topology in AlgebraicGeometry/Sites/Nisnevich/ belongs to §2.12)
- Ready now: no: needs §2.1, §2.6, §2.9, §2.12 (all partial). The morphisms of topoi `epsilonFppfEtale`, `aX`, `etaleToNisnevich`, `nisnevichToZariski` could be defined from the Mathlib topologies plus the existing Nisnevich site; the cohomology comparisons cannot
- Serves defs: 21 (20 also cites it)
- Evidence: README l.3772 "### 2.10 Comparison morphisms between the topologies of a scheme", Needs "§2.1, §2.6, §2.9, §2.12"; grep `epsilonFppfEtale|nisnevichToZariski|quasiCoherent_topology_comparison` empty.

### §2.20 relative dualising complexes, Serre duality (cited for 20)
- Status: NOT-STARTED
- Ready now: no: needs §0.18, §2.18, §2.19, §2.21
- Serves defs: 20
- Evidence: README l.4452 "### 2.20 Relative dualising complexes and modules, Serre duality, curve comparison"; grep `relativeDualizingModule|RelativeDualizingComplex|cm_serre_duality` empty.

### §4.1 thickenings and formally smooth/étale morphisms (cited for 20)
- Status: PARTIAL: thickenings in TauCeti/AlgebraicGeometry/Morphisms/Thickening.lean; `Formal.FormallySmooth`, `smooth_iff_formallySmooth`, `smooth_lifting_torsor` missing
- Ready now: yes for the lifting definitions; `smooth_lifting_torsor` needs §2.3 (partial)
- Serves defs: 20
- Evidence: README l.5305 "### 4.1 Thickenings, formally smooth and étale morphisms, the lifting criterion, torsors of lifts", Needs "§2.3; Tau Ceti `.../Morphisms/Thickening.lean`"; STATUS Layer 4 remaining "lifting criterion (4.1)".

### §4.14 Hilbert/Quot/Hom/Isom schemes
- Status: NOT-STARTED for Hilbert/Quot/Hom/Isom (no `hilbert_quot_schemes`, Quot or Hilb functor anywhere in Tau Ceti)
- Ready now: no: needs §2.6 (partial), §4.12 (not started: no `generic_flatness`, `chow_lemma`), StableReduction Layer 2 (partial: "coherent cohomology and base change ... ampleness criterion and openness" remaining), JacobianChallenge Layer C (partial: "coherence of R^q f_* for proper f ... cohomology and base change" remaining). JacobianChallenge Layer C's Sym^d in turn consumes §4.14, so the order must be Layer C coherence, then §4.14, then Sym^d
- Serves defs: 24, 30 (and, through JacobianChallenge Layers C/D, 19, 71, 80, 84, 85)
- Evidence: README l.6008 "### 4.14 Hilbert and Quot schemes", Needs l.6025 "§2.6, §4.12; StableReduction Layer 2; JacobianChallenge Layer C". STATUS's Layer 4 "remaining" list (lifting criterion 4.1, deformation functors 4.3, formal functions and algebraization 4.9–4.10, strict transforms 4.11, Bertini 4.13) only names sections that have started; §4.14 is untouched, not done. The coverage prose says Layers 1–5 have "only their first definitions".

### §4.14 (Grassmannian clause) relative Grassmannian Gr(E, d), Plücker embedding
- Status: PARTIAL: the affine case is done. `Module.Grassmannian.scheme R M k` over `Spec R` for any module `M`, with charts and gluing (Grassmannian/Basic.lean), functor of points on affine tests (`schemeHomEquiv`, Points.lean), separated and proper for finite `M` (`isProper_toSpec`, Proper.lean), plus ideal/rank/isotropic loci and the universal quotient. Missing: a non-affine base `S`, representability on all `S`-schemes, the Plücker closed immersion with `det Q` very ample. No `Plucker` in AlgebraicGeometry; there is only linear-algebra `LinearAlgebra/Projectivization/Plucker.lean`.
- Ready now: yes. This clause does not need §4.12; it is the same object that ModularCurves §0G owns (see below), so implement it once there
- Serves defs: 25, 26
- Evidence: README l.6018–6025 "The construction embeds Quot into a relative Grassmannian, which is stated here: for `S` Noetherian, `E` locally free of rank `r`..."; ModularCurves §0G claims ownership of the same object.

### §4.15 StableCurves.Mbar g n
- Status: NOT-STARTED (grep `Mbar|StableCurves|isom_stable_curves` empty)
- Ready now: no: the definition needs §1.18 `StackInGroupoids` (not started) and StableReduction Layer 3 stable families (partial: "semistable and stable families with their criteria" remaining). Algebraicity needs §1.20, §4.6, §4.14 and StableReduction Layers 2–3, 8–9 (l.6086)
- Serves defs: 24
- Evidence: README l.6037 "### 4.15 The moduli stack of stable pointed curves" ("Define `StableCurves.Mbar g n : StackInGroupoids` (§1.18)").

### §4.11 modifications and strict transforms (weak link for 25)
- Status: PARTIAL: `TauCeti.AlgebraicGeometry.IsModification` with `.birational`, `.comp`, `.isIso_of_isFinite` (Morphisms/Modification/*), and the strict transform under a blow-up as a scheme-theoretic closure (Blowup/StrictTransform.lean, Blowup/Pullback.lean). Missing: `IsModification.centre`, `.functionField_equiv`, `.isAlteration`, and the general witness-based `strictTransform*` API (`strictTransform_eq_closure`, `strictTransformModule`, `strictTransform_supportComparison`).
- Ready now: yes (Needs §0.9 and StableReduction Layer 4 blow-ups, which exist)
- Serves defs: 25
- Evidence: README l.5820 "### 4.11 Modifications and strict transforms"; STATUS Layer 4 remaining "strict transforms (4.11)"; grep results above.

### §0.20 Japanese/Nagata rings, finiteness of normalization
- Status: PARTIAL: `TauCeti.Ring.IsN1`, `IsJapanese`, `IsUniversallyJapanese`, `IsNagata` and their API (RingTheory/Japanese.lean, Nagata.lean, UniversallyJapanese.lean), `IsJapanese.polynomial`, `IsUniversallyJapanese.isNagata_of_finiteType`, and `isFinite_fromNormalization_of_isJapanese` (AlgebraicGeometry/Normalization/Finite.lean). Missing: Nagata's theorem, i.e. `IsNagata.polynomial`, `IsNagata.of_finiteType`, `isNagata_iff_isUniversallyJapanese`, `nagata_normalization_finite`, and the complete-local cases.
- Ready now: yes (Needs only existing Tau Ceti files)
- Serves defs: 26
- Evidence: README l.1448 "### 0.20 Japanese and Nagata rings"; STATUS Layer 0 remaining "complete local Nagata (0.20), 0.21", which understates §0.20: grep shows none of the missing names. 26's finiteness does not wait on this item: finite-type algebras over a field are Japanese and Nagata (`IsUniversallyJapanese.of_field`, `.isJapanese`, `.isNagata_of_finiteType`), and `isFinite_fromNormalization_of_isJapanese` turns that into finiteness of normalization for integral schemes of finite type over `k`.

### §3.3 degrees of vector bundles
- Status: PARTIAL: `FiniteLocallyFreeSheaf.FixedRank.vectorBundleDegree` (VectorBundle/Degree.lean) with additivity in short exact sequences under finiteness hypotheses on cohomology (`vectorBundleDegree_add_of_shortExact`, `_of_isCurveOver`), `_elementaryModification`, `_baseChange`, twisting by a line bundle and by an effective Cartier divisor (`vectorBundleDegree_twist`, `vectorBundleDegree_twist_of_isEffective`), and tensoring a finitely supported modification with a vector bundle (`vectorBundleDegree_tensor_eq_add_mul_eulerCharBelow_of_shortExact`). Rank-one Riemann–Roch `InvertibleSheaf.eulerCharBelow_eq_relativeDegree_add_one_sub_genus` (WeilDivisor/Scheme/RiemannRoch/Basic.lean) and `LineBundleClass.intersectionNumber` (IntersectionNumber/Basic.lean). Missing: `_tensor` for a general vector bundle `V`, `_dual`, `_det`, `vectorBundleDegree_pullback`, the discharge of the finiteness hypotheses on proper `X` of dimension `≤ 1`, `vectorBundle_riemann_roch`, `curve_serre_duality`.
- Ready now: yes for `_tensor`, `_dual`, `_det` and `vectorBundleDegree_pullback` under the existing finiteness hypotheses (the dual and determinant are in VectorBundle/Dual/ and VectorBundle/Determinant/); discharging the hypotheses needs §2.6, and Riemann–Roch and duality need §2.6 and §2.20
- Serves defs: 24 (curve class β)
- Evidence: README l.4917 "### 3.3 Degrees of vector bundles, Riemann–Roch and Serre duality on curves"; STATUS Layer 3 remaining "degree laws for tensor, dual, determinant and pullback, and Riemann-Roch on curves (3.3)".

### §3.7 Picard stacks, universal sections, Abel maps
- Status: NOT-STARTED (`picardStack`, `sectionStack`, `picard_norm_sequence` absent). Functor-level Abel maps exist in TauCeti/AlgebraicGeometry/PicardFunctor/Abel/*, but they belong to JacobianChallenge Layers D/F, not to §3.7's stack-level maps.
- Ready now: no: needs §1.18, §1.19, §3.4, §3.5, §3.6 and JacobianChallenge Layers C–D
- Serves defs: 30
- Evidence: README l.5173 "### 3.7 Picard stacks, universal sections, Abel maps and the norm sequence", Needs l.5210 "§1.18, §1.19, §3.4, §3.5, §3.6; JacobianChallenge Layers C–D".

### §5.2 proper pushforward beyond closed immersions
- Status: PARTIAL: cycle-level pushforward over a field, `Chow.cyclesMap` (functorial, degree-compatible), in Chow/Pushforward.lean, plus Chow-group pushforward along closed immersions (Chow/ClosedImmersion.lean). Missing: descent of proper pushforward to `ChowGroup`, `flatPullback`, `flatPullback_properPushforward`, `localization_exact`.
- Ready now: yes (needs §5.1, which is present; injectivity of homotopy invariance needs §5.4)
- Serves defs: 16, 27
- Evidence: README l.7000 "### 5.2 Proper pushforward, flat pullback and the localisation sequence"; STATUS Layer 5 remaining "proper pushforward beyond closed immersions and flat pullback (5.2)".

### §5.4 projective bundles and Chern classes
- Status: NOT-STARTED (grep `chernClass|ChernClass|firstChernClass` empty in AlgebraicGeometry)
- Ready now: no: needs §0.3 (begun), §5.2 (partial), §5.3 (not started; needs §3.3, §5.1, §5.2)
- Serves defs: 27
- Evidence: README l.7065 "### 5.4 Projective bundles and Chern classes", Needs l.7085 "§0.3, §5.2, §5.3; AlgebraicVectorBundles".

### §5.5 normalCone, deformationToNormalCone, refined Gysin
- Status: NOT-STARTED
- Ready now: no: needs §0.2, §0.3, §5.2, §5.3, §5.4 and StableReduction Layer 4. `normalCone` and `conormal` as definitions need only §0.2 (relative Spec) and Mathlib `reesAlgebra`, so they could start now
- Serves defs: 27
- Evidence: README l.7109 "### 5.5 Normal cones, deformation to the normal cone and refined Gysin maps", Needs l.7160–7162; grep `normalCone|deformationToNormalCone|refinedGysin` empty.

### §5.9–§5.10 surface pairing Chow.intersectionNumber, numerical equivalence, Num
- Status: NOT-STARTED: `Chow.intersectionNumber`, `Chow.NumericallyEquivalent`, `Num` exist only in Suggested.lean/README. Tau Ceti's `LineBundleClass.intersectionNumber` is line bundle against curve, not the surface pairing.
- Ready now: yes for the definitions. §5.9's `Chow.intersectionNumber` needs only the existing `eulerCharBelow`, `InvertibleSheaf.dual` and `.tensorProduct` (LineBundle/Dual.lean, TensorProduct.lean). `Num` needs that pairing and `Scheme.IsProjectiveOver` (l.7620). The theorems (Hodge index, Riemann–Roch on surfaces) need §2.20, §3.3, §5.3, §5.6.
- Serves defs: 19
- Evidence: README l.7461 "### 5.9 Surfaces: the relative intersection pairing ...", l.7565 "### 5.10 ...", l.7579 "**Numerical equivalence.** *Chow.NumericallyEquivalent* / *Num*"; grep `NumericallyEquivalent` empty.

### §5.10 "Numerical Néron–Severi finiteness" `Num.free_finiteRank`
- Status: NOT-STARTED
- Ready now: no: needs `Num` (above) and the Néron–Severi theorem
- Serves defs: 78 (paper only, not the definition)
- Evidence: README l.7589 "**Numerical Néron–Severi finiteness.** *Num.free_finiteRank*". It is stated only for smooth projective surfaces over algebraically closed fields.

## TauCetiRoadmap/ReductiveGroupsPartII
STATUS.md snapshot: d92acc5 2026-11-09 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### RG2.0 Topologies on rational points (local and adelic G(F_v))
- Status: PARTIAL. Exists: the affine point topology and topological group (Topology/Algebra/PointTopology/Basic.lean, Group.lean, Separation.lean); compact open integral points `isOpenEmbedding_integralPoints` (Topology/Algebra/PointTopology/IntegralPoints.lean); congruence subgroups (Algebra/AlgebraicGroup/CongruenceSubgroup/Topology.lean, ProP.lean); scheme point topology (PointTopology/Scheme/). Missing (STATUS): smooth maps open on points, analytic charts and Haar Jacobians (the archimedean charts are here), Frobenius fixed points of Ĕ, and scheme-level functoriality.
- Ready now: yes. The remaining items depend only on this layer and on Mathlib/LocalFields. Adelic points themselves are owned by AdelicAlgebraicGroups, not this roadmap.
- Serves defs: 67, 68, 73, 83, 90
- Evidence: README l.437 "## Layer RG2.0: topologies on rational points"; STATUS "remaining: smooth maps open on points, analytic charts and Haar Jacobians, Frobenius fixed points of Ĕ, scheme-level functoriality".

### RG2.0a Weil restriction and the Deligne torus S
- Status: PARTIAL. Weil restriction exists: Algebra/HopfAlgebra/WeilRestriction.lean (`WeilRestriction.homEquiv`, `pointsMulEquiv`); RingTheory/WeilRestriction/{Basic,Splitting,Composition,Smooth,Etale}.lean; point-topology comparison Topology/Algebra/PointTopology/WeilRestriction.lean; norm tori with ℂ/ℝ real points (Algebra/AlgebraicGroup/NormTorus/Complex.lean). The README names `ResHopf`, `mapHopf` and `functor_isCorepresentable` do not exist under those names. The Deligne torus (`DeligneTorus.S`, `complexSplitting`, `weight`, `mu`, …) is missing.
- Ready now: yes. The Deligne torus needs norm-torus, separable splitting and the points-topology comparison, all present.
- Serves defs: 13, 23, 68
- Evidence: README l.943 "## Layer RG2.0a: Weil restriction and the Deligne torus", l.1379 "### RG2.0a.3 the Deligne torus" (*deligne-torus*); STATUS "remaining: Deligne torus, integral Weil restriction, Edixhoven tame fixed points, descent of reductivity"; grep DeligneTorus/deligneTorus finds nothing.

### RG2.3 (RG2.3.1) Reductive integral models and hyperspecial subgroups
- Status: NOT-STARTED. No `SmoothModel`, `IsHyperspecialSubgroup` or `ModelField`. The relative reductivity predicate `reductiveCommHopfAlgPropertyOver` exists (Algebra/AlgebraicGroup/Reductive/Over.lean).
- Ready now: yes for RG2.3.1 (*smooth-affine-model*, *reductive-model*): it needs RG2.0 integral points (done) and ReductiveGroups Layer 3. The rest of RG2.3 (parahorics, Bruhat-Tits schemes) needs RG2.1 (partial) and RG2.2 (untouched).
- Serves defs: 67, 82, 83
- Evidence: README l.3760 "## Layer RG2.3: parahoric and congruence group schemes", l.3858 "**Reductive models over O and hyperspecial subgroups.** (*reductive-model*)"; STATUS RG2.3 "untouched".

### RG2.5 Dual group and L-group
- Status: NOT-STARTED. No `AbsoluteRootData`, `LGroup` or dual-group declarations. Supplier pieces exist: `TauCeti.Pinning`, `RootPairingIsogeny`, `centerGroupScheme`, `IsCentralIsogeny`.
- Ready now: no: needs RG2.1 (π₁(G), z-extensions; partial), the ReductiveGroups Layer 7 root datum and the Layer 9 pinned Chevalley-Demazure group (both partial).
- Serves defs: 11, 88
- Evidence: README l.6704 "## Layer RG2.5: integral dual data", l.6724 "### RG2.5.1 the dual group and its Galois action", l.6931 "### RG2.5.2 the L-group and its functoriality"; STATUS RG2.5 "untouched".

## TauCetiRoadmap/RepresentationTheory/LieGroups
STATUS.md snapshot: c4312fa 2026-11-09 (umbrella RepresentationTheory/STATUS.md; Tau Ceti checked at a6027b1d24, 2026-11-11)

### Layer 7 (first bullet) Compact real form of a complex semisimple Lie algebra; Cartan involution θ of a real semisimple 𝔤₀
- Status: NOT-STARTED. There are no `compactRealForm`/`CartanInvolution`-style Lie-algebra declarations. Ingredients that exist: Serre presentation iso `serreLiftEquiv` (Algebra/Lie/Presentation/Serre/Injective.lean), complex-linear `serreChevalleyInvolution` (Algebra/Lie/Presentation/Serre/Automorphism.lean), Chevalley involution and structure-constant normalization (Algebra/Lie/Weights/Chevalley/Involution.lean, Algebra/Lie/Weights/StructureConstant/Normalization.lean).
- Ready now: yes. This is a purely Lie-algebraic bullet. Its inputs (LieHighestWeight Layer 7 Serre presentation and Layer 0 sl₂ strings) are in place. The conjugate-linear τ, H_τ positivity, real-form descent and θ = στ|𝔤₀ can all be built now. The later group-level Layer 7 bullets (universal complexification, compact integration) are not ready: they need Layer 4 integration (partial) and Layer 5 covers.
- Serves defs: 1, 4, 54, 62, 79
- Evidence: README l.787 "### Layer 7: complexification and real forms", first bullet l.788 "**Compact real forms of semisimple Lie algebras.**", θ at l.802-806 ("Layer 9 consumes this θ"); STATUS Layer 7 "untouched"; grep for compactRealForm/CompactRealForm/realForm in Lie files gives nothing relevant.

### Layer 9 Cartan, Iwasawa, KAK decompositions (CartanInvolution, IsRealReductive, cartan_polar_decomposition, IwasawaData, restricted roots, kakDecomposition)
- Status: PARTIAL. Only the GL_n matrix cases exist: Iwasawa `iwasawaDiffeomorph` (Geometry/Lie/Iwasawa.lean, LinearAlgebra/Matrix/GeneralLinearGroup/Iwasawa.lean), KAK for GL_n(ℝ/ℂ) (LinearAlgebra/Matrix/GeneralLinearGroup/Cartan.lean), maximal compact (…/MaximalCompact.lean), symplectic polar and Cartan involution (Analysis/Matrix/Polar/Symplectic.lean, Geometry/Lie/Symplectic/Cartan.lean), and unitary upper-triangular with positive diagonal = 1 (Analysis/Matrix/Triangular.lean). None of the Suggested.lean names exist: `FiniteCartanMatrixModel`, `CartanInvolution`, `IsRealReductive`, `IwasawaData`, `IsIwasawaTriple`, `iwasawaDecomposition`, `kakDecomposition`, `cartan_polar_decomposition`, `restrictedRoots`, `Nplus`, `triangularRealDiagonal`, `positiveTriangular`, `bijOn_exp_triangular`, `lieExp_bijective_of_immersed_positiveTriangular`.
- Ready now: partly. Ready: the global matrix-cover model with `cartan_polar_decomposition` for a closed transpose-stable H ≤ GL_N (it consumes only the matrix polar decomposition), and the "Connected subgroups of the positive triangular group" bullet. Not ready: the semisimple finite-center specialization, restricted roots/KAK and the general Iwasawa theorem. These need Layer 7's θ (not started) and Layer 6 tori (partial).
- Serves defs: 1, 4, 54, 62, 79, 83
- Evidence: README l.1199 "### Layer 9: the Cartan, Iwasawa, and KAK decompositions", l.1230 `cartan_polar_decomposition`/`CartanInvolution`/`IsRealReductive`, l.1354 "**Restricted roots and KAK.**"; STATUS "remaining: the global real-reductive Cartan, Iwasawa and KAK decompositions beyond GL n"; Suggested.lean l.459-652.

### Layer 5 enveloping-algebra bullet U(𝔤) as left-invariant differential operators; central characters
- Status: PARTIAL. Done: `TauCeti.envelopingAction` and `range_envelopingAction` (Geometry/Lie/EnvelopingAlgebra/Basic.lean); `envelopingAction_injective` and `envelopingAlgEquivAdjoin` (Geometry/Lie/EnvelopingAlgebra/Faithful.lean). Missing: the stated real/complex central-character packaging `Z(U_ℝ(𝔤)) → Z(End_U(V))` for irreducible real modules. The highest-weight version exists in LieHighestWeight (`vermaCentralCharacter`), and centre eigenspaces are in Algebra/Lie/UniversalEnveloping/CenterEigenspace.lean.
- Ready now: yes. Layer 5's other bullets (covers, centres) are listed separately; this bullet needs only LieHighestWeight Layer 3 PBW, which is done.
- Serves defs: 1, 5, 83
- Evidence: README l.518 "### Layer 5: simply-connected covers and the enveloping algebra", bullet l.626 "**The universal enveloping algebra.**"; STATUS Layer 5 "partial" (no remaining text); grep envelopingAction hits the 2 files above.

### Layer 8 Borel-Weil, complex flag manifolds, Bruhat (minimal parabolics P_α)
- Status: NOT-STARTED
- Ready now: no: needs the Layer 7 algebraization of compact complexifications and ReductiveGroups Layer 7 generic Bruhat (partial).
- Serves defs: 4 (weak link)
- Evidence: README l.1078 "### Layer 8: Borel-Weil, flag manifolds, and Bruhat"; the minimal parabolics are complex algebraic P_α ⊂ G_ℂ (l.1155 "minimal-parabolic map pα:G/B+→G/Pα+"), not real parabolics; STATUS Layer 8 "untouched".

## TauCetiRoadmap/JacobianChallenge
STATUS.md snapshot: 385ec2d 2026-11-06 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### Layer C Sym^d X = Hilb^d
- Status: PARTIAL: the functor `Div_{X/S}` of relative effective Cartier divisors and its degree subfunctor (EffectiveCartierDivisor/Functor.lean, Degree/), representability for d = 0 and d = 1 (`graphDivisorDegreeOne`, EffectiveCartierDivisor/Representable.lean). No `Sym^d X` for d ≥ 2.
- Ready now: no: README l.208 routes it through SchemeAndStackFoundations §4.14 Hilbert schemes (not started), which itself needs Layer C's coherence of `R^q f_*` (remaining)
- Serves defs: 30
- Evidence: README l.203–210 "Relative effective Cartier divisors and symmetric powers ... Use SchemeAndStackFoundations §4.14's Hilbert schemes"; STATUS Layer C remaining "... Sym^d X".

### Layer D Picard scheme, Pic^0, Jacobian
- Status: PARTIAL: fppf Picard sheaf `relativePicardFppfSheaf`, rigidified functor, `Pic⁰_{X/S}` with base change, functor-level Abel maps (PicardFunctor/*). The `AbelianVariety` carrier exists, and `JacobianVariety` is only named in a docstring (AbelianVariety/Basic.lean l.29), not defined. Missing: the obstruction sequence, Hilbert quotients, representability (`pointedCurvePicard_representable`), smoothness and properness of Pic⁰.
- Ready now: no: the Hilbert-quotient and representability steps need SchemeAndStackFoundations §4.14 and Layer C. The obstruction sequence needs SchemeAndStackFoundations §1.1, §2.2, §2.11.
- Serves defs: 19, 30, 71, 80, 84, 85
- Evidence: README l.218 "### Layer D, the relative Picard functor and the Jacobian scheme"; STATUS "Layer D ... lacks the obstruction sequence, Hilbert quotients, representability, smoothness and properness".

### Layer E polarizations, theta W_{g-1}, theorem of the cube
- Status: PARTIAL (rigidity, tangent space, dimension zero, elliptic curves). No cube or square theorem, polarization, or `W_{g−1}`/theta (grep `theorem_of_cube|thetaDivisor|IsPolarization` empty).
- Ready now: no: theta needs Layer D `Pic^{g−1}` (representability) and Layer C `Sym^{g−1}`. The cube theorem (Milne's proof via seesaw) needs Layer C cohomology and base change (remaining).
- Serves defs: 30, 80
- Evidence: README l.333 "**Cube and square.**", l.387 "**Polarizations and theta.** ... construct the Cartier divisor `W_{g−1} ⊂ Pic^{g−1}`"; STATUS "no cube theorem, projectivity, dual, polarization".

### Layer F Abel–Jacobi
- Status: PARTIAL: Abel–Jacobi on functors of points (PicardFunctor/Abel/{Jacobi,Fppf,PicZero}.lean), the `AbelianVariety.IsAlbanese` carrier (AbelianVariety/Albanese.lean). No Abel–Jacobi morphism of schemes, universal property, or base change.
- Ready now: no: needs the Layer D Jacobian scheme and Layer E duality/biduality
- Serves defs: 30
- Evidence: README l.448 "### Layer F, Abel–Jacobi and the universal property"; STATUS "Layer F states the Albanese property, and has Abel–Jacobi on functors of points, but no Abel–Jacobi morphism of schemes".

## TauCetiRoadmap/ReductiveGroups
STATUS.md snapshot: 7a6772d 2026-11-10 (Tau Ceti checked at a6027b1d24, 2026-11-11; README at roadmap 5f7befb6, after PR #1332)

### Layer 5 (solvable groups) Structure of smooth connected solvable groups, G = G_u ⋊ T
- Status: PARTIAL. Exists: `torus_coinvariants_unipotentRadical` (G/G_u is a torus). Missing: that a maximal torus T meets G_u trivially and maps isomorphically onto G/G_u, the decomposition G = G_u ⋊ T, and conjugacy of subgroups of multiplicative type into T by G_u(k̄) (Milne, Theorem 16.33(b),(d)). STATUS lists Layer 5 as done.
- Ready now: yes. It is the input that Layer 7 torus conjugacy, and through it the root datum, wait on.
- Serves defs: 1, 4, 11, 23, 79
- Evidence: README l.2268 "## Layer 5: solvable and unipotent groups; the unipotent radical", l.2293 "**Solvable groups.**" bullet ("Prove, over `k̄`, the decomposition `G = G_u ⋊ T` ... (Milne, Theorem 16.33(d), p. 336)"; *Needs:* the unipotent theory, the pinned Lie–Kolchin theorem and torus quotient, Layer 4's tori, Layer 3's quotients); grep finds no `G_u ⋊ T` decomposition in Algebra/AlgebraicGroup/Solvable/ (SemidirectProduct.lean only proves solvability of semidirect products); Layer 7 torus conjugacy goes through Borel containment (Borel/Conjugacy/Containment.lean) and then conjugacy of maximal tori inside the solvable Borel.

### Layer 7 Root datum, relative root system, parabolics P_G(λ) and Levi decompositions
- Status: PARTIAL. Exists: the parabolic predicates `IsParabolic`/`IsParabolicOverAlgClosed` (Algebra/AlgebraicGroup/Parabolic/Basic.lean); dynamic `parabolicDefiningHopfIdeal`/`leviDefiningHopfIdeal` with `parabolicLeviFppfQuotientIso` (Algebra/AlgebraicGroup/Dynamic/…); GL_n weight parabolics proved parabolic (Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/Borel.lean); torus conjugacy under extra hypotheses (Torus/Conjugation.lean). Missing: `StructureAcceptance.exists_conjugate_eq_of_isMaximalTorus` (unconditional), `exists_levi_complement_of_isParabolic`, `exists_titsSystem_of_isBorel`, P_G(λ) parabolic for general reductive G, the root datum of (G,T), and the relative root system.
- Ready now: no. Unconditional torus conjugacy needs the structure of smooth connected solvable groups, G = G_u ⋊ T with subgroups of multiplicative type conjugate into T by G_u(k̄) (Milne, Theorem 16.33(b),(d)). The README assigns this to Layer 5's "Solvable groups" bullet, which STATUS lists as done, but Tau Ceti has only `torus_coinvariants_unipotentRadical` (G/G_u is a torus); Borel containment (Borel/Conjugacy/Containment.lean) is in place. The split root datum needs torus conjugacy, then the rank-one subgroups G_α with their coroots (Milne 21.11) and generation of N/T by reflections (Milne 21.37). The roots, pinnings and rational Weyl group exist (Tangent/RootSpace.lean, Pinning/Basic.lean, DiagonalizableGroup/Normalizer/WeylGroup.lean). The completeness of G/P needs the Layer 3 quotient representability (partial). Bruhat cells need Layer 7C (partial).
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
- Evidence: README l.4976 "## Layer 9D: classification, relative groups and forms", l.4977 "The **isomorphism** and **existence theorems**: split reductive groups ↔ root data"; STATUS "remaining: isomorphism and existence theorems, multiplicative type over a base, …".

### 3A.5e The complex Lie group G(ℂ)
- Status: NOT-STARTED. Only the pinned inputs exist: point topology and topological group `TauCeti.PointTopology.isTopologicalGroup` (Topology/Algebra/PointTopology/Group.lean) and scheme point topology with charts (Topology/Algebra/PointTopology/Scheme/Charts.lean). No complex manifold or Lie-group structure on G(ℂ).
- Ready now: no: needs 3A.5b-3A.5d (open-chart embeddings, scheme-level fibre product, smooth complex charts). STATUS lists these as the 3A remainder ("complex-point comparison").
- Serves defs: 68
- Evidence: README l.1914 "**3A.5e The complex Lie group `G(ℂ)`.**" ("By 3A.5c–3A.5d, `G(ℂ)` is a Hausdorff, second-countable complex manifold"); STATUS 3A "remaining: complex-point comparison, restriction to O(1) sections and remaining worked tests"; supplier contract l.1058 "The library does not state that an affine open chart is an open embedding…".

## TauCetiRoadmap/RiemannianGeometry
STATUS.md snapshot: d9fbe7b 2026-11-11 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### R5a Immersion geometry: pullback connection, normal bundle, B, S, ∇⊥
- Status: PARTIAL: flat-ambient groundwork only: `TauCeti.secondFundamentalForm` (Analysis/InnerProductSpace/SecondFundamentalForm.lean:82), `shapeOperator` (Analysis/InnerProductSpace/ShapeOperator.lean:90), Gauss formula along curves (Geometry/Manifold/VectorBundle/CovariantDerivative/AlongCurve/Immersion.lean), embedding normal spaces (Geometry/Manifold/SmoothEmbedding/NormalSpace/), pullback metric along immersions (Geometry/Manifold/Riemannian/Pullback/Basic.lean:237). Nothing for a Riemannian ambient: no pullback ambient connection, normal bundle ν_f, intrinsic B, S, ∇⊥, or Gauss/Codazzi/Ricci
- Ready now: normal-bundle comparison: yes (needs SBC B2.1 pullback/Hom bundles, which Mathlib already supplies natively, and GT 1.5 normal bundle, pinned in Tau Ceti). B/S/∇⊥: no per README, which lists "SmoothBundlesConnections B2–B4" (B3–B4 untouched). This dependency looks soft, since R5a uses Tau Ceti's vector-bundle `CovariantDerivative`, not principal connections; R1 curvature is done
- Serves defs: 31, 49, 52, 65, 66
- Evidence: README l.2840 "### R5a. Immersion geometry and first variation"; *Needs* l.2866 "SmoothBundlesConnections B2.1 (smooth pullback and Hom bundles); GeometricTopology Layer 1 (embedding normal bundle)" and l.2935 "R1 curvature and tensor connections; R5a smooth normal comparison; SmoothBundlesConnections B2–B4"; STATUS coverage Layer 5 remaining "R5a beyond flat-ambient groundwork, and all of R5b"; grep `normalConnection|meanCurvature|principalCurvature` in Tau Ceti: no hits

### R5a.1 Orientation-free C² relative volume
- Status: NOT-STARTED (`riemannianVolume` and the immersion pullback metric exist; no relative density J_t / relative-volume functional)
- Ready now: no: needs R5a induced metric (available via `ContMDiffRiemannianMetric.pullback`) and DG Layer 12 densities (12.4 Riemannian density/integralDensity missing)
- Serves defs: 52
- Evidence: README l.2939 "#### R5a.1. Orientation-free C² relative volume"; *Needs* l.2993 "R5a induced metric; DifferentialGeometry Layer 12 densities"

### R5a.2 Principal curvatures, H, minimality, first variation, minimal cones
- Status: NOT-STARTED (only the Euclidean B/S above)
- Ready now: no: needs R5a's B/S pairing; the first-variation part also needs R5a.1 and DG Layer 12 integration/divergence
- Serves defs: 49, 52, 65, 66
- Evidence: README l.2997 "#### R5a.2. First variation and immersion examples", "Define principal curvatures as the eigenvalues of S_ν ... H=(tr B)/m ... minimality is H=0"; l.3034 "minimal cone equivalence away from the cone vertex"; *Needs* l.3022

### R5b Second variation, Jacobi operator, stability, Dirichlet index
- Status: NOT-STARTED (only the abstract coercive-form spectral API, e.g. `IsCoercive.isLeast_rayleighQuotient`, which the README consumes)
- Ready now: no: needs R5a, R5a.1, R5a.2
- Serves defs: 52, 65
- Evidence: README l.3216 "### R5b. General normal second variation and hypersurface stability", "consumes R5a's immersion geometry, R5a.1's ... relative-volume lemma and R5a.2's first variation"; l.3265 "Define the Dirichlet Jacobi operator L_D"; STATUS "R5b ... ha[s] not begun"

### R1.3 Normal homogeneous metrics on G/H
- Status: NOT-STARTED: Riemannian submersions have splitting, connection and O'Neill tensors with their symmetries and the integrability criterion for the horizontal distribution (Geometry/Manifold/Riemannian/Submersion/{Basic,Connection,ONeill,Integrability}.lean); no O'Neill curvature formulas and no homogeneous quotient metric. STATUS coverage Layer 1 remaining "... and the O'Neill curvature formulas"
- Ready now: no: needs SBC B1.4's smooth G/H (partial, no quotient yet; see below)
- Serves defs: 62
- Evidence: README l.1013 "### 1.3 Metric changes, Lie groups and submersions", l.1117 "construct the normal homogeneous metric on SBC B1.4's G/H ... prove G→G/H is a Riemannian submersion"

### R4 item 4 Cartan–Hadamard
- Status: NOT-STARTED: the supplier `norm_le_norm_mfderiv_riemannianExp_of_sectionalCurvature_nonpos` exists (Geometry/Manifold/Riemannian/Jacobi/Comparison.lean); no `cartanHadamard_isCoveringMap`, no R4.3 covering criterion
- Ready now: no: needs R4 item 3 (covering criterion for local isometries from complete manifolds; not in code). HopfRinow L4 is completed
- Serves defs: 62
- Evidence: README l.2207 "4. Cartan–Hadamard (`cartanHadamard_isCoveringMap`)", *Needs* l.2218 "R4.3 (covering criterion), HopfRinow (Completed) Layer 4"; STATUS "R4 has its models, the nonpositive-curvature exponential bound ... but no comparison theorem"

## TauCetiRoadmap/EtaleCohomologyFoundations
STATUS.md snapshot: 3150404 2026-10-23 (no coverage JSON; prose only. Tau Ceti checked at a6027b1d24, 2026-11-11, which is well ahead of this STATUS for §F.0.2)

### §F.0.2 Finite étale Galois categories and the étale fundamental groupoid
- Status: PARTIAL, and enough for def 84's use of π₁. In code: `PreGaloisCategory (FiniteEtaleScheme S)` for every S (AlgebraicGeometry/FiniteEtale/Quotient.lean:339); `FiberFunctor (fiber x)` and `GaloisCategory (FiniteEtaleScheme S)` for connected S, plus any two geometric points joined by a path (FiniteEtale/Galois/Category.lean:111); π₁(T,x) := `Aut (FiniteEtaleScheme.fiber x)` (profinite), with functoriality `mapAutFiber`/`mapFiberIso` and change of basepoint `mapAutFiber_conjAut` (Galois/Functoriality.lean); paths on disconnected bases versus connected components (Galois/Component.lean); `galContinuousMulEquivAutFiber : Gal(Ω/K) ≃ₜ* π₁(Spec K,x)` (Galois/FundamentalGroup.lean); finite étale K-group schemes ≃ finite Gal-modules (Galois/Basic.lean). Missing: a named `π₁` definition (it is used as `Aut (fiber x)`), `VanishingCycles.lisseMonodromyEquiv` (needs §F.0.1), `VanishingCycles.fieldSheavesEquiv`, the `Spec(k[x₁,x₂,…])` check.
- Ready now: yes for `fieldSheavesEquiv` and naming/packaging π₁. lisseMonodromyEquiv: no, needs §F.0.1 finite lisse Λ-module sheaves.
- Serves defs: 84
- Evidence: README l.200 "## F.0.2 Finite étale Galois categories and the étale fundamental groupoid" (`VanishingCycles.finiteEtaleGaloisCategory`). STATUS: "§F.0.2 is partial: most of the Galois-category axioms hold, but finite-group quotients, conservativity, the `GaloisCategory` instance, `π₁`, paths and lisse monodromy are missing". Every item in that list except lisse monodromy and a named `π₁` is in code (see above).

### §F.0.1 Finite and constructible étale module sheaves (prerequisite of every cohomology item below)
- Status: PARTIAL, minimal. AlgebraicGeometry/Sites/EtaleSepClosed.lean has étale sheaves (including `ModuleCat Λ`-valued) on Spec Ω ≃ coefficients, so a geometric point has no higher cohomology. FiniteEtale/Sheaf.lean has finite étale covers as étale sheaves of sets, with stalks equal to geometric fibres. Missing: `VanishingCycles.constructibleEtale` itself (module stalks, finite lisse, stratifications, constructibility, extension by zero, closure properties).
- Ready now: yes, mostly. The Mathlib inputs (smallEtaleTopology, AffineEtale.sheafEquiv, SheafOfModules) are present. The cited SchemeAndStackFoundations §§2.1, 2.9–2.10 have only first definitions (SSF STATUS a67a650), so work may have to supply local substitutes.
- Serves defs: 18, 19, 69, 77 (indirectly; F.1, F.4.x and F.0.2's monodromy all need it)
- Evidence: README l.175 "## F.0.1 Finite and constructible étale module sheaves". STATUS: "The source shows nothing for §F.0.1". Grep for `constructibleEtale|IsFiniteLisse|lisseMonodromy` in TauCeti finds nothing.

### §F.1 Derived sheaves and coherent diagrams: `finiteCoefficientCohomology` (cup products, Z/ℓⁿ cohomology)
- Status: NOT-STARTED. Neither `constructibleDerivedCategory` nor `finiteCoefficientCohomology` exists. No cup product on `Sheaf.H` or on étale cohomology exists in TauCeti or Mathlib. The cup files in TauCeti are for chain complexes, Hochschild cochains and Galois cohomology only.
- Ready now: no. It needs §§F.0.1–F.0.4, §0.7 (supportLocalization), EnhancedDerivedSheaves §§0.1–0.4 (`tensorHom`, `functorCoherence`, both not done) and SSF §§2.1–2.2, 2.5, 2.7, 2.17. A cup product on `Sheaf.H` stated as a `ShiftedHom` (PR #1891 design) could be built on Mathlib's DerivedCategory without the enhancement, but the README routes it through `ClassicalDerived.tensorHom`.
- Serves defs: 18 (cup products), 69, 77 (étale cohomology with Z/ℓⁿ coefficients)
- Evidence: README l.457 "## F.1 Derived sheaves and coherent diagrams". The cup product is in the second block "**Finite-coefficient cohomology and coherent actions.** `VanishingCycles.finiteCoefficientCohomology` ... Build cup products, coefficient restriction ...", whose *Needs* line cites "EnhancedDerivedSheaves §§0.3–0.4, especially tensorHom and functorCoherence". STATUS: "nothing ... for §§F.0.3–F.10".

### §F.2.1 Proper base change and §F.2.2 Smooth base change
- Status: NOT-STARTED. `VanishingCycles.etaleBaseChange`, `properBaseChange` and `smoothBaseChange` are absent.
- Ready now: no. F.2.1 needs SSF §§2.1–2.2 (Leray is still remaining per SSF STATUS) and EnhancedDerivedSheaves §§0.1–0.4. F.2.2 needs F.1 `finiteCoefficientCohomology` and SSF §0.9.
- Serves defs: 69 (and 77 through the étale cohomology of modular curves)
- Evidence: README l.504 "## F.2.1 Proper base change for arbitrary torsion" (`VanishingCycles.properBaseChange`). README l.522 "## F.2.2 Smooth base change in the rotated square" (`VanishingCycles.smoothBaseChange`). STATUS: base change "not started".

### §§F.4.1–F.4.2 Normalized adic systems and classical Z_ℓ realization
- Status: NOT-STARTED. `normalizedAdicSystems` and `classicalAdicRealization` are absent. Mathlib's pro-étale `Scheme.EllAdicCohomology` exists but is the §F.4.3 comparison target, not this.
- Ready now: no. Needs F.0.1–F.0.4, F.1, F.2–F.3 and EnhancedDerivedSheaves §0.3 `inverseLimits`/`derivedCompletion`. The last is not done (EDS Layer 0 remaining: "derived limits, completion comparison").
- Serves defs: 69 (Z_ℓ coefficients), 77
- Evidence: README l.959 "## F.4.1 Normalized bounded constructible systems" and l.979 "## F.4.2 Classical realization and finite-level cohomology limits". STATUS: adic realization "not started".

### §F.4.5 Rational realization and finite-dimensional cohomology (b₂)
- Status: NOT-STARTED. `VanishingCycles.rationalAdicRealization` is absent.
- Ready now: no. Its README *Needs* line is "normalizedAdicSystems through adicFiniteness" (§§F.4.1–F.4.4, which in turn need F.3 finiteness), §F.0.2, F.2 Künneth and §F.4.0 stable lattices. None of these except §F.0.2 has started. It is near the end of the ECF dependency chain.
- Serves defs: 19
- Evidence: README l.1041 "## F.4.5 Rational realization and finite-dimensional cohomology". It proves "`RΓ_(c)(X,K_Qℓ)≅RΓ_(c)(X,K_Zℓ)⊗ᴸℚ_ℓ`, finite-dimensional `Hⁱ_(c)`" for separated finite-type X over separably closed k, which is what b₂ needs. STATUS: adic realization "not started".

## TauCetiRoadmap/ComplexKahlerGeometry
STATUS.md snapshot: d9fbe7b 2026-11-11 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### K1 + K2 type calculus, T^{1,0}, (1,1)-forms, Dolbeault, i∂∂̄
- Status: PARTIAL: the pieces defs 14/38 need are in place: eigenbundles T^{1,0}/T^{0,1} (Geometry/Symplectic/Manifold/AlmostComplex/Eigenbundle/), type projections and `IsOfType φ J p q` (Geometry/Manifold/DifferentialForm/AlmostComplexType.lean:205), ∂, ∂̄, d=∂+∂̄, ∂̄²=0 (Geometry/Manifold/DifferentialForm/Dolbeault/{Basic,ComplexManifold}.lean), `dC` with ddᶜ=2i∂∂̄ (Dolbeault/DC.lean), Dolbeault complex and cohomology with pullback, wedge product and `H^(p,0)` (Dolbeault/{Complex,Cohomology,Wedge}.lean), the `(0,q)` polydisc Dolbeault–Grothendieck lemma on smaller concentric polydiscs (`exists_contDiffOn_delBarCoeff_eq_of_polydisc`, Analysis/Complex/Wirtinger/Polydisc.lean). Missing: Newlander–Nirenberg, parametrized submanifolds, the whole-polydisc `(p,q)` lemma, Dolbeault theorem; i∂∂̄ only for smooth forms (no C² version, which is not a target either)
- Ready now: yes (remaining K1/K2 work is not needed for defs 14/38)
- Serves defs: 14, 38
- Evidence: README l.370 "## Layer 1: complex structures and type calculus (K1)", l.558 "## Layer 2: Dolbeault calculus and the local lemmas (K2)"; STATUS "K1 is partial ... K2 is partial: ∂ and ∂̄ have their bidegrees ... `dᶜ = i(∂̄ − ∂)` satisfies `ddᶜ = 2i∂∂̄`"; grep confirms `typeProjection`, `IsOfType`, `dC`, `delBar_delBar_ofComplexManifold`

### §5.9 K5b.0 Hermitian metrics, fundamental form, dvol = ω^n/n!
- Status: NOT-STARTED (no Hermitian-metric-on-TM structure, no `ω^n/n!` comparison; `riemannianVolume` exists in Geometry/Manifold/Riemannian/VolumeDensity/Volume.lean:87, `SmoothTwoForm.Compatible` in Geometry/Symplectic/Manifold/TwoForm.lean:339)
- Ready now: no: README needs Layers 1, 2 and 4 (K4 barely started: no holomorphic bundles or Chern connections), 5.1's pointwise star/density layer (partial: the pointwise star, `DensityBundle` (Geometry/Manifold/VectorBundle/Density.lean) and the fixed-compact topology on compactly supported sections (Geometry/Manifold/VectorBundle/Section/CompactSupportTopology.lean) exist; the orientation line, `BundleTest` on density-twisted bundles and bundle distributions do not) and 5.7 formal adjoints (missing)
- Serves defs: 14, 38
- Evidence: README l.2198 "### 5.9 Local Hermitian identities on arbitrary complex manifolds (K5b, K5b.0)", "Prove `dvol_g=ω^n/n!` for the complex orientation"; *Needs* l.2240 "Layers 1, 2 and 4; 5.1's pointwise star and density layer and 5.7's formal adjoints"; STATUS "K4, K5b, K6, K7.2–K7.4 and K8 are untouched"; metric conventions `g(u,v)=ω(u,Jv)`, `h_T=g+iω` are pinned in Conventions l.147-160 (not a separate target)

### §6.1 K6.0 Kähler predicate IsKahler
- Status: NOT-STARTED: no `IsKahler` in Tau Ceti. All three ingredients of the Suggested.lean real-carrier definition exist: `SmoothForm.IsClosed` (Geometry/Manifold/DifferentialForm/Closed.lean:48), `SmoothTwoForm.Compatible` (Geometry/Symplectic/Manifold/TwoForm.lean:339), `nijenhuis` (Geometry/Symplectic/Manifold/Nijenhuis.lean:165)
- Ready now: the definition `IsKahler form J := form.IsClosed ∧ form.Compatible J ∧ J.nijenhuis = 0` (Suggested.lean l.398) is ready now. The rest of 6.1 is not: needs K4, 5.1's formal-adjoint comparison and K1 Newlander–Nirenberg for the complex-manifold comparison
- Serves defs: 14, 38
- Evidence: README l.2321 "### 6.1 Local Kähler and curvature identities (K6.0)", "The canonical predicate is a Hermitian metric on a complex manifold with closed fundamental form ... real-carrier condition `IsKahler form J`"; Dependencies l.2690 "6.1 uses Layers 1, 2 and 4 and 5.1's local formal-adjoint comparison"; grep `IsKahler` in Tau Ceti: no hits

### §5.7 K5a Hodge/Laplace self-adjoint H² realization, compact resolvent
- Status: NOT-STARTED: the smooth operators exist (`hodgeLaplacian` Geometry/Manifold/Riemannian/Codifferential.lean:246, `laplaceBeltrami` Geometry/Manifold/Riemannian/Laplacian.lean:274) and the abstract `LinearPMap.HasCompactResolvent` API exists (Analysis/InnerProductSpace/LinearPMap/CompactResolvent.lean), as do integer-order bundle Sobolev spaces `TauCeti.SobolevSection` over a finite bundle atlas (Geometry/Manifold/VectorBundle/Sobolev/), but there is no H² realization, real-order distributional Sobolev scale or Rellich on manifolds
- Ready now: no: needs PseudodifferentialOperators P1.0 (Layer 1 partial), 5.4 compact-bundle Sobolev scale (the distributional `BundleSobolev E s` is missing), 5.1 density/test layer (partial, see §5.9); HopfRinow L1 and DG 8.5 are in place
- Serves defs: 40
- Evidence: README l.1948 "### 5.7 Laplace-type estimates, spectral theory and the real Hodge theorem (K5a)", l.2013 "For every formally self-adjoint nonnegative Laplace-type system P on a compact boundaryless base, build its geometric H² realization", l.2038 "satisfies `LinearPMap.HasCompactResolvent`"; *Needs* l.2075; STATUS "K5a is partial: ... Hodge Laplacian ... chart `C^k` seminorms and the topology on smooth sections ... but not the orientation line, density bundle, bundle distributions or Sobolev scale"

### §5.3 K5a.SmoothSectionMontel Fréchet topology on smooth sections
- Status: PARTIAL: `ContMDiffSection.frameTopology` (Geometry/Manifold/VectorBundle/Section/Topology.lean:89) is a complete locally convex TVS of compact-derivative convergence (`ContMDiffSection.completeSpace_frameTopology`, Section/Complete.lean, with no compactness or countability hypothesis), with countable seminorms and metrizability (Section/CountableSeminorms.lean), atlas independence (Section/FrameCover.lean), restriction, Hausdorff, and continuous evaluation. Missing: the `MontelSpace` instance and the identification of the dual with compactly supported distributions.
- Ready now: no for the Montel and dual parts, which list 5.1 as a need.
- Serves defs: 63
- Evidence: README l.1620 "### 5.3 The smooth-section Fréchet topology and the Montel property (K5a.SmoothSectionMontel)"; completeness from Tau Ceti PR #32110 (Section/Complete.lean); grep `MontelSpace` finds only the complex-analysis Montel theorem (Analysis/Complex/Conformal/Montel/)

## TauCetiRoadmap/HeegaardFloer
STATUS.md snapshot: c0c3d15 2026-11-09 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### F2.1 (§4.1) spaces of smooth tame/compatible J, contraction, relative extension, C^∞ continuity
- Status: PARTIAL: linear `ContractibleSpace {J // ω.Tames J}` / `{J // ω.Compatible J}` (TauCeti/Geometry/Symplectic/Cayley/Contractible.lean) with operator-norm topology (Geometry/Symplectic/AlmostComplex/Topology.lean); on manifolds: nonemptiness `SmoothTwoForm.IsNondegenerate.exists_compatible` (…/Manifold/AlmostComplex/Polar.lean), smooth Cayley path `SmoothTwoForm.Compatible.cayleyPath` (CayleyPath.lean), relative extension from a closed set `Compatible.exists_compatible_eqOn` (Extension.lean), four-manifold metric criterion (Metric.lean), Darboux `IsSymplectic.exists_standardDarbouxChart` (…/Manifold/Darboux.lean). Missing: the space of smooth tame/compatible J on M as a topological space (C^∞ topology on compact sources), continuity of the contraction, finite-parameter relative family extension, finite-C^k estimates.
- Ready now: yes (the generic compact-derivative section topology `ContMDiffSection.frameTopology` in Geometry/Manifold/VectorBundle/Section/Topology.lean, complete by `ContMDiffSection.completeSpace_frameTopology` in Section/Complete.lean, can be put on End(TM); pointwise contraction and extension exist).
- Serves defs: 63
- Evidence: README l.2542 "Construct the spaces of smooth tame and compatible J on a finite-dimensional symplectic manifold ... C-infinity continuity on compact sources"; STATUS Layer 4 remaining "local theory, boundary Gromov compactness, transversality and gluing, nonsqueezing" (J-space not listed separately; prose "compatible structures on manifolds"); no `TopologicalSpace` instance on `SmoothAlmostComplexStructure` found.

### F0.5 (§2.7) finite-C^ℓ almost-complex parameter spaces and regularity-loss comparisons
- Status: PARTIAL: finite-regularity carriers `ContMDiffAlmostComplexStructure`, families `ContMDiffAlmostComplexStructureFamily`, chart reading/reconstruction `chartEquiv`, `inChart` (…/Manifold/AlmostComplex/{ContMDiff,Family,Chart,Family/Chart}.lean). Missing: the Banach manifold of C^ℓ tame/compatible J (conjugation charts, openness, Nemytskii estimates), universal CR section, derivative-budget comparisons.
- Ready now: no: needs F1.1–F1.2 `W^{1,p}`/bundle estimates (STATUS Layer 3 remaining) and F0.0 Banach-manifold floor (partial).
- Serves defs: 63 (also input to 56, 60 via F2.4/F2.6d)
- Evidence: README l.1873 "### 2.7 Regularity-loss comparisons for surface and strip Cauchy–Riemann sections (F0.5)"; STATUS Layer 3 remaining "W^{1,p} and bundle versions of the interior estimates, Sobolev spaces on strips ..."; grep `universalCauchyRiemann` none.

### F2.2 (§4.2) local theory: unique continuation, isolated critical points, adapted coordinates
- Status: NOT-STARTED. Inputs only: the scalar similarity principle (TauCeti/Analysis/Complex/Wirtinger/Similarity.lean) and the unique-continuation consequences of a similarity factorization `ξ = Φ σ` (`TauCeti.HasSimilarityFactorizationAt`, `eqOn_zero_of_hasSimilarityFactorizationAt_of_eqOn_zero`, `exists_analyticOrderAt_eq_of_hasSimilarityFactorizationAt` in Analysis/Complex/CauchyRiemann/UniqueContinuation.lean), with no theorem producing that factorization for a linear CR equation.
- Ready now: no: needs PH3.5 vector similarity principle and PH5.1 elliptic regularity (both not done), F1.1 Sobolev adapters.
- Serves defs: 60
- Evidence: README l.2592 "### 4.2 Local theory (F2.2)", *Needs* l.2643; STATUS Layer 4 remaining "local theory"; no isolated-critical-point/unique-continuation results for J-curves in Geometry/Symplectic/JHolomorphic/.

### F2.4 (§4.4) and F2.6d (§4.6d) universal moduli spaces, regular J
- Status: NOT-STARTED; local-coordinate linearization exists (`cauchyRiemannLinearization`, Geometry/Symplectic/JHolomorphic/Linearization.lean), the localized variation of a smooth J at an injective point (positive pairing with a cokernel covector, Geometry/Symplectic/Manifold/AlmostComplex/Variation.lean), and Fredholm/Sard–Smale scaffolding (Analysis/Fredholm/{SardSmale,UniversalLevelSet,Parametric}.lean).
- Ready now: no: needs F0.0 sharp Sard–Smale (only codim/index ≤ 2), F0.5 parameter spaces, F2.2 somewhere-injectivity, F1.2 adjoint identification; F2.6d also F2.6b–c and PH5.2.
- Serves defs: 56, 60, 63
- Evidence: README l.2688 "### 4.4 Transversality (F2.4)", *Needs* l.2711; l.2975 "### 4.6d Transversality and degree (F2.6d)", *Needs* l.3027; STATUS Layer 2 remaining "sharp Sard and Sard-Smale in higher codimension and index", Layer 4 "transversality and gluing".

### F2.6e (§4.6e) normal operator of embedded spheres, four-dimensional regularity
- Status: PARTIAL (local only): `normalCauchyRiemannLinearization`, descent of the linearization to `V ⧸ range du` in TauCeti/Geometry/Symplectic/JHolomorphic/Normal/Linearization.lean. Missing: normal bundle real CR operator, intersection multiplicities, Micallef–White, adjunction, automatic surjectivity for d ≥ −1.
- Ready now: no: needs F2.2, F2.6b, F1.5 line Riemann–Roch, F1.2 Hölder/Beltrami package.
- Serves defs: 60
- Evidence: README l.3029 "### 4.6e Four-dimensional curves and regularity (F2.6e)", "For an embedded sphere construct the quotient real CR operator on its normal" (l.3140), *Needs* l.3172.

### F4.B (§6.2) Spin^c, Turaev model, grading carrier
- Status: NOT-STARTED for Spin^c: no Turaev vector-field model, no Spin^c torsor, no c₁. Adjacent combinatorial code only: `HeegaardRegionSystem.WeaklyAdmissibleAt` (spin^c read through Maslov index of periodic domains) and relative grading in TauCeti/LowDimTopology/Heegaard/{SpincAdmissibility,RelativeGrading}.lean; the group `CliffordAlgebra.spinCGroup` = (Spin × U(1))/(−1,−1) with `det` and `toSpecialOrthogonal` (LinearAlgebra/CliffordAlgebra/Spin/SpinC.lean) and its Lie-group structure (Geometry/Lie/CliffordAlgebra/SpinC/Basic.lean).
- Ready now: no: needs F4.A geometric pointed diagrams (only combinatorial `HeegaardRegionSystem`, no handlebody-glued Y found) and F1.4–F1.5.
- Serves defs: 64
- Evidence: README l.3646 "### 6.2 Spinᶜ, periodic surfaces and the grading carrier (F4.B)", *Needs* l.3744; STATUS Layer 6 remaining "spin^c structures in general"; SpincAdmissibility.lean: "identification ... with the Chern class pairing is geometric and is not formalized here".

## TauCetiRoadmap/ModularCurves
STATUS.md snapshot: 7ca783d 2026-11-09 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### §0G relative finite-locally-free Grassmannian, Plücker
- Status: PARTIAL: affine case fully in Tau Ceti (TauCeti/AlgebraicGeometry/Grassmannian/*: `scheme`, `glueData`, `chartι`, `schemeHomEquiv`, `isProper_toSpec`, `schemeUniversalIdeal`, Hopf-ideal locus, `FiniteLocallyFree.lean`). Missing: gluing over a non-affine base with independence of trivialisations, universal quotient and kernel, base change, `Grass_1(F) ≅ Proj_S(Sym F)`, the Plücker closed immersion.
- Ready now: yes for gluing over a non-affine base. The rank-one identification and Plücker need StableReduction Layer 2's relative Proj and AlgebraicVectorBundles L0C/L2A (exterior powers, `gradedSymmetricAlgebra`).
- Serves defs: 25 (and 26)
- Evidence: README l.901 "### 0G. Parameter spaces for subgroup schemes" ("This block owns the relative Grassmannian of a finite locally free `𝒪_S`-module"); STATUS Layer 0 remaining "0G over a non-affine base".

### Layer 10 compactified coarse X_H, X_0(N)
- Status: NOT-STARTED (TauCeti/AlgebraicGeometry/ModularCurve/ has `Y₁(N)`, Legendre and level-three lines, no coarse `Y₀(N)` or `X_H`)
- Ready now: no: needs Layer 8 (`[Γ₀(N)]`; STATUS "8A; 8B beyond finiteness ...; 8C and 8D" remaining), Layer 9 quotients and coarse schemes (STATUS "everything beyond the Legendre and level-three rings"), the formal-cusp package and a Riemann–Hurwitz package
- Serves defs: 69, 71
- Evidence: README l.3145 "## Layer 10: compactified coarse curves over `ℤ[1/N]`, cusps, and the Shimura covering", Dependencies l.3364; STATUS "Layer 10 untouched".

## TauCetiRoadmap/SmoothBundlesConnections
STATUS.md snapshot: d92acc5 2026-11-09 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### B1.4 Slices, quotients and homogeneous spaces G/H
- Status: PARTIAL: Haar-averaged invariant Riemannian metrics for compact group actions (`exists_contMDiffRiemannianMetric_inner_mfderiv`, Geometry/Manifold/Riemannian/Invariant.lean), compact stabilizers and closed orbits of proper actions (`ProperSMul.isCompact_stabilizer`, `ProperSMul.isClosed_orbit`, Topology/Algebra/ProperAction/Orbit.lean), orbit maps of free points as closed smooth embeddings (`isSmoothEmbedding_smul_const`, Geometry/Manifold/GroupAction/Orbit.lean), transverse slice maps `(g, s) ↦ g • σ s` as local diffeomorphisms (`isLocalDiffeomorphAt_smul_slice_iff`, Geometry/Manifold/GroupAction/TransverseSlice.lean), equivariant charts for finite groups only (GroupAction/Linearization.lean), and quotients by discrete groups (Geometry/Manifold/Instances/Quotient.lean). Missing: the free proper quotient theorem `exists_freeProperQuotient_isSubmersion`, the compact-isotropy equivariant exponential chart and slice theorem `G ×_H B`, and smooth G/H for closed H
- Ready now: yes: B1.1 is in place, LieGroups Layer 2 is done, HopfRinow is completed, DG 12.1 auxiliary metrics and Geometry/Manifold/Instances/Quotient.lean exist; the free proper quotient theorem is the next step on the existing slices
- Serves defs: 62
- Evidence: README l.421 "### B1.4 Slices, quotients and homogeneous spaces", l.432 "Prove the free proper quotient theorem first by transverse local charts and properness"; *Needs* l.490; grep `freeProperQuotient` in Tau Ceti: no hits

### B2 pullback connection (as cited)
- Status: B2.1 (pullback/Hom/associated bundles) is PARTIAL: smooth associated bundles and complexification exist. B2 has no connection content
- Ready now: n/a (see R5a)
- Serves defs: 49
- Evidence: README l.559 "### B2.1 Associated bundles and complex structures" constructs pullback, tensor, dual and Hom bundles only; connection pullback is in B3.1 l.879 ("smoothness, pullback, restriction") and B3.3 l.948 for principal/associated connections

### B3–B4 Principal connections, curvature, gauge group
- Status: NOT-STARTED (Layers 3–7 "untouched"; the only gauge code is the U(1) vortex theory on ℂ, Analysis/PDE/Vortex/, which is unrelated)
- Ready now: no: B3.1 needs B1.5 (Ehresmann connections, untouched) and B2.5 (frame bundles/ad(P), missing); B4 needs B3.1–B3.3
- Serves defs: 37, 48
- Evidence: README l.871 "### B3.1 Principal connections" (*Needs* l.904 "B1.5, B2.5; DifferentialGeometry Layer 0, Layer 1; LieGroups Layer 1"), l.979 "### B4.1 Curvature and the exterior covariant derivative", l.1010 "### B4.2 The gauge group"; STATUS coverage Layer 3/4 "state":"untouched"

## TauCetiRoadmap/GeometricCurrents
STATUS.md snapshot: 5d671b9 2026-10-24 (stale: more Euclidean current code has landed since; Tau Ceti checked at a6027b1d24, 2026-11-11)

### G1–G2 Mass and pushforward of Lipschitz images
- Status: PARTIAL, Euclidean only: mass/local mass (Analysis/Distribution/Mass/Basic.lean), the Radon mass measure (Mass/Measure.lean), L¹ extension and Borel restriction (Mass/Extension.lean), normal currents (Mass/Normal.lean), weak compactness (Mass/Compactness.lean), smooth pushforward of compactly supported currents (Analysis/Distribution/CutoffPushforward.lean), integration and simplex currents. Missing: the manifold `TestForm`/`Current` carrier, integer-rectifiable currents, Lipschitz pushforward (G2), slicing
- Ready now: no for the manifold carrier: G1 needs K5a's early `BundleTest` (CKG 5.1, missing), Calib C1 comass and HopfRinow L0. G2 needs GMT G2–6 (G2 lacks tangent-plane uniqueness and the tangential area formula) and Calib C2. A Euclidean Lipschitz pushforward could start on the existing Euclidean carrier
- Serves defs: 57
- Evidence: README l.137 "## G1. Test forms, currents and mass", l.240 "## G2. Integer rectifiability, integration, pushforward and slicing", l.298 "Extend pushforward to locally Lipschitz maps"; dependency graph l.964-966; STATUS "G1 is partial, and only in its Euclidean part ... G2 ... untouched"

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
STATUS.md snapshot: 385ec2d 2026-11-06 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### G2 Rectifiable sets, approximate tangents, area formula
- Status: PARTIAL: `CountablyRectifiable`, the density theorem, a.e. existence of approximate tangent planes (Geometry/MeasureTheory/Rectifiable/ApproximateTangent.lean) and a measurable choice of tangent projections (Rectifiable/MeasurableTangent.lean), and the cone condition for the classical tangent plane of a differentiable normal graph (Rectifiable/Graph.lean). The Lipschitz area formula ℝᵐ→ℝⁿ with multiplicity is in MeasureTheory/Function/AreaFormula/{Basic,Lipschitz,Multiplicity}.lean, and there is coarea for surjective derivatives. Missing: a.e. uniqueness of tangent planes, tangential differentiation, the tangential area formula on rectifiable sets, and coarea for general Lipschitz maps
- Ready now: yes
- Serves defs: 53, 57
- Evidence: README l.148 "## G2: Rectifiability, area, and coarea"; STATUS coverage G2 remaining "uniqueness and measurability of tangent planes, tangential differentiation and area formula, coarea for general Lipschitz maps"

### G5 De Giorgi structure theorem
- Status: PARTIAL: perimeter API, essential and reduced boundaries, outer normal, density estimates, the `|Dχ| ≤ nω_n Hⁿ⁻¹` bound and separate blow-up ingredients. Missing: De Giorgi's theorem itself (rectifiability of ∂*E, `|Dχ_E| = Hⁿ⁻¹⌞∂*E`), the essential/reduced comparison, and the frontier criterion
- Ready now: yes (G3–G4 are essentially done; the needed G2 rectifiability API exists)
- Serves defs: 55
- Evidence: README l.248 "## G5: Finite perimeter and boundary structure", "Prove ... De Giorgi's structure theorem"; STATUS coverage G5 remaining "assembled blow-up, De Giorgi rectifiability and perimeter measure as Hausdorff measure on the reduced boundary ..."

## TauCetiRoadmap/CStarAlgebras
STATUS.md snapshot: 3930ad9 2026-11-11 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### C2.1 State extension
- Status: NOT-STARTED. State space API exists (`TauCeti.stateSpace`, `isCompact_stateSpace`, `stateSpace_nonempty` via Hahn–Banach, Krein–Milman `closure_convexHull_extremePoints_stateSpace`, `pullbackFunctional`) in TauCeti/Analysis/CStarAlgebra/StateSpace.lean; no extension from a subalgebra.
- Ready now: yes for the unital case (Hahn–Banach, Krein–Milman and states all available); the nonunital case goes through C1.2 unitization, which STATUS lists as remaining in Layer 1.
- Serves defs: 36
- Evidence: README l.544 "### 2.1 State extension (C2.1)", *Needs* "BanachSpaceTheory B1–B2; VonNeumannAlgebras V0"; no extension theorem in StateSpace.lean.

### C3.2 Completely bounded maps
- Status: NOT-STARTED (no `IsCompletelyBounded`/cb norm anywhere in TauCeti).
- Ready now: no: needs C3.1 abstract operator spaces (not started). The C*-algebra-only `IsCompletelyBounded` of Suggested.lean (via `CStarMatrix`) could be stated now.
- Serves defs: 36, 46
- Evidence: README l.918 "### 3.2 Completely bounded maps (C3.2)", *Needs* "§3.1; BanachSpaceTheory B1"; grep `CompletelyBounded|cbNorm` empty.

### C3.3 / C5.3 Column/row, MIN/MAX; operator-space tensor products
- Status: NOT-STARTED.
- Ready now: no: C3.3 needs C3.1–3.2; C5.3 needs §3.1–3.3 and §4.4 (Wittstock).
- Serves defs: 36, 46
- Evidence: README l.948 "### 3.3 Column and row spaces, MIN and MAX, operator algebras (C3.3)"; l.1169 "### 5.3 Operator-space tensor products (C5.3)", *Needs* "§3.1–§3.3, §4.4"; grep `OperatorSpace|Ruan` only unrelated hits.

### C4.1 Completely positive maps, Schwarz, multiplicative domain
- Status: NOT-STARTED in TauCeti (Mathlib `CompletelyPositiveMap`/`→CP` with only basic API; Schwarz exists only for C*-conditional expectations, TauCeti/Analysis/CStarAlgebra/ConditionalExpectation/Basic.lean).
- Ready now: partly: Schwarz and commutative-domain/range parts can start on Mathlib `→CP`; `‖φ‖_cb` needs C3.2, multiplicative-domain proof route needs §4.2 Stinespring, and VonNeumannAlgebras V13a (Layer 13 untouched).
- Serves defs: 36
- Evidence: README l.986 "### 4.1 Completely positive maps, Schwarz and the multiplicative domain (C4.1)", *Needs* "VonNeumannAlgebras V13a; Mathlib `CompletelyPositiveMap`, `CStarMatrix`; §4.2 for the dilation route"; grep `multiplicativeDomain|Kadison.*Schwarz` empty.

### C5.4 Direct sums, products, inductive limits, C*(F_∞)
- Status: NOT-STARTED (no C*-inductive limits; quotient C*-algebras exist in TauCeti/Analysis/CStarAlgebra/Quotient.lean).
- Ready now: yes (*Needs* "Mathlib `lp`; §1.3 (ideals and quotients)"; quotient by closed ideal present).
- Serves defs: 36
- Evidence: README l.1203 "### 5.4 Direct sums, products, inductive limits and the universal unitary algebra (C5.4)"; grep for C*-algebra `DirectLimit`/inductive limit empty.

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

## TauCetiRoadmap/DerivedModuleAlgebra
STATUS.md snapshot: d9fbe7b 2026-11-11 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### §0.4 The full cotangent complex and §0.8 transitivity triangle
- Status: NOT-STARTED. `Algebra.CotangentComplex` is absent. Only Mathlib's naive `Extension.cotangentComplex` is used. Inputs: the standard polynomial resolution stages and their varying-base maps exist (Algebra/Category/CommAlgCat/PolynomialResolution/{Basic,Map,Simplicial}.lean), but the resolution property does not.
- Ready now: no. §0.4 needs §0.1 (resolution property and the Lπ_! comparison missing) and §0.2 (derived tensor bifunctor and base-change adjunction missing; K-flat models exist). §0.8 needs §§0.4, 0.6 and 0.2.
- Serves defs: 27
- Evidence: README l.1271 "### 0.4 The full cotangent complex" (signature `Algebra.CotangentComplex (A B) : DerivedCategory (ModuleCat B)`); l.1463 "### 0.8 The cotangent transitivity triangle". STATUS Layer 2 remaining: "the full cotangent complex (§0.4) and everything built on it, §§0.6–0.25". Layer 1 remaining: "the derived tensor bifunctor and base-change adjunction, resolution comparison of §0.1 ...".

### §§1.2–1.3 derived I-completeness and completion; §1.7 I-completely flat
- Status: PARTIAL. §1.2: `TauCeti.derivedComplete` in D(A), the ideal `derivedCompleteIdeal`, radical/generator invariance, and the module telescope criterion `TauCeti.IsDerivedComplete` (RingTheory/AdicCompletion/DerivedComplete.lean, .../DerivedComplete/Module.lean). Missing from §1.2: the cohomology criterion. §1.3 completion reflector, §1.4–1.6 and §1.7 complete flatness are absent (no `derivedCompletion` or `completeFlatness` in code).
- Ready now: §1.3: no, needs §1.1.1 derived Hom with the tensor–Hom adjunction (`derivedHom` exists, adjunction remaining) and the rest of §1.2. §1.7: no, needs §0.2's derived tensor bifunctor.
- Serves defs: 81
- Evidence: README l.2024 "### 1.2 Derived ideal completeness", l.2064 "### 1.3 The derived completion reflector", l.2359 "### 1.7 Complete flatness and complete faithful flatness". STATUS Layer 3 remaining: "exactness of the derived limit, tensor–Hom adjunction, cohomology criterion for completeness, §§1.3–1.9".

## TauCetiRoadmap/EnhancedDerivedSheaves
STATUS.md snapshot: 385ec2d 2026-11-06 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### §0.3 Derived tensor and internal Hom `ClassicalDerived.tensorHom` (with §0.4 functorCoherence)
- Status: PARTIAL, inputs only. The K-flat half of §0.2 exists: every unbounded complex of sheaves of modules has a K-flat resolution by flat terms (`CochainComplex.exists_quasiIso_isKFlat_sheafOfModules`, Algebra/Category/ModuleCat/Sheaf/TensorProduct/KFlat.lean). Tensoring with a fixed K-flat complex descends to the derived category (`CochainComplex.kFlatTensor`, Algebra/Homology/Monoidal/KFlat/DerivedTensor.lean). Missing: the derived tensor bifunctor on sheaves, internal RHom, the tensor–Hom adjunction, K-injective replacement on ringed sites, the enhanced category (§0.1) and all of §0.4.
- Ready now: no, as the README specifies it. §0.3 needs §§0.1–0.2, i.e. the enhanced category via the dg nerve, which needs E0.6 shift/cone comparison and E0.8 presentability, both remaining. A homotopy-category-level ⊗ᴸ on `DerivedCategory (SheafOfModules R)` from the existing K-flat resolutions could start now as a substep.
- Serves defs: 18
- Evidence: README l.455 "### 0.3 Tensor, internal Hom and derived limits" ("provide `ClassicalDerived.tensorHom`: K-flat replacement defines `⊗ᴸ_R` ..."). README l.492 "### 0.4 Coherent derived functors". STATUS Layer 0 remaining: "K-injective replacement on ringed sites, the enhanced module-sheaf category, derived tensor-Hom, derived limits, completion comparison, functor coherence".

### Layer E5:cotangent-export The cotangent complex of animated rings
- Status: NOT-STARTED. No `squareZeroExtension` (animated), `derivedDerivations` or animated `cotangentComplex`.
- Ready now: no. Needs E5:animation (`animatedAlgebras`, `animatedModules`, `animationExtension`, `animatedPushout`; untouched) and DerivedModuleAlgebra §§0.4–0.13 (not started).
- Serves defs: 27
- Evidence: README l.2865 "## Layer E5:cotangent-export: The cotangent complex of animated rings". STATUS coverage: "Layer E5 ... untouched".

## TauCetiRoadmap/GeometricTopology
STATUS.md snapshot: 3987f93 2026-11-09 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### Layer 1.1 Smooth collars
- Status: NOT-STARTED for smooth collars. Topological collars exist: `IsCollar`/`IsCollared` (Geometry/Manifold/Boundary/Collar/Global.lean:46), Brown's collaring theorem (Collar/Brown.lean) and `boundaryCollar` (Collar/Euclidean.lean:65). There is no smooth collar structure, no existence theorem, and no uniqueness up to isotopy
- Ready now: yes, with a caveat: the README needs DG Layer 3 flows (smooth flow dependence is done), but flowing an inward vector field on a manifold with boundary may need more than the boundaryless flow API
- Serves defs: 66
- Evidence: README l.788 "### 1.1 Smooth collars"; STATUS coverage Layer 1 remaining "general boundary collars, gluing along boundary pieces and handle attachment"

### 1.7 / 1.7.2 Compact smooth surfaces, Mod(F)
- Status: NOT-STARTED (no mapping class group or surface Dehn twists; the `DehnTwist` hits are group-theoretic HNN/pushout files)
- Ready now: the Mod(F) definition alone: yes, since Layer 3.1 (Diff(M) topology, Layer 3 done) is all it needs. The 1.7.2 theorems: no, they need 1.7, and 1.7 needs Layer 11.2.1 (partial), 1.2, 1.3 (missing), 1.3.1, 1.4 and 11.3
- Serves defs: 59
- Evidence: README l.1049 "### 1.7 Compact smooth surfaces" (*Needs* l.1096), l.1212 "### 1.7.2 Mapping class groups of compact surfaces and Dehn twists" (*Needs* l.1279 "Layer 1.5 ..., Layer 1.7 ..., Layer 3.1 ..., Layer 3.3 ..., Layer 3.4")

## TauCetiRoadmap/OperatorTheory/SelfAdjointSpectralTheory
STATUS.md snapshot: 9b8af47 2026-11-09 (umbrella OperatorTheory/STATUS.md; Tau Ceti checked at a6027b1d24, 2026-11-11)

### SA-E01, SA-E03–E07 Spectral PVM of an unbounded self-adjoint operator, projections, resolvent formula
- Status: NOT-STARTED (no `ProjValMeasure ℝ` built from a `LinearPMap`). Inputs present: unitary Cayley transform `IsSelfAdjoint.cayley_mem_unitary` (Analysis/InnerProductSpace/LinearPMap/Cayley.lean), bounded normal `ContinuousLinearMap.spectralPVM` (Analysis/InnerProductSpace/BorelCalculus/Basic.lean), reindexing `ProjValMeasure.map` (ProjValMeasure/Map.lean), resolvent API (LinearPMap/Resolvent.lean).
- Ready now: yes (Part D done, Part B PVM/Borel calculus and SA-B25 present; SA-E02 zero mass at 1 must be proved first). SA-E09 later needs Part C SA-C12–19 (Part C partial).
- Serves defs: 35, 45
- Evidence: README l.1202 "SA-E01: Spectral PVM of an unbounded self-adjoint operator", l.1208–1215 SA-E03..E07; STATUS Part E remaining "the unbounded spectral PVM, resolvent formula, generated group and Stone uniqueness"; Suggested.lean l.692 `spectralPVM (hA : IsSelfAdjoint A) : ProjValMeasure ℝ H := sorry`.

## TauCetiRoadmap/PseudodifferentialOperators
STATUS.md snapshot: d92acc5 2026-11-09 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### §5.4 Compact-base C^{k,α} Hölder spaces
- Status: NOT-STARTED: Euclidean `CkHolderSpace`/`HolderSpace` exist (Analysis/Holder/), but no Hölder space on a manifold (grep `HolderSpace` under Geometry/: no hits)
- Ready now: the scalar/bundle C^{k,α} norm sub-item ("by chart/connection comparisons"): yes in practice, since Euclidean C^{k,α} and the finite-atlas C^k infrastructure exist. The whole §5.4 (Zygmund C^r_*, mapping theorems): no, it needs P2–P4 (partial) and §5.3 Besov estimates
- Serves defs: 32
- Evidence: README l.1337 "### 5.4 Hölder, Zygmund and little Hölder spaces", "Supply the compact-base bundle C^(k,α) norms by chart/connection comparisons"; *Needs* l.1428; STATUS coverage Layer 5 remaining "... Holder-Zygmund mapping ..."

### P7 §7.1 and P7a §8.1 Scalar self-adjoint Laplacian realization on closed manifolds
- Status: NOT-STARTED (Layer 7 has "only one preparatory step"; Layer 8 untouched)
- Ready now: no: §7.1 needs P6 (untouched) and K5a's realization (CKG §5.7, not started). §8.1 needs RiemannianGeometry R4.7, P5 density, P6 and P7
- Serves defs: 40
- Evidence: README l.1600 "### 7.1 Powers and their Sobolev domains" ("Consume K5a's generic nonnegative Laplace-system self-adjoint H² realization"), l.1935 "### 8.1 Quotients and the scalar realization" (*Needs* l.1981); STATUS "Layers 6 and 8 are untouched, and Layer 7 has only one preparatory step"

## TauCetiRoadmap/PseudoholomorphicCurveAnalysis
STATUS.md snapshot: 4973204 2026-11-09 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### PH6.1 Sobolev sections over compact surfaces with boundary
- Status: PARTIAL: a generic boundaryless bundle carrier `TauCeti.SobolevSection A μ p k` (`W^{k,p}(V)` over a `FiniteBundleAtlas`, closedness/completeness, `lowerOrderL`) exists in TauCeti/Geometry/Manifold/VectorBundle/Sobolev/{Basic,ContMDiffSection,SMul}.lean, and for surfaces modelled on `ℂ` its chart readings are the local classes `MemWkpLoc` and conversely (`TauCeti.SobolevSection.memWkpLoc_coord`, `exists_ae_eq_coord_of_memWkpLoc`, Sobolev/Local.lean), in arbitrary bundle charts rather than isothermal ones. Missing: the whole `∂Σ ≠ ∅` construction (half-disc atlas, norm independence, Rellich, Morrey, multiplication for kp>2), comparison with P5.2 on interior subsurfaces.
- Ready now: no: needs PH2.4 isothermal coordinates/bordered atlas (partial; no isothermal charts in code), PH1.2 Morrey/algebra/composition at higher order (partial: first-order chain rule and multiplication in Analysis/Sobolev/Local/{ChainRule,Multiplication}.lean; the half-disc higher-order reflection with its weak derivative `HasWeakFDerivOn.planarReflection` is in Local/Reflection.lean), PDE Lane A item 6 trace; the boundaryless sub-case could start against the existing carrier.
- Serves defs: 56, 60
- Evidence: README l.1045 "### 6.1 Sobolev sections over compact surfaces with boundary"; STATUS coverage `{"id":"Layer 6","state":"untouched"}`, Layer 1 remaining "Morrey, algebra, composition ... half-disc extension theorem"; grep `SobolevSection` hits only the generic bundle files above.

### PH6.2 Real Cauchy–Riemann operators
- Status: PARTIAL: the smooth half is in code (newer than STATUS): `TauCeti.IsRealCauchyRiemannOperator` (Leibniz-rule definition), `difference`/`isZeroOneForm_difference` (two operators differ by a zeroth-order (0,1)-form), `add_zeroOrder`, complex-linear part `sectionComplexLinearPart` + `antilinearPart` with uniqueness (MS Ex. C.1.7), and `IsCovariantDerivativeOn.isRealCauchyRiemannOperator_zeroOnePart` (a complex connection gives `(∇)^{0,1}`), in TauCeti/Geometry/Manifold/VectorBundle/CauchyRiemann/{Basic,Connection}.lean. Missing: operators of class `W^{ℓ−1,p}` (`D = D₀ + α`), their realizations `W^{ℓ,p} → W^{ℓ−1,p}` with totally real boundary condition `F`.
- Ready now: no: the Sobolev-class part needs PH6.1.
- Serves defs: 56, 60
- Evidence: README l.1083 "### 6.2 Real Cauchy–Riemann operators"; STATUS (2026-11-08) Layer 6 "untouched"; grep `IsRealCauchyRiemannOperator` -> CauchyRiemann/Basic.lean (496 lines), Connection.lean.

### PH6.3 Fredholm property, kernel and cokernel
- Status: NOT-STARTED (generic Fredholm library exists: TauCeti/Analysis/Fredholm/*, incl. Adjoint, CompactPerturbation, DeterminantLine; nothing CR-specific).
- Ready now: no: needs PH6.1–6.2 Sobolev realizations, PH3.3–3.5 (Sobolev-coefficient, boundary estimates, vector similarity principle; not started), PH4.1, PH2.4.
- Serves defs: 56, 60
- Evidence: README l.1128 "### 6.3 Fredholm property, kernel and cokernel"; deps l.1215 "PH1 (through PH6.1's localizations), PH2.4, PH3.3–PH3.5, PH4.1"; STATUS Layer 3 remaining "higher-order Hölder gain, W1p bound for T, Sobolev-coefficient and boundary estimates, vector similarity principle".

### PH7 (7.1 Maslov index of a bundle pair, 7.2 Riemann–Roch)
- Status: PARTIAL (ingredients only): loop Maslov index `TotallyRealLoop.maslovIndex`, `maslovIndex_map/_prod/_rotation` in TauCeti/LinearAlgebra/TotallyReal/Maslov/*.lean; STATUS also cites nowhere-vanishing sections in high rank and Hermitian metrics. No doubled bundle `E_F`, no `μ(E,F)`, no index formula.
- Ready now: no: 7.1 needs PH2.4's Schottky double as a Riemann surface (only a topological double exists); 7.2 needs PH6 (incl. 6.3) and PH3.5, plus CharacteristicClasses C2.3/C3.2 and AlgebraicTopology Stage 6/7.1/8.7.
- Serves defs: 56, 60
- Evidence: README l.1223 "### 7.1 Maslov index of a bundle pair", l.1271 "### 7.2 Riemann–Roch" ("prove `ind_ℝ D = nχ(Σ) + μ(E, F)`"); STATUS Layer 7 remaining "Maslov index of a bundle pair and Riemann–Roch; only splitting-step ingredients exist".

## TauCetiRoadmap/AdicEtaleGeometry
STATUS.md snapshot: 93d1fe5 2026-10-26 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### Layer A0 Completed tensor products and fibre products
- Status: PARTIAL, more than STATUS says. In code: `Huber.IsCompletedPushout` and the Huber-pair `completedTensor` (RingTheory/Huber/TensorProduct/{Pushout,Pair,Plus,UniversalProperty}.lean). Ring-level associativity, symmetry and unit (TensorProduct/{Associator,Symmetry,Unit}.lean; A0.7 at ring level). Rational localisation (TensorProduct/Rational.lean; A0.4 algebra). Finite étale base change (TensorProduct/FiniteEtale.lean; A0.5 algebra). Transitivity (BaseChange.lean). Affinoid fibre products `AdicSpace.affinoid_isPullback`, `affinoid_isPullback_of_isStablySheafyRing_left/right`, and Tate point lifting `exists_ofPair_completedTensor_point` (AlgebraicGeometry/AdicSpace/Pullback/Affinoid.lean). A0.8 in full: analytic points, the analytic locus `PreAdicSpace.analyticLocus` with `analyticLocus.ι`, `analyticLocus.lift`, `analyticLocus.range_ι` (AlgebraicGeometry/AdicSpace/PreAdicSpace/Analytic.lean), the cartesian restriction square for adic morphisms `IsAdic.isPullback_analyticLocusMap` (Morphisms/AnalyticLocus.lean), and `isAdic_iff_mapsTo_analyticPoints` (Morphisms/Adic.lean). Missing: global (glued) fibre products, `AdicSpace.FibreProduct.lift`/`ofPairPushout`, chart independence (A0.6), and the adic-space-level A0.4/A0.5/A0.7 comparisons.
- Ready now: yes for the A0.4/A0.5/A0.7 adic-space packaging. The glued fibre product depends on AdicSpacesPartII R0.7 existence (below).
- Serves defs: 22
- Evidence: README l.747 "## Layer A0: completed tensor products and the fibre products actually used". STATUS: "A0.1–A0.7 are untouched", and A0.8's analytic locus listed as remaining; both are stale against code a6027b1d24.

### A1.6 étale/finite étale sites, A1.7 geometric points, A1.14 change of base field
- Status: NOT-STARTED. No `AdicSpace.IsEtaleLocalDescription`, `AdicSpace.smallEtale` or `smallEtaleTopology` for adic spaces. What exists in A1: A1.0.0, A1.0.1, the morphism half of A1.0.3, and part of A1.2 (`finiteAlgebra.homEquiv`).
- Ready now: no. A1.6 needs *strongly-sheafy-huber-pair* (A1.1), *etale-morphism* and *etale-base-change* (A1.3–A1.5) and A0 pullbacks. A1.7 needs A1.6. A1.14 needs the pro-étale site (A1.10–A1.12, *proetale-coherence*), the etale-descent targets and AdicSpacesPartII R0.7/R0.19.
- Serves defs: 22
- Evidence: README l.3259 "### A1.6 the étale and finite étale sites" (*etale-site*, `AdicSpace.smallEtale X`); l.3670 "### A1.7 geometric points, enough points, strict localisations"; l.5511 "### A1.14 coherence and change of base field" (*etale-descent-along-algebraic-extension* l.5539, *proetale-field-extension-slice* l.5565). STATUS remaining: "A1.0.2, object descent in A1.0.3, A1.0.4-5, A1.1, A1.2 fibres and base change, A1.3 onward".

## TauCetiRoadmap/AdicSpacesPartII
STATUS.md snapshot: 1c6a1a4 2026-11-11 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### R0.7 Fibre products (and R0.6 lft for rigid spaces)
- Status: PARTIAL. *valuation-amalgamation* (`ValuationSpectrum.exists_amalgamation`) is done. *affinoid-fibre-product* is in code (`TauCeti.AdicSpace.affinoid_isPullback`, `isPullback_ofPair_of_isCompletedPushout`, the unconditional version when one factor is stably sheafy and the other is topologically of finite type; AlgebraicGeometry/AdicSpace/Pullback/Affinoid.lean). Missing: the non-adic ascending-union case, *fibre-products-existence* (`hasPullback_of_finiteType`), `exists_pullback_point` and base-change stability. For "rigid space lft" (R0.6): `IsAdic`, `LocallyOfWeaklyFiniteType`, `LocallyOfPlusWeaklyFiniteType` and `QuasiCompact` exist (AdicSpace/Morphisms/); finite presentation and locally Huber-standard spaces are missing.
- Ready now: yes for gluing affinoid fibre products to *fibre-products-existence* in the lft-over-stably-sheafy case (the gluing step uses the Huber-pair rational-localisation comparison of R0.3, whose ring-level form is RingTheory/Huber/TensorProduct/Rational.lean). The non-adic case needs R0.6 completion. R0.2 sheafiness for noetherian rings of definition (*noetherian-type-stably-sheafy*, partial) remains a prerequisite for the noetherian-type charts.
- Serves defs: 22
- Evidence: README l.3557 "### R0.7 fibre products" (*affinoid-fibre-product* at ~l.3622, *fibre-products-existence* at ~l.3702). *fibre-products-existence* Needs l.3736 (*affinoid-fibre-product*, *fibre-product-along-finite-type*, *adic-iff-analytic-locus*, *noetherian-type-stably-sheafy*, ...). STATUS remaining: "non-affinoid fibre products (R0.7)", with "The Huber-pair form of the rational-localisation comparison (R0.3) is a prerequisite".

## TauCetiRoadmap/AdicSpacesPartIV
STATUS.md snapshot: 7ca783d 2026-11-09 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### R4.1–R4.6 étale sites on analytic adic spaces, rigid comparison, geometric points
- Status: NOT-STARTED for the site theory. Only R4.7 algebraic normal-crossings charts and the punctured-disc noncompactness check exist.
- Ready now: no. R4 re-exports AdicEtaleGeometry A1's *etale-site* (not started) onto R0/R1 carriers. R4.4's rigid comparison also needs AdicSpacesPartII R1 (untouched).
- Serves defs: 22
- Evidence: README l.562 "## Layer R4: étale and pro-étale sites"; l.583 "### R4.1 the étale site on the analytic carriers"; l.727 "### R4.4 rigid comparison"; l.827 "### R4.6 geometric points and pullback". The Checks at l.1712 have Sh(X_ét) ≃ continuous Gal(K^sep/K)-sets via ξ. STATUS remaining: "the étale and pro-étale sites, nu, rigid comparison and geometric points".

## TauCetiRoadmap/CharacteristicClasses
STATUS.md snapshot: d92acc5 2026-11-09 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### C4 Chern–Weil forms
- Status: NOT-STARTED (no Chern–Weil code; grep `ChernWeil`: no hits)
- Ready now: no: C4.1 applies invariant polynomials to "SBC's principal curvature" (SBC B4.1, untouched); comparisons need C1–C3 (C1 partial, C3 untouched)
- Serves defs: 48
- Evidence: README l.1321 "## C4. Curvature classes and their integral comparison", item 1 "Apply them to curvature using DG's value-bundle wedge/composition and SBC's principal curvature"; l.1996 "C4's invariant-form construction and line comparison use C1–C3 and the smooth suppliers"; STATUS "C3, C4, C5, C5a and C7 are untouched"

## TauCetiRoadmap/DGAInfinity
STATUS.md snapshot: 7ca783d 2026-11-09 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### Layer 8 Hochschild cochains (ordinary algebras, normalized, HH²)
- Status: PARTIAL. Positive-arity Hochschild cochains of an A∞ algebra, with the Hochschild differential `[m,-]`, braces, the Gerstenhaber bracket and cohomology (Algebra/Homology/AInfinity/Algebra/Hochschild/{Basic,Complex,Cohomology}.lean). Normalized cochains for a strict unit, `PositiveHochschild.normalizedComplex` (Hochschild/Normalized.lean); whether the inclusion is a quasi-isomorphism is not addressed. Formal deformations and obstruction classes in Hochschild degree two (Deformation.lean); first-order deformations are degree-one cocycles. An ordinary or DG algebra becomes an A∞ algebra via `IsNonUnitalDGAlgebra.toAInfinityAlgebra` (DG.lean). For an ordinary algebra `A` and an `A`-bimodule `M` (so `M = A` gives Cⁿ(A,A)), the multilinear cochains `Aⁿ → M` in every arity including zero carry the Hochschild coboundary `TauCeti.hochschildBimoduleCoboundary` with `δ ∘ δ = 0`, degree-zero cocycles the centre and degree-one cocycles the derivations (RingTheory/HochschildCohomology/Coboundary.lean); the packaged cochain complex and cohomology there, `hochschildCochainComplex`/`hochschildCohomology` (Complex.lean), have coefficients in `Hom_R(A, M)`, not in `M`. Missing: the cochain complex and cohomology HHⁿ(A, M) with bimodule coefficients, HH² ↔ infinitesimal deformations and HH³ ↔ obstructions for ordinary algebras, normalization comparison, and quasi-equivalence/Morita invariance.
- Ready now: yes. The README names no blocking prerequisites for the ordinary-algebra HH²/HH³ clause, and both the A∞ machinery it specializes and the bimodule-coefficient coboundary are present.
- Serves defs: 10
- Evidence: README l.520 "### Layer 8: Hochschild cochains, deformations, Massey products, and formality" ("For an ordinary associative algebra, recover `HH²` for infinitesimal deformations and `HH³` for obstructions"). STATUS remaining: "normalization and invariance comparisons, Deligne groupoids over Q-algebras, higher Massey products".

## TauCetiRoadmap/DifferentialGeometry
STATUS.md snapshot: d9fbe7b 2026-11-11 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### Layer 12 (12.4 density, 12.5 divergence theorem)
- Status: PARTIAL: `riemannianVolume`, the gradient, divergence and Laplacian, and the boundaryless compactly supported divergence theorem `integral_divergence_eq_zero` (Geometry/Manifold/Riemannian/DivergenceTheorem.lean:225) exist. Missing: the 12.4 Riemannian density and its `integralDensity` link, and the 12.5 boundary divergence theorem `integral_divergence_eq_boundaryFlux`
- Ready now: no: 12.4 needs 5.5a's `integralDensity` and its agreement with top-form integration. The rest of 5.5a is in code: `Density`, `RoughDensity` and the density `toDensity` of a top form and an orientation (LinearAlgebra/Density/{Basic,Orientation}.lean, Geometry/Manifold/Density/Basic.lean), and the smooth `DensityBundle` (Geometry/Manifold/VectorBundle/Density.lean). `integralDensity` itself needs only 5.2 (form integration, in code), so it can start now. 12.5 needs 12.4. Compactly supported variations on boundaryless sources can already use `integral_divergence_eq_zero`
- Serves defs: 52
- Evidence: README l.2796 "### Layer 12: Riemannian metrics and the Laplace–Beltrami operator", l.2936 "**12.5 Divergence theorem and Green.**"; STATUS coverage Layer 12 remaining names the Riemannian density with its `integralDensity` comparison (12.4) and the divergence theorem with boundary (12.5); Layer 5 remaining "densities on manifolds, integralDensity and Stokes with corners (5.5)"; grep `integralDensity` in Tau Ceti: no hits

## TauCetiRoadmap/FlagVarieties
STATUS.md snapshot: 7ca783d 2026-11-09 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### Layer 2 Standard algebraic parabolics P_J
- Status: NOT-STARTED for general G. The GL_n case is done in Layer 1 (`standardWeight`, weight parabolics; Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/). Abstract Tits-system standard parabolics exist (GroupTheory/TitsSystem/Parabolic/).
- Ready now: no: STATUS says "blocked on ReductiveGroups 7/7b" (needs the Tits system on G(k), B W_J B and the scheme bridge).
- Serves defs: 79
- Evidence: README l.135 "## Layer 2: standard algebraic parabolics and the BN-pair bridge"; STATUS Layer 2 "untouched", "remaining: standard parabolics P_J and their order classification; blocked on ReductiveGroups 7/7b".

## TauCetiRoadmap/NoncommutativeIntegration
STATUS.md snapshot: 2cc438a 2026-11-11 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### §1.5 Finite-trace inclusions; Lp(B(H),Tr) = S_p
- Status: NOT-STARTED (no generalized singular numbers / τ-measurable operators). Supporting: approximation numbers (TauCeti/Analysis/OperatorIdeal/ApproximationNumber/), operator-ideal Schatten families (Analysis/OperatorIdeal/Family*), finite-dimensional Schatten seminorm (Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Schatten.lean).
- Ready now: no: needs §1.1, §1.3, §1.4 (not started) and VonNeumannAlgebras V10.Affiliation/V10.TracialLp (Layer 10 untouched).
- Serves defs: 46 (weak link)
- Evidence: README l.360 "### 1.5 Finite-trace inclusions and the commutative and Schatten identifications", *Needs* "§1.1, §1.3, §1.4; OperatorTheory/OperatorIdeals Parts A–B"; grep `generalizedSingularNumber|tauMeasurable` empty.

## TauCetiRoadmap/PerfectoidSpaces
STATUS.md snapshot: none (no STATUS.md in this roadmap; Tau Ceti checked at a6027b1d24, 2026-11-11)

### P4.15.2 universal prisms and perfection; P4.15.3 the affine Hodge–Tate input (Čech–Alexander Δ_{C/B})
- Status: NOT-STARTED. Grep for `DeltaRing|δ-ring|Prism` (ring sense) in TauCeti finds nothing. The only "prism" hits are simplicial/cubical topology.
- Ready now: no for the sections as written. P4.15.2 needs P4.15.1, which needs DerivedModuleAlgebra §§0.1–0.4, 0.14 and 1.1–1.9 (largely unstarted), plus P1.16–P1.18, P1.24 and P0.19 cotangent. P4.15.3 additionally needs P0.19's full cotangent complex. The bare δ-ring/distinguished-element/prism definitions and rigidity have no derived prerequisites beyond the derived (p,J)-completeness predicate (which exists) and could start now as a substep.
- Serves defs: 81
- Evidence: README l.11053 "#### P4.15.2 universal prisms and perfection" (*semiperfectoid-universal-prism*); l.11090 "#### P4.15.3 the affine Hodge–Tate input" (*semiperfectoid-affine-hodge-tate*, which states "No global prismatic-cohomology output is required"). l.10959 "#### P4.15.1 derived completion and complete flat descent" is the prerequisite.

## TauCetiRoadmap/SpinGeometry
STATUS.md snapshot: 4b48b03 2026-11-10 (describes Tau Ceti to 7ca783d; Tau Ceti checked at a6027b1d24, 2026-11-11)

### G4.2 Principal spin lifts
- Status: NOT-STARTED (G4.1a–b frame adapters done; no `SpinStructure` in Tau Ceti). The carriers the section names exist: `TauCeti.PrincipalBundle` with `PrincipalBundle.pullback` (Topology/FiberBundle/Principal/Basic.lean, Geometry/Manifold/FiberBundle/Pullback.lean), cocycle gluing `TauCeti.fiberBundleCoreOfGroupCocycle` (Geometry/Manifold/FiberBundle/GroupCocycle.lean), `TauCeti.OrthonormalFrameBundle` with `toOrientationCover` (Topology/VectorBundle/Orientation/OrthonormalFrame.lean), the structure group `CliffordAlgebra.realCliffordSpinGroupZero` (LinearAlgebra/CliffordAlgebra/Spin/Real/Basic.lean).
- Ready now: no as specified: needs TopologicalKTheory T6.4's numerable principal-bundle category and CharacteristicClasses C1.0's oriented frames and metric-change transport (neither in code). The `SpinStructure` structure for n ≥ 1 (a `PrincipalBundle` for `realCliffordSpinGroupZero n` with an equivariant map to `OrthonormalFrameBundle`) uses only existing carriers and could be stated now. G4 has no Spin^c content; it is only the Spin analogue for def 64.
- Serves defs: 64
- Evidence: README l.1461 "## Layer 4: Spin lifts, obstruction and classification", l.1585 "### 4.2 Principal spin lifts (G4.2)" ("A spin structure on an oriented metric V of rank n is a numerable principal Spin(n)-bundle P with an equivariant map P→Fr⁺_SO(V)"), *Needs* l.1652; STATUS "The topological and smooth frame adapters of G4.1 are done ... there are no Clifford bundles (G3), spin structures (G4.2–G4.4)"; grep `SpinStructure` empty.

## TauCetiRoadmap/StableReduction
STATUS.md snapshot: a67a650 2026-11-06 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### Layer 10 PrestableMap, IsStableMap, openness
- Status: PARTIAL: `PrestableMap`, isomorphisms/category, automorphisms with `infinitesimalAut`, contracted components with the closed-point, dimension and field-extension characterizations (TauCeti/AlgebraicGeometry/Curves/StableMaps/{Basic,Category,Automorphism,Contracted}.lean). Missing: `IsStableMap`, base-change invariance, openness for projective targets, the finite-automorphism and ampleness characterizations, and the constant-map/source-stability theorem.
- Ready now: yes for `IsStableMap` (needs the Layer 3 pointed-prestable core, which exists, plus a normalization genus of components; no `normalizationGenus` is in Tau Ceti yet, so build it from Normalization/ and `Scheme.genus`). Openness and the ampleness criterion need Layer 2's openness of ampleness (remaining).
- Serves defs: 24
- Evidence: README l.732 "### Layer 10: stable maps and their stability condition"; STATUS l.32 "Layer 10 has prestable maps, automorphisms and contracted components, but no `IsStableMap`"; grep `IsStableMap` empty.

### Layer 11 stable-map API and map-aware stabilization
- Status: PARTIAL: evaluation maps and polarization degree (StableMaps/Degree.lean); decorated dual graphs, clutching, contraction, cutting, forgetting, stabilization files exist in StableMaps/DualGraph/. STATUS remaining: "additivity and local constancy of degree, single-marking contraction, gluing of stable maps, map-aware stabilization in families".
- Ready now: no: needs Layer 10 `IsStableMap`, Layer 2 polarized descent and contraction descent, and Layer 3 single-marking contraction (all remaining)
- Serves defs: 24
- Evidence: README l.778 "### Layer 11: basic stable-map API and map-aware stabilization"; STATUS l.32 "Layer 11 has evaluation maps, the polarization degree of a map over a field, and decorated dual graphs".

## TauCetiRoadmap/SymplecticGeometry/CotangentLagrangian
STATUS.md snapshot: 5fc1aa8 2026-11-10 (umbrella SymplecticGeometry/STATUS.md; Tau Ceti checked at a6027b1d24, 2026-11-11)

### C3.1 Discrete action, iterates and convex billiards
- Status: NOT-STARTED (no `billiard`, `exists_billiard_periodic_reflection` or `exists_equiv_periodic_of_generating` in code).
- Ready now: yes: consumes C3's generating relations, which exist (TauCeti/Geometry/Symplectic/Cotangent/GeneratingFunction/{Correspondence,Composition,MixedHessian,Family,...}.lean), plus Mathlib `AddCircle` measure and recurrence; the perimeter-maximiser existence theorem needs no billiard map.
- Serves defs: 92
- Evidence: CotangentLagrangian/README l.471 "### C3.1. Discrete action, iterates and convex billiards", l.727 "C3.1 consumes C3's generating relations, Mathlib's `AddCircle` measure ... it consumes nothing from the later roadmaps"; STATUS "C3 is partial: generating functions give canonical transformations".

## TauCetiRoadmap/TaubesGromov
STATUS.md snapshot: 3b24211 2026-11-09 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### TG1 Embedded normal operators and application regularity
- Status: NOT-STARTED (only the local normal linearization of HF, Geometry/Symplectic/JHolomorphic/Normal/Linearization.lean).
- Ready now: no: needs PH6.2–6.3 realizations, HF F1.4 determinant orientation, GT tube, HF/M simple-curve transversality (F2.4/F2.6d).
- Serves defs: 60
- Evidence: README l.40 "## TG1. Embedded normal operators and application regularity"; STATUS prose "TG1, TG6.1, TG6.3, TG7–TG9, TG10.1, TG10.3, TG11.3 and TG11.4 are untouched", frontier "This needs TG1's embedded normal operator".

## TauCetiRoadmap/VonNeumannAlgebras
STATUS.md snapshot: 5be5068 2026-11-11 (Tau Ceti checked at a6027b1d24, 2026-11-11)

### Layer 13 (V13b) injective = hyperfinite
- Status: NOT-STARTED.
- Ready now: no: needs V13a and V11 standard form, V12 ultrapowers, V5/V6 traces; Layers 3–7 and 9–13 are all untouched.
- Serves defs: 36
- Evidence: README l.4633 "## Layer 13: Hyperfiniteness and injective classification", l.4692 "### 13.2 Semidiscreteness, approximation and classification (V13b)"; STATUS `{"id":"Layer 13","state":"untouched"}`; grep `Hyperfinite|Semidiscrete` empty.
