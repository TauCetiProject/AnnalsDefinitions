# Needs roadmap written

Snapshot 2026-11-11 (Tau Ceti `a6027b1d24fc`, Mathlib `1b1ccf4b088b`, roadmaps `5f7befb6`, 437 open roadmap PRs).

Every one of the 100 definitions is in exactly one of four files: [ready-to-write-statements.md](ready-to-write-statements.md), [ready-to-formalize-in-tau-ceti.md](ready-to-formalize-in-tau-ceti.md), [needs-roadmap-review.md](needs-roadmap-review.md), [needs-roadmap-written.md](needs-roadmap-written.md). A definition is placed in the furthest-along file whose condition holds for the definition as Kevin Buzzard's text states it; gaps that matter only for a particular paper are noted on the entry.

**Condition:** neither a merged roadmap nor an open PR names the definition as a target (or the ones that do cover only part of it). Something has to be written: a section of an existing roadmap or PR, or a new roadmap. Either way the unit of work is the theory the definition belongs to, not the definition. The groupings are proposals; each census file's "Library-scale gap" describes the theory in more detail.

Order: among the new roadmaps, classical ergodic theory and Lorentzian geometry and causality unblock the most below them. The ergodic-theory roadmap underlies hyperbolic dynamics and billiards, the Lorentzian one underlies hyperbolic PDE, and the Gibbs/DLR formalism serves both lattice spin systems and dimers.

## Extend an existing roadmap or PR

21 definitions.


### Block theory (extension of PR #1775)

Sources: Navarro, *Characters and Blocks of Finite Groups*, Ch. 3–4.

- **#9 Height zero characters of a block.** PR [#1775](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1775) (blocks, defect groups, Brauer correspondent).  
  Papers: [2024·200(2)·4] Brauer's Height Zero Conjecture; [2025·201(2)·2] The Alperin--McKay and Brauer's height zero conjecture for the prime 2. [census](../census/009.md)

### Coprime action on characters (beside InductionRestriction)

Sources: Isaacs, *Character Theory of Finite Groups*, Ch. 13; Navarro, *Character Theory and the McKay Conjecture*.

The cited paper also needs Deligne–Lusztig theory.

- **#8 Glauberman correspondence.** Code: Clifford theory; Mathlib: Schur–Zassenhaus; coprime action in PR [#1634](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1634) L3.  
  Papers: [2020·192(1)·4] Green functions and Glauberman degree-divisibility. [census](../census/008.md)

### Hochschild theory (DGAInfinity Layer 8 or PR #1493)

Sources: Loday, *Cyclic Homology*, §§1.3, 3.4; Weibel, Ch. 9.

- **#10 Hochschild--Kostant--Rosenberg antisymmetrisation map.** [DGAInfinity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/DGAInfinity/README.md) L8 (Hochschild cochains); homological HKR in PR [#1493](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1493) §1.9.  
  Papers: [2020·191(2)·3] A $k$-linear triangulated category without a model. [census](../census/010.md)

### Spectral sequences: general convergence

Sources: Weibel, Ch. 5; Boardman, *Conditionally convergent spectral sequences*.

- **#6 Convergence of a spectral sequence.** Code: spectral sequence of a filtered complex, convergence for finite filtrations.  
  Papers: [2020·191(3)·4] A geometric version of the circle method. [census](../census/006.md)

### Classical split groups (ReductiveGroups or ChevalleyGroups)

Sources: Knus–Merkurjev–Rost–Tignol, *The Book of Involutions*, §§12–13, 23.

- **#11 Split classical groups $\mathrm{Sp}_{2n}$, $\mathrm{SO}_l$ and general spin groups $\mathrm{GSpin}_l$.** Code: `Sp₂ₘ` pinned group scheme, `SOₙ` of the identity form; GSpin in PR [#1756](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1756) §0.0.  
  Papers: [2024·200(3)·2] Doubling constructions: Global functoriality for non-generic cuspidal representations. [census](../census/011.md)

