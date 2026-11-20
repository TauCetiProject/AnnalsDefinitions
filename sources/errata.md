# Errata for the definition texts

Known mathematical errors in [`definitions_100_v2_textbook.md`](definitions_100_v2_textbook.md),
which is kept verbatim. Line numbers refer to that file.

## Proposition 13.3(a): the vanishing ideal is not a Hopf ideal

- **Where:** l.606 to l.608 (Definition 13.2), l.612 (Proposition 13.3(a)) and l.637.
- **Claim:** `I_V`, the ideal of rational functions vanishing on `h(ℂ^×)`, is a Hopf ideal, so
  `MT(V) = Spec ℚ[GL_V]/I_V` is the `ℚ`-Zariski closure of `h(ℂ^×)`.
- **Correction:** `MT(V)` is cut out by the largest Hopf ideal contained in `I_V`; the `ℚ`-closure
  of `h(ℂ^×)` need not be a group. The description as the intersection of all algebraic subgroups
  containing `h(ℂ^×)` is correct.
- **Evidence:** `V = ℚ(ζ₅)`, `h(z)` multiplying by `z/z̄` at one complex place and trivially at the
  other (weight 0). The `ℚ`-closure is the union of a one-dimensional torus and its Galois
  conjugate, over `ℝ` the set `(U(1) × 1) ∪ (1 × U(1))`, which is not a subgroup; `MT(V)` is the
  norm-one torus of `ℚ(ζ₅)/ℚ(√5)`. Merged ShimuraVarieties §P.3a works this example as a Check.

## Theorem 10.5: the unnormalised HKR map is `n!` times the canonical isomorphism

- **Where:** l.485 to l.486.
- **Claim:** the unnormalised HKR map induces an isomorphism `T^n_{R/k} → HH^n(R,R)` over any field.
- **Correction:** it induces `n!` times the isomorphism `D₁∧⋯∧D_n ↦ [D₁∪⋯∪D_n]` (as Remark (1)
  records), so it is an isomorphism exactly when multiplication by `n!` is bijective on
  `T^n_{R/k}`. Injectivity on cochains (l.487) holds as stated.
- **Evidence:** for `R = 𝔽₂[x,y]`, `n = 2`, the cocycle `⟨∂_x, ∂_y⟩` is the coboundary of
  `∂_x∂_y`, so the induced map `T² → HH²` is zero although `T² ≅ HH² ≅ R`. Open
  https://github.com/TauCetiProject/TauCetiRoadmap/pull/2447 "HochschildHomologyAndHKR: roadmap"
  works this example in §7.5 and states the theorem for the canonical map in §9.2.

## Definition 85.6: the function-field height scales under base change

- **Where:** l.2899; Remark (4) (l.2901) calls the normalisation "absolute".
- **Claim:** `h_Fal(A_L) = h_Fal(A)` for every finite `L/K`, in the function-field case too.
- **Correction:** over a function field, with `k` fixed, `h_Fal(A_L) = [L:K]·h_Fal(A)` for every
  finite `L/K`. Independence of the auxiliary `K'` holds, and so does invariance in the number-field
  case.
- **Evidence:** on a common semistable extension `M ⊇ L`, both heights are `deg_{B_M/k}(ω_M)`
  divided by `[M:K]` and `[M:L]` respectively. Open
  https://github.com/TauCetiProject/TauCetiRoadmap/pull/1833
  "ArakelovGeometryAndAbelianHeightsPartII: roadmap" §13.1 states this scaling for curves of genus
  at least 2.
