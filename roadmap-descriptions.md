# Roadmap descriptions

A title and a short description for each roadmap and roadmap PR that the census cites. [roadmaps.md](roadmaps.md) is generated from this file and the census by [scripts/build_roadmaps.py](scripts/build_roadmaps.py); see [AGENTS.md](AGENTS.md#updating-the-repository).

The format is Markdown with one `##` heading per roadmap: it reads on GitHub, an edit to one description is a one-line diff, and the script parses it with the Python standard library alone. An entry has:

- the heading: the roadmap's folder as the census links it, without the leading `TauCetiRoadmap/`. For a roadmap that the census cites only by its PR, it is the folder the PR adds.
- `Title:` the roadmap's title in plain words.
- `PR: #N`, for a roadmap that the census cites by its PR: the pull request that adds the folder.
- one paragraph, on one line, of two or three sentences saying what the roadmap builds and its main results.

An entry headed `## #N` describes a cited pull request that adds no roadmap folder of its own, such as a revision of a merged roadmap.

The descriptions are written from each roadmap's README for a mathematician who does not know the project: no Lean identifiers, no section numbers, and nothing the README does not say. This file does not record whether a roadmap is merged: [roadmaps.md](roadmaps.md) lists a roadmap as merged when the census links its folder on TauCetiRoadmap `main`, and as an open PR otherwise.

## AbelianSchemesAndArithmeticModuli
Title: Abelian schemes and arithmetic moduli (the Jacobian challenge, part II)

Develops abelian schemes over an arbitrary base: rigidity and the theorem of the cube in families, the dual abelian scheme, polarizations, isogenies and Weil pairings, Tate modules with the de Rham and crystalline realizations, and the deformation theorems of Serre–Tate and Grothendieck–Messing. Over the complex numbers it gives the lattice uniformization, Riemann forms, the Appell–Humbert theorem and the equivalence between polarized abelian varieties and polarized Hodge structures of weight one. Over a field it proves the basic arithmetic of homomorphisms, including finiteness of Hom and positivity of the Rosati involution.

## AbelianSchemesAndArithmeticModuliPartII
Title: Abelian schemes and arithmetic moduli, part II
PR: #1405

Develops three strands of the theory of abelian varieties: completed Poincaré bundles with their universal connections, Betti maps of families of complex abelian varieties, and integral realizations of abelian varieties over finite fields. Main results include the cohomology of the completed Poincaré sheaf and ordinary CM trivializations, criteria for maximal Betti rank with applications to fibre powers of families of curves, the Honda–Tate classification, and counts of isogeny and isomorphism classes of abelian varieties over finite fields.

## AbelianSurfacesModularity
Title: Modularity of abelian surfaces
PR: #1746

Develops the 2–3 switch for abelian surfaces over ℚ: permitted mod-3 symplectic images, ordinary local points at 2 and 3 on moduli of marked genus-two curves, and residual automorphy of mod-2 representations with image A₅ or S₅. With ordinary modularity lifting for GSp₄ as input, it proves modularity of abelian surfaces and genus-two curves over ℚ with good ordinary reduction at 3, a permitted mod-3 image and conditions at 2, hence entire L-functions with a functional equation, a positive density of modular genus-two equations, and residual modularity modulo 2.

## AbelianVarietiesOverFiniteFields
Title: Abelian varieties over finite fields

Develops the invariants of an abelian variety over a finite field that are determined by the characteristic polynomial of its Frobenius: point counts, simple factors, twists, the endomorphism field, the p-rank and Newton polygon, and the group of rational points. Main results include Waterhouse's list of elliptic isogeny classes, invariants of Frobenius orders, Deligne's equivalence for ordinary abelian varieties, the Centeleghe–Stix equivalence over prime fields with the resulting count of isomorphism classes, and the Howe–Nart–Ritzenthaler criterion for Jacobians in isogeny classes of abelian surfaces.

## AbundanceStatement
Title: Stating abundance for projective klt varieties
PR: #545

Develops the divisor, positivity and singularity theory needed to state the abundance conjecture: for a normal projective variety with klt singularities over an algebraically closed field of characteristic zero, a nef canonical divisor is semiample. It builds ℚ-Cartier divisors on normal varieties, the canonical divisor from differentials, discrepancies and klt singularities, the cone of curves and nefness, ampleness with Kleiman's criterion, and semiampleness, and formulates the conjecture as a precise statement without proving it.

## AdelicAlgebraicGroups
Title: Adelic algebraic groups and arithmetic quotients

Develops the adelic points of affine algebraic groups over number fields: their topology, Haar and Tamagawa measures, arithmetic quotients, reduction theory, strong approximation and changes of level. Main results include finiteness of class numbers, finite volume and compactness criteria for the adelic quotient, and the theorem that S-arithmetic subgroups of connected reductive groups without rational characters are lattices; arithmetic lattices in real Lie groups are defined here.

## AInfCohomology
Title: Integral A_inf cohomology and Breuil–Kisin–Fargues structures

Constructs the integral p-adic cohomology of Bhatt, Morrow and Scholze for smooth and semistable formal schemes over the ring of integers of a complete algebraically closed extension of ℚₚ, together with the décalage operator and Fargues' classification of Breuil–Kisin–Fargues modules. Main results are the comparison of this cohomology for proper smooth or semistable formal schemes with étale, crystalline and de Rham cohomology, the resulting torsion inequalities, the de Rham lattice of a semistable model, and Breuil–Kisin descent over a discretely valued base.

## AlgebraicGromovWittenTheory
Title: Algebraic Gromov–Witten theory and quantum cohomology
PR: #1998

Constructs algebraic Gromov–Witten theory for a smooth projective variety over a field of characteristic zero: the moduli stack of stable maps, its virtual fundamental class, and primary and descendant invariants with the string, dilaton and divisor equations. From the genus-zero invariants it builds small and big quantum cohomology and proves associativity through the WDVV equation.

## AlgebraicModularFormsAndSerreWeights
Title: Algebraic modular forms and Serre weights

Builds modular forms as sections of line bundles on modular curves in every integer weight, with integral q-expansions, the Hasse invariant and theta operator in characteristic p, the Serre weight of a local Galois representation, and the Deligne–Serre lifting of eigenvalues. It attaches Galois representations to classical eigenforms of every weight at least one and formulates residual modularity.

## AlgebraicModuliForArithmeticGeometry
Title: Algebraic moduli and representability for arithmetic geometry

Builds the representability machinery for moduli problems: projective bundles, Grassmannians of quotients of coherent sheaves and flag schemes, Hilbert, Hom and Isom schemes, effective descent, gerbes, rigidification of stacks, and Artin's representability criteria. Main results include Mumford's uniform regularity bound and the boundedness of Hilbert polynomials, the classification of gerbes with abelian band by their class in H², Artin approximation, and nonarchimedean GAGA for proper algebraic spaces.

## AlgebraicModuliForArithmeticGeometryPartII
Title: Algebraic moduli for arithmetic geometry, part II: numerical Picard groups and contraction descent

Develops numerical classes of invertible sheaves and Cartier divisors on proper schemes, over a field and over Noetherian bases, and uses them to descend contractions. It constructs relative numerical groups, cones of curves, nefness and Kleiman's criterion, and the Picard scheme of a proper scheme with its local system of numerical classes. Main results are a positive-power criterion for constancy of numerical classes, descent of geometric contractions and of fibre graphs of surfaces, comparisons over discrete valuation rings, and independence of the Alexeev–Hacon–Kawamata Picard rank from the resolution.

## AmenableTracesOnCStarAlgebras
Title: Amenable traces on C\*-algebras

Develops tracial states on C\*-algebras and their approximation by completely positive contractions into matrix algebras, defining amenable, quasidiagonal and uniform amenable traces. Main results include the Connes–Kirchberg characterisation of amenable traces, the description of uniform amenable traces through injectivity of the associated von Neumann algebra, the cases of nuclear and exact algebras, and the theorem that a discrete group is amenable exactly when its reduced C\*-algebra has an amenable trace.

## AnabelianGeometryAndNonabelianChabauty
Title: Anabelian geometry and nonabelian Chabauty

Builds continuous nonabelian cohomology and path torsors for étale fundamental groups, unipotent fundamental groups with their realizations, and Selmer varieties. Main results include Chabauty–Kim finiteness, the equations of quadratic Chabauty, and reconstruction of hyperbolic curves from their arithmetic fundamental groups; the section conjecture is stated as a conjecture.

## AnalyticStableMaps
Title: Analytic stable maps and their implicit atlases

Constructs the analytic moduli theory of stable pseudoholomorphic maps from nodal curves to a closed symplectic manifold with a tame almost complex structure. It covers the linearized operator and its index, the factorisation of a closed curve through a simple one, transversality for generic almost complex structures, Gromov compactness in every genus, gluing, and implicit atlases on the moduli spaces.

## ArakelovGeometryAndAbelianHeights
Title: Arakelov geometry and heights of abelian varieties

Develops hermitian line bundles over rings of integers with their arithmetic degree and the resulting heights of points, puts the Faltings metric on the Hodge line of an abelian variety, and defines the Faltings height and its stable version over number fields. Main results include the behaviour of the height under isogeny, its comparison with the modular height, and Northcott finiteness for polarized abelian varieties.

## ArakelovGeometryAndAbelianHeightsPartII
Title: Arakelov geometry and abelian heights, part II
PR: #1833

Extends Arakelov theory to adelic line bundles over general bases, as needed for admissible metrics on families of curves. Its main results are nefness of the admissible canonical bundle, its bigness for families of maximal variation, and a comparison between its self-intersection and the stable Faltings height that is uniform over all curves of a given genus at least two over number fields and function fields of one variable.

## ArcTopologyAndDescent
Title: The arc-topology and descent for étale cohomology

Develops the excision theory of the arc-topology from valuation algebra and the scheme arc-site, and proves that a finitary v-sheaf with values in an infinity-category compactly generated by cotruncated objects is an arc-sheaf exactly when it satisfies Milnor excision. Arc-covers are the universal spectral submersions, are stable under cofiltered limits with affine transition maps, and on quasi-compact quasi-separated perfect schemes in characteristic p are exactly the universally effective epimorphisms; the coherent arc-topos gives excision and formal glueing for every arc-sheaf with values in a category with small limits. Applications include étale objects, characteristic-zero differential cohomology, perfect complexes on perfections, completed generic fibres and integral perfectoid hyperdescent, and the end theorem is Artin–Grothendieck vanishing for arbitrary torsion coefficients on affinoid algebras.

## ArithmeticDynamics
Title: Arithmetic dynamics
PR: #1335

Develops the arithmetic of iterated maps, especially rational maps of the projective line: preperiodic points, canonical heights, local escape functions and invariant measures, dynatomic curves, and Galois actions on trees of iterated preimages. Main results include equidistribution of small points and of periodic points, the facts that z² + c over ℚ has at most one rational 3-cycle and no rational 4- or 5-cycles, Stoll's surjective arboreal representations, Ritt's classification of polynomials with equal iterates, uniform common torsion images for Legendre curves, and dynamical Mordell–Lang for étale maps.

## ArithmeticFuchsianGroups
Title: Arithmetic Fuchsian groups, commensurators and isospectral covers
PR: #2026

Develops the arithmetic theory of lattices in PSL₂(ℝ) coming from orders in quaternion algebras over totally real fields split at exactly one real place. Main results are discreteness, finite covolume and the covolume formula for maximal orders, the finiteness theorems of Borel for bounded covolume and of Takeuchi for a given signature, Margulis' criterion that a lattice is arithmetic exactly when its commensurator is dense, and nonisometric isospectral degree-eight covers of every closed hyperbolic surface of genus at least three with nonarithmetic maximal uniformizing group.

## ArithmeticGaloisRepresentations
Title: Arithmetic Galois representations and conductors

Develops continuous representations of absolute Galois groups with their integral models and reductions, their restrictions to decomposition groups with Frobenius polynomials and Weil–Deligne representations, Artin and Swan conductors, and the Tate modules of elliptic curves and abelian varieties. It also provides symmetric and other powers of representations and the conditions on residual images used in automorphy lifting.

## ArithmeticLocallySymmetricSpaces
Title: Arithmetic locally symmetric spaces and their cohomology

Builds the locally symmetric spaces attached to a connected reductive group over a number field and a compact open level, and their cohomology with integral coefficients. It covers the decomposition into arithmetic quotients of the symmetric space, neat levels, local systems, the Borel–Serre compactification, Hecke actions, duality, and the comparison with automorphic forms.

## ArithmeticLocallySymmetricSpacesPartII
Title: Arithmetic locally symmetric spaces, part II: weight multiplicities
PR: #2401

Proves fixed-level bounds in the weight aspect for the cohomology of congruence subgroups of SL₂ over a number field with a complex place, using completed homology and Iwasawa modules. Main results are Fu's local theorem bounding the homology of weight twists of a finitely generated Iwasawa module for products of congruence subgroups of SL₂(ℤₚ), Fu's sharp bound for dimensions of cusp forms of a given weight at fixed level, and two-sided linear bounds in the weight for the first and second cohomology of Bianchi groups.

## AutomorphicCongruences
Title: Automorphic congruences and reverse main-conjecture divisibilities
PR: #1816

Develops Eisenstein congruences on unitary groups that produce Galois extension classes and lower bounds for Selmer groups, with the comparisons of periods and local conditions and the passage to universal deformation families and cyclotomic towers. Main results are the Skinner–Urban divisibilities, the Castella–Liu–Wan and Fouquet–Wan divisibilities, Wan's divisibility for Hilbert families, and the Burungale–Castella–Skinner cyclotomic main conjecture for elliptic curves over ℚ with good ordinary reduction at p > 3, after inverting p and, under an image condition, integrally, each under its own hypotheses.

## AutomorphicFormsOnReductiveGroups
Title: Automorphic forms on reductive groups

Builds the analytic and representation-theoretic setting for automorphic forms on a connected reductive group over a number field: smooth, Schwartz and moderate-growth functions on the adelic group, Harish-Chandra modules of the real group with infinitesimal characters, discrete series and archimedean Langlands parameters, automorphic representations with their local components, and constant terms and cuspidality. It ends with cohomological and coherent representations and with explicit dictionaries for GL₁, GL₂ and GSp₄, including the passage from classical modular forms to adelic ones.

## AutomorphicGaloisRepresentations
Title: Galois representations attached to modular and Hilbert modular forms
PR: #1007

Realises the Galois representations of cuspidal eigenforms of weight at least two in parabolic cohomology and compares them with the motivic construction, constructs those of Hilbert modular forms, and places the Artin representations of weight-one forms in the same normalisation. Results include local compatibility at every place, compatible systems, ordinary and crystalline properties, large-image theorems, and maps from deformation rings to integral Hecke algebras.

## AutomorphicGaloisRepresentationsPartII
Title: Automorphic Galois representations, part II: regular algebraic GLₙ

Constructs the continuous semisimple Galois representations attached to regular algebraic cuspidal representations of GLₙ over CM and totally real fields, through the cohomology of compact unitary Shimura varieties in the polarized case and through boundary cohomology in the non-self-dual case. Main results are local–global compatibility away from the coefficient prime, comparison at the coefficient prime, partly under an irreducibility hypothesis, assembly into compatible systems, and residual properties such as the existence of infinitely many decomposed generic primes.

## AutomorphicLFunctionsAndLocalFactors
Title: Automorphic L-functions and local factors

Develops the analytic theory of L-functions of characters and of automorphic representations of GLₙ: local and adelic Fourier analysis, the Godement–Jacquet and Rankin–Selberg integrals, and the local factors they define. It ends by comparing Satake and Weil–Deligne determinants and by treating rational period structures.

## AutomorphicLFunctionsAndLocalFactorsPartII
Title: Automorphic L-functions and local factors, part II

Develops the doubling method for standard L-functions: classical doubling for unitary groups, with its archimedean sections, and generalised doubling for split symplectic, special orthogonal and general spin groups. Its main results are local functional equations, entireness of the global L-functions after highly ramified twists, and a weak transfer of automorphic representations of these groups to general linear groups.

## AutomorphicPadicLFunctionsPartII
Title: Automorphic p-adic L-functions, part II: critical Hecke values
PR: #1543

Studies the critical values of L-functions of algebraic Hecke characters of a totally imaginary field containing a CM field, through Eisenstein–Kronecker classes on abelian schemes with complex multiplication. Its results are the integrality and algebraicity of these values after division by CM periods, and their p-adic interpolation by measures in the ordinary case.

## AutomorphicSpectralTheory
Title: Automorphic spectral theory and trace distributions

Constructs the spectral decomposition of the space of square-integrable functions on the automorphic quotient of a reductive group over a number field, by Eisenstein series and their residues. Arthur truncation and the Maass–Selberg relations then lead to the coarse, fine and invariant trace formulas, with applications to GLₙ such as solvable base change.

## AutomorphicSpectralTheoryPartII
Title: Automorphic spectral theory and trace distributions, part II

Develops multipliers of the Schwartz algebra of a reductive group over a number field: entire functions of controlled growth give multipliers on the real group, which are combined with spherical Hecke operators at finite places. The main results use such multipliers to isolate prescribed parts of the cuspidal spectrum, with the supporting analysis of weighted function spaces on automorphic quotients.

## BallQuotientsAndComplexHyperbolicLattices
Title: Ball quotients and complex hyperbolic lattices

Studies the complex ball as the symmetric space of PU(1,n) and the lattices in this group, arithmetic or not: cusps, finite generation, Selberg's lemma, and the quotient of the ball as a normal complex space. It constructs the toroidal and minimal compactifications and proves that the minimal compactification is a normal projective variety, so that every ball quotient is quasi-projective, and that the quotient by a torsion-free lattice has a unique algebraic structure; in the arithmetic case it compares with the Baily–Borel compactification. It ends with totally geodesic and special subvarieties.

## BianchiModularForms
Title: Bianchi modular forms
PR: #1719

Builds weight-two Bianchi modular forms for GL₂ over an imaginary quadratic field, both as harmonic cuspidal 1-forms on hyperbolic three-space and as cuspidal group cohomology, proves the Eichler–Shimura–Harder comparison, and develops the arithmetic invariants the LMFDB displays: Hecke operators at all primes, newforms, base change from classical forms, CM forms and their inducing characters.

## BochnerSpaces
Title: Bochner spaces

Develops measurability, Bochner and Pettis integration, Bochner spaces, integral operators and vector measures for functions with values in a Banach space. Main results include the Pettis measurability theorem, Hille's theorem on closed operators and Bochner integrals, Minkowski's integral inequality and Fubini's theorem, the identification of the Bochner space L¹ with a projective tensor product, criteria for Pettis integrability, and the characterization of duality of Bochner spaces by the Radon–Nikodým property.

## BorelEquivalenceRelations
Title: Borel equivalence relations, the G₀ dichotomy and Silver's theorem

Develops the classical descriptive set theory of Borel equivalence relations on Polish and standard Borel spaces by category methods, without forcing or effective descriptive set theory. Its two main results are Silver's theorem, that a Borel equivalence relation has countably many classes or continuum many pairwise inequivalent points forming a Cantor set, and the dichotomy of Kechris, Solecki and Todorcevic, that an analytic graph has a countable Borel colouring or receives a continuous homomorphism from the graph G₀; reusable tools include the perfect set theorem for analytic sets, Borel colourings and the Kuratowski–Ulam theorem.

## CalibratedGeometry
Title: Calibrations, volume minimization and special Lagrangian geometry

Develops calibrated geometry, from the linear algebra of comass and calibrated planes through volume minimization to the Kähler and special Lagrangian calibrations and the deformation theory of compact special Lagrangian submanifolds. Main results are the fundamental theorem of calibrations for compact submanifolds and integral chains, the Wirtinger inequality in every degree with volume minimization of complex submanifolds of Kähler manifolds, minimality of special Lagrangian submanifolds, and McLean's theorem that their deformations form a smooth manifold of dimension equal to the first Betti number.

## CharacteristicClasses
Title: Characteristic classes and Chern–Weil theory

Builds characteristic classes of vector bundles both topologically, from Thom classes and the cohomology of projective bundles, and geometrically, from the curvature of a connection, and proves that the two agree in real cohomology. It constructs the Stiefel–Whitney classes mod 2, the integral Chern, Pontryagin and Euler classes with Thom and Gysin maps, the cohomology of classifying spaces, the Chern character and the Todd, L and Â classes. Main results include the vanishing of the Euler class as the obstruction to a nowhere-zero section, the Euler class of a closed manifold evaluating to its Euler characteristic, Thom's theorem on embedded representatives in codimensions one and two, Whitney's nonimmersion theorem for projective spaces, Borel's theorem on the rational cohomology of classifying spaces and the identification of the second Stiefel–Whitney class with the obstruction to a spin structure.

## ClassicalAdicEtaleCohomology
Title: Classical analytic étale cohomology

Develops the étale cohomology of analytic adic spaces needed to pass from schemes and formal models to analytic spaces, starting from sheaves with supports, henselian comparison, formal specialization and analytic covering spaces. Main results are comparison and invariance theorems for nearby cycles over valuation rings, cohomology with proper supports, normalized traces for smooth morphisms and Poincaré duality, comparison with Berkovich spaces, and computations for discs, annuli, exhaustions of affine space and the boundary of a smooth curve.

## ClassicalAdicEtaleCohomologyPartII
Title: Classical analytic étale cohomology, part II: almost duality and constructible proper base change

Builds integral Faltings traces and local almost Poincaré duality on admissible formal models over the ring of integers of a complete algebraically closed extension of ℚₚ, using almost coherent sheaves, polystable root towers and descent through finite quotients. Main results are Poincaré duality for smooth proper rigid spaces with mod p, p-power torsion, integral and rational coefficients, Zariski-constructible proper pushforward, proper base change for all torsion coefficients, and constancy of the torsion cohomology sheaves of a proper rigid space over smooth rigid bases.

## ClassicalErgodicTheory
Title: Classical ergodic theory, entropy, the variational principle and flows

Builds classical ergodic theory for measure-preserving maps, group actions and flows: factors and joinings, the mixing hierarchy and its spectral characterisations, Kolmogorov–Sinai entropy, topological entropy and pressure, and the variational principle. It defines equilibrium states and measures of maximal entropy, and proves Bowen's uniqueness theorem for expansive systems with specification and the Ruelle–Perron–Frobenius theorem.

## CohomologyComparisons
Title: p-adic cohomology comparisons
PR: #1064

Constructs comparison maps between étale, A_inf, crystalline, de Rham, infinitesimal and Hyodo–Kato cohomology in p-adic geometry, compatible with coefficient maps, Frobenius, Galois actions, filtrations and integral lattices. Main results are the crystalline comparison and lattice recovery of Bhatt–Morrow–Scholze in good reduction, the semistable comparison of Česnavičius–Koshikawa, the semistable comparison C_st of Colmez–Nizioł for proper rigid spaces and the relative filtered comparison of Guo–Reinecke, with applications to Chern classes, torsion bounds and Pan's comparisons on modular curves.

## Completed/HopfRinow
Title: Geodesics, the exponential map, and the Hopf–Rinow theorem

Develops the geodesic theory of Riemannian manifolds: covariant differentiation along curves, the geodesic equation and geodesic flow, the exponential map and its local inverse, normal neighbourhoods, the Gauss lemma and minimizing geodesics. The main result is the Hopf–Rinow theorem: on a connected Riemannian manifold, completeness of the exponential map at a point, compactness of closed bounded sets, metric completeness and geodesic completeness are equivalent, and each implies that any two points are joined by a minimizing geodesic.

## CompletedCohomologyAndLocalGlobalCompatibility
Title: Completed cohomology and p-adic local–global compatibility over ℚ
PR: #1270

Specialises completed cohomology to modular curves and quaternionic Shimura curves over ℚ and studies it as a representation of GL₂(ℚₚ), of the Galois group and of the Hecke algebra. Its main results are Emerton's local–global compatibility with the p-adic local Langlands correspondence, in Banach, mod p and homological forms, with applications to patched modules in modularity lifting.

## CompletedCohomologyPartII
Title: Completed cohomology, homology and arithmetic towers: Part II

Defines completed cohomology and completed homology of a tower of arithmetic locally symmetric spaces: with torsion coefficients one takes the colimit over the levels at p and then the limit over the coefficients. It proves finiteness and admissibility over the Iwasawa algebra, descent to finite level and duality, and compares the result with étale cohomology for the modular, Siegel, unitary and Hilbert towers, with their Galois and Hecke actions.

## ComplexComparisonPartII
Title: Complex comparison, part II: coherent, de Rham–Betti and étale comparison

Compares complex algebraic geometry with complex analytic geometry and topology for coherent, de Rham and étale coefficients. Main results are coherent GAGA for projective and proper schemes and derived GAGA for proper algebraic spaces, Remmert's proper mapping theorem and Chow's theorem, the comparison of algebraic de Rham and singular cohomology with Gauss–Manin connections and Hodge theory, Deligne's Riemann–Hilbert correspondence for regular singular connections, the Riemann existence theorem, and Artin's comparison of étale and singular cohomology with finite and adic coefficients.

## ComplexHessianEquations
Title: Complex Hessian equations

Treats fully nonlinear elliptic equations of complex Hessian type on compact complex manifolds, written through the eigenvalues of a real (1,1)-form relative to a Hermitian metric. It develops spectral functions, Gårding cones and admissible pairs, the comparison principle and uniqueness, and on compact Kähler manifolds Yau's theorem on the complex Monge–Ampère equation and the sharp L∞ estimates of Guo, Phong and Tong.

## ComplexKahlerGeometry
Title: Complex manifolds, Dolbeault theory and Kähler geometry

Develops complex manifolds, Dolbeault theory and Kähler geometry: the Newlander–Nirenberg theorem, the Dolbeault–Grothendieck lemma, the local algebra of holomorphic germs, holomorphic and Hermitian bundles, and elliptic theory on compact Hermitian manifolds with Serre duality. On compact Kähler manifolds it proves the Kähler identities, the Hodge decomposition, hard Lefschetz and the Hodge–Riemann relations.

## ComplexMultiplicationAndExplicitReciprocity
Title: Complex multiplication and explicit reciprocity
PR: #1254

Develops complex multiplication starting from CM types and reflex norms: abelian schemes with complex multiplication and their twists by ideals, polarised CM lattices, the reciprocity law on torsion points, class polynomials and the class fields they generate, and the Hecke characters of CM abelian varieties. It also treats reduction of CM abelian varieties and the isogeny graphs that arise.

## ComplexMultiplicationAndExplicitReciprocityPartII
Title: Complex multiplication and explicit reciprocity, part II
PR: #1695

Extends the theory of complex multiplication to arithmetic heights of CM abelian varieties. It proves the averaged Colmez formula for their Faltings heights by two independent routes, through arithmetic intersection theory on orthogonal Shimura varieties and through isogenies and quaternionic CM points, and deduces subpolynomial bounds for individual CM heights and power-type lower bounds for Galois orbits of CM points in terms of their discriminants. With a height bound for CM lifts this gives finiteness of CM points of bounded degree, while the individual Colmez conjecture is only formulated.

## CompressibleEulerEquations
Title: Compressible Euler equations, symmetric hyperbolic systems and maximal developments
PR: #2442

Develops the classical theory of the compressible Euler equations of a perfect fluid on ℝ × ℝⁿ: the barotropic and full systems, their symmetric hyperbolic form, sound cones and domains of dependence. Main results are local well-posedness in Sobolev spaces for data without vacuum, uniqueness on domains of dependence, and the theory of developments of initial data, including the existence of maximal developments and the fact that their regular boundary is null for the acoustical metric.

## CompressibleEulerEquationsPartII
Title: Compressible Euler equations, part II: acoustical geometry and characteristic data
PR: #3010

Builds the geometry of the acoustical metric of a solution of the compressible Euler equations, whose null cones are the sound cones: acoustical functions whose level sets are sound fronts, acoustical coordinates, and the characteristic boundary of a development, each point of which lies on a null geodesic issuing from the edge of the data. It then treats initial data prescribed partly on a characteristic hypersurface, with their developments, maximal developments, local existence near the edge and the Goursat problem, and shows that the plane-symmetric centered rarefaction wave of a polytropic gas fits this setting.

## CongruenceSpectralGap
Title: The congruence spectral gap

Builds the Laplacian on the quotient of the upper half-plane by a congruence subgroup of SL₂(ℤ), with its spectral decomposition, and proves the lower bound 21/100 for the bottom of its positive spectrum. The proof goes through the Luo–Rudnick–Sarnak bound for unitary cuspidal representations of GLₘ over ℚ with spherical archimedean component.

## ConstructiveFieldTheoryPhi4
Title: Constructive scalar field theory on the lattice: φ⁴, Ising and their scaling limits
PR: #2432

Builds the lattice side of Euclidean scalar field theory: single-site measures of φ⁴ and Ising type, finite-volume Gibbs measures, the Griffiths–Simon class and the classical correlation inequalities. It constructs the infinite-volume state, proves reflection positivity and the infrared bound, and defines the random fields reachable as scaling limits of lattice systems, showing that the Gaussian free field is one of them.

## CountableStructureSpaces
Title: Spaces of countable structures and the López–Escobar theorem

Builds the Polish space of structures of a countable relational language with universe ℕ, the action of the infinite symmetric group by relabelling, and the basic invariant descriptive set theory of this space. Its main result is the López–Escobar theorem: a class of countable structures is Borel and isomorphism-invariant exactly when it is the class of models of a sentence of the infinitary logic Lω₁ω. It also proves that every isomorphism class is Borel and that the class of well-orders is not.

## CountableStructureSpacesPartII
Title: Countable structure spaces, Part II: Borel reducibility of isomorphism relations and Borel completeness
PR: #2418

Compares the isomorphism relations of classes of countable structures by Borel reducibility and defines Borel completeness, also for languages with function symbols. It proves the Friedman–Stanley theorem that countable graphs, trees and linear orders are Borel complete, the Becker–Kechris universality theorem for actions of the infinite symmetric group, and that a Borel complete isomorphism relation is not Borel.

## CrystallineCohomologyPartII
Title: Crystalline cohomology, de Rham–Witt complexes and logarithmic structures, Part II: Witt vector cohomology of singular varieties

Develops Witt vector cohomology of varieties in characteristic p, including singular ones: rational and Frobenius-inverted Witt vector cohomology, h-descent, compact supports, Hodge–Witt cohomology with supports and the action of correspondences, and Witt-rational singularities. Main results are the theorem of Berthelot, Bloch and Esnault that compactly supported Witt vector cohomology computes the slope less than one part of rigid cohomology, and congruences modulo q for point counts over finite fields, including Ax–Katz, Serre's congruence for theta divisors and Esnault's theorem for rationally chain connected varieties.

## CStarAlgebras
Title: C\*-algebras, operator spaces and approximation

Develops the structure and representation theory of C\*-algebras, operator spaces with completely positive and completely bounded maps, C\*-tensor products, and approximation properties such as nuclearity, exactness and quasidiagonality. Main results include Stinespring's dilation theorem, Wittstock's extension theorem, the characterizations of nuclearity by uniqueness of the C\*-tensor norm, semidiscreteness of the bidual and amenability, the Choi–Effros lifting theorem, Kirchberg's tensor characterizations of the weak expectation and local lifting properties, Voiculescu's noncommutative Weyl–von Neumann theorem, and permanence of exactness under quotients.

## CStarClassification
Title: Classification of AF and purely infinite simple C\*-algebras

Develops two classification theories for C\*-algebras: AF algebras by their scaled ordered K₀-group, and Kirchberg algebras, the separable nuclear purely infinite simple ones, by KK-equivalence. Main results are Elliott's classification of AF algebras with the range of the invariant, Glimm's classification of UHF algebras, Kirchberg's embedding of exact algebras into O₂, the absorption theorems for O₂ and O∞, Phillips's homomorphism theorem, and the Kirchberg–Phillips classification with its K-theoretic form under the universal coefficient theorem.

## CyclotomicClassGroupsAndStickelberger
Title: Cyclotomic class groups and Stickelberger theory

Develops the Galois-module theory of class groups of cyclotomic fields: Stickelberger's theorem at every conductor, the Herbrand–Ribet theorem, Kummer's criterion for regular primes, circular units and the growth of class numbers in the cyclotomic tower. The converse to Herbrand's theorem goes through Ribet's modular construction, for which the abelian variety attached to a weight 2 newform is built.

## DGAInfinity
Title: DG and A-infinity algebras, categories, and modules

Builds the algebraic foundations of differential graded and A∞ algebras, categories, modules and bimodules, from signed multilinear algebra through bar–cobar constructions and Maurer–Cartan twisting. Main results include Kadeishvili's minimal model theorem with homological transfer, derived Morita theory with compact generators, Drinfeld's DG quotients and their comparison with Verdier quotients, Hochschild deformation theory and intrinsic formality, smooth, proper and Calabi–Yau structures, Euler forms on perfect objects, and relative quadratic Koszul duality.

## DGFloerPartII
Title: DG Floer theory, Part II: spheres, knotted hypersurfaces and bordism
PR: #1799

Applies Floer homology with coefficients in DG local systems to further theorems of Barraud, Damian, Humilière and Oancea on almost existence of contractible periodic orbits and finiteness of the π₁-sensitive Hofer–Zehnder capacity. Main results are their criterion in a form realizing a rational multiple of a homology class by a closed oriented manifold, almost existence and finite capacity for manifolds abundant with 2-spheres, such as spheres, compact Lie groups other than tori and projective spaces, and a theorem on knotted hypersurfaces in cotangent bundles.

## DiamondEtaleCohomology
Title: Étale cohomology of diamonds and its four operations

Builds the étale derived category of a diamond or small v-stack as a presentable stable category, with pullback, direct image, derived tensor product and internal Hom carrying their adjunctions, composition laws and base change. It develops partially proper morphisms, canonical compactifications, étale extension by zero, proper base change, and constructible and perfect-constructible complexes with cohomological bounds, after Scholze. The main result is compact generation, with compact objects identified with perfect-constructible complexes under a uniform cohomological bound.

## DimerModelsAndLozengeTilings
Title: Dimer models and lozenge tilings

Builds the dimer model on the hexagonal lattice, that is, lozenge tilings of the triangular lattice: height functions and Thurston's criterion for tileability, Kasteleyn's theorem, and Gibbs measures on tilings of the plane with their slopes. Its main results are the existence of an ergodic Gibbs measure of every slope and, for every interior slope, its explicit determinantal description by the incomplete beta kernel.

## DiracScatteringAndNonlinearFourierTransform
Title: Dirac scattering and the non-linear Fourier transform

Develops one-dimensional Dirac systems on the half-line: fundamental solutions, Hermite–Biehler functions, scattering functions and, for square-integrable potentials, the SU(1,1) non-linear Fourier transform with its Plancherel identity. It continues with de Branges spaces, Weyl functions and spectral measures, and, for real potentials, proves pointwise convergence of the non-linear Fourier transform at almost every resonance-free point, the conditional form of Poltoratski's non-linear Carleson theorem.

## DynamicalDegreesOfRationalMaps
Title: Dynamical degrees of rational maps
PR: #2431

Builds the degree theory of dominant rational maps between projective varieties over an arbitrary field: the graph of a rational map, intersection numbers, and the positivity inequalities of Siu and of Khovanskii and Teissier. Its main results are the existence of the dynamical degrees as limits, their independence of the polarisation, their log-concavity and their invariance under birational conjugacy; the algebraic entropy is defined from them.

## EllipticCurveModularity
Title: Modularity and modular parametrisations of elliptic curves over ℚ
PR: #1018

Builds the correspondence between elliptic curves over ℚ and weight-two newforms with rational coefficients, and the modular parametrisation of a curve by the modular curve X₀(N) at its conductor. Main results are the existence and uniqueness of the newform attached to every elliptic curve over ℚ, deduced from Serre's modularity theorem and Faltings's isogeny theorem, with level equal to the conductor and agreement of all Euler factors, and the equivalence of the newform, Jacobian-quotient and parametrisation forms of modularity, with analytic continuation of the L-function.

## EllipticCurveModularityImaginaryQuadraticPartII
Title: Modularity of elliptic curves over imaginary quadratic fields, Part II: all CM fields
PR: #2445

Proves that every elliptic curve over every CM number field is modular: it corresponds to a weight-zero isobaric automorphic representation of GL₂ with trivial central character, with matching local factors at every finite place and matching L-functions. It adapts the prime-switching argument used for imaginary quadratic fields by making the auxiliary curve modular before cyclotomic base change and, for fields containing a fifth root of unity, by a modularity lifting theorem at 5 that keeps a place with unipotent residual inertia, produced by degenerating the family of covers.

## EllipticCurveModularityPartIIGL2TypeAbelianVarieties
Title: Abelian varieties of GL₂-type and modularity of ℚ-curves
PR: #1036

Studies abelian varieties of GL₂-type over ℚ, their endomorphism algebras and their λ-adic representations. It proves that each is a quotient of a modular Jacobian J₁(N), with the expected conductor and level, and deduces the modularity of ℚ-curves.

## EllipticCurvePeriodsAndModularParametrizations
Title: Periods of elliptic curves and modular parametrizations
PR: #1715

Develops the invariants of an elliptic curve over a number field built from the period lattices at its infinite places: local and global periods, the analytic order of the Tate–Shafarevich group defined through the Birch and Swinnerton-Dyer formula, and lattice formulas for the Faltings height. For curves over ℚ it treats optimal modular parametrizations, the Petersson formula for the modular degree, divisibility results for the Manin constant, rationality of L(E,1)/Ω in analytic rank zero, and Stevens' curve of least Faltings height in an isogeny class.

## EndoscopicTransferAndUnitaryTraceComparison
Title: Endoscopic transfer and unitary trace comparison

Builds the theory of stable conjugacy and endoscopic transfer: transfer factors, the fundamental lemma, and the stable and twisted trace comparisons for unitary groups. It uses them to stabilise the traces of Igusa correspondences, to describe local packets and the global classification for unitary groups, and to prove transfers in rank four such as the one between GSp₄ and GL₄.

## EnriquesSurfaces
Title: Enriques surfaces, projective models and automorphisms

Constructs the algebraic geometry of Enriques surfaces: integral Picard and numerical invariants, genus-one pencils, linear systems of low degree, double-plane and Reye models, and automorphism groups through their action on the associated lattices. Its main results identify the automorphism group of a generic nodal or unnodal Enriques surface, away from small characteristics, with a level-two congruence subgroup of a reflection group acting on such a lattice.

## EnriquesSurfacesAndIntegralNonexistence
Title: Enriques surfaces and nonexistence over the integers
PR: #1488

Treats the arithmetic of Enriques surfaces in all characteristics, including two: genus-one fibrations, canonical coverings, families and Picard descent. Its main results are that there is no flat proper family of Enriques surfaces over the integers, and that there is no non-exceptional Enriques surface over the field with two elements whose Picard scheme is constant.

## EtaleCohomologyFoundations
Title: Étale cohomology foundations

Builds étale cohomology of schemes with finite, adic and rational coefficients: Nagata compactification, constructible sheaves, proper and smooth base change, cohomological dimension, Artin vanishing and finiteness, purity, duality and perverse sheaves. Its main results are the six operations on bounded constructible complexes with their base change, Künneth and duality theorems, and the exact sequence of arithmetic fundamental groups.

## EtaleDualityAndPerverseSheaves
Title: Étale cohomology foundations, part II: refined duality, perverse decomposition and local traces

Extends the foundations of étale cohomology of schemes with duality for constructible complexes over self-injective finite coefficients, flat traces with multiplicities, higher étale Chern classes, and the functor calculus of perverse sheaves and intersection complexes. Main results are the weight filtration and geometric semisimplicity of mixed perverse sheaves, the decomposition theorem and relative hard Lefschetz, and trace comparisons for cohomological correspondences in the contracting and tubular-neighbourhood cases.

## EulerSystemsAndKolyvaginSystems
Title: Euler systems, Kolyvagin systems and higher-rank descent

Develops the passage from Euler systems of Galois cohomology classes to bounds on Selmer groups: Kolyvagin derivative classes, Kolyvagin systems of rank one, descent with bounded error, self-dual Selmer structures, Stark systems and higher-rank systems, and Iwasawa-theoretic variation. Main results are Selmer bounds from a nonzero Kolyvagin class after Rubin, Mazur–Rubin and Howard, with equality under primitivity, Fitting-ideal control from higher-rank Euler systems, and Rubin's weak Leopoldt theorem. Arithmetic Euler systems and their norm relations enter as hypotheses.

## FaltingsFinitenessAndIsogenyTheorems
Title: Faltings finiteness, semisimplicity and isogeny theorems
PR: #1004

Proves the finiteness theorems of Faltings' 1983 paper on abelian varieties over number fields, with the corrections of his erratum. Main results are finiteness of principally polarized abelian varieties of bounded modular height, stationarity of heights in ℓ-divisible towers, the Tate conjecture for endomorphisms and semisimplicity of Tate modules, finiteness of isogeny classes with good reduction outside a finite set, the Shafarevich conjecture for abelian varieties and for curves of genus at least two, and the corresponding statements for elliptic curves.

## FaltingsFinitenessAndIsogenyTheoremsPartII
Title: Quantitative isogenies and uniform integral Tate bounds
PR: #1738

Develops quantitative forms of Faltings' isogeny theory for abelian varieties over number fields and finitely generated fields of characteristic zero. Rosati metrics and the Masser–Wüstholz period theorem give polynomial bounds on endomorphisms, arithmetic of orders and Hom discriminants removes polarizations from isogeny estimates, and an elliptic isogeny estimate becomes a bound in the height of the j-invariant. Main results are quantitative simple factorization, isogeny bounds depending only on the dimension, and uniform index bounds for integral Tate algebras and adelic Galois images.

## FiniteFlatGroupsAndIntegralPadicHodgeTheory
Title: Finite flat group schemes and integral p-adic Hodge theory

Develops finite flat commutative group schemes and p-divisible groups, with the integral p-adic Hodge theory classifying them by semilinear algebra: Tate's Hodge–Tate decomposition and generic fibre theorem, Raynaud's results and the Oort–Tate classification, Dieudonné theory with the Dieudonné–Manin classification, Fontaine–Laffaille theory, and Breuil–Kisin theory, including Kisin's classification of crystalline lattices and of p-divisible groups over p-adic integer rings. Applications include local residual types and Serre weights, Fontaine's ramification bound, flat deformation conditions and Raynaud's determinant theorem.

## FiniteFlatGroupsAndIntegralPadicHodgeTheoryPartII
Title: Finite flat group schemes and integral p-adic Hodge theory, part II
PR: #1843

Builds integral tensor structures on Dieudonné displays and the deformation theory of p-divisible groups with tensors. Main results are the criteria for very good integral Hodge embeddings, the theorem identifying adapted deformations over discrete valuation rings with the local-model quotient of a versal family under an infinitesimal compatibility hypothesis, and the construction of adapted ordinary lifts from a central Newton–Levi filtration, to which every element of the rational σ-centralizer lifts as a self-quasi-isogeny.

## FourManifolds
Title: Four-dimensional manifolds, intersection forms and elliptic examples

Builds the geometry and algebra of four-manifolds: explicit smooth models and handle decompositions, the homotopy classification by intersection forms, topological surgery and the homeomorphism classification, Spinᶜ structures, and elliptic surfaces. It includes the restrictions on definite intersection forms that come from anti-self-dual gauge theory.

## FreeGroupsAndLimitGroups
Title: Free groups, equations over groups, and limit groups

Develops free groups and the groups that resemble them: conjugacy, roots and centralizers, Stallings graphs of finitely generated subgroups, Bass–Serre theory, equations and coordinate groups over a group, quadratic and Makanin's generalized equations, limit groups, Lyndon length functions and JSJ decompositions. Main results are decidability of systems of equations and inequations over a free group, Merzljakov's theorem on formal solutions, the equivalence of limit groups, fully residually free groups and coordinate groups of irreducible algebraic sets, finite Makanin–Razborov diagrams, and the Kharlampovich–Myasnikov implicit function theorems.

## FukayaTheory
Title: Fukaya categories of compact Lagrangian branes

Constructs Lagrangian Floer cohomology and the filtered curved Fukaya category of compact Lagrangian branes in a symplectic manifold, with weak bounding cochains, continuation functors, modules and split-closed derived categories, built from moduli spaces of pseudoholomorphic discs. Main results are the curved A∞ relations, invariance of the localized categories under Hamiltonian isotopy, the bound of the number of intersection points of an exact or weakly exact brane with its Hamiltonian image by its total Betti number, and the Floer cohomology of the zero section.

## FunctionFieldArithmeticPartII
Title: Function field arithmetic, part II
PR: #1831

Extends the arithmetic of function fields to infinite root stacks of line bundles with sections and to geometric class field theory with quadratic ramification, building the graded root Picard stack with an adelic presentation and normalized character sheaves in every degree. The main result, after Yun–Zhang, is that for a double cover of smooth projective curves over a finite field of odd characteristic, the Frobenius trace function of the quadratic character sheaf on the root Picard stack is the quadratic idele class character.

## GaloisActionOnEtaleCohomology
Title: The Galois action on étale cohomology of geometric fibres

Constructs the action of the absolute Galois group on the étale cohomology of the geometric fibre, for a scheme over a field and for a rigid space over a complete non-archimedean field. It proves the functoriality of the action, its continuity with ℓ-adic and rational coefficients, the comparison with higher direct images to the base point, and the Hochschild–Serre spectral sequence.

## GaloisSectionsPadicPeriodMaps
Title: Galois sections and p-adic period mappings

Studies sections of the fundamental exact sequence of a variety over a number field by means of p-adic period maps. It defines Selmer sections and their localisation maps and proves, for a smooth projective curve of genus at least two over a number field with no CM subfield, that only finitely many local points at each finite place arise from Selmer sections.

## GaugeQuiltFieldTheory
Title: Connected symplectic gauge field theory and quilted sewing

Constructs the connected (2+1)-dimensional Floer field theory of Wehrheim and Woodward for coprime rank and degree. Surfaces carrying unitary bundles with fixed determinant are sent to integral, ℤ/4-graded extended Fukaya categories of their moduli spaces of central-curvature connections, and three-dimensional bordisms to quilted A∞ functors. Main results are the Lagrangian correspondences of elementary bordisms, independence of the Cerf decomposition, and the resulting functor on the decorated connected bordism category.

## GaussianIsoperimetryAndClusters
Title: Weighted perimeter, Gaussian isoperimetry and clusters

Builds perimeter with respect to a positive density on Euclidean space, clusters of sets with their interfaces and isoperimetric profiles, and Ehrhard symmetrisation. Main results are the Gaussian isoperimetric theorem with its equality case (half-spaces are the only minimisers), also in its two-cell cluster form, the inequalities of Borell–Sudakov–Tsirelson and Bobkov, and Ehrhard's inequality for convex sets.

## GeometricCurrents
Title: Integral currents, geometric homology and minimizing hypersurfaces

Builds currents on Riemannian manifolds: mass, integer-rectifiable and integral currents, boundary, pushforward and slicing, and the homology of integral currents with its comparison to singular homology. It then proves deformation and compactness theorems, treats the Plateau problem and mass minimisation in a homology class, and proves interior regularity of area-minimising hypersurfaces in ambient dimension at most seven.

## GeometricMeasureTheory
Title: Geometric measure theory: rectifiability, BV, and finite perimeter

Builds Euclidean geometric measure theory: rectifiable curves and arclength, rectifiable sets with the area and coarea formulas, functions of bounded variation and their variation measures, approximation and compactness, and sets of finite perimeter with their reduced boundaries. Main results are the structure theorem for sets of finite perimeter, the coarea formula for functions of bounded variation, traces and the Gauss–Green formula, giving the measure-theoretic basis used for the Euclidean isoperimetric inequality.

## GeometricTopology
Title: Geometric topology

Builds the geometric topology of manifolds from the smooth level upwards: manifolds with boundary, gluing, handles and tubular neighbourhoods, locally flat embeddings, diffeomorphism groups, knots and links, Dehn surgery, hyperbolic structures, decompositions of three-manifolds, Heegaard splittings, foliations and triangulations. It states the theorems these make available, among them the annulus theorem, Mostow rigidity, the JSJ theorem and geometrization.

## GeometryOfNumbersAndQuadraticArithmetic
Title: Geometry of numbers, quadratic forms and homogeneous arithmetic

Develops the geometry of numbers and the arithmetic of integral quadratic and hermitian lattices: covolumes and successive minima, genera and spinor genera, representation densities and the mass of a genus, and Siegel's mean value theorem. It includes the homogeneous dynamics behind Margulis's theorem on values of indefinite quadratic forms and Duke's equidistribution theorem, with the entropy of measure-preserving maps, as well as LLL-reduced bases and the hermitian K-theory of exact categories.

## GibbsMeasuresAndTheIsingModel
Title: Gibbs measures and the Ising model

Builds the theory of infinite-volume Gibbs measures of lattice spin systems with a finite single-site space: existence by compactness, extremal Gibbs measures as the tail-trivial ones, and Dobrushin's uniqueness criterion. It applies this to the nearest-neighbour Ising model on the integer lattice, with the plus and minus states, uniqueness in one dimension and at high temperature, and spontaneous magnetization in two dimensions by Peierls' argument.

## GL2AutomorphicRepresentationsAndTransfer
Title: GL₂ automorphic representations and transfer

Builds the local and adelic representation theory of GL₂ that links classical modular forms to automorphic transfer: newvectors, Whittaker functions and local factors, the comparison with classical and Hilbert modular forms, the Jacquet–Langlands correspondence, and cyclic and solvable base change. Its applications include the automorphy of solvable Artin representations and modularity theorems in characteristic two.

## GlaubermanZStar
Title: Isolated involutions and Glauberman's Z\* theorem
PR: #1778

Proves Glauberman's Z\* theorem: in a finite group, an involution that commutes with none of its other conjugates is central modulo the largest normal subgroup of odd order. It develops isolated involutions and their fusion, the reduction of a minimal counterexample, the Brauer–Suzuki theorem for groups with generalized quaternion Sylow 2-subgroups, constancy of principal 2-block characters on involution sections, and the character-value argument that completes the proof.

## GromovWittenTheory
Title: Gromov–Witten theory of closed symplectic manifolds

Constructs the cohomology-valued Gromov–Witten operations of a closed symplectic manifold with a tame almost complex structure from virtual classes of moduli spaces of stable maps, and from them the Novikov-completed cohomological field theory, the genus-zero quantum product and descendant and ancestor classes. Main results are the Kontsevich–Manin axioms for these operations, independence of the almost complex structure, the genus-one degree-zero normalization by the Euler characteristic, associativity of the quantum product, and the string, dilaton, divisor and genus-zero topological recursion relations.

## GrossZagierAndArithmeticHeightsPartII
Title: Gross–Zagier formulas and arithmetic heights, part II: unitary special cycles and the arithmetic fundamental lemma
PR: #2457

Builds the arithmetic intersection theory of special cycles on unitary Rapoport–Zink spaces and unitary Shimura varieties of signature (n−1,1). Main results are the Kudla–Rapoport identities in four unramified and ramified local settings, the arithmetic Siegel–Weil formulas, and Zhang's arithmetic fundamental lemma for strongly regular elements when p is large relative to n. In the ramified Krämer setting the identity is proved in rank at most three and stated in higher rank under an explicit hypothesis, as is the ramified Siegel–Weil formula in dimension at least four.

## GroupActionsOnRiemannSurfaces
Title: Finite group actions on compact Riemann surfaces
PR: #1728

Develops finite group actions on compact Riemann surfaces of genus at least two through generating vectors of a signature, with refined passports, braid and topological equivalence, full automorphism groups of families, hyperelliptic and cyclic trigonal families, and the action on differentials and on the Jacobian. Main results are the Riemann existence criterion relating actions to generating vectors, the Hurwitz and Wiman bounds with Harvey's criterion for cyclic groups, Singerman's list, Macbeath's fixed-point formula, the Eichler trace and Chevalley–Weil formulas, and the group-algebra decomposition of the Jacobian.

## HardSphereDynamicsAndKineticLimits
Title: Hard-sphere dynamics and kinetic limits
PR: #2448

Builds the dynamics of finitely many hard spheres in Euclidean space or on a flat torus: elastic collisions, trajectories and, by Alexander's theorem, a measure-preserving flow defined off a null set. On this flow it develops the Liouville equation, marginals and correlation functions, equilibrium ensembles and the Boltzmann collision operator; Lanford's theorem on the Boltzmann–Grad limit is stated, and its law-of-large-numbers consequence is proved.

## HeegaardFloer
Title: Analytic Heegaard Floer homology

Builds integral Morse homology, the Fredholm and Cauchy–Riemann analysis of pseudoholomorphic curves with compactness and gluing, Lagrangian Floer homology in the exact case, and Heegaard Floer homology defined by holomorphic curves. Results along the way include the nonsqueezing theorem, invariance of Floer homology, and knot Floer homology with its comparison to combinatorial descriptions.

## HeightsRationalPointsAndObstructions
Title: Heights, rational points and obstructions
PR: #1017

Builds heights on varieties over number fields and function fields, including Weil's height machine and Néron–Tate heights on abelian varieties, then descent and the Mordell–Weil theorem. It goes on to adelic points with the Brauer–Manin and descent obstructions, and to finiteness results for rational and integral points on curves, for points in subgroups of finite rank and for points of small height.

## HeightsRationalPointsAndObstructionsPartII
Title: Heights, rational points and obstructions, part II: uniform Bogomolov and Mordell–Lang
PR: #1821

Develops uniform results for small points and rational points on subvarieties of abelian varieties. Main results are the Dimitrov–Gao–Habegger height inequality for non-degenerate subvarieties, Kühne's equidistribution in families, the uniform Bogomolov theorem of Gao–Ge–Kühne, uniform Mordell–Lang through a gap principle and a quantitative Vojta method, the geometric Bogomolov theorem over function fields of every characteristic, Yuan's uniform Bogomolov-type bound for curves over global fields, and a bielliptic family of genus-two curves as a worked case.

## HigherHidaAndColemanTheory
Title: Higher Hida and Coleman theory
PR: #2342

Extends p-adic families of modular forms to coherent cohomology of Shimura varieties in every degree. It constructs perfect ordinary Iwasawa complexes for Siegel modular varieties of every genus and higher Coleman theory for abelian-type Shimura varieties quasi-split at p, with analytic weight families, finite-slope complexes and cohomological eigenvarieties. Main results are derived Hida control and integral Serre duality for Siegel varieties, geometric classicality, deformation of interior eigenpackets, amplitude and sharp slope bounds, and a two-term control theorem for the singular Klingen family.

## HilbertModularVarietiesAndShimuraCurves
Title: Hilbert modular varieties and quaternionic Shimura curves

Constructs Hilbert modular varieties of a totally real field with Deligne–Pappas integral models, and Shimura curves attached to quaternion algebras split at exactly one real place, with the Drinfeld half-plane, integral model towers, cohomology and Hecke actions. Main results are Čerednik–Drinfeld uniformisation at a ramified prime, the Ihara lemma for Shimura curves with integral saturation, the Ihara lemma for definite quaternion algebras over every totally real field, and twisted moduli of Hilbert–Blumenthal abelian varieties with paired torsion having prescribed real and local points.

## HochschildHomologyAndHKR
Title: Hochschild homology and the Hochschild–Kostant–Rosenberg theorem
PR: #2447

Builds Hochschild homology and cohomology of an associative algebra over a commutative ring with coefficients in a bimodule: the complexes and their normalisation, the low degrees, the bar resolution with the comparison to Ext and Tor, and the cup product. Its main result is the cohomological Hochschild–Kostant–Rosenberg theorem, which identifies the Hochschild cohomology of an algebra that is smooth and projective over the base ring with its polyvector fields; polynomial algebras are computed by the Koszul resolution.

## HolderMapsBetweenManifolds
Title: Hölder maps between manifolds and Hölder diffeomorphism groups
PR: #3015

Defines maps of class C^{k,α} between smooth manifolds, possibly with boundary and corners, by the Hölder regularity of their coordinate representatives, and proves that the class does not depend on the charts, is closed under composition and has tangent maps one order lower. It builds the group of C^{k,α} diffeomorphisms with its inverse function theorems and topologies, showing that the C^{k,α} topology does not make it a topological group while the topology of convergence in every lower Hölder exponent does. On a compact manifold it develops the Banach spaces C^{k,α}(M), their inclusions, the comparison with Hölder continuity for a Riemannian distance, pullback and smoothing.

## HyperbolicDynamicsAndThermodynamicFormalism
Title: Hyperbolic dynamics and thermodynamic formalism
PR: #2441

Builds the theory of uniformly hyperbolic diffeomorphisms and flows on manifolds: hyperbolic sets and Anosov systems, stable and unstable manifolds, local product structure, expansivity and specification. It joins this to the thermodynamic formalism, proving that a Hölder potential on a basic set has exactly one equilibrium state (the theorems of Bowen and of Bowen and Ruelle), the uniqueness of the measure of maximal entropy, and the description of the SRB measure of a hyperbolic attractor of a flow.

## IgusaVarietiesAndTorsionConcentration
Title: Igusa varieties, compactified period fibres and torsion concentration
PR: #1090

Proves Koshikawa's vanishing theorem for unitary Shimura varieties: at a prime split completely in the CM field, with hyperspecial level, localization at a generic maximal ideal of the spherical Hecke algebra confines mod-ℓ cohomology to one side of the middle degree, with integral and boundary consequences (Caraiani–Newton in the form needed when `F⁺ = ℚ`). The route is Mantovan's filtration through Igusa varieties and local Shimura varieties, Koshikawa's semiperversity theorem for the local factor, and partial toroidal and minimal compactifications of central leaves and Igusa varieties identified with the fibres of the Hodge–Tate period map. Layer 0 sets up the quasi-split unitary similitude datum over a CM field with a self-dual lattice, its Hecke algebras, `p`-divisible groups with extra structure, Rapoport–Zink spaces and central leaves.

## IgusaVarietiesAndTorsionConcentrationPartII
Title: Igusa varieties and torsion concentration, Part II: compact unitary Shimura varieties
PR: #2439

Proves the Caraiani–Scholze theorem on the generic part of the mod ℓ cohomology of compact unitary PEL Shimura varieties, both Kottwitz's simple Shimura varieties and those attached to hermitian spaces quasi-split at all finite places. If the Galois representation of a maximal ideal of the spherical Hecke algebra is decomposed generic at a suitable auxiliary prime, the localized cohomology is concentrated in the middle degree. The proof compares the cohomology of Igusa varieties with automorphic representations through the trace formula, and the results include integral and twisted-coefficient forms.

## ImplicitAtlases
Title: Implicit atlases and rational virtual fundamental classes

Develops Pardon's implicit atlases on compact Hausdorff spaces, built from finite-group equivariant thickenings with obstruction spaces, and constructs from them virtual cochain complexes, a virtual orientation sheaf and a rational virtual fundamental class on Čech cohomology. Main results are independence of the class from the finite subatlas, its boundary, cobordism, refinement, pushforward and normalization properties, agreement with the Euler pairing of a smooth section, a product formula, and a formula for transverse fiber products through a Gysin map.

## IncompressibleFluids
Title: Incompressible fluids

Develops the theory of the incompressible Navier–Stokes and Euler equations on the whole space: solenoidal fields, the Helmholtz–Weyl decomposition and the Leray projection, the Stokes semigroup and its estimates, and the nonlinear and compactness estimates. Main results include Leray's existence theorem for weak solutions, two-dimensional uniqueness and regularity, Prodi–Serrin weak–strong uniqueness, the Fujita–Kato and Kato theorems for mild solutions, and for the Euler equations Kato's local well-posedness, the Beale–Kato–Majda criterion, the inviscid limit and the global two-dimensional theory of Wolibner and Yudovich.

## InfinitaryModelExistence
Title: Infinitary model existence, omitting types and interpolation

Derives the model theory of the infinitary logic Lω₁ω over countable languages from one engine, the model existence theorem for consistency properties, together with countable fragments, infinitary types, projective classes and the graph translation from function symbols to relations. Main results are downward Löwenheim–Skolem for countable fragments, the omitting types theorem, Craig, Lyndon and Malitz interpolation and projective-class separation for sentences, and Marker's boundedness theorems showing that no Lω₁ω sentence defines the class of well-orders.

## InstantonFloerTheory
Title: Instanton Floer theory

Constructs instanton Floer homology of three-manifolds from moduli spaces of anti-self-dual connections on cylinders, in three versions: an integral theory for admissible SO(3) bundles, a theory of integral homology spheres that accounts for the reducible connection, and a framed theory over the complex numbers for every closed oriented three-manifold. It establishes naturality, maps induced by cobordisms, operations from universal classes, exact surgery triangles, excision, Künneth formulas for disjoint unions, and an Atiyah–Floer type comparison in the admissible case.

## IntegralHeckeAndGaloisDeterminants
Title: Integral Hecke actions, determinants and interpolation

Develops the integral algebra that attaches Galois data to Hecke eigensystems over torsion and nonreduced coefficient rings: Chenevier's determinants as multiplicative polynomial laws, reconstruction of representations over henselian local rings, derived Hecke actions on cohomology, and Hecke polynomials for GLₙ and GSp₄. Main results are an interpolation theorem giving a unique continuous determinant with prescribed Frobenius characteristic polynomials, its descent modulo a nilpotent ideal with a uniform exponent, and an integral Ribet theorem producing an extension module whose Fitting ideal lies in the congruence ideal.

## InverseGaloisAndArithmeticFundamentalGroups
Title: Inverse Galois theory and arithmetic fundamental groups

Develops the arithmetic of finite covers behind inverse Galois theory: Galois algebras, local systems, pro-étale and tame fundamental groups, rigidity, braid orbits of Nielsen classes, embedding problems and Hurwitz spaces. Main results are Hilbert's irreducibility theorem over number fields, rational rigidity, the stable classification of braid orbits by the lifting invariant, Shafarevich's theorem that every finite solvable group is a Galois group over a number field, and the description of components of Hurwitz spaces by lifting invariants. The inverse Galois problem over ℚ is formulated as an open statement.

## InverseGaloisAndArithmeticFundamentalGroupsPartII
Title: Inverse Galois theory and arithmetic fundamental groups, Part II: homological stability for Hurwitz spaces

Proves the homological stability theorem of Ellenberg, Venkatesh and Westerland for Hurwitz spaces of branched covers of the disc with monodromy in a nonsplitting conjugacy class of a finite group. The components of all Hurwitz spaces form a graded ring whose central stabilizing element induces homology isomorphisms in a linear range, proved with Koszul-type complexes and arc complexes. Consequences are Betti number bounds uniform in the number of branch points, transferred to the étale cohomology of Hurwitz schemes over the algebraic closure of a finite field.

## JacobianChallenge
Title: The Jacobian challenge

For a smooth proper geometrically connected curve over a field, builds the Jacobian as an abelian variety representing the degree-zero Picard functor, without assuming a rational point, and, for each rational point, the Abel–Jacobi map with its universal property. Along the way it develops Riemann–Roch and Serre duality on curves, relative Picard schemes, and abelian varieties with their duals, polarizations and theta divisor.

## JacobianChallengePartII
Title: The Jacobian challenge, Part II: relative Jacobians, theta bundles and universal differences

Continues the Jacobian challenge in families: for a smooth projective curve over a noetherian base it shows that the relative Jacobian is an abelian scheme with a canonical principal polarization, and builds Abel maps without a chosen section. It then treats theta divisors and the Poincaré bundle for an arbitrary divisor of degree one, and the difference and Faltings–Zhang morphisms on fibre powers.

## K3Surfaces
Title: K3 surfaces, cohomology, periods, cones and Torelli

Develops the geometry of algebraic and complex analytic K3 surfaces: the absence of global vector fields and one-forms in characteristic p > 2, Ricci-flat Kähler metrics, the even unimodular lattice of signature (3,19) on second cohomology, marked deformation families, period domains and twistor families. Main results are local and global Torelli theorems with surjectivity of the period map, the description of the Kähler cone by smooth rational curves, Picard number 22 for unirational K3 surfaces, and the period description of K3 surfaces with a fixed-point-free involution.

## K3SurfacesAndSymplecticBoundedness
Title: K3 surfaces, Part II: Picard lattices and symplectic boundedness

Extends the theory of K3 surfaces to smooth proper surfaces over arbitrary fields of every characteristic, with their crystalline and étale cohomology and their geometric and arithmetic Picard lattices. Main results are the vanishing of global vector fields and one-forms in every characteristic, bounds on Picard ranks, faithful action of automorphisms on cohomology, a uniform bound on finite automorphism groups, Mukai's bound of 960 for finite symplectic groups in characteristic zero, and separated moduli of polarized K3 surfaces of fixed degree with finitely many isomorphism classes over each finite field.

## KleinianGroups
Title: Kleinian groups, hyperbolic 3-manifolds, and arithmetic volume
PR: #432

Develops discrete subgroups of PSL(2,ℂ) acting on hyperbolic 3-space, their fundamental domains and covolumes, and the Bianchi groups with their congruence subgroups. Main results compute from explicit fundamental domains the covolume of PSL(2,ℤ[i]) as one third of Catalan's constant and that of PSL(2,ℤ[ω]) as √3 L(2,χ₋₃)/8, and deduce the volumes of two congruence quotient manifolds. It also formulates Thurston's open question on rational relations among hyperbolic volumes, with a provable finite approximation.

## KTheoryFiniteLocalFields
Title: K-theory of finite and local fields

Computes the higher algebraic K-groups of nonarchimedean local fields, building on Quillen's calculation for finite fields, through rigidity for henselian rings, integral K₂ and trace-method calculations of Hesselholt and Madsen with logarithmic de Rham–Witt complexes. Main results include Moore's structure theorem for K₂ of a local field, Izhboldin's torsion theorem in characteristic p, and the identification of the p-completed K-groups with Galois cohomology, keeping integral, finite-coefficient and completed groups distinct, together with comparison maps to completions of number fields.

## LevelOneAutomorphicFormsForClassicalGroups
Title: Level-one automorphic forms for classical groups
PR: #2285

Develops the Chenevier–Taïbi theory of level-one algebraic cuspidal automorphic representations of PGLₘ over ℚ, using the Rankin–Selberg explicit formula, Arthur's classification for classical groups and Arthur's L²-Lefschetz trace formula. Main results are the classification of such representations of motivic weight at most 22, with partial classifications in weights 23 and 24, dimensions of spaces of level-one Siegel cusp forms in low genus, and the four weight-13 cusp forms of genera 8, 12, 16 and 24 as harmonic theta series of the Leech lattice.

## LieGroupsPartII
Title: Lie groups, part II: minimal parabolic subgroups, the Bruhat decomposition and the self-adjoint matrix model of real reductive groups

Continues the structure theory of real reductive Lie groups after the Cartan, Iwasawa and KAK decompositions, for groups that need not be connected, semisimple, linear or of finite centre. It proves conjugacy of Cartan involutions and of Iwasawa decompositions with a common split centre, defines the minimal parabolic subgroup with its Langlands decomposition, proves the Bruhat decomposition, and shows that the real points of a connected reductive group over ℝ, realised as a self-adjoint matrix group, carry all of this structure.

## LocalAnabelianGeometry
Title: Anabelian geometry of p-adic local fields
PR: #1811

Proves Mochizuki's theorem that isomorphisms between finite extensions of ℚₚ correspond bijectively to outer isomorphisms of their absolute Galois groups preserving the upper ramification filtrations, together with Hyeon's refinement for m-step solvable quotients. The proof recovers from the filtered Galois group, one at a time, the numerical invariants of the field, the cyclotomic character, inertia, the additive and integral structure of the field, Hodge–Tate weights and uniformizing characters, and then glues the resulting field isomorphisms.

## LocalAnabelianGeometryPartII
Title: Local anabelian geometry, Part II: Abrashkin's theorems
PR: #2867

Proves Abrashkin's theorems that a nonarchimedean local field of residue characteristic p, of characteristic 0 or p, is determined by the maximal pro-p quotient of its absolute Galois group together with its upper ramification filtration. Every isomorphism of these filtered groups is conjugation by a unique isomorphism of the maximal p-extensions carrying one base field to the other, for every prime p, including p = 2.

## LocalFiniteGroupTheory
Title: Local analysis of finite groups
PR: #1634

Develops the local analysis of finite groups through normalizers and centralizers of p-subgroups: p-cores, the Fitting and generalized Fitting subgroups, components, coprime action, the Thompson subgroup, normal p-complements and signalizer functors. Main results include Hall's theorem, the conjugacy part of Schur–Zassenhaus, the Baer–Suzuki theorem, Bender's theorem, Thompson's replacement theorem, Glauberman's ZJ theorem, Thompson's theorem that a finite group with a fixed-point-free automorphism of prime order is nilpotent, and Glauberman's solvable signalizer functor theorem.

## LocallyAnalyticDistributions
Title: Locally analytic distributions, growth and character spaces

Develops locally analytic functions and distributions on ℤₚ, on products of p-adic integer rings and on compact p-adic analytic manifolds, the Hyodo–Kato cohomology of semistable Stein curves, and the Fredholm theory of Serre, Coleman and Buzzard for compact operators over Noetherian Banach algebras, as needed for p-adic families. Main results include nonarchimedean Hahn–Banach and open mapping theorems, the Amice transform dictionary, the Amice–Vélu–Vishik extension and uniqueness theorem with its sharp degree bound, Mellin transforms on character spaces, and finite-slope decompositions.

## LorentzianGeometry
Title: Lorentzian geometry and causality
PR: #2232

Specializes the semi-Riemannian foundations to Lorentzian geometry: Lorentzian scalar products and time cones, time orientations and spacetimes, causal curves, spacelike and null hypersurfaces with optical functions and null generators, and acoustical metrics as the model. It develops the causal ladder, global hyperbolicity, Cauchy surfaces and domains of dependence, also inside subsets of manifolds with boundary and for metrics of low regularity, and ends with focusing and the singularity theorems of Hawking and Penrose.
## MaassForms
Title: Maass forms: the hyperbolic Laplacian on Γ₀(N)\ℍ, Hecke–Maass newforms, and their invariants
PR: #1717

Develops the classical theory of weight-zero Maass cusp forms for Γ₀(N) with a Dirichlet character: the hyperbolic Laplacian and its self-adjoint realization, Fourier–Whittaker expansions in K-Bessel functions, Hecke operators, Atkin–Lehner and Fricke involutions, and newforms with strong multiplicity one. Main results include Selberg's bound λ₁ ≥ 3/16, Selberg's eigenvalue conjecture as a statement proved at level one, Weyl's law, L-functions of Hecke–Maass newforms with their functional equation, and Maass forms for PSL₂(ℤ[i]) on hyperbolic three-space.

## MappingClassGroupsAndCanonicalRepresentations
Title: Mapping class groups and canonical representations of surface groups
PR: #2266

Builds the theory behind the theorem of Landesman and Litt: a representation of the fundamental group of a punctured surface of genus g, of rank r with r² < g + 1, whose conjugacy class has finite orbit under the mapping class group has finite image. It develops pure mapping class groups acting on surface groups, representation schemes, versal families of pointed curves, and the Hodge theory of unitary local systems on families of punctured curves.

## MathematicalBilliards
Title: Mathematical billiards

Builds the two classical planar billiard systems. For a strictly convex table it constructs the billiard ball map on the phase cylinder, shows that it is a twist map preserving the measure sin δ dδ ds, and proves Birkhoff's theorems on rotational invariant curves and on periodic orbits. For a polygonal table it constructs the phase space, the billiard flow and the translation surface obtained by unfolding a rational polygon, and for general measure-preserving flows it develops weak mixing.

## MetaplecticAutomorphicForms
Title: Metaplectic groups, Weil representations and automorphic theta kernels
PR: #1063

Constructs the Weil representation and the metaplectic double cover over local fields and adeles, and from them the local theta correspondence, global theta kernels and theta lifts, half-integral weight Maass forms with the Kohnen plus space, and the Shimura lift. Main results are Howe duality, conservation relations and see-saw identities, the regularized Siegel–Weil formula, the Rallis inner product formula and theta nonvanishing, the Duke–Imamoḡlu–Tóth trace identities, and the genus-two Jacobi–Eisenstein analysis of Bump–Friedberg–Hoffstein used for nonvanishing of quadratic twists.

## ModularCharactersAndBlocksPartII
Title: Modular characters and blocks, Part II: the Glauberman correspondence and heights of characters
PR: #2411

Continues the theory of blocks in two directions. The first is the character theory of coprime actions, ending in the Glauberman correspondence and its degree divisibility. The second is the theory of heights: Brauer's theorem on heights, height zero characters, the Fong–Reynolds correspondence and Reynolds' theorem on blocks with a normal defect group, with the height zero and Alperin–McKay conjectures stated as properties of blocks.

## ModularCurvesPartII
Title: Modular curves, Part II: uniformization, integral boundary and Hecke cohomology

Compares arithmetic modular curves with analytic quotients of the upper half-plane, builds their integral compactifications and bad fibres, and constructs the Hecke action on their Jacobians and cohomology. Results include compact uniformisation with the fields of definition of the cusps, Ihara's theorems, and, for the abelian varieties attached to newforms of weight 2, the corresponding quotients of J₀(N), oldform factors and Abel–Jacobi maps.

## ModularityAndLanglandsExtensions
Title: Modularity and Langlands extensions
PR: #1180

Extends modularity results to Artin representations, potential automorphy, symmetric power functoriality and the Sato–Tate conjecture, and treats packets for classical groups. It sets up the comparisons of normalizations these results need and states the remaining Langlands conjectures precisely.

## ModularityAndLanglandsExtensionsPartII
Title: Modularity and Langlands extensions, part II: the proof of symmetric power functoriality
PR: #2449

Carries out the proof of symmetric power functoriality for holomorphic modular forms: analytic continuation along eigenvarieties, level raising on unitary groups, automorphy lifting for symmetric powers, and functoriality for tensor products. The final results are the existence of every symmetric power lift of a non-CM newform of weight at least 2, and the holomorphy of the symmetric power L-functions of such newforms away from the level and of level-one eigenforms.

## ModularSymbolsPadicLFunctions
Title: Modular symbols and analytic p-adic L-functions of modular forms

Builds the cohomological theory of modular symbols with arbitrary coefficients, with Hecke, diamond and sign operators, the cohomological Eichler–Shimura isomorphism and the rational Drinfeld–Manin splitting, and proves algebraicity of twisted critical L-values divided by signed periods. On the p-adic side it builds overconvergent modular symbols, proves Stevens' control theorem in small slope, and constructs the p-adic L-function of a refinement of slope less than k + 1 with its interpolation formula, uniqueness and integral ordinary form. It also covers the critical-slope p-adic L-function of a non-θ-critical refinement, Pollack's signed p-adic L-functions at supersingular primes with a_p = 0, tame twists, and worked examples of level 11.

## MordellLawrenceVenkatesh
Title: The Mordell conjecture after Lawrence and Venkatesh
PR: #1231

Proves Faltings's theorem, that a curve of genus at least two over a number field has finitely many rational points, by the method of Lawrence and Venkatesh, and the finiteness of solutions of the S-unit equation by the same method. Along the way it builds p-adic period maps for families of abelian varieties, the Kodaira–Parshin family, and the surface topology and mapping class groups used to show that its monodromy is large.

## MordellLawrenceVenkateshPartII
Title: The Mordell conjecture after Lawrence and Venkatesh, part II
PR: #2461

Develops the higher-dimensional form of the Lawrence–Venkatesh method, which bounds integral points of a family through p-adic period maps and the Galois representations of its fibres. Its applications are the non-density of integral points on the parameter spaces of smooth projective hypersurfaces of large dimension and degree, and the finiteness, up to translation, of smooth hypersurfaces in a fixed ample class with good reduction in an abelian variety of dimension at least two, with explicit exceptional degrees in dimension three.

## MotivesAndAlgebraicCycles
Title: Algebraic cycles, pure and mixed motives

Builds Chow motives from correspondences with their Betti, de Rham and étale realizations, geometric motives with compact support from finite correspondences and motivic complexes, and Nori motives, and compares these constructions. Main results include Jannsen's semisimplicity theorem for numerical motives, comparisons with higher Chow groups, neutral and relative Tannakian reconstruction, and the identification of formal periods with the coordinate ring of a bitorsor. It formulates the Hodge, Tate, standard and Beilinson–Bloch conjectures as precise statements and proves their known implications and special cases.

## NashBlowups
Title: Nash blowups

Constructs the Nash blowup of a variety as the closure of the smooth locus in the Grassmannian of rank-d quotients of the sheaf of differentials, together with the normalized Nash blowup and the iterations of both. It proves the universal property, Nobile's theorem that in characteristic zero the Nash blowup is an isomorphism only for smooth varieties, the theorem of Duarte and Núñez-Betancourt for normal varieties in characteristic p, and a principle by which iterated Nash blowups never resolve certain singularities.

## NeronModelsAndSemistableAbelianVarieties
Title: Néron models and semistable abelian varieties

Builds Néron models of abelian varieties over discrete valuation rings and Dedekind schemes, their special fibres and component groups, and semistable reduction, including the semistable reduction theorem and the uniformisation of degenerating abelian varieties. Consequences include the criterion of Néron–Ogg–Shafarevich, the monodromy pairing, and conductors and local Euler factors.

## NonabelianLevelStructures
Title: Nonabelian level structures on elliptic curves
PR: #2273

Develops Chen's theory of moduli of elliptic curves with level structure by a finite group G, given by connected G-torsors over punctured elliptic curves: ramification of the level covers, their functoriality, the classification of cusps by finite group data, and cusp automorphism groups. Main results are Chen's combinatorial congruence, a divisibility for orbits of outer automorphisms of the rank-two free group on generating pairs of G, its consequence for nonabelian finite simple groups, and the geometry and noncongruence of the Markoff level curves of trace −2.

## NoncompactQuantumSymmetry
Title: Noncompact quantum symmetry and particle representations

Develops the measurable and unitary representation theory of locally compact groups needed to pass from spacetime symmetry to particle models: rays and projective representations, locally continuous multipliers, smooth vectors, systems of imprimitivity and induction. The central results are the locally compact imprimitivity theorem with its normalized induced Hilbert-space model and the Mackey machine, which classifies regular irreducible representations of semidirect products through dual orbits, stabilizers and their projective representations. These are applied to the Euclidean, Galilei, Poincaré and de Sitter groups, with the domain and differentiability results that connect group representations to observables.

## OddOrderTheorem
Title: The Feit–Thompson odd order theorem

Proves that every finite group of odd order is solvable, by the Bender–Glauberman local analysis and Peterfalvi's character theory. Along the way it develops the reduction to a minimal simple counterexample, local analysis for solvable groups of odd order, the Dade isometry and coherence of characters, the division of maximal subgroups of a minimal counterexample into five types with their character analysis, and the finite field comparison that yields the final contradiction.

## OperatorKTheory
Title: Operator K-theory, extensions and KK-theory

Builds the K-groups K₀ and K₁ of complex C\*-algebras from projections and unitaries, and Kasparov's bivariant groups KK(A,B) with the Kasparov product. Main results are Bott periodicity, the six-term exact sequence of an extension, Atkinson's theorem and Fredholm indices, the Brown–Douglas–Fillmore theorem, K-theory computations for free-group, rotation and Cuntz algebras, the bootstrap class with the universal coefficient and Künneth theorems, and E-theory from asymptotic morphisms.

## OperatorTheory/SelfAdjointSpectralTheory
Title: Self-adjoint spectral theory: the Borel functional calculus, unbounded operators, and Stone's theorem

Develops the spectral theory of self-adjoint operators on Hilbert space: one-parameter unitary groups and their generators, the bounded Borel functional calculus and projection-valued measures, closed operators and their resolvents. Its last part constructs the spectral measure of an unbounded self-adjoint operator through the Cayley transform, proves the resolvent formula, and shows that the unitary group it generates by Yosida approximation is the one given by Stone's theorem.

## OperatorTheory/UnboundedOperators
Title: Unbounded operators on Hilbert space

Develops closed, densely defined operators on Hilbert space: the unbounded Borel functional calculus, normal operators and joint spectral theory, the essential spectrum, and the decomposition of a self-adjoint operator into pure point, absolutely continuous and singular continuous parts. It also covers symmetric operators and their self-adjoint extensions, closed forms and the Friedrichs extension, analytic vectors, and perturbation theorems of Kato–Rellich type.

## PadicDifferentialEquationsAndRigidCohomology
Title: p-adic differential equations, rigid cohomology and p-adic weights

Develops differential and Frobenius modules over the Robba ring and related rings of overconvergent series, and builds rigid cohomology of varieties over finite fields with coefficients in overconvergent F-isocrystals. Main results are Kedlaya's slope filtration theorem and the p-adic local monodromy theorem, finiteness, Poincaré duality and the Lefschetz trace formula for rigid cohomology with coefficients, Kedlaya's p-adic Weil II, and the equality of crystalline, rigid and ℓ-adic factors of zeta functions of smooth proper varieties over finite fields.

## PadicHodgeTheory
Title: p-adic Hodge theory and geometric comparison

Builds the rational period rings and period functors of p-adic Hodge theory with their filtrations and admissibility, Robba realizations and B-pairs, monodromy, weak admissibility and Weil–Deligne parameters, and relative de Rham objects. Its endpoints are the group-valued period torsor, the localization presentation of the de Rham differential lattice, filtered de Rham comparison with coefficients, crystalline and semistable geometric comparison, and the good-reduction criterion. Explicit Kummer and Tate-curve periods fix the conventions.

## PainleveEquations
Title: Painlevé equations

Constructs the Painlevé equations as flat nonlinear connections, the isomonodromic connections, on moduli spaces of meromorphic connections with prescribed singularities, and Painlevé functions as their horizontal sections. Main results are smoothness and symplectic structure of these phase spaces, flatness of the isomonodromic connection, the Painlevé property through the Riemann–Hilbert correspondence, Okamoto's surfaces of initial conditions with symmetries and Riccati reductions, tau functions from Fredholm determinant lines, and comparison with the classical scalar, Hamiltonian and linear-system forms.

## PDE
Title: Partial differential equations

Builds the theory of second-order elliptic and parabolic equations on Euclidean domains: Sobolev spaces with their embedding, trace, extension and compactness theorems, the harmonic-analysis estimates (interpolation, Calderón–Zygmund theory, BMO), maximum principles, the Hopf lemma and the Aleksandrov–Bakelman–Pucci estimate, and the energy method for the Dirichlet, mixed and Neumann problems with their Fredholm theory and spectra. Its end results are solvability, regularity (De Giorgi–Nash–Moser, Schauder and Calderón–Zygmund estimates, Krylov–Safonov) and the maximum and Harnack principles for uniformly elliptic operators, with parabolic Schauder theory, Strichartz estimates and quasilinear existence as extensions.

## PELModuli
Title: Siegel and PEL moduli problems

Builds the moduli problems of abelian schemes with a polarization, an action of an order and a level structure, which include the Siegel, Hilbert and unitary cases. It starts from the linear algebra of lattices with an order action and their similitude groups, proves that the moduli problem is a smooth algebraic stack over the appropriate base, and identifies its complex points with a union of arithmetic quotients of hermitian symmetric domains.

## PELModuliPartII
Title: Siegel and PEL moduli problems, Part II: unitary integral and formal moduli
PR: #2453

Builds integral and formal moduli of unitary type for the arithmetic of unitary Shimura varieties: unitary Rapoport–Zink spaces of principal, almost self-dual, exotic and Krämer type with their special homomorphisms, integral CM moduli at every prime, and global integral models built from pairs of CM and unitary abelian schemes. Main results are formal smoothness or regular semistable reduction of the local spaces, finite étaleness of the CM moduli, smoothness, semistability and quasi-projectivity of the global models, and uniformization of their basic loci.

## PerfectoidQuotients
Title: Perfectoid quotients and their prismatic prerequisites

Develops the integral commutative algebra and explicit root constructions that accompany universal perfectoid quotients: Fontaine's generators over rings with torsion, torsion bounds for Witt vectors, removal of torsion, root closures, completed ring operations, radical formulas in characteristic p, and almost faithfully flat root extensions over a perfectoid field. Main results are that completions of root closures are perfectoid, an ind-syntomic refinement modulo p of André's cover, and functorial almost absolutely integrally closed extensions.

## PerfectoidQuotientsPartII
Title: Perfectoid quotients, part II: structure of integral perfectoid rings and the ind-syntomic André lemma

Extends PerfectoidQuotients to the structure theory of integral perfectoid rings with torsion: what the tilt determines (the ring modulo ϖ^p, its torsion, adic completeness, being a valuation ring and its value group, algebraic closedness of the fraction field), fibre products along surjections, and presentations as quotients of torsion-free perfectoid rings. It proves André's lemma without completions, for faithfully flat ind-syntomic ϖ-Henselian extensions, and deduces faithfully flat semiperfectoid covers of all p-Zariski rings. For regular local rings it gives faithfully flat perfectoid covers and the almost vanishing of Tor along finite subextensions of the absolute integral closure, which for F-finite residue fields is Heitmann–Ma's theorem.

## PerfectoidSpaces
Title: Perfectoid rings and spaces

Builds perfectoid rings and perfectoid spaces in general, without a perfectoid base field: almost mathematics, tilting, the tilting equivalence with its identification of étale sites, the almost purity theorem and the pro-étale site. It also introduces δ-rings and prisms, which it uses in its treatment of Zariski closed immersions.

## PlanarTopology
Title: Planar topology and the piecewise-linear structure of surfaces
PR: #271

Develops the classical topology of the plane and of surfaces by triangulation and polygonal approximation. Main results are the Jordan curve and crosscut theorems, invariance of domain in dimension two, Radó's theorem that compact surfaces are triangulable, the two-dimensional Hauptvermutung and Pachner's theorem, invariance of the Euler characteristic and orientability, the Schoenflies theorem with tameness of curves and graphs, uniqueness of piecewise-linear and smooth structures, and Epstein's theorem that homotopic homeomorphisms of surfaces are isotopic.

## PositiveMass
Title: Asymptotically Euclidean geometry and positive mass

Develops asymptotically Euclidean ends of Riemannian manifolds, the ADM mass and weighted Sobolev and Hölder analysis on such manifolds, and gives two proofs of the Riemannian positive mass theorem with rigidity: the minimal hypersurface argument in dimensions 3 to 7 and Witten's spinor argument for spin manifolds in all dimensions. Main results are nonnegativity of the mass of every end and Euclidean rigidity at an end of zero mass, including the Cecchini–Zeidler form for one asymptotically Euclidean end of a complete spin manifold with arbitrary other ends.

## PotentialAutomorphyInfrastructurePartII
Title: Potential automorphy infrastructure, Part II: polarized automorphy lifting and finiteness of deformation rings
PR: #2135

Develops automorphy lifting for Galois representations of CM and totally real fields that are conjugate self-dual up to twist, using algebraic modular forms on definite unitary groups, their Hecke algebras and Taylor–Wiles patching. Main results are Thorne's minimal lifting and finiteness theorems and his 2-adic lifting theorem, ordinary lifting and finiteness theorems, potential ordinary automorphy with prescribed Steinberg places, residually reducible deformation theory after Thorne and Allen–Newton–Thorne, and the integral R = T theorem of Liu–Tian–Xiao–Zhang–Zhu.

## PotentialModularityAndCompatibleSystems
Title: Potential modularity and compatible systems
PR: #1075

Develops weakly compatible systems of Galois representations of arbitrary rank, with their operations, monodromy, purity and L-functions, and the choice of auxiliary fields with prescribed local behaviour used to move modularity between coefficient primes. Main results are Moret-Bailly's theorem on points with local splitting conditions over global function fields, potential modularity of given lifts with specified local types, density-one residual irreducibility, and ordinary finiteness results via patching on definite unitary groups, as used in the Khare–Wintenberger proof of Serre's conjecture and in potential automorphy in higher rank.

## PrismaticCohomology
Title: Prismatic cohomology, Part I: Delta rings, prisms and relative cohomology

The first part of the prismatic theory: δ-rings and prisms over general rings, the site of bounded prisms, and the relative prismatic cohomology of a formal scheme over a bounded prism. It proves the Hodge–Tate and crystalline comparisons for smooth formal schemes and, under a torsion-freeness hypothesis on the prism, the de Rham comparison, and it constructs perfectoidizations.

## PrismaticCohomologyPartII
Title: Prismatic cohomology, Part II: Nygaard filtration, absolute prisms and q-de Rham theory

The second part of the prismatic theory. It treats Breuil–Kisin twists and the Nygaard filtration, absolute prismatic cohomology through the Cartier–Witt stack, and the q-crystalline and q-de Rham comparisons.

## PrismaticCohomologyPartIII
Title: Prismatic cohomology, Part III: Étale and syntomic comparisons and F-crystals

The third part of the prismatic theory. It proves the étale comparison, builds syntomic complexes, and establishes the equivalence between prismatic F-crystals over a complete discrete valuation ring of mixed characteristic and lattices in crystalline Galois representations.

## PrismaticCohomologyPartIV
Title: Prismatic cohomology, Part IV: logarithmic prismatic cohomology

Extends prismatic cohomology to log schemes, constructing log δ-rings and log prisms, saturated and animated log prismatic cohomology, and the log Nygaard filtration. Main results are the log Hodge–Tate, crystalline, q-de Rham and semistable comparisons, a Kummer-étale comparison with realizations in Kummer local systems, the Hyodo–Kato isomorphism, and the fact that log prismatic cohomology groups are Breuil–Kisin–Fargues modules.

## ProbabilisticAndMetricNumberTheoryPartII
Title: Probabilistic, metric and ergodic number theory, Part II: transfer operators and uniform renewal counting

Studies a free semigroup of linear maps acting on a cone in n-dimensional space, n ≥ 3, through transfer operators for its countably many projective branches, developing the Ionescu-Tulcea–Marinescu inequality, Hennion's essential radius bound, Birkhoff cone contraction, a Ruelle–Perron–Frobenius theorem with spectral gap and a uniform renewal theorem. Main results are a unique exponent β(n) > 1 admitting a conformal probability measure and an asymptotic count of semigroup words by growth, uniform in the starting point, with β(3) = 2 and an explicit constant when n = 3.

## PseudodifferentialOperators
Title: Pseudodifferential operators and elliptic analysis on bundles

Builds differential operators on vector bundles and the classical pseudodifferential calculus: symbols, quantization, composition and adjoints. On this it develops mapping properties on Sobolev, Lᵖ, Hölder and Zygmund spaces, elliptic parametrices with regularity and Fredholm theory on compact manifolds, powers of elliptic operators, and wave front sets.

## PseudoholomorphicCurveAnalysis
Title: Elliptic analysis of pseudoholomorphic curves

Builds the elliptic regularity theory of the Cauchy–Riemann equation used in symplectic topology: Sobolev maps from Riemann surfaces into almost complex manifolds, totally real boundary conditions, and linear estimates for real Cauchy–Riemann operators with Sobolev coefficients. Main results are the elliptic bootstrapping theorem for pseudoholomorphic maps and the Fredholm theory and Riemann–Roch theorem for real Cauchy–Riemann operators on compact surfaces with boundary.

## PurityForFlatCohomology
Title: Purity for flat cohomology and the conjectures of Gabber
PR: #1840

Proves purity for flat cohomology after Česnavičius and Scholze: for a Noetherian local complete intersection and a commutative finite flat group scheme, the fppf cohomology with supports in the closed point vanishes below the dimension. It builds fppf cohomology with supports, and deduces purity for torsors and gerbes, Gabber's conjectures on local Picard and Brauer groups, and purity for the Brauer group of regular schemes.

## QuantitativeOrbitMethodAndMicrolocalAnalysisOnLieGroups
Title: The quantitative orbit method and microlocal analysis on Lie groups
PR: #1842

Builds a microlocal calculus on unitary representations of Lie groups that is uniform in the representation, with symbols on the dual of the Lie algebra, and develops localization at infinitesimal characters, Rossmann's character formula and Kirillov-type trace asymptotics over coadjoint orbits. The main result is the asymptotic formula of Nelson and Venkatesh for smoothly weighted sums of Gan–Gross–Prasad periods of anisotropic orthogonal and unitary pairs over number fields, obtained using equidistribution of semiclassical limits by Ratner's theorem.

## QuantumFoundations
Title: Mathematical foundations of quantum systems
PR: #1771

Sets out the mathematics of quantum systems: states, observables and measurements, projection lattices and their probability measures, dynamics, composite systems and the canonical commutation relations, symmetries and projective representations. It ends with concrete particle models, among them the free Hamiltonian on L²(ℝⁿ), spin, the harmonic oscillator and the hydrogen atom.

## QuasicoherentSheavesOnPrestacks
Title: Quasi-coherent sheaves on prestacks
PR: #2450

Develops the ∞-category of quasi-coherent sheaves on a prestack, the limit of module categories over its affine points, for ordinary, animated and connective derived test rings, showing that the first two theories are restrictions of the third. Main results are flat hyperdescent without finiteness hypotheses, invariance under fpqc sheafification, affine pushforward with base change and the projection formula, agreement with quasi-coherent sheaves on schemes, perfect and almost perfect objects, quotients by group prestacks, and compact generation for qcqs schemes, perfect stacks and quotient stacks in characteristic zero.

## QuasiregularMaps
Title: Quasiregular maps
PR: #2134

Defines quasiregular maps between oriented Riemannian manifolds of the same dimension as continuous Sobolev maps satisfying a distortion inequality, and develops their outer, inner and maximal distortions. Main results are the comparison of these distortions, agreement with the classical definition on Euclidean domains, quasiregularity of suitable simplicial maps, and the first properties of quasiregularly elliptic manifolds, among them that every closed orientable flat manifold is quasiregularly elliptic.

## QWittVectors
Title: Arithmetic Λ-rings and q-Witt vectors

Builds big Witt rings, arithmetic Λ-rings and their equivalence with special λ-rings, and absolute and relative q-Witt rings with their exactness, base change and completions, from integral Witt polynomials, commutative algebra and derived completion. The endpoints are relative degree-zero q-Witt rings for every Λ-base and algebra, the completed relative Frobenius fixing q for étale coefficients, positive-degree q-Witt operations, complete framed difference calculus, and integer torsion-freeness and degreewise completion for smooth algebras over perfectly covered bases with their functorial p-complete E∞ de Rham comparison. All primes, including 2, and all positive truncation indices are included.

## RankOneConverse
Title: Rank-one converses and anticyclotomic localization
PR: #1805

Proves Skinner's p-converse theorems for weight-two newforms of squarefree level that are ordinary at a prime p ≥ 5: a one-dimensional Bloch–Kato Selmer group with injective localization at p forces a simple zero of the L-function and a Heegner point of infinite order. The argument over imaginary quadratic fields uses anticyclotomic Iwasawa theory, and quadratic twists with prescribed local behaviour give the rank-one converses over ℚ, a finite Selmer group criterion, and a rank-zero converse.

## RankZeroOneBSDPartII
Title: Rank-zero and rank-one Birch–Swinnerton-Dyer theory, Part II: Eisenstein converses and twist proportions
PR: #1732

Develops the converse theorems of Castella–Grossi–Lee–Skinner at Eisenstein primes: for an elliptic curve over ℚ with a rational cyclic isogeny of odd prime degree p, good reduction at p and a local condition on the kernel character, a p-adic Selmer group of corank r at most one forces analytic and Mordell–Weil rank r and a finite Tate–Shafarevich group. The proof uses quadratic twists, anticyclotomic Iwasawa theory, Heegner points and the Gross–Zagier formula, and yields positive proportions of rank-zero and rank-one quadratic twists in families with a 3-isogeny.

## RationalAnalyticPrismatization
Title: Rational analytic prismatization
PR: #2456

Builds Gelfand analytic geometry over ℚₚ, with Berkovich spectra, Gelfand stacks and their six-functor formalism, and analytic de Rham stacks, and on it the rational analytic prismatization of Anschütz, Le Bras, Rodríguez Camargo and Scholze with its twistor and Hodge–Tate stacks. Main results include full faithfulness of pullback from the twistor stack of a smooth rigid space to its relative Fargues–Fontaine curve, an equivalence on perfect complexes, recovery of pro-étale cohomology and Sen operators, Poincaré duality, decompletion for p-adic Lie group actions, and recovery of Scholze's Riemann–Hilbert functor.

## RealSemisimpleLieGroups
Title: Real semisimple Lie groups, parabolic subgroups and Riemannian symmetric spaces

Builds the structure theory of real semisimple and reductive Lie groups on top of the Cartan, Iwasawa and KAK decompositions: Cartan involutions, restricted roots, the real rank, the restricted Weyl group, minimal and general parabolic subgroups with their Langlands decompositions, and the Bruhat decomposition. It then develops the Riemannian symmetric space G/K: its invariant metric, curvature and geodesics, flats and rank, the conjugacy of maximal compact subgroups, and quotients by discrete subgroups.

## ReductiveGroups
Title: Reductive algebraic groups

Builds the general theory of affine algebraic groups and reductive groups from Hopf algebras and comodules: representations, Lie algebras, quotients, tori, solvable and unipotent groups, structure theory with root data, parabolics and the Bruhat decomposition, finite groups of Lie type, and classification by root data. It constructs the pinned Chevalley–Demazure group scheme over the integers of every root datum, and identifies with these models the classical group schemes over every commutative ring: symplectic and symplectic-similitude groups, orthogonal and special orthogonal groups of a quadratic form with the Dickson invariant, and general spin and spin groups, with their low-rank isomorphisms. It also develops highest-weight representations and regular-semisimple spectral quotients.

## ReductiveGroupsPartIII
Title: Reductive groups, part III: arithmetic conjugacy quotients and tori

Studies semisimple conjugacy classes and maximal tori of reductive groups over number fields and their completions, starting from the variety of conjugacy classes. Results include the group form of Chevalley's restriction theorem, approximation of local maximal tori by a global one, and the group-theoretic part of the independence of ℓ of Frobenius classes in the Mumford–Tate group of an abelian variety.

## RefinedTraceMethods
Title: Refined trace methods
PR: #1493

Builds cyclic and cyclotomic refinements of Hochschild homology, the cyclotomic trace from K-theory, and the arithmetic filtrations on topological Hochschild homology and its variants. Its comparisons identify these filtrations with prismatic and syntomic cohomology and with q-Hodge complexes.

## RelativisticQuantumFieldTheory
Title: Relativistic quantum field theory, free fields and perturbative renormalization

Develops the mathematics linking Lorentzian field equations and Fock space models to local quantum fields: causal Green operators of the Klein–Gordon, Dirac and Maxwell equations, free fields as operator-valued tempered distributions, the Wightman and Haag–Kastler frameworks, Feynman graphs and their Hopf algebras, and renormalization by extension of distributions. Main results include the Reeh–Schlieder, spin–statistics and PCT theorems under stated hypotheses, Osterwalder–Schrader reconstruction, Haag–Ruelle scattering and the LSZ formula for massive theories, the forest formula and Ward identities, and Shale's implementability theorem.

## RepresentationTheory/LieGroups
Title: Lie groups and the Lie algebra correspondence

Builds the correspondence between Lie groups and Lie algebras: the exponential map, the adjoint representation, the closed-subgroup theorem, the Lie functor and Lie's third theorem. It continues with the structure of compact and reductive groups: maximal tori and the Weyl integration formula, complexification and real forms, the Borel–Weil theorem, and the Cartan, Iwasawa and KAK decompositions with restricted roots.

## RepresentationTheory/LieHighestWeight
Title: Representations of semisimple Lie algebras, highest weight theory, and the Weyl formulas

Develops complements to the highest weight theory of semisimple Lie algebras, building on Verma modules, the Weyl character formula and the Harish-Chandra isomorphism. It proves that Serre's relations present a split semisimple Lie algebra in characteristic zero, constructs explicit models of the exceptional Lie algebras, among them G₂ and F₄ as derivation algebras of the octonions and of the Albert algebra, extends the comparisons of centres of enveloping algebras to reductive Lie algebras such as gl(n), and studies the affine Weyl group acting on the closed fundamental alcove.

## RepresentationTheory/ModularCharactersAndBlocks
Title: Modular characters and blocks of finite groups

Develops the modular representation theory of a finite group at a prime p: p-modular systems, Brauer characters and the decomposition map, projective characters and Brauer reciprocity, blocks over the three coefficient rings, the Brauer homomorphism and defect groups. Its main results are Brauer's three main theorems, the conjugacy of defect groups, and the behaviour of blocks under normal subgroups.

## RepresentationTheory/SpinRepresentations
Title: Clifford algebras, the Pin and Spin groups, and spin representations

Develops Clifford algebras of quadratic spaces, the Pin and Spin double covers of orthogonal groups, and spin and half-spin representations, over the complex numbers and for real forms. Main results are a criterion for Clifford algebra automorphisms to come from isometries, highest-weight descriptions of the spin and half-spin representations, the vector representation in dimension six as an exterior square, comparisons of real and complex spin groups, triality for Spin₈, and Kostant's isotypy theorem and ρ-decomposition for the Clifford algebra of a semisimple Lie algebra.

## RiemannHypothesisForDirichletLFunctions/FiniteReductiveGroups
Title: Finite reductive groups and the characters of GL_n(F_q)

Builds the complex character theory of the finite groups of rational points of connected reductive groups over finite fields: Harish-Chandra induction and series, Gelfand–Graev representations, and Deligne–Lusztig induction through ℓ-adic cohomology, with the inner product formula, Green functions and Lusztig series. For GL_n it gives Green's classification of the irreducible characters, Shintani descent in prime degree, and the depth-zero supercuspidal representations of p-adic GL_n.

## RiemannHypothesisForDirichletLFunctions/HermitianFormsAndLattices
Title: Hermitian forms and lattices

Develops the arithmetic of Hermitian and skew-Hermitian forms over quadratic étale algebras and of their lattices: unitary group schemes and their reductive structure, Witt theory and the local and global classification of Hermitian spaces, and Hermitian lattices over rings of integers with their duals, integral models, genera, class sets and masses. Its main results are the Tamagawa number two of unitary groups, the mass formula, Siegel's main theorem and Hermitian theta series of definite lattices.

## RiemannianGeometry
Title: Curvature, Jacobi fields, submanifolds, and Bochner geometry

Develops Riemannian geometry from curvature onwards: Jacobi fields and index forms, comparison theorems and space forms, isometric immersions with the first and second variation of volume, focal points, and Bochner–Weitzenböck formulas. It also treats Schrödinger-type operators on compact manifolds.

## RiemannianGeometry/MinimalSurfaces
Title: Minimal surfaces

Develops the theory of smooth minimal hypersurfaces in Riemannian manifolds and of minimal surfaces in three-manifolds. Main results include the half-space theorem, ε-regularity and local compactness, the Morse index and stability, the curvature estimate for stable surfaces, removable singularities, Frankel's theorem and the Choi–Schoen compactness theorem.

## RiemannianManifoldsWithConvexBoundary
Title: Riemannian manifolds with convex boundary

Treats the boundary of a Riemannian manifold with boundary as a hypersurface: boundary defining functions, the second fundamental form, and strictly convex, convex and strictly concave boundaries with their characterisation by Hessians. It goes on to geodesics at the boundary, boundary normal coordinates, and the exit time and scattering relation of compact non-trapping manifolds.

## SatoTateGroups
Title: Sato–Tate groups
PR: #1725

Develops Sato–Tate groups as closed subgroups of unitary groups satisfying the axioms of Fité, Kedlaya, Rotger and Sutherland, with moments and event probabilities computed by Weyl integration. Main results are the classifications in degrees two and four, the latter with fifty-seven groups, the Sato–Tate group of an abelian variety built from its ℓ-adic Galois image, with fifty-two of these groups matched to endomorphism types of abelian surfaces, a general statement of the Sato–Tate conjecture, and its proof for elliptic curves with complex multiplication.

## SchattenClassesAndSchurMultipliers
Title: Schatten classes and Schur multipliers
PR: #2421

Builds Schur multipliers on the Schatten classes of L²(Ω, μ) for a σ-finite measure space, from the kernels of Hilbert–Schmidt operators, with their norms and completely bounded norms. Main results include the Grothendieck–Haagerup characterisation, the theorem of Lafforgue and de la Salle that the norm and the completely bounded norm agree on atomless spaces, transference between Fourier and Schur multipliers on ℝⁿ, and the Hörmander–Mikhlin–Schur multiplier theorem.

## SchemeAndStackFoundations
Title: Scheme, stack, cohomology and intersection foundations

Collects the general algebraic geometry on which arithmetic geometry rests. It covers descent, algebraic spaces, torsors and algebraic stacks, and cohomology on the Zariski, étale, fppf and pro-étale sites with coherent duality. It also treats curves, divisors and Picard functors, deformation theory, formal schemes and alterations, and Chow groups with Chern classes and Riemann–Roch.

## SchemeAndStackFoundationsPartII
Title: Scheme and stack foundations, Part II: flat cohomology
PR: #2272

Develops flat cohomology with coefficients in commutative finite locally free group schemes over complete and henselian bases, after Česnavičius–Scholze and Bouthier–Česnavičius. Main results are continuity of flat cohomology over derived complete animated rings with its comparison to ordinary quotients, invariance over henselian pairs, algebraization over topological rings and on punctured spectra, discreteness of completely flat perfectoid modules, and adically faithfully flat descent with supports.

## SchrodingerOperatorsAndSpectralTypes
Title: Schrödinger operators and spectral types
PR: #2424

Defines the absolutely continuous, singular continuous and pure point spectra of a self-adjoint operator and proves criteria for them, including the Kato–Rosenblum theorem on trace-class perturbations. It constructs the self-adjoint Laplace–Beltrami operator of a complete Riemannian manifold (the theorem of Gaffney, Chernoff and Strichartz) with its basic spectral properties, and the Schrödinger operators −Δ + V with bounded real potential on L²(ℝᵈ), with their self-adjointness, cores and essential spectrum.

## SelmerIwasawaCohomology
Title: Selmer groups and Iwasawa cohomology

Builds Selmer groups and Selmer complexes for p-adic Galois representations, compares local conditions under Tate duality, and carries them up cyclotomic towers and towers with group ℤₚᵈ as Iwasawa cohomology, with control and duality theorems. It includes Kummer theory, Selmer groups and the Tate–Shafarevich group of abelian varieties over number fields, structure theorems for ordinary Selmer groups, and a precise statement of the Iwasawa–Greenberg main conjecture.

## SemiRiemannianFoundations
Title: Semi-Riemannian foundations
PR: #3176

Develops scalar products and metrics of every signature and of limited regularity, local bundle connections and curvature, one geodesic flow across regularities with its exponential map and Gauss lemmas, the geometry of nondegenerate immersions, and Jacobi fields with variation theory. Main results are the existence and uniqueness of the Levi-Civita connection of a strong nondegenerate metric on a Banach manifold, the maximal geodesic flow of a connection with locally Lipschitz coefficients, and the regularity of the squared distance function in normal neighbourhoods of a C^{1,1} metric.

## SerreWeightAndLevelOptimisation
Title: Weight and level optimisation of residual modular representations

Starting from a modular two-dimensional residual Galois representation, builds the integral level-changing arguments that bring its level away from the coefficient prime to the full Artin conductor and its weight to the Serre weight: lowering the level away from p, weight optimisation at p, and removing the coefficient prime from the level. It includes odd-characteristic companion forms, the weight-one and Jacobian multiplicity inputs for nonregular modularity lifting, Buzzard's dyadic arguments, and the totally real optimisation theorems used inside the proof of Khare–Wintenberger. Global residual modularity is a hypothesis throughout the general optimisation results.

## SheafConvolutionOnAbelianVarieties
Title: Sheaf convolution on abelian varieties
PR: #1809

Constructs convolution of perverse sheaves on an abelian variety in characteristic zero modulo negligible objects, with twisted cohomological fibre functors and the resulting geometric and arithmetic Tannaka groups, using generic vanishing, Simpson's linearity theorems and the Fourier–Mukai transform for D-modules. Main results are the Euler characteristics and Hodge–Tate multiplicities of smooth ample hypersurfaces, the identification of their convolution groups through characteristic cycles and minuscule representations, generic monodromy for families of twists, a Galois-uniform product theorem, and finiteness of fibres of period maps.

## ShimuraCompactifications
Title: Toroidal compactifications and boundary geometry

Constructs toroidal compactifications of Shimura varieties and their integral models, with the boundary geometry on which automorphic forms, q-expansions and Hecke operators depend. Main results are Pink's toroidal compactification in characteristic zero with its canonical model and map to the Baily–Borel compactification, independence of coherent cohomology from the cone decomposition, degenerations of abelian schemes, integral toroidal and minimal compactifications of PEL Shimura varieties at good primes with the Koecher principle, and Dimitrov's integral compactifications of Hilbert modular varieties with the q-expansion principle.

## ShimuraData
Title: Shimura data, Hermitian domains, and adelic level structures

Builds the Hodge-theoretic and group-theoretic material used with Shimura data: rational weights, Mumford–Tate groups and Hodge-generic abelian varieties, variations of Hodge structure and their polarizations, compact duals over reflex fields, and explicit Hilbert and Siegel data. Its main results are that every connected Shimura datum lifts to a full datum satisfying the additional axioms, and a neatness criterion for certain adelic level subgroups.

## ShimuraVarieties
Title: Complex Shimura varieties and canonical models

Constructs complex Shimura varieties as towers of arithmetic quotients of hermitian symmetric domains, their Baily–Borel compactifications, and canonical models over reflex fields: first the Siegel case by complex multiplication, then Hodge and abelian type, then general Shimura data. It also treats Mumford–Tate groups and the Galois representations of abelian varieties with values in them.

## ShimuraVarietiesPartII
Title: Shimura varieties, Part II: integral models and common Frobenius classes
PR: #2463

Constructs integral models of Hodge-type Shimura varieties with parahoric level, with canonical étale and crystalline tensors and local model diagrams, and descends them to all abelian-type Shimura varieties for p > 2, ramified primes included. On the special fibre it develops Newton strata, the μ-ordinary locus and isogeny groups of points, proving density of the ordinary locus. The main result is Kisin and Zhou's theorem, under their hypotheses, that the ℓ-adic Frobenius classes at a point of the special fibre come from one rational conjugacy class.

## SmallRamificationAndAbelianVarietyBaseCases
Title: Small ramification and the base cases for Serre modularity

Develops the arithmetic results that end the level-one arguments for Serre modularity: bounds turning a small local different into a small global discriminant, and the Tate–Serre base cases in characteristics two and three, where finite subgroup theory rules out an absolutely irreducible representation. For abelian varieties it determines the simple factors and extensions of finite flat torsion and compares growing torsion with a fixed finite-field point count, giving Fontaine's theorem and Schoof's five-prime theorem as geometric base cases. A realisation theorem for weight-two representations brings these back to residual representations and gives a table of terminal weights.

## SmoothRepresentationsOfLocalGroups
Title: Smooth representations of local groups

Builds the smooth representation theory of locally profinite groups over a general coefficient ring, and of reductive p-adic groups in particular: Hecke algebras, parabolic induction and Jacquet functors, admissibility, second adjointness, the Bernstein decomposition and centre, and the Satake isomorphism. These are the local representations and Hecke algebras that the global automorphic theory uses.

## SobolevDifferentialForms
Title: Sobolev spaces of differential forms and the L² de Rham complex

Builds the Sobolev theory of differential forms on Euclidean domains: the weak exterior derivative, the spaces of Lᵖ forms whose weak exterior derivative is in Lᵖ for 1 ≤ p ≤ ∞, pullback under diffeomorphisms and bi-Lipschitz maps, tangential traces, Green's formula and gluing of forms along common boundaries. Main results are the L² de Rham complex as a Hilbert complex with its Hodge decomposition, the Gaffney identity on the cube, and Picard's compactness theorem with closed range of the complex on bounded Lipschitz domains.

## SobolevMapsBetweenManifolds
Title: Sobolev maps between manifolds

Develops first-order Sobolev maps between manifolds: the local class of continuous maps whose chart representatives lie locally in the Sobolev space of exponent p, the weak differential, its norm and, for oriented Riemannian manifolds of equal dimension, the Jacobian. Main results are independence of charts and metrics, chain rules, pullback of differential forms commuting with the exterior derivative, smooth approximation, and a degree for Sobolev maps of exponent n between closed oriented manifolds of dimension n.

## SpectralSequencesAndConvergence
Title: Spectral sequences and convergence

Builds, over an arbitrary abelian category, the language in which a spectral sequence converges: cycle and boundary towers, the limit page, and weak, ordinary and strong convergence to filtered objects in a prescribed set of degrees. It proves the comparison theorem, convergence for filtered complexes under the usual boundedness hypotheses, and Boardman's theorems on conditional convergence of exact couples.

## SpectralSequencesAndConvergencePartII
Title: Spectral sequences and convergence, part II: the standard constructions and their products

Constructs the standard spectral sequences of homological algebra and proves that they converge: the two spectral sequences of a double complex, the hypercohomology and composite-functor spectral sequences, the universal-coefficient, Künneth and change-of-rings spectral sequences, and the Bockstein spectral sequence. It also treats products, with the Leibniz rule on every page.

## StableReduction
Title: Stable reduction of curves and stable maps

Proves stable reduction for curves over a discrete valuation ring: after a finite extension of the base, a stable model exists and is unique. It also defines stable maps to a scheme and their families, with the stability criteria and the stabilization construction that a proof of properness of the moduli space of stable maps requires; the moduli stack itself is not constructed here.

## StableReductionPartII
Title: Stable reduction of curves, Part II
PR: #1841

Develops, building on stable reduction over discrete valuation rings, the explicit geometry of moduli of stable pointed curves over arbitrary bases: tricanonical embeddings, local charts at nodes, adding and contracting markings, Hodge bundles, stable compactifications, Torelli maps and relative Picard functors. Main results identify the universal curve with the moduli of curves with one extra marking, give the integral Noether isomorphism of determinant lines, extend families after finite base change, and prove positivity of the Hodge bundle under maximal variation.

## StackPointsAndResidualGerbes
Title: Points of algebraic stacks, stabilisers and residual gerbes

Develops the local structure of an algebraic stack at a point, in the conventions of the Stacks Project: substacks, finite type and closed points, automorphism groups, gerbes, and the residual gerbe at a point with its existence theorems. Its main results identify the residual gerbe at a rational point with the classifying stack of the automorphism group, and relate the tangent space to the normal space at a closed rational point.

## SurfaceGroupCharacterVarieties
Title: Surface group character varieties
PR: #2430

Constructs the outer action of the mapping class group of a punctured surface on its fundamental group, the representation scheme of a finitely generated group, and the character variety of such a group in a real reductive group, the space of reductive representations modulo conjugation. Main results are that the character variety is Hausdorff, locally compact and second countable, that for complex groups it is homeomorphic to the complex points of the affine quotient, and that the mapping class group acts on it by homeomorphisms.

## SurfaceTopology
Title: Surface topology, finite presentations, and classification
PR: #271

Develops finite presentations of compact surfaces by triangulations and by generalized maps, given by three involutions on a finite set, and proves that these determine and are determined by the surface. Main results are the realization theorem, the Heffter–Edmonds–Ringel correspondence between cellular graph embeddings and rotation systems, polygonal normal forms, and the classification of compact surfaces with boundary by Euler characteristic, orientability and number of boundary components. Further parts treat simplicial homology, the Dehn–Lickorish theorem, the planarity theorems of Kuratowski and Fáry, and the five-colour theorem.

## SymmetricHyperbolicSystems
Title: Linear symmetric hyperbolic systems
PR: #2246

Develops the classical theory of linear first-order systems on ℝ × ℝⁿ that are symmetric hyperbolic in the sense of Friedrichs, by Friedrichs' energy method and his finite difference scheme, without Fourier analysis or Sobolev spaces. For smooth coefficients with bounded derivatives and smooth compactly supported data, main results are existence of a C¹ solution of the Cauchy problem, uniqueness with a domain of dependence and explicit propagation speed, the L² energy estimate, and convergence of the scheme under the Courant–Friedrichs–Lewy condition.

## SymplecticGeometry/CotangentLagrangian
Title: Cotangent bundles and Lagrangian geometry

Develops the symplectic geometry of cotangent bundles and Lagrangian submanifolds: the cotangent bundle as a phase space, embedded Lagrangians, generating functions and the canonical transformations they define, and neighbourhood theorems for symplectic germs along a submanifold. Convex planar billiards appear as an example of a map given by a generating function.

## TaubesGromov
Title: Taubes–Gromov theory

Constructs Taubes's integer count of embedded pseudoholomorphic curves in a closed symplectic four-manifold and relates it to the Seiberg–Witten invariant through vortices and the monopole equations with a large parameter. It includes the normal operators of embedded curves and an application to mapping tori of surfaces.

## TeichmullerGeometry
Title: Teichmüller geometry of closed surfaces
PR: #1169

Builds the Teichmüller theory of a closed oriented surface of genus at least two: the space of marked complex structures with its complex structure of dimension 3g − 3, the action of the mapping class group and the Dehn–Nielsen–Baer theorem, Fenchel–Nielsen coordinates, the Teichmüller metric, and the Nielsen realization theorem. Its final results are that the marked hyperbolic surfaces with trivial isometry group, those with nonarithmetic uniformizing group, and those whose uniformizing group is maximal among discrete subgroups of PGL₂(ℝ) each form an open dense subset of Teichmüller space.

## TracesOnCStarAlgebras
Title: Traces on C\*-algebras and their trace ideals

Develops possibly unbounded traces on C\*-algebras in Dixmier's sense, with their domain ideals, lower semicontinuity, semifiniteness, and the trace ideals of elements b with |b|ᵖ of finite trace. Main results are Combes's theorem, Dixmier's theorem extending a semifinite lower semicontinuous trace to a faithful normal semifinite trace on the generated von Neumann algebra, Hölder inequalities for trace ideals, invariance of K-theory under passage to trace ideals, and, for AF algebras, a bijection between densely defined lower semicontinuous traces and positive homomorphisms from K₀ to ℝ.

## TwistedAutomorphicDescents
Title: Twisted automorphic descents and cuspidal automorphic modules

Develops the twisted automorphic descent of Jiang and Zhang for special orthogonal and unitary groups over number fields: Bessel–Fourier coefficients of leading residues of Eisenstein series, unfolding of Bessel–Eisenstein integrals, and their factorization into local integrals. Main results are that a nonzero Bessel period forces a nonzero central L-value, the converse under a weak Fourier support hypothesis, and recovery of a prescribed cuspidal automorphic representation, up to outer automorphism, from regular or subregular Fourier support, with conjectural inputs kept as explicit hypotheses.

## VariationalMethods
Title: Variational methods and constrained spectral theory

Develops the link between weak compactness in Banach spaces, minimization of quadratic energies and self-adjoint operators on Hilbert space, for a form domain compactly and densely embedded in a Hilbert space. Main results are the direct method of the calculus of variations, constrained Rayleigh minimizers with their Euler–Lagrange equation, an orthonormal eigenbasis with eigenvalues tending to infinity, the Courant–Fischer min–max principle on the form domain, compact resolvent and spectrum of the associated operator, and convergence of Ritz–Galerkin approximations.

## Varifolds
Title: Varifolds

Builds the theory of k-dimensional varifolds on open subsets of a Riemannian manifold, in the generality of Allard: Radon measures on the Grassmann bundle, their first variation, and stationary, rectifiable and integral varifolds. Main results are the monotonicity formula, Allard's rectifiability theorem, the compactness theorems for rectifiable and integral varifolds, tangent cones and the constancy theorem.

## VirtualFundamentalClass
Title: The Behrend–Fantechi virtual fundamental class

Carries out the construction of Behrend and Fantechi: the intrinsic normal cone of a Deligne–Mumford stack, obstruction theories, and the virtual fundamental class of a perfect obstruction theory with a global resolution, shown to be independent of all choices. Along the way it builds rational Chow groups, Gysin maps and degrees of zero-cycles for separated Deligne–Mumford stacks, and a relative version of the class.

## VirtualFundamentalClassPartII
Title: Virtual fundamental classes, part II: integral and non-separated Chow theory of Deligne–Mumford stacks and virtual classes over general bases
PR: #2446

Extends the Chow theory of Deligne–Mumford stacks to integral coefficients and to stacks that need not be separated, with the intersection ring of a smooth stack, the comparison with the moduli space, and the degree of the residual gerbe at a closed point. It defines the virtual class without the resolution property, proves deformation invariance of virtual counts, and constructs the perfect obstruction theory of spaces of maps from curves.

## VonNeumannAlgebras
Title: Von Neumann algebras, factors, and modular theory

Develops the theory of von Neumann algebras: operator topologies, preduals and normality, projection comparison, standard forms, Hilbert modules with coupling constant and index, group algebras and crossed products, Tomita–Takesaki theory, weights, Connes's invariants and ultraproducts. Main results are the bicommutant and Kaplansky density theorems, existence and uniqueness of the trace on a II₁ factor, the Tomita–Takesaki theorem, Connes's classification of type III factors, Dye's theorem, and the equivalence of injectivity with hyperfiniteness together with the classification of injective factors.

## WeightsInEtaleCohomology
Title: Weights in étale cohomology: arithmetic cohomology and eigenform applications

Connects weight theorems to the arithmetic representations that occur in good reduction, modular forms and local comparison theorems, building the comparisons that identify Frobenius on a representation with Frobenius on a geometric fibre and fixing the coefficient and Tate-twist conventions. It treats good reduction of curves and abelian varieties, specialization and degeneration models with Picard–Lefschetz normalization, pencils over finite fields, and arithmetic cohomology with projectors, including parabolic purity and hard Lefschetz. The applications to eigenforms are Ramanujan bounds and the local polynomials of a fixed form at good primes.

## WeilConjectures
Title: Weil conjectures and cohomological zeta functions

Relates point counts over finite fields to the zeta function and its cohomological factors, and assembles the Weil conjectures for a smooth proper scheme over a finite field: integral factors independent of ℓ, the absolute values of the reciprocal roots, and the functional equation. It also contains explicit calculations for curves and surfaces, among them the definition and numerical invariants of Enriques surfaces.

## YangMillsConnectionsAndCaloricGauge
Title: Yang–Mills connections on Euclidean space and the caloric gauge

Develops connections on Euclidean space with values in a compact Lie group at critical regularity: Sobolev gauge transformations, Uhlenbeck's Coulomb gauge, the good global gauge theorem, and the topological class and instanton number of a finite-energy connection. It then treats harmonic Yang–Mills connections on ℝ⁴ (energy gap and ground state), the Yang–Mills heat flow, and the caloric gauge of Oh and Tataru, ending with the theorem that the caloric connections form a C¹ submanifold of a Banach space.

## #2489
Title: SchemeAndStackFoundations: cohomologically affine morphisms

Extends the merged roadmap SchemeAndStackFoundations with a section on cohomologically affine morphisms of algebraic stacks (quasi-compact, quasi-separated, with exact quasi-coherent pushforward) and linearly reductive group schemes over a base, with flat base change, Serre's affineness criterion and the comparison with complete reducibility of comodules over a field; it adds no roadmap.

## #2490
Title: GeometricCurrents: Lipschitz chains in metric spaces, mass and filling volume

Extends the merged roadmap GeometricCurrents, on integral currents and minimizing hypersurfaces in Riemannian manifolds, with Lipschitz singular chains in an arbitrary metric space, the mass of a chain measured with Hausdorff measure counted with multiplicity, the area formula on Riemannian manifolds, and the filling volume of a cycle and the filling volume function of a space.

## #2491
Title: MinimalSurfaces: stability across a singular set and strict stability

Extends the merged roadmap RiemannianGeometry/MinimalSurfaces with item 7.8: stability and weighted strict stability of a smooth hypersurface tested by ambient functions that cross the singular set of its closure, the reduction of strict stability to a weighted Hardy-type inequality, and the criterion that a minimal cone is strictly stable exactly when the lowest eigenvalue of its link satisfies λ₁ + ((n−2)/2)² > 0, following Simon's papers on stable minimal hypersurfaces with prescribed singular sets.

## #2529
Title: AnalyticStableMaps: the normal Cauchy–Riemann operator

Extends the merged roadmap AnalyticStableMaps, on moduli spaces of stable pseudoholomorphic maps, with the generalized tangent and normal bundles of a nonconstant closed pseudoholomorphic curve through its critical points, the normal Cauchy–Riemann operator with its Fredholm theory and index, its behaviour under branched covers, and Wendl's notion of a super-rigid curve.

## #2531
Title: SchemeAndStackFoundations: quasi-affine descent, quasi-finite spaces and fppf cohomology with supports

Extends the merged roadmap SchemeAndStackFoundations with effective fppf descent of affine, quasi-affine and separated locally quasi-finite morphisms, separated locally quasi-finite algebraic spaces over a scheme, and cohomology on the big fppf site with coefficients in the larger universe, including fppf cohomology with supports in a closed subset with its long exact sequence and excision; it adds no roadmap.

## #2536
Title: ComplexKahlerGeometry: soft-sheaf acyclicity from SmoothBundlesConnections, Čech refinement maps from Tau Ceti

Revises the merged roadmap ComplexKahlerGeometry so that the acyclicity of soft sheaves is taken from SmoothBundlesConnections B6.1 and the Čech refinement maps from existing Tau Ceti code, rather than restated; it adds no roadmap.