### Stacks and moduli (SchemeAndStackFoundations)

Sources: Stacks Project, Properties of Algebraic Stacks §11 and Morphisms of Stacks §§28–31; Alper, *Good moduli spaces for Artin stacks*; Nobile, *Some properties of the Nash blowing-up*; Cox–Little–Schenck, *Toric Varieties*.

Residual gerbes after §1.20; cohomologically affine morphisms and good moduli spaces after §§1.22–1.23; Nash blowups beside §4.11. #26's paper also needs algebraic toric varieties.

- **#17 Cohomologically affine morphisms of algebraic stacks.** [SchemeAndStackFoundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/SchemeAndStackFoundations/README.md) §1.22 (`QCoh.pushforward`), §1.23.  
  Papers: [2020·191(3)·1] A Luna étale slice theorem for algebraic stacks. [census](../census/017.md)
- **#29 Residual gerbe at a point of an algebraic stack.** [SchemeAndStackFoundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/SchemeAndStackFoundations/README.md) §§1.18–1.22 (stacks, BG, QCoh).  
  Papers: [2020·191(3)·1] A Luna étale slice theorem for algebraic stacks. [census](../census/029.md)
- **#25 Nash blowup of a variety.** Code: `Scheme.relativeDifferentials`, `Module.Grassmannian.scheme`; [SchemeAndStackFoundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/SchemeAndStackFoundations/README.md) §4.14 (coherent Grassmannian).  
  Papers: [2026·203(2)·7] Nash blowup fails to resolve singularities in dimensions four and higher. [census](../census/025.md)
- **#26 Normalized Nash blowup.** = #25 then Mathlib `Scheme.Hom.normalization`.  
  Papers: [2026·203(2)·7] Nash blowup fails to resolve singularities in dimensions four and higher. [census](../census/026.md)

### Rigid étale cohomology (section of PR #875)

Sources: Huber, *Étale Cohomology of Rigid Analytic Varieties and Adic Spaces*, §§2.6, 3.1.

- **#22 Galois action on the étale cohomology of the geometric fibre.** Scheme case [EtaleCohomologyFoundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/EtaleCohomologyFoundations/README.md) §F.4.6; rigid étale cohomology PR [#875](https://github.com/TauCetiProject/TauCetiRoadmap/pull/875).  
  Papers: [2025·201(3)·2] Mod-$p$ Poincaré Duality in $p$-adic analytic geometry. [census](../census/022.md)

### Operator algebras (CStarAlgebras; beside OperatorIdeals)

Sources: Brown–Ozawa, *C\*-Algebras and Finite-Dimensional Approximations*, Ch. 6; Pisier, *Similarity Problems and Completely Bounded Maps*, Ch. 5.

- **#36 Amenable trace on a C\*-algebra.** [CStarAlgebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/CStarAlgebras/README.md) C4.1, C6, C7.1, C8.3 (c.p.c. maps, nuclearity, quasidiagonality).  
  Papers: [2020·192(2)·1] Subalgebras of simple AF-algebras. [census](../census/036.md)
- **#46 Schur multiplier on Schatten classes.** Code: Schatten classes; [CStarAlgebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/CStarAlgebras/README.md) C3.2 (completely bounded maps).  
  Papers: [2023·198(3)·5] Schur multipliers in Schatten-von Neumann classes. [census](../census/046.md)

### Riemannian geometry: boundaries, non-compact L² analysis, singular minimal hypersurfaces; varifolds (RiemannianGeometry, GeometricCurrents)

Sources: Simon, *Introduction to Geometric Measure Theory*; Grigor'yan, *Heat Kernel and Analysis on Manifolds*, Ch. 11; Paternain–Salo–Uhlmann, *Geometric Inverse Problems*, Ch. 3.

