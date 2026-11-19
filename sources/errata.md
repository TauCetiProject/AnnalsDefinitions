# Errata for the definition texts

Known mathematical errors in [`definitions_100_v2_textbook.md`](definitions_100_v2_textbook.md),
which is kept verbatim. Line numbers refer to that file.

## Proposition 13.3(a): the vanishing ideal is not a Hopf ideal

- **Where:** l.612 (Proposition 13.3(a)) and l.637 (the remark for formalisers).
- **Claim:** `I_V`, the ideal of functions vanishing on `h(ℂ^×)`, is a Hopf ideal, so `MT(V)` is
  `Spec ℚ[GL_V]/I_V`.
- **Correction:** `MT(V)` is cut out by the largest Hopf ideal contained in `I_V`; the `ℚ`-closure
  of `h(ℂ^×)` need not be a group.
- **Evidence:** for `V = ℚ(ζ₅)` with `h` acting by `z/z̄` on one complex place, the `ℚ`-closure is
  `(U(1) × 1) ∪ (1 × U(1))`; merged ShimuraVarieties §P.3a states this as a Check.

## Theorem 10.5: the unnormalised HKR map needs `n!` invertible

- **Where:** l.485 to l.487.
- **Claim:** the unnormalised HKR map `T^n_{R/k} → HH^n(R,R)` is an isomorphism over any field.
- **Correction:** it is `n!` times the canonical isomorphism, so it is an isomorphism exactly when
  `n!` is invertible on `T^n_{R/k}`.
- **Evidence:** for `R = 𝔽₂[x,y]`, `n = 2` it is zero on `HH²`; open
  https://github.com/TauCetiProject/TauCetiRoadmap/pull/2447 "HochschildHomologyAndHKR: roadmap"
  §7.5 states the theorem for the canonical map.

## Definition 85.6: the function-field height is not invariant under base change

- **Where:** l.2899, repeated in Remark (4).
- **Claim:** `h_Fal(A_L) = h_Fal(A)` for every finite `L/K`, in the function-field case too.
- **Correction:** over a function field `h_Fal(A_L) = [L:K]·h_Fal(A)`; only independence of the
  auxiliary `K'` holds.
- **Evidence:** open https://github.com/TauCetiProject/TauCetiRoadmap/pull/1833
  "ArakelovGeometryAndAbelianHeightsPartII: roadmap" §13.1 states this scaling.