- **#40 The Laplace–Beltrami operator on $L^2$ of a complete Riemannian manifold.** Code: `laplaceBeltrami`; closed case [ComplexKahlerGeometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/ComplexKahlerGeometry/README.md) K5a, [PseudodifferentialOperators](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/PseudodifferentialOperators/README.md) P7; Friedrichs extension PR [#1027](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1027).  
  Papers: [2023·198(2)·6] Near optimal spectral gaps for hyperbolic surfaces. [census](../census/040.md)
- **#53 Stationary varifold.** [GeometricCurrents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/GeometricCurrents/README.md) G6 (varifolds induced by currents).  
  Papers: [2023·197(3)·4] Stable minimal hypersurfaces in ℝ^N+1+ℓ with singular set an arbitrary closed K⊂{0}×ℝ^ℓ; [2023·198(3)·2] Regularity of minimal surfaces near quadratic cones. [census](../census/053.md)
- **#65 Strict stability of a minimal cone/hypersurface (Simon's inequality).** [RiemannianGeometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/RiemannianGeometry/README.md) R5a.2, R5b.  
  Papers: [2023·197(3)·4] Stable minimal hypersurfaces in ℝ^N+1+ℓ with singular set an arbitrary closed K⊂{0}×ℝ^ℓ. [census](../census/065.md)
- **#66 Strictly convex boundary of a Riemannian manifold.** [RiemannianGeometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/RiemannianGeometry/README.md) R5a (applied to ∂M).  
  Papers: [2021·194(1)·1] Local and global boundary rigidity and the geodesic X-ray transform in the normal gauge. [census](../census/066.md)

### Pseudoholomorphic curves (PseudoholomorphicCurveAnalysis, TaubesGromov)

Sources: McDuff–Salamon, *J-holomorphic Curves and Symplectic Topology*, Ch. 3; Wendl, *Lectures on Holomorphic Curves*, §3.4.

[HeegaardFloer](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/HeegaardFloer/README.md) F2.4/F2.6d and [PseudoholomorphicCurveAnalysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/PseudoholomorphicCurveAnalysis/README.md) PH6–PH7 use #56 implicitly.

- **#56 Linearized Cauchy–Riemann operator at a J-holomorphic curve.** [HeegaardFloer](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/HeegaardFloer/README.md) F2.4/F2.6d, [PseudoholomorphicCurveAnalysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/PseudoholomorphicCurveAnalysis/README.md) PH6–PH7 (implicit).  
  Papers: [2023·198(1)·2] Transversality and super-rigidity for multiply covered holomorphic curves. [census](../census/056.md)
- **#60 Normal Cauchy–Riemann operator of a J-holomorphic curve.** [TaubesGromov](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/TaubesGromov/README.md) TG1, [HeegaardFloer](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/HeegaardFloer/README.md) F2.6e (embedded case).  
  Papers: [2023·198(1)·2] Transversality and super-rigidity for multiply covered holomorphic curves. [census](../census/060.md)

### Mapping class groups (after PR #1231)

Sources: Farb–Margalit, *A Primer on Mapping Class Groups*.

Needs #59 and #61, both in open PRs.

- **#58 MCG-finite representation of a surface group.** PR [#1231](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1231) §5.9 (Mod(S) action on representations).  
  Papers: [2024·199(2)·6] Canonical representations of surface groups. [census](../census/058.md)

### Borel reducibility of countable structures (sequel to BorelEquivalenceRelations and PR #1316)

Sources: Gao, *Invariant Descriptive Set Theory*, Ch. 13; Becker–Kechris, *The Descriptive Set Theory of Polish Group Actions*.

Needs #98.

- **#94 Borel complete class of countable structures.** Code: `Setoid.BorelReducible`, `RelationalConfiguration`, `isoSetoid`; PR [#1316](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1316).  
  Papers: [2024·199(3)·4] Torsion-free abelian groups are Borel complete. [census](../census/094.md)

### Unbounded operators (amend PR #1027)

Sources: Reed–Simon, *Methods of Modern Mathematical Physics* II, §X.2; Kato, *Perturbation Theory for Linear Operators*, §V.4.

PR [#1027](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1027) UO-E06 specifies −Δ + V on L²(ℝ³); the definition is for all d.

- **#45 Schrödinger operator $-\Delta+V$ on $L^2(\mathbb{R}^d)$.** PR [#1027](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1027) UO-E06 (d = 3); Kato–Rellich in code.  
  Papers: [2026·203(2)·1] Bethe–Sommerfeld Conjecture and absolutely continuous spectrum of multi-dimensional quasi-periodic Schrödinger operators. [census](../census/045.md)

## New roadmaps

19 definitions.


### Lorentzian geometry and causality

Sources: O'Neill, *Semi-Riemannian Geometry*; Beem–Ehrlich–Easley, *Global Lorentzian Geometry*; Hawking–Ellis. Neighbours: RiemannianGeometry, Completed/HopfRinow.

- **#50 Lorentzian manifold, time orientation and spacetime.** Code: `ContMDiffNondegenerateMetric` and its Levi-Civita connection ([Completed/HopfRinow](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/Completed/HopfRinow/README.md) L1).  
  Papers: [2023·198(1)·3] Naked singularities for the Einstein vacuum equations: The exterior solution; [2025·201(3)·3] Naked singularity censoring with anisotropic apparent horizon; [2025·202(2)·1] The interior of dynamical vacuum black holes I: The $C^0$-stability of the Kerr Cauchy horizon; [2025·202(2)·2] On the stability of multi-dimensional rarefaction waves I: the energy estimates; [2025·202(2)·3] On the stability of multi-dimensional rarefaction waves II: existence of solutions and applications to the Riemann problem. [census](../census/050.md)
- **#51 Null (characteristic) hypersurface of a Lorentzian manifold.** [Completed/HopfRinow](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/Completed/HopfRinow/README.md) L1 (metric, connection); needs #50.  
  Papers: [2025·202(2)·2] On the stability of multi-dimensional rarefaction waves I: the energy estimates; [2025·202(2)·3] On the stability of multi-dimensional rarefaction waves II: existence of solutions and applications to the Riemann problem. [census](../census/051.md)

### Hyperbolic PDE: energy methods, symmetric hyperbolic systems, domains of dependence

Sources: Taylor, *PDE III*, Ch. 16; Majda, *Compressible Fluid Flow and Systems of Conservation Laws*; Bär–Ginoux–Pfäffle, *Wave Equations on Lorentzian Manifolds*. Neighbours: PDE, LocalVariationalFieldTheory.

Needs #50, #51.

- **#33 Domain of dependence and development of initial data for the compressible Euler equations.**  
  Papers: [2025·202(2)·2] On the stability of multi-dimensional rarefaction waves I: the energy estimates; [2025·202(2)·3] On the stability of multi-dimensional rarefaction waves II: existence of solutions and applications to the Riemann problem. [census](../census/033.md)

### Pluripotential theory, complex Monge–Ampère and Hessian equations

Sources: Guedj–Zeriahi, *Degenerate Complex Monge–Ampère Equations*; Székelyhidi, *An Introduction to Extremal Kähler Metrics*. Neighbour: ComplexKahlerGeometry.

- **#38 Fully nonlinear complex Hessian-type equations on a compact Hermitian manifold.** [ComplexKahlerGeometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/ComplexKahlerGeometry/README.md) K1/K2/K5b/K6 (Hermitian and Kähler calculus).  
  Papers: [2023·198(1)·4] On $L^\infty$ estimates for complex Monge-Ampère equations. [census](../census/038.md)

### Complex hyperbolic geometry and ball quotients

Sources: Goldman, *Complex Hyperbolic Geometry*; Mok, on projective algebraicity of ball quotients; Borel–Ji. Builds on PR [#2229](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2229) (RealSemisimpleLieGroups), which specifies `SU(n,1)/S(U(n)×U(1))` as a Riemannian symmetric space, its totally geodesic submanifolds and its quotients by discrete subgroups.

PR [#933](https://github.com/TauCetiProject/TauCetiRoadmap/pull/933) §2.7 specifies arithmetic ball quotients.

- **#15 Ball quotients as quasi-projective varieties.** PR [#933](https://github.com/TauCetiProject/TauCetiRoadmap/pull/933) §2.7 (arithmetic quotients); analytification PR [#848](https://github.com/TauCetiProject/TauCetiRoadmap/pull/848); Hermitian domains PR [#1038](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1038).  
  Papers: [2023·197(1)·3] Special subvarieties of non-arithmetic ball quotients and Hodge theory. [census](../census/015.md)
- **#31 Totally geodesic subvariety of a ball quotient.** [RiemannianGeometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/RiemannianGeometry/README.md) R5a (total geodesicity).  
  Papers: [2023·197(1)·3] Special subvarieties of non-arithmetic ball quotients and Hodge theory. [census](../census/031.md)

### Canonical systems and nonlinear Fourier analysis

Sources: Remling, *Spectral Theory of Canonical Systems*; de Branges, *Hilbert Spaces of Entire Functions*; Garnett, *Bounded Analytic Functions*. Neighbour: OperatorTheory.

- **#43 SU(1,1) non-linear Fourier transform of an $L^2$ function on the half-line.**  
  Papers: [2024·199(2)·4] Pointwise convergence of the non-linear Fourier transform. [census](../census/043.md)
- **#44 Scattering functions of a real Dirac system.**  
  Papers: [2024·199(2)·4] Pointwise convergence of the non-linear Fourier transform. [census](../census/044.md)

### Classical ergodic theory: entropy, variational principle, mixing for flows

Sources: Walters, *An Introduction to Ergodic Theory*; Downarowicz, *Entropy in Dynamical Systems*; Cornfeld–Fomin–Sinai. Builds on Mathlib's ergodic theory and `Dynamics.coverEntropy`.

KS entropy is specified in PRs [#851](https://github.com/TauCetiProject/TauCetiRoadmap/pull/851) and [#1335](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1335).

- **#93 Billiard flow in a polygon.**  
  Papers: [2026·203(3)·1] Weakly mixing polygonal billiards. [census](../census/093.md)
- **#96 Equilibrium state (measure) of a Hölder potential.** KS entropy in PRs [#851](https://github.com/TauCetiProject/TauCetiRoadmap/pull/851) §4.2, [#1335](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1335); Mathlib `Dynamics.coverEntropy`.  
  Papers: [2023·197(1)·2] Smooth mixing Anosov flows in dimension three are exponentially mixing. [census](../census/096.md)
- **#97 Measure of maximal entropy.** KS entropy in PRs [#851](https://github.com/TauCetiProject/TauCetiRoadmap/pull/851) §4.2, [#1335](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1335); Mathlib `Dynamics.coverEntropy`.  
  Papers: [2022·195(2)·2] Measures of maximal entropy for surface diffeomorphisms. [census](../census/097.md)

### Uniformly hyperbolic dynamics and thermodynamic formalism

Sources: Katok–Hasselblatt, *Introduction to the Modern Theory of Dynamical Systems*; Fisher–Hasselblatt, *Hyperbolic Flows*; Bowen, *Equilibrium States*. Builds on the ergodic-theory roadmap.

- **#91 Anosov flow.** Code: `flowOf`, continuous distributions, Riemannian metrics.  
  Papers: [2023·197(1)·2] Smooth mixing Anosov flows in dimension three are exponentially mixing. [census](../census/091.md)

### Billiards and kinetic limits

Sources: Tabachnikov, *Geometry and Billiards*; Chernov–Markarian, *Chaotic Billiards*; Gallagher–Saint-Raymond–Texier, *From Newton to Boltzmann*. Builds on the ergodic-theory roadmap.

- **#39 Hard sphere dynamics on the torus.**  
  Papers: [2023·198(3)·3] Statistical dynamics of a hard sphere gas: fluctuating Boltzmann equation and large deviations. [census](../census/039.md)

### Classical statistical mechanics: Gibbs measures, lattice spin systems, dimers

Sources: Georgii, *Gibbs Measures and Phase Transitions*; Friedli–Velenik, *Statistical Mechanics of Lattice Systems*; Gorin, *Lectures on Random Lozenge Tilings*. Neighbour: RandomMatrices.

- **#99 Scaling limit of lattice $\phi^4$ fields (reachable random field).** Ingredients in Mathlib (product measures, densities, convergence in distribution).  
  Papers: [2021·194(1)·3] Marginal triviality of the scaling limits of critical 4D Ising and $\lambda\phi_4^4$ models. [census](../census/099.md)
- **#100 Translation-invariant ergodic Gibbs measure on lozenge tilings of given slope.** Ingredients in Mathlib (perfect matchings, conditional expectation, ergodicity).  
  Papers: [2023·198(3)·1] Universality for lozenge tiling local statistics. [census](../census/100.md)

### Weighted and Gaussian isoperimetry

Sources: Maggi, *Sets of Finite Perimeter and Geometric Variational Problems*; Bakry–Gentil–Ledoux. Neighbours: Isoperimetry, GeometricMeasureTheory.

- **#55 Gaussian $q$-cluster.** [GeometricMeasureTheory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/GeometricMeasureTheory/README.md) G5 (Euclidean perimeter); Mathlib `stdGaussian`.  
  Papers: [2022·195(1)·2] The Gaussian Double-Bubble and Multi-Bubble Conjectures. [census](../census/055.md)

### Filling invariants

Sources: Gromov, *Filling Riemannian Manifolds*; Bridson, *The Geometry of the Word Problem*. Neighbour: GeometricCurrents.

- **#57 Lipschitz singular chains and their mass.** [GeometricCurrents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/GeometricCurrents/README.md) G1–G3; [GeometricMeasureTheory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/GeometricMeasureTheory/README.md) G2.  
  Papers: [2021·193(3)·2] Filling functions of arithmetic groups. [census](../census/057.md)

### Surface group representations and character varieties

Sources: Goldman, *The Symplectic Nature of Fundamental Groups of Surfaces*; Labourie, *Lectures on Representations of Surface Groups*; Simpson, *Higgs Bundles and Local Systems*.

Cartan involutions and maximal compact subgroups of real reductive groups are in PR [#2229](https://github.com/TauCetiProject/TauCetiRoadmap/pull/2229) Layer 0, §2.2 and §5.4.

- **#54 Character variety of a surface group in a real reductive group.** [LieGroups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/main/TauCetiRoadmap/RepresentationTheory/LieGroups/README.md) L7, L9; PR [#1169](https://github.com/TauCetiProject/TauCetiRoadmap/pull/1169) (PSL₂(ℝ)).  
  Papers: [2024·200(3)·1] A general Cayley correspondence and higher rank Teichmüller spaces. [census](../census/054.md)

### Degree growth of rational maps

Sources: Lazarsfeld, *Positivity in Algebraic Geometry I*, Ch. 1–2; Dinh–Sibony; Guedj's survey on ergodic properties of rational maps.

Numerical classes and intersection numbers are in PR [#545](https://github.com/TauCetiProject/TauCetiRoadmap/pull/545).

- **#95 Dynamical degree of a dominant rational self-map.** PR [#545](https://github.com/TauCetiProject/TauCetiRoadmap/pull/545) (N¹, nef classes, intersection numbers); Mathlib rational maps.  
  Papers: [2021·194(1)·5] Spectral interpretations of dynamical degrees and applications. [census](../census/095.md)

## Beyond the 100

The cited papers also need theory that is not among the 100 definitions and that no roadmap plans: Deligne–Lusztig theory of finite reductive groups (for #2's and #8's papers; Digne–Michel, *Representations of Finite Groups of Lie Type*), algebraic toric varieties (#26), Margulis superrigidity (#68), Sen theory and locally analytic vectors (#77), and torus and cosection localization of virtual classes (#27). The census files record these under "Library-scale gap".
