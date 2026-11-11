---
title: "100 definitions for Tau Ceti: textbook versions"
subtitle: "Definitions needed to state the main theorems of 157 Annals of Mathematics papers (2020–2026)"
date: "October 2026"
geometry: margin=2.5cm
toc: true
toc-depth: 2
colorlinks: true
---

# About this document {-}

Each entry gives one of the 100 definitions in `definitions_100_v2` as it might appear in a textbook: the precise definition, together with only the background from the same chapter that is needed for it to make sense (auxiliary definitions, and statements of results needed for well-definedness). Material from earlier chapters is assumed. Entry numbers match `definitions_100_v2.md`, which records for each definition what already exists in Mathlib or Tau Ceti and which papers need it; "Definition #n" refers to entry n. Papers are cited as [year, volume(issue), no. number].

These texts were drafted by AI agents from the papers and standard sources and have not yet been reviewed by a human.

# Algebra, representation theory & homotopy theory

## 1. Real rank of a semisimple Lie group

*Chapter context.* This is the chapter on restricted roots in a text on the structure theory of real semisimple Lie groups (in the style of Knapp, *Lie Groups Beyond an Introduction*, Ch. VI, or Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Ch. V). The reader already knows real semisimple Lie algebras and the Killing form $B$, and knows Cartan involutions: an involutive automorphism $\theta$ of $\mathfrak g$ such that $B_\theta(X,Y):=-B(X,\theta Y)$ is positive definite. Such a $\theta$ exists, and any two are conjugate under $\mathrm{Int}(\mathfrak g)$. The reader also knows the Cartan decomposition $\mathfrak g=\mathfrak k\oplus\mathfrak p$ into the $(+1)$- and $(-1)$-eigenspaces of $\theta$, and Lie groups with their Lie algebras and analytic subgroups. Maximal abelian subspaces of $\mathfrak p$ and the real rank are defined here.

Throughout, $\mathfrak g$ is a finite-dimensional real semisimple Lie algebra, $\theta$ is a Cartan involution of $\mathfrak g$, and $\mathfrak g=\mathfrak k\oplus\mathfrak p$ is the corresponding Cartan decomposition. Thus $[\mathfrak k,\mathfrak k]\subseteq\mathfrak k$, $[\mathfrak k,\mathfrak p]\subseteq\mathfrak p$ and $[\mathfrak p,\mathfrak p]\subseteq\mathfrak k$.

**Definition 1.1.** A *maximal abelian subspace of $\mathfrak p$* is a real linear subspace $\mathfrak a\subseteq\mathfrak p$ such that $[X,Y]=0$ for all $X,Y\in\mathfrak a$, and which is maximal under inclusion among the linear subspaces of $\mathfrak p$ with this property. Such subspaces exist because $\dim\mathfrak g<\infty$. Note that $\mathfrak a=0$ is allowed; this happens exactly when $\mathfrak p=0$.

**Theorem 1.2 (conjugacy of maximal abelian subspaces).** Let $K_\theta\subseteq\mathrm{Int}(\mathfrak g)$ be the connected Lie subgroup with Lie algebra $\operatorname{ad}_{\mathfrak g}(\mathfrak k)$.

1. If $\mathfrak a,\mathfrak a'$ are maximal abelian subspaces of $\mathfrak p$, then $k(\mathfrak a')=\mathfrak a$ for some $k\in K_\theta$. Moreover $\mathfrak p=\bigcup_{k\in K_\theta}k(\mathfrak a)$.
2. If $\theta'=\varphi\theta\varphi^{-1}$ with $\varphi\in\mathrm{Int}(\mathfrak g)$ is another Cartan involution, then $\varphi$ carries $\mathfrak p$ onto $\mathfrak p'$, the $(-1)$-eigenspace of $\theta'$. It also carries maximal abelian subspaces of $\mathfrak p$ onto maximal abelian subspaces of $\mathfrak p'$.

Consequently $\dim_{\mathbb R}\mathfrak a$ is the same for every Cartan involution of $\mathfrak g$ and every maximal abelian subspace $\mathfrak a$ of the corresponding $\mathfrak p$. (Knapp, op. cit., Ch. VI; Helgason, op. cit., Ch. V.)

**Proposition 1.3 (restricted roots).** Let $\mathfrak a\subseteq\mathfrak p$ be maximal abelian. Each operator $\operatorname{ad}H$, for $H\in\mathfrak a$, is self-adjoint for $B_\theta$, and these operators commute. So $\mathfrak g=\mathfrak g_0\oplus\bigoplus_{\lambda\in\Sigma}\mathfrak g_\lambda$, where $\mathfrak g_\lambda=\{X\in\mathfrak g:[H,X]=\lambda(H)X\ \forall H\in\mathfrak a\}$. Here $\Sigma=\Sigma(\mathfrak g,\mathfrak a)$ is the finite set of nonzero $\lambda\in\mathfrak a^*$ with $\mathfrak g_\lambda\neq0$, and $\mathfrak g_0=Z_{\mathfrak k}(\mathfrak a)\oplus\mathfrak a$. The set $\Sigma$ is a root system in $\mathfrak a^*$, possibly non-reduced (of type $BC$), and it spans $\mathfrak a^*$.

**Definition 1.4 (real rank).**

1. The *real rank* of $\mathfrak g$ is the non-negative integer
$$\operatorname{rank}_{\mathbb R}(\mathfrak g):=\dim_{\mathbb R}\mathfrak a ,$$
where $\mathfrak a$ is any maximal abelian subspace of $\mathfrak p$ for any Cartan decomposition $\mathfrak g=\mathfrak k\oplus\mathfrak p$. By Theorem 1.2 this does not depend on the choices.

2. Let $G$ be a real Lie group whose Lie algebra $\mathrm{Lie}(G)$ is semisimple. Its *real rank* (also written $\mathbb R$-rank or $\mathbb R\text{-}\mathrm{rank}(G)$) is $\operatorname{rank}_{\mathbb R}(G):=\operatorname{rank}_{\mathbb R}(\mathrm{Lie}(G))$. It depends only on the Lie algebra. So it is unchanged under passing to coverings, to quotients by discrete central subgroups, and to open subgroups.
3. *Factors.* Let $G$ be a connected semisimple Lie group, and let $\mathrm{Lie}(G)=\mathfrak g_1\oplus\dots\oplus\mathfrak g_s$ be the (unique) decomposition into simple ideals. The *almost-simple factors* of $G$ are the connected normal Lie subgroups $G_i$ with Lie algebra $\mathfrak g_i$. A factor $G_i$ is *compact* if $\mathfrak g_i$ is a compact Lie algebra, that is, if $B|_{\mathfrak g_i}$ is negative definite. One has
$$\operatorname{rank}_{\mathbb R}(G)=\sum_{i=1}^s\operatorname{rank}_{\mathbb R}(\mathfrak g_i),$$
and $\operatorname{rank}_{\mathbb R}(\mathfrak g_i)=0$ if and only if $\mathfrak g_i$ is compact. $G$ has *higher rank* if $\operatorname{rank}_{\mathbb R}(G)\ge2$.

The additivity in (3) holds because every Cartan involution preserves each simple ideal. Then $\mathfrak p=\bigoplus_i(\mathfrak p\cap\mathfrak g_i)$, and $\mathfrak a=\bigoplus_i\mathfrak a_i$ with $\mathfrak a_i$ maximal abelian in $\mathfrak p\cap\mathfrak g_i$.

*Remarks.*

(1) *Equivalent descriptions.*
* Root systems: since $\Sigma(\mathfrak g,\mathfrak a)$ spans $\mathfrak a^*$, $\operatorname{rank}_{\mathbb R}(\mathfrak g)$ is the rank of the restricted root system.
* Algebraic groups (Borel--Tits): let $\mathbf H$ be a connected semisimple linear algebraic group over $\mathbb R$, and let $G$ be an open subgroup of $\mathbf H(\mathbb R)$, e.g. $\mathbf H(\mathbb R)^0$. Then $\operatorname{rank}_{\mathbb R}(G)$ is the dimension of a maximal $\mathbb R$-split torus of $\mathbf H$. For instance $\mathfrak a$ may be taken to be the Lie algebra of $\mathbf S(\mathbb R)$ for a suitable maximal $\mathbb R$-split torus $\mathbf S$.
* Symmetric spaces: for $G$ connected with finite centre and $K$ maximal compact, $\operatorname{rank}_{\mathbb R}(G)$ is the rank of the Riemannian symmetric space $X=G/K$. This is the maximal dimension of a flat, i.e. a complete totally geodesic submanifold isometric to a Euclidean space. The maximal flats through $eK$ are the orbits $\exp(\mathfrak a)\cdot eK$.
* Complex rank: $\operatorname{rank}_{\mathbb R}(\mathfrak g)\le\operatorname{rank}_{\mathbb C}(\mathfrak g_{\mathbb C})$, with equality exactly when $\mathfrak g$ is split.

(2) *Examples.* $\operatorname{rank}_{\mathbb R}\mathrm{SL}(n,\mathbb R)=n-1$, where $\mathfrak a$ is the traceless diagonal matrices. $\operatorname{rank}_{\mathbb R}\mathrm{SL}(n,\mathbb C)=n-1$, viewed as a real group. $\operatorname{rank}_{\mathbb R}\mathrm{Sp}(2n,\mathbb R)=n$. $\operatorname{rank}_{\mathbb R}\mathrm{SO}(p,q)=\operatorname{rank}_{\mathbb R}\mathrm{SU}(p,q)=\min(p,q)$. $\operatorname{rank}_{\mathbb R}\mathrm{Sp}(n,1)=1$. Compact groups have real rank $0$.

(3) *Reductive variant.* For a connected reductive $\mathbb R$-group $\mathbf H$, the $\mathbb R$-rank is the dimension of a maximal $\mathbb R$-split torus. This equals $\operatorname{rank}_{\mathbb R}$ of the derived group plus the dimension of the maximal $\mathbb R$-split central torus. Some authors instead use the semisimple rank, i.e. the rank of the derived group. The Annals papers below only use semisimple $G$, where no ambiguity arises.

(4) *Use in the Annals papers.*
* [2021, 193(3), no. 2]: $G$ is connected, centre-free and semisimple without compact factors, and $k=\mathbb R\text{-}\mathrm{rank}(G)\ge3$, which equals the rank of $X=G/K$.
* [2022, 196(3), no. 1]: $G$ is connected semisimple with finite centre, and every non-compact almost-simple factor has real rank $\ge2$. There $\dim_{\mathbb R}\mathfrak a$ is called the real rank.
* [2022, 196(3), no. 2]: $G$ is connected semisimple with finite centre, of $\mathbb R$-rank $\ge2$. The almost-simple factors of real rank $1$ enter the definition of a "higher-rank lattice".
* [2023, 197(1), no. 6]: $G$ is connected, centre-free and simple, of real rank $\ge2$.

## 2. p-block (Brauer block) of a finite group

*Chapter context.* This is the opening chapter on block theory in a text on modular representation theory of finite groups (in the style of Navarro, *Characters and Blocks of Finite Groups*, or Linckelmann, *The Block Theory of Finite Group Algebras*). The reader knows ordinary character theory: $\mathrm{Irr}(G)$, central characters, and the central primitive idempotents $e_\chi=\frac{\chi(1)}{|G|}\sum_{g\in G}\chi(g^{-1})g$. The reader also knows complete discrete valuation rings, idempotent lifting, and group algebras $RG$ over a commutative ring $R$. Blocks are defined here.

Throughout, $G$ is a finite group and $p$ is a prime ($p$ need not divide $|G|$).

**Definition 2.1 ($p$-modular system).** A *$p$-modular system* is a triple $(K,\mathcal O,k)$ with the following properties.

* $\mathcal O$ is a complete discrete valuation ring with maximal ideal $J(\mathcal O)$.
* $K=\mathrm{Frac}(\mathcal O)$ has characteristic $0$.
* $k=\mathcal O/J(\mathcal O)$ has characteristic $p$.

It is *large enough for $G$* if $K$ contains a primitive $e$-th root of unity, where $e$ is the exponent of $G$. Then $KG$ is split semisimple. We write $\mathrm{Irr}(G)$ for the characters of the simple $KG$-modules. Choosing a field embedding of $\mathbb Q(\zeta_e)$ into $\mathbb C$ identifies $\mathrm{Irr}(G)$ with the complex irreducible characters. Every $\chi\in\mathrm{Irr}(G)$ is extended $K$-linearly to $KG$.

**Proposition 2.2.** Let $(K,\mathcal O,k)$ be a $p$-modular system.

1. The $G$-conjugacy class sums $\hat C=\sum_{g\in C}g$ form an $\mathcal O$-basis of $Z(\mathcal OG)$ and a $k$-basis of $Z(kG)$. Hence reduction modulo $J(\mathcal O)$ is a surjection $Z(\mathcal OG)\to Z(kG)$.
2. Since $\mathcal O$ is complete, this map induces a bijection $b\mapsto\bar b$ from the primitive idempotents of the commutative ring $Z(\mathcal OG)$ onto those of $Z(kG)$.
3. There are finitely many primitive idempotents $b_1,\dots,b_t$ of $Z(\mathcal OG)$. They are pairwise orthogonal, $b_ib_j=0$ for $i\ne j$, and they satisfy $1=b_1+\dots+b_t$. Hence $\mathcal OG=\prod_i\mathcal OGb_i$ as $\mathcal O$-algebras, and each factor is indecomposable.

**Definition 2.3 ($p$-blocks).** Fix a $p$-modular system $(K,\mathcal O,k)$ large enough for $G$.

1. A *$p$-block* (or *Brauer $p$-block*, or *block*) of $G$ is a primitive idempotent $b$ of the commutative ring $Z(\mathcal OG)$. Equivalently, via Proposition 2.2(2), it is a primitive idempotent $\bar b$ of $Z(kG)$. Such a $b$ is called a *block idempotent*, and $\mathcal OGb$ (resp. $kG\bar b$) is the *block algebra*.
2. The set of ordinary irreducible characters *in* $b$ is
$$\mathrm{Irr}(G,b)=\mathrm{Irr}(b):=\{\chi\in\mathrm{Irr}(G):\chi(b)\neq0\}=\{\chi\in\mathrm{Irr}(G): e_\chi b=e_\chi\}.$$
For each $\chi$, either $e_\chi b=e_\chi$ (and then $\chi(b)=\chi(1)$) or $e_\chi b=0$ (and then $\chi(b)=0$).

3. A finitely generated $kG$-module $V$ *belongs to* $b$ if $\bar bV=V$, equivalently $\bar b'V=0$ for every block $b'\neq b$. In particular a simple $kG$-module belongs to exactly one block. $\mathrm{IBr}(G,b)$ denotes the irreducible Brauer characters of the simple $kG$-modules belonging to $b$.
4. For $\chi\in\mathrm{Irr}(G)$, $\mathrm{bl}(\chi)$ denotes the unique block $b$ with $\chi\in\mathrm{Irr}(G,b)$. The *principal block* $b_0(G)$ is $\mathrm{bl}(1_G)$.

By 2.2(3), $\mathrm{Irr}(G)=\bigsqcup_{b}\mathrm{Irr}(G,b)$ and $\mathrm{IBr}(G)=\bigsqcup_b\mathrm{IBr}(G,b)$, and each $\mathrm{Irr}(G,b)$ is non-empty. In terms of idempotents, $b=\sum_{\chi\in\mathrm{Irr}(G,b)}e_\chi$ in $KG$. So a block is determined by the set $\mathrm{Irr}(G,b)$, and one often identifies the two, writing $B$ for either.

**Proposition 2.4 (Brauer's criterion via central characters).** For $\chi\in\mathrm{Irr}(G)$ let $\omega_\chi\colon Z(KG)\to K$ be its central character, $\omega_\chi(\hat C)=|C|\chi(g_C)/\chi(1)$ with $g_C\in C$. Then $\omega_\chi(Z(\mathcal OG))\subseteq\mathcal O$. Let $\lambda_\chi\colon Z(kG)\to k$ be its reduction modulo $J(\mathcal O)$. Two characters $\chi,\psi\in\mathrm{Irr}(G)$ lie in the same block if and only if $\lambda_\chi=\lambda_\psi$, i.e. $\omega_\chi(\hat C)\equiv\omega_\psi(\hat C)\pmod{J(\mathcal O)}$ for every conjugacy class $C$ of $G$. The block of $\chi$ is the unique $b$ with $\lambda_\chi(\bar b)=1$.

*Remarks.*

(1) *Formulation over $\mathbb C$ (as in Navarro's book).* Let $R\subset\mathbb C$ be the ring of algebraic integers and $M\supset pR$ a maximal ideal. Define $\chi\sim\psi$ if $\omega_\chi(\hat C)\equiv\omega_\psi(\hat C)\pmod M$ for all classes $C$. The equivalence classes are exactly the sets $\mathrm{Irr}(G,b)$ above, for the $p$-modular system with $K$ the completion of $\mathbb Q(\zeta_e)\subset\mathbb C$ at the prime $M\cap\mathbb Z[\zeta_e]$. The resulting partition of $\mathrm{Irr}(G)$ does not depend on the choice of $M$. This formulation needs no $p$-adic rings and is often the most convenient one to formalise.

(2) *Basic facts.* If $p\nmid|G|$, every block contains exactly one $\chi$. Blocks of a direct product $G_1\times G_2$ are the products $b_1\otimes b_2$. "Large enough" only matters for the identification with $\mathrm{Irr}(G)$. Without it one still has blocks of $\mathcal OG$, but $\mathrm{Irr}(G,b)$ must then be read after extending scalars, and blocks may split.

(3) *Decomposition matrix.* For $\chi\in\mathrm{Irr}(G)$, its restriction to the $p$-regular elements is $\chi^0=\sum_{\varphi\in\mathrm{IBr}(G)}d_{\chi\varphi}\varphi$, with $d_{\chi\varphi}\in\mathbb Z_{\ge0}$. Here $d_{\chi\varphi}\neq0$ forces $\mathrm{bl}(\chi)=\mathrm{bl}(\varphi)$. So the decomposition matrix is block diagonal, and the *decomposition matrix of $b$* is $(d_{\chi\varphi})_{\chi\in\mathrm{Irr}(G,b),\varphi\in\mathrm{IBr}(G,b)}$.

(4) *Use in the Annals papers.*
* [2024, 200(2), no. 4] and [2025, 201(2), no. 2] use Definition 2.3 for arbitrary finite $G$, together with $\mathrm{Irr}(B)$ or $\mathrm{Irr}(G,b)$. The latter paper writes $\ell$ for the prime and fixes "an $\ell$-modular system large enough for $G$".
* [2020, 192(2), no. 7] uses $\ell$-blocks of finite reductive groups $G=\mathbf G^F$ with $\ell\neq p=\operatorname{char}$. A *unipotent $\ell$-block* is a block $b$ with $\mathrm{Irr}(G,b)$ containing at least one unipotent character. "The decomposition matrix of the unipotent $\ell$-blocks" is the submatrix of (3) with rows in $\bigcup_b\mathrm{Irr}(G,b)$ and columns in $\bigcup_b\mathrm{IBr}(G,b)$, both over the unipotent blocks $b$.

## 3. Defect group of a block

*Chapter context.* This is the chapter on defect groups in a text on block theory of finite groups (in the style of Linckelmann, *The Block Theory of Finite Group Algebras*, Thévenaz, *$G$-Algebras and Modular Representation Theory*, or Navarro, *Characters and Blocks of Finite Groups*). The reader knows $p$-modular systems $(K,\mathcal O,k)$ and $p$-blocks $b$ of a finite group $G$ (Definition #2), Sylow theory, and group algebras. The relative trace map and the Brauer homomorphism are introduced here.

Throughout, $G$ is a finite group and $(K,\mathcal O,k)$ is a $p$-modular system large enough for $G$. Let $A$ be $\mathcal OG$ or $kG$. The group $G$ acts on $A$ by conjugation, $^g x:=gxg^{-1}$.

**Definition 3.1 (fixed points and relative traces).**

1. For a subgroup $H\le G$, put $A^H:=\{x\in A: {}^hx=x\ \forall h\in H\}$. This is the centraliser of $H$ in $A$, a subalgebra, and $A^G=Z(A)$.
2. For subgroups $Q\le H\le G$, the *relative trace* is the $\mathcal O$-linear map
$$\mathrm{Tr}_Q^H\colon A^Q\to A^H,\qquad \mathrm{Tr}_Q^H(x)=\sum_{h\in[H/Q]}{}^hx,$$
where $[H/Q]$ is any set of representatives of the left cosets $hQ$. The sum does not depend on the choice of representatives, because $x$ is $Q$-fixed. Its image $A^H_Q:=\mathrm{Tr}_Q^H(A^Q)$ is an ideal of $A^H$.

3. Basic rules:
* transitivity: $\mathrm{Tr}_H^L\circ\mathrm{Tr}_Q^H=\mathrm{Tr}_Q^L$;
* conjugation: $\mathrm{Tr}^G_{{}^gQ}({}^gx)=\mathrm{Tr}^G_Q(x)$;
* the Mackey formula.

Consequently, if $Q\le_G R$ (meaning ${}^gQ\le R$ for some $g\in G$), then $A^G_Q\subseteq A^G_R$.

**Theorem 3.2 (defect groups; Green, Brauer).** Let $b$ be a block of $G$, i.e. a primitive idempotent of $Z(\mathcal OG)$.

1. The subgroups $Q\le G$ with $b\in(\mathcal OG)^G_Q$ that are minimal under inclusion are $p$-subgroups of $G$, and they form a single $G$-conjugacy class.
2. For $Q\le G$ one has $b\in(\mathcal OG)^G_Q$ if and only if $Q$ contains a $G$-conjugate of one, hence every, such minimal subgroup.
3. The same minimal subgroups are obtained by replacing $\mathcal OG$ and $b$ with $kG$ and $\bar b$.

For (1): if $S$ is a Sylow $p$-subgroup of $Q$, then $\mathrm{Tr}_S^Q$ is multiplication by the unit $|Q:S|$ on $(\mathcal OG)^Q$, so $(\mathcal OG)^G_Q\subseteq(\mathcal OG)^G_S$. Conjugacy follows from the Mackey formula and the fact that $Z(\mathcal OG)b$ is a local ring, because $b$ is primitive (Rosenberg's lemma).

**Definition 3.3 (defect group, defect).** Let $b$ be a $p$-block of $G$.

1. A *defect group* of $b$ is a subgroup $D\le G$ such that $b\in\mathrm{Tr}_D^G\big((\mathcal OG)^D\big)$, and $b\notin\mathrm{Tr}_Q^G\big((\mathcal OG)^Q\big)$ for every proper subgroup $Q<D$. Equivalently, by Theorem 3.2(3), $\bar b\in\mathrm{Tr}_D^G((kG)^D)$ and $D$ is minimal with this property.
2. By Theorem 3.2, "$D$ is a defect group of $b$" is a property of subgroups $D\le G$. It holds for a single $G$-conjugacy class of $p$-subgroups. One therefore speaks of "the defect group $D$ of $b$", meaning any member of this class.
3. If $|D|=p^{d}$, the integer $d=d(b)\ge0$ is the *defect* of $b$.

*Remarks.*

(1) *Characterisation via the Brauer homomorphism.* For a $p$-subgroup $Q\le G$, the *Brauer homomorphism* is
$$\mathrm{Br}_Q\colon (kG)^Q\to kC_G(Q),\qquad \sum_{g\in G}a_gg\mapsto\sum_{g\in C_G(Q)}a_gg.$$
It is a surjective algebra homomorphism with kernel $\sum_{R<Q}(kG)^Q_R$. Then $D$ is a defect group of $b$ if and only if $D$ is maximal among the $p$-subgroups $Q$ with $\mathrm{Br}_Q(\bar b)\neq0$. (Here $\mathrm{Br}_Q(\bar b)\neq0$ if and only if $Q\le_G D$.) The same characterisation appears as: $\Delta D=\{(x,x):x\in D\}$ is a vertex of $\mathcal OGb$, viewed as an $\mathcal O[G\times G]$-module.

(2) *Characters.* Let $|G|_p=p^a$ and $d=d(b)$. Then $p^{a-d}=\min\{\chi(1)_p:\chi\in\mathrm{Irr}(G,b)\}$ (Brauer). This gives an alternative, purely character-theoretic definition of the defect, but not of the group $D$.
* Defect zero: $d(b)=0$ (i.e. $D=1$) if and only if $\mathrm{Irr}(G,b)=\{\chi\}$ with $\chi(1)_p=|G|_p$.
* The principal block has the Sylow $p$-subgroups as defect groups.
* Every defect group contains $O_p(G)$, and is of the form $S\cap{}^gS$ for some Sylow $p$-subgroup $S$ and some $g\in G$ (Green).

(3) *Brauer correspondent.* This is needed for the Alperin--McKay statement in [2025, 201(2), no. 2]. Let $D$ be a defect group of $b$, and put $N=N_G(D)$. Then $\mathrm{Br}_D(\bar b)$ is $N$-stable and lies in $kC_G(D)$, hence in $Z(kN)$. Brauer's First Main Theorem says two things:
* $\mathrm{Br}_D(\bar b)$ is a primitive idempotent of $Z(kN)$, i.e. a block of $N$, with defect group $D$;
* $b\mapsto\mathrm{Br}_D(\bar b)$ is a bijection between the blocks of $G$ with defect group $D$ and the blocks of $N_G(D)$ with defect group $D$.

The block $B$ of $N_G(D)$ (lifted to $Z(\mathcal ON)$ by Definition #2) with $\bar B=\mathrm{Br}_D(\bar b)$ is the *Brauer correspondent* of $b$. Classically it is described as the unique block $B$ of $N_G(D)$ with $B^G=b$, where $\lambda_{B^G}(\hat C)=\lambda_B(\widehat{C\cap N})$ for classes $C$ of $G$.

(4) *Use in the Annals papers.* [2024, 200(2), no. 4] and [2025, 201(2), no. 2] use Definition 3.3 for arbitrary finite groups and primes. They only use $D$ up to conjugacy, through $|G:D|_p$, through whether $D$ is abelian, and through $N_G(D)$. All three are conjugation invariant.

## 4. Parabolic subgroups of a real semisimple Lie group (minimal and standard parabolics)

*Chapter context.* This is the chapter on parabolic subgroups in a text on the structure theory of real semisimple Lie groups (in the style of Knapp, *Lie Groups Beyond an Introduction*, Ch. VII). The reader knows the following.

* Cartan involutions and decompositions $\mathfrak g=\mathfrak k\oplus\mathfrak p$.
* Maximal abelian subspaces $\mathfrak a\subseteq\mathfrak p$, the restricted roots $\Sigma=\Sigma(\mathfrak g,\mathfrak a)$ with root spaces $\mathfrak g^\beta$, and the restricted Weyl group $W=N_K(\mathfrak a)/Z_K(\mathfrak a)$.
* Positive systems and simple roots, and the Iwasawa decomposition $G=KAN$.
* The Bruhat decomposition $G=\bigsqcup_{w\in W}PwP$.

Minimal and standard parabolic subgroups and their Langlands decompositions are defined here.

Throughout, $G$ is a connected real semisimple Lie group with finite centre, and $\mathfrak g=\mathrm{Lie}(G)$.

**Setup 4.1 (Iwasawa data).** Fix the following.

* A Cartan involution $\theta$ of $\mathfrak g$, with Cartan decomposition $\mathfrak g=\mathfrak k\oplus\mathfrak p$, and $K\le G$ the analytic subgroup with Lie algebra $\mathfrak k$. It is compact, because the centre of $G$ is finite.
* A maximal abelian subspace $\mathfrak a\subseteq\mathfrak p$, with restricted root space decomposition $\mathfrak g=\mathfrak m\oplus\mathfrak a\oplus\bigoplus_{\beta\in\Sigma}\mathfrak g^\beta$, where $\mathfrak m:=Z_{\mathfrak k}(\mathfrak a)$.
* A positive system $\Sigma_+\subseteq\Sigma$, i.e. $\Sigma_+=\{\beta:\beta(H_0)>0\}$ for some $H_0\in\mathfrak a$ with $\beta(H_0)\ne0$ for all $\beta\in\Sigma$. Let $\Pi\subseteq\Sigma_+$ be its simple roots. Every $\beta\in\Sigma$ is a linear combination of $\Pi$ with integer coefficients that are all $\ge0$ or all $\le0$.

Put $\mathfrak n:=\bigoplus_{\beta\in\Sigma_+}\mathfrak g^\beta$. Let $M:=Z_K(\mathfrak a)=\{k\in K:\mathrm{Ad}(k)H=H\ \forall H\in\mathfrak a\}$, which is compact and possibly disconnected. Let $A:=\exp\mathfrak a$ and $N:=\exp\mathfrak n$, the analytic subgroups. Any two choices of $(\theta,\mathfrak a,\Sigma_+)$ are conjugate under $\mathrm{Ad}(G)$, using successively the conjugacy of Cartan involutions, of maximal abelian subspaces under $K$, and of positive systems under $W$.

**Definition 4.2 (minimal parabolic subgroup).** The *standard minimal parabolic subgroup* attached to $(\theta,\mathfrak a,\Sigma_+)$ is $P:=MAN$. It is a closed subgroup of $G$ with Lie algebra $\mathfrak q_\emptyset:=\mathfrak m\oplus\mathfrak a\oplus\mathfrak n$, the *minimal parabolic subalgebra*. Its *Langlands decomposition* is the statement that multiplication $M\times A\times N\to P$ is a diffeomorphism. Here $M$ centralises $A$, and $MA$ normalises $N$. A *minimal parabolic subgroup* of $G$ is any conjugate $gPg^{-1}$, $g\in G$. By 4.1 these form one conjugacy class, which does not depend on the choices.

**Definition 4.3 (standard parabolic subalgebras and subgroups).** For a subset $\Pi'\subseteq\Pi$, let $\Sigma_{\Pi'}:=\Sigma\cap\operatorname{Span}_{\mathbb R}(\Pi')$ and define
$$\mathfrak q_{\Pi'}:=\mathfrak m\oplus\mathfrak a\oplus\bigoplus_{\beta\in\Sigma_+\cup\Sigma_{\Pi'}}\mathfrak g^\beta,\qquad Q_{\Pi'}:=N_G(\mathfrak q_{\Pi'})=\{g\in G:\mathrm{Ad}(g)\mathfrak q_{\Pi'}=\mathfrak q_{\Pi'}\}.$$
A *standard parabolic subalgebra* is a subalgebra of $\mathfrak g$ containing $\mathfrak q_\emptyset$. A *standard parabolic subgroup* is a subgroup of $G$ containing $P$. Both notions are relative to $(\theta,\mathfrak a,\Sigma_+)$.

**Theorem 4.4.**

1. Each $\mathfrak q_{\Pi'}$ is a Lie subalgebra. The map $\Pi'\mapsto\mathfrak q_{\Pi'}$ is an inclusion-preserving bijection from subsets of $\Pi$ onto the standard parabolic subalgebras.
2. The map $\Pi'\mapsto Q_{\Pi'}$ is an inclusion-preserving bijection from subsets of $\Pi$ onto the standard parabolic subgroups, with $Q_\emptyset=P$ and $Q_\Pi=G$. Each $Q_{\Pi'}$ is closed, has Lie algebra $\mathfrak q_{\Pi'}$, and equals $\bigcup_{w\in W_{\Pi'}}PwP$. Here $W_{\Pi'}\le W$ is generated by the reflections in $\Pi'$, and $w$ is represented in $N_K(\mathfrak a)$. In particular every subgroup containing $P$ is automatically closed.
3. (*Langlands decomposition.*) Put $\mathfrak a_{\Pi'}=\{H\in\mathfrak a:\alpha(H)=0\ \forall\alpha\in\Pi'\}$, $A_{\Pi'}=\exp\mathfrak a_{\Pi'}$, $\mathfrak n_{\Pi'}=\bigoplus_{\beta\in\Sigma_+\setminus\Sigma_{\Pi'}}\mathfrak g^\beta$ and $N_{\Pi'}=\exp\mathfrak n_{\Pi'}$.
* The *Levi subgroup* is $L_{\Pi'}:=Z_G(\mathfrak a_{\Pi'})$. It equals $M_{\Pi'}\times A_{\Pi'}$, where $M_{\Pi'}=\bigcap_\chi\ker|\chi|$, over continuous homomorphisms $\chi\colon L_{\Pi'}\to\mathbb R^\times$.
* Multiplication $M_{\Pi'}\times A_{\Pi'}\times N_{\Pi'}\to Q_{\Pi'}$ is a diffeomorphism, $N_{\Pi'}$ is the nilradical of $Q_{\Pi'}$, and $Q_{\Pi'}=L_{\Pi'}\ltimes N_{\Pi'}$.
* For $\Pi'=\emptyset$ this recovers $P=MAN$.

(Knapp, op. cit., Ch. VII. For (2), Bruhat decomposition plus the theory of Tits systems, Bourbaki, *Lie Groups and Lie Algebras*, Ch. IV, §2.)

**Definition 4.5 (parabolic subgroups).** A *parabolic subgroup* of $G$ is a subgroup $Q\le G$ that contains some minimal parabolic subgroup. Equivalently, $Q=gQ_{\Pi'}g^{-1}$ for some $g\in G$ and some $\Pi'\subseteq\Pi$, and then $\Pi'$ is uniquely determined by $Q$ (the *type* of $Q$). A *parabolic subalgebra* is an $\mathrm{Ad}(G)$-conjugate of some $\mathfrak q_{\Pi'}$. Equivalently, it is a real subalgebra $\mathfrak q$ such that $\mathfrak q\otimes\mathbb C$ contains a Borel subalgebra of $\mathfrak g_{\mathbb C}$. Parabolic subgroups and parabolic subalgebras correspond bijectively via $Q\mapsto\mathrm{Lie}(Q)$ and $\mathfrak q\mapsto N_G(\mathfrak q)$.

* $Q$ is *proper* if $Q\ne G$, i.e. $\Pi'\neq\Pi$.
* The *maximal* proper parabolic subgroups are the conjugates of $Q_{\Pi\setminus\{\alpha\}}$, $\alpha\in\Pi$.
* The *codimension* of $Q$ is $\dim G/Q=\dim\mathfrak n_{\Pi'}$.

*Remarks.*

(1) *Dynamical description.* Let $X\in\mathfrak a$ satisfy $\alpha(X)=0$ for $\alpha\in\Pi'$ and $\alpha(X)>0$ for $\alpha\in\Pi\setminus\Pi'$. Then $\mathfrak q_{\Pi'}$ is the sum of the eigenspaces of $\operatorname{ad}X$ with eigenvalue $\ge0$. Also
$$Q_{\Pi'}=\{g\in G:\exp(-tX)\,g\,\exp(tX)\text{ stays bounded as }t\to+\infty\}.$$
Every parabolic subgroup arises this way from some $X\in\mathfrak p$. The Higgs-bundle literature uses the same recipe for complex groups: $P_s=\{g:e^{ts}ge^{-ts}\text{ bounded as }t\to\infty\}$ for $s\in i\mathfrak k$. This is the convention in [2024, 200(3), no. 1].

(2) *Algebraic groups and disconnected real forms.* Suppose $G=\mathbf H(\mathbb R)$ or $G=\mathbf H(\mathbb R)^0$ for a connected reductive $\mathbb R$-group $\mathbf H$. For example, the real form $\mathrm G^{\mathbb R}=\mathrm G^{\tau}$ of a complex reductive group, which may be disconnected. Then the parabolic subgroups are the groups $G\cap\mathbf Q(\mathbb R)$, for $\mathbf Q$ an $\mathbb R$-parabolic subgroup of $\mathbf H$. Equivalently, they are $G\cap\mathrm Q$ for $\tau$-stable parabolic subgroups $\mathrm Q$ of the complexification, or $N_G(\mathfrak q)$ for parabolic subalgebras $\mathfrak q$. For connected $G$ this agrees with Definition 4.5, and the minimal ones come from minimal $\mathbb R$-parabolics. For reductive $\mathfrak g$, $\mathfrak a$ also contains the split part of the centre, on which all restricted roots vanish. Otherwise nothing changes.

(3) *Conventions in the sources.*
* [2022, 196(3), no. 1] and [2022, 196(3), no. 2] define a standard parabolic subgroup as a *closed* subgroup containing $P$, and use exactly the $\mathfrak q_{\Pi'}$ above. In the first paper this is written with $\operatorname{Span}(-\Pi')$, which gives the same set $\Sigma_+\cup\Sigma_{\Pi'}$.
* By Theorem 4.4(2), closedness is automatic.
* Some books parametrise standard parabolics by the complementary set $\Pi\setminus\Pi'$ ("the simple roots whose negatives are excluded"). The papers' homogeneous spaces are $Q\backslash G$, with right actions, and $G/Q$; their codimension counts are $\dim\mathfrak g/\mathfrak q$.

## 5. Infinitesimal character (and Casimir eigenvalue) of a representation of a real reductive group

*Chapter context.* This is an early chapter of a text on representations of real reductive groups (in the style of Knapp, *Representation Theory of Semisimple Groups*, or Wallach, *Real Reductive Groups I*). The reader knows the following.

* Universal enveloping algebras and their centres.
* The Harish-Chandra isomorphism for a complex reductive Lie algebra (recalled below).
* $(\mathfrak g,K)$-modules and admissibility.
* Continuous representations of Lie groups and their smooth vectors.

Infinitesimal characters of representations of real groups are defined here.

**Setup.** Let $\mathbf H$ be a connected reductive group over $\mathbb R$ and $G$ an open subgroup of $\mathbf H(\mathbb R)$. Examples are $\mathrm{GL}_n(\mathbb R)$, $\mathrm{PGL}_2(\mathbb R)$, and the real points of the split classical groups. Complex groups $\mathbf H'(\mathbb C)$ arise by taking $\mathbf H=\mathrm{Res}_{\mathbb C/\mathbb R}\mathbf H'$.

Let $K\le G$ be a maximal compact subgroup, $\mathfrak g_0=\mathrm{Lie}(G)$ and $\mathfrak g=\mathfrak g_0\otimes_{\mathbb R}\mathbb C$, a complex reductive Lie algebra. Write $U(\mathfrak g)$ for the universal enveloping algebra and $Z(\mathfrak g)$ for its centre.

**Theorem 5.1 (Harish-Chandra isomorphism).** Let $\mathfrak h\subseteq\mathfrak g$ be a Cartan subalgebra, $W=W(\mathfrak g,\mathfrak h)$ its Weyl group, and $\Delta^+$ a positive system of roots. Let $\rho=\frac12\sum_{\alpha\in\Delta^+}\alpha$, and let $\mathfrak n^{\pm}=\bigoplus_{\alpha\in\pm\Delta^+}\mathfrak g_\alpha$. Then $U(\mathfrak g)=U(\mathfrak h)\oplus(\mathfrak n^-U(\mathfrak g)+U(\mathfrak g)\mathfrak n^+)$. Write $p(z)\in U(\mathfrak h)=S(\mathfrak h)=\mathbb C[\mathfrak h^*]$ for the $U(\mathfrak h)$-component of $z\in Z(\mathfrak g)$. Then
$$\gamma\colon Z(\mathfrak g)\to\mathbb C[\mathfrak h^*],\qquad \gamma(z)(\lambda)=p(z)(\lambda-\rho),$$
is an algebra isomorphism onto $\mathbb C[\mathfrak h^*]^W$, and it does not depend on $\Delta^+$. For $\lambda\in\mathfrak h^*$, put $\chi_\lambda(z):=\gamma(z)(\lambda)$. Then:

1. every algebra homomorphism $Z(\mathfrak g)\to\mathbb C$ equals $\chi_\lambda$ for some $\lambda$;
2. $\chi_\lambda=\chi_\mu$ if and only if $\mu\in W\lambda$;
3. $Z(\mathfrak g)$ acts on the Verma module of highest weight $\lambda-\rho$ by $\chi_\lambda$.

Any two Cartan subalgebras are conjugate under $\mathrm{Int}(\mathfrak g)$. Every conjugating element induces the same bijection $\mathfrak h^*/W\to\mathfrak h'^*/W'$, and this bijection is compatible with $\lambda\mapsto\chi_\lambda$. Hence
$$\mathrm{Hom}_{\text{alg}}(Z(\mathfrak g),\mathbb C)\;\cong\;\mathfrak h^*/W$$
canonically, for any choice of $\mathfrak h$.

**Definition 5.2 (infinitesimal character).**

1. Let $V$ be a $U(\mathfrak g)$-module, e.g. a $(\mathfrak g,K)$-module. $V$ *has infinitesimal character* $\chi$, where $\chi\colon Z(\mathfrak g)\to\mathbb C$ is an algebra homomorphism, if $z\cdot v=\chi(z)v$ for all $z\in Z(\mathfrak g)$ and $v\in V$. Writing $\chi=\chi_\lambda$, one also says that $V$ has infinitesimal character $\lambda\in\mathfrak h^*$. Here $\lambda$ is well defined as an element of $\mathfrak h^*/W$. With this normalisation the trivial representation has infinitesimal character $\rho$.
2. Let $(\pi,V)$ be a continuous representation of $G$ on a complete locally convex space, e.g. a Hilbert, Banach or Fréchet space. Let $V^\infty$ be its smooth vectors, on which $U(\mathfrak g)$ acts by differentiation. $\pi$ *has infinitesimal character* $\chi$ if $V^\infty$ does, as a $U(\mathfrak g)$-module. If $\pi$ is admissible, this is equivalent to its Harish-Chandra module $V_K$ ($K$-finite vectors) having infinitesimal character $\chi$, because $V_K$ is dense in $V^\infty$.

**Proposition 5.3 (existence).**

* Every irreducible $(\mathfrak g,K)$-module has an infinitesimal character. This is Schur's lemma in Dixmier's form, since such a module has countable dimension.
* Every irreducible admissible representation of $G$ has an infinitesimal character, in particular every irreducible unitary representation (Harish-Chandra).

So "the infinitesimal character" of an irreducible representation is a well-defined point of $\mathfrak h^*/W$.

**Definition 5.4 (Casimir element and eigenvalue).** Let $B$ be a nondegenerate $\mathrm{Ad}(G)$-invariant symmetric bilinear form on $\mathfrak g_0$, e.g. the Killing form if $\mathfrak g_0$ is semisimple, or $\operatorname{tr}(XY)$ on $\mathfrak{gl}_n$. Let $(X_i)$ be a basis of $\mathfrak g_0$ and $(X^i)$ the $B$-dual basis. The *Casimir element* $\Omega_B:=\sum_iX_iX^i$ lies in $Z(\mathfrak g)$ and does not depend on the basis. If $V$ has infinitesimal character $\lambda$, then $\Omega_B$ acts on $V$ by the *Casimir eigenvalue*
$$\chi_\lambda(\Omega_B)=\langle\lambda,\lambda\rangle_B-\langle\rho,\rho\rangle_B,$$
where $\langle\,,\rangle_B$ is the bilinear form on $\mathfrak h^*$ dual to $B|_{\mathfrak h}$.

*Remarks.*

(1) *$\mathrm{SL}_2$ and $\mathrm{PGL}_2(\mathbb R)$.* Take the basis $H=\mathrm{diag}(1,-1)$, $E=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, $F=\begin{pmatrix}0&0\\1&0\end{pmatrix}$. Then $Z(\mathfrak{sl}_2)=\mathbb C[\Omega]$ with $\Omega=\frac14H^2+\frac12(EF+FE)$, the Casimir element for $B(X,Y)=2\operatorname{tr}(XY)$. Identify $\mathfrak h^*/W$ with $\mathbb C/\{\pm1\}$ via $\lambda\mapsto s=\lambda(H)/2$, so that $\rho\mapsto\frac12$. Then $\Omega$ acts by $s^2-\frac14$.
* The trivial representation has $s=\frac12$.
* The unitary principal series induced from $\mathrm{diag}(y,1)\mapsto\mathrm{sgn}(y)^\epsilon|y|^{it}$ has $s=\pm it$.
* The discrete series of lowest $\mathrm{SO}(2)$-weight $k\ge2$ has $s=\pm\frac{k-1}2$.
* On $K$-fixed vectors, $-\Omega$ is the hyperbolic Laplacian $-y^2(\partial_x^2+\partial_y^2)$.

[2026, 203(3), no. 3] works with $G=\mathrm{PGL}_2(\mathbb R)$ and calls the real number $\lambda_\pi:=\frac14+\Omega_\pi=s^2$ "the infinitesimal character". There $\Omega_\pi$ is the scalar by which this $\Omega$ acts on smooth vectors, and the Laplace eigenvalue is $\frac14-\lambda_\pi$.

(2) *Relation with Langlands parameters* (used in [2024, 200(3), no. 2]). Let $\mathbf H$ be split over $\mathbb R$ with maximal torus $\mathbf T$ and dual torus $\hat T\subseteq\hat G$. There is a canonical $W$-equivariant identification $\mathfrak h^*=X^*(\mathbf T)\otimes\mathbb C=X_*(\hat T)\otimes\mathbb C=\hat{\mathfrak t}$. Let $\phi\colon W_{\mathbb R}\to{}^LG$ be an L-parameter whose restriction to $\mathbb C^\times$ is $z\mapsto z^{\mu}\bar z^{\nu}$, with $\mu,\nu\in\hat{\mathfrak t}$ and $\mu-\nu\in X_*(\hat T)$. Then every member of its L-packet has infinitesimal character $W\mu$. Equivalently, $W\mu$ is the semisimple $\hat G$-orbit in $\hat{\mathfrak g}$ determined by $\phi$.

Thus for $r\colon\hat G\to\mathrm{GL}_N(\mathbb C)$, "the infinitesimal character of $\Pi_v$ is determined via $r$ by that of $\pi_v$" means the following. If $\pi_v$ has infinitesimal character $\mu\in\hat{\mathfrak t}$, then $\Pi_v$ has infinitesimal character $dr(\mu)$, read as an element of $\mathfrak h^*_{\mathrm{GL}_N}/S_N=\mathbb C^N/S_N$, i.e. the multiset of eigenvalues of $dr(\mu)$.

(3) *Complex places.* For $G=\mathbf H'(\mathbb C)$ one has $\mathfrak g\cong\mathfrak g_0\oplus\bar{\mathfrak g}_0$. An infinitesimal character is then a pair $(\lambda,\lambda')\in(\mathfrak h_0^*/W_0)^2$, matching the pair $(\mu,\nu)$ of the L-parameter $z\mapsto z^\mu\bar z^\nu$ of $W_{\mathbb C}=\mathbb C^\times$.

(4) *Conventions.* Some authors use the unshifted parameter $\lambda-\rho$ (the highest weight of a finite-dimensional representation). Others use $-\Omega$, or a different invariant form, for the Casimir. Always check which $\rho$-shift and which invariant form a source uses.

## 6. Convergence of a spectral sequence

*Chapter context.* This is the chapter on spectral sequences in a text on homological algebra (in the style of Weibel, *An Introduction to Homological Algebra*, Ch. 5). The reader knows abelian categories, cochain complexes and their cohomology, and filtered objects. The reader also knows what a spectral sequence is: pages, differentials, and the identification of each page with the cohomology of the previous one. This section defines the limit page $E_\infty$ and convergence.

Throughout, $\mathcal A$ is an abelian category, e.g. modules over a ring or $\mathbb Q_\ell$-vector spaces with a group action. We consider a *cohomological spectral sequence* $(E_r,d_r)_{r\ge r_0}$ consisting of the following data.

* Objects $E_r^{p,q}$ for $p,q\in\mathbb Z$ and integers $r\ge r_0$.
* Differentials $d_r\colon E_r^{p,q}\to E_r^{p+r,q-r+1}$ with $d_rd_r=0$.
* Isomorphisms $E_{r+1}^{p,q}\cong\ker(d_r\colon E_r^{p,q}\to E_r^{p+r,q-r+1})/\operatorname{im}(d_r\colon E_r^{p-r,q+r-1}\to E_r^{p,q})$.

Here $p$ is the *filtration degree* and $n=p+q$ the *total degree*.

**Definition 6.1 (the limit page $E_\infty$).**

1. *Cycles and boundaries.* Using the isomorphisms, one defines inductively subobjects
$$0=B_{r_0}^{p,q}\subseteq B_{r_0+1}^{p,q}\subseteq\cdots\subseteq Z_{r_0+1}^{p,q}\subseteq Z_{r_0}^{p,q}=E_{r_0}^{p,q}$$
with $E_r^{p,q}\cong Z_r^{p,q}/B_r^{p,q}$. Here $Z_{r+1}/B_r$ corresponds to $\ker d_r$ and $B_{r+1}/B_r$ to $\operatorname{im}d_r$. If $\mathcal A$ has countable intersections and unions of subobjects (e.g. a module category), put
$$E_\infty^{p,q}:=Z_\infty^{p,q}/B_\infty^{p,q},\qquad Z_\infty=\bigcap_rZ_r,\quad B_\infty=\bigcup_rB_r .$$
2. *Stabilisation.* The position $(p,q)$ *stabilises* if there is $r(p,q)$ such that, for all $r\ge r(p,q)$, both $d_r$ out of $E_r^{p,q}$ and $d_r$ into $E_r^{p,q}$ are zero. Then $E_r^{p,q}\cong E_{r+1}^{p,q}$ for $r\ge r(p,q)$, and one sets $E_\infty^{p,q}:=E_{r(p,q)}^{p,q}$. This agrees with (1) whenever (1) is defined, and it makes sense in any abelian category.
3. The spectral sequence is *bounded* if for each $n$ only finitely many $E_{r_0}^{p,n-p}$ are nonzero. A bounded spectral sequence stabilises at every position, since for large $r$ the source and target of the relevant $d_r$ vanish. It *degenerates at $E_s$* if $d_r=0$ for all $r\ge s$, and then $E_s=E_\infty$.

**Definition 6.2 (convergence).** Let $(H^n)_{n\in\mathbb Z}$ be objects of $\mathcal A$. Each comes with a decreasing filtration $\cdots\supseteq F^pH^n\supseteq F^{p+1}H^n\supseteq\cdots$ by subobjects, with graded pieces $\mathrm{gr}^pH^n=F^pH^n/F^{p+1}H^n$.

1. $(E_r)$ *weakly converges* to $H^\bullet$ if $E_\infty$ is defined, as in 6.1(1) or 6.1(2), and one is given isomorphisms
$$\beta^{p,q}\colon E_\infty^{p,q}\xrightarrow{\ \sim\ }\mathrm{gr}^pH^{p+q}\qquad\text{for all }p,q\in\mathbb Z .$$
2. $(E_r)$ *converges* to $H^\bullet$, written $E_{r_0}^{p,q}\Rightarrow H^{p+q}$, if it weakly converges and each filtration is *exhaustive*, $\bigcup_pF^pH^n=H^n$, and *separated*, $\bigcap_pF^pH^n=0$.
3. It *converges strongly* if, moreover, each $H^n$ is complete: $H^n\to\varprojlim_pH^n/F^pH^n$ is an isomorphism.
4. *Finite case.* If for each $n$ there are $a_n\le b_n$ with $F^{a_n}H^n=H^n$ and $F^{b_n}H^n=0$, the filtration is *finite*. Then (1)--(3) coincide, and $H^n$ is an iterated extension of the finitely many objects $E_\infty^{p,n-p}$, $a_n\le p<b_n$.
5. *Convergence in a range.* Let $I\subseteq\mathbb Z$ be a set of total degrees, e.g. $I=\{n:n>n_0\}$. $(E_r)$ *converges to $H^n$ for $n\in I$* if filtered objects $H^n$ are given only for $n\in I$, and the conditions above hold for all $(p,q)$ with $p+q\in I$. Nothing is asserted about $E_\infty^{p,q}$ for $p+q\notin I$.

The filtrations and the isomorphisms $\beta^{p,q}$ are part of the data. Convergence is a structure on the pair $\big((E_r),(H^n,F)\big)$, not merely a property of $(E_r)$.

**Proposition 6.3 (spectral sequence of a filtered complex).** Let $C^\bullet$ be a cochain complex in $\mathcal A$, with a decreasing filtration by subcomplexes $F^pC^\bullet$ that is finite in each degree. Then there is a spectral sequence with
$$E_0^{p,q}=\mathrm{gr}^pC^{p+q},\qquad E_1^{p,q}=H^{p+q}(\mathrm{gr}^pC^\bullet),$$
with $d_r$ of bidegree $(r,1-r)$, which is bounded. It converges to $H^{p+q}(C^\bullet)$ for the filtration $F^pH^n(C^\bullet)=\operatorname{im}\big(H^n(F^pC^\bullet)\to H^n(C^\bullet)\big)$. (Stacks Project, Tag 012K; Weibel, op. cit., Ch. 5.)

*Remarks.*

(1) *Homological indexing* is the same with $E^r_{p,q}$, $d^r\colon E^r_{p,q}\to E^r_{p-r,q+r-1}$ and increasing filtrations.
(2) *What convergence gives.* Over a field with finite-dimensional terms, convergence yields $\dim H^n=\sum_p\dim E_\infty^{p,n-p}$. In general it determines $H^n$ only up to extensions, so an isomorphism $H^n\cong\bigoplus_pE_\infty^{p,n-p}$ is a non-canonical statement valid e.g. over a field. A vanishing $E_r^{p,q}=0$ for all $p+q=n$ forces $H^n=0$.
(3) *Terminology varies.* Weibel's "approaches/abuts to" is (2), and his "converges" adds completeness and regularity. Boardman (*Conditionally convergent spectral sequences*) has a finer hierarchy. For bounded spectral sequences with finite filtrations, which is the only case needed below, all notions agree.
(4) *Use in [2020, 191(3), no. 4].* The spectral sequence there is that of Proposition 6.3 for a finite decreasing filtration, indexed by $m\in\{0,\dots,d+1\}$, of a complex of $\ell$-adic Galois representations. It starts at $r_0=1$, and $E_1^{m,s}=0$ unless $0\le m\le d$, so it is bounded. It therefore converges, in all degrees, to the cohomology of that complex. The theorem's phrase "converges to a complex whose $i$th cohomology is isomorphic to $H_c^{i+2d(n-k)}(\mathrm{Mor}_{d,P}(\mathbb A^1,X)_{\bar K},\mathbb Q_\ell)$, provided $i>\dots$" combines two things: this convergence, and an identification of the $i$-th cohomology valid only in the stated range. Equivalently, $(E_r)$ converges to $H^i:=H_c^{i+2d(n-k)}(\cdots)$ for $i\in I$ in the sense of 6.2(5). The isomorphisms are of $\mathbb Q_\ell$-vector spaces, compatible with the Frobenius action in the finite-field version.

## 7. Discrete series representations of $\mathrm{GL}_2(\mathbb{R})$

*Chapter context.* This is the chapter on representations of $\mathrm{GL}_2(\mathbb R)$ in a text on automorphic forms (in the style of Bump, *Automorphic Forms and Representations*, Ch. 2, or Jacquet--Langlands, *Automorphic Forms on GL(2)*). The reader knows the following.

* Haar measure, unitary representations and Schur's lemma.
* $(\mathfrak g,K)$-modules, admissible representations and Harish-Chandra modules, together with infinitesimal equivalence.
* Normalised parabolic induction.

The principal series, their reducibility, and the discrete series are treated here.

**Notation.**

* $G=\mathrm{GL}_2(\mathbb R)$, with centre $Z=\{zI:z\in\mathbb R^\times\}\cong\mathbb R^\times$ and $K=\mathrm O(2)$.
* $B$ is the upper triangular Borel subgroup, and $\kappa_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}\in\mathrm{SO}(2)$.
* Every quasi-character (continuous homomorphism) $\chi\colon\mathbb R^\times\to\mathbb C^\times$ is uniquely of the form $\mathrm{sgn}^\epsilon|\cdot|^s$ with $\epsilon\in\{0,1\}$ and $s\in\mathbb C$.
* $G$ and $G/Z$ are unimodular, and we fix a Haar measure $d\dot g$ on $G/Z$.

**Definition 7.1 (principal series).** For quasi-characters $\chi_1,\chi_2$ of $\mathbb R^\times$, let $I(\chi_1,\chi_2)$ be the space of $K$-finite functions $f\colon G\to\mathbb C$ such that
$$f\Big(\begin{pmatrix}a&x\\0&d\end{pmatrix}g\Big)=\chi_1(a)\chi_2(d)\Big|\frac ad\Big|^{1/2}f(g).$$
It is a $(\mathfrak g,K)$-module under right translation. (The smooth or $L^2$ completions give the corresponding representations of $G$.) Its $\mathrm{SO}(2)$-types are the characters $\kappa_\theta\mapsto e^{in\theta}$ with $n\equiv\epsilon_1+\epsilon_2\pmod 2$, each with multiplicity one, where $\chi_i=\mathrm{sgn}^{\epsilon_i}|\cdot|^{s_i}$.

**Proposition 7.2 (reducibility).** $I(\chi_1,\chi_2)$ is irreducible unless $\chi_1\chi_2^{-1}(t)=t^{p}\,\mathrm{sgn}(t)$ for some integer $p\neq0$. Suppose $\chi_1\chi_2^{-1}(t)=t^{k-1}\mathrm{sgn}(t)=|t|^{k-1}\mathrm{sgn}(t)^k$ with an integer $k\ge2$, i.e. $s_1-s_2=k-1$ and $\epsilon_1+\epsilon_2\equiv k\pmod2$. Then $I(\chi_1,\chi_2)$ has a unique nonzero proper submodule. It is infinite-dimensional, with $\mathrm{SO}(2)$-types $n\equiv k\pmod2$, $|n|\ge k$, and the quotient is irreducible of dimension $k-1$. For $p=-(k-1)\le-1$ the roles are reversed: there is a $(k-1)$-dimensional submodule and an infinite-dimensional irreducible quotient. (Bump, op. cit., Ch. 2; Jacquet--Langlands, op. cit.)

**Definition 7.3 ($D_k$).** For an integer $k\ge2$, let $D_k$ be the infinite-dimensional irreducible submodule of $I\big(|\cdot|^{\frac{k-1}2}\mathrm{sgn}^k,\ |\cdot|^{-\frac{k-1}2}\big)$. It has the following properties.

* Its $\mathrm{SO}(2)$-types are $e^{in\theta}$ for $n\in\{\pm k,\pm(k+2),\pm(k+4),\dots\}$, each with multiplicity one.
* Its central character is $zI\mapsto\mathrm{sgn}(z)^k$.
* $D_k\otimes(\mathrm{sgn}\circ\det)\cong D_k$.
* Its infinitesimal character is that of the $(k-1)$-dimensional representation $\mathrm{Sym}^{k-2}(\mathbb C^2)\otimes|\det|^{-(k-2)/2}$. In particular $\Omega=\frac14H^2+\frac12(EF+FE)\in Z(\mathfrak{sl}_2)$ acts by $\frac{k(k-2)}4$.
* Restricted to $\mathrm{SL}_2(\mathbb R)$ it is the sum of the holomorphic and antiholomorphic discrete series of weight $k$.

**Definition 7.4 (discrete series, essentially discrete series).**

1. Let $(\pi,\mathcal H)$ be an irreducible unitary representation of $G$. By Schur's lemma it has a unitary central character, so $|\langle\pi(g)v,w\rangle|$ is a function on $G/Z$. $\pi$ is *square-integrable modulo the centre*, or a *discrete series representation*, if there are nonzero $v,w\in\mathcal H$ with
$$\int_{G/Z}|\langle\pi(g)v,w\rangle|^2\,d\dot g<\infty .$$
Equivalently, this holds for all $v,w\in\mathcal H$.

2. An irreducible admissible representation $\pi$ of $G$, or an irreducible Harish-Chandra module, is *essentially square-integrable* (*essentially discrete series*) if there is a quasi-character $\chi$ of $\mathbb R^\times$ such that $\pi\otimes(\chi\circ\det)$ is infinitesimally equivalent to a discrete series representation. One may always take $\chi=|\cdot|^{\sigma}$ with $\sigma\in\mathbb R$.

**Theorem 7.5 (classification; Bargmann, Harish-Chandra).**

1. An irreducible unitary $\pi$ is a discrete series representation if and only if its Harish-Chandra module is isomorphic to $D_k\otimes|\det|^{it}$ for some integer $k\ge2$ and some $t\in\mathbb R$.
2. An irreducible admissible $\pi$ is essentially square-integrable if and only if $\pi_K\cong D_k\otimes|\det|^{s}$ for some integer $k\ge2$ and $s\in\mathbb C$. The pair $(k,s)$ is uniquely determined by $\pi$, and $k$ is the *weight* of $\pi$.
3. Equivalently, $\pi$ is essentially square-integrable of weight $k$ if and only if it is an infinite-dimensional subquotient of $I(\chi_1,\chi_2)$, with $\chi_i=\mathrm{sgn}^{\epsilon_i}|\cdot|^{s_i}$, $s_1-s_2\in\mathbb Z_{>0}$ and $k=s_1-s_2+1\equiv\epsilon_1+\epsilon_2\pmod 2$.

*Remarks.*

(1) *Weight $1$ is excluded.* For $k=1$, $I(\mathrm{sgn},1)$ is irreducible. It is a limit of discrete series: tempered, but not square-integrable modulo the centre. It corresponds to weight-one forms, which are not covered by Theorem A of [2026, 203(1), no. 4].
(2) *Langlands parameter.* Under the archimedean local Langlands correspondence, $D_k$ corresponds to the irreducible 2-dimensional representation $\mathrm{Ind}_{\mathbb C^\times}^{W_{\mathbb R}}\big(z\mapsto(z/|z|)^{k-1}\big)$ of the Weil group $W_{\mathbb R}$. Twisting by $|\det|^s$ corresponds to twisting by $|\cdot|_{W_{\mathbb R}}^s$ (Knapp, *Local Langlands correspondence: the archimedean case*). The essentially discrete series are exactly the $\pi$ whose parameter is irreducible.
(3) *Notation varies.* Some authors write $\pi_k$, $\sigma_k$, $D_k^{\pm}$ (for $\mathrm{SL}_2$), or parametrise by $k-1$ (the "Harish-Chandra parameter") instead. For $\mathrm{PGL}_2(\mathbb R)$, only even $k$ occur, and [2026, 203(3), no. 3] writes $\pi(k)$ for $D_{2k}$.
(4) *Use in [2026, 203(1), no. 4].* "$\pi_\infty$ essentially square-integrable" means that for every real place $v$ of the totally real field $F$, $\pi_v$ is essentially square-integrable in the sense of 7.4(2). By Theorem 7.5 this means $\pi_v\cong D_{k_v}\otimes|\det|^{s_v}$ with $k_v\ge2$. The paper uses exactly the subquotient description 7.5(3), possibly with non-paritious weights. These are the $\pi$ attached to cuspidal Hilbert modular forms of weights $k_v\ge2$.

## 8. Glauberman correspondence

*Chapter context.* This is the chapter on coprime actions in a text on character theory of finite groups (in the style of Isaacs, *Character Theory of Finite Groups*, Ch. 13, or Navarro, *Character Theory and the McKay Conjecture*). The reader knows irreducible complex characters, inner products $[\alpha,\beta]$, restriction, and Clifford theory. The reader also knows the elementary theory of coprime actions: Schur--Zassenhaus, Glauberman's lemma, and fixed-point subgroups. The Glauberman correspondence is constructed here.

**Setting.** Let $\Gamma$ and $S$ be finite groups with $\gcd(|\Gamma|,|S|)=1$, and let $S$ act on $\Gamma$ by automorphisms, $(s,x)\mapsto{}^sx$. This is a *coprime action*. Then:

* $C_\Gamma(S)=\{x\in\Gamma:{}^sx=x\ \forall s\in S\}$ is the fixed-point subgroup;
* $S$ acts on $\mathrm{Irr}(\Gamma)$ by $({}^s\chi)(x)=\chi({}^{s^{-1}}x)$;
* $\mathrm{Irr}_S(\Gamma)$ is the set of $S$-fixed irreducible characters.

If $T\trianglelefteq S$, then $C_\Gamma(T)$ is $S$-stable, and $S/T$ acts coprimely on it with $C_{C_\Gamma(T)}(S/T)=C_\Gamma(S)$.

**Theorem 8.1 (Glauberman, the $p$-group case).** Suppose $S$ is a $p$-group for a prime $p$, so that $p\nmid|\Gamma|$, and let $\chi\in\mathrm{Irr}_S(\Gamma)$. There is a unique $\chi^*\in\mathrm{Irr}(C_\Gamma(S))$ such that $p\nmid[\chi_{C_\Gamma(S)},\chi^*]$. Here $\chi_{C_\Gamma(S)}$ is the restriction. The map $\chi\mapsto\chi^*$ is a bijection $\mathrm{Irr}_S(\Gamma)\to\mathrm{Irr}(C_\Gamma(S))$.

**Theorem 8.2 (Glauberman; uniqueness and compatibility).** Consider all pairs $(\Gamma,S)$ of a coprime action as above with $S$ *solvable*. There is a unique way to assign to each such pair a bijection
$$\pi(\Gamma,S)\colon\mathrm{Irr}_S(\Gamma)\to\mathrm{Irr}(C_\Gamma(S))$$
such that the following hold.

1. If $S$ is a $p$-group, $\pi(\Gamma,S)(\chi)=\chi^*$ as in Theorem 8.1. (In particular $\pi(\Gamma,1)=\mathrm{id}$.)
2. Let $T\trianglelefteq S$ and $\chi\in\mathrm{Irr}_S(\Gamma)$. Then $\beta:=\pi(\Gamma,T)(\chi)\in\mathrm{Irr}(C_\Gamma(T))$ is $S/T$-invariant, and
$$\pi(\Gamma,S)(\chi)=\pi\big(C_\Gamma(T),S/T\big)(\beta).$$

Moreover each $\pi(\Gamma,S)$ is equivariant for automorphisms of $\Gamma\rtimes S$ that stabilise both $\Gamma$ and $S$. (Isaacs, op. cit., Ch. 13.)

Concretely, $\pi(\Gamma,S)$ can be computed recursively. Choose a chain $1=S_0\trianglelefteq S_1\trianglelefteq\cdots\trianglelefteq S_m=S$ of normal subgroups of $S$ with each $S_i/S_{i-1}$ a $p_i$-group; such a chain exists because $S$ is solvable. Put $\Gamma_i=C_\Gamma(S_i)$, on which $S_{i+1}/S_i$ acts. Then $\pi(\Gamma,S)$ is the composite of the $p_i$-group bijections of Theorem 8.1 for $(\Gamma_{i-1},S_i/S_{i-1})$, restricted to $S$-invariant characters. Theorem 8.2 says the result does not depend on the chain.

**Definition 8.3 (Glauberman correspondence).** Let $S$ be solvable and act coprimely on $\Gamma$. The *Glauberman correspondence* is the bijection
$$\mathrm{Irr}_S(\Gamma)\longleftrightarrow\mathrm{Irr}(C_\Gamma(S)),\qquad \theta\mapsto\theta^*:=\pi(\Gamma,S)(\theta),$$
of Theorem 8.2. We call $\theta^*$ the *Glauberman correspondent* of $\theta$.

*Remarks.*

(1) *What a formaliser needs.* The data is a coprime action $S\to\mathrm{Aut}(\Gamma)$ with $S$ solvable. The output is a bijection of finite sets, characterised by 8.2(1)--(2). Two routes are possible:
* define $\pi(\Gamma,S)$ by strong induction on $|S|$, using any normal subgroup $T$ with $S/T$ of prime order, or with $T$ a $p$-group, and then prove independence;
* define it via the chain construction above.

The existence part of Theorem 8.1, the uniqueness of the constituent with multiplicity prime to $p$, is the key nontrivial input.

(2) *Cyclic $S$ (Glauberman's original construction).* If $S=\langle s\rangle$ is cyclic, there is a character formula. Each $\chi\in\mathrm{Irr}_S(\Gamma)$ has a canonical extension $\hat\chi$ to $\Gamma\rtimes S$, and $\hat\chi(cs)=\varepsilon\,\chi^*(c)$ for all $c\in C_\Gamma(S)$, with a sign $\varepsilon=\pm1$ independent of $c$.
(3) *Non-solvable $S$.* If $S$ is not solvable, then $|\Gamma|$ is odd (Feit--Thompson). Isaacs constructed a canonical bijection for $|\Gamma|$ odd, and it agrees with Glauberman's when both are defined. [2020, 192(1), no. 4] assumes $S$ solvable and uses Glauberman's bijection.
(4) *Use in [2020, 192(1), no. 4].* The theorem completed there is *Glauberman degree-divisibility*: if $\theta\in\mathrm{Irr}_S(\Gamma)$ and $\theta^*$ is its Glauberman correspondent, then $\theta^*(1)\mid\theta(1)$. This was reduced by Hartley--Turull to a congruence for Deligne--Lusztig Green functions. Characters are complex-valued, and $\mathrm{Irr}_S(\Gamma)$, $C_\Gamma(S)$ are as in the Setting.

## 9. Height zero characters of a block

*Chapter context.* This is the chapter on defect groups and heights in a text on block theory of finite groups (in the style of Navarro, *Characters and Blocks of Finite Groups*). The reader knows $p$-blocks $b$ and the sets $\mathrm{Irr}(G,b)$ (Definition #2), and defect groups of blocks (Definition #3). Heights are defined here.

Throughout, $G$ is a finite group and $p$ a prime. For a nonzero integer $n$, $n_p$ is the largest power of $p$ dividing $n$, and $\nu_p(n)$ is its exponent, so $n_p=p^{\nu_p(n)}$. Write $|G|_p=p^a$.

**Theorem 9.1 (Brauer).** Let $b$ be a $p$-block of $G$ with defect group $D$, and put $|D|=p^{d}$, where $d=d(b)$ is the defect of $b$.

1. For every $\chi\in\mathrm{Irr}(G,b)$, the integer $|G:D|_p=p^{a-d}$ divides $\chi(1)$.
2. There exists $\chi\in\mathrm{Irr}(G,b)$ with $\chi(1)_p=p^{a-d}$.

Equivalently, $p^{a-d}=\min\{\chi(1)_p:\chi\in\mathrm{Irr}(G,b)\}$. (Navarro, op. cit.; Feit, *The Representation Theory of Finite Groups*.)

**Definition 9.2 (height; height zero characters).** Let $b$ and $D$ be as in Theorem 9.1.

1. The *height* of $\chi\in\mathrm{Irr}(G,b)$ is the integer
$$h(\chi):=\nu_p(\chi(1))-(a-d)\ \ge 0,$$
so that $\chi(1)_p=|G:D|_p\,p^{h(\chi)}$.

2. The set of *height zero characters* of $b$ is
$$\mathrm{Irr}_0(G,b)=\mathrm{Irr}_0(b):=\{\chi\in\mathrm{Irr}(G,b):\chi(1)_p=|G:D|_p\}=\{\chi\in\mathrm{Irr}(G,b):h(\chi)=0\}.$$
Since $D$ is a $p$-group, $|G:D|_p=|G|_p/|D|$.

By Theorem 9.1(2), $\mathrm{Irr}_0(G,b)\neq\emptyset$. Since the defect groups of $b$ form one $G$-conjugacy class (Definition #3), $|D|$, and hence $h(\chi)$ and $\mathrm{Irr}_0(G,b)$, do not depend on the choice of $D$. When the block is written as a set $B=\mathrm{Irr}(G,b)$, one writes $\mathrm{Irr}_0(B)$ and $h_\chi$.

*Remarks.*

(1) *Equivalent formulations.*
* $\chi\in\mathrm{Irr}_0(G,b)$ if and only if $p\nmid\chi(1)\,|D|/|G|_p$. The latter is an integer by 9.1(1).
* In terms of the *defect of $\chi$*, $d(\chi):=a-\nu_p(\chi(1))$, one has $h(\chi)=d(b)-d(\chi)$. So the height zero characters are those of maximal defect $d(\chi)=d(b)$.
* Theorem 9.1(2) yields a character-theoretic description of $|D|$, used as the definition of $d(b)$ in some texts: $|D|=p^{\,a-\min_\chi\nu_p(\chi(1))}$.

(2) *Special cases.*
* For the principal block, $D$ is a Sylow $p$-subgroup. Then $\mathrm{Irr}_0(G,b_0)$ is the set of $p'$-degree characters in the principal block.
* For a block of defect zero, $\mathrm{Irr}(G,b)=\mathrm{Irr}_0(G,b)$ consists of a single character.
* Heights are also defined for irreducible Brauer characters in the same way, but this is not needed below.

(3) *Use in the Annals papers.*
* [2024, 200(2), no. 4] proves, for $p$ odd: if $\mathrm{Irr}(B)=\mathrm{Irr}_0(B)$, then $D$ is abelian. Together with Kessar--Malle for the converse and Ruhstorfer for $p=2$, this is Brauer's Height Zero Conjecture.
* [2025, 201(2), no. 2] works with $\ell=2$. It uses $\mathrm{Irr}_0(G,b)$ and, for the Alperin--McKay conjecture, $\mathrm{Irr}_0(N_G(D),B)$. Here $B$ is the Brauer correspondent of $b$, a block of $N_G(D)$ with the same defect group $D$ (see Definition #3, Remarks), so its heights are computed with $|N_G(D):D|_\ell$.

## 10. Hochschild--Kostant--Rosenberg antisymmetrisation map

*Chapter context.* This is the chapter on Hochschild cohomology of commutative algebras in a text on homological algebra or deformation theory (in the style of Loday, *Cyclic Homology*, Ch. 1 and 3, or Weibel, *An Introduction to Homological Algebra*, Ch. 9). The reader knows the Hochschild cochain complex $C^\bullet(A,M)$ of an associative algebra with coefficients in a bimodule, its cohomology $\mathrm{HH}^\bullet(A,M)$ and the cup product. The reader also knows derivations, Kähler differentials, exterior powers, and smooth algebras. Polyvector fields and the HKR map are introduced here.

Throughout, $k$ is a commutative ring and $R$ a commutative $k$-algebra. Write $R^{n}$ for the product of $n$ copies of $R$.

**Convention 10.1 (Hochschild cochains).** $C^n(R,R)$ is the $R$-module of $k$-multilinear maps $f\colon R^{n}\to R$, i.e. $\mathrm{Hom}_k(R^{\otimes_kn},R)$, with $C^0(R,R)=R$. The differential $\delta\colon C^n\to C^{n+1}$ is
$$(\delta f)(r_1,\dots,r_{n+1})=r_1f(r_2,\dots,r_{n+1})+\sum_{i=1}^n(-1)^if(r_1,\dots,r_ir_{i+1},\dots,r_{n+1})+(-1)^{n+1}f(r_1,\dots,r_n)r_{n+1}.$$
Then $Z^nC(R,R)=\ker\delta$ and $\mathrm{HH}^n(R,R)=H^n(C^\bullet(R,R),\delta)$. A cochain is *normalised* if it vanishes whenever some $r_i\in k\cdot1$.

**Definition 10.2 (polyvector fields).** $\mathrm{Der}_k(R)=\mathrm{Der}_k(R,R)$ is the $R$-module of $k$-linear derivations $D\colon R\to R$. For $n\ge0$, the module of *$n$-polyvector fields* is
$$T^n_{R/k}:=\textstyle\bigwedge^n_R\mathrm{Der}_k(R,R),$$
with $T^0_{R/k}=R$. Note that the exterior power is taken over $R$, not over $k$.

**Lemma 10.3.** For $D_1,\dots,D_n\in\mathrm{Der}_k(R)$, define $\langle D_1,\dots,D_n\rangle\in C^n(R,R)$ by
$$\langle D_1,\dots,D_n\rangle(r_1,\dots,r_n)=\sum_{\sigma\in S_n}\mathrm{sgn}(\sigma)\,D_{\sigma(1)}(r_1)\,D_{\sigma(2)}(r_2)\cdots D_{\sigma(n)}(r_n)=\det\big(D_j(r_i)\big)_{i,j}.$$
1. The map $(D_1,\dots,D_n)\mapsto\langle D_1,\dots,D_n\rangle$ is $R$-multilinear and alternating, i.e. it vanishes if $D_i=D_j$ for some $i\neq j$. Hence it induces an $R$-linear map $\bigwedge^n_R\mathrm{Der}_k(R)\to C^n(R,R)$.
2. Each $\langle D_1,\dots,D_n\rangle$ is a derivation in each argument separately, i.e. a multiderivation. Hence it is a normalised Hochschild cocycle: $\delta\langle D_1,\dots,D_n\rangle=0$.

**Definition 10.4 (HKR antisymmetrisation map).** Let $n\ge0$ and suppose $n!$ is invertible in $k$. The *HKR map* in degree $n$ is the $R$-linear map
$$\Phi^n_{\mathrm{HKR}}\colon T^n_{R/k}\to Z^nC(R,R)\subseteq C^n(R,R),\qquad D_1\wedge\dots\wedge D_n\mapsto\frac1{n!}\langle D_1,\dots,D_n\rangle .$$
Explicitly, $\Phi(D_1\wedge\dots\wedge D_n)(r_1,\dots,r_n)=\frac1{n!}\sum_{\sigma\in S_n}\mathrm{sgn}(\sigma)\prod_{i=1}^nD_{\sigma(i)}(r_i)$. For $n=0$ it is the identity of $R$, and for $n=1$ it is the inclusion $\mathrm{Der}_k(R)\subseteq C^1(R,R)$. The *unnormalised* HKR map $D_1\wedge\dots\wedge D_n\mapsto\langle D_1,\dots,D_n\rangle$ is defined over any $k$, and differs from $\Phi^n_{\mathrm{HKR}}$ by the factor $n!$.

**Theorem 10.5 (Hochschild--Kostant--Rosenberg).** Let $k$ be a field and $R$ a smooth $k$-algebra of finite type, e.g. $R=k[x_1,\dots,x_m]$. For every $n$, the unnormalised HKR map induces an isomorphism of $R$-modules
$$T^n_{R/k}\xrightarrow{\ \sim\ }\mathrm{HH}^n(R,R).$$
Hence so does $\Phi^n_{\mathrm{HKR}}$ whenever $n!\in k^\times$. Moreover the map is injective already on cochains. This is because $\Omega^1_{R/k}$ is finitely generated projective, so $\bigwedge^n_R\mathrm{Der}_k(R)$ identifies with the alternating $R$-multilinear forms on $\Omega^1_{R/k}$, i.e. with alternating multiderivations. If $\mathbb Q\subseteq k$, then $\bigoplus_n\Phi^n_{\mathrm{HKR}}$ induces an isomorphism of graded commutative algebras $(T^\bullet_{R/k},\wedge)\cong(\mathrm{HH}^\bullet(R,R),\cup)$. This holds on cohomology, not on cochains. (Loday, op. cit., Ch. 3; Hochschild--Kostant--Rosenberg, *Differential forms on regular affine algebras*.)

*Remarks.*

(1) *Why $1/n!$.* With the factor $1/n!$ the map is multiplicative on cohomology. Without it, $[\langle D_1,\dots,D_n\rangle]=n!\,[D_1\cup\dots\cup D_n]$. Both versions have the same image up to the unit $n!$ when $n!\in k^\times$. In particular they define the same submodule of $Z^nC(R,R)$, and the same nonvanishing conditions.
(2) *Polynomial rings.* For $R=k[x_1,\dots,x_n]$, $\mathrm{Der}_k(R)$ is free on $\partial_1,\dots,\partial_n$ with $\partial_i=\partial/\partial x_i$, and $T^n_{R/k}=R\,\partial_1\wedge\dots\wedge\partial_n$. For $\eta=g\,\partial_1\wedge\dots\wedge\partial_n$, $g\in R$:
$$\Phi_{\mathrm{HKR}}(\eta)(r_1,\dots,r_n)=\frac{g}{n!}\det\Big(\frac{\partial r_i}{\partial x_j}\Big)_{i,j=1}^n ,$$
a Jacobian determinant.

(3) *Sign conventions.* In $A_\infty$/DG conventions the Hochschild differential of an ungraded algebra may differ from 10.1 by signs depending only on $n$. This changes neither the cocycles nor the HKR image.
(4) *Use in [2020, 191(2), no. 3].* There $k$ is a field of characteristic $0$, or an infinite field of characteristic $>n$, and $R=k[x_1,\dots,x_n]$ with $n\ge3$. In degree $n$ the integer $n!$ is invertible in $k$. "The HKR theorem furnishes an inclusion $T^n_{R/k}\subset Z^nC(R,R)$ inducing $T^n_{R/k}\cong\mathrm{HH}^n(R,R)$" refers to $\Phi^n_{\mathrm{HKR}}$, in top degree $n=\dim R$, as in Remark (2). An element $\eta\in T^n_{R/k}$ is thereby a $k$-multilinear map $R^n\to R$. The $A_\infty$-algebra $R_\eta$ has $m_2$ the multiplication of $R[\varepsilon]$ and $m_n=\varepsilon\,\Phi_{\mathrm{HKR}}(\eta)$, extended $k[\varepsilon]$-linearly. The hypothesis $\eta\neq0$ is insensitive to the normalisation.

## 11. Split classical groups $\mathrm{Sp}_{2n}$, $\mathrm{SO}_l$ and general spin groups $\mathrm{GSpin}_l$

*Chapter context.* This is the chapter on classical groups in a text on reductive groups over fields (in the style of Springer, *Linear Algebraic Groups*, or Knus--Merkurjev--Rost--Tignol, *The Book of Involutions*). The reader knows the following.

* Affine group schemes over a field, given by their functors of points on commutative algebras.
* Connected reductive groups, split maximal tori, root data, and the isomorphism theorem: a split connected reductive group is determined up to isomorphism by its based root datum, and every based root datum occurs.
* Langlands dual groups, Clifford algebras and the spin group.

The classical groups of the title are fixed here, with the normalisations used in the automorphic literature.

Throughout, $F$ is a field of characteristic $\neq2$ (in the applications, a number field or one of its completions), and $A$ denotes an arbitrary commutative $F$-algebra. $J_l$ is the $l\times l$ permutation matrix with $1$ in positions $(i,l+1-i)$, and $I_m$ is the identity matrix.

**Definition 11.1 (split symplectic and special orthogonal groups).** Put
$$J_{\mathrm{Sp}_{2n}}:=J_{2n}\,\mathrm{diag}(-I_n,I_n)=\begin{pmatrix}0&J_n\\-J_n&0\end{pmatrix},\qquad J_{\mathrm{SO}_l}:=J_l .$$
1. $\mathrm{Sp}_{2n}$ ($n\ge0$) is the group scheme $A\mapsto\{g\in\mathrm{GL}_{2n}(A):{}^tg\,J_{\mathrm{Sp}_{2n}}\,g=J_{\mathrm{Sp}_{2n}}\}$. For such $g$ the condition $\det g=1$ holds automatically. It is the automorphism group of the alternating form $\langle x,y\rangle={}^tx\,J_{\mathrm{Sp}_{2n}}\,y$.
2. $\mathrm{SO}_l$ ($l\ge0$) is the group scheme $A\mapsto\{g\in\mathrm{SL}_l(A):{}^tg\,J_l\,g=J_l\}$. It is the special orthogonal group of the split quadratic form $q(x)=\frac12{}^tx J_lx=\sum_{i\le\lfloor l/2\rfloor}x_ix_{l+1-i}+\big(\tfrac12x_{(l+1)/2}^2\text{ if }l\text{ odd}\big)$, of maximal Witt index $\lfloor l/2\rfloor$.

These are smooth connected split reductive $F$-groups. In each case $T=G\cap\{\text{diagonal}\}$ is a split maximal torus, consisting of the matrices $\mathrm{diag}(t_1,\dots,t_n,t_n^{-1},\dots,t_1^{-1})$, with an extra middle entry $1$ for $\mathrm{SO}_{2n+1}$, and $B=G\cap\{\text{upper triangular}\}$ is a Borel subgroup. The types are:

| group | type | rank |
|---|---|---|
| $\mathrm{Sp}_{2n}$ | $C_n$, simply connected | $n$ |
| $\mathrm{SO}_{2n+1}$ | $B_n$, adjoint | $n$ |
| $\mathrm{SO}_{2n}$ | $D_n$, $n\ge2$ | $n$ |

$\mathrm{SO}_2\cong\mathbb G_m$ is a split torus, and $\mathrm{Sp}_0$, $\mathrm{SO}_0$, $\mathrm{SO}_1$ are trivial.

**Definition 11.2 (split general spin group, via root datum).** Let $l\ge0$ and $n=\lfloor l/2\rfloor$. Put $X=\bigoplus_{i=0}^n\mathbb Ze_i$ and $X^\vee=\bigoplus_{i=0}^n\mathbb Ze_i^\vee$, with $\langle e_i,e_j^\vee\rangle=\delta_{ij}$. For $l>2$ define simple roots $\Delta$ and simple coroots $\Delta^\vee$ as follows.

* $l=2n$ even: $\Delta=\{e_1-e_2,\dots,e_{n-1}-e_n,\ e_{n-1}+e_n\}$ and $\Delta^\vee=\{e_1^\vee-e_2^\vee,\dots,e_{n-1}^\vee-e_n^\vee,\ e_{n-1}^\vee+e_n^\vee-e_0^\vee\}$.
* $l=2n+1$ odd: $\Delta=\{e_1-e_2,\dots,e_{n-1}-e_n,\ e_n\}$ and $\Delta^\vee=\{e_1^\vee-e_2^\vee,\dots,e_{n-1}^\vee-e_n^\vee,\ 2e_n^\vee-e_0^\vee\}$.

For $l\le2$ put $\Delta=\Delta^\vee=\emptyset$. Then $\mathrm{GSpin}_l$ is the split connected reductive $F$-group with based root datum $(X,\Delta,X^\vee,\Delta^\vee)$, together with its split maximal torus $T$ ($X^*(T)=X$) and Borel subgroup $B$. It has rank $n+1$. Moreover:

* $\mathrm{GSpin}_0=\mathrm{GSpin}_1=\mathrm{GL}_1$ and $\mathrm{GSpin}_2=\mathrm{GL}_1\times\mathrm{GL}_1$.
* For $l>2$, the identity component of the centre is $e_0^\vee(\mathrm{GL}_1)$.
* For $l>2$, the characters trivial on the derived group are the multiples of $\Upsilon:=2e_0+e_1+\dots+e_n$. This is the unique one with $\langle\Upsilon,e_0^\vee\rangle=2$, the *spinor norm*, and $\mathrm{Spin}_l:=\ker\Upsilon$ is the derived group, which is simply connected.

**Proposition 11.3 (Clifford model).** Let $V=F^l$ with the quadratic form $q$ of 11.1(2), let $C(V)=T(V)/(v\otimes v-q(v))$ be its Clifford algebra with even part $C^+(V)$, and let $\tau$ be the canonical anti-involution, $\tau(v_1\cdots v_r)=v_r\cdots v_1$. Put
$$\mathrm{GSpin}(V)(A)=\{g\in(C^+(V)\otimes_FA)^\times:\ g\,(V\otimes A)\,g^{-1}=V\otimes A\}.$$
1. $g\mapsto\nu(g):=\tau(g)g$ is a character $\nu\colon\mathrm{GSpin}(V)\to\mathbb G_m$. Its kernel is the spin group $\mathrm{Spin}(V)$.
2. $g\mapsto(v\mapsto gvg^{-1})$ gives an exact sequence $1\to\mathbb G_m\to\mathrm{GSpin}(V)\to\mathrm{SO}(V)\to1$, with $\mathbb G_m$ the central scalars.
3. Multiplication induces $(\mathbb G_m\times\mathrm{Spin}(V))/\mu_2\xrightarrow{\sim}\mathrm{GSpin}(V)$, where $\mu_2$ is embedded as $\{(1,1),(-1,-1)\}$ and $-1\in\mathrm{Spin}(V)$ is the nontrivial element of $\ker(\mathrm{Spin}(V)\to\mathrm{SO}(V))$.
4. $\mathrm{GSpin}(V)\cong\mathrm{GSpin}_l$ of Definition 11.2. Under this isomorphism the central $\mathbb G_m$ is $e_0^\vee(\mathrm{GL}_1)$, $\nu$ is $\Upsilon$, and $\mathrm{GSpin}_l/e_0^\vee(\mathrm{GL}_1)\cong\mathrm{SO}_l$.

(Asgari--Shahidi; Hundley--Sayag; Knus--Merkurjev--Rost--Tignol, op. cit.)

*Remarks.*

(1) *Dual groups and the standard representation $r_G$* (the table in [2024, 200(3), no. 2]). Each $\hat G$ embeds naturally in $\mathrm{GL}_N(\mathbb C)$; this embedding is $r_G$.

| $G$ | $\hat G$ | $N$ |
|---|---|---|
| $\mathrm{Sp}_{2n}$ | $\mathrm{SO}_{2n+1}(\mathbb C)$ | $2n+1$ |
| $\mathrm{SO}_{2n+1}$ | $\mathrm{Sp}_{2n}(\mathbb C)$ | $2n$ |
| $\mathrm{SO}_{2n}$ | $\mathrm{SO}_{2n}(\mathbb C)$ | $2n$ |
| $\mathrm{GSpin}_{2n+1}$ | $\mathrm{GSp}_{2n}(\mathbb C)$ | $2n$ |
| $\mathrm{GSpin}_{2n}$ | $\mathrm{GSO}_{2n}(\mathbb C)$ | $2n$ |

Here $\mathrm{GSp}$ and $\mathrm{GSO}$ are the similitude groups $\{g:{}^tgJg=e_0(g)J\}$, connected component for $\mathrm{GSO}$, and $e_0$ is the similitude character.

(2) *Ranks in Theorem 0.1 of [2024, 200(3), no. 2].* "Split special orthogonal of rank $n$" means $\mathrm{SO}_{2n}$ or $\mathrm{SO}_{2n+1}$. "Split general spin group of rank $n+1$" means $\mathrm{GSpin}_{2n}$ or $\mathrm{GSpin}_{2n+1}$. In both cases $n\ge1$. Representations of $\mathrm{SO}_l(F)$ are the representations of $\mathrm{GSpin}_l(F)$ trivial on $e_0^\vee(F^\times)$, since $\mathrm{GSpin}_l(F)\to\mathrm{SO}_l(F)$ is surjective by Hilbert 90.
(3) *Low rank.* $\mathrm{GSpin}_3\cong\mathrm{GL}_2$ and $\mathrm{GSpin}_5\cong\mathrm{GSp}_4$. Also $\mathrm{GSpin}_4\cong\{(g_1,g_2)\in\mathrm{GL}_2\times\mathrm{GL}_2:\det g_1=\det g_2\}$.
(4) *Other conventions.* Some authors use $\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix}$ for $\mathrm{Sp}_{2n}$, or other split forms for $\mathrm{SO}_l$. These give isomorphic groups, but different standard tori and Borel subgroups. In characteristic $2$, $\mathrm{SO}_l$ must be defined via the quadratic form, using the Dickson invariant when $l$ is even, not via $J_l$.

# Algebraic geometry

## 12. The Hodge structure on $H^1$ of a complex abelian variety

*Chapter context.* A chapter on the Hodge theory of complex abelian varieties in a graduate text on abelian varieties (in the style of Mumford's *Abelian Varieties* or Birkenhake--Lange's *Complex Abelian Varieties*). The reader knows abelian varieties over $\mathbb{C}$ and their analytifications, GAGA, singular (co)homology, cup and cap products and the de Rham theorem, ample line bundles and first Chern classes, and abstract pure and polarized rational Hodge structures; the Hodge structure on $H^1(A(\mathbb{C}),\mathbb{Q})$ and its polarizations are constructed here.

Throughout, $A$ is an abelian variety over $\mathbb{C}$ of dimension $g$, $A(\mathbb{C})$ is its analytification (a compact connected complex Lie group), and $T_0=\operatorname{Lie}(A)$ is the tangent space of $A(\mathbb{C})$ at the origin, a complex vector space of dimension $g$.

**Proposition 12.1 (uniformization).** The exponential map $\exp\colon T_0\to A(\mathbb{C})$ of the complex Lie group $A(\mathbb{C})$ is a surjective holomorphic group homomorphism, and its kernel $\Lambda$ is a lattice in $T_0$ (a subgroup generated by an $\mathbb{R}$-basis of $T_0$, so $\Lambda\cong\mathbb{Z}^{2g}$). It induces an isomorphism of complex Lie groups $T_0/\Lambda\cong A(\mathbb{C})$, and canonical isomorphisms $\Lambda\cong\pi_1(A(\mathbb{C}),0)\cong H_1(A(\mathbb{C}),\mathbb{Z})$ sending $\lambda$ to the class of the loop $\gamma_\lambda(t)=\exp(t\lambda)$, $t\in[0,1]$. (Mumford, *Abelian Varieties*, Chapter I.)

Consequently, for $R=\mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C}$ there are canonical isomorphisms
$$H^1(A(\mathbb{C}),R)\;\cong\;\operatorname{Hom}_{\mathbb{Z}}(\Lambda,R),\qquad \alpha\mapsto\big(\lambda\mapsto\langle\alpha,[\gamma_\lambda]\rangle\big).$$
Since $\Lambda\otimes_{\mathbb{Z}}\mathbb{R}=T_0$ as real vector spaces, $H^1(A(\mathbb{C}),\mathbb{R})=\operatorname{Hom}_{\mathbb{R}}(T_0,\mathbb{R})$ and $H^1(A(\mathbb{C}),\mathbb{C})=H^1(A(\mathbb{C}),\mathbb{Q})\otimes_{\mathbb{Q}}\mathbb{C}=\operatorname{Hom}_{\mathbb{R}}(T_0,\mathbb{C})$, the real-linear maps $T_0\to\mathbb{C}$; complex conjugation (acting on the factor $\mathbb{C}$) is $\varphi\mapsto\overline{\varphi}$, $\overline{\varphi}(v)=\overline{\varphi(v)}$.

**Definition 12.2 (the Hodge structure $V_A$).** Put
$$H^{1,0}:=\operatorname{Hom}_{\mathbb{C}}(T_0,\mathbb{C})\subseteq \operatorname{Hom}_{\mathbb{R}}(T_0,\mathbb{C})=H^1(A(\mathbb{C}),\mathbb{C}),\qquad H^{0,1}:=\overline{H^{1,0}},$$
the $\mathbb{C}$-linear and the $\mathbb{C}$-antilinear forms on $T_0$. Every real-linear $\varphi$ decomposes uniquely as $\varphi=\varphi'+\varphi''$ with $\varphi'(v)=\tfrac12(\varphi(v)-i\varphi(iv))$ linear and $\varphi''(v)=\tfrac12(\varphi(v)+i\varphi(iv))$ antilinear, so
$$H^1(A(\mathbb{C}),\mathbb{C})=H^{1,0}\oplus H^{0,1},\qquad \dim_{\mathbb{C}}H^{1,0}=\dim_{\mathbb{C}}H^{0,1}=g .$$
The *Hodge structure of $A$* is $V_A:=H^1(A(\mathbb{C}),\mathbb{Q})$ with this decomposition: a pure rational Hodge structure of weight $1$ with Hodge numbers $h^{1,0}=h^{0,1}=g$ (all other $h^{p,q}=0$). In filtration form its Hodge filtration is $F^p=H^1(A(\mathbb{C}),\mathbb{C})$ for $p\le 0$, $F^1=H^{1,0}$, $F^p=0$ for $p\ge 2$. It is the rationalization of the integral Hodge structure on the lattice $H^1(A(\mathbb{C}),\mathbb{Z})=\operatorname{Hom}(\Lambda,\mathbb{Z})$. Its Weil operator $C$ (equal to $i$ on $H^{1,0}$ and $-i$ on $H^{0,1}$) is given on $H^1(A(\mathbb{C}),\mathbb{R})=\operatorname{Hom}_{\mathbb{R}}(T_0,\mathbb{R})$ by $(C\alpha)(v)=\alpha(iv)$.

**Proposition 12.3 (holomorphic differentials).** For $\omega\in H^0(A,\Omega^1_{A/\mathbb{C}})$ the analytification $\omega^{\mathrm{an}}$ is a closed, translation-invariant holomorphic $1$-form, so $\omega^{\mathrm{an}}$ is determined by its value $\omega_0\in\operatorname{Hom}_{\mathbb{C}}(T_0,\mathbb{C})$ at $0$, and its de Rham class is $\lambda\mapsto\int_{\gamma_\lambda}\omega^{\mathrm{an}}=\omega_0(\lambda)$. Hence $\omega\mapsto[\omega^{\mathrm{an}}]$ is an isomorphism $H^0(A,\Omega^1_{A/\mathbb{C}})\xrightarrow{\ \sim\ }H^{1,0}$. Likewise $H^{0,1}\cong H^1(A,\mathcal{O}_A)$ via Dolbeault cohomology. (GAGA, plus Liouville: the coefficients of a holomorphic $1$-form pulled back to $T_0$ are $\Lambda$-periodic, hence constant.)

**Definition 12.4 (the polarization attached to an ample line bundle).** Let $L$ be an ample line bundle on $A$ and $c_1(L)\in H^2(A(\mathbb{C}),\mathbb{Z})$ the first Chern class of $L^{\mathrm{an}}$, normalized so that $\langle c_1(L),[C]\rangle=\deg(L|_C)$ for every smooth projective curve $C\subseteq A$ (equivalently, the connecting map of $0\to\mathbb{Z}\to\mathcal{O}\xrightarrow{\exp(2\pi i\,\cdot)}\mathcal{O}^\times\to0$). Let $[A(\mathbb{C})]\in H_{2g}(A(\mathbb{C}),\mathbb{Z})$ be the fundamental class for the complex orientation. Define
$$Q_L\colon V_A\times V_A\to\mathbb{Q},\qquad Q_L(\alpha,\beta):=\big\langle \alpha\cup\beta\cup c_1(L)^{g-1},\,[A(\mathbb{C})]\big\rangle .$$

**Proposition 12.5.** $Q_L$ is a polarization of $V_A$: it takes integer values on $H^1(A(\mathbb{C}),\mathbb{Z})$, is alternating and nondegenerate, its $\mathbb{C}$-bilinear extension satisfies $Q_L(H^{1,0},H^{1,0})=0$, and $i\,Q_L(\alpha,\overline{\alpha})>0$ for every nonzero $\alpha\in H^{1,0}$. Equivalently, on $H^1(A(\mathbb{C}),\mathbb{R})$: $Q_L(C\alpha,C\beta)=Q_L(\alpha,\beta)$ and $Q_L(C\alpha,\alpha)>0$ for $\alpha\neq0$. In particular $V_A$ is a polarizable Hodge structure. (Hodge--Riemann bilinear relations, since $c_1(L)$ is represented by a Kähler form and $H^1$ is primitive; or directly from the Riemann relations, Mumford loc. cit. Chapter I, Birkenhake--Lange Ch. 4.)

*Remarks.*

- For a formaliser the simplest model is: $\Lambda=\ker(\exp)$, $V_A:=\operatorname{Hom}_{\mathbb{Z}}(\Lambda,\mathbb{Q})$, $V_A\otimes\mathbb{C}=\operatorname{Hom}_{\mathbb{R}}(T_0,\mathbb{C})$, $F^1=\operatorname{Hom}_{\mathbb{C}}(T_0,\mathbb{C})$. This fits Tau Ceti's filtration-style `HodgeStructure` of weight $1$ (effective), and the effective weight-one Hodge structures on $\operatorname{Hom}(\Lambda,\mathbb{Z})$ correspond to complex structures on $\Lambda\otimes\mathbb{R}$; here the complex structure is the one of $T_0$, transported to the dual through $C\alpha=\alpha(i\,\cdot)$.
- Dual convention: many sources (Deligne; Shimura-variety literature) use $H_1(A(\mathbb{C}),\mathbb{Q})=\Lambda\otimes\mathbb{Q}$, the dual Hodge structure, of weight $-1$ and type $\{(-1,0),(0,-1)\}$, with $T_0\cong H_1(A(\mathbb{C}),\mathbb{C})/F^0$. The two have the same Mumford--Tate group (Definition #13) under $g\mapsto (g^{\vee})^{-1}$. [2025, 202(3), no. 3] takes $V_B=H^1_B(A(\mathbb{C}),\mathbb{Q})$ and says it has "type $((0,-1),(-1,0))$": they list the exponents of the characters of the Deligne torus acting on $V_B\otimes\mathbb{C}$, which with the convention $h(z)|_{V^{p,q}}=z^{-p}\bar z^{-q}$ of Definition #13 are $(-1,0)$ and $(0,-1)$, consistent with the above.
- The class $c_1(L)\in H^2=\bigwedge^2\operatorname{Hom}(\Lambda,\mathbb{Z})$ is also often recorded as an alternating *Riemann form* $E_L$ on $\Lambda$, invariant under $i$ with $E_L(iu,u)>0$ for $u\neq0$ in Mumford's convention ($H=E_L(i\cdot,\cdot)+iE_L$ positive definite Hermitian); the sign depends on the conventions for $c_1$ and for $H^2\cong\bigwedge^2H^1$, so it is safest to fix signs by the intrinsic condition $iQ(\alpha,\overline\alpha)>0$ on $H^{1,0}$. The papers only need *some* polarization (equivalently: $V_A$ is polarizable), not a specific one; $Q_L$ depends only on the polarization $\phi_L\colon A\to A^\vee$.
- Use in the Annals papers: [2025, 202(3), no. 3] uses $V_B$ only to define the Mumford--Tate group $\mathbf{G}$ of $A$ (for $A$ over a number field $E\subset\mathbb{C}$, applied to $A_{\mathbb{C}}$), and its étale comparison $V_B\otimes\mathbb{Q}_\ell\cong H^1_{\mathrm{\acute et}}(A_{\overline E},\mathbb{Q}_\ell)$. The arXiv PDF of [2020, 191(2), no. 7] was not available to check its conventions.

## 13. Mumford--Tate group of a rational Hodge structure

*Chapter context.* A chapter on Mumford--Tate groups in a graduate text on Hodge theory and its arithmetic applications (in the spirit of Deligne's *Hodge cycles on abelian varieties*, Milne's *Introduction to Shimura varieties*, or Green--Griffiths--Kerr's *Mumford--Tate Groups and Domains*). The reader knows linear algebraic groups over fields of characteristic $0$ (affine group schemes of finite type, closed subgroups, base change, identity components, reductive groups), the Deligne torus $\mathbb{S}=\operatorname{Res}_{\mathbb{C}/\mathbb{R}}\mathbb{G}_m$, and pure rational Hodge structures with their duals, tensor products, Tate twists and polarizations. The homomorphism $h$, Hodge tensors and the Mumford--Tate group are introduced here.

Throughout, $V$ is a finite-dimensional $\mathbb{Q}$-vector space carrying a pure Hodge structure of weight $w\in\mathbb{Z}$: $V_{\mathbb{C}}=V\otimes_{\mathbb{Q}}\mathbb{C}=\bigoplus_{p+q=w}V^{p,q}$ with $\overline{V^{p,q}}=V^{q,p}$. We write $\mathrm{GL}_V$ for the algebraic group over $\mathbb{Q}$ with $\mathrm{GL}_V(R)=\operatorname{Aut}_R(V\otimes_{\mathbb{Q}}R)$ for $\mathbb{Q}$-algebras $R$. Recall $\mathbb{S}(\mathbb{R})=\mathbb{C}^\times$, and $\mathbb{S}_{\mathbb{C}}\cong\mathbb{G}_m\times\mathbb{G}_m$ so that $z\in\mathbb{S}(\mathbb{R})$ maps to $(z,\bar z)$.

**Definition 13.1 ($h$ and the Hodge cocharacter).** The Hodge structure determines the homomorphism of real algebraic groups $h\colon\mathbb{S}\to\mathrm{GL}_{V,\mathbb{R}}$ such that, for $z\in\mathbb{C}^\times=\mathbb{S}(\mathbb{R})$, $h(z)$ acts on $V^{p,q}$ as multiplication by $z^{-p}\bar z^{-q}$ (this endomorphism of $V_{\mathbb{C}}$ commutes with complex conjugation, so lies in $\mathrm{GL}(V_{\mathbb{R}})$). On complex points, $h_{\mathbb{C}}(z_1,z_2)$ acts on $V^{p,q}$ by $z_1^{-p}z_2^{-q}$. The *Hodge cocharacter* is $\mu=\mu_h\colon\mathbb{G}_{m,\mathbb{C}}\to\mathrm{GL}_{V,\mathbb{C}}$, $\mu(z)=h_{\mathbb{C}}(z,1)$, acting on $V^{p,q}$ by $z^{-p}$. The restriction of $h$ to $\mathbb{G}_{m,\mathbb{R}}\subset\mathbb{S}$ (that is, $r\in\mathbb{R}^\times$) is the *weight cocharacter* $r\mapsto r^{-w}\cdot\mathrm{id}_V$.

**Definition 13.2 (Mumford--Tate group).** The *Mumford--Tate group* $\mathrm{MT}(V)$ is the smallest algebraic subgroup $M\subseteq\mathrm{GL}_V$ defined over $\mathbb{Q}$ (closed subgroup scheme) such that $h$ factors through $M_{\mathbb{R}}$, i.e. $h(z)\in M(\mathbb{R})$ for all $z\in\mathbb{C}^\times$. Concretely, fix a $\mathbb{Q}$-basis of $V$, so that $\mathbb{Q}[\mathrm{GL}_V]=\mathbb{Q}[x_{ij},\det^{-1}]$, and put
$$I_V:=\{\,f\in\mathbb{Q}[\mathrm{GL}_V]\;:\;f(h(z))=0\ \text{for all } z\in\mathbb{C}^\times\,\}.$$
Then $\mathrm{MT}(V)$ is the closed subscheme $\operatorname{Spec}\mathbb{Q}[\mathrm{GL}_V]/I_V$; for every $\mathbb{Q}$-algebra $R$, $\mathrm{MT}(V)(R)=\{g\in\mathrm{GL}(V\otimes R): f(g)=0 \text{ for all } f\in I_V\}$. For an abelian variety $A$ over $\mathbb{C}$ (or over a subfield of $\mathbb{C}$), the *Mumford--Tate group of $A$* is $\mathrm{MT}(A):=\mathrm{MT}(V_A)$ for the Hodge structure $V_A=H^1(A(\mathbb{C}),\mathbb{Q})$ of Definition #12.

**Proposition 13.3 (well-definedness and first properties).**

(a) $I_V$ is a Hopf ideal, and $\mathrm{MT}(V)$ is the intersection of all algebraic subgroups $M\subseteq\mathrm{GL}_V$ with $h(\mathbb{C}^\times)\subseteq M(\mathbb{R})$, which is again such a subgroup (it is the Zariski closure over $\mathbb{Q}$ of $h(\mathbb{C}^\times)$). Since $\mathbb{S}(\mathbb{R})$ is Zariski dense in $\mathbb{S}$, "$h(\mathbb{C}^\times)\subseteq M(\mathbb{R})$" is equivalent to "$h$ factors through $M_{\mathbb{R}}$".

(b) $\mathrm{MT}(V)$ is equally the smallest algebraic $\mathbb{Q}$-subgroup $M$ with $\mu(\mathbb{C}^\times)\subseteq M(\mathbb{C})$ (as $M_{\mathbb{C}}$ is stable under complex conjugation, it then contains $\bar\mu$, and $\mu,\bar\mu$ generate $h_{\mathbb{C}}(\mathbb{S}_{\mathbb{C}})$).

(c) $\mathrm{MT}(V)$ is connected, and contains the image of the weight cocharacter; in particular, if $w\neq0$ then $\mathrm{MT}(V)$ contains the scalars $\mathbb{G}_m\subseteq\mathrm{GL}_V$.

(d) If $V$ is polarizable, $\mathrm{MT}(V)$ is reductive. For $V=V_A$ and any polarization $Q$ of $V_A$, $\mathrm{MT}(A)\subseteq\mathrm{GSp}(V_A,Q)$, since $Q(h(z)x,h(z)y)=|z|^{-2}Q(x,y)$.

**Definition 13.4 (Hodge tensors).** For $m,n\ge0$ let $T^{m,n}=V^{\otimes m}\otimes(V^\vee)^{\otimes n}$ with its induced Hodge structure of weight $(m-n)w$ and its natural $\mathrm{GL}_V$-action. A *Hodge tensor* (Hodge class of type $(0,0)$) is an element $t\in T^{m,n}$ such that $t\otimes1\in(T^{m,n}_{\mathbb{C}})^{0,0}$; equivalently $h(z)t=t$ for all $z\in\mathbb{C}^\times$. Nonzero Hodge tensors can exist only if $(m-n)w=0$.

**Proposition 13.5 (tensor and Tannakian descriptions).** (a) Every element of $\mathrm{MT}(V)(R)$, for every $\mathbb{Q}$-algebra $R$, fixes every Hodge tensor; a $\mathbb{Q}$-subspace of $T^{m,n}$ (or of a finite direct sum of such spaces) is a sub-Hodge structure if and only if it is $\mathrm{MT}(V)$-stable.

(b) If $V$ is polarizable, then $\mathrm{MT}(V)$ is exactly the subgroup of $\mathrm{GL}_V$ fixing all Hodge tensors:
$$\mathrm{MT}(V)(R)=\{\,g\in\mathrm{GL}(V\otimes R)\;:\;g(t\otimes1)=t\otimes1\ \text{for all } m,n\ge0 \text{ and all Hodge tensors } t\in T^{m,n}\,\},$$
and finitely many Hodge tensors suffice. If $w\neq0$ only the spaces $T^{r,r}$ contribute.

(c) $\mathrm{MT}(V)$ is the Tannakian group of the smallest Tannakian subcategory $\langle V\rangle^{\otimes}$ of rational Hodge structures containing $V$ (closed under $\oplus$, $\otimes$, duals and subquotients) with the forgetful fibre functor: restriction along $h$ gives an equivalence $\operatorname{Rep}_{\mathbb{Q}}(\mathrm{MT}(V))\simeq\langle V\rangle^{\otimes}$.

(These are standard: Deligne, *Hodge cycles on abelian varieties* (in Deligne--Milne--Ogus--Shih, LNM 900); (b) follows from (a), Chevalley's theorem and reductivity.)

*Remarks.*

- *Sign conventions are irrelevant for the group.* Many authors let $h(z)$ act on $V^{p,q}$ by $z^{p}\bar z^{q}$ instead; this replaces $h$ by $h(z^{-1})$, which has the same image, so $\mathrm{MT}(V)\subseteq\mathrm{GL}_V$ is unchanged. Likewise $\mathrm{MT}(V^\vee)$ is the image of $\mathrm{MT}(V)$ under $g\mapsto(g^\vee)^{-1}$, so using $H_1$ instead of $H^1$ of an abelian variety gives the "same" group.
- *Variant with a $\mathbb{G}_m$ factor.* Some sources define the Mumford--Tate group inside $\mathrm{GL}_V\times\mathbb{G}_m$, as $\mathrm{MT}(V\oplus\mathbb{Q}(1))$, so that Hodge classes in Tate twists $T^{m,n}(r)$ are also fixed. For $V$ polarizable of weight $w\neq0$ its projection to $\mathrm{GL}_V$ is an isogeny onto $\mathrm{MT}(V)$ (kernel in $\mu_w$), an isomorphism for $V=V_A$. The *Hodge group* (special Mumford--Tate group) $\mathrm{Hg}(V)$ is the smallest $\mathbb{Q}$-subgroup whose real points contain $h(\{|z|=1\})$; for $w\neq0$, $\mathrm{MT}(V)=\mathbb{G}_m\cdot\mathrm{Hg}(V)$, and for abelian varieties $\mathrm{Hg}(A)=(\mathrm{MT}(A)\cap\mathrm{Sp}(V_A,Q))^{0}$.
- *Use in the Annals papers.* [2025, 202(3), no. 3] (Definition 6.1.2 there) defines $\mathbf{G}$ as the smallest $\mathbb{Q}$-subgroup of $\mathrm{GL}(V_B)$, $V_B=H^1_B(A(\mathbb{C}),\mathbb{Q})$, whose complex points contain the image of $\mu$, and also uses both the Tannakian description and the description as the stabilizer of the Hodge cycles in $V_B^{\otimes r}\otimes(V_B^\vee)^{\otimes r}$; these agree with Definition 13.2 by Propositions 13.3(b) and 13.5. There $A$ is defined over a number field $E\subset\mathbb{C}$ and $\mathbf{G}$ depends on the embedding. The arXiv PDF of [2020, 191(2), no. 7] was not available to check its conventions.
- For a formaliser: the definition needs only the ideal $I_V$ (polynomials with rational coefficients in the matrix entries and $\det^{-1}$ vanishing on the real matrices $h(z)$); "smallest" is then automatic. Reductivity and the tensor description are theorems, not part of the definition.

## 14. The volume form $\omega^n$ and integration on a compact Kähler (or Hermitian) manifold

*Chapter context.* An early chapter on Hermitian and Kähler metrics in a graduate text on complex geometry and complex Monge--Ampère equations (in the style of Huybrechts' *Complex Geometry* or Demailly's *Complex Analytic and Differential Geometry*). The reader knows complex manifolds, holomorphic coordinates, the bundles $T^{1,0}X$, differential forms of type $(p,q)$ and the operators $\partial,\bar\partial$, orientations and integration of top-degree forms and the Riemannian volume measure on smooth manifolds; Hermitian and Kähler forms, the top power $\omega^n$ and the associated measure are introduced here.

Throughout, $X$ is a complex manifold of complex dimension $n\ge1$; in local holomorphic coordinates $z^j=x^j+iy^j$ ($1\le j\le n$). We give $X$ its *canonical orientation*, in which $dx^1\wedge dy^1\wedge\cdots\wedge dx^n\wedge dy^n$ is positive (well defined, since a holomorphic change of coordinates has real Jacobian $|\det(\partial w/\partial z)|^2>0$).

**Definition 14.1 (Hermitian and Kähler forms).** A *real $(1,1)$-form* on $X$ is a smooth real $2$-form which in every holomorphic chart reads
$$\alpha=i\sum_{j,k=1}^n a_{\bar kj}\,dz^j\wedge d\bar z^k,\qquad a_{\bar jk}=\overline{a_{\bar kj}},$$
i.e. the matrix $(a_{\bar kj})$ is Hermitian at each point. It is *positive* if $\sum_{j,k}a_{\bar kj}\xi^j\bar\xi^k>0$ for every point and every $\xi\in\mathbb{C}^n\setminus\{0\}$, and *non-negative* if $\ge0$. A positive real $(1,1)$-form $\omega=i\sum g_{\bar kj}\,dz^j\wedge d\bar z^k$ is a *Hermitian metric* (or Hermitian form); it is a *Kähler form* if moreover $d\omega=0$. The pair $(X,\omega)$ is then a Hermitian, respectively Kähler, manifold. The *associated Riemannian metric* is $g_\omega(u,v):=\omega(u,Jv)$ for real tangent vectors $u,v$, where $J$ is the complex structure; locally $g_\omega=2\,\mathrm{Re}\sum g_{\bar kj}\,dz^j\otimes d\bar z^k$.

**Proposition 14.2 (the top power).** Let $\omega$ be a Hermitian form and $\omega^n=\omega\wedge\cdots\wedge\omega$ ($n$ factors). In local holomorphic coordinates
$$\omega^n=n!\,\det(g_{\bar kj})\,\prod_{j=1}^n\big(i\,dz^j\wedge d\bar z^j\big)=n!\,2^n\det(g_{\bar kj})\;dx^1\wedge dy^1\wedge\cdots\wedge dx^n\wedge dy^n ,$$
so $\omega^n$ is a nowhere-vanishing, positively oriented real $2n$-form (a volume form). Moreover $\omega^n/n!$ is the Riemannian volume form of $g_\omega$ (Wirtinger). More generally, if $\omega'=i\sum g'_{\bar kj}\,dz^j\wedge d\bar z^k$ is any real $(1,1)$-form, then
$$\omega'^n=\det(h)\,\omega^n,\qquad h^j{}_k:=\sum_m g^{j\bar m}g'_{\bar mk},$$
where $(g^{j\bar m})$ is the inverse matrix of $(g_{\bar kj})$; $h$ is an endomorphism of $T^{1,0}X$, self-adjoint for $\omega$, so its eigenvalues $\lambda_1,\dots,\lambda_n$ are real and $\omega'^n=\lambda_1\cdots\lambda_n\,\omega^n$.

**Definition 14.3 (the measure $\omega^n$, integrals and volume).** Let $\omega$ be a Hermitian form on $X$. The *measure $\omega^n$* is the Borel measure $\mu_\omega$ on $X$ given on a chart domain $U$ with coordinates $z$ and a Borel set $E\subseteq U$ by
$$\mu_\omega(E)=\int_{z(E)}n!\,2^n\det\big(g_{\bar kj}\big)\,d\mathcal{L}^{2n},$$
with $\mathcal{L}^{2n}$ Lebesgue measure on $\mathbb{C}^n=\mathbb{R}^{2n}$ (coordinates $x^1,y^1,\dots,x^n,y^n$); these local definitions agree on overlaps by Proposition 14.2 and the change-of-variables formula, and define a unique Radon measure. Equivalently $\mu_\omega=n!\cdot\mathrm{vol}_{g_\omega}$, where $\mathrm{vol}_{g_\omega}$ is the Riemannian volume measure of $g_\omega$. For a Borel function $u\colon X\to[0,\infty]$, or $u\in L^1(\mu_\omega)$, put
$$\int_X u\,\omega^n:=\int_X u\,d\mu_\omega .$$
If $X$ is compact (and non-empty), the *volume* is $V=V_\omega:=\int_X\omega^n=\mu_\omega(X)\in(0,\infty)$. If $\eta$ is a continuous real $2n$-form, the *ratio* $\eta/\omega^n$ is the unique continuous function $f$ with $\eta=f\,\omega^n$, and $\int_X\eta=\int_X f\,\omega^n$ (this is the usual integral of a top-degree form for the canonical orientation). For instance, for a real function $\varphi$ of class $C^2$ with $\omega_\varphi:=\omega+i\partial\bar\partial\varphi$, the *relative volume* $\omega_\varphi^n/\omega^n$ equals $\det(h_\varphi)=\prod_j\lambda_j[h_\varphi]$ with $h_\varphi$ as in Proposition 14.2 for $\omega'=\omega_\varphi$.

**Proposition 14.4 (cohomological invariance in the Kähler case).** If $X$ is compact and $\omega$, $\omega'$ are closed real $(1,1)$-forms with $\omega'-\omega=i\partial\bar\partial\varphi$ for a $C^2$ function $\varphi$, then $\int_X\omega'^n=\int_X\omega^n$ (Stokes). In particular the volume of a compact Kähler manifold depends only on the class $[\omega]\in H^2(X,\mathbb{R})$. For a merely Hermitian $\omega$ this fails in general.

*Remarks.*

- *Normalizations differ.* Many sources write $\omega=\tfrac{i}{2}\sum g_{\bar kj}dz^j\wedge d\bar z^k$ (then $\omega^n/n!$ is the Euclidean volume for $g_{\bar kj}=\delta_{jk}$), or $\tfrac{i}{2\pi}\sum\cdots$, or integrate against $\omega^n/n!$. The Annals papers use $\omega=i\sum g_{\bar kj}dz^j\wedge d\bar z^k$ (no factor $\tfrac12$) and the measure $\omega^n$ itself, without $n!$. A formaliser must fix one: with the convention above, $\mu_\omega=n!\,\mathrm{vol}_{g_\omega}$ where $g_\omega(u,v)=\omega(u,Jv)$; for $\omega=i\,dz\wedge d\bar z$ on $\mathbb{C}$ one gets $\mu_\omega=2\,\mathcal{L}^2$. Quantities such as $\frac1V\int_X u\,\omega^n$ and the normalisation $\int_X e^{nF}\omega^n=V$ are insensitive to constant factors.
- *Use in the papers.* [2023, 198(1), no. 4] works on a compact Kähler manifold without boundary $(X,\omega_X)$: $V=\int_X\omega_X^n$, entropy $\mathrm{Ent}_p(F)=\frac1V\int_X e^{nF}|F|^p\omega_X^n$, and $V_t=\int_X\omega_t^n$ for $\omega_t=\chi+t\omega_X$ ($\chi$ closed non-negative $(1,1)$, so $\omega_t$ is Kähler for $t>0$). [2024, 200(1), no. 6] works on a compact *Hermitian* manifold $(X,\omega)$ (no closedness), with $\|e^{nF}\|_{L^1(\log L)^p}=\int_X(1+|F|^p)e^{nF}\omega^n$ and $e^{nF}=\omega_\varphi^n/\omega^n$; there Proposition 14.4 is unavailable, which is why the relative volume appears. So the definition must be made for Hermitian, not only Kähler, forms.
- Integrability: on compact $X$, continuous functions are $\mu_\omega$-integrable; $\mu_\omega$ and $\mu_{\omega'}$ are mutually absolutely continuous with continuous positive density $\det(g^{-1}g')$ for two Hermitian forms, so null sets and $L^p$ spaces (not norms) are independent of $\omega$.

## 15. Ball quotients as quasi-projective varieties

*Chapter context.* A chapter on complex hyperbolic space forms in a graduate text on locally symmetric varieties (Hermitian symmetric domains and their arithmetic and non-arithmetic quotients). The reader knows real Lie groups, Haar measure and lattices in locally compact groups, complex analytic spaces and normal complex spaces, complex algebraic varieties, analytification and GAGA, and quotients of complex manifolds by properly discontinuous group actions; the complex ball, its automorphism group, and the algebraic structure on its quotients by lattices are treated here.

Throughout, $n\ge1$ is an integer.

**Definition 15.1 (the ball and $\mathrm{PU}(1,n)$).** On $\mathbb{C}^{n+1}$ let $\langle z,w\rangle=z_0\bar w_0-\sum_{i=1}^n z_i\bar w_i$, a Hermitian form of signature $(1,n)$. Let $\mathrm{U}(1,n)=\{g\in\mathrm{GL}_{n+1}(\mathbb{C}):\langle gz,gw\rangle=\langle z,w\rangle\ \forall z,w\}$ and $G=\mathrm{PU}(1,n)=\mathrm{U}(1,n)/\{\lambda\cdot\mathrm{id}:|\lambda|=1\}$, a connected real Lie group. The *complex $n$-ball* is the open subset
$$X=\mathbb{B}^n=\{[z]\in\mathbb{P}^n(\mathbb{C}):\langle z,z\rangle>0\}\;\cong\;\{w\in\mathbb{C}^n:|w_1|^2+\cdots+|w_n|^2<1\},\qquad [1:w]\leftrightarrow w .$$
$G$ acts on $X$ by $[g]\cdot[z]=[gz]$; this action is faithful, transitive and by biholomorphisms, the stabilizer $K$ of $[1:0:\cdots:0]$ is compact ($K\cong\mathrm{U}(n)$), and $G$ is the full group of biholomorphisms of $X$. Thus $X=G/K$ is the Hermitian symmetric domain of $G$, and the inclusion $X\subset\mathbb{P}^n=X^\vee$ (the compact dual) is the Borel embedding. The *canonical Kähler metric* on $X$ is the $G$-invariant Kähler form $\omega_X=-i\partial\bar\partial\log(1-|w|^2)$ (the Bergman metric up to a positive constant; every $G$-invariant Kähler form is a positive multiple of it).

**Definition 15.2 (lattice).** A *lattice* in $G$ is a discrete subgroup $\Gamma\subseteq G$ such that $\Gamma\backslash G$ carries a finite $G$-invariant Borel measure (equivalently, a Borel fundamental domain for $\Gamma$ in $G$ has finite Haar measure). It is *cocompact* if $\Gamma\backslash G$ is compact.

**Proposition 15.3 (the analytic quotient).** Let $\Gamma\subseteq G$ be a lattice. Then $\Gamma$ acts properly discontinuously on $X$ with finite stabilizers, and the topological quotient $\Gamma\backslash X$, with the sheaf of $\Gamma$-invariant holomorphic functions, is a normal complex space of dimension $n$ (H. Cartan, *Quotient d'un espace analytique par un groupe d'automorphismes*); denote it $S_\Gamma^{\mathrm{an}}$ and let $\pi\colon X\to S^{\mathrm{an}}_\Gamma$ be the quotient map. If $\Gamma$ is torsion-free, it acts freely, $S^{\mathrm{an}}_\Gamma$ is a complex manifold and $\pi$ is a universal covering. Every lattice is finitely generated and (Selberg's lemma) has a torsion-free normal subgroup of finite index $\Gamma'$, and $S^{\mathrm{an}}_\Gamma=(\Gamma/\Gamma')\backslash S^{\mathrm{an}}_{\Gamma'}$.

**Theorem 15.4 (algebraicity; Baily--Borel, Siu--Yau, Mok).** Let $\Gamma\subseteq G$ be a lattice. There are a normal projective variety $S^*_\Gamma$ over $\mathbb{C}$, a finite set $\partial\subseteq S^*_\Gamma$ of closed points (the *cusps*; empty if and only if $\Gamma$ is cocompact), and an isomorphism of complex analytic spaces
$$\phi\colon (S^*_\Gamma\setminus\partial)^{\mathrm{an}}\xrightarrow{\ \sim\ }\Gamma\backslash X .$$
($n=1$: classical; $\Gamma$ arithmetic: Baily--Borel, *Compactification of arithmetic quotients of bounded symmetric domains*; general $\Gamma$, $n\ge2$: Siu--Yau constructed the compactification by adding finitely many normal points, and Mok, *Projective algebraicity of minimal compactifications of complex-hyperbolic space forms of finite volume*, proved it projective, for torsion-free $\Gamma$; the general case follows by taking the quotient by the finite group $\Gamma/\Gamma'$.)

**Proposition 15.5 (uniqueness of the algebraic structure).** If $S_1,S_2$ are quasi-projective complex varieties and $\phi_j\colon S_j^{\mathrm{an}}\xrightarrow{\sim}\Gamma\backslash X$ are isomorphisms of complex spaces, then $\phi_2^{-1}\circ\phi_1$ is the analytification of a (unique) isomorphism of varieties $S_1\cong S_2$. (For torsion-free $\Gamma$: Borel's extension theorem in the arithmetic case, and a big Picard theorem of Deng in general, as in [2023, 197(1), no. 3, Thm. 3.1.12].)

**Definition 15.6 (ball quotient).** Let $\Gamma\subseteq\mathrm{PU}(1,n)$ be a lattice. The *ball quotient* $S_\Gamma=\Gamma\backslash\mathbb{B}^n$ is the normal quasi-projective complex variety $S_\Gamma:=S^*_\Gamma\setminus\partial$ (a Zariski-open subvariety of the projective variety $S^*_\Gamma$, the *minimal* or *Baily--Borel compactification*) together with the identification $\phi\colon S^{\mathrm{an}}_\Gamma\cong\Gamma\backslash X$ of Theorem 15.4. By Proposition 15.5 the pair $(S_\Gamma,\phi)$ is determined up to unique isomorphism by $\Gamma$, so "the" ball quotient is well defined; its *(algebraic) subvarieties* are the closed subvarieties of $S_\Gamma$, and the *uniformizing map* is $\pi\colon X\to S_\Gamma(\mathbb{C})$. If $\Gamma$ is torsion-free, $S_\Gamma$ is smooth.

*Remarks.*

- *Formalisation.* Cleanest is to make the variety part of the data: an *algebraic model* of $\Gamma\backslash X$ is a pair $(S,\phi)$ with $S$ a quasi-projective (normal) variety over $\mathbb{C}$ and $\phi\colon S^{\mathrm{an}}\cong\Gamma\backslash X$; existence (Theorem 15.4, deep for non-arithmetic $\Gamma$) and uniqueness (Proposition 15.5) are separate theorems, and statements about subvarieties of $S_\Gamma$ are independent of the model.
- *Arithmeticity*, as used in [2023, 197(1), no. 3]: $\Gamma$ is arithmetic if there are a semisimple linear algebraic group $\mathbf{G}$ over $\mathbb{Q}$ and a surjective homomorphism with compact kernel $p\colon\mathbf{G}(\mathbb{R})\to G$ such that $\Gamma$ is commensurable with $p(\mathbf{G}(\mathbb{Z}))$ ($\mathbf{G}(\mathbb{Z})$ taken via any faithful representation and lattice). Non-arithmetic lattices are known only for small $n$ (e.g. $n=2,3$, Deligne--Mostow).
- *Totally geodesic subvarieties* (used in the paper's Theorems 1.2.1 and 1.2.2) refer to the Kähler metric on the smooth locus of $S_\Gamma$ induced by $\omega_X$ (on all of $S_\Gamma$ when $\Gamma$ is torsion-free). *Algebraic subvarieties of $X\times S_\Gamma$* (Theorem 1.2.2) are taken with respect to the Borel embedding: irreducible analytic components of $(X\times S_\Gamma)\cap Z$ for algebraic subvarieties $Z\subseteq\mathbb{P}^n\times S_\Gamma$.
- The paper takes $G=\mathrm{PU}(1,n)$ with $n>1$ and arbitrary lattices; since its statements depend only on the commensurability class of $\Gamma$, it assumes $\Gamma$ torsion-free throughout (so $S_\Gamma$ is a smooth quasi-projective variety). It works with "real Shimura data" $(G,X,\Gamma)$, but for $\mathrm{PU}(1,n)$ this is exactly the above. The reviewer should check the extension of Theorem 15.4 and Proposition 15.5 to lattices with torsion via a finite quotient, which is standard but not stated in the paper.

## 16. Rational Chow groups of a Deligne--Mumford stack and the degree of zero-cycles

*Chapter context.* A chapter on intersection theory on Deligne--Mumford stacks (after Vistoli and Kresch) in a graduate text on moduli spaces and Gromov--Witten theory. The reader knows algebraic stacks and Deligne--Mumford (DM) stacks, closed and open substacks, étale atlases, the point space $|\mathcal{M}|$, residual gerbes and geometric points, coarse moduli spaces (Keel--Mori), and Fulton's intersection theory for schemes and algebraic spaces: cycles, the order function $\operatorname{ord}$ of a one-dimensional Noetherian local domain, rational equivalence, proper push-forward, and the degree of zero-cycles on proper schemes. Cycles and rational equivalence on DM stacks and the degree map are defined here.

Throughout, $k$ is a field and $\mathcal{M}$ is a DM stack of finite type over $k$.

**Definition 16.1 (cycles).** An *integral closed substack* of $\mathcal{M}$ is a reduced closed substack $\mathcal{V}$ with $|\mathcal{V}|$ irreducible; these correspond bijectively to the irreducible closed subsets of $|\mathcal{M}|$. Its *dimension* $\dim\mathcal{V}$ is $\dim U$ for any étale surjection $U\to\mathcal{V}$ from a scheme $U$ (every irreducible component of $U$ has this dimension, so it is independent of $U$). For $m\ge0$, $Z_m(\mathcal{M})$ is the free abelian group on the integral closed substacks of dimension $m$; its elements are *$m$-cycles*.

**Definition 16.2 (rational functions and divisors).** Let $\mathcal{V}$ be an integral DM stack of finite type over $k$. Its *function field* is $k(\mathcal{V})=\varinjlim_{\mathcal{V}'}\Gamma(\mathcal{V}',\mathcal{O}_{\mathcal{V}})$, the colimit over the dense open substacks $\mathcal{V}'\subseteq\mathcal{V}$; it is a field. Let $f\in k(\mathcal{V})^\times$ and let $\mathcal{W}\subseteq\mathcal{V}$ be an integral closed substack with $\dim\mathcal{W}=\dim\mathcal{V}-1$. Choose an étale morphism $u\colon U\to\mathcal{V}$ from an integral scheme $U$ with $\mathcal{W}\times_{\mathcal{V}}U\ne\emptyset$ and an irreducible component $W'$ of $\mathcal{W}\times_{\mathcal{V}}U$, and set
$$\operatorname{ord}_{\mathcal{W}}(f):=\operatorname{ord}_{W'}(u^*f)\in\mathbb{Z},$$
the order of $u^*f\in k(U)^\times$ in the one-dimensional local domain $\mathcal{O}_{U,W'}$. This is independent of $(U,u,W')$, because étale local homomorphisms of one-dimensional Noetherian local domains preserve lengths of $A/aA$. Only finitely many $\mathcal{W}$ have $\operatorname{ord}_{\mathcal{W}}(f)\ne0$, and $\operatorname{div}(f):=\sum_{\mathcal{W}}\operatorname{ord}_{\mathcal{W}}(f)[\mathcal{W}]\in Z_{\dim\mathcal{V}-1}(\mathcal{V})$.

**Definition 16.3 (rational Chow groups).** Let $R_m(\mathcal{M})\subseteq Z_m(\mathcal{M})$ be the subgroup generated by the cycles $\operatorname{div}(f)$, for $\mathcal{V}\subseteq\mathcal{M}$ an integral closed substack of dimension $m+1$ and $f\in k(\mathcal{V})^\times$ (pushed forward to $Z_m(\mathcal{M})$ via $\mathcal{V}\subseteq\mathcal{M}$). The *Chow group of $m$-dimensional cycles with rational coefficients* is
$$A_m(\mathcal{M})_{\mathbb{Q}}:=\big(Z_m(\mathcal{M})/R_m(\mathcal{M})\big)\otimes_{\mathbb{Z}}\mathbb{Q},\qquad A_*(\mathcal{M})_{\mathbb{Q}}:=\bigoplus_{m\ge0}A_m(\mathcal{M})_{\mathbb{Q}}.$$

**Proposition 16.4 (comparisons).** (a) If $\mathcal{M}$ is a scheme or algebraic space, $A_*(\mathcal{M})_{\mathbb{Q}}$ is Fulton's Chow group tensored with $\mathbb{Q}$.

(b) (Vistoli.) Suppose $\mathcal{M}$ is separated, with coarse moduli space $p\colon\mathcal{M}\to\overline{M}$. Then $\mathcal{V}\mapsto p(\mathcal{V})$ is a dimension-preserving bijection from integral closed substacks of $\mathcal{M}$ to integral closed subspaces of $\overline{M}$, and $p_*[\mathcal{V}]:=\deg(\mathcal{V}/p(\mathcal{V}))\,[p(\mathcal{V})]$ induces an isomorphism $p_*\colon A_*(\mathcal{M})_{\mathbb{Q}}\xrightarrow{\sim}A_*(\overline{M})_{\mathbb{Q}}$. Here $\deg(\mathcal{V}/p(\mathcal{V}))\in\mathbb{Q}_{>0}$; if $\operatorname{char}k=0$ it equals $1/e_{\mathcal{V}}$, where $e_{\mathcal{V}}$ is the order of the automorphism group of a geometric generic point of $\mathcal{V}$.

(c) The groups of Definition 16.3 are Vistoli's rational Chow groups; for DM stacks Kresch's Chow groups (*Cycle groups for Artin stacks*) and, for quotient stacks with finite stabilizers, Edidin--Graham's equivariant Chow groups agree with them after tensoring with $\mathbb{Q}$.

**Definition 16.5 (degree of a zero-cycle).** The integral closed substacks of dimension $0$ are the residual gerbes $\mathcal{G}_x$ of the closed points $x\in|\mathcal{M}|$. Let $k(x)$ be the residue field of $x$ (so $\mathcal{G}_x$ is a gerbe over $\operatorname{Spec}k(x)$, and $[k(x):k]<\infty$), and let $\operatorname{Aut}(\bar x)$ be the automorphism group of a geometric point $\bar x\colon\operatorname{Spec}\Omega\to\mathcal{M}$ lying over $x$, a finite group because $\mathcal{M}$ is DM (its order does not depend on $\bar x$). Define
$$\deg[\mathcal{G}_x]:=\frac{[k(x):k]}{|\operatorname{Aut}(\bar x)|}\in\mathbb{Q}_{>0},$$
and extend $\mathbb{Q}$-linearly to $\deg\colon Z_0(\mathcal{M})_{\mathbb{Q}}\to\mathbb{Q}$. If $k$ is algebraically closed, $k(x)=k$ and $\deg[\mathcal{G}_x]=1/|\operatorname{Aut}(x)|$; for instance $\deg[B G]=1/|G|$ for a finite group $G$.

**Theorem 16.6 (the degree map).** If $\mathcal{M}$ is proper over $k$, then $\deg$ vanishes on $R_0(\mathcal{M})_{\mathbb{Q}}$ and so induces a $\mathbb{Q}$-linear map
$$\deg=\int_{\mathcal{M}}\colon A_0(\mathcal{M})_{\mathbb{Q}}\to\mathbb{Q}.$$
It satisfies $\deg=\deg_{\overline M}\circ p_*$ with $p$ as in 16.4(b), and $\deg(f_*\alpha)=\deg(\alpha)$ for proper $f\colon\mathcal{M}\to\mathcal{N}$ of proper DM stacks. For $\alpha\in A_*(\mathcal{M})_{\mathbb{Q}}$ one writes $\int_{\alpha}1:=\deg(\alpha_0)$, $\alpha_0$ the component of $\alpha$ in $A_0(\mathcal{M})_{\mathbb{Q}}$. (Vistoli, *Intersection theory on algebraic stacks and on their moduli spaces*.)

*Remarks.*

- *Use in the Annals paper.* In [2021, 194(3), no. 1], $N_{g,d}=\int_{[\overline{\mathcal{M}}_g(Q,d)]^{\mathrm{vir}}}1$, where $\overline{\mathcal{M}}_g(Q,d)$ is the proper DM stack (over $\mathbb{C}$) of stable maps to the quintic threefold and $[\,\cdot\,]^{\mathrm{vir}}\in A_0(\overline{\mathcal{M}}_g(Q,d))_{\mathbb{Q}}$ is its virtual class (Behrend--Fantechi, Li--Tian; virtual dimension $0$ for a Calabi--Yau threefold and no markings). So $N_{g,d}\in\mathbb{Q}$ is $\deg$ of that class. Integrals with insertions, and the torus-equivariant (localized) classes used in that paper, need further structure (Chern classes acting on $A_*$, equivariant Chow groups) not defined here.
- *Formalisation.* Over $k=\mathbb{C}$ all residue fields of closed points are $\mathbb{C}$. A shortcut is to *define* $A_*(\mathcal{M})_{\mathbb{Q}}:=A_*(\overline M)_{\mathbb{Q}}$ and $\deg:=\deg_{\overline M}$ via Proposition 16.4(b), but then $p_*$ (with its factors $1/e_{\mathcal{V}}$) must be used to compare cycles on $\mathcal{M}$; for $\overline{\mathcal{M}}_g(Q,d)$ the coarse space is a projective scheme.
- Integral Chow groups of stacks differ between sources (Vistoli's "naive" groups, Kresch, Edidin--Graham); only rational coefficients are needed here, and then all agree. A reviewer may want to double-check that Vistoli's rational equivalence is literally the naive one of Definition 16.3; in any case they agree after $\otimes\mathbb{Q}$ via 16.4(b).

## 17. Cohomologically affine morphisms of algebraic stacks

*Chapter context.* A chapter on good moduli spaces and linearly reductive groups in a graduate text on algebraic stacks (following Alper, *Good moduli spaces for Artin stacks*). The reader knows algebraic stacks and their morphisms, the properties quasi-compact, quasi-separated and affine for morphisms, quotient stacks $[X/G]$ and classifying stacks $BG$, and the abelian category $\mathrm{QCoh}(\mathcal{X})$ of quasi-coherent sheaves on an algebraic stack (on the lisse-étale site, or as cartesian modules on a smooth presentation) with push-forward and flat base change. Cohomologically affine morphisms and linearly reductive groups are defined here.

**Proposition 17.1 (push-forward).** Let $f\colon\mathcal{X}\to\mathcal{Y}$ be a quasi-compact and quasi-separated morphism of algebraic stacks. Then $f_*$ carries quasi-coherent sheaves to quasi-coherent sheaves, giving a left exact additive functor $f_*\colon\mathrm{QCoh}(\mathcal{X})\to\mathrm{QCoh}(\mathcal{Y})$, right adjoint to $f^*$. For every flat morphism $g\colon\mathcal{Y}'\to\mathcal{Y}$, with base change $f'\colon\mathcal{X}'=\mathcal{X}\times_{\mathcal{Y}}\mathcal{Y}'\to\mathcal{Y}'$ and $g'\colon\mathcal{X}'\to\mathcal{X}$, the base change map $g^*f_*\mathcal{F}\to f'_*g'^*\mathcal{F}$ is an isomorphism. In particular, for $\mathcal{Y}'=\operatorname{Spec}A$ affine and flat over $\mathcal{Y}$, $\Gamma(\operatorname{Spec}A,g^*f_*\mathcal{F})=\Gamma(\mathcal{X}',g'^*\mathcal{F})$.

**Definition 17.2 (cohomologically affine).** A morphism $f\colon\mathcal{X}\to\mathcal{Y}$ of algebraic stacks is *cohomologically affine* if

1. $f$ is quasi-compact,
2. $f$ is quasi-separated, and
3. the functor $f_*\colon\mathrm{QCoh}(\mathcal{X})\to\mathrm{QCoh}(\mathcal{Y})$ is exact; since it is always left exact, this means: for every epimorphism $\mathcal{F}\to\mathcal{G}$ in $\mathrm{QCoh}(\mathcal{X})$, the map $f_*\mathcal{F}\to f_*\mathcal{G}$ is an epimorphism in $\mathrm{QCoh}(\mathcal{Y})$.

An algebraic stack $\mathcal{X}$ is *cohomologically affine* if $\mathcal{X}\to\operatorname{Spec}\mathbb{Z}$ is; for qcqs $\mathcal{X}$ this says that $\Gamma(\mathcal{X},-)\colon\mathrm{QCoh}(\mathcal{X})\to\mathrm{Ab}$ is exact.

**Definition 17.3 (linearly reductive group).** Let $k$ be a field and $G$ an affine group scheme of finite type over $k$. Then $G$ is *linearly reductive* if the morphism $BG\to\operatorname{Spec}k$ is cohomologically affine. Since $\mathrm{QCoh}(BG)$ is equivalent to the category of (possibly infinite-dimensional) representations of $G$ on $k$-vector spaces, with push-forward to $\operatorname{Spec}k$ given by $V\mapsto V^G$, this says that the invariants functor $V\mapsto V^G$ is exact on all representations; equivalently, every finite-dimensional representation of $G$ is a direct sum of irreducible ones.

**Proposition 17.4 (basic properties).** (Alper, loc. cit., Section 3.)

(a) Affine morphisms are cohomologically affine. A qcqs morphism of algebraic spaces is cohomologically affine if and only if it is affine (Serre's criterion).

(b) If $f\colon\mathcal{X}\to\mathcal{Y}$ is qcqs and $g\colon\mathcal{Y}'\to\mathcal{Y}$ is faithfully flat, and the base change $f'$ is cohomologically affine, then so is $f$ (by flat base change, Proposition 17.1). Conversely cohomologically affine morphisms are stable under flat base change along affine $g$, and under arbitrary base change when $\mathcal{Y}$ has quasi-affine diagonal.

(c) If $\mathcal{Y}$ has quasi-affine diagonal and $f$ has affine diagonal, then $f$ is cohomologically affine if and only if $Rf_*\colon D^+_{\mathrm{QCoh}}(\mathcal{X})\to D^+_{\mathrm{QCoh}}(\mathcal{Y})$ is t-exact, i.e. $R^if_*\mathcal{F}=0$ for all $i>0$ and all quasi-coherent $\mathcal{F}$; this can fail without the hypotheses.

(d) If $\operatorname{char}k=0$, a smooth affine group $G$ over $k$ is linearly reductive if and only if its identity component is reductive. If $k$ is algebraically closed of characteristic $p>0$, a smooth affine $G$ is linearly reductive if and only if $G^0$ is a torus and $p\nmid|G/G^0|$ (Nagata).

*Remarks.*

- *Use in the Annals paper.* [2020, 191(3), no. 1] recalls Definition 17.2 exactly as above ("a quasi-separated and quasi-compact morphism $f$ is cohomologically affine if $f_*$ on quasi-coherent sheaves is exact") and uses it to define linearly reductive groups (Definition 17.3, hypothesis of its Theorems 1.1 and 1.2) and *good moduli spaces*: a qcqs morphism $\pi\colon\mathcal{X}\to Y$ to an algebraic space $Y$ which is cohomologically affine with $\mathcal{O}_Y\to\pi_*\mathcal{O}_{\mathcal{X}}$ an isomorphism. The GIT quotient $N_x/\!\!/G_x=\operatorname{Spec}(\operatorname{Sym}N_x^\vee)^{G_x}$ in Theorem 1.2 is the good moduli space of $[N_x/G_x]$.
- Exactness is required on *quasi-coherent* sheaves only, not on all $\mathcal{O}_{\mathcal{X}}$-modules of the lisse-étale site. Quasi-separatedness is part of the definition so that $f_*$ preserves quasi-coherence. Some sources formulate (c) as the definition; it is equivalent only under the stated diagonal hypotheses.
- Typical examples: $BG\to\operatorname{Spec}k$ for $G$ finite of order prime to $\operatorname{char}k$, for $G=\mathbb{G}_m$, or for $G=\mathrm{GL}_n$ in characteristic $0$; $[\operatorname{Spec}A/G]\to\operatorname{Spec}A^G$ for linearly reductive $G$. Non-example: $B\mathbb{G}_a\to\operatorname{Spec}k$, and $B\mathbb{Z}/p\to\operatorname{Spec}k$ in characteristic $p$.

## 18. Cup product in étale cohomology

*Chapter context.* A chapter on products and duality in étale cohomology, in a graduate text on the étale cohomology of schemes and of rigid-analytic spaces. The reader knows sites and topoi, sheaves of $\Lambda$-modules for a commutative ring $\Lambda$, their tensor product, sheaf cohomology as right derived functors of global sections, the derived category $D(X_{\mathrm{\acute et}},\Lambda)$ with derived tensor product, the étale site of a scheme and (after Huber) of a rigid-analytic space, inverse images, and Tate twists $\Lambda(d)=\mu_n^{\otimes d}$ for $\Lambda=\mathbb{Z}/n$ with $n$ invertible. Cup products are defined here.

Throughout, $X$ is a scheme or a rigid-analytic space over a non-archimedean field $K$ (an adic space locally of finite type over $\operatorname{Spa}(K,\mathcal{O}_K)$), $X_{\mathrm{\acute et}}$ its étale site, $\Lambda$ a commutative ring (in the application $\Lambda=\mathbb{F}_p$), and $H^i(X,\mathcal{F})=H^i_{\mathrm{\acute et}}(X,\mathcal{F})=R^i\Gamma(X,\mathcal{F})$ for sheaves $\mathcal{F}$ of $\Lambda$-modules on $X_{\mathrm{\acute et}}$ (computed in $\Lambda$-modules; the result agrees with abelian-sheaf cohomology). $\mathcal{F}\otimes_\Lambda\mathcal{G}$ is the sheafification of $U\mapsto\mathcal{F}(U)\otimes_\Lambda\mathcal{G}(U)$.

**Definition 18.1 (cup product).** Let $\pi$ be the morphism from the topos of $X_{\mathrm{\acute et}}$ to the point, so $R\Gamma(X,-)=R\pi_*$ and $\pi^*$ is the (exact) constant-sheaf functor. For $K,L\in D(X_{\mathrm{\acute et}},\Lambda)$ let
$$R\Gamma(X,K)\otimes^{\mathbf{L}}_\Lambda R\Gamma(X,L)\longrightarrow R\Gamma(X,K\otimes^{\mathbf{L}}_\Lambda L)$$
be the map adjoint to $\pi^*R\pi_*K\otimes^{\mathbf{L}}_\Lambda\pi^*R\pi_*L\to K\otimes^{\mathbf{L}}_\Lambda L$ (tensor product of the two counits). For sheaves $\mathcal{F},\mathcal{G}$ of $\Lambda$-modules and $i,j\ge0$, the *cup product*
$$\cup\colon H^i(X,\mathcal{F})\otimes_\Lambda H^j(X,\mathcal{G})\longrightarrow H^{i+j}(X,\mathcal{F}\otimes_\Lambda\mathcal{G})$$
is the composite of (1) the Künneth map $H^i(M)\otimes_\Lambda H^j(N)\to H^{i+j}(M\otimes^{\mathbf{L}}_\Lambda N)$ for $M=R\Gamma(X,\mathcal{F})$, $N=R\Gamma(X,\mathcal{G})$ (on K-flat representatives: $[a]\otimes[b]\mapsto[a\otimes b]$ for cocycles $a,b$), (2) $H^{i+j}$ of the map above with $K=\mathcal{F}$, $L=\mathcal{G}$, and (3) $H^{i+j}$ of the canonical map $\mathcal{F}\otimes^{\mathbf{L}}_\Lambda\mathcal{G}\to\mathcal{H}^0(\mathcal{F}\otimes^{\mathbf{L}}_\Lambda\mathcal{G})=\mathcal{F}\otimes_\Lambda\mathcal{G}$. If $\Lambda$ is a field, $\otimes^{\mathbf{L}}_\Lambda=\otimes_\Lambda$ on sheaves and step (3) is the identity.

**Proposition 18.2 (characterization).** Assume $\Lambda$ is a field. The cup products are the unique family of $\Lambda$-bilinear maps $H^i(X,\mathcal{F})\times H^j(X,\mathcal{G})\to H^{i+j}(X,\mathcal{F}\otimes_\Lambda\mathcal{G})$, natural in $\mathcal{F}$ and $\mathcal{G}$, such that:

1. for $i=j=0$ it is $(s,t)\mapsto s\otimes t$, $\Gamma(X,\mathcal{F})\times\Gamma(X,\mathcal{G})\to\Gamma(X,\mathcal{F}\otimes\mathcal{G})$;
2. for a short exact sequence $0\to\mathcal{F}'\to\mathcal{F}\to\mathcal{F}''\to0$ with connecting maps $\delta$: $\delta(a\cup b)=\delta a\cup b$ for $a\in H^i(X,\mathcal{F}'')$, $b\in H^j(X,\mathcal{G})$;
3. for a short exact sequence $0\to\mathcal{G}'\to\mathcal{G}\to\mathcal{G}''\to0$: $\delta(a\cup b)=(-1)^i\,a\cup\delta b$ for $a\in H^i(X,\mathcal{F})$, $b\in H^j(X,\mathcal{G}'')$.

(Over a field every such sequence stays exact after tensoring, and uniqueness follows by dimension shifting, embedding sheaves into injectives. For general $\Lambda$ the same holds for sequences that stay exact after tensoring.)

**Proposition 18.3 (properties).** (a) Associativity: $(a\cup b)\cup c=a\cup(b\cup c)$ under $(\mathcal{F}\otimes\mathcal{G})\otimes\mathcal{H}\cong\mathcal{F}\otimes(\mathcal{G}\otimes\mathcal{H})$. (b) Graded commutativity: $a\cup b=(-1)^{ij}\,\tau_*(b\cup a)$ for $a\in H^i$, $b\in H^j$, with $\tau\colon\mathcal{G}\otimes\mathcal{F}\cong\mathcal{F}\otimes\mathcal{G}$ the swap. (c) Functoriality: for a morphism $f\colon Y\to X$ (of schemes, or of adic spaces), $f^*(a\cup b)=f^*a\cup f^*b$ in $H^{i+j}(Y,f^{-1}\mathcal{F}\otimes f^{-1}\mathcal{G})$, using $f^{-1}(\mathcal{F}\otimes\mathcal{G})=f^{-1}\mathcal{F}\otimes f^{-1}\mathcal{G}$. In particular cup products commute with every automorphism of $X$ that is compatible with given isomorphisms $f^{-1}\mathcal{F}\cong\mathcal{F}$, $f^{-1}\mathcal{G}\cong\mathcal{G}$.

*Remarks.*

- *Use in the Annals paper.* In [2025, 201(3), no. 2], Theorem 1.1.4, $X$ is a smooth proper rigid-analytic space of pure dimension $d$ over $K$ of mixed characteristic $(0,p)$, $C=\widehat{\overline K}$, $X_C=X\times_{\operatorname{Spa}(K,\mathcal{O}_K)}\operatorname{Spa}(C,\mathcal{O}_C)$, $\Lambda=\mathbb{F}_p$, $\mathbb{F}_p(d)=\mu_p^{\otimes d}$, and the pairing is $H^i(X_C,\mathbb{F}_p)\otimes_{\mathbb{F}_p}H^{2d-i}(X_C,\mathbb{F}_p(d))\xrightarrow{\cup}H^{2d}(X_C,\mathbb{F}_p\otimes\mathbb{F}_p(d))=H^{2d}(X_C,\mathbb{F}_p(d))$, followed by the trace. Each $\sigma\in\operatorname{Gal}(\overline K/K)$ acts continuously on $C$, hence on $X_C$ (over $X$), compatibly with $\mu_p^{\otimes d}$; by 18.3(c) the cup product is Galois-equivariant. The paper relies on the general cup product on ringed sites as constructed in the Stacks Project (which it cites), also for $R\nu_*\widehat{\mathcal{O}}^+_X$ on the pro-étale site.
- *Signs.* Conventions for the Künneth map and shifts change cup products by signs depending only on $(i,j)$; perfectness of a pairing is insensitive to this. The convention fixed here is the one making 18.2(2)--(3) hold with the signs shown.
- *Formalisation.* The definition makes sense on any site, so one construction serves schemes (étale, fppf, ...) and adic spaces. If cohomology is modelled as $H^i(X,\mathcal{F})=\operatorname{Ext}^i(\Lambda_X,\mathcal{F})$ (as in Mathlib's sheaf cohomology) and $-\otimes_\Lambda\mathcal{G}$ is exact (e.g. $\Lambda$ a field), then $a\cup b$ agrees, up to a sign depending only on $(i,j)$, with the Yoneda composite of $b\in\operatorname{Ext}^j(\Lambda_X,\mathcal{G})$ and $a\otimes\mathcal{G}\in\operatorname{Ext}^i(\mathcal{G},\mathcal{F}\otimes\mathcal{G})$ (by Proposition 18.2).
- *Perfect pairing.* A bilinear map $P\otimes_{\mathbb{F}_p}Q\to\mathbb{F}_p$ of finite-dimensional spaces is perfect if the induced maps $P\to Q^\vee$ and $Q\to P^\vee$ are isomorphisms.

## 19. Enriques surface over an algebraically closed field

*Chapter context.* A chapter on surfaces of Kodaira dimension zero in a graduate text on the classification of algebraic surfaces in arbitrary characteristic (after Bombieri--Mumford; see Cossec--Dolgachev, *Enriques Surfaces I*). The reader knows smooth proper schemes over a field, the canonical (dualizing) sheaf $\omega_Y=\Omega^2_{Y/k}$ of a smooth surface, coherent cohomology and Euler characteristics, intersection numbers and degrees of invertible sheaves on curves, the Picard scheme, and $\ell$-adic étale cohomology; Enriques surfaces are defined here.

Throughout, $k$ is an algebraically closed field of characteristic $p\ge0$, and $\ell$ denotes a prime different from $p$.

**Definition 19.1 (numerical triviality and Betti numbers).** Let $Y$ be a smooth proper $k$-scheme of pure dimension $2$.

(a) An invertible sheaf $\mathcal{L}$ on $Y$ is *numerically trivial* if $\deg(\mathcal{L}|_C)=0$ for every integral closed curve $C\subseteq Y$, where $\deg(\mathcal{L}|_C)=\chi(C,\mathcal{L}|_C)-\chi(C,\mathcal{O}_C)$; equivalently $(\mathcal{L}\cdot\mathcal{M})=0$ for all invertible $\mathcal{M}$, i.e. the class of $\mathcal{L}$ in $\operatorname{Num}(Y)=\operatorname{Pic}(Y)/\{\text{numerically trivial}\}$ is $0$. One writes $c_1=0$ (or $K_Y\equiv0$) when $\omega_Y$ is numerically trivial.

(b) The *$i$-th Betti number* is $b_i(Y)=\dim_{\mathbb{Q}_\ell}H^i_{\mathrm{\acute et}}(Y,\mathbb{Q}_\ell)$, where $H^i_{\mathrm{\acute et}}(Y,\mathbb{Q}_\ell)=\big(\varprojlim_nH^i_{\mathrm{\acute et}}(Y,\mathbb{Z}/\ell^n)\big)\otimes_{\mathbb{Z}_\ell}\mathbb{Q}_\ell$. It is finite and independent of $\ell\ne p$.

**Definition 19.2 (Enriques surface).** An *Enriques surface* over $k$ is a scheme $Y$ such that

1. $Y$ is smooth and proper over $k$, of pure dimension $2$;
2. $h^0(\mathcal{O}_Y):=\dim_kH^0(Y,\mathcal{O}_Y)=1$ (equivalently, $Y$ is connected);
3. the canonical sheaf $\omega_Y$ is numerically trivial;
4. $b_2(Y)=10$.

A morphism of Enriques surfaces is a morphism of $k$-schemes.

**Proposition 19.3 (Bombieri--Mumford).** Let $Y$ be an Enriques surface over $k$. Then $Y$ is projective; $b_1(Y)=b_3(Y)=0$, $b_2(Y)=\rho(Y)=10$; $\operatorname{Num}(Y)$ with the intersection form is an even unimodular lattice of signature $(1,9)$, isomorphic to $U\oplus E_8$ with $U$ the hyperbolic plane and $E_8$ negative definite; $\chi(\mathcal{O}_Y)=1$, $K_Y^2=0$, $c_2(Y)=12$; $h^1(\mathcal{O}_Y)=h^2(\mathcal{O}_Y)\le1$; and the scheme $\operatorname{Pic}^\tau_{Y/k}$ of numerically trivial invertible sheaves is a finite group scheme of order $2$ whose $k$-points are generated by $\omega_Y$. If $p\ne2$, then $\operatorname{Pic}^\tau_{Y/k}\cong\mathbb{Z}/2$, $\omega_Y\not\cong\mathcal{O}_Y$, $\omega_Y^{\otimes2}\cong\mathcal{O}_Y$ and $h^1(\mathcal{O}_Y)=h^2(\mathcal{O}_Y)=0$. If $p=2$, $Y$ is called *classical*, *singular* (also *ordinary*) or *supersingular* according as $\operatorname{Pic}^\tau_{Y/k}$ is $\mathbb{Z}/2$, $\mu_2$ or $\alpha_2$. (Bombieri--Mumford, *Enriques' classification of surfaces in char. p*, II and III; Cossec--Dolgachev.)

*Remarks.*

- *Equivalent formulations.* For $p\ne2$ (in particular over $\mathbb{C}$) Enriques surfaces are exactly the smooth projective surfaces with $h^1(\mathcal{O}_Y)=h^2(\mathcal{O}_Y)=0$ and $\omega_Y^{\otimes2}\cong\mathcal{O}_Y$, $\omega_Y\not\cong\mathcal{O}_Y$; equivalently, quotients of K3 surfaces by a fixed-point-free involution. In characteristic $2$ these descriptions fail (e.g. $\omega_Y\cong\mathcal{O}_Y$ for singular and supersingular surfaces), which is why the characteristic-free definition uses numerical triviality of $\omega_Y$ and $b_2=10$. Among minimal surfaces with numerically trivial canonical sheaf (abelian, bielliptic or quasi-bielliptic, K3, Enriques), the Enriques ones are exactly those with $b_2=10$.
- *Use in the Annals paper.* [2023, 197(1), no. 1], Section 4, takes exactly Definition 19.2 ("a smooth proper scheme $Y$ with $h^0(\mathcal{O}_Y)=1$, $c_1=0$ and $b_2=10$", $c_1=0$ meaning $\omega_Y$ numerically trivial) over algebraically closed fields of every characteristic; the case $p=2$, with the trichotomy of Proposition 19.3 (and the *exceptional* Enriques surfaces of Ekedahl--Shepherd-Barron), is essential there, since the main theorem rests on the non-existence of suitable Enriques surfaces over $\mathbb{F}_2$. Families over rings are Definition #20.
- *Formalisation.* "Surface" means pure dimension $2$; one may instead require $Y$ projective (equivalent by Proposition 19.3, or by the Zariski--Goodman theorem that smooth proper surfaces are projective). Condition 4 can be stated for one fixed $\ell\ne p$. Degrees on curves can be computed through Euler characteristics as in 19.1(a), avoiding a separate intersection theory.

## 20. Families of Enriques surfaces and the moduli stack $\mathscr{M}_{\mathrm{Enr}}$

*Chapter context.* The same chapter as Definition #19 (Enriques surfaces in arbitrary characteristic), in its section on families and moduli. The reader knows algebraic spaces and their morphisms (flat, proper, of finite presentation, smooth), base change, geometric points, the big fppf site $(\mathrm{Aff}/\mathbb{Z})_{\mathrm{fppf}}$, categories fibred in groupoids and stacks; Enriques surfaces over algebraically closed fields are Definition #19.

Throughout, $R$ is a commutative ring and $S=\operatorname{Spec}R$. A *geometric point* of $S$ is a morphism $\bar s\colon\operatorname{Spec}\Omega\to S$ with $\Omega$ an algebraically closed field; for an $S$-algebraic space $\mathfrak{Y}$ its *geometric fibre* is $\mathfrak{Y}_{\bar s}=\mathfrak{Y}\times_S\operatorname{Spec}\Omega$.

**Definition 20.1 (family of Enriques surfaces).** A *family of Enriques surfaces over $R$* is a pair $(\mathfrak{Y},f)$ where $\mathfrak{Y}$ is an algebraic space and $f\colon\mathfrak{Y}\to\operatorname{Spec}R$ is a morphism such that

1. $f$ is flat, proper and of finite presentation, and
2. for every geometric point $\bar s\colon\operatorname{Spec}\Omega\to\operatorname{Spec}R$, the geometric fibre $\mathfrak{Y}_{\bar s}$ is (representable by) a scheme which is an Enriques surface over $\Omega$ in the sense of Definition #19.

An *isomorphism* of families $(\mathfrak{Y},f)\to(\mathfrak{Y}',f')$ over $R$ is an isomorphism of algebraic spaces $\mathfrak{Y}\cong\mathfrak{Y}'$ commuting with $f,f'$. For a ring map $R\to R'$, the *base change* $(\mathfrak{Y}\times_{\operatorname{Spec}R}\operatorname{Spec}R',\,f_{R'})$ is a family over $R'$ (conditions 1 and 2 are stable under base change). When $R=K$ is a field, a family over $K$ is called an *Enriques surface over $K$*.

**Definition 20.2 (the moduli stack).** $\mathscr{M}_{\mathrm{Enr}}$ is the category fibred in groupoids over the category $\mathrm{Aff}/\mathbb{Z}$ of affine schemes whose objects over $\operatorname{Spec}R$ are the families of Enriques surfaces over $R$, and whose morphisms from $(\mathfrak{Y}',f')$ over $\operatorname{Spec}R'$ to $(\mathfrak{Y},f)$ over $\operatorname{Spec}R$ are pairs consisting of a morphism $\operatorname{Spec}R'\to\operatorname{Spec}R$ and an isomorphism of families $\mathfrak{Y}'\cong\mathfrak{Y}\times_{\operatorname{Spec}R}\operatorname{Spec}R'$ over $R'$. Its *fibre category* $\mathscr{M}_{\mathrm{Enr}}(R)$ is the groupoid of families over $R$ and their isomorphisms.

**Proposition 20.3.** (a) $\mathscr{M}_{\mathrm{Enr}}$ is a stack for the fppf topology on $\mathrm{Aff}/\mathbb{Z}$: isomorphisms of families form fppf sheaves, and fppf descent data for families are effective (fppf descent for algebraic spaces, together with fppf-locality of flatness, properness and finite presentation on the base; condition 2 can be checked after any extension of the algebraically closed field $\Omega$).

(b) If $(\mathfrak{Y},f)$ is a family over $R$, then $f$ is smooth of relative dimension $2$ (flat, of finite presentation, with smooth geometric fibres).

(c) The relative Picard functor of a family is representable by a scheme $\operatorname{Pic}_{\mathfrak{Y}/R}$, whose subgroup $\operatorname{Pic}^\tau_{\mathfrak{Y}/R}$ of fibrewise numerically trivial classes is open and finite locally free of rank $2$ over $R$, and $\operatorname{Num}_{\mathfrak{Y}/R}=\operatorname{Pic}_{\mathfrak{Y}/R}/\operatorname{Pic}^\tau_{\mathfrak{Y}/R}$ is a local system of free abelian groups of rank $10$ ([2023, 197(1), no. 1], Proposition 5.3).

*Remarks.*

- *The Annals theorem.* [2023, 197(1), no. 1] defines families exactly as in 20.1 and $\mathscr{M}_{\mathrm{Enr}}$ exactly as in 20.2 (over $(\mathrm{Aff}/\mathbb{Z})$ with the fppf topology), and proves $\mathscr{M}_{\mathrm{Enr}}(\mathbb{Z})=\varnothing$: there is no algebraic space $\mathfrak{Y}$ with a flat, proper, finitely presented $f\colon\mathfrak{Y}\to\operatorname{Spec}\mathbb{Z}$ all of whose geometric fibres (over $\overline{\mathbb{Q}}$ and over $\overline{\mathbb{F}}_p$ for every $p$) are Enriques surfaces. For the statement itself only the objects of $\mathscr{M}_{\mathrm{Enr}}(\mathbb{Z})$ matter; the stack structure (and its algebraicity, which is not needed) plays no role in the statement.
- *Why algebraic spaces.* The total space is allowed to be an algebraic space rather than a scheme, which makes the non-existence statement stronger and makes $\mathscr{M}_{\mathrm{Enr}}$ a stack (fppf descent of schemes need not be effective). Over $\operatorname{Spec}\mathbb{Z}$ a formaliser may first restrict to schemes $\mathfrak{Y}$ as a weaker variant.
- *Representability of fibres.* A smooth proper algebraic space of dimension $2$ over a field is a scheme (Artin), so "is a scheme" in condition 2 is automatic; it is included so that Definition #19 (stated for schemes) applies verbatim. A reviewer may wish to confirm the precise reference.
- Condition 2 quantifies over all geometric points; it suffices to check one geometric point over each point of $\operatorname{Spec}R$ (Definition #19 is invariant under extension of algebraically closed fields).

## 21. Fppf cohomology with supports in a closed subset

*Chapter context.* A chapter on flat (fppf) cohomology of schemes in a graduate text on arithmetic duality and purity (in the spirit of Milne's *Arithmetic Duality Theorems*, Chapter III). The reader knows the big fppf site $(\mathrm{Sch}/X)_{\mathrm{fppf}}$ of a scheme $X$, abelian sheaves on it and their cohomology $H^i(X,\mathcal{F})=H^i_{\mathrm{fppf}}(X,\mathcal{F})$ (right derived functors of $\mathcal{F}\mapsto\mathcal{F}(X)$), cohomology of an object $U$ of the site ($H^i(U,\mathcal{F})=H^i(U,\mathcal{F}|_U)$), and that a commutative group scheme over $X$ defines an fppf sheaf. Cohomology with supports is defined here.

Throughout, $X$ is a scheme, $Z\subseteq X$ is a closed subset, $U=X\setminus Z$ with open immersion $j\colon U\to X$, and $\mathcal{F}$ is an abelian sheaf on $(\mathrm{Sch}/X)_{\mathrm{fppf}}$ (for instance a commutative $X$-group scheme $G$, viewed as the sheaf $T\mapsto G(T)$).

**Definition 21.1 (sections with support and cohomology with supports).** The group of *sections of $\mathcal{F}$ supported in $Z$* is
$$\Gamma_Z(X,\mathcal{F}):=\ker\big(\mathcal{F}(X)\to\mathcal{F}(U)\big).$$
This is a left exact functor from abelian sheaves on $(\mathrm{Sch}/X)_{\mathrm{fppf}}$ to abelian groups. The *fppf cohomology of $X$ with supports in $Z$* is its sequence of right derived functors,
$$H^i_Z(X,\mathcal{F}):=R^i\Gamma_Z(X,\mathcal{F})\qquad(i\ge0),$$
computed with an injective resolution $\mathcal{F}\to\mathcal{I}^\bullet$: $H^i_Z(X,\mathcal{F})=H^i(\Gamma_Z(X,\mathcal{I}^\bullet))$. In derived terms, $R\Gamma_Z(X,\mathcal{F}):=\operatorname{fib}\big(R\Gamma(X,\mathcal{F})\to R\Gamma(U,\mathcal{F})\big)$ in $D(\mathbb{Z})$, and $H^i_Z=H^iR\Gamma_Z$.

**Proposition 21.2 (the long exact sequence).** For an injective abelian sheaf $\mathcal{I}$ the restriction $\mathcal{I}(X)\to\mathcal{I}(U)$ is surjective (as $\mathbb{Z}[h_U]\to\mathbb{Z}[h_X]$ is a monomorphism). Hence $0\to\Gamma_Z(X,\mathcal{I}^\bullet)\to\Gamma(X,\mathcal{I}^\bullet)\to\Gamma(U,\mathcal{I}^\bullet)\to0$ is exact, giving a distinguished triangle $R\Gamma_Z(X,\mathcal{F})\to R\Gamma(X,\mathcal{F})\to R\Gamma(U,\mathcal{F})\xrightarrow{+1}$ and a long exact sequence, natural in $\mathcal{F}$ and in $(X,Z)$:
$$0\to H^0_Z(X,\mathcal{F})\to H^0(X,\mathcal{F})\to H^0(U,\mathcal{F})\to H^1_Z(X,\mathcal{F})\to H^1(X,\mathcal{F})\to H^1(U,\mathcal{F})\to H^2_Z(X,\mathcal{F})\to\cdots.$$
Equivalently, $H^i_Z(X,\mathcal{F})=\operatorname{Ext}^i\big(\mathbb{Z}[h_X]/\mathbb{Z}[h_U],\mathcal{F}\big)$, Ext of abelian fppf sheaves on $\mathrm{Sch}/X$.

**Proposition 21.3 (excision and comparison).** (a) If $V\subseteq X$ is open with $Z\subseteq V$, restriction induces isomorphisms $H^i_Z(X,\mathcal{F})\cong H^i_Z(V,\mathcal{F})$. (b) If $G$ is a smooth commutative quasi-projective $X$-group scheme, the fppf groups $H^i(X,G)$ agree with étale cohomology (Grothendieck, *Le groupe de Brauer III*), and so, by the five lemma applied to 21.2, do the groups with supports; for quasi-coherent coefficients they agree with Zariski cohomology with supports, i.e. Grothendieck's local cohomology.

**Definition 21.4 (the local case).** For a local ring $(R,\mathfrak{m})$ and an abelian fppf sheaf $\mathcal{F}$ on $\operatorname{Spec}R$ (e.g. a commutative, finite, flat $R$-group scheme $G$), put $U_R:=\operatorname{Spec}R\setminus\{\mathfrak{m}\}$ (the punctured spectrum) and
$$H^i_{\mathfrak{m}}(R,\mathcal{F}):=H^i_{\{\mathfrak{m}\}}(\operatorname{Spec}R,\mathcal{F}),$$
so that there is a long exact sequence $\cdots\to H^i_{\mathfrak{m}}(R,G)\to H^i(R,G)\to H^i(U_R,G)\to H^{i+1}_{\mathfrak{m}}(R,G)\to\cdots$, with $H^i(R,G)=H^i_{\mathrm{fppf}}(\operatorname{Spec}R,G)$.

*Remarks.*

- *Use in the Annals paper.* [2024, 199(1), no. 2] (Theorem 1.1.1) uses $H^i_{\mathfrak{m}}(R,G)$ for $R$ a Noetherian local complete intersection and $G$ commutative, finite and flat (hence finite locally free) over $R$, forms all cohomology in the fppf topology, and implicitly identifies it with étale cohomology for smooth coefficients and with Zariski cohomology for quasi-coherent ones (Proposition 21.3(b)). It uses $R\Gamma_Z(-,G)$ systematically, also for animated rings, via the "cohomology with supports triangle" of Proposition 21.2; only the classical case of Definition 21.4 is needed for the main statements.
- *Site conventions.* The groups do not depend on whether one uses $(\mathrm{Sch}/X)_{\mathrm{fppf}}$ or the site of affine $X$-schemes, nor on the universe (or cardinal bound, as in the paper) used to make the big site small. $\Gamma_Z(X,\mathcal{F})$ depends on $Z$ only as a subset; no scheme structure on $Z$ is involved.
- *Formalisation.* With Mathlib's sheaf cohomology $H^i(X,\mathcal{F})$ (Ext from the constant sheaf) on `Scheme.fppfTopology`, the cleanest definitions are $\operatorname{Ext}^i(\mathbb{Z}[h_X]/\mathbb{Z}[h_U],\mathcal{F})$ or the derived fibre; the long exact sequence then comes from the short exact sequence $0\to\mathbb{Z}[h_U]\to\mathbb{Z}[h_X]\to\mathbb{Z}[h_X]/\mathbb{Z}[h_U]\to0$ and $H^i(U,\mathcal{F})=\operatorname{Ext}^i(\mathbb{Z}[h_U],\mathcal{F})$.

## 22. Galois action on the étale cohomology of the geometric fibre

*Chapter context.* This is the chapter on étale cohomology of rigid-analytic spaces in a book on $p$-adic geometry. The reader is assumed to know Huber's adic spaces and fibre products $X\times_{\operatorname{Spa}(K,\mathcal{O}_K)}\operatorname{Spa}(L,\mathcal{O}_L)$. They should also know the étale site $X_{\mathrm{et}}$, its abelian sheaves and their cohomology, and pull-back maps $h^*\colon H^i(Z,\mathcal{G})\to H^i(Y,h^{-1}\mathcal{G})$ for a morphism $h\colon Y\to Z$. The analogous action of $\mathrm{Gal}(\bar k/k)$ on $H^i(X_{\bar k},\mathcal{F})$ for $k$-schemes is also assumed. Here we construct the action of $G_K$ on $H^i(X_C,\mathcal{F})$ for a rigid space $X$ over $K$.

**Notation 22.1.** $K$ is a *non-archimedean field*, i.e. a field complete for a non-trivial rank-one valuation $|\cdot|$, with valuation ring $\mathcal{O}_K$. We fix an algebraic closure $\bar K$, put $G_K:=\mathrm{Gal}(\bar K/K)$ with its Krull topology, and let $C:=\widehat{\bar K}$ be the completion of $\bar K$. A *rigid-analytic $K$-space* is an adic space locally of finite type over $\operatorname{Spa}(K,\mathcal{O}_K)$. For such $X$ and a complete extension $L/K$, write $X_L:=X\times_{\operatorname{Spa}(K,\mathcal{O}_K)}\operatorname{Spa}(L,\mathcal{O}_L)$. Let $\mathrm{pr}\colon X_C\to X$ be the projection.

**Proposition 22.2.** The valuation of $K$ extends uniquely to $\bar K$, so every $\sigma\in G_K$ is an isometry of $\bar K$. Hence $\sigma$ extends uniquely to a continuous ring automorphism of $C$, again written $\sigma$. This extension fixes $K$, is isometric and preserves $\mathcal{O}_C$. Moreover $C$ is algebraically closed (Krasner's lemma), and $\sigma\mapsto\sigma$ identifies $G_K$ with the group of continuous $K$-automorphisms of $C$.

**Definition 22.3.** For $\sigma\in G_K$, let $\operatorname{Spa}(\sigma)\colon\operatorname{Spa}(C,\mathcal{O}_C)\to\operatorname{Spa}(C,\mathcal{O}_C)$ be the automorphism of adic spaces over $\operatorname{Spa}(K,\mathcal{O}_K)$ induced by $\sigma$. Its comorphism on global sections is $\sigma\colon C\to C$. Put
$$\sigma_X:=\mathrm{id}_X\times\operatorname{Spa}(\sigma)\colon X_C\to X_C .$$
This is an automorphism of the adic space $X_C$ over $X$. It is not $C$-linear unless $\sigma=1$. It satisfies $\mathrm{pr}\circ\sigma_X=\mathrm{pr}$, $1_X=\mathrm{id}$ and $(\sigma\tau)_X=\tau_X\circ\sigma_X$, because $\operatorname{Spa}$ is contravariant.

**Definition 22.4 (the Galois action).** Let $\mathcal{F}$ be an abelian sheaf on $X_{\mathrm{et}}$ and put $\mathcal{F}_C:=\mathrm{pr}^{-1}\mathcal{F}$. Since $\mathrm{pr}\circ\sigma_X=\mathrm{pr}$, there is a canonical isomorphism $c_\sigma\colon\sigma_X^{-1}\mathcal{F}_C\xrightarrow{\sim}\mathcal{F}_C$. For $i\ge0$ and $\sigma\in G_K$ define
$$\rho(\sigma)\colon H^i_{\mathrm{et}}(X_C,\mathcal{F}_C)\xrightarrow{\ \sigma_X^*\ }H^i_{\mathrm{et}}(X_C,\sigma_X^{-1}\mathcal{F}_C)\xrightarrow{\ c_\sigma\ }H^i_{\mathrm{et}}(X_C,\mathcal{F}_C),$$
and write $\sigma\cdot c:=\rho(\sigma)(c)$. One abbreviates $H^i_{\mathrm{et}}(X_C,\mathcal{F}):=H^i_{\mathrm{et}}(X_C,\mathcal{F}_C)$. This action of $G_K$ is the *natural Galois action* on the cohomology of the geometric fibre.

The principal coefficients are as follows. If $p$ is invertible in $K$, let $\mu_p$ be the étale sheaf $U\mapsto\{f\in\mathcal{O}_U(U)^\times: f^p=1\}$. It is étale-locally isomorphic to $\mathbb{Z}/p$. Put $\mathbf{F}_p(j):=\mu_p^{\otimes j}$ for $j\ge0$ and $\mathbf{F}_p(j):=\mathcal{H}om(\mu_p^{\otimes(-j)},\mathbb{Z}/p)$ for $j<0$. The sheaves $\mathbb{Z}/\ell^n(j)$, for $\ell$ invertible in $K$, are defined in the same way. Their pull-backs to $X_C$ are the corresponding sheaves on $X_C$.

**Proposition 22.5.**

(a) $\rho$ is a left action, $\rho(\sigma\tau)=\rho(\sigma)\rho(\tau)$, by group automorphisms, which are $\Lambda$-linear if $\mathcal{F}$ is a sheaf of $\Lambda$-modules.
(b) The action is functorial. Pull-back $f_C^*$ along a morphism $f\colon Y\to X$ of rigid $K$-spaces is $G_K$-equivariant, and so is the map induced by a morphism of sheaves on $X_{\mathrm{et}}$. The cup product $H^i(X_C,\mathcal{F})\otimes H^{j}(X_C,\mathcal{G})\to H^{i+j}(X_C,\mathcal{F}\otimes\mathcal{G})$ is $G_K$-equivariant for the diagonal action on the source.
(c) Continuity. Suppose $X$ is quasi-compact and quasi-separated and $\mathcal{F}$ is torsion. Then the natural maps $H^i(X_L,\mathcal{F})\to H^i(X_C,\mathcal{F})$, where $L$ runs over the finite extensions of $K$ in $\bar K$, induce an isomorphism $\varinjlim_L H^i(X_L,\mathcal{F})\xrightarrow{\sim}H^i(X_C,\mathcal{F})$ (Huber's limit theorem). Moreover $G_L$ fixes the image of $H^i(X_L,\mathcal{F})$. Hence every class has an open stabiliser, i.e. $H^i(X_C,\mathcal{F})$ is a discrete $G_K$-module.
(d) Equivalent description. Abelian sheaves on $\operatorname{Spa}(K,\mathcal{O}_K)_{\mathrm{et}}$ are equivalent to discrete $G_K$-modules, via the stalk at the geometric point $\operatorname{Spa}(C,\mathcal{O}_C)\to\operatorname{Spa}(K,\mathcal{O}_K)$. Let $f\colon X\to\operatorname{Spa}(K,\mathcal{O}_K)$ be qcqs. Under this equivalence, $R^if_*\mathcal{F}$ corresponds to $H^i(X_C,\mathcal{F})$ with the action of Definition 22.4.

**Definition 22.6 (Galois-equivariant maps; $\ell$-adic variant).** A homomorphism between $G_K$-modules is *Galois-equivariant* if it commutes with the actions. A fixed abelian group such as $\mathbf{F}_p$ carries the trivial action unless a twist is indicated. Let $X$ be qcqs and $\ell$ a prime invertible in $K$, with $\ell=p$ allowed when $\mathrm{char}\,K=0$. Define
$$H^i(X_C,\mathbb{Z}_\ell(j)):=\varprojlim_n H^i(X_C,\mathbb{Z}/\ell^n(j))$$
with the inverse-limit topology, where each term is discrete. It carries the inverse limit of the actions of 22.4, which is continuous. Put $H^i(X_C,\mathbb{Q}_\ell(j)):=H^i(X_C,\mathbb{Z}_\ell(j))\otimes_{\mathbb{Z}_\ell}\mathbb{Q}_\ell$.

*Remarks.*

(1) Why $C$ and not $\bar K$. $X_{\bar K}$ is not a rigid space, because $\bar K$ is not complete, so the geometric fibre of a rigid space is $X_C$. Let $X$ be a proper $K$-scheme. Then $H^i(X_{\bar K},\mathcal{F})\cong H^i(X_C,\mathcal{F})\cong H^i((X^{\mathrm{an}})_C,\mathcal{F}^{\mathrm{an}})$ for torsion $\mathcal{F}$, by invariance under extension of algebraically closed base field and Huber's comparison theorem. These isomorphisms are $G_K$-equivariant, so the action above extends the scheme-theoretic one.
(2) Twists matter for equivariance. A primitive $p$-th root of unity $\zeta\in C$ gives $\mathbf{F}_p\cong\mu_p$ on $X_C$. Hence $H^i(X_C,\mathbf{F}_p(j))\cong H^i(X_C,\mathbf{F}_p)$ as groups, but not equivariantly. Equivariantly, $H^i(X_C,\mathbf{F}_p(j))\cong H^i(X_C,\mathbf{F}_p)\otimes_{\mathbf{F}_p}\mu_p(\bar K)^{\otimes j}$, where $G_K$ acts on $\mu_p(\bar K)$ by the mod-$p$ cyclotomic character.
(3) Sign conventions. With $\operatorname{Spa}$ contravariant, $\sigma\mapsto\sigma_X^*$ is already a left action. For $X=\operatorname{Spa}(K,\mathcal{O}_K)$ it gives the usual action $\zeta\mapsto\sigma(\zeta)$ on $H^0(X_C,\mu_p)=\mu_p(C)$. Some sources write the action as $(\sigma^{-1})^*$ or $\sigma_*$, depending on how they attach a morphism to $\sigma$. All standard conventions give $\zeta\mapsto\sigma(\zeta)$ on $\mu_p(C)$, and that requirement pins the convention down.
(4) Finiteness. For $X$ smooth and proper, the groups $H^i(X_C,\mathbf{F}_p(j))$ are finite-dimensional. For $\ell=p$ this is Scholze's theorem (P. Scholze, *$p$-adic Hodge theory for rigid-analytic varieties*); for $\ell\neq p$ it is classical (Huber, Berkovich). So the $\mathbb{Z}_\ell$-groups are finitely generated continuous $G_K$-representations. [2025, 201(3), no. 2] uses pro-étale cohomology for $\mathbb{Z}_p$-coefficients, which agrees with the limit above in this situation.
(5) Use in [2025, 201(3), no. 2] (Theorem 1.1.4). There $K$ is a non-archimedean field of mixed characteristic $(0,p)$ and $X$ is a smooth proper rigid $K$-space of pure dimension $d$. The coefficients are $\mathbf{F}_p$ and $\mathbf{F}_p(d)$. The trace $t_X\colon H^{2d}(X_C,\mathbf{F}_p(d))\to\mathbf{F}_p$ is Galois-equivariant for the trivial action on $\mathbf{F}_p$. It is constructed as a map of sheaves $R^{2d}f_*\mathbf{F}_p(d)\to\mathbf{F}_p$ on $\operatorname{Spa}(K,\mathcal{O}_K)_{\mathrm{et}}$, via 22.5(d). The pairing is then equivariant by 22.5(b). The paper writes $X_{\widehat{\overline K}}$ for $X_C$.

## 23. Hodge-generic abelian variety

*Chapter context.* This belongs to a chapter on Mumford–Tate groups of abelian varieties, in a book on Hodge theory and abelian varieties. Assumed known: complex abelian varieties and polarizations; the polarized weight-one rational Hodge structure $V=H^1(A(\mathbb{C}),\mathbb{Q})$ of Definition #12; the Mumford–Tate group $\mathrm{MT}(V)\subseteq\mathrm{GL}(V)$ of a rational Hodge structure (Definition #13); the general symplectic group $\mathrm{GSp}$ with its multiplier. Here: Hodge-genericity of abelian varieties and of families.

**Notation 23.1.** Let $A$ be a complex abelian variety of dimension $g\ge1$. Put $V:=H^1(A(\mathbb{C}),\mathbb{Q})$, of dimension $2g$, with the Hodge structure of Definition #12. A polarization of $A$ (the class of an ample line bundle) determines, as in Definition #12, a non-degenerate alternating form $\psi\colon V\times V\to\mathbb{Q}$. This form is a morphism of Hodge structures $V\otimes V\to\mathbb{Q}(-1)$. Put
$$\mathrm{GSp}(V,\psi):=\{\,g\in\mathrm{GL}(V):\ \exists\,\nu(g)\in\mathbb{G}_m,\ \psi(gx,gy)=\nu(g)\psi(x,y)\ \forall x,y\,\}.$$
This is a connected reductive $\mathbb{Q}$-group. A symplectic basis of $V$ identifies it with $\mathrm{GSp}_{2g}$. Its dimension is $2g^2+g+1$. Write $\mathrm{MT}(A):=\mathrm{MT}(V)$.

**Proposition 23.2.** $\mathrm{MT}(A)$ is a connected reductive $\mathbb{Q}$-subgroup of $\mathrm{GL}(V)$. It contains the scalars $\mathbb{G}_m$ (the weight is $1\neq0$). Moreover $\mathrm{MT}(A)\subseteq\mathrm{GSp}(V,\psi)$ for every polarization form $\psi$, since $\psi$ is a Hodge tensor up to the weight twist. Its commutant in $\mathrm{End}_{\mathbb{Q}}(V)$ is the image of $\mathrm{End}(A)\otimes\mathbb{Q}$ acting on $V$ by pull-back (a ring anti-isomorphism onto it).

**Definition 23.3 (Hodge-generic abelian variety).**

(a) A complex abelian variety $A$ of dimension $g$ is *Hodge-generic* if $\mathrm{MT}(A)=\mathrm{GSp}(V,\psi)$ for the form $\psi$ of some polarization of $A$. Because both groups are connected and $\mathrm{MT}(A)\subseteq\mathrm{GSp}(V,\psi)$, this is equivalent to $\dim\mathrm{MT}(A)=2g^2+g+1$. One also says that $A$ has *maximal Mumford–Tate group* $\mathrm{GSp}_{2g}$.
(b) Let $A$ be an abelian variety over $\bar{\mathbb{Q}}$, and fix an embedding $\bar{\mathbb{Q}}\hookrightarrow\mathbb{C}$. Then $A$ is *Hodge-generic* if $A_{\mathbb{C}}$ is. The same applies to abelian varieties over any subfield of $\mathbb{C}$.
(c) Let $S$ be a connected smooth complex variety and $\mathcal{A}\to S$ an abelian scheme of relative dimension $g$; in particular this applies to an irreducible subvariety of a fine moduli space $\mathcal{A}_{g,N}$ ($N\ge3$) of polarized abelian varieties with level structure, with its universal family. The family is *Hodge-generic* if some fibre $\mathcal{A}_s$, $s\in S(\mathbb{C})$, is Hodge-generic. For $S$ over $\bar{\mathbb{Q}}$, use the fixed embedding.

**Proposition 23.4.** Definitions 23.3(a) and 23.3(c) are well posed and behave as follows.

(i) Independence of the polarization. If $A$ is Hodge-generic, then $\mathrm{End}(A)\otimes\mathbb{Q}=\mathbb{Q}$, by 23.2. Hence $\mathrm{NS}(A)\otimes\mathbb{Q}=\mathbb{Q}$ and all polarization forms are rational multiples of each other. Therefore "some polarization" may be replaced by "every polarization" in (a).
(ii) Very general fibres. If $\mathcal{A}\to S$ is Hodge-generic, the set of $s\in S(\mathbb{C})$ with $\mathcal{A}_s$ not Hodge-generic is a countable union of proper closed analytic subsets of $S$. These subsets are in fact algebraic (Cattani–Deligne–Kaplan). So a very general fibre is Hodge-generic. In general the Mumford–Tate group of a very general fibre is the *generic Mumford–Tate group* of the family. Hodge-genericity of the family means this group is $\mathrm{GSp}_{2g}$. (Y. André, *Mumford–Tate groups of mixed Hodge structures and the theorem of the fixed part*.)

*Remarks.*

(1) Equivalent formulations.
* Let the Hodge group $\mathrm{Hg}(A)$ be the smallest $\mathbb{Q}$-subgroup of $\mathrm{GL}(V)$ whose real points contain $h(\{z\in\mathbb{C}^\times:|z|=1\})$. Then $\mathrm{MT}(A)=\mathbb{G}_m\cdot\mathrm{Hg}(A)$, and $A$ is Hodge-generic if and only if $\mathrm{Hg}(A)=\mathrm{Sp}(V,\psi)$.
* $A$ is Hodge-generic if and only if, for all $m,n\ge0$, every Hodge tensor in $V^{\otimes m}\otimes(V^\vee)^{\otimes n}$ (with the appropriate Tate twist) is $\mathrm{GSp}(V,\psi)$-invariant.
* For $\mathcal{A}_g$, an irreducible subvariety $Z$ is Hodge-generic if and only if it is not contained in a proper special (Shimura) subvariety.
* $H_1$ can be used in place of $H^1$: the two Mumford–Tate groups correspond under $g\mapsto(g^\vee)^{-1}$.
(2) Endomorphisms. $\mathrm{End}(A_{\mathbb{C}})=\mathbb{Z}$ is necessary but not sufficient. Mumford constructed $4$-dimensional abelian varieties with endomorphism ring $\mathbb{Z}$ whose Hodge group is strictly smaller than $\mathrm{Sp}_8$ (D. Mumford, *A note of Shimura's paper "Discontinuous groups and abelian varieties"*). CM abelian varieties are never Hodge-generic, since their Mumford–Tate group is a torus.
(3) Choice of embedding over $\bar{\mathbb{Q}}$. In 23.3(b) the property does not depend on the embedding $\bar{\mathbb{Q}}\hookrightarrow\mathbb{C}$. By Deligne's theorem that Hodge classes on abelian varieties are absolutely Hodge (P. Deligne, *Hodge cycles on abelian varieties*, in LNM 900), the dimensions of the spaces of Hodge tensors are the same for all embeddings, and then (1) applies. A formaliser may simply fix the embedding.
(4) Use in [2020, 191(2), no. 7] (Masser–Zannier, *Abelian varieties isogenous to no Jacobian*). The paper concerns abelian varieties over $\bar{\mathbb{Q}}$ of dimension $g\ge4$ that are not isogenous to any Jacobian. No arXiv version was available to us, so we could not check whether its hypotheses use the pointwise notion (a) and (b) or the family notion (c), for example a Hodge-generic curve in $\mathcal{A}_g$. Both are given here.

## 24. Moduli stack of stable maps $\overline{\mathcal{M}}_{g,n}(X,\beta)$

*Chapter context.* This belongs to the chapter on moduli of stable maps, in a book on Gromov–Witten theory in algebraic geometry. Assumed known: algebraic and Deligne–Mumford stacks as categories fibred in groupoids over $(\mathrm{Sch}/k)$; nodal curves, their normalization and dualizing sheaf $\omega$; the stack $\overline{\mathcal{M}}_{g,n}$ of stable pointed curves; degrees of line bundles on proper curves. Throughout, $k$ is a field of characteristic $0$ (in the application $k=\mathbb{C}$) and $X$ is a projective $k$-scheme.

**Definition 24.1 (prestable curves).** Let $K$ be an algebraically closed field. A *prestable curve of genus $g$ with $n$ markings* over $K$ is a tuple $(C;x_1,\dots,x_n)$. Here $C$ is a connected, proper, reduced $K$-scheme of pure dimension $1$ whose singularities are at worst ordinary double points (nodes), with $h^1(C,\mathcal{O}_C)=g$. The $x_i\in C(K)$ are pairwise distinct smooth points. For an irreducible component $E$ of $C$ with normalization $\tilde E$, the *special points* of $E$ are the points of $\tilde E$ lying over nodes of $C$ or over marked points. A self-node of $E$ contributes two special points.

A *family* of such curves over a $k$-scheme $S$ is a flat, proper morphism of finite presentation $\pi\colon C\to S$ with sections $x_1,\dots,x_n\colon S\to C$, satisfying two conditions. Every geometric fibre $(C_{\bar s};x_i(\bar s))$ is a prestable curve of genus $g$ with $n$ markings. The sections are pairwise disjoint and land in the smooth locus of $\pi$.

**Definition 24.2 (curve classes).** A *curve class* on $X$ is a group homomorphism $\beta\colon\mathrm{Pic}(X)\to\mathbb{Z}$. A morphism $f\colon C\to X_K$ from a prestable curve over $K\supseteq k$ *has class $\beta$* if $\deg_C f^*L=\beta(L)$ for all $L\in\mathrm{Pic}(X)$. Here $f^*L$ means the pull-back of $L_K$, and the degree is the sum of the degrees over the irreducible components. One writes $\beta=f_*[C]$. Given an ample $\mathcal{O}_X(1)$, the *degree* of $f$ is $d:=\deg_Cf^*\mathcal{O}_X(1)$.

**Definition 24.3 (stable map).** Let $K\supseteq k$ be algebraically closed. An *$n$-pointed genus-$g$ stable map to $X$ of class $\beta$* over $K$ is a tuple $(C;x_1,\dots,x_n;f)$ satisfying the following conditions.

* $(C;x_i)$ is a prestable curve of genus $g$ with $n$ markings over $K$.
* $f\colon C\to X_K$ is a $K$-morphism of class $\beta$.
* Stability: let $E$ be an irreducible component of $C$ on which $f$ is constant. Let $h$ be the genus of its normalization and $m$ the number of its special points. Then $2h-2+m>0$. In other words, a contracted component of geometric genus $0$ has at least $3$ special points, and one of geometric genus $1$ has at least one.

An *isomorphism* $(C;x_i;f)\to(C';x'_i;f')$ is an isomorphism $\varphi\colon C\to C'$ with $\varphi(x_i)=x'_i$ and $f'\circ\varphi=f$.

**Definition 24.4 (the moduli stack).** $\overline{\mathcal{M}}_{g,n}(X,\beta)$ is the following category fibred in groupoids over $(\mathrm{Sch}/k)$, with the fppf (or étale) topology.

* An object over a $k$-scheme $S$ is a tuple $(\pi\colon C\to S;x_1,\dots,x_n;f\colon C\to X)$. Here $(\pi;x_i)$ is a family of prestable curves of genus $g$ with $n$ markings (24.1), and $f$ is a $k$-morphism. For every geometric point $\bar s$ of $S$, the fibre $(C_{\bar s};x_i(\bar s);f|_{C_{\bar s}})$ must be a stable map of class $\beta$ (24.3).
* A morphism from $(C'\to S';x'_i;f')$ to $(C\to S;x_i;f)$ over $h\colon S'\to S$ is a morphism $\tilde h\colon C'\to C$ such that the square formed by $\tilde h$, $h$ and the two projections is cartesian, with $\tilde h\circ x'_i=x_i\circ h$ and $f\circ\tilde h=f'$.

For a polarized $X$ put $\overline{\mathcal{M}}_{g,n}(X,d):=\coprod_{\beta(\mathcal{O}_X(1))=d}\overline{\mathcal{M}}_{g,n}(X,\beta)$. Only finitely many of these summands are non-empty (boundedness). Write $\overline{\mathcal{M}}_{g}(X,\beta):=\overline{\mathcal{M}}_{g,0}(X,\beta)$. The *evaluation maps* are $\mathrm{ev}_i:=f\circ x_i\colon\overline{\mathcal{M}}_{g,n}(X,\beta)\to X$.

**Theorem 24.5.** In characteristic $0$, $\overline{\mathcal{M}}_{g,n}(X,\beta)$ is a proper Deligne–Mumford stack of finite type over $k$. It has a projective coarse moduli space. Stability holds on an open set: in a family of prestable maps, the locus of $S$ over which the fibres are stable is open. The degree $\deg f^*L$ is locally constant on $S$. (M. Kontsevich; K. Behrend and Yu. Manin, *Stacks of stable maps and Gromov–Witten invariants*; W. Fulton and R. Pandharipande, *Notes on stable maps and quantum cohomology*.)

*Remarks.*

(1) Equivalent forms of stability. For a prestable map over $K$, the following are equivalent: (i) stability as in 24.3; (ii) the automorphism group is finite (in characteristic $0$); (iii) $\omega_C(x_1+\dots+x_n)\otimes f^*L^{\otimes3}$ is ample for some (equivalently every) ample $L$ on $X$. The equivalence of (i) and (iii) is a degree count: $\deg\omega_C(\sum x_i)|_E=2h-2+m$ on each component $E$.
(2) Homology classes. Over $k=\mathbb{C}$ one often takes $\beta\in H_2(X(\mathbb{C}),\mathbb{Z})$ and requires $f_*[C]:=(f\circ\nu)_*[\tilde C]=\beta$, where $\nu\colon\tilde C\to C$ is the normalization. This is a locally constant condition, so it cuts out open and closed substacks refining 24.4. For the quintic both conventions reduce to the degree: $\mathrm{Pic}(Q)=\mathbb{Z}H$ (Grothendieck–Lefschetz), and $H_2(Q,\mathbb{Z})=\mathbb{Z}\ell$ with $\int_\ell H=1$ (Lefschetz). Thus $\overline{\mathcal{M}}_g(Q,d)=\overline{\mathcal{M}}_{g,0}(Q,d\ell)$.
(3) Degenerate cases. If $\beta=0$ and $2g-2+n\le0$, the stack is empty. If $\beta=0$ and $2g-2+n>0$, then $\overline{\mathcal{M}}_{g,n}(X,0)\cong\overline{\mathcal{M}}_{g,n}\times X$. For $2g-2+n>0$ there is a stabilization morphism $\overline{\mathcal{M}}_{g,n}(X,\beta)\to\overline{\mathcal{M}}_{g,n}$, which forgets $f$ and contracts unstable components. The stack is usually singular and of impure dimension. The fundamental class used in Gromov–Witten theory is the virtual class of Definition #27, of dimension $\int_\beta c_1(T_X)+(\dim X-3)(1-g)+n$ when $X$ is smooth.
(4) Positive characteristic. There the stack is still algebraic and proper, but in general not Deligne–Mumford. For instance, a Frobenius-type map can have the non-reduced automorphism group scheme $\mu_p$. This is why we assume characteristic $0$.
(5) Use in [2021, 194(3), no. 1]. There $X=Q\subset\mathbb{P}^4_{\mathbb{C}}$ is a smooth quintic threefold, $n=0$, and $d\ge0$. $N_{g,d}=\int_{[\overline{\mathcal{M}}_g(Q,d)]^{\mathrm{vir}}}1$ with virtual dimension $0$. The term $d=0$ is non-empty only for $g\ge2$. The paper also uses $\overline{\mathcal{M}}_{g,n}(\mathbb{P}^4,d)$ and the NMSP moduli spaces, which are not defined here.

## 25. Nash blowup of a variety

*Chapter context.* This belongs to a chapter on canonical modifications of singular varieties, in a book on resolution of singularities. Assumed known: schemes of finite type over a field; Kähler differentials $\Omega_{X/k}$ and the smooth locus; scheme-theoretic closure and reduced induced structures; projective and birational morphisms; the Grassmannian $\mathrm{Grass}(d,n)$ of $d$-dimensional subspaces of $k^n$. The Grassmannian of quotients of a coherent sheaf and the Nash blowup are introduced here.

**Setting 25.1.** Let $k$ be a field. Let $X$ be a reduced separated $k$-scheme of finite type and pure dimension $d$. Let $X_{\mathrm{sm}}\subseteq X$ be the open locus where $X\to\operatorname{Spec}k$ is smooth, and $\operatorname{Sing}(X):=X\setminus X_{\mathrm{sm}}$. We assume $X_{\mathrm{sm}}$ is dense in $X$. This is automatic if $k$ is perfect, in particular if $k$ is algebraically closed as in the paper. On $X_{\mathrm{sm}}$ the sheaf $\Omega_{X/k}$ is locally free of rank $d$.

**Definition 25.2 (Grassmannian of quotients).** Let $\mathcal{M}$ be a coherent $\mathcal{O}_X$-module and $r\ge0$. Then $\mathrm{Grass}_r(\mathcal{M})$ is the functor on $X$-schemes sending $h\colon T\to X$ to the set of quotients $h^*\mathcal{M}\twoheadrightarrow\mathcal{Q}$ with $\mathcal{Q}$ locally free of rank $r$. Two quotients count as equal when they have the same kernel.

**Proposition 25.3.** $\mathrm{Grass}_r(\mathcal{M})$ is represented by a scheme that is projective over $X$. The Plücker morphism $[h^*\mathcal{M}\to\mathcal{Q}]\mapsto[\wedge^rh^*\mathcal{M}\to\wedge^r\mathcal{Q}]$ is a closed immersion into $\mathbb{P}(\wedge^r\mathcal{M})=\operatorname{Proj}\operatorname{Sym}(\wedge^r\mathcal{M})$. Its formation commutes with base change on $X$. A surjection $\mathcal{M}\twoheadrightarrow\mathcal{M}'$ induces a closed immersion $\mathrm{Grass}_r(\mathcal{M}')\hookrightarrow\mathrm{Grass}_r(\mathcal{M})$. Also $\mathrm{Grass}_r(\mathcal{O}_X^n)=X\times_k\mathrm{Grass}_r(k^n)$, where the second factor is the Grassmannian of $r$-dimensional quotients of $k^n$. (Grothendieck–Dieudonné, EGA I, 1971 edition.)

**Definition 25.4 (Nash blowup).** In Setting 25.1, the identity quotient $\Omega_{X/k}|_{X_{\mathrm{sm}}}\to\Omega_{X/k}|_{X_{\mathrm{sm}}}$ is a locally free quotient of rank $d$. It therefore defines a morphism $\sigma\colon X_{\mathrm{sm}}\to\mathrm{Grass}_d(\Omega_{X/k})$ lifting the inclusion $X_{\mathrm{sm}}\subseteq X$. Define:

* $X^*$ is the closure of $\sigma(X_{\mathrm{sm}})$ in $\mathrm{Grass}_d(\Omega_{X/k})$ with its reduced induced structure, equivalently the scheme-theoretic image of $\sigma$;
* $\nu\colon X^*\to X$ is the restriction of the structure morphism $\mathrm{Grass}_d(\Omega_{X/k})\to X$.

The pair $(X^*,\nu)$ is the *Nash blowup* of $X$. The *iterated Nash blowups* are $X^{(0)}:=X$ and $X^{(i+1)}:=(X^{(i)})^*$, with the composite maps $X^{(i)}\to X$.

**Proposition 25.5.**

(a) $\nu$ is projective. $\nu^{-1}(X_{\mathrm{sm}})=\sigma(X_{\mathrm{sm}})$ is dense in $X^*$, and $\nu$ restricts to an isomorphism $\nu^{-1}(X_{\mathrm{sm}})\to X_{\mathrm{sm}}$. Hence $\nu$ is proper and birational, and $X^*$ again satisfies Setting 25.1. In particular the iterates are defined.
(b) Universal property. The universal quotient gives a locally free rank-$d$ quotient of $\nu^*\Omega_{X/k}$. Let $h\colon Y\to X$ be a morphism with $Y$ reduced and $h^{-1}(X_{\mathrm{sm}})$ dense in $Y$, such that $h^*\Omega_{X/k}$ has a locally free quotient of rank $d$. Then this quotient is unique, and $h$ factors uniquely through $\nu$.
(c) Locality. For $U\subseteq X$ open, $U^*=\nu^{-1}(U)$.
(d) Embedded description. Let $X\subseteq\mathbb{A}^n_k$ be closed. For $x\in X_{\mathrm{sm}}(k)$, let $T_xX:=\{v\in k^n:\sum_j\frac{\partial f}{\partial x_j}(x)v_j=0\ \forall f\in I(X)\}$, a $d$-dimensional linear subspace. The *Gauss map* $\Phi\colon X_{\mathrm{sm}}\to\mathrm{Grass}(d,n)$, $x\mapsto T_xX$, is a morphism. Then $(X^*,\nu)$ is isomorphic over $X$ to the Zariski closure of the graph of $\Phi$ in $X\times\mathrm{Grass}(d,n)$, with the first projection. To see this, the surjection $\mathcal{O}_X^n\to\Omega_{X/k}$, $e_j\mapsto dx_j$, embeds $\mathrm{Grass}_d(\Omega_{X/k})$ into $X\times\mathrm{Grass}_d(k^n)$. Dualizing quotients of $k^n$ into subspaces of $(k^n)^\vee=k^n$ (dual basis $\partial/\partial x_j$) identifies $\sigma$ with the graph of $\Phi$. In particular the closed-graph construction does not depend on the embedding.

*Remarks.*

(1) Which definition to formalise. The intrinsic Definition 25.4 is needed because iterates are not affine. In [2026, 203(2), no. 7] the "second iteration of the normalized Nash blowup" is a Nash blowup of a non-affine variety. By 25.5(c) and (d), this agrees with gluing the embedded construction over affine charts.
(2) Blow-up description. $\nu$ is the blow-up of $X$ along a coherent ideal sheaf. Concretely, it is the blow-up along any ideal sheaf isomorphic, as an $\mathcal{O}_X$-module, to $(\wedge^d\Omega_{X/k})/(\text{torsion})$; such ideals exist locally on $X$, and the blow-ups glue. In practice it is computed via Jacobian ideals (logarithmic Jacobian ideals for toric varieties).
(3) Characterisation of smoothness. In characteristic $0$, $\nu$ is an isomorphism if and only if $X$ is smooth (A. Nobile, *Some properties of the Nash blowing-up*). This fails in characteristic $p$: for distinct primes $p,q$, the curve $x^p=y^q$ in $\mathbb{A}^2$ is isomorphic to its Nash blowup when $\mathrm{char}\,k\in\{p,q\}$. For normal $X$ in positive characteristic, $\nu$ is an isomorphism if and only if $X$ is smooth (Duarte–Núñez-Betancourt, as cited in [2026, 203(2), no. 7]). The normalized variant is Definition #26.
(4) Use in [2026, 203(2), no. 7]. There $k$ is algebraically closed, of arbitrary characteristic. $X$ is a normal affine toric variety of dimension $d\ge4$, and "variety" allows equidimensional reducible schemes. "Contains an open affine subset isomorphic to $X$" means an open subscheme of $X^*$ isomorphic to $X$ as a $k$-scheme. That isomorphism is not over $X$.

## 26. Normalized Nash blowup

*Chapter context.* This is the same chapter as the Nash blowup (Definition #25), on canonical modifications of singular varieties in a book on resolution of singularities. Assumed known: normalization of reduced schemes of finite type over a field and its universal property; relative normalization (integral closure of $\mathcal{O}_Y$ in a quasi-coherent $\mathcal{O}_Y$-algebra); Definition #25 and its properties. We keep Setting 25.1: $X$ is a reduced separated $k$-scheme of finite type, of pure dimension $d$, with dense smooth locus $X_{\mathrm{sm}}$.

**Recollection 26.1 (normalization of a reduced scheme).** Let $Y$ be a reduced $k$-scheme of finite type with irreducible components $Y_1,\dots,Y_r$ and generic points $\xi_1,\dots,\xi_r$. Its *normalization* $\eta\colon Y^{\mathrm{nor}}\to Y$ is the relative normalization of $Y$ in $\coprod_i\operatorname{Spec}\kappa(\xi_i)\to Y$. Equivalently, $Y^{\mathrm{nor}}=\coprod_i Y_i^{\mathrm{nor}}$, where $Y_i^{\mathrm{nor}}$ is the integral closure of $Y_i$ in its function field. The morphism $\eta$ is finite (finiteness of integral closure for algebras of finite type over a field) and birational. It is an isomorphism over the normal locus of $Y$. It has the following universal property. Let $Z$ be a normal scheme and $h\colon Z\to Y$ a morphism mapping every generic point of $Z$ to a generic point of $Y$. Then $h$ factors uniquely through $\eta$.

**Definition 26.2 (normalized Nash blowup).** Let $(X^*,\nu)$ be the Nash blowup of $X$ (Definition #25). Let $\eta\colon\overline{X^*}\to X^*$ be the normalization of the reduced scheme $X^*$. The *normalized Nash blowup* of $X$ is the pair
$$\bigl(\overline{X^*},\ \bar\nu\bigr),\qquad \bar\nu:=\nu\circ\eta\colon\overline{X^*}\to X^*\to X .$$
Its *iterates* are defined recursively by
$$Y_0:=X,\quad \pi_0:=\mathrm{id}_X;\qquad Y_{i+1}:=\overline{Y_i^{\,*}},\quad \pi_{i+1}:=\pi_i\circ\bar\nu_{Y_i}\colon Y_{i+1}\to X .$$
$Y_i$ is the *$i$-th iteration* of the normalized Nash blowup. The "second iteration" is $Y_2$, the normalized Nash blowup of the normalized Nash blowup. One says that iterating the normalized Nash blowup *resolves the singularities* of $X$ if $Y_i$ is smooth over $k$ for some $i$. The same terminology is used for the plain iterates $X^{(i)}$ of Definition #25.

**Proposition 26.3.**

(a) $\overline{X^*}$ is normal, separated, of finite type and of pure dimension $d$. Its smooth locus contains the dense open $\eta^{-1}(X^*_{\mathrm{sm}})\cong X^*_{\mathrm{sm}}$. So $\overline{X^*}$ again satisfies Setting 25.1, and the iterates are defined.
(b) $\bar\nu$ is projective and birational, and $\bar\nu^{-1}(X_{\mathrm{sm}})\to X_{\mathrm{sm}}$ is an isomorphism. Indeed, $X_{\mathrm{sm}}$ is normal, so $\eta$ is an isomorphism over $\nu^{-1}(X_{\mathrm{sm}})\cong X_{\mathrm{sm}}$.
(c) Universal property. Let $Z$ be normal and $h\colon Z\to X$ a morphism satisfying three conditions: $h$ maps generic points to generic points; $h^{-1}(X_{\mathrm{sm}})$ is dense in $Z$; and $h^*\Omega_{X/k}$ admits a locally free quotient of rank $d$. Then $h$ factors uniquely through $\bar\nu$. This follows from Definition #25 (universal property) and 26.1.
(d) Locality. For $U\subseteq X$ open, the normalized Nash blowup of $U$ is $\bar\nu^{-1}(U)\to U$. Hence if $Y_m$ contains an open subscheme isomorphic to $X$, then so does $Y_{jm}$ for every $j\ge1$, and the iteration never resolves the singularities of a singular $X$.
(e) Suppose $X$ is normal. Then $\bar\nu$ is an isomorphism if and only if $\nu$ is. Indeed, if $\nu\circ\eta$ is an isomorphism, then $\eta$ is a finite birational closed immersion into the reduced scheme $X^*$, hence an isomorphism. Consequently $\bar\nu$ is an isomorphism if and only if $X$ is smooth, in every characteristic, by the results quoted in Definition #25 (Nobile in characteristic $0$; Duarte–Núñez-Betancourt for normal $X$ in characteristic $p$).

*Remarks.*

(1) Notation. [2026, 203(2), no. 7] writes the normalized Nash blowup as $(\overline{X^*},\eta\circ\nu)$. In standard composition order the map to $X$ is $\nu\circ\eta$ as above, first normalize and then project.
(2) Comparison with plain iteration. For normal $X$ the two procedures can differ already at the first step, because $X^*$ need not be normal. In characteristic $p$ only the normalized version is reasonable, since the plain Nash blowup of a non-normal singular curve may be an isomorphism (Definition #25, Remarks).
(3) Formalisation. Mathlib's relative normalization `AlgebraicGeometry.Scheme.Hom.normalization`, applied to $\coprod_i\operatorname{Spec}\kappa(\xi_i)\to X^*$ (or componentwise), produces $\eta$. Iteration requires only that $\overline{X^*}$ again satisfy Setting 25.1, which is 26.3(a).
(4) Use in [2026, 203(2), no. 7]. There $k$ is algebraically closed and $X$ is a normal singular affine toric variety of dimension $d\ge4$. The results say that $Y_1$ ($\mathrm{char}\,k\neq3$) or $Y_2$ ($\mathrm{char}\,k=3$) contains an open affine subscheme isomorphic to $X$, as an abstract $k$-scheme. By 26.3(d), the iteration therefore never resolves $X$. In characteristic $0$ the same holds for $X^*$ itself.

## 27. Perfect obstruction theory and virtual fundamental class

*Chapter context.* This belongs to the chapter on virtual fundamental classes, in a book on enumerative geometry and Gromov–Witten theory. Assumed known:

* Deligne–Mumford and Artin stacks locally of finite type over a field $k$ of characteristic $0$, and quotient stacks;
* the derived category of $\mathcal{O}_M$-modules on the étale site, perfect complexes, and the cotangent complex $L_M$ (and $L_{M/\mathfrak{M}}$ for a morphism of DM type), with $\tau^{\ge-1}$ its truncation;
* normal cones $C_{U/W}=\operatorname{Spec}\bigoplus_{i\ge0}I^i/I^{i+1}$ of closed embeddings and Fulton's intersection theory;
* rational Chow groups $A_*(M)_{\mathbb{Q}}$ of DM stacks, with flat pull-back, Gysin maps for vector bundles and the degree of zero-cycles on proper $M$ (Definition #16);
* the moduli stack $\overline{\mathcal{M}}_{g,n}(X,\beta)$ (Definition #24).

**Definition 27.1 (cones).** For a coherent sheaf $\mathcal{F}$ on a DM stack $M$, put $C(\mathcal{F}):=\operatorname{Spec}_M\operatorname{Sym}\mathcal{F}$. If $\mathcal{F}$ is locally free of rank $r$, then $C(\mathcal{F})$ is the total space of the rank-$r$ vector bundle with sheaf of sections $\mathcal{F}^\vee$. For a closed embedding $U\hookrightarrow W$ with ideal $I$, the normal cone $C_{U/W}$ is a closed subcone of $N_{U/W}:=C(I/I^2)$. If $W$ has pure dimension $w$, then $C_{U/W}$ has pure dimension $w$ (Fulton, *Intersection theory*, Appendix B).

**Definition 27.2 (the stacks $h^1/h^0$).** Let $E\in D(\mathcal{O}_M)$ have $h^i(E)=0$ for $i\notin\{-1,0\}$, with $h^{-1}(E)$ and $h^0(E)$ coherent. Suppose étale-locally $E\cong[E^{-1}\xrightarrow{d}E^0]$, with $E^0$ locally free and $E^{-1}$ coherent. Put
$$h^1/h^0(E^\vee)|_U:=[\,C(E^{-1})/C(E^0)\,].$$
This is the quotient stack for the additive action of the group scheme $C(E^0)$ on $C(E^{-1})$ through $C(d)\colon C(E^0)\to C(E^{-1})$. These glue to a stack over $M$ that is independent of the presentation up to canonical equivalence. If $E$ is perfect of amplitude $[-1,0]$, i.e. both $E^i$ can be chosen locally free, it is a *vector bundle stack*.

**Theorem 27.3 (intrinsic normal cone; Behrend–Fantechi).** Let $M$ be a DM stack locally of finite type over $k$. Let $f\colon M\to\mathfrak{M}$ be a morphism of DM type to a smooth Artin stack $\mathfrak{M}$ of pure dimension $m$; take $\mathfrak{M}=\operatorname{Spec}k$ and $m=0$ for the absolute case.

*Local charts.* A local chart is the following data: an étale $U\to M$ with $U$ a scheme, a smooth morphism $W\to\mathfrak{M}$ with $W$ a scheme, and a closed embedding $U\hookrightarrow W$ over $\mathfrak{M}$. Such charts cover $M$. On a chart, $\tau^{\ge-1}L_{M/\mathfrak{M}}|_U\cong[I/I^2\to\Omega_{W/\mathfrak{M}}|_U]$.

*The cones.* The relative intrinsic normal sheaf is $N_{M/\mathfrak{M}}:=h^1/h^0((\tau^{\ge-1}L_{M/\mathfrak{M}})^\vee)$. On a chart it is $[N_{U/W}/T_{W/\mathfrak{M}}|_U]$, where $T_{W/\mathfrak{M}}:=C(\Omega_{W/\mathfrak{M}})$. The substacks $[C_{U/W}/T_{W/\mathfrak{M}}|_U]$ glue to a closed substack $C_{M/\mathfrak{M}}\subseteq N_{M/\mathfrak{M}}$, independent of the charts. This is the *intrinsic normal cone*. It has pure dimension $m$; in the absolute case, pure dimension $0$. (K. Behrend and B. Fantechi, *The intrinsic normal cone*, Invent. Math. 1997.)

**Definition 27.4 (perfect obstruction theory).** In the setting of 27.3, an *obstruction theory* for $M$ over $\mathfrak{M}$ is a pair $(E,\varphi)$. Here $E\in D(\mathcal{O}_M)$ is as in 27.2, and $\varphi\colon E\to\tau^{\ge-1}L_{M/\mathfrak{M}}$ is a morphism in $D(\mathcal{O}_M)$ with two properties: $h^0(\varphi)$ is an isomorphism and $h^{-1}(\varphi)$ is surjective. It is *perfect* if $E$ is perfect of amplitude $[-1,0]$. Then the *rank* $\operatorname{rk}E:=\operatorname{rk}E^0-\operatorname{rk}E^{-1}$ is locally constant. The *virtual dimension* is $\operatorname{vd}:=\operatorname{rk}E+m$. The *obstruction sheaf* is $\mathrm{Ob}:=h^1(E^\vee)$.

**Proposition 27.5 (Behrend–Fantechi).** $\varphi$ is an obstruction theory if and only if the induced morphism $N_{M/\mathfrak{M}}\to\mathfrak{E}:=h^1/h^0(E^\vee)$ is a closed immersion. In that case $C_{M/\mathfrak{M}}$ is a closed subcone stack of $\mathfrak{E}$.

**Definition 27.6 (virtual fundamental class).** Let $(E,\varphi)$ be a perfect obstruction theory. Assume $E$ has a global resolution: $E\cong[E^{-1}\to E^0]$ on all of $M$, with $E^{-1}$ and $E^0$ locally free. Then $\mathfrak{E}=[C(E^{-1})/C(E^0)]$, and $p\colon C(E^{-1})\to\mathfrak{E}$ is smooth of relative dimension $\operatorname{rk}E^0$. Put
$$C_1:=C_{M/\mathfrak{M}}\times_{\mathfrak{E}}C(E^{-1})\ \subseteq\ C(E^{-1}).$$
This is a closed subcone of the vector bundle $C(E^{-1})$, of rank $\operatorname{rk}E^{-1}$, and it has pure dimension $m+\operatorname{rk}E^0$. Let $[C_1]=\sum_i\mu_i[C_{1,i}]$ be its fundamental cycle, the sum over irreducible components with their geometric multiplicities. The *virtual fundamental class* is
$$[M]^{\mathrm{vir}}=[M,E]^{\mathrm{vir}}:=0^!_{C(E^{-1})}[C_1]\ \in A_{\operatorname{vd}}(M)_{\mathbb{Q}}.$$
Here $0^!$ is the Gysin map of the zero section, i.e. the inverse of flat pull-back $A_*(M)_{\mathbb{Q}}\xrightarrow{\sim}A_{*+\operatorname{rk}E^{-1}}(C(E^{-1}))_{\mathbb{Q}}$. The class is independent of the global resolution (Behrend–Fantechi). If $M$ is proper and $\operatorname{vd}=0$, the *virtual count* is $\deg[M]^{\mathrm{vir}}\in\mathbb{Q}$, the degree of Definition #16.

**Definition 27.7 (Gromov–Witten virtual class).** Let $X$ be smooth projective over $k$ and $M=\overline{\mathcal{M}}_{g,n}(X,\beta)$ (Definition #24). Let $\mathfrak{M}=\mathfrak{M}_{g,n}$ be the stack of prestable $n$-pointed genus-$g$ curves (24.1), a smooth Artin stack of pure dimension $3g-3+n$. The map $M\to\mathfrak{M}$ forgets $f$. Let $\pi\colon\mathcal{C}\to M$ and $f\colon\mathcal{C}\to X$ be the universal curve and map. Then $E:=(R\pi_*f^*T_X)^\vee$ carries a canonical perfect relative obstruction theory $\varphi\colon E\to\tau^{\ge-1}L_{M/\mathfrak{M}}$, and $E$ has a global resolution (K. Behrend, *Gromov–Witten invariants in algebraic geometry*, Invent. Math. 1997). The class $[\overline{\mathcal{M}}_{g,n}(X,\beta)]^{\mathrm{vir}}:=[M,E]^{\mathrm{vir}}$ has dimension
$$\operatorname{vd}=\chi(f^*T_X)+3g-3+n=\int_\beta c_1(T_X)+(\dim X-3)(1-g)+n .$$

*Remarks.*

(1) Sanity checks for a formaliser.
* If $M$ is a local complete intersection, then $E=\tau^{\ge-1}L_M$ is a perfect obstruction theory and $[M]^{\mathrm{vir}}=[M]$.
* If $M$ is smooth, $\mathrm{Ob}$ is locally free and $[M]^{\mathrm{vir}}=c_{\mathrm{top}}(\mathrm{Ob})\cap[M]$.
* If $M=Z(s)$ is the zero scheme of a section $s$ of a vector bundle $V$ on a smooth $W$, then $E=[V^\vee|_M\to\Omega_W|_M]$, and $[M]^{\mathrm{vir}}$ is Fulton's localized top Chern class.
(2) Conventions. Behrend–Fantechi write $L_M$ for the truncation $\tau^{\ge-1}L_M$. Some sources phrase the condition on $\varphi$ as "$h^0$ iso, $h^{-1}$ epi" of $E\to L_M$; this is the same. Using Kresch's Chow groups of Artin stacks, one can drop the global resolution and set $[M]^{\mathrm{vir}}=0^!_{\mathfrak{E}}[C_{M/\mathfrak{M}}]$. If a relative and an absolute obstruction theory are compatible, they give the same class.
(3) Use in [2021, 194(3), no. 1]. There $X=Q$ is the quintic threefold, so $c_1(T_Q)=0$, $\dim Q=3$ and $n=0$. Hence $\operatorname{vd}=0$ and $N_{g,d}=\deg[\overline{\mathcal{M}}_g(Q,d)]^{\mathrm{vir}}\in\mathbb{Q}$. The proofs use refinements not defined here: torus-equivariant virtual localization (Graber–Pandharipande) and cosection-localized virtual cycles (Kiem–Li) for the NMSP moduli spaces.

## 28. Points of an algebraic stack

*Chapter context.* This belongs to the chapter on the underlying topological space of an algebraic stack, in a book on algebraic stacks (conventions of the Stacks Project). Assumed known: algebraic spaces and their points $|U|$; algebraic stacks over a base scheme $S$, i.e. stacks in groupoids on $(\mathrm{Sch}/S)_{\mathrm{fppf}}$ with diagonal representable by algebraic spaces and a smooth surjective morphism from a scheme; 2-fibre products, 2-isomorphisms, open and closed substacks; flat, smooth and finite type morphisms of stacks. Points, $k$-points, closed points, finite type points and stabilizers are defined here.

**Definition 28.1 (points).** Let $\mathcal{X}$ be an algebraic stack. A *field-valued point* is a morphism $p\colon\operatorname{Spec}K\to\mathcal{X}$ with $K$ a field. Two such points $p\colon\operatorname{Spec}K\to\mathcal{X}$ and $q\colon\operatorname{Spec}L\to\mathcal{X}$ are *equivalent* if the following holds. There are a field $\Omega$ and field extensions $K\to\Omega$, $L\to\Omega$ such that the composites $\operatorname{Spec}\Omega\to\operatorname{Spec}K\xrightarrow{p}\mathcal{X}$ and $\operatorname{Spec}\Omega\to\operatorname{Spec}L\xrightarrow{q}\mathcal{X}$ are 2-isomorphic, i.e. isomorphic objects of the fibre category $\mathcal{X}_{\operatorname{Spec}\Omega}$. This is an equivalence relation. The proof of transitivity amalgamates two field extensions of a common field. The set of equivalence classes is $|\mathcal{X}|$, the *points* of $\mathcal{X}$. A morphism $f\colon\mathcal{X}\to\mathcal{Y}$ induces $|f|\colon|\mathcal{X}|\to|\mathcal{Y}|$, $[p]\mapsto[f\circ p]$.

**Proposition 28.2 (topology).** Let $\mathcal{X}$ be an algebraic stack.

(a) For every smooth surjective $U\to\mathcal{X}$ with $U$ a scheme, $|U|\to|\mathcal{X}|$ is surjective. So every point is represented by some $\operatorname{Spec}\kappa(u)\to U\to\mathcal{X}$, and $|\mathcal{X}|$ is a set.
(b) There is a unique topology on $|\mathcal{X}|$ such that, for every flat, locally finitely presented morphism $U\to\mathcal{X}$ from an algebraic space, the map $|U|\to|\mathcal{X}|$ is continuous and open. For any smooth surjective $U\to\mathcal{X}$ from a scheme, it is the quotient topology. Every $|f|$ is continuous.
(c) $\mathcal{U}\mapsto|\mathcal{U}|$ is a bijection from open substacks of $\mathcal{X}$ to open subsets of $|\mathcal{X}|$. Every closed subset is $|\mathcal{Z}|$ for a unique reduced closed substack $\mathcal{Z}$.
(Stacks Project, Properties of Algebraic Stacks, section on points.)

A point $x\in|\mathcal{X}|$ is *closed* if $\{x\}$ is closed in $|\mathcal{X}|$. It is a *finite type point* if it can be represented by a morphism $\operatorname{Spec}K\to\mathcal{X}$ that is locally of finite type.

**Definition 28.3 ($k$-points; stabilizers; smooth points).** Let $k$ be a field and $\mathcal{X}$ an algebraic stack over $k$, i.e. over $S=\operatorname{Spec}k$.

(a) $\mathcal{X}(k)$ is the groupoid $\mathcal{X}_{\operatorname{Spec}k}$. Its objects are the $k$-morphisms $x\colon\operatorname{Spec}k\to\mathcal{X}$ and its morphisms are the 2-isomorphisms. "A point $x\in\mathcal{X}(k)$" means an object, and its image in $|\mathcal{X}|$ is again written $x$. Such an $x$ is called *closed* if its image is a closed point.
(b) For a field-valued point $p\colon\operatorname{Spec}K\to\mathcal{X}$, the *stabilizer* is
$$G_p:=\mathrm{Isom}(p,p)=\operatorname{Spec}K\times_{(p,p),\,\mathcal{X}\times_k\mathcal{X},\,\Delta}\mathcal{X}.$$
This is the group algebraic space over $K$ whose $T$-points are the automorphisms of $p|_T$ in $\mathcal{X}_T$. It is locally of finite type over $K$, because the diagonal is, and hence it is a group scheme. It is of finite type if $\mathcal{X}$ is quasi-separated. $\mathcal{X}$ *has affine stabilizers* if $G_p$ is affine for every field-valued point $p$.

(c) If $\mathcal{X}$ is locally of finite type over $k$, a point $x\in|\mathcal{X}|$ is *smooth* if it lies in $|\mathcal{U}|$ for an open substack $\mathcal{U}\subseteq\mathcal{X}$ that is smooth over $k$.

**Proposition 28.4 (points over an algebraically closed field).** Let $k$ be algebraically closed and $\mathcal{X}$ locally of finite type over $k$.

(a) Two objects $x,y\in\mathcal{X}(k)$ have the same image in $|\mathcal{X}|$ if and only if $x\cong y$ in $\mathcal{X}(k)$. Indeed, $\mathrm{Isom}(x,y)$ is an algebraic space locally of finite type over $k$; if it is non-empty it has a $k$-point. Hence $\mathcal{X}(k)/{\cong}\hookrightarrow|\mathcal{X}|$.
(b) The image of $\mathcal{X}(k)$ is exactly the set of finite type points. This set is dense in every closed subset of $|\mathcal{X}|$ (Stacks Project, Morphisms of Stacks, section on points of finite type).
(c) Consequently, every closed point of $|\mathcal{X}|$ is the image of some $x\in\mathcal{X}(k)$, unique up to isomorphism. Its stabilizer $G_x$ is well defined up to isomorphism, via conjugation by an isomorphism $x\cong x'$.

*Remarks.*

(1) Examples. For a scheme or algebraic space, $|\mathcal{X}|$ is the usual underlying space. For $\mathcal{X}=[\mathbb{A}^1_k/\mathbb{G}_m]$ with the scaling action, $|\mathcal{X}|$ has two points. The image of $0$ is closed, with stabilizer $\mathbb{G}_m$. The image of $1\in\mathbb{A}^1(k)$ is open and not closed, with trivial stabilizer. So a $k$-point need not be closed.
(2) Non-closed base fields. Over a field that is not algebraically closed, non-isomorphic $k$-points can define the same point. For instance $|B(\mathbb{Z}/2)_{\mathbb{Q}}|$ is a single point, while $B(\mathbb{Z}/2)(\mathbb{Q})/{\cong}\;=\mathbb{Q}^\times/\mathbb{Q}^{\times2}$. So $\mathcal{X}(k)$ and $|\mathcal{X}|$ must be kept apart.
(3) Formalisation. $|\mathcal{X}|$ is a quotient of a set of pairs (field, morphism) by the relation in 28.1. Size issues are avoided by 28.2(a), or by bounding the cardinality of $K$. The topology is best defined by the quotient description in 28.2(b), together with independence of the atlas.
(4) Use in [2020, 191(3), no. 1] (Alper–Hall–Rydh). There $k$ is algebraically closed, and $\mathcal{X}$ is quasi-separated, locally of finite type over $k$, with affine stabilizers. Theorem 1.1 starts from $x\in\mathcal{X}(k)$, not necessarily closed. Theorem 1.2 starts from a smooth and closed $x\in|\mathcal{X}|$, which by 28.4(c) comes from a $k$-point. Then $G_x$ is its stabilizer group scheme and $N_x$ is computed from the residual gerbe at $x$ (Definition #29).

## 29. Residual gerbe at a point of an algebraic stack

*Chapter context.* This is the same chapter as Definition #28 (points of algebraic stacks), in a book on algebraic stacks with Stacks Project conventions. Assumed known: monomorphisms, closed immersions and 2-fibre products of algebraic stacks; strictly full substacks; reduced and locally Noetherian stacks; gerbes; the classifying stack $BG=[\operatorname{Spec}k/G]$ of a group scheme; quasi-coherent sheaves on $BG$ as $G$-representations (for $G$ affine). Definition #28 supplies $|\mathcal{X}|$, $\mathcal{X}(k)$ and the stabilizers $G_x$.

**Lemma 29.1.** Let $\mathcal{X}$ be an algebraic stack and $x\in|\mathcal{X}|$. The following are equivalent:

1. there are an algebraic stack $\mathcal{Z}$ and a monomorphism $\mathcal{Z}\to\mathcal{X}$ such that $|\mathcal{Z}|$ is a singleton with image $x$;
2. the same holds with $\mathcal{Z}$ in addition reduced;
3. there are an algebraic stack $\mathcal{Z}$, a monomorphism $j\colon\mathcal{Z}\to\mathcal{X}$, a field $K$ and a flat surjective $z\colon\operatorname{Spec}K\to\mathcal{Z}$ with $j(z)=x$.

If these hold, there is a unique strictly full subcategory $\mathcal{Z}_x\subseteq\mathcal{X}$ that is a reduced, locally Noetherian algebraic stack with $|\mathcal{Z}_x|$ a singleton mapping to $x$. The inclusion $\mathcal{Z}_x\to\mathcal{X}$ is a monomorphism. (Stacks Project, Properties of Algebraic Stacks, section on residual gerbes.)

**Definition 29.2 (residual gerbe).** If the conditions of 29.1 hold, one says the *residual gerbe of $\mathcal{X}$ at $x$ exists*. The *residual gerbe* is then the monomorphism $\mathcal{Z}_x\to\mathcal{X}$ of 29.1, also written $\mathcal{G}_x\to\mathcal{X}$. For a morphism $f\colon\mathcal{W}\to\mathcal{X}$, put $f^{-1}(\mathcal{Z}_x):=\mathcal{W}\times_{\mathcal{X}}\mathcal{Z}_x$, a substack of $\mathcal{W}$ via a monomorphism.

**Proposition 29.3 (basic properties).** Let $\mathcal{X}$ be an algebraic stack and $x\in|\mathcal{X}|$.

(a) Existence. Residual gerbes exist at every point in three cases: if $\mathcal{X}$ is locally Noetherian; if the inertia $\mathcal{I}_{\mathcal{X}}\to\mathcal{X}$ is quasi-compact, for instance if $\mathcal{X}$ is quasi-separated; and if $\mathcal{X}$ is quasi-DM (Stacks Project, Morphisms of Stacks, section on existence of residual gerbes).
(b) Factorization. Every field-valued point $\operatorname{Spec}K\to\mathcal{X}$ in the class $x$ factors through $\mathcal{Z}_x\to\mathcal{X}$.
(c) Uniqueness. Every monomorphism $\mathcal{Z}\to\mathcal{X}$ from a reduced, locally Noetherian algebraic stack with one point mapping to $x$ factors as an equivalence $\mathcal{Z}\simeq\mathcal{Z}_x$ followed by the inclusion.
(d) Structure. $\mathcal{Z}_x$ is a gerbe over a reduced, locally Noetherian algebraic space with one point. It is regular, and it inherits being DM, quasi-DM, separated or quasi-separated from $\mathcal{X}$.
(e) Closed points. If $\mathcal{X}$ is locally Noetherian, then $x$ is closed if and only if $\mathcal{Z}_x\to\mathcal{X}$ is a closed immersion. In that case $\mathcal{Z}_x$ is the reduced closed substack with $|\mathcal{Z}_x|=\{x\}$.
(f) Functoriality. If $f\colon\mathcal{X}\to\mathcal{Y}$ maps $x$ to $y$ and both residual gerbes exist, then $f$ restricts to a morphism $\mathcal{Z}_x\to\mathcal{Z}_y$.

**Proposition 29.4 (residual gerbe at a $k$-point).** Let $k$ be algebraically closed, let $\mathcal{X}$ be locally of finite type over $k$, and let $x\in\mathcal{X}(k)$ with stabilizer $G_x=\mathrm{Isom}(x,x)$ (Definition #28). Then $x$ factors as $\operatorname{Spec}k\to\mathcal{Z}_x\to\mathcal{X}$, and $\operatorname{Spec}k\to\mathcal{Z}_x$ is flat, surjective and locally of finite presentation. Since $\mathcal{Z}_x\to\mathcal{X}$ is a monomorphism, $\operatorname{Spec}k\times_{\mathcal{Z}_x}\operatorname{Spec}k=\operatorname{Spec}k\times_{\mathcal{X}}\operatorname{Spec}k=G_x$. Hence there is a canonical equivalence
$$\mathcal{Z}_x\simeq BG_x=[\operatorname{Spec}k/G_x],$$
under which $x$ corresponds to the trivial torsor. In particular, for $x$ closed, $BG_x\hookrightarrow\mathcal{X}$ is a closed immersion.

**Definition 29.5 (infinitesimal neighbourhoods and normal space).** In the situation of 29.4, assume $x$ is closed. Let $\mathcal{I}\subseteq\mathcal{O}_{\mathcal{X}}$ be the ideal sheaf of $\mathcal{Z}_x=BG_x$.

* The *$n$-th infinitesimal neighbourhood* of $x$ is the closed substack $\mathcal{X}^{[n]}_x\subseteq\mathcal{X}$ defined by $\mathcal{I}^{n+1}$.
* The coherent sheaf $\mathcal{I}/\mathcal{I}^2$ on $BG_x$ is a finite-dimensional $G_x$-representation, when $G_x$ is affine. The *normal space* is the dual representation $N_x:=(\mathcal{I}/\mathcal{I}^2)^\vee$.

*Remarks.*

(1) Examples. For a scheme $X$, $\mathcal{Z}_x=\operatorname{Spec}\kappa(x)\to X$. For $\mathcal{X}=[\mathbb{A}^1/\mathbb{G}_m]$, the residual gerbe at the origin is $B\mathbb{G}_m\hookrightarrow\mathcal{X}$, a closed immersion. At the open point it is the open immersion $[\mathbb{G}_m/\mathbb{G}_m]=\operatorname{Spec}k\hookrightarrow\mathcal{X}$, a monomorphism that is not closed.
(2) Comparison. In Laumon–Moret-Bailly a gerbe is attached to each point of a quasi-separated stack, and it need not be algebraic in their generality. On quasi-separated stacks it agrees with 29.2. Over a non-closed field, $\mathcal{Z}_x$ is a gerbe that need not be neutral, so the identification with $BG$ in 29.4 needs a point defined over the base field.
(3) For a formaliser. The cleanest route in the generality of [2020, 191(3), no. 1] is Proposition 29.4: define $\mathcal{Z}_x$ for $x\in\mathcal{X}(k)$ as the strictly full substack of objects locally isomorphic to $x$, and prove $\mathcal{Z}_x\simeq BG_x$. Lemma 29.1 is needed only for general points.
(4) Use in [2020, 191(3), no. 1]. There $k$ is algebraically closed, and $\mathcal{X}$ is quasi-separated, locally of finite type, with affine stabilizers. "$BG_x\hookrightarrow\mathcal{X}$, the residual gerbe at $x$" is 29.4, for $x\in\mathcal{X}(k)$. Theorem 1.1 states $BH\cong f^{-1}(BG_x)$ for $f\colon[\operatorname{Spec}A/H]\to\mathcal{X}$, the fibre product of 29.2. The left side is the residual gerbe of $[\operatorname{Spec}A/H]$ at the $H$-fixed point $w$. In Theorem 1.2, $x$ is closed and $N_x$ is as in 29.5. It equals the tangent space $T_{\mathcal{X},x}$ when $G_x$ is smooth.

## 30. Theta divisor of a Jacobian

*Chapter context.* This belongs to the chapter on the Jacobian of a curve, in a book on abelian varieties and curves. Assumed known:

* smooth projective geometrically integral curves $C$ over a field $K$, Riemann–Roch and Serre duality;
* the Picard scheme $\mathrm{Pic}_{C/K}$, its components $\mathrm{Pic}^d_{C/K}$ (torsors under $J:=\mathrm{Pic}^0_{C/K}$), and the Jacobian $J$ as an abelian variety of dimension $g$;
* the theorem of the square, the polarization $\varphi_L\colon J\to J^\vee$, $a\mapsto t_a^*L\otimes L^{-1}$, of a line bundle, the dual abelian variety and the Poincaré bundle.

Symmetric powers, $W_d$ and the theta divisor are introduced here. Let $g\ge1$ be the genus of $C$.

**Proposition 30.1 (symmetric powers).** For $d\ge1$ the quotient $C^{(d)}:=C^d/S_d$ exists. It is a smooth projective geometrically integral $K$-variety of dimension $d$. It represents the functor sending $T$ to the set of relative effective Cartier divisors of degree $d$ in $C\times T$ over $T$. Put $C^{(0)}:=\operatorname{Spec}K$, corresponding to the zero divisor.

**Definition 30.2 (Abel–Jacobi maps and $W_d$).** For $d\ge0$, let $u_d\colon C^{(d)}\to\mathrm{Pic}^d_{C/K}$ be the morphism $D\mapsto[\mathcal{O}(D)]$. Let $W_d\subseteq\mathrm{Pic}^d_{C/K}$ be its scheme-theoretic image, an integral closed subvariety. Over $\bar K$,
$$W_d(\bar K)=\{\,L\in\mathrm{Pic}^d(C_{\bar K}):\ h^0(C_{\bar K},L)>0\,\}.$$
For $0\le d\le g$, the map $u_d$ is birational onto $W_d$, and $\dim W_d=d$. In particular $W_{g-1}$ is a prime divisor in $\mathrm{Pic}^{g-1}_{C/K}$.

**Definition 30.3 (theta divisor).** Let $L\supseteq K$ be a field and $\kappa\in\mathrm{Pic}^{g-1}_{C/K}(L)$. For instance, $\kappa$ can be the class of a line bundle of degree $g-1$ on $C_L$; over $L=\bar K$ every point is of this form. Let $\tau_\kappa\colon J_L\to(\mathrm{Pic}^{g-1}_{C/K})_L$ be the isomorphism $\xi\mapsto\xi\otimes\kappa$. The *theta divisor attached to $\kappa$* is the prime divisor
$$\theta_\kappa:=\tau_\kappa^{-1}\bigl((W_{g-1})_L\bigr)\subseteq J_L,\qquad \theta_\kappa(\bar K)=\{\xi\in J(\bar K): h^0(C_{\bar K},\xi\otimes\kappa)>0\}.$$
A *theta divisor* of $J$ is any $\theta_\kappa$, as an effective divisor on $J_L$. It is *symmetric* if $[-1]^*\theta_\kappa=\theta_\kappa$. Put
$$\Theta:=\mathcal{O}_J\bigl(\theta_\kappa+[-1]^*\theta_\kappa\bigr).$$
Equivalently, for $\alpha$ a divisor of degree $1$ on $C_L$, $\theta_{(g-1)\alpha}$ is the image of $C_L^{g-1}\to J_L$, $(x_1,\dots,x_{g-1})\mapsto\sum_i(x_i-\alpha)$. This is the description used in [2026, 203(1), no. 2].

**Proposition 30.4.**

(a) Riemann's theorem. $\theta_\kappa$ is an ample effective divisor with $h^0(J_L,\mathcal{O}(\theta_\kappa))=1$, and $\varphi_{\mathcal{O}(\theta_\kappa)}\colon J_L\to J_L^\vee$ is an isomorphism. This principal polarization does not depend on $\kappa$ and is defined over $K$: it is the *canonical principal polarization* $\varphi$ of $J$.
(b) Translates and symmetry. $t_a^*\theta_\kappa=\theta_{\kappa\otimes a}$ for $a\in J(L)$, so the theta divisors are exactly the translates of any one of them. Also $[-1]^*\theta_\kappa=\theta_{\omega_C\otimes\kappa^{-1}}$, by Riemann–Roch and Serre duality: $h^0(M)=h^0(\omega_C\otimes M^{-1})$ for $\deg M=g-1$. Hence $\theta_\kappa$ is symmetric if and only if $\kappa^{\otimes2}\cong\omega_C$, i.e. $\kappa$ is a theta characteristic. These form a torsor under $J[2]$.
(c) The bundle $\Theta$. By the theorem of the square, the isomorphism class of $\Theta$ does not depend on $\kappa$. It is symmetric and ample, algebraically equivalent to $2\theta_\kappa$, and isomorphic to $\mathcal{O}(2\theta_0)$ for every symmetric theta divisor $\theta_0$. It descends to a line bundle on $J$ over $K$, unique once rigidified at $0$. Moreover, let $\mathcal{P}$ be the Poincaré bundle on $J\times J^\vee$, normalized along both zero sections. Then $\Theta\cong(\mathrm{id},\varphi)^*\mathcal{P}$, because $[2]^*\mathcal{L}\cong\mathcal{L}^{3}\otimes[-1]^*\mathcal{L}$ for every line bundle $\mathcal{L}$.

(See e.g. J. Milne, *Jacobian varieties*, in Cornell–Silverman (eds.), *Arithmetic Geometry*; Arbarello–Cornalba–Griffiths–Harris, *Geometry of Algebraic Curves I*.)

*Remarks.*

(1) A theta divisor is determined only up to translation, and is defined over $K$ only if $\kappa$ can be chosen $K$-rational. The canonical objects over $K$ are the principal polarization $\varphi$ and the symmetric bundle $\Theta$, which is "twice the theta divisor". For $g=1$: $W_0=\{[\mathcal{O}_C]\}$, $\theta_\kappa$ is the point $\kappa^{-1}$, and $\Theta$ has degree $2$.
(2) Heights. $\Theta$ is symmetric, so its Néron–Tate height $\widehat h_\Theta$ (Definition #80) is a quadratic form. A non-symmetric $\theta_\kappa$ would give a height with a linear part. One has $\widehat h_\Theta=2\,\widehat h_{\mathcal{O}(\theta_0)}$ for symmetric $\theta_0$. Hence the normalization $\widehat h=\tfrac12\widehat h_\Theta$ of [2026, 203(1), no. 2] is the Néron–Tate height of a symmetric theta divisor.
(3) Families. For a smooth projective relative curve $X\to S$ of genus $g$, there may be no line bundle of fibre degree $g-1$, hence no relative theta divisor. But $\varphi$ exists over $S$ (Mumford–Fogarty–Kirwan, GIT, §6), and $\Theta:=\Delta_J^*(\mathrm{id}\times\varphi)^*\mathcal{P}$ is defined over $S$. [2026, 203(1), no. 2] writes $\Theta=\Delta_J^*(P^\vee)$ (Definition 2.4) with the opposite sign convention for its $P$, and checks that it agrees fibrewise with $\mathcal{O}(\theta_\alpha+[-1]^*\theta_\alpha)$ (its Theorem A.3(4)).
(4) Use in [2026, 203(1), no. 2]. There $K$ is a number field or a function field of one variable, $C$ has genus $g>1$, and the theta divisor appears only through $\Theta$ on $J_{\bar K}$ and its relative version. The paper calls $\Theta$ symmetric, relatively ample, rigidified, and fibrewise algebraically equivalent to twice a theta divisor.

## 31. Totally geodesic subvariety of a ball quotient

*Chapter context.* This belongs to a chapter on special subvarieties of ball quotients, in a book on complex hyperbolic geometry and locally symmetric varieties. Assumed known: Riemannian and Kähler manifolds, geodesics, totally geodesic submanifolds; the group $G=\mathrm{PU}(1,n)$ and its action on the complex $n$-ball; lattices $\Gamma\subset G$; the ball quotient $S_\Gamma=\Gamma\backslash X$ with its structure of normal quasi-projective complex variety and the quotient map $\pi\colon X\to S_\Gamma$ (Definition #15); arithmetic lattices (Definition #68).

**Setting 31.1.** Let $V=\mathbb{C}^{n+1}$, $n\ge1$, carry the Hermitian form $\phi(z,w)=z_1\bar w_1-\sum_{i=2}^{n+1}z_i\bar w_i$, of signature $(1,n)$. Put $X:=\{[z]\in\mathbb{P}(V):\phi(z,z)>0\}$. In the chart $z_1=1$ this is the unit ball $\mathbb{B}^n\subset\mathbb{C}^n$. The group $G=\mathrm{PU}(V,\phi)\cong\mathrm{PU}(1,n)$ acts transitively by biholomorphisms. The *canonical Kähler metric* $g_X$ is a $G$-invariant Kähler metric on $X$, for instance the Bergman metric. Such a metric is unique up to a positive constant, and none of the notions below depends on the constant. Let $\Gamma\subset G$ be a lattice and $\pi\colon X\to S_\Gamma=\Gamma\backslash X$ the quotient map.

**Definition 31.2.** A submanifold $N$ of a Riemannian manifold $(M,g)$ is *totally geodesic* if, for every geodesic $\gamma$ of $M$ with $\gamma(0)\in N$ and $\gamma'(0)\in T_{\gamma(0)}N$, one has $\gamma(t)\in N$ for all sufficiently small $|t|$. Equivalently, the second fundamental form of $N$ vanishes. Here $N$ is embedded, not necessarily closed.

**Proposition 31.3 (complex totally geodesic submanifolds of the ball).** Let $W'\subseteq V$ be a complex linear subspace of dimension $m+1$, with $1\le m\le n$, on which $\phi$ has signature $(1,m)$. Then $X_{W'}:=X\cap\mathbb{P}(W')$ is a closed, connected, totally geodesic complex submanifold of $X$. It is biholomorphic to $\mathbb{B}^m$, and in the ball model it is $\mathbb{B}^n\cap A$ for a complex affine subspace $A$. Its stabilizer in $G$ acts on it through $\mathrm{PU}(1,m)$. Conversely, every connected totally geodesic complex submanifold of $X$ of dimension $m\ge1$ is an open subset of a unique $X_{W'}$. Consequently, if $Z\subseteq X$ is an irreducible closed analytic subset of dimension $m\ge1$ whose regular locus is totally geodesic, then $Z=X_{W'}$ for a unique $W'$. (W. Goldman, *Complex hyperbolic geometry*.)

**Definition 31.4 (totally geodesic subvariety).** In Setting 31.1, let $W\subseteq S_\Gamma$ be an irreducible closed algebraic subvariety of dimension $\ge1$. Then $W$ is *totally geodesic* if some irreducible component $Z$ of the analytic set $\pi^{-1}(W)\subseteq X$ has totally geodesic regular locus $Z^{\mathrm{reg}}\subseteq(X,g_X)$. By 31.3 this means $Z=X_{W'}$. Since $\Gamma$ permutes the components of $\pi^{-1}(W)$ transitively and acts by isometries, "some" may be replaced by "every". Further terminology:

* $W$ is a *strict* totally geodesic subvariety if in addition $W\neq S_\Gamma$;
* $W$ is a *maximal* totally geodesic subvariety if it is strict and is not strictly contained in any strict totally geodesic subvariety of $S_\Gamma$.

$S_\Gamma$ itself is totally geodesic, with $Z=X$. Points are excluded by the condition $\dim W\ge1$.

**Proposition 31.5 (equivalent formulations).**

(a) Smooth-locus formulation. Let $\Gamma'\subseteq\Gamma$ be a torsion-free normal subgroup of finite index, which exists by Selberg's lemma. Then $S_{\Gamma'}$ is a complex manifold with the Kähler metric induced by $g_X$, and $p\colon S_{\Gamma'}\to S_\Gamma$ is finite. $W$ is totally geodesic if and only if the regular locus of some (equivalently every) irreducible component of $p^{-1}(W)$ is totally geodesic in $S_{\Gamma'}$. If $\Gamma$ is torsion-free, this says that $W^{\mathrm{reg}}$ is totally geodesic in $S_\Gamma$, which is the phrasing of [2023, 197(1), no. 3].
(b) Group-theoretic formulation. Let $W$ be totally geodesic with $Z=X_{W'}$, and let $H\subseteq G$ be the stabilizer of $X_{W'}$. Then $\Gamma\cap H$ is a lattice in $H$, and $W=\pi(X_{W'})$. Conversely, if $\Gamma\cap H$ is a lattice in $H$, then $\pi(X_{W'})$ is a closed algebraic totally geodesic subvariety. This is the description of totally geodesic subvarieties as "$\Gamma$-special" subvarieties in [2023, 197(1), no. 3] (Definition 3.1.13, Theorem 1.3.2).

*Remarks.*

(1) Only complex totally geodesic submanifolds matter, because $W$ is a complex subvariety. The ball also contains totally real totally geodesic submanifolds (copies of real hyperbolic space), which are not considered here. For $n=1$ the only totally geodesic subvariety is $S_\Gamma$.
(2) The paper's maximality. [2023, 197(1), no. 3] calls a totally geodesic subvariety maximal if it is not strictly contained in any totally geodesic subvariety different from $S_\Gamma$. Read literally, this also counts $S_\Gamma$ as maximal. That one extra element does not affect the finiteness statement of Theorem 1.2.1.
(3) Arithmeticity. Theorem 1.2.1 says: if $\Gamma$ is non-arithmetic (Definition #68), there are only finitely many maximal totally geodesic subvarieties. For arithmetic $\Gamma$, by contrast, Hecke correspondences show that one strict totally geodesic subvariety, if it exists, forces countably infinitely many. Conversely, infinitely many maximal ones force $\Gamma$ to be arithmetic.
(4) Use in [2023, 197(1), no. 3]. There $G=\mathrm{PU}(1,n)$ with $n>1$, and $\Gamma$ is an arbitrary lattice, possibly non-cocompact and with torsion. Subvarieties are algebraic subvarieties of the quasi-projective variety $S_\Gamma$. In Theorem 1.2.2, "contained in a strict totally geodesic subvariety" uses the notion of 31.4. The algebraic structure on $X\times S_\Gamma$ used there, from the Borel embedding $X\subset\mathbb{P}^n$, is not needed for this definition.

# Analysis & PDE

## 32. The spaces $C^k(M)$ and $C^{k,\alpha}(M)$ on a compact manifold

*Chapter context.* A chapter on function spaces on manifolds in a book on global analysis or smooth dynamics. The reader knows smooth manifolds (possibly with boundary), charts and atlases, partitions of unity, derivatives of functions on open subsets of $\mathbb{R}^n$, Banach spaces, Riemannian metrics and their distance functions, and Hölder functions on a metric space; the normed spaces $C^k(M)$ and $C^{k,\alpha}(M)$ are defined here.

Throughout, $M$ is a compact $C^\infty$ manifold of dimension $n$, possibly with boundary (charts then take values in the half-space $\{x\in\mathbb{R}^n : x_n\ge 0\}$, and derivatives at boundary points are one-sided limits, which exist by continuity of the interior derivatives). Functions take values in $\mathbb{F}=\mathbb{R}$ or $\mathbb{C}$; for $\mathbb{F}^N$-valued functions, apply everything componentwise. We fix $k\in\mathbb{N}=\{0,1,2,\dots\}$ and $\alpha\in(0,1]$. For a set $S\subseteq\mathbb{R}^n$ and $v\colon S\to\mathbb{F}$ we write $\|v\|_{\infty,S}=\sup_{S}|v|$ and
$$[v]_{\alpha,S}=\sup_{x,y\in S,\ x\neq y}\frac{|v(x)-v(y)|}{|x-y|^{\alpha}}\in[0,\infty].$$

**Definition 32.1 (admissible chart system).** An *admissible chart system* on $M$ is a finite family $\mathcal{A}=\{(U_i,\varphi_i,K_i)\}_{i=1}^{m}$ where each $(U_i,\varphi_i)$ is a chart of the smooth structure of $M$, each $K_i\subseteq U_i$ is compact, and $M=K_1\cup\dots\cup K_m$. Such systems exist by compactness.

**Definition 32.2 (the spaces).**

(a) $C^k(M)$ is the set of functions $u\colon M\to\mathbb{F}$ such that $u\circ\varphi^{-1}$ is $k$ times continuously differentiable on $\varphi(U)$ for every chart $(U,\varphi)$ of $M$. Given an admissible chart system $\mathcal{A}$, put $u_i=u\circ\varphi_i^{-1}$ and
$$\|u\|_{C^k}=\max_{1\le i\le m}\ \max_{|\beta|\le k}\ \|\partial^\beta u_i\|_{\infty,\varphi_i(K_i)},$$
where $\beta$ runs over multi-indices in $\mathbb{N}^n$. Also $C^\infty(M)=\bigcap_k C^k(M)$.

(b) $C^{k,\alpha}(M)$ is the set of $u\in C^k(M)$ such that
$$\|u\|_{C^{k,\alpha}}=\|u\|_{C^k}+\max_{1\le i\le m}\ \max_{|\beta|=k}\ [\partial^\beta u_i]_{\alpha,\varphi_i(K_i)}<\infty.$$
The case $\alpha=1$ is allowed ($C^{0,1}(M)$ is the space of Lipschitz functions). For real $r\ge 0$ we write $C^r(M)=C^k(M)$ if $r=k$ is an integer, and $C^r(M)=C^{\lfloor r\rfloor,\,r-\lfloor r\rfloor}(M)$ otherwise; also $C^{k+\alpha}(M)$ means $C^{k,\alpha}(M)$.

(c) A map $f\colon M\to M'$ between compact manifolds is *of class $C^{k,\alpha}$* if it is continuous and, for all charts $(U,\varphi)$ of $M$ and $(V,\psi)$ of $M'$ and every compact $K\subseteq U\cap f^{-1}(V)$, the local representative $\psi\circ f\circ\varphi^{-1}$ is $C^k$ on $\varphi(U\cap f^{-1}(V))$ and all its partial derivatives of order $k$ have finite $[\,\cdot\,]_{\alpha,\varphi(K)}$. For $k\ge 1$, a *$C^{k,\alpha}$ diffeomorphism* is a bijection $f$ such that $f$ and $f^{-1}$ are of class $C^{k,\alpha}$. "$C^\infty$" and "$C^{k}$" for maps have the usual meaning.

**Proposition 32.3.** (i) For $u\in C^k(M)$, $\|u\|_{C^k}<\infty$, and $u\in C^{k,\alpha}(M)$ if and only if, for every chart $(U,\varphi)$ and every compact $K\subseteq U$, the order-$k$ partial derivatives of $u\circ\varphi^{-1}$ have finite $[\,\cdot\,]_{\alpha,\varphi(K)}$. In particular the set $C^{k,\alpha}(M)$ does not depend on $\mathcal{A}$.
(ii) If $\mathcal{A},\mathcal{A}'$ are two admissible chart systems, the corresponding $C^k$ norms are equivalent, and so are the corresponding $C^{k,\alpha}$ norms.
(iii) $(C^k(M),\|\cdot\|_{C^k})$ and $(C^{k,\alpha}(M),\|\cdot\|_{C^{k,\alpha}})$ are Banach spaces, and $C^{k,\alpha}(M)\subseteq C^{k',\alpha'}(M)$ continuously whenever $k'\le k$ and $k'+\alpha'\le k+\alpha$, where $k'\in\mathbb{N}$, $\alpha'\in[0,1]$, and $C^{k',0}$ means $C^{k'}$ (but $C^{k,1}\not\subseteq C^{k+1}$).
(iv) Let $d$ be the distance of a Riemannian metric on $M$ (with $M$ connected). Then $u\in C^{0,\alpha}(M)$ if and only if $\sup_{x\ne y}|u(x)-u(y)|/d(x,y)^{\alpha}<\infty$, and $\|u\|_{\infty}+\sup_{x\ne y}|u(x)-u(y)|/d(x,y)^{\alpha}$ is an equivalent norm on $C^{0,\alpha}(M)$.

(Proof: chart transition maps are $C^\infty$, hence bi-Lipschitz with bounded derivatives on compact sets; use the chain rule and the Leibniz formula, and a Lebesgue-number argument to pass from small to large distances.)

**Definition 32.4.** The *$C^k$ norm* and *$C^{k,\alpha}$ (Hölder) norm* on $M$ are the norms of Definition 32.2 for some fixed admissible chart system; by Proposition 32.3(ii) they are well defined up to equivalence, and all statements of the form "$\le C\|u\|_{C^r}$ for some constant $C$" are independent of the choice. A function in $C^{0,\alpha}(M)$ for some $\alpha\in(0,1]$ is called *Hölder continuous* (with exponent $\alpha$).

*Remarks.* (1) Equivalent norms in common use: sums instead of maxima; $\sum_j\|(\rho_j u)\circ\varphi_j^{-1}\|_{C^{k,\alpha}(\mathbb{R}^n)}$ for a partition of unity $(\rho_j)$ subordinate to a finite atlas; Hölder quotients restricted to $|x-y|\le 1$; or, given a Riemannian metric, $\max_{j\le k}\sup|\nabla^j u|$ plus a Hölder seminorm of $\nabla^k u$ defined via parallel transport along short geodesics. Only the equivalence class of the norm matters in the papers.

(2) The integer case $C^k$ is *not* $C^{k-1,1}$; the convention $C^r=C^{\lfloor r\rfloor,r-\lfloor r\rfloor}$ is used only for non-integer $r$.
(3) On a non-compact manifold (or one with non-compact boundary) one uses the local space $C^{k,\alpha}_{\mathrm{loc}}$: the condition of Proposition 32.3(i) for every chart and compact $K$, with no global norm.
(4) Uses: [2023, 197(1), no. 2] takes complex-valued test functions $A,B\in C^\beta(M)$ for every $\beta>0$, on a compact Riemannian 3-manifold (small $\beta$ is the substantial case, since $C^\beta$ shrinks as $\beta$ grows; for $\beta\le 1$ Proposition 32.3(iv) shows that the Riemannian distance may be used). [2024, 199(3), no. 5] uses the $C^{\mathbf r}(M)$ norm $\|\cdot\|_{\mathbf r}$ with $\mathbf r\in\mathbb{N}$ in the definition of exponential mixing (and $C^r$ for real $r>0$ in its Appendix B), and $C^{1+\alpha}$ diffeomorphisms in the sense of Definition 32.2(c). [2023, 198(1), no. 3] states $g_{\mu\nu}\in C^{1,c\epsilon^2}(\mathcal{M})$ and $g_{\mu\nu}\in C^N$ for the coordinate components of a metric on a non-compact manifold with boundary, i.e. a statement about the functions $g_{\mu\nu}$ in the given coordinates $(u,\hat v,\theta^A)$ (with charts on $\mathbb{S}^2$); no global norm is specified there, and the natural reading is the local one of Remark (3).

## 33. Domain of dependence and development of initial data for the compressible Euler equations

*Chapter context.* A chapter on the acoustical geometry of compressible fluids in a monograph on multidimensional hyperbolic conservation laws. The reader knows the isentropic compressible Euler equations, Lorentzian metrics, time orientations and null hypersurfaces (Definition #51), and classical ($C^1$) solutions of first-order systems; the acoustical causal structure, domains of dependence and developments are defined here.

Throughout, spacetime is $\mathfrak{M}=\mathbb{R}_t\times\Sigma$ with $\Sigma=\mathbb{R}^n$ or $\Sigma=\mathbb{R}\times(\mathbb{R}/2\pi\mathbb{Z})^{n-1}$, with coordinates $(t,x^1,\dots,x^n)$ and $\Sigma_{\tau}=\{t=\tau\}$. The isentropic Euler equations for density $\rho>0$ and velocity $v=(v^1,\dots,v^n)$ are
$$(\partial_t+v\cdot\nabla)\rho=-\rho\,\nabla\cdot v,\qquad(\partial_t+v\cdot\nabla)v=-\rho^{-1}\nabla p,\tag{E}$$
with a smooth equation of state $p=p(\rho)$, $p'>0$, and sound speed $c=\sqrt{p'(\rho)}>0$. (For the polytropic law $p=k_0\rho^\gamma$, $\gamma>1$, the map $\rho\mapsto c$ is a bijection onto $(0,\infty)$ and one uses $(v,c)$ as unknowns.) A *state* on a set $D\subseteq\mathfrak{M}$ is a pair $(\rho,v)$ of class $C^1$ on $D$ (i.e. $C^1$ on the interior, which is dense in $D$, with all first derivatives extending continuously to $D$) with $\rho>0$.

**Definition 33.1 (acoustical metric and causal curves).** The *acoustical metric* of a state is the Lorentzian metric
$$g=-c^2\,dt^2+\sum_{i=1}^n\big(dx^i-v^i\,dt\big)^2 .$$
A tangent vector $X=X^t\partial_t+X^i\partial_i\neq0$ at a point of $D$ is *causal* if $g(X,X)\le0$, *null* if $g(X,X)=0$, and *future-directed* if $X^t>0$ (every causal vector has $X^t\neq0$, since $g(X,X)=\sum_i (X^i)^2$ when $X^t=0$). A *future-directed causal curve* in $D$ is a curve that can be parametrised by $t$ as $\gamma(t)=(t,x(t))$, $t\in I$ an interval, with $x\colon I\to\Sigma$ locally Lipschitz, $\gamma(I)\subseteq D$, and
$$\big|\dot x(t)-v(t,x(t))\big|\le c(t,x(t))\qquad\text{for a.e. }t\in I,$$
which is exactly the condition that $\dot\gamma$ is future-directed causal. If $b=\max I$, the curve *ends at* $\gamma(b)$; it is *past-inextendible in $D$* if there is no future-directed causal curve in $D$ defined on an interval $I'\supsetneq I$ with $\max I'=b$ that restricts to $\gamma$ on $I$ (the one-point curve $I=\{b\}$ is allowed).

**Definition 33.2 (future domain of dependence).** Let $(\rho,v)$ be a state on $D$ with acoustical metric $g$ and let $S\subseteq D$. The *future domain of dependence of $S$ in $D$* is
$$\mathcal{D}^+_D(S)=\{p\in D:\ \text{every past-inextendible future-directed causal curve in } D \text{ ending at } p \text{ meets } S\}.$$
Trivially $S\subseteq\mathcal{D}^+_D(S)$; if $D\subseteq\{t\ge t_0\}$ and $S\subseteq\Sigma_{t_0}$, then $\mathcal{D}^+_D(S)\cap\Sigma_{t_0}\subseteq S$.

**Definition 33.3 (data and development).** *Initial data* consist of a set $S\subseteq\mathfrak{M}$ which is either (i) a closed subset of $\Sigma_{t_0}$ with nonempty interior in $\Sigma_{t_0}$, or (ii) a union $S=S_0\cup C$ of such a set $S_0\subseteq\Sigma_{t_0}$ and a hypersurface $C\subseteq\{t\ge t_0\}$ with $C\cap\Sigma_{t_0}\subseteq S_0$ (characteristic data), together with prescribed values $(\bar\rho,\bar v)$ on $S$. A *development* of the data is a pair $(D,(\rho,v))$ where

1. $D\subseteq\{t\ge t_0\}$, $S\subseteq D$, and $(\rho,v)$ is a state on $D$ solving (E) on the interior of $D$;
2. $(\rho,v)|_S=(\bar\rho,\bar v)$;
3. $D=\mathcal{D}^+_D(S)$ for the acoustical metric of $(\rho,v)$, i.e. every point of $D$ is determined by the data;
4. in case (ii), $C$ is a null hypersurface of $g$ in the sense of Definition #51.

Developments are ordered by $(D_1,\phi_1)\le(D_2,\phi_2)$ iff $D_1\subseteq D_2$ and $\phi_2|_{D_1}=\phi_1$.

**Proposition 33.4 (uniqueness; maximal development).** If $(D_1,\phi_1)$ and $(D_2,\phi_2)$ are developments of the same data, then $\phi_1=\phi_2$ on $D_1\cap D_2$. Consequently, if the data admit a development, the union $D_{\max}$ of the domains of all developments, with the glued solution, is again a development, and it is the unique maximal element for $\le$. (Proof: local uniqueness for quasilinear symmetric hyperbolic systems in lens-shaped domains, propagated by a continuity argument along the time function $t$; for this framework see D. Christodoulou, *The Formation of Shocks in 3-Dimensional Fluids*.) Existence: for data of type (i) given by restrictions to $S$ of $H^s$ functions on $\Sigma_{t_0}$, $s>n/2+1$, with $\bar\rho$ bounded below by a positive constant, extend the data to all of $\Sigma_{t_0}$, solve by local well-posedness on $[t_0,t_0+T]\times\Sigma$, and restrict to the domain of dependence of $S$; characteristic data (ii) need in addition the constraint and compatibility conditions on $C$.

**Definition 33.5 (domain of dependence of the data; characteristic boundary).** The *(future) domain of dependence of the data*, or *the development of the data*, is $D_{\max}$ (in practice intersected with a time slab $\{t_0\le t\le t^*\}$). Its *characteristic boundary* is the part of its topological boundary lying in $\{t>t_0\}$, i.e. $\partial D_{\max}\cap\{t>t_0\}$ (for case (ii), excluding $C$). Where it is a $C^1$ hypersurface it is a null hypersurface of $g$ (Definition #51), ruled by null geodesics of $g$; in the situations below these issue from the edge $\partial_{\Sigma_{t_0}}S_0$ of the data set (compare the smooth Lorentzian theory of Cauchy horizons in Hawking–Ellis, *The Large Scale Structure of Space-Time*, Ch. 6).

*Remarks.* (1) The acoustical metric depends on the unknown, so "domain of dependence of the data" only makes sense through developments (Definition 33.3): condition 3 refers to the metric of the very solution being constructed. For a known solution on an open set $U$, $\mathcal{D}^+_U(S)$ of Definition 33.2 is the ordinary Lorentzian notion. Equivalent formulations use piecewise $C^1$ causal curves, or the sets $J^-(p)$; $g^{-1}(dt,dt)=-c^{-2}<0$, so $t$ is a time function and the $\Sigma_\tau$ are spacelike.

(2) In the half-space problem with data on $S=\{t=0,\ x^1\ge0\}$, $\partial D_{\max}\cap\{t>0\}$ is the "right-going" acoustical null hypersurface $C_0$ emanating from $\{t=0,x^1=0\}$, which to first approximation moves with speed $v^1+c$.
(3) Uses: [2025, 202(2), no. 2] takes $n=2$, $\Sigma=\mathbb{R}\times\mathbb{R}/2\pi\mathbb{Z}$, $p=k_0\rho^\gamma$, $\gamma\in(1,3)$; $D_0$ is the domain of dependence of irrotational data on $\{x^1\ge0\}$ with characteristic boundary $C_0$, and $\mathcal{D}$ is the development of characteristic data of type (ii) on $\Sigma_\delta^{u^*}\cup C_0$ (the data on $C_0$ being the trace of the solution in $D_0$); the main theorem asserts $\mathcal{D}\supset\mathcal{D}(1,u^*)$. [2025, 202(2), no. 3] uses the characteristic boundaries $\underline{C}_0$, $C_0$ of the domains of dependence of the left data on $\{x^1\le0\}$ and the right data on $\{x^1\ge0\}$.

## 34. Neumann eigenvalues and eigenfunctions of the Laplacian on a bounded domain

*Chapter context.* A chapter on the spectral theory of the Laplacian in a book on elliptic PDE (or spectral geometry). The reader knows the Sobolev spaces $H^1(\Omega)$ and $H^1_0(\Omega)$, Lipschitz domains and the trace theorem, the Rellich–Kondrachov theorem, the spectral theorem for compact self-adjoint operators, the Riesz representation theorem, and the Dirichlet eigenvalues (defined in the preceding section via $H^1_0(\Omega)$); the Neumann problem is treated here.

Throughout, $\Omega\subseteq\mathbb{R}^n$ is a nonempty bounded open set with Lipschitz boundary, $L^2(\Omega)$ is the real Hilbert space with $\langle u,w\rangle=\int_\Omega uw\,dx$, and $\Delta=-\sum_{j}\partial_j^2$ is the nonnegative Laplacian.

**Definition 34.1 (weak Neumann eigenfunction).** The *Neumann form* is the symmetric bilinear form $q(u,w)=\int_\Omega\nabla u\cdot\nabla w\,dx$ on $H^1(\Omega)$. A pair $(\mu,u)\in\mathbb{R}\times H^1(\Omega)$ with $u\neq0$ is a *Neumann eigenpair* if
$$q(u,w)=\mu\,\langle u,w\rangle\qquad\text{for all } w\in H^1(\Omega).$$
Then $u$ is a *Neumann eigenfunction* with *Neumann eigenvalue* $\mu$, and $E_\mu=\{u\in H^1(\Omega): q(u,w)=\mu\langle u,w\rangle\ \forall w\in H^1(\Omega)\}$ is the *eigenspace*; the *multiplicity* of $\mu$ is $\dim E_\mu$. (Testing against all of $H^1(\Omega)$, not just $H^1_0(\Omega)$, is what imposes the boundary condition $\partial u/\partial n=0$.)

**Theorem 34.2 (Neumann spectrum).** The inclusion $H^1(\Omega)\hookrightarrow L^2(\Omega)$ is compact. Consequently there is an orthonormal basis $(u_k)_{k\ge1}$ of $L^2(\Omega)$ and real numbers $\mu_1\le\mu_2\le\cdots$ with $\mu_k\to\infty$ such that each $(\mu_k,u_k)$ is a Neumann eigenpair; every Neumann eigenvalue equals some $\mu_k$; each eigenvalue has finite multiplicity, equal to $\#\{k:\mu_k=\mu\}$; and $\mu_1=0$, with $E_0$ the locally constant functions, so $\dim E_0$ is the number of connected components of $\Omega$. The numbers satisfy the min–max formula
$$\mu_k=\min_{\substack{V\subseteq H^1(\Omega)\\ \dim V=k}}\ \max_{u\in V\setminus\{0\}}\frac{\int_\Omega|\nabla u|^2\,dx}{\int_\Omega u^2\,dx},$$
so the sequence $(\mu_k)$ is independent of the choice of basis. (Proof: for $f\in L^2(\Omega)$ let $Tf\in H^1(\Omega)$ be the unique solution of $q(Tf,w)+\langle Tf,w\rangle=\langle f,w\rangle$ for all $w\in H^1(\Omega)$; $T$ is compact, self-adjoint and positive on $L^2(\Omega)$, and its eigenvalues are $(1+\mu_k)^{-1}$.)

**Proposition 34.3 (regularity and the classical problem).** Let $(\mu,u)$ be a Neumann eigenpair.

(i) $u$ is real-analytic in $\Omega$ and $\Delta u=\mu u$ there.
(ii) If $\partial\Omega$ is $C^\infty$, then $u\in C^\infty(\overline\Omega)$ and $\partial u/\partial n=0$ on $\partial\Omega$, with $n$ the outward unit normal.
(iii) If $\Omega\subseteq\mathbb{R}^2$ is the interior of a polygon (e.g. a triangle) with vertex set $P$, then $u$ extends continuously to $\overline\Omega$, is $C^\infty$ (indeed real-analytic) on $\overline\Omega\setminus P$, and $\partial u/\partial n=0$ on each open side.
Conversely, in the situations (ii) and (iii), if $u\in H^1(\Omega)\cap C^2(\Omega)\cap C^1(\overline\Omega\setminus P)$ (with $P=\emptyset$ in case (ii)), $u\neq0$, satisfies $\Delta u=\mu u$ in $\Omega$ and $\partial u/\partial n=0$ on $\partial\Omega\setminus P$, then $(\mu,u)$ is a Neumann eigenpair. (Green's formula; near the vertices use logarithmic cut-offs, points having zero capacity in $\mathbb{R}^2$.)

**Definition 34.4 (Neumann eigenvalues, spectrum, second eigenfunction).** Let $\Omega$ be as above.

(a) The *$k$-th Neumann eigenvalue* of $\Omega$ is the number $\mu_k(\Omega)$ of Theorem 34.2 ($k\ge1$); thus $0=\mu_1(\Omega)\le\mu_2(\Omega)\le\cdots$, each eigenvalue repeated according to its multiplicity.
(b) The *Neumann (Laplace) spectrum* of $\Omega$ is the sequence $(\mu_k(\Omega))_{k\ge1}$, equivalently the multiset of Neumann eigenvalues with their multiplicities. Two domains $\Omega,\Omega'$ are *Neumann isospectral* if $\mu_k(\Omega)=\mu_k(\Omega')$ for all $k$.
(c) The *second Neumann eigenvalue* is $\mu_2(\Omega)$; a *second Neumann eigenfunction* is any $u\in E_{\mu_2(\Omega)}\setminus\{0\}$. If $\Omega$ is connected, $\mu_2(\Omega)>0$ is the smallest positive Neumann eigenvalue and
$$\mu_2(\Omega)=\min\Big\{\tfrac{\int_\Omega|\nabla u|^2}{\int_\Omega u^2}:\ u\in H^1(\Omega)\setminus\{0\},\ \int_\Omega u\,dx=0\Big\},$$
the minimisers being exactly the second Neumann eigenfunctions.

*Remarks.* (1) Equivalently, $\mu_k(\Omega)$ are the eigenvalues of the *Neumann Laplacian* $\Delta_N$, the nonnegative self-adjoint operator on $L^2(\Omega)$ associated with the closed form $q$ on $H^1(\Omega)$: its domain is the set of $u\in H^1(\Omega)$ for which some $f\in L^2(\Omega)$ satisfies $q(u,w)=\langle f,w\rangle$ for all $w\in H^1(\Omega)$, and $\Delta_N u=f$; it has compact resolvent. Complex scalars give the same eigenvalues.

(2) Conventions: many analysts write $\Delta=+\sum\partial_j^2$ and eigenvalue problems $-\Delta u=\mu u$; some index from $\mu_0=0$, so that "the first nonzero eigenvalue" is $\mu_1$. Some authors drop the Lipschitz hypothesis and work on arbitrary bounded open sets, where $H^1(\Omega)\hookrightarrow L^2(\Omega)$ may fail to be compact.
(3) Uses: [2020, 191(1), no. 3] takes $\Omega=T$ a Euclidean triangle and the classical formulation (smooth $u$ with $\Delta u=\mu_2u$, $\partial u/\partial n=0$ at smooth boundary points), which by Proposition 34.3(iii) agrees with Definition 34.4(c) for $u\in H^1(T)$; vertices are never counted as critical points. [2022, 196(3), no. 4] compares the Neumann (and Dirichlet) spectra, counted with multiplicity, of bounded planar domains with $C^\infty$ boundary, "uniquely determined" meaning up to rigid motions of $\mathbb{R}^2$.

## 35. Absolutely continuous spectrum of a self-adjoint operator

*Chapter context.* A chapter on the spectral types of self-adjoint operators in a book on spectral theory or mathematical physics. The reader knows (possibly unbounded) self-adjoint operators on a complex Hilbert space, their spectrum, the spectral theorem in projection-valued-measure form, and the Lebesgue decomposition of finite Borel measures on $\mathbb{R}$; the spectral subspaces and the spectral types are introduced here.

Throughout, $\mathcal{H}$ is a complex Hilbert space, $H$ is a self-adjoint operator in $\mathcal{H}$ with domain $\mathcal{D}(H)$, and $E$ is its spectral measure (projection-valued measure on the Borel sets of $\mathbb{R}$, with $H=\int\lambda\,dE(\lambda)$). Lebesgue measure on $\mathbb{R}$ is denoted $|\cdot|$.

**Definition 35.1 (spectral measure of a vector).** For $f\in\mathcal{H}$, the *spectral measure of $f$* (with respect to $H$) is the finite positive Borel measure on $\mathbb{R}$
$$\mu_f(B)=\langle E(B)f,f\rangle=\|E(B)f\|^2,\qquad \mu_f(\mathbb{R})=\|f\|^2 .$$
It is characterised by $\langle (H-z)^{-1}f,f\rangle=\int_{\mathbb{R}}(\lambda-z)^{-1}\,d\mu_f(\lambda)$ for all $z\in\mathbb{C}\setminus\mathbb{R}$.

**Definition 35.2 (spectral subspaces).** Put
$$\mathcal{H}_{\mathrm{ac}}=\{f\in\mathcal{H}:\ \mu_f \text{ is absolutely continuous with respect to } |\cdot|\},\qquad \mathcal{H}_{\mathrm{s}}=\{f\in\mathcal{H}:\ \mu_f\perp|\cdot|\},$$
$$\mathcal{H}_{\mathrm{pp}}=\{f:\ \mu_f \text{ is a countable sum of point masses}\},\qquad \mathcal{H}_{\mathrm{sc}}=\{f:\ \mu_f\perp|\cdot| \text{ and } \mu_f(\{\lambda\})=0\ \forall\lambda\}.$$
Since $\mu_f(N)=\|E(N)f\|^2$, one has the concrete descriptions $\mathcal{H}_{\mathrm{ac}}=\bigcap_{N}\ker E(N)$, the intersection over all Lebesgue-null Borel sets $N\subseteq\mathbb{R}$, and $\mathcal{H}_{\mathrm{s}}=\{f:\ E(N)f=f \text{ for some Lebesgue-null Borel } N\}$; $\mathcal{H}_{\mathrm{pp}}$ is the closed linear span of the eigenvectors of $H$.

**Proposition 35.3.** (i) $\mathcal{H}_{\mathrm{ac}}$, $\mathcal{H}_{\mathrm{sc}}$, $\mathcal{H}_{\mathrm{pp}}$ are closed, mutually orthogonal subspaces with $\mathcal{H}=\mathcal{H}_{\mathrm{ac}}\oplus\mathcal{H}_{\mathrm{sc}}\oplus\mathcal{H}_{\mathrm{pp}}$ and $\mathcal{H}_{\mathrm{s}}=\mathcal{H}_{\mathrm{sc}}\oplus\mathcal{H}_{\mathrm{pp}}=\mathcal{H}_{\mathrm{ac}}^{\perp}$.
(ii) Each of them reduces $H$: if $P$ denotes the orthogonal projection onto one of them, then $PE(B)=E(B)P$ for all Borel $B$, $P\,\mathcal{D}(H)\subseteq\mathcal{D}(H)$, and $HPf=PHf$ for $f\in\mathcal{D}(H)$. Hence $H_{\mathrm{ac}}:=H|_{\mathcal{D}(H)\cap\mathcal{H}_{\mathrm{ac}}}$ is a self-adjoint operator in the Hilbert space $\mathcal{H}_{\mathrm{ac}}$, with spectral measure $B\mapsto E(B)|_{\mathcal{H}_{\mathrm{ac}}}$, and similarly for the other types.
(iii) For $f\in\mathcal{H}$, the Lebesgue decomposition $\mu_f=\mu_{f,\mathrm{ac}}+\mu_{f,\mathrm{sc}}+\mu_{f,\mathrm{pp}}$ is given by $\mu_{f,\mathrm{ac}}=\mu_{P_{\mathrm{ac}}f}$, etc.
(See Reed–Simon, *Methods of Modern Mathematical Physics I*, Ch. VII–VIII.)

**Definition 35.4 (absolutely continuous spectrum).** The *absolutely continuous spectrum* of $H$ is
$$\sigma_{\mathrm{ac}}(H)=\sigma(H_{\mathrm{ac}}),$$
the spectrum of the self-adjoint operator $H_{\mathrm{ac}}$ in $\mathcal{H}_{\mathrm{ac}}$ (with $\sigma_{\mathrm{ac}}(H)=\emptyset$ if $\mathcal{H}_{\mathrm{ac}}=\{0\}$). Equivalently,
$$\sigma_{\mathrm{ac}}(H)=\{\lambda\in\mathbb{R}:\ E\big((\lambda-\varepsilon,\lambda+\varepsilon)\big)P_{\mathrm{ac}}\neq0\ \text{for every }\varepsilon>0\},$$
which is also the closure of $\bigcup_{f\in\mathcal{H}_{\mathrm{ac}}}\operatorname{supp}\mu_f$. Likewise $\sigma_{\mathrm{sc}}(H)=\sigma(H_{\mathrm{sc}})$ and $\sigma_{\mathrm{pp}}(H)=\sigma(H_{\mathrm{pp}})$ (the closure of the set of eigenvalues). $H$ has *purely absolutely continuous spectrum* if $\mathcal{H}_{\mathrm{ac}}=\mathcal{H}$.

*Remarks.* (1) $\sigma_{\mathrm{ac}}(H)$ is a closed subset of $\sigma(H)$ and $\sigma(H)=\sigma_{\mathrm{ac}}(H)\cup\sigma_{\mathrm{sc}}(H)\cup\sigma_{\mathrm{pp}}(H)$, but the three sets need not be disjoint. An interval $[a,b]$ (or $[a,\infty)$) lies in $\sigma_{\mathrm{ac}}(H)$ iff $E(I)P_{\mathrm{ac}}\neq0$ for every nonempty open interval $I\subseteq(a,b)$ (resp. $(a,\infty)$). Since absolutely continuous measures have no atoms and are carried by sets of positive Lebesgue measure, every neighbourhood of a point of $\sigma_{\mathrm{ac}}(H)$ meets $\sigma_{\mathrm{ac}}(H)$ in a set of positive Lebesgue measure; in particular $\sigma_{\mathrm{ac}}(H)$ has no isolated points. Example: for multiplication by $x$ on $L^2([0,1])$, $\mathcal{H}_{\mathrm{ac}}=\mathcal{H}$ and $\sigma_{\mathrm{ac}}=[0,1]$.

(2) $\sigma_{\mathrm{ac}}$ is invariant under unitary equivalence and under trace-class perturbations (Kato–Rosenblum), but not under compact ones.
(3) Use: in [2026, 203(2), no. 1], $\mathcal{H}=L^2(\mathbb{R}^d)$, $d\ge2$, and $H=-\Delta+V$ with $V(\mathbf{x})=\sum_{|\mathbf{n}|<Q}V_{\mathbf{n}}e^{i\langle\mathbf{n}\vec{\boldsymbol\omega},\mathbf{x}\rangle}$ a real trigonometric polynomial (real since $V_{\mathbf{n}}=\overline{V_{-\mathbf{n}}}$). $V$ is bounded, so $H$ is self-adjoint on $\mathcal{D}(H)=H^2(\mathbb{R}^d)$ (Kato–Rellich). The theorem asserts $[\lambda_*,\infty)\subseteq\sigma_{\mathrm{ac}}(H)$.

## 36. Amenable trace on a C\*-algebra

*Chapter context.* A chapter on traces and finite-dimensional approximation in a book on C\*-algebras (in the style of Brown–Ozawa, *C\*-Algebras and Finite-Dimensional Approximations*). The reader knows C\*-algebras (not necessarily unital), positive linear functionals and states, the GNS construction, completely positive maps, the matrix algebras $M_n=M_n(\mathbb{C})$, and von Neumann algebras; tracial states and amenable traces are introduced here.

**Definition 36.1 (tracial state; faithful).** Let $A$ be a C\*-algebra. A *tracial state* (in this chapter simply a *trace*) on $A$ is a state $\tau$ on $A$ (a positive linear functional $\tau\colon A\to\mathbb{C}$ with $\|\tau\|=1$) such that $\tau(ab)=\tau(ba)$ for all $a,b\in A$; equivalently, $\tau(a^*a)=\tau(aa^*)$ for all $a\in A$. It is *faithful* if $\tau(a^*a)=0$ implies $a=0$. For $n\ge1$, $\tau_{M_n}(x)=\frac1n\sum_{j=1}^n x_{jj}$ is the unique tracial state on $M_n$, and the *(normalised) 2-norm* on $M_n$ is
$$\|x\|_2=\tau_{M_n}(x^*x)^{1/2}=\Big(\tfrac1n\sum_{j,k}|x_{jk}|^2\Big)^{1/2}.$$

**Definition 36.2 (c.p.c. map).** A linear map $\varphi\colon A\to M_n$ is *completely positive* if $\varphi\otimes\mathrm{id}_{M_k}\colon A\otimes M_k\to M_n\otimes M_k$ is positive for every $k\ge1$, and *contractive* if $\|\varphi\|\le1$ (operator norm on $M_n$). A completely positive contractive map is called *c.p.c.*; if $A$ is unital and $\varphi(1)=1$, it is *u.c.p.*

**Definition 36.3 (amenable trace).** A tracial state $\tau$ on a C\*-algebra $A$ is *amenable* if there exist a directed set $I$ and, for each $i\in I$, an integer $n(i)\ge1$ and a c.p.c. map $\varphi_i\colon A\to M_{n(i)}$, such that for all $a,a'\in A$
$$\lim_{i}\big\|\varphi_i(aa')-\varphi_i(a)\varphi_i(a')\big\|_2=0\qquad\text{and}\qquad\lim_i\tau_{M_{n(i)}}\big(\varphi_i(a)\big)=\tau(a).$$
(The 2-norm is that of $M_{n(i)}$.) A C\*-algebra *admits a faithful amenable trace* if it has a tracial state that is both faithful and amenable.

**Proposition 36.4 (standard reformulations).** Let $\tau$ be a tracial state on $A$.

(i) If $A$ is separable, $\tau$ is amenable iff there is a sequence $(\varphi_k\colon A\to M_{n(k)})_{k\ge1}$ of c.p.c. maps satisfying the two limit conditions as $k\to\infty$.
(ii) If $A$ is unital, the c.p.c. maps may be taken u.c.p.; and $\tau$ is amenable iff for some (equivalently, every) faithful representation $A\subseteq B(\mathcal{H})$ there is a state $\psi$ on $B(\mathcal{H})$ with $\psi|_A=\tau$ and $\psi(uTu^*)=\psi(T)$ for all unitaries $u\in A$ and all $T\in B(\mathcal{H})$ (an *$A$-central state*, or *hypertrace*, extending $\tau$).
(iii) If $A$ is nuclear, every tracial state on $A$ is amenable. If $A$ is exact, $\tau$ is amenable iff the von Neumann algebra $\pi_\tau(A)''$ generated by its GNS representation is hyperfinite (injective).
(iv) If $\iota\colon A\to B$ is a $^*$-homomorphism, $\tau_B$ is an amenable trace on $B$, and $\tau_B\circ\iota$ is a state (e.g. $\iota$ unital), then $\tau_B\circ\iota$ is an amenable trace on $A$ (compose the approximating maps with $\iota$); it is faithful if $\tau_B$ is faithful and $\iota$ is injective.
(References: N. Brown, *Invariant means and finite representation theory of C\*-algebras*, Mem. Amer. Math. Soc. 184 (2006); Brown–Ozawa, Ch. 6. The notion goes back to Connes in the II$_1$-factor setting and to Kirchberg for C\*-algebras.)

*Remarks.* (1) Some books (e.g. Brown–Ozawa) take the hypertrace condition (ii) as the definition for unital $A$, and prove the approximation characterisation; Definition 36.3, with c.p.c. maps, has the advantage of making sense verbatim for non-unital $A$, and it is the one used in [2020, 192(2), no. 1]. Note that the multiplicativity defect is measured in the 2-norm, not the operator norm: requiring $\|\varphi_i(aa')-\varphi_i(a)\varphi_i(a')\|\to0$ in operator norm instead gives the stronger notion of a *quasidiagonal* trace.

(2) Use: [2020, 192(2), no. 1], Theorem A, where "trace" always means tracial state, $A$ is separable and exact, and "trace-preserving embedding" means an injective $^*$-homomorphism $\iota\colon A\to B$ with $\tau_B\circ\iota=\tau_A$. By (iii) and (iv), the existence of such an embedding into a simple unital AF-algebra $B$ (which is nuclear, and on which every trace is faithful) forces $\tau_A$ to be faithful and amenable; the paper shows that, modulo the UCT, this is the only obstruction.

## 37. Caloric gauge and the manifold of caloric connections

*Chapter context.* A chapter on the Yang–Mills heat flow and gauge fixing in a monograph on energy-critical gauge field equations on $\mathbb{R}^4$. The reader knows compact Lie groups and bi-invariant inner products, $\mathfrak{g}$-valued connection 1-forms, covariant derivatives, curvature and gauge transformations, the homogeneous Sobolev spaces $\dot H^\sigma(\mathbb{R}^4)$, Littlewood–Paley projections $P_k$ ($k\in\mathbb{Z}$), and $C^1$ submanifolds of Banach spaces with their tangent spaces; the caloric gauge is introduced here.

Throughout, $\mathbf{G}$ is a compact Lie group with Lie algebra $\mathfrak{g}$ and a bi-invariant inner product $\langle\cdot,\cdot\rangle$. A *connection* on $\mathbb{R}^4$ is a 4-tuple $a=(a_1,\dots,a_4)$ of $\mathfrak{g}$-valued functions; $\dot H^1$ denotes $\dot H^1(\mathbb{R}^4;\mathfrak{g})^4$ (completion of $C^\infty_c$ for $\|\nabla a\|_{L^2}$; it embeds in $L^4$) and $L^2=L^2(\mathbb{R}^4;\mathfrak{g})^4$. For a connection, $D_j=\partial_j+[a_j,\cdot\,]$ and $f_{jk}=\partial_ja_k-\partial_ka_j+[a_j,a_k]$; indices are Euclidean, repeated indices summed. A gauge transformation $O\colon\mathbb{R}^4\to\mathbf{G}$ acts by $\mathcal{G}(O)a_j=Oa_jO^{-1}-\partial_jO\,O^{-1}$.

**Definition 37.1 (Yang–Mills heat flow in the local caloric gauge).** For $a\in\dot H^1$ and an interval $J=[0,s_0)$, the *Yang–Mills heat flow* with data $a$ is the equation for $s\mapsto A(s)=(A_j(s))_j$
$$\partial_sA_j=D^\ell F_{\ell j}\quad(j=1,\dots,4),\qquad A(0)=a,\tag{YMHF}$$
where $D$, $F$ are formed from $A(s)$ (this is the covariant flow $F_{sj}=D^\ell F_{\ell j}$ in the gauge $A_s=0$). Data $a$ are *regular* if $a\in\dot H^\sigma$ for all $\sigma\ge1$; a *regular solution* is an $A$ with $A\in C(J;\dot H^\sigma)$ for all $\sigma\ge1$ satisfying (YMHF) in the sense of distributions on $(0,s_0)\times\mathbb{R}^4$. An *$\dot H^1$ solution* is $A\in C(J;\dot H^1)$ such that for every $s_1\in J$ and every sequence of regular data $a^{(n)}\to a$ in $\dot H^1$, the regular solutions $A^{(n)}$ exist on $[0,s_1]$ for $n$ large and $A^{(n)}\to A$ in $C([0,s_1];\dot H^1)$.

**Theorem 37.2 (Oh–Tataru).** (i) Regular data have unique maximal regular solutions, and for every $a\in\dot H^1$ there is a unique maximal $\dot H^1$ solution $A$, on $[0,s^*)$ with $s^*=s^*(a)\in(0,\infty]$ (it is regular if $a$ is).
(ii) If $s^*<\infty$ then $\|F\|_{L^3([0,s^*)\times\mathbb{R}^4)}=\infty$.
(iii) If $s^*=\infty$ and the *caloric size* $Q(a)=\|F\|_{L^3([0,\infty)\times\mathbb{R}^4)}$ is finite, then $a_\infty=\lim_{s\to\infty}A(s)$ exists in $\dot H^1$ and is flat ($f_\infty=0$).
(iv) If the energy $\frac12\int\langle f_{jk},f_{jk}\rangle\,dx$ is $<2E_{\mathrm{GS}}$ (twice the ground state energy), then $s^*=\infty$ and $Q(a)<\infty$.
(S.-J. Oh, D. Tataru, *The Yang–Mills heat flow and the caloric gauge*, arXiv:1709.08599.) Below, "$Q(a)<\infty$" includes $s^*(a)=\infty$.

**Definition 37.3 (caloric connection; caloric gauge).** A connection $a\in\dot H^1$ is *caloric* if $Q(a)<\infty$ and $a_\infty=0$, i.e. its Yang–Mills heat flow exists for all $s\ge0$, has finite caloric size, and $A(s)\to0$ in $\dot H^1$ as $s\to\infty$. The set of caloric connections is denoted $\mathcal{C}$. A connection (or a family $t\mapsto A_x(t)$ of spatial connections) is *in the caloric gauge* if it is caloric (for every $t$).

**Proposition 37.4 (gauge fixing).** If $\tilde a\in\dot H^1$ has $Q(\tilde a)<\infty$, write $(\tilde a_\infty)_j=O^{-1}\partial_jO$ with $O\colon\mathbb{R}^4\to\mathbf{G}$; then $a=\mathcal{G}(O)\tilde a$ is caloric, and it is the unique caloric connection gauge-equivalent to $\tilde a$ up to constant gauge transformations $a\mapsto O_0aO_0^{-1}$, $O_0\in\mathbf{G}$.

**Definition 37.5 (the space $\mathcal{H}$).** For $u\colon\mathbb{R}^4\to\mathfrak{g}$ put $\|u\|_{\ell^1L^2}=\sum_{k\in\mathbb{Z}}\|P_ku\|_{L^2}$. Let
$$\mathcal{H}=\{a\in\dot H^1:\ \partial^ja_j\in\ell^1L^2\},\qquad \|a\|_{\mathcal{H}}^2=\|a\|_{\dot H^1}^2+\|\partial^ja_j\|_{\ell^1L^2}^2,$$
a Banach space.

**Theorem 37.6 (the caloric manifold).** $\mathcal{C}\subseteq\mathcal{H}$, and $\mathcal{C}$ is a $C^1$ submanifold of $\mathcal{H}$. For $a\in\mathcal{C}$ with heat flow $A$ and $b\in L^2$ (resp. $b\in\mathcal{H}$), the linearised flow
$$\partial_sB_i=D^j(D_jB_i-D_iB_j)+[B^j,F_{ji}],\qquad B(0)=b,\tag{LYMHF}$$
($D,F$ those of $A(s)$) has a unique global solution in $C([0,\infty);L^2)$ (resp. in $\mathcal{H}$), and the tangent space of $\mathcal{C}$ at $a$ is $T_a\mathcal{C}=\{b\in\mathcal{H}:\ B(s)\to0 \text{ in } \mathcal{H} \text{ as } s\to\infty\}$. (Oh–Tataru, op. cit., Section 7.)

**Definition 37.7 ($L^2$ tangent bundle; caloric data).** For $a\in\mathcal{C}$,
$$T^{L^2}_a\mathcal{C}=\{b\in L^2:\ \text{the solution } B \text{ of (LYMHF) satisfies } \|B(s)\|_{L^2}\to0 \text{ as } s\to\infty\},$$
a closed subspace of $L^2$, equal to the closure of $T_a\mathcal{C}$ in the $L^2$ topology. The *$L^2$ tangent bundle* of $\mathcal{C}$ is $T^{L^2}\mathcal{C}=\{(a,b):\ a\in\mathcal{C},\ b\in T^{L^2}_a\mathcal{C}\}\subseteq\mathcal{H}\times L^2$, with the subspace topology. Its elements are the *caloric (gauge) initial data sets*.

*Remarks.* (1) "Local caloric gauge" ($A_s=0$ along the heat flow) and "(global) caloric gauge" (Definition 37.3) are different conditions. The informal phrasing "the heat flow exists globally and $A(s)\to0$" omits $Q(a)<\infty$, which Oh–Tataru include in the definition. Uniqueness in Proposition 37.4 is only modulo constant gauge transformations; on $\mathcal{H}$ one may normalise $O(x)\to\mathrm{Id}$ as $x\to\infty$.

(2) For every $e\in L^2$ there is a unique decomposition $e=b-Da_0$ with $b\in T^{L^2}_a\mathcal{C}$, $a_0\in\dot H^1$ (a nonlinear div–curl decomposition), which links caloric data $(a,b)$ with gauge-covariant data $(a,e)$ satisfying the constraint $D^je_j=0$.
(3) Use: in [2021, 194(2), no. 1], $\mathbf{G}$ is noncommutative, the caloric solutions are curves $t\mapsto(A_x,\partial_tA_x)(t)\in T^{L^2}\mathcal{C}$, and the Threshold Theorem concerns data in $T^{L^2}\mathcal{C}$ (rough data) and in $T^{L^2}\mathcal{C}\cap\dot{\mathcal{H}}^N$, $\dot{\mathcal{H}}^N=\dot H^N\times\dot H^{N-1}$ (regular data); by Theorem 37.2(iv) and Proposition 37.4 every topologically trivial datum below $2E_{\mathrm{GS}}$ has a caloric representative.

## 38. Fully nonlinear complex Hessian-type equations on a compact Hermitian manifold

*Chapter context.* A chapter on fully nonlinear elliptic equations in a book on complex geometry and geometric PDE. The reader knows compact complex manifolds, Hermitian and Kähler metrics and their fundamental forms, real $(1,1)$-forms and the operator $i\partial\bar\partial$ in local holomorphic coordinates, plurisubharmonic functions, and elementary symmetric functions; Hessian-type equations defined through eigenvalues are introduced here.

Throughout, $X$ is a compact complex manifold without boundary, of complex dimension $n$, with a Hermitian metric whose fundamental form is written in local holomorphic coordinates as $\omega_X=i\,g_{\bar kj}\,dz^j\wedge d\bar z^k$, $(g_{\bar kj})$ positive definite Hermitian, $(g^{j\bar k})$ its inverse; summation over repeated indices.

**Definition 38.1 (eigenvalues relative to $\omega_X$).** Let $\alpha=i\,\alpha_{\bar kj}\,dz^j\wedge d\bar z^k$ be a real $(1,1)$-form (so $\overline{\alpha_{\bar kj}}=\alpha_{\bar jk}$). The *endomorphism of $\alpha$ relative to $\omega_X$* is the endomorphism $h=h[\alpha]$ of $T^{1,0}X$ with components $h^j{}_k=g^{j\bar m}\alpha_{\bar mk}$. It is self-adjoint for the Hermitian inner product $g$, so at each $x\in X$ it has $n$ real eigenvalues, the roots (with multiplicity) of $\det\big(\alpha_{\bar kj}(x)-\lambda\,g_{\bar kj}(x)\big)=0$. The *eigenvalue vector* $\lambda[\alpha](x)\in\mathbb{R}^n$ is this $n$-tuple, defined up to permutation. For a real function $\varphi\in C^2(X)$ and a smooth real $(1,1)$-form $\chi$ put
$$\chi_\varphi=\chi+i\partial\bar\partial\varphi,\qquad (\chi_\varphi)_{\bar kj}=\chi_{\bar kj}+\partial_j\partial_{\bar k}\varphi,\qquad h_\varphi=h[\chi_\varphi],\quad \lambda[h_\varphi]=\lambda[\chi_\varphi].$$

**Definition 38.2 (admissible cone and operator).** An *admissible pair* $(f,\Gamma)$ consists of:

(a) an open cone $\Gamma\subseteq\mathbb{R}^n$ with vertex at the origin ($r\lambda\in\Gamma$ for $\lambda\in\Gamma$, $r>0$), invariant under permutations of coordinates, with
$$\Gamma_n:=\{\lambda:\lambda_1>0,\dots,\lambda_n>0\}\subseteq\Gamma\subseteq\Gamma_1:=\{\lambda:\lambda_1+\dots+\lambda_n>0\};$$
(b) a $C^1$ function $f\colon\Gamma\to\mathbb{R}$, invariant under permutations of the components of $\lambda$, which is *elliptic*, $\partial f/\partial\lambda_j>0$ on $\Gamma$ for all $j$, and *homogeneous of degree one*, $f(r\lambda)=rf(\lambda)$ for $r>0$.
Because $f$ and $\Gamma$ are symmetric, "$\lambda[h]\in\Gamma$" and $F(h):=f(\lambda[h])$ are well defined for Hermitian endomorphisms $h$, and $F$ is $C^1$ on the open set where $\lambda[h]\in\Gamma$. The pair satisfies the *structural condition* with constant $\gamma>0$ if
$$\det\Big(\frac{\partial F}{\partial h_{ij}}(h)\Big)\ge\gamma\quad\text{whenever }\lambda[h]\in\Gamma,$$
equivalently (diagonalise $h$) $\prod_{j=1}^n\frac{\partial f}{\partial\lambda_j}(\lambda)\ge\gamma$ for all $\lambda\in\Gamma$.

**Definition 38.3 (the equation).** Let $(f,\Gamma)$ be admissible, $\chi$ a smooth real $(1,1)$-form on $X$, $F\colon X\to\mathbb{R}$ continuous and $c>0$ a constant. A *solution* of the complex Hessian-type equation
$$f\big(\lambda[h_\varphi]\big)=c\,e^{F},\qquad \sup_X\varphi=0,\qquad \lambda[h_\varphi]\in\Gamma\tag{H}$$
is a real function $\varphi\in C^2(X)$ such that, at every $x\in X$, $\lambda[\chi_\varphi](x)\in\Gamma$ (one says $\varphi$ is *$(\chi,\Gamma)$-admissible*) and $f(\lambda[\chi_\varphi](x))=c\,e^{F(x)}$, and such that $\max_X\varphi=0$. Here $h_\varphi$ is taken relative to $\omega_X$ (Definition 38.1), even when $\chi\neq\omega_X$. The right-hand side is normalised by $\int_Xe^{nF}\omega_X^n=\int_X\omega_X^n=:V$; for given data $(\chi,F)$ the constant $c$ is then part of the unknown, determined by $c^n=V^{-1}\int_Xf(\lambda[h_\varphi])^n\,\omega_X^n$.

**Examples 38.4.** (1) *Complex Monge–Ampère:* $\Gamma=\Gamma_n$, $f(\lambda)=(\lambda_1\cdots\lambda_n)^{1/n}$. Then $f(\lambda[h_\varphi])^n=\det h_\varphi=\chi_\varphi^n/\omega_X^n$, so (H) reads $\chi_\varphi^n=c^ne^{nF}\omega_X^n$ with $\chi_\varphi>0$; here $\prod_j\partial f/\partial\lambda_j=n^{-n}$. (2) *Complex $k$-Hessian:* $\Gamma=\Gamma_k=\{\sigma_1>0,\dots,\sigma_k>0\}$, $f=\sigma_k^{1/k}$, $1\le k\le n$, $\sigma_k$ the $k$-th elementary symmetric polynomial. (3) *Hessian quotients:* $f=(\sigma_k/\sigma_l)^{1/(k-l)}$ on $\Gamma_k$, $0\le l<k\le n$, and variants such as $(\sigma_k/\sigma_l)^{1/(k-l)}+c'\sigma_m^{1/m}$, $c'>0$.

*Remarks.* (1) Most of the literature (Caffarelli–Nirenberg–Spruck, and work on the complex case) additionally assumes $\Gamma$ convex and $f$ concave, $f>0$ in $\Gamma$, $f=0$ on $\partial\Gamma$; [2023, 198(1), no. 4] needs none of these, only Definition 38.2 and the structural condition. It also notes that homogeneity can be weakened to $\sum_j\lambda_j\,\partial f/\partial\lambda_j\le\Lambda f$.

(2) The equation is often written with $\chi+dd^c\varphi$, where $dd^c$ is a positive constant multiple of $i\partial\bar\partial$ (e.g. $\frac{i}{2\pi}\partial\bar\partial$ or $2i\partial\bar\partial$, depending on the normalisation of $d^c$); this only rescales $\varphi$ by a positive constant. The notation $\chi_\varphi$ for the background form plus $i\partial\bar\partial\varphi$ is written $\omega_\varphi$ when $\chi=\omega_X$.
(3) Use: in [2023, 198(1), no. 4], $X$ is compact *Kähler* and $\omega_X$ its Kähler form. Theorem 1 takes $\chi=\omega_X$, $c=1$; Theorem 2 takes $\chi=\omega_t=\chi_0+t\,\omega_X$, $t\in(0,1]$, with $\chi_0$ a closed nonnegative $(1,1)$-form, $F=F_t$, $c=c_t$, eigenvalues still relative to $\omega_X$. The estimates involve the entropy $\mathrm{Ent}_p(F)=V^{-1}\int_Xe^{nF}|F|^p\,\omega_X^n$, $V_t=\int_X\omega_t^n$, and the energy $E_t(\varphi)=V_t^{-1}\int_X(-\varphi)\,f(\lambda[h_{t,\varphi}])^n\,\omega_X^n$.

## 39. Hard sphere dynamics on the torus

*Chapter context.* The opening chapter on the microscopic model in a book on the kinetic theory of dilute gases (the derivation of the Boltzmann equation from particle systems). The reader knows the flat torus, Lebesgue measure on phase space, flows and invariant measures, and ordinary differential equations; the hard sphere flow is constructed here.

Throughout, $d\ge2$, $\mathbb{T}^d=\mathbb{R}^d/\mathbb{Z}^d$ with the quotient distance $|x-y|=\min\{|\tilde x-\tilde y|:\tilde x,\tilde y \text{ lifts}\}$, and $0<\varepsilon<\frac12$. For $x,y\in\mathbb{T}^d$ with $|x-y|<\frac12$, write $x\ominus y\in\mathbb{R}^d$ for the unique lift of $x-y$ of length $|x-y|$. For $N\ge1$ put $\mathbb{D}=\mathbb{T}^d\times\mathbb{R}^d$, $Z_N=(z_1,\dots,z_N)\in\mathbb{D}^N$ with $z_i=(x_i,v_i)$, $X_N=(x_1,\dots,x_N)$, $V_N=(v_1,\dots,v_N)$.

**Definition 39.1 (phase space, collisions, scattering).**

(a) The *phase space* of $N$ spheres of diameter $\varepsilon$ is the open set $\mathcal{D}^\varepsilon_N=\{Z_N\in\mathbb{D}^N:\ |x_i-x_j|>\varepsilon\ \text{for all } i\neq j\}$, with closure $\overline{\mathcal{D}^\varepsilon_N}$ (all $|x_i-x_j|\ge\varepsilon$).
(b) For $i\neq j$, a configuration $Z_N\in\overline{\mathcal{D}^\varepsilon_N}$ is a *binary collision of $(i,j)$* if $|x_i-x_j|=\varepsilon$ and $|x_k-x_l|>\varepsilon$ for every other pair $\{k,l\}\neq\{i,j\}$. Its *collision vector* is $\nu=(x_i\ominus x_j)/\varepsilon\in\mathbb{S}^{d-1}$, and the collision is *incoming* (pre-collisional), *outgoing* (post-collisional) or *grazing* according as $(v_i-v_j)\cdot\nu<0$, $>0$ or $=0$.
(c) The *scattering law* (specular reflection) replaces $(v_i,v_j)$ by
$$v_i'=v_i-\big((v_i-v_j)\cdot\nu\big)\,\nu,\qquad v_j'=v_j+\big((v_i-v_j)\cdot\nu\big)\,\nu,$$
leaving all other $z_k$ unchanged. It is an involution, conserves $v_i+v_j$ and $|v_i|^2+|v_j|^2$, and exchanges incoming and outgoing collisions.

**Definition 39.2 (hard sphere trajectory).** Let $Z_N^0\in\mathcal{D}^\varepsilon_N$. A *(forward) hard sphere trajectory* with initial datum $Z^0_N$ is a map $[0,\infty)\ni t\mapsto Z_N(t)=(X_N(t),V_N(t))\in\overline{\mathcal{D}^\varepsilon_N}$ together with a set $\mathcal{T}\subseteq(0,\infty)$ of *collision times* having only finitely many elements in each bounded interval, such that:

1. $Z_N(0)=Z^0_N$; $X_N$ is continuous; $V_N$ is right-continuous, with left limits $V_N(t^-)$;
2. on each maximal interval $I\subseteq[0,\infty)\setminus\mathcal{T}$, $V_N$ is constant and $\frac{d}{dt}X_N=V_N$ (free transport, $x_i(t)=x_i(s)+(t-s)v_i$ in $\mathbb{T}^d$), and $Z_N(t)\in\mathcal{D}^\varepsilon_N$;
3. at each $\tau\in\mathcal{T}$ there is a pair $(i,j)$ such that $(X_N(\tau),V_N(\tau^-))$ is an incoming binary collision of $(i,j)$, and $V_N(\tau)$ is obtained from $V_N(\tau^-)$ by the scattering law (so $Z_N(\tau)$ is outgoing).
Backward trajectories on $(-\infty,0]$ are defined symmetrically (time reversal $v\mapsto-v$). Since the first contact time of free transport is determined by the data, a trajectory, if it exists, is unique.

**Theorem 39.3 (Alexander).** There is a Lebesgue-null set $\mathcal{N}^\varepsilon_N\subseteq\mathcal{D}^\varepsilon_N$ such that every $Z^0_N\in\mathcal{G}^\varepsilon_N:=\mathcal{D}^\varepsilon_N\setminus\mathcal{N}^\varepsilon_N$ has a forward and a backward hard sphere trajectory, i.e. a trajectory on all of $\mathbb{R}$ with only binary, non-grazing collisions, finitely many in each bounded time interval. Setting $\mathbf{T}^\varepsilon_N(t)Z^0_N=Z_N(t)$, for each $t\in\mathbb{R}$ the map $\mathbf{T}^\varepsilon_N(t)$ is defined on $\mathcal{G}^\varepsilon_N$, takes values in $\mathcal{G}^\varepsilon_N$ outside a null set, preserves Lebesgue measure, and $\mathbf{T}^\varepsilon_N(t+s)=\mathbf{T}^\varepsilon_N(t)\mathbf{T}^\varepsilon_N(s)$ almost everywhere. (R. K. Alexander, *The infinite hard sphere system*, PhD thesis, Berkeley, 1975; see also Gallagher–Saint-Raymond–Texier, *From Newton to Boltzmann: hard spheres and short-range potentials*.)

**Definition 39.4 (hard sphere dynamics).** The *hard sphere dynamics* (hard sphere flow) of $N$ spheres of diameter $\varepsilon$ in $\mathbb{T}^d$ is the almost-everywhere defined measure-preserving flow $(\mathbf{T}^\varepsilon_N(t))_{t\in\mathbb{R}}$ on $\mathcal{D}^\varepsilon_N$ of Theorem 39.3. For a random initial configuration whose law on $\mathcal{D}^\varepsilon_N$ is absolutely continuous with respect to Lebesgue measure, the trajectory $t\mapsto\mathbf{T}^\varepsilon_N(t)Z^0_N$ is therefore defined with probability one. For a variable number of particles one uses the *grand canonical phase space* $\mathcal{D}^\varepsilon=\bigsqcup_{N\ge0}\mathcal{D}^\varepsilon_N$ (with $\mathcal{D}^\varepsilon_0$ a point, and $\mathcal{D}^\varepsilon_N=\emptyset$ for $N$ large), on which the flow acts componentwise; a density $W^{\varepsilon0}$ is transported as $W^\varepsilon(t)=W^{\varepsilon0}\circ\mathbf{T}^\varepsilon_N(-t)$, the weak form of the Liouville equation $\partial_tW+V_N\cdot\nabla_{X_N}W=0$ in $\mathcal{D}^\varepsilon_N$ with specular reflection on $\partial\mathcal{D}^\varepsilon_N$.

*Remarks.* (1) Grazing collisions could be included with trivial scattering ($v'=v$), but the flow is not continuous there; the null set $\mathcal{N}^\varepsilon_N$ also contains data leading to collisions of more than two spheres at once and to infinitely many collisions in finite time. The dynamics is invariant under relabelling of particles. (2) Some authors use a different torus side length, or $\mathbb{R}^d$ or a box with specular walls; the construction is the same. (3) Use: [2023, 198(3), no. 3] takes this dynamics with random initial data distributed by the grand canonical measure (1.1.6), in the Boltzmann–Grad scaling $\mu_\varepsilon=\varepsilon^{-(d-1)}$; the empirical measure $\pi^\varepsilon_t=\mu_\varepsilon^{-1}\sum_{i=1}^{\mathcal{N}}\delta_{\mathbf{z}^\varepsilon_i(t)}$ and the fluctuation field are built from $(\mathbf{z}^\varepsilon_i(t))_i=\mathbf{T}^\varepsilon_{\mathcal{N}}(t)\mathbf{Z}^{\varepsilon0}_{\mathcal{N}}$, where $\mathcal{N}$ is the (random) number of particles.

## 40. The Laplace–Beltrami operator on $L^2$ of a complete Riemannian manifold

*Chapter context.* A chapter on the $L^2$ theory of the Laplacian in a book on spectral geometry. The reader knows smooth Riemannian manifolds, the Riemannian volume measure, gradient, divergence and the smooth Laplace–Beltrami operator on $C^\infty(X)$, Green's formula, and unbounded operators on Hilbert spaces (closures, adjoints, self-adjointness, spectrum, the spectral theorem); the self-adjoint realisation of the Laplacian is constructed here.

Throughout, $(X,g)$ is a smooth Riemannian manifold without boundary, of dimension $m$, with Riemannian measure $\mathrm{vol}_g$; $L^2(X)=L^2(X,\mathrm{vol}_g;\mathbb{C})$ with $\langle u,w\rangle=\int_Xu\,\overline w\,d\mathrm{vol}_g$. In local coordinates, $\Delta u=-\operatorname{div}\operatorname{grad}u=-\frac{1}{\sqrt{\det g}}\,\partial_i\big(\sqrt{\det g}\,g^{ij}\partial_ju\big)$ (the *nonnegative* Laplacian).

**Definition 40.1 (the minimal operator).** Let $\Delta_0$ be the unbounded operator in $L^2(X)$ with domain $\mathcal{D}(\Delta_0)=C^\infty_c(X)$ and $\Delta_0u=\Delta u$. By Green's formula, for $u,w\in C^\infty_c(X)$,
$$\langle\Delta_0u,w\rangle=\int_Xg(\operatorname{grad}u,\overline{\operatorname{grad}w})\,d\mathrm{vol}_g=\langle u,\Delta_0w\rangle,\qquad\langle\Delta_0u,u\rangle=\|\operatorname{grad}u\|^2_{L^2}\ge0,$$
so $\Delta_0$ is densely defined, symmetric and nonnegative, hence closable. Its adjoint is the *maximal operator*: $\mathcal{D}(\Delta_0^*)=\{u\in L^2(X):\ \Delta u\in L^2(X)\}$, with $\Delta u$ taken in the sense of distributions, and $\Delta_0^*u=\Delta u$.

**Theorem 40.2 (Gaffney; Chernoff; Strichartz).** If $(X,g)$ is complete as a metric space, then $\Delta_0$ is essentially self-adjoint: its closure $\overline{\Delta_0}$ equals $\Delta_0^*$ and is the unique self-adjoint extension of $\Delta_0$. Moreover $\overline{\Delta_0}$ coincides with the operator associated with the closed nonnegative form $q(u)=\int_X|\operatorname{grad}u|^2\,d\mathrm{vol}_g$ on $H^1(X)=\{u\in L^2:\ \operatorname{grad}u\in L^2\}$ (for complete $X$, $C^\infty_c(X)$ is dense in $H^1(X)$). (See R. Strichartz, *Analysis of the Laplacian on the complete Riemannian manifold*, J. Funct. Anal. 1983.)

**Definition 40.3 (the $L^2$ Laplacian and its spectrum).** Let $(X,g)$ be complete. The *Laplace–Beltrami operator on $L^2(X)$* is the nonnegative self-adjoint operator
$$\Delta_X=\overline{\Delta_0}=\Delta_0^*,\qquad \mathcal{D}(\Delta_X)=\{u\in L^2(X):\ \Delta u\in L^2(X)\}.$$
Its spectrum $\operatorname{spec}(\Delta_X)=\sigma(\Delta_X)$ is a closed subset of $[0,\infty)$. For $\lambda\in\mathbb{R}$ the *multiplicity* of $\lambda$ is $\dim\ker(\Delta_X-\lambda)\in\{0,1,2,\dots,\infty\}$, and $\lambda$ is an *eigenvalue* if this is $\ge1$ (eigenfunctions are smooth, by elliptic regularity). The *discrete spectrum* $\sigma_{\mathrm d}(\Delta_X)$ is the set of isolated points of $\sigma(\Delta_X)$ that are eigenvalues of finite multiplicity, and the *essential spectrum* is $\sigma_{\mathrm{ess}}(\Delta_X)=\sigma(\Delta_X)\setminus\sigma_{\mathrm d}(\Delta_X)$. For $a>0$ with $\sigma(\Delta_X)\cap[0,a)\subseteq\sigma_{\mathrm d}(\Delta_X)$, the set $\sigma(\Delta_X)\cap[0,a)$ is finite or a sequence accumulating only at $a$, and "$\operatorname{spec}(\Delta_X)\cap[0,a)$ with multiplicities" means the multiset of these eigenvalues, each repeated according to its multiplicity.

**Proposition 40.4 (two standard cases).**

(i) If $X$ is compact (closed), $\Delta_X$ has compact resolvent, $\sigma(\Delta_X)=\sigma_{\mathrm d}(\Delta_X)$, and its eigenvalues, repeated with multiplicity, form a sequence $0=\lambda_0(X)\le\lambda_1(X)\le\lambda_2(X)\le\cdots\to\infty$; the multiplicity of $0$ is the number of connected components, so for connected $X$, $\lambda_1(X)>0$ is the first nonzero eigenvalue, and $\lambda_1(X)=\min\{\|\operatorname{grad}u\|^2/\|u\|^2:\ 0\ne u\in H^1(X),\ \int_Xu\,d\mathrm{vol}_g=0\}$.
(ii) If $X$ is a complete, finite-area, non-compact hyperbolic surface (constant curvature $-1$), then $\sigma_{\mathrm{ess}}(\Delta_X)=[\frac14,\infty)$, $\sigma(\Delta_X)\cap[0,\frac14)$ is a finite set of eigenvalues of finite multiplicity, $0$ is an eigenvalue (constants are in $L^2$) of multiplicity equal to the number of components, and the spectrum in $[\frac14,\infty)$ is absolutely continuous apart from embedded eigenvalues (Lax–Phillips; see also H. Iwaniec, *Spectral Methods of Automorphic Forms*).

*Remarks.* (1) Sign conventions: geometers' $\Delta=-\operatorname{div}\operatorname{grad}\ge0$ is used here and in the papers; if a library defines the smooth Laplace–Beltrami operator as $\operatorname{div}\circ\operatorname{grad}$, then $\Delta_X$ is the closure of its negative. (2) Without completeness, $\Delta_0$ may have many self-adjoint extensions (e.g. Dirichlet and Neumann Laplacians on a bounded domain); the Friedrichs extension is then the usual choice, and for complete $X$ all choices agree. Completeness of $X$ is needed, not compactness. (3) Use: [2023, 198(2), no. 6] takes $X$ complete, orientable, of constant curvature $-1$ and finite area, and its finite-degree Riemannian covers $X_n$ (again of finite area); Theorem 1.1 compares $\sigma(\Delta_{X_n})\cap[0,\frac14-\epsilon)$ and $\sigma(\Delta_X)\cap[0,\frac14-\epsilon)$ as multisets, which makes sense by Proposition 40.4(ii); Corollary 1.3 concerns $\lambda_1$ of closed connected hyperbolic surfaces, as in Proposition 40.4(i).

## 41. Quasiregular map between Riemannian manifolds

*Chapter context.* The opening chapter on quasiregular mappings in a book on geometric function theory on manifolds. The reader knows oriented Riemannian manifolds, their volume forms and measures, and the Sobolev class $W^{1,p}_{\mathrm{loc}}(M,N)$ of continuous maps with weak differential $Df$, operator norm $\lVert Df\rVert$ and Jacobian $J_f$ (Definition #47).

Throughout, $n\ge 2$ and $M$, $N$ are oriented Riemannian $n$-manifolds without boundary (not necessarily compact, complete or connected), with metrics $g_M,g_N$ and Riemannian volume forms $\mathrm{vol}_M,\mathrm{vol}_N$. The Euclidean space $\mathbb{R}^n$ and its open subsets carry the Euclidean metric and the standard orientation.

**Definition 41.1.** Let $f\colon M\to N$ be a map and $K\ge 1$ a real number.

(a) $f$ is **quasiregular with distortion constant $K$** if
  1. $f$ is continuous;
  2. $f\in W^{1,n}_{\mathrm{loc}}(M,N)$ (Definition #47, with $p=n$); and
  3. the *distortion inequality*
  $$\lVert Df(x)\rVert^{\,n}\le K\,J_f(x)$$
  holds for $\mathrm{vol}_M$-almost every $x\in M$. Here $\lVert Df(x)\rVert$ is the operator norm of the weak differential $Df(x)\colon T_xM\to T_{f(x)}N$ with respect to $g_M,g_N$, and $J_f(x)$ is its determinant with respect to the orientations and metrics, i.e. $(Df(x))^*\mathrm{vol}_N=J_f(x)\,\mathrm{vol}_M$.

(b) $f$ is **quasiregular** if it is quasiregular with distortion constant $K$ for some $K\in[1,\infty)$.

(c) The **outer distortion** of a quasiregular $f$ is $K_O(f):=\inf\{K\ge1: \lVert Df\rVert^n\le K J_f \text{ a.e.}\}$. The infimum is attained. With the convention $0/0:=0$, it equals $\max\{1,\operatorname*{ess\,sup}_x \lVert Df(x)\rVert^n/J_f(x)\}$.

*Remarks.*

(1) Elementary consequences. The inequality forces $J_f\ge 0$ a.e., so quasiregular maps preserve orientation in the measure-theoretic sense. It also gives $Df(x)=0$ for a.e. $x$ with $J_f(x)=0$, and $J_f\in L^1_{\mathrm{loc}}(M)$ because $0\le J_f\le\lVert Df\rVert^n$. Constant maps are quasiregular with every $K\ge 1$. Orientation-preserving conformal maps satisfy the inequality with $K=1$. An orientation-preserving smooth local diffeomorphism with $M$ compact is quasiregular. If $f$ satisfies the inequality with constant $K$, and $h\colon N\to N'$ is an orientation-preserving smooth local diffeomorphism with $\lVert Dh\rVert^n\le K'J_h$ everywhere, then $h\circ f$ satisfies it with $KK'$, by the chain rule $D(h\circ f)=Dh(f)\,Df$.
(2) Other conventions. In Rickman's monograph *Quasiregular Mappings* (Euclidean domains), the definition uses "$f$ continuous and ACL$^n$", which is equivalent to "continuous and $W^{1,n}_{\mathrm{loc}}$". Rickman's "$K$-quasiregular" means $\max\{K_O(f),K_I(f)\}\le K$, where the *inner distortion* $K_I(f)$ is the least $K'$ with $J_f(x)\le K'\,\ell(Df(x))^n$ a.e. and $\ell(L):=\min_{|v|=1}|Lv|$. Since $K_I\le K_O^{\,n-1}$ and $K_O\le K_I^{\,n-1}$, the class of quasiregular maps is the same; only the meaning of "$K$" differs. [2025, 201(2), no. 3] uses the outer form 41.1(a) ("satisfies (1.1) with constant $K$"). Some authors drop continuity and assume only $f\in W^{1,n}_{\mathrm{loc}}$. By Reshetnyak's theorem such a map has a continuous representative, but 41.1 requires $f$ itself to be continuous.
(3) Basic structure theorem (Reshetnyak): a non-constant quasiregular map between connected manifolds is open and discrete. It is not needed to state the definition.
(4) Dependence on the metrics. The constant $K$ depends on $g_M,g_N$. Replacing $g_N$ (or $g_M$) by a metric uniformly comparable to it preserves quasiregularity, with a different constant. Any two metrics on a compact manifold are comparable in this sense, so for compact $N$ the class of quasiregular maps $\mathbb{R}^n\to N$ depends only on the smooth structure and orientation of $N$. On $\mathbb{R}^n$ the Euclidean metric is always meant.
(5) In [2025, 201(2), no. 3], $M$ is $\mathbb{R}^n$ or the ball $B^n(0,2)$, $N$ is closed, connected and oriented, and one also uses $f^*\mathrm{vol}_N=J_f\,\mathrm{vol}_M$ as a locally finite measure.

## 42. Quasiregularly elliptic manifold

*Chapter context.* The chapter on value distribution and Picard-type theorems for quasiregular mappings into manifolds, in a book on geometric function theory. The reader knows oriented Riemannian manifolds and quasiregular maps between them (Definition #41, which builds on the Sobolev class of Definition #47).

The space $\mathbb{R}^n$ always carries the Euclidean metric and its standard orientation.

**Definition 42.1.** Let $n\ge 2$ and let $N$ be a connected, oriented Riemannian $n$-manifold without boundary.

(a) $N$ is **quasiregularly elliptic** if there exists a non-constant quasiregular map $f\colon\mathbb{R}^n\to N$ in the sense of Definition #41. Explicitly, $f$ is continuous, $f\in W^{1,n}_{\mathrm{loc}}(\mathbb{R}^n,N)$, $f$ is not constant, and there is $K\ge 1$ with $\lVert Df\rVert^n\le K\,J_f$ almost everywhere on $\mathbb{R}^n$.

(b) For $K\ge 1$, $N$ is **$K$-quasiregularly elliptic** if there is a non-constant quasiregular map $f\colon\mathbb{R}^n\to N$ satisfying the distortion inequality $\lVert Df\rVert^n\le K\,J_f$ a.e. with this constant $K$.

Thus $N$ is quasiregularly elliptic iff it is $K$-quasiregularly elliptic for some $K\ge1$. The theorem in [2025, 201(2), no. 3] concerns **closed** quasiregularly elliptic manifolds: $N$ is in addition compact (and without boundary).

*Remarks.*

(1) Independence of choices for closed $N$. Any two Riemannian metrics on a compact manifold are uniformly comparable. So for closed $N$, being quasiregularly elliptic depends only on the smooth manifold $N$ (the constant $K$ does depend on the metric). It does not depend on the orientation either: if $f\colon\mathbb{R}^n\to N$ is quasiregular and $r$ is a reflection of $\mathbb{R}^n$, then $f\circ r$ is quasiregular into $N$ with the opposite orientation, with the same $K$. For non-compact $N$ the property can depend on the metric, and a formaliser should keep the metric as data.
(2) Terminology. The term is used in exactly this sense by Bonk and Heinonen (Quasiregular mappings and cohomology, Acta Math. 2001), by Prywes, and in [2025, 201(2), no. 3]. The question of which closed simply connected manifolds are quasiregularly elliptic goes back to Gromov.
(3) Examples and constraints for closed $N$. The torus $T^n$ is quasiregularly elliptic: use the smooth covering map $\mathbb{R}^n\to T^n$ with a flat metric, where $K=1$. If $M$ is quasiregularly elliptic and $g\colon M\to N$ is a non-constant quasiregular map between closed connected manifolds, then $N$ is quasiregularly elliptic, because compositions of quasiregular maps are quasiregular and non-constant quasiregular maps are open. For example, an orientation-preserving piecewise linear branched covering $T^n\to N$, quasiregular with respect to the smooth structures, makes $N$ quasiregularly elliptic ([2025, 201(2), no. 3], Introduction and Appendix B). Conversely, Prywes's theorem gives, for closed quasiregularly elliptic $N$, $\dim H^k_{\mathrm{dR}}(N)\le\binom{n}{k}$, and [2025, 201(2), no. 3] strengthens this: $H^*_{\mathrm{dR}}(N)$ embeds as a graded algebra into $\bigwedge^*\mathbb{R}^n$. For example, $\#^4(S^2\times S^2)$ is not quasiregularly elliptic. For non-compact $N$ these cohomological bounds fail.
(4) For formalisation it is convenient to package (b) as a predicate $\mathrm{QRElliptic}(N,K)$, and (a) as $\exists K\ge1,\ \mathrm{QRElliptic}(N,K)$. "Non-constant" means $f$ is not a constant map; for continuous $f$ this is equivalent to $f$ not being a.e. equal to a constant.

## 43. SU(1,1) non-linear Fourier transform of an $L^2$ function on the half-line

*Chapter context.* The chapter on scattering for Dirac systems with square-integrable potential, in a book on non-linear Fourier analysis / spectral theory of canonical systems. The reader knows the real Dirac system, its fundamental matrix and Hermite–Biehler functions, and the scattering functions $a(t,z)$, $b(t,z)$ of a real potential $f\in L^1_{\mathrm{loc}}(\mathbb{R}_+)$ with their basic properties (Definition #44: $G=\begin{pmatrix}a^\#&b^\#\\ b&a\end{pmatrix}$ solves $\partial_tG=\begin{pmatrix}0&e^{-2izt}f\\ e^{2izt}f&0\end{pmatrix}G$, $G(0,z)=I$; and $|a|\ge1$, $|b|<|a|$ on $\overline{\mathbb{C}_+}$). Bounded holomorphic functions on $\mathbb{C}_+=\{\operatorname{Im}z>0\}$ and convergence in measure are also assumed.

Notation: $\Pi$ is the finite Borel measure $d\Pi(x)=dx/(1+x^2)$ on $\mathbb{R}$. Measurable functions $g_t$ *converge in measure with respect to $\Pi$* to $g$ as $t\to\infty$ if $\Pi(\{x:|g_t(x)-g(x)|>\varepsilon\})\to0$ for every $\varepsilon>0$. The limit is unique up to $\Pi$-null sets, which are exactly the Lebesgue-null sets. Since $\Pi$ is finite and has a density bounded above and below on bounded intervals, this is the same as convergence in Lebesgue measure on every bounded interval. Note that $L^2(\mathbb{R}_+)\subset L^1_{\mathrm{loc}}(\mathbb{R}_+)$, by Cauchy–Schwarz on each $[0,T]$.

**Proposition 43.1 (existence of the scattering limit).** Let $f\in L^2(\mathbb{R}_+)$ be real, with scattering functions $a,b$ (Definition #44). Then, as $t\to\infty$:

1. $a(t,\cdot)$ and $b(t,\cdot)$ converge uniformly on compact subsets of $\mathbb{C}_+$ to holomorphic functions $a(\infty,\cdot)$, $b(\infty,\cdot)$ on $\mathbb{C}_+$; there $|a(\infty,z)|\ge1$ and $|b(\infty,z)|\le|a(\infty,z)|$.
2. The restrictions $a(t,\cdot)|_{\mathbb{R}}$ and $b(t,\cdot)|_{\mathbb{R}}$ converge in measure with respect to $\Pi$ to measurable functions $a(\infty,\cdot)$, $b(\infty,\cdot)\colon\mathbb{R}\to\mathbb{C}$ (defined a.e.), and $|a(\infty,x)|^2-|b(\infty,x)|^2=1$ for a.e. $x\in\mathbb{R}$.

*(See [2024, 199(2), no. 4], §5. Part 1 is due to Denisov, in the equivalent language of Krein systems: Continuous analogs of polynomials orthogonal on the unit circle and Krein systems, IMRS 2006. Part 2 is deduced in the paper from part 1 using the Smirnov-class structure of $a$, $b$. The inequalities pass to the limit from Definition #44; on $\mathbb{R}$ use an a.e.-convergent subsequence.)*

**Definition 43.2 (non-linear Fourier transform).** Let $f\in L^2(\mathbb{R}_+)$ be real.

(a) The **non-linear Fourier transform** of $f$ consists of two functions, both written $\overset{\curlywedge}{f}$:
$$\overset{\curlywedge}{f}(z):=\frac{b(\infty,z)}{a(\infty,z)}\quad(z\in\mathbb{C}_+),\qquad \overset{\curlywedge}{f}(x):=\frac{b(\infty,x)}{a(\infty,x)}\quad(\text{a.e. }x\in\mathbb{R}),$$
with the limits of Proposition 43.1. The first is a holomorphic function on $\mathbb{C}_+$ with $|\overset{\curlywedge}{f}|\le1$. The second is a measurable function on $\mathbb{R}$ defined up to null sets, with $|\overset{\curlywedge}{f}(x)|^2=1-|a(\infty,x)|^{-2}<1$ a.e. The denominators satisfy $|a(\infty,\cdot)|\ge1$.

(b) For $T>0$ let $f_T:=f\cdot 1_{(0,T)}$. Its scattering functions are constant in $t$ for $t\ge T$ (Definition #44, Remarks). Hence the limits are attained, and for **every** $z\in\overline{\mathbb{C}_+}=\mathbb{C}_+\cup\mathbb{R}$
$$\overset{\curlywedge}{f}_T(z)=\frac{b(T,z)}{a(T,z)},$$
where $a,b$ are the scattering functions of $f$ itself. This is a function holomorphic near $\overline{\mathbb{C}_+}$ and defined at every real point. The same formula defines $\overset{\curlywedge}{f}$ for any real $f\in L^1_{\mathrm{loc}}$ supported in $[0,T]$.

*Remarks.*

(1) Equivalent definition on $\mathbb{R}$, convenient for formalisation: $\overset{\curlywedge}{f}|_{\mathbb{R}}$ is the limit in $\Pi$-measure of the functions $x\mapsto b(T,x)/a(T,x)$ as $T\to\infty$. This follows from 43.1(2), because $|a(T,x)|\ge 1$ and $(a,b)\mapsto b/a$ is uniformly continuous on bounded subsets of $\{|a|\ge1\}$. Theorem 1 of [2024, 199(2), no. 4] says that for every real $f\in L^2(\mathbb{R}_+)$ this convergence holds pointwise: $\overset{\curlywedge}{f}_T(s)\to\overset{\curlywedge}{f}(s)$ for a.e. $s\in\mathbb{R}$. So the statement only needs (a) on $\mathbb{R}$ and (b) on $\mathbb{R}$.
(2) Compatibility. The paper's discussion in §5 treats $\overset{\curlywedge}{f}|_{\mathbb{R}}$ as the a.e. (non-tangential) boundary function of the bounded holomorphic function $\overset{\curlywedge}{f}|_{\mathbb{C}_+}$, and likewise for $a(\infty,\cdot)$, which is outer in $\mathbb{C}_+$. With that identification $(a,b)$ is recovered from $\overset{\curlywedge}{f}$: $a(\infty,\cdot)$ is the outer function with $|a|=(1-|\overset{\curlywedge}{f}|^2)^{-1/2}$ on $\mathbb{R}$, and $b=a\overset{\curlywedge}{f}$. A formaliser may prefer to define $\overset{\curlywedge}{f}|_{\mathbb{R}}$ as these boundary values (which exist a.e. by Fatou's theorem), but must then prove agreement with Definition 43.2(a).
(3) Why "SU(1,1)". For real $x$ the matrix $G(t,x)=\begin{pmatrix}\overline{a}&\overline{b}\\ b&a\end{pmatrix}$ lies in $SU(1,1)$. The scattering matrix $G(\infty,\cdot)$ (written with an overbrace in the paper) is the continuous half-line analogue of the SU(1,1) non-linear Fourier transform of Tao–Thiele. The paper works with the quotient $b/a$, which determines $G(\infty,\cdot)$ by Remark (2). For small $f$, $b(\infty,x)\approx\int_0^\infty f(s)e^{2ixs}\,ds$, a rescaled linear Fourier transform.
(4) Conventions differ between sources: Tao–Thiele's $a$ is $a^\#$ here, and the exponent $e^{2izt}$ versus $e^{izt}$ rescales the variable. [2024, 199(2), no. 4] uses only real $f$, with the normalisations above.

## 44. Scattering functions of a real Dirac system

*Chapter context.* A chapter on Dirac systems and their scattering data in a book on spectral theory of canonical systems / non-linear Fourier analysis. The reader knows Lebesgue integration, (locally) absolutely continuous functions, entire functions and the Hardy space of the upper half-plane. The theory of linear ODEs with merely integrable coefficients is recalled here (Proposition 44.1).

Notation: $\mathbb{R}_+=[0,\infty)$; $L^1_{\mathrm{loc}}(\mathbb{R}_+)$ is the space of measurable $f\colon\mathbb{R}_+\to\mathbb{R}$ (real-valued throughout) with $\int_0^T|f|<\infty$ for every $T<\infty$; $\mathbb{C}_+=\{z:\operatorname{Im}z>0\}$. For an entire function $H$, its Schwarz reflection is $H^\#(z):=\overline{H(\bar z)}$. We write
$$\Omega=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad Q(t)=\begin{pmatrix}0&f(t)\\ f(t)&0\end{pmatrix}.$$

**Proposition 44.1 (Carathéodory solutions).** Let $P\colon\mathbb{R}_+\times\mathbb{C}\to\mathbb{C}^{d\times d}$ be such that $t\mapsto P(t,z)$ is measurable for each $z$, $z\mapsto P(t,z)$ is entire for a.e. $t$, and for each compact $K\subset\mathbb{C}$ there is $p_K\in L^1_{\mathrm{loc}}(\mathbb{R}_+)$ with $\lVert P(t,z)\rVert\le p_K(t)$ for a.e. $t$ and all $z\in K$. Then for every $z$ there is a unique continuous $Y(\cdot,z)\colon\mathbb{R}_+\to\mathbb{C}^{d\times d}$ with
$$Y(t,z)=I+\int_0^t P(s,z)\,Y(s,z)\,ds\qquad(t\ge 0).$$
It is locally absolutely continuous in $t$, with $\partial_tY=PY$ a.e. Moreover $z\mapsto Y(t,z)$ is entire for each $t$, and $\lVert Y(t,z)\rVert\le\exp\int_0^tp_K$ for $z\in K$. *(Picard iteration converges uniformly on $[0,T]\times K$; Gronwall gives uniqueness.)*

**Definition 44.2 (real Dirac system).** For real $f\in L^1_{\mathrm{loc}}(\mathbb{R}_+)$ and $z\in\mathbb{C}$, the *real Dirac system with potential $f$* is
$$\Omega\,\dot X(t)=z\,X(t)-Q(t)\,X(t),\qquad X\colon\mathbb{R}_+\to\mathbb{C}^2 ,$$
equivalently $\dot X=\begin{pmatrix} f&-z\\ z&-f\end{pmatrix}X$ a.e., with $X$ locally absolutely continuous. Its **fundamental (transfer) matrix** $M(t,z)=\begin{pmatrix}A&B\\ C&D\end{pmatrix}(t,z)$ is the solution of this system with $M(0,z)=I$ (Proposition 44.1). Its columns are the solutions with Neumann data $(1,0)^T$ and Dirichlet data $(0,1)^T$. The **Hermite–Biehler functions** of the system are
$$E(t,z)=A(t,z)-iC(t,z),\qquad \tilde E(t,z)=B(t,z)-iD(t,z).$$

**Definition 44.3 (scattering functions).** Let $f\in L^1_{\mathrm{loc}}(\mathbb{R}_+)$ be real. Let $G(t,z)\in\mathbb{C}^{2\times 2}$ ($t\ge0$, $z\in\mathbb{C}$) be the solution, given by Proposition 44.1, of
$$\partial_t G(t,z)=\begin{pmatrix}0&e^{-2izt}f(t)\\ e^{2izt}f(t)&0\end{pmatrix}G(t,z),\qquad G(0,z)=I .$$
The **scattering functions** of $f$ are
$$a(t,z):=G_{22}(t,z),\qquad b(t,z):=G_{21}(t,z)\qquad(t\ge 0,\ z\in\mathbb{C}).$$
For each $t$, these are entire functions of $z$. The **scattering functions in the Hermite–Biehler normalisation** are $\mathcal{E}(t,z)=e^{itz}E(t,z)$ and $\tilde{\mathcal{E}}(t,z)=e^{itz}\tilde E(t,z)$.

**Proposition 44.4.** For real $f\in L^1_{\mathrm{loc}}(\mathbb{R}_+)$ and all $t\ge0$, $z\in\mathbb{C}$:

1. $A,B,C,D$ are real entire functions ($H^\#=H$), $\det M\equiv 1$, $\partial_tE=-izE+fE^\#$ with $E(0,\cdot)=1$, and $\partial_t\tilde E=-iz\tilde E+f\tilde E^\#$ with $\tilde E(0,\cdot)=-i$.
2. $a(t,z)=\tfrac12 e^{itz}\big(E(t,z)+i\tilde E(t,z)\big)$ and $b(t,z)=\tfrac12 e^{itz}\big(E(t,z)-i\tilde E(t,z)\big)$.
3. $G=\begin{pmatrix}a^\#&b^\#\\ b&a\end{pmatrix}$ and $\det G=a\,a^\#-b\,b^\#\equiv1$. Hence for real $x$, $G(t,x)=\begin{pmatrix}\overline{a}&\overline{b}\\ b&a\end{pmatrix}\in SU(1,1)$ and $|a(t,x)|^2-|b(t,x)|^2=1$.
4. Integral equations: $a(t,z)=1+\int_0^t f(s)e^{2izs}b^\#(s,z)\,ds$ and $b^\#(t,z)=\int_0^t f(s)e^{-2izs}a(s,z)\,ds$.
5. For $\operatorname{Im}z\ge0$: $|a(t,z)|\ge 1$ and $|b(t,z)|<|a(t,z)|$. So $b(t,\cdot)/a(t,\cdot)$ is holomorphic on a neighbourhood of $\overline{\mathbb{C}_+}$ and bounded by $1$ there.
6. Free case $f\equiv0$: $E=e^{-itz}$, $\tilde E=-ie^{-itz}$, $a\equiv1$, $b\equiv0$.

*(Items 1–4 are direct computations from the equations, as in [2024, 199(2), no. 4], §§2 and 5. For 3: $\overline{G(t,\bar z)}$ solves the system with the off-diagonal coefficients interchanged. For 5, write $y=\operatorname{Im}z\ge0$. With $\beta(s)=e^{2izs}b^\#(s,z)$ one gets $\partial_s(|a|^2-|\beta|^2)=4y|\beta|^2\ge0$, hence $|a|^2\ge1$. With $J=\operatorname{diag}(1,-1)$ and $\Psi(s)=G(t,z)G(s,z)^{-1}\operatorname{diag}(e^{-izs},e^{izs})$ one gets $\partial_s(\Psi J\Psi^*)=2y\Psi\Psi^*\ge0$; comparing $s=0$ with $s=t$ gives $|a(t,z)|^2-|b(t,z)|^2\ge e^{-2yt}$.)*

*Remarks.*

(1) The primary object for formalisation is the pair of functions $a,b\colon\mathbb{R}_+\times\mathbb{C}\to\mathbb{C}$ of Definition 44.3. The route through $M$, $E$, $\tilde E$ (Proposition 44.4(2)) is equivalent; it is the one taken in the paper, which defines $a,b$ by formula (5.2) and derives the $G$-equation (5.3).
(2) Convention warning: in Tao–Thiele (Nonlinear Fourier Analysis, lecture notes) the letter $a$ denotes what is here $a^\#$. Other sources use $e^{\pm izt}$ instead of $e^{\pm2izt}$, which rescales $z$ by $2$. The Dirac system is sometimes written with a complex potential $f+ig$, with $\pm g$ on the diagonal of $Q$; [2024, 199(2), no. 4] uses real $f$ only.
(3) The paper calls $E(t,\cdot)$ and $\tilde E(t,\cdot)$ Hermite–Biehler: $|E(t,z)|>|E(t,\bar z)|$ for $z\in\mathbb{C}_+$ and $t>0$, and both have exponential type $t$ (Krein's formula). These facts are not needed to define $a,b$.
(4) If $f$ vanishes on $(T,\infty)$, then $G(t,z)=G(T,z)$ for all $t\ge T$. In particular, for $f_T=f\cdot 1_{(0,T)}$ the scattering functions of $f_T$ at any time $t\ge T$ equal those of $f$ at time $T$.

## 45. Schrödinger operator $-\Delta+V$ on $L^2(\mathbb{R}^d)$

*Chapter context.* The first chapter on Schrödinger operators in a book on spectral theory and mathematical physics. The reader knows unbounded operators on Hilbert spaces (domains, closedness, adjoints, self-adjointness, spectrum, resolvent), the spectral theorem with spectral measures and the decomposition into absolutely continuous, singular continuous and pure point parts, the Fourier–Plancherel transform on $L^2(\mathbb{R}^d)$, and distributions.

Conventions: $d\ge1$. $L^2(\mathbb{R}^d)$ is the complex Hilbert space of (classes of) square-integrable functions for Lebesgue measure. $\mathcal{F}$ is the unitary Fourier transform, $(\mathcal{F}u)(\xi)=(2\pi)^{-d/2}\int e^{-i\langle x,\xi\rangle}u(x)\,dx$ on $L^1\cap L^2$, extended by continuity. $\Delta=\sum_{j=1}^d\partial_j^2$, and $-\Delta$ is the non-negative Laplacian; no factors $\tfrac12$ or $\hbar$ appear.

**Definition 45.1.** The Sobolev space $H^2(\mathbb{R}^d)$ is
$$H^2(\mathbb{R}^d)=\{u\in L^2(\mathbb{R}^d):\ (1+|\xi|^2)\,\mathcal{F}u\in L^2(\mathbb{R}^d)\},\qquad \lVert u\rVert_{H^2}=\lVert(1+|\xi|^2)\mathcal{F}u\rVert_{L^2}.$$
Equivalently, $H^2$ consists of the $u\in L^2$ whose distributional derivatives $\partial^\alpha u$ with $|\alpha|\le2$ all lie in $L^2$. Equivalently again, it consists of the $u\in L^2$ with distributional Laplacian $\Delta u\in L^2$. All three descriptions give the same space with equivalent norms. It is the Bessel potential space of order $2$.

**Proposition 45.2 (free Laplacian).** The operator $H_0$ with domain $D(H_0)=H^2(\mathbb{R}^d)$ and
$$H_0u:=-\Delta u=\mathcal{F}^{-1}\big(|\xi|^2\,\mathcal{F}u\big)$$
(the distributional Laplacian, which lies in $L^2$) is self-adjoint and non-negative, with spectrum $\sigma(H_0)=[0,\infty)$. It is unitarily equivalent via $\mathcal{F}$ to multiplication by $|\xi|^2$ on its maximal domain, and $C_c^\infty(\mathbb{R}^d)$ is a core for it.

**Proposition 45.3 (bounded perturbations).** If $A$ is self-adjoint on a Hilbert space and $B$ is bounded, everywhere defined and self-adjoint, then $A+B$ with domain $D(A)$ is self-adjoint, and $\inf\sigma(A+B)\ge\inf\sigma(A)-\lVert B\rVert$. *(Because $(A+B)^*=A^*+B$ for bounded $B$. This is also the case of relative bound $0$ in the Kato–Rellich theorem.)*

**Definition 45.4 (Schrödinger operator).** Let $V\colon\mathbb{R}^d\to\mathbb{R}$ be measurable, real-valued and essentially bounded, i.e. $V\in L^\infty(\mathbb{R}^d;\mathbb{R})$. Multiplication by $V$ is then a bounded self-adjoint operator on $L^2(\mathbb{R}^d)$ of norm $\lVert V\rVert_\infty$. The **Schrödinger operator with potential $V$** is the linear operator $H=-\Delta+V$ on $L^2(\mathbb{R}^d)$ with
$$D(H)=H^2(\mathbb{R}^d),\qquad Hu=-\Delta u+V\,u\quad(u\in H^2(\mathbb{R}^d)).$$
By Propositions 45.2 and 45.3, $H$ is self-adjoint and bounded below: $H\ge\operatorname*{ess\,inf}V$, so $\sigma(H)\subset[\operatorname*{ess\,inf}V,\infty)$. It is essentially self-adjoint on $C_c^\infty(\mathbb{R}^d)$ and on the Schwartz space, so it is the closure of the differential expression $-\Delta+V$ on either space. It depends only on the a.e.-class of $V$.

*Quasi-periodic case (the case of [2026, 203(2), no. 1]).* Fix $l\in\mathbb{N}$ and *basic frequencies* $\boldsymbol\omega_1,\dots,\boldsymbol\omega_l\in\mathbb{R}^d$, with $\vec{\boldsymbol\omega}=(\boldsymbol\omega_1,\dots,\boldsymbol\omega_l)$. For $\mathbf{n}\in\mathbb{Z}^l$ put $\mathbf{n}\vec{\boldsymbol\omega}=\sum_j n_j\boldsymbol\omega_j\in\mathbb{R}^d$ and $|\mathbf{n}|=\max_j|n_j|$. Fix $Q\in\mathbb{N}$ and complex numbers $V_{\mathbf{n}}$ for $|\mathbf{n}|<Q$ with $V_{-\mathbf{n}}=\overline{V_{\mathbf{n}}}$. The quasi-periodic potential
$$V(\mathbf{x})=\sum_{|\mathbf{n}|<Q}V_{\mathbf{n}}\,e^{i\langle\mathbf{n}\vec{\boldsymbol\omega},\mathbf{x}\rangle}$$
is real-valued, smooth and bounded by $\sum|V_{\mathbf{n}}|$, so Definition 45.4 applies.

*Remarks.*

(1) The a.c. spectrum. Theorem 1.1 of [2026, 203(2), no. 1] concerns $\sigma_{\mathrm{ac}}(H)$. This is the spectrum of the restriction of $H$ to the closed reducing subspace $\mathcal{H}_{\mathrm{ac}}=\{\psi:\ \mu_\psi\ll\text{Lebesgue}\}$, where $\mu_\psi(B)=\langle 1_B(H)\psi,\psi\rangle$ is the spectral measure of $\psi$. The theorem asserts $[\lambda_*,\infty)\subset\sigma_{\mathrm{ac}}(H)$. This is spectral-theory material from an earlier chapter, applied to the operator of 45.4.
(2) In the paper, $d\ge2$ and $l>d$, $\vec{\boldsymbol\omega}\in[-1/2,1/2]^{dl}$, and the frequencies are (generically) rationally independent; "for a.e. $\vec{\boldsymbol\omega}$" refers to Lebesgue measure on $[-1/2,1/2]^{dl}$. The paper's display (1.3) writes $|\mathbf{n}|\le Q$, while (1.4) and Theorem 1.1 use $|\mathbf{n}|<Q$. The choice is immaterial: it only renames $Q$.
(3) Generalisations, not needed here. Real $V\in L^2+L^\infty$ for $d\le3$, or more generally $-\Delta$-bounded with relative bound $<1$, still gives a self-adjoint operator on $H^2$ by Kato–Rellich. Potentials that are merely bounded below need the form method (Friedrichs extension), and the domain is then in general not $H^2$. Complex $V$ gives non-self-adjoint operators.
(4) For formalisation: $H$ can be built as a densely defined linear map (a `LinearPMap`) with domain $H^2$, as the sum of the self-adjoint Fourier multiplier $|\xi|^2$ and a bounded multiplication operator, and self-adjointness then follows from 45.3.

## 46. Schur multiplier on Schatten classes

*Chapter context.* A chapter on Schur multipliers in a book on operator ideals / non-commutative harmonic analysis. The reader knows bounded operators on Hilbert spaces and the Schatten classes. For $1\le p<\infty$, $S_p(H)$ is the space of compact $A$ with $\lVert A\rVert_p=(\operatorname{tr}|A|^p)^{1/p}<\infty$; $S_\infty(H)$ is the space of compact operators with the operator norm. The reader also knows that $S_p\subset S_q$ contractively for $p\le q$, that finite-rank operators are dense in every $S_p$, and the Hilbert–Schmidt class $S_2$. The kernel description of $S_2(L^2)$ and Schur multipliers are introduced here.

Throughout, $(\Omega,\mu)$ is a $\sigma$-finite measure space; the case needed is $\Omega=\mathbb{R}^n$ with Lebesgue measure. We write $S_p(\Omega):=S_p(L^2(\Omega,\mu))$ and $S_p(\mathbb{R}^n)$ for $S_p(L^2(\mathbb{R}^n))$.

**Proposition 46.1 (Hilbert–Schmidt kernels).** For $k\in L^2(\Omega\times\Omega,\mu\otimes\mu)$, the formula
$$(T_kg)(x)=\int_\Omega k(x,y)\,g(y)\,d\mu(y)\qquad(g\in L^2(\Omega))$$
(the integral converges absolutely for a.e. $x$) defines $T_k\in S_2(\Omega)$ with $\lVert T_k\rVert_2=\lVert k\rVert_{L^2(\Omega\times\Omega)}$. The map $k\mapsto T_k$ is a unitary isomorphism $L^2(\Omega\times\Omega)\to S_2(\Omega)$. For $A\in S_2(\Omega)$, its *kernel* or *matrix* $(A_{xy})=k_A$ is the unique element of $L^2(\Omega\times\Omega)$, up to null sets, with $A=T_{k_A}$.

**Definition 46.2 (Schur multiplier).** Let $M\colon\Omega\times\Omega\to\mathbb{C}$ be measurable and essentially bounded, i.e. $M\in L^\infty(\Omega\times\Omega)$; call $M$ the *symbol*. The **Schur multiplier** with symbol $M$ is the linear map
$$S_M\colon S_2(\Omega)\to S_2(\Omega),\qquad S_M(A):=T_{M\cdot k_A},\quad\text{i.e. } \big(S_M(A)\big)_{xy}=M(x,y)A_{xy}.$$
It is bounded with $\lVert S_M\colon S_2\to S_2\rVert=\lVert M\rVert_{L^\infty}$, because via Proposition 46.1 it is multiplication by $M$ on $L^2(\Omega\times\Omega)$. It depends only on the a.e.-class of $M$.

**Definition 46.3 ($S_p$-norm of a Schur multiplier).** Let $M\in L^\infty(\Omega\times\Omega)$ and $1\le p\le\infty$. Set
$$\big\lVert S_M\colon S_p(\Omega)\to S_p(\Omega)\big\rVert:=\sup\big\{\lVert S_M(A)\rVert_p:\ A\in S_2(\Omega)\cap S_p(\Omega),\ \lVert A\rVert_p\le1\big\}\in[0,\infty],$$
with the convention $\lVert B\rVert_p=\infty$ if $B\notin S_p$. Note that $S_2\cap S_p=S_p$ for $p\le2$, and $S_2\cap S_p=S_2$ for $p\ge2$. $S_M$ is **bounded on $S_p$** if this number is finite. Then $S_M|_{S_2\cap S_p}$ extends uniquely, by density of $S_2\cap S_p$ in $S_p$, to a bounded operator $S_p(\Omega)\to S_p(\Omega)$ with this norm. The extension is again denoted $S_M$.

The **completely bounded norm** is $\lVert S_M\rVert_{cb}:=\sup_{m\ge1}\lVert \mathrm{id}_{M_m}\otimes S_M\rVert$, where $\mathrm{id}_{M_m}\otimes S_M$ acts on $S_p(\ell^2_m\otimes L^2(\Omega))$, identified with $m\times m$ matrices $(A_{ij})$ of operators on $L^2(\Omega)$, by $(A_{ij})\mapsto(S_M(A_{ij}))$. Equivalently, it is the norm of the Schur multiplier on $\{1,\dots,m\}\times\Omega$ (counting measure times $\mu$) with symbol $((i,x),(j,y))\mapsto M(x,y)$.

*Remarks.*

(1) This is exactly the convention of [2023, 198(3), no. 5], §1.1: "$S_M$ is bounded on $S_p$ when its restriction to $S_2\cap S_p$ extends to a bounded map". The paper's Theorem A uses $\Omega=\mathbb{R}^n$ with Lebesgue measure, $1<p<\infty$, and the plain norm of 46.3.
(2) Symbols in Theorem A. There $M\in C^{[n/2]+1}(\mathbb{R}^{2n}\setminus\{x=y\})$; the diagonal is a null set, so $M$ determines an a.e.-class. The $\gamma=0$ term of $|||M|||_{\mathrm{HMS}}$ is $2\sup_{x\ne y}|M(x,y)|$, so $|||M|||_{\mathrm{HMS}}<\infty$ forces $M\in L^\infty$, and Definitions 46.2–46.3 apply. When $|||M|||_{\mathrm{HMS}}=\infty$ the inequality is vacuous. A formaliser can therefore state Theorem A under the hypothesis $|||M|||_{\mathrm{HMS}}<\infty$.
(3) Standard facts. For $1\le p\le\infty$ and conjugate exponent $p'$: $\lVert S_M\rVert_{S_p\to S_p}=\lVert S_M\rVert_{S_{p'}\to S_{p'}}$, by trace duality and the transpose symbol $M^t(x,y)=M(y,x)$. Interpolation then gives $\lVert M\rVert_\infty=\lVert S_M\rVert_{S_2\to S_2}\le\lVert S_M\rVert_{S_p\to S_p}$. If $\mu$ has no atoms, $\lVert S_M\rVert_{cb}=\lVert S_M\rVert$; if $\Omega$ is locally compact, $\mu$ is a $\sigma$-finite Radon measure and $M$ is continuous, the norm is the supremum of the norms of the restrictions $M|_{\Sigma\times\Sigma}$ over finite subsets $\Sigma$ of the support of $\mu$, as matrix Schur multipliers. Both facts are due to Lafforgue–de la Salle (Duke Math. J. 160 (2011)), as quoted in the paper.
(4) Special cases. For finite $\Omega$ with counting measure, $S_M(A)=(M(j,k)A_{jk})$ is the entrywise (Hadamard) product of matrices. For Toeplitz symbols $M(x,y)=m(x-y)$ one gets Herz–Schur multipliers, related to Fourier multipliers $T_m$ on $L^p(\mathbb{R}^n)$ by transference.
(5) Do not confuse this with the group-cohomological Schur multiplier $H^2(G,k^\times)$.

## 47. Sobolev space $W^{1,p}_{\mathrm{loc}}(M,N)$ of maps between Riemannian manifolds

*Chapter context.* A chapter on Sobolev maps in a book on quasiregular mappings / geometric function theory on manifolds. The reader knows smooth manifolds, charts, orientations, Riemannian metrics and their volume forms and measures, null sets on manifolds, and the Euclidean theory: for an open $\Omega\subset\mathbb{R}^m$ and $1\le p\le\infty$, the space $W^{1,p}_{\mathrm{loc}}(\Omega)$ of real functions $u\in L^p_{\mathrm{loc}}(\Omega)$ whose distributional partial derivatives $\partial_j u$ lie in $L^p_{\mathrm{loc}}(\Omega)$. For $u=(u^1,\dots,u^k)$ we write $u\in W^{1,p}_{\mathrm{loc}}(\Omega;\mathbb{R}^k)$ if every $u^i\in W^{1,p}_{\mathrm{loc}}(\Omega)$, and $Du(y)=(\partial_j u^i(y))_{i,j}\in\mathbb{R}^{k\times m}$ (defined for a.e. $y$) is its weak Jacobian matrix.

Throughout, $M$ and $N$ are smooth manifolds (without boundary, Hausdorff, second countable) of dimensions $m$ and $k$, and $1\le p\le\infty$. "Almost everywhere" on a manifold refers to the null sets of $M$ (sets whose image under every chart is Lebesgue-null), which are exactly the null sets of the Riemannian volume measure of any Riemannian metric.

**Proposition 47.1 (chain rules).** Let $\Omega,\Omega'\subset\mathbb{R}^m$ be open.

(a) If $\theta\colon\Omega'\to\Omega$ is a $C^\infty$ diffeomorphism and $u\in W^{1,p}_{\mathrm{loc}}(\Omega;\mathbb{R}^k)$, then $u\circ\theta\in W^{1,p}_{\mathrm{loc}}(\Omega';\mathbb{R}^k)$ and $D(u\circ\theta)(y)=Du(\theta(y))\,D\theta(y)$ for a.e. $y\in\Omega'$.

(b) If $u\in W^{1,p}_{\mathrm{loc}}(\Omega;\mathbb{R}^k)$ is continuous with $u(\Omega)\subset W$, $W\subset\mathbb{R}^k$ open, and $F\colon W\to\mathbb{R}^l$ is $C^1$, then $F\circ u\in W^{1,p}_{\mathrm{loc}}(\Omega;\mathbb{R}^l)$ and $D(F\circ u)(y)=DF(u(y))\,Du(y)$ for a.e. $y$.

(c) Membership in $W^{1,p}_{\mathrm{loc}}$ is local: if $\Omega=\bigcup_i\Omega_i$ with $\Omega_i$ open and $u|_{\Omega_i}\in W^{1,p}_{\mathrm{loc}}(\Omega_i;\mathbb{R}^k)$ for all $i$, then $u\in W^{1,p}_{\mathrm{loc}}(\Omega;\mathbb{R}^k)$.

*(Standard; see e.g. W. P. Ziemer, Weakly Differentiable Functions, Ch. 2. In (b) continuity is used only to know that on each compact $K\subset\Omega$ the map $u$ takes values in a compact subset of $W$, on which $DF$ is bounded.)*

For a continuous map $f\colon M\to N$ and charts $(U,\varphi)$ of $M$, $(V,\psi)$ of $N$, put $U_f:=U\cap f^{-1}(V)$ (open, by continuity) and call
$$f_{\varphi\psi}:=\psi\circ f\circ\varphi^{-1}\colon \varphi(U_f)\to\mathbb{R}^k$$
the *local representative* of $f$.

**Proposition 47.2 (independence of charts).** Let $f\colon M\to N$ be continuous. If $f_{\varphi\psi}\in W^{1,p}_{\mathrm{loc}}(\varphi(U_f);\mathbb{R}^k)$ for all charts $(U,\varphi)$, $(V,\psi)$ from some atlas of $M$ and some atlas of $N$, then the same holds for all charts of $M$ and $N$. In that case there is a map $x\mapsto Df(x)$, defined for a.e. $x\in M$, with $Df(x)\colon T_xM\to T_{f(x)}N$ linear, such that for all charts
$$d\psi_{f(x)}\circ Df(x)\circ (d\varphi_x)^{-1}=Df_{\varphi\psi}(\varphi(x))\quad\text{for a.e. } x\in U_f ,$$
(both sides viewed as linear maps $\mathbb{R}^m\to\mathbb{R}^k$); $Df$ is unique up to a null set and is measurable (its matrix in any chart pair is measurable). *(Proof: Proposition 47.1(a) for the change of chart on $M$, 47.1(b) with $F$ a transition map of $N$, and 47.1(c).)*

**Definition 47.3.** Let $1\le p\le\infty$.

(a) The set $W^{1,p}_{\mathrm{loc}}(M,N)$ consists of all **continuous** maps $f\colon M\to N$ such that for every chart $(U,\varphi)$ of $M$ and every chart $(V,\psi)$ of $N$ the local representative satisfies $f_{\varphi\psi}\in W^{1,p}_{\mathrm{loc}}(\varphi(U_f);\mathbb{R}^k)$ (by Proposition 47.2 it suffices to check this for one atlas of $M$ and one atlas of $N$). It is a set of maps, not a vector space.

(b) For $f\in W^{1,p}_{\mathrm{loc}}(M,N)$, the a.e.-defined field of linear maps $Df(x)\colon T_xM\to T_{f(x)}N$ of Proposition 47.2 is the **weak differential** of $f$.

(c) If $M,N$ carry Riemannian metrics $g_M,g_N$, the **operator norm** of the weak differential is the a.e.-defined measurable function
$$\lVert Df\rVert(x):=\sup\{\,|Df(x)v|_{g_N}:\ v\in T_xM,\ |v|_{g_M}\le 1\,\}\in[0,\infty).$$

(d) If moreover $m=k=n$ and $M,N$ are oriented, with Riemannian volume forms $\mathrm{vol}_M,\mathrm{vol}_N$, the **Jacobian (determinant)** of $f$ is the a.e.-defined measurable function $J_f\colon M\to\mathbb{R}$ determined by
$$\big(Df(x)\big)^*\big((\mathrm{vol}_N)_{f(x)}\big)=J_f(x)\,(\mathrm{vol}_M)_x ,$$
i.e. $J_f(x)=\det Df(x)$ computed in positively oriented $g_M$- and $g_N$-orthonormal bases of $T_xM$ and $T_{f(x)}N$. In positively oriented charts,
$$J_f(x)=\det Df_{\varphi\psi}(\varphi(x))\cdot\frac{\sqrt{\det\big(g_N\big)_{ij}(\psi(f(x)))}}{\sqrt{\det\big(g_M\big)_{ij}(\varphi(x))}} ,$$
where $(g_M)_{ij}$, $(g_N)_{ij}$ are the coefficient matrices of the metrics in the coordinates $\varphi$, $\psi$. The pulled-back volume form is the a.e.-defined $n$-form $f^*\mathrm{vol}_N:=J_f\,\mathrm{vol}_M$.

*Remarks.*

(1) For continuous $f$, given Riemannian metrics: $f\in W^{1,p}_{\mathrm{loc}}(M,N)$ iff all local representatives lie in $W^{1,1}_{\mathrm{loc}}$ and $\lVert Df\rVert\in L^p_{\mathrm{loc}}(M,\mathrm{vol}_M)$. That is because on compact subsets of charts the metric coefficients are bounded above and below, and $f_{\varphi\psi}$ is locally bounded. Hadamard's inequality gives $|J_f|\le\lVert Df\rVert^n$ a.e., so $J_f\in L^{p/n}_{\mathrm{loc}}(M)$ when $m=k=n$; in particular $J_f\in L^1_{\mathrm{loc}}$ for $p=n$.
(2) Equivalent formulation via an embedding. Let $\iota\colon N\to\mathbb{R}^l$ be a smooth embedding (e.g. a Nash isometric embedding). Then a continuous $f$ lies in $W^{1,p}_{\mathrm{loc}}(M,N)$ iff $\iota\circ f\in W^{1,p}_{\mathrm{loc}}(M,\mathbb{R}^l)$ (componentwise, in charts of $M$), and then $D(\iota\circ f)=d\iota\circ Df$ a.e. If $\iota$ is isometric then $\lVert Df\rVert=\lVert D(\iota\circ f)\rVert$. [2025, 201(2), no. 3] uses this form (Appendix B, with a Nash embedding).
(3) For **discontinuous** maps the chart definition is meaningless. The usual definition there (Bethuel, Hajłasz and others) is $\{f:\iota\circ f\in W^{1,p}(M,\mathbb{R}^l),\ \iota\circ f\in\iota(N)\text{ a.e.}\}$, for compact $N$. On non-compact targets that version can depend on $\iota$. Quasiregular theory, and [2025, 201(2), no. 3], uses only continuous maps, and the continuity requirement in 47.3(a) is deliberate.
(4) When $M=\Omega\subset\mathbb{R}^n$ and $N=\mathbb{R}^n$ (Euclidean metrics, standard orientation), $Df$ is the weak Jacobian matrix, $\lVert Df\rVert$ its operator norm and $J_f=\det Df$. In [2025, 201(2), no. 3] the case used is $p=n=\dim M=\dim N\ge 2$, with $M=\mathbb{R}^n$ or a Euclidean ball and $N$ closed, connected and oriented.

## 48. Topological class (instanton number) of a finite-energy connection on $\mathbb{R}^4$

*Chapter context.* A chapter on finite-energy connections in a book on Yang–Mills theory (elliptic and hyperbolic) on $\mathbb{R}^4$. The reader knows compact Lie groups, their Lie algebras and bi-invariant inner products, homotopy groups, the Sobolev spaces $H^1_{\mathrm{loc}}(\mathbb{R}^4)$ and $\dot H^1(\mathbb{R}^4)$ with $H^1_{\mathrm{loc}}\subset L^4_{\mathrm{loc}}$ and $\dot H^1\subset L^4$, and smooth connections on the trivial bundle over $\mathbb{R}^4$ as Lie-algebra-valued $1$-forms, with their curvature and gauge transformations.

Throughout, $\mathbf{G}$ is a compact Lie group, realised (Peter–Weyl) as a closed subgroup of some $U(N)$, so its Lie algebra is $\mathfrak{g}\subset\mathfrak{u}(N)$. It carries a bi-invariant inner product $\langle\cdot,\cdot\rangle$. For $\mathbf{G}=SU(2)$ the standard choice is $\langle X,Y\rangle=-\operatorname{tr}(XY)$. Here $\dot H^1(\mathbb{R}^4)$ is the closure of $C_c^\infty$ under $\lVert\nabla u\rVert_{L^2}$, realised inside $L^4$ by the Sobolev inequality. Indices $j,k,\ldots$ run over $1,\dots,4$, repeated indices are summed, and $\mathbb{R}^4$ has its standard orientation.

**Definition 48.1.**

(a) A **finite-energy connection** on $\mathbb{R}^4$ is $a=a_j\,dx^j$ with $a_j\in H^1_{\mathrm{loc}}(\mathbb{R}^4;\mathfrak{g})$ whose curvature
$$f_{jk}=\partial_ja_k-\partial_ka_j+[a_j,a_k]\in L^2_{\mathrm{loc}}$$
lies in $L^2(\mathbb{R}^4)$. Its (static) energy is $\mathcal{E}_e(a)=\int_{\mathbb{R}^4}\tfrac12\langle f_{jk},f_{jk}\rangle\,dx$.

(b) An **admissible gauge transformation** is a measurable $O\colon\mathbb{R}^4\to\mathbf{G}$ with $O\in W^{1,1}_{\mathrm{loc}}$ and $O_{;j}:=(\partial_jO)O^{-1}\in H^1_{\mathrm{loc}}(\mathbb{R}^4;\mathfrak{g})$. Equivalently, $O\in H^2_{\mathrm{loc}}$ with values in $\mathbf{G}$ a.e. It acts by
$$\mathcal{G}(O)a_j:=O\,a_j\,O^{-1}-O_{;j},$$
which maps finite-energy connections to finite-energy connections, with $f\mapsto OfO^{-1}$ and $\mathcal{E}_e$ preserved. Two finite-energy connections are **gauge equivalent** if one is $\mathcal{G}(O)$ of the other.

**Theorem 48.2 (good global gauge; Oh–Tataru, *The hyperbolic Yang–Mills equation for connections in an arbitrary topological class*, Thm. 1.5).** Every finite-energy connection $a$ is gauge equivalent to one of the form
$$\tilde a=-\eta\,O_{(\infty);x}+b .$$
Here $\eta\in C^\infty(\mathbb{R}^4)$ vanishes near $0$ and $1-\eta$ has compact support; $O_{(\infty)}\colon\mathbb{R}^4\setminus\{0\}\to\mathbf{G}$ is smooth and $0$-homogeneous ($O_{(\infty)}(\lambda x)=O_{(\infty)}(x)$ for $\lambda>0$); and $b\in\dot H^1(\mathbb{R}^4;\mathfrak{g})$.

**Proposition 48.3 (well-definedness; same source, as summarised in [2021, 194(2), no. 1], §2.3).** In Theorem 48.2, the homotopy class of $O_{(\infty)}|_{S^3}\colon S^3\to\mathbf{G}$ is determined by the gauge-equivalence class of $a$, up to translation by constants (Remark 3). Every homotopy class occurs, and $O_{(\infty)}$ may be chosen arbitrarily within its class.

**Definition 48.4.** Assume $\mathbf{G}$ is connected, so free homotopy classes $S^3\to\mathbf{G}$ form the group $\pi_3(\mathbf{G})$. Let $a$ be a finite-energy connection.

(a) The **topological class** of $a$ is $[a]:=[O_{(\infty)}|_{S^3}]\in\pi_3(\mathbf{G})$, for any representative $\tilde a$ of $a$ as in Theorem 48.2; by Proposition 48.3 it is an invariant of the gauge-equivalence class of $a$.
(b) $a$ is **topologically trivial** if $[a]=[0]$, the class of the zero connection, i.e. the trivial element of $\pi_3(\mathbf{G})$ ($O_{(\infty)}$ is homotopic to a constant map).
(c) The **characteristic number** (instanton number) of $a$ is
$$\chi(a):=\int_{\mathbb{R}^4}-\langle f\wedge f\rangle=-\frac14\int_{\mathbb{R}^4}\langle f_{ij},f_{kl}\rangle\,dx^i\wedge dx^j\wedge dx^k\wedge dx^l ,$$
which converges absolutely by the pointwise *Bogomol'nyi bound* $|\langle f\wedge f\rangle|\le\tfrac12\langle f_{jk},f_{jk}\rangle\,dx$. Hence $|\chi(a)|\le\mathcal{E}_e(a)$.

(d) A finite-energy initial data set $(a,e)$ for the hyperbolic Yang–Mills equation, or a finite-energy solution $A$ on $I\times\mathbb{R}^4$, is topologically trivial if $a$, respectively $A_x(t)=(A_j(t))_j$, is. The class of $A_x(t)$ does not depend on $t$.

**Proposition 48.5 (Oh–Tataru; quoted in [2021, 194(2), no. 1], §1.1.7 and Thm. 2.16).** (i) A finite-energy connection is topologically trivial iff it is gauge equivalent to a connection with all $a_j\in\dot H^1(\mathbb{R}^4)$. (ii) $\chi(a)$ depends only on $[a]$, and $\chi([0])=0$. (iii) For $\mathbf{G}=SU(2)$ and $\langle X,Y\rangle=-\operatorname{tr}(XY)$, one has $\chi(a)=8\pi^2c_2(a)$ with $c_2(a):=\frac1{8\pi^2}\int\operatorname{tr}(f\wedge f)\in\mathbb{Z}$. The integer $c_2$ determines $[a]\in\pi_3(SU(2))\cong\mathbb{Z}$ (up to a sign convention), and every integer occurs.

*Remarks.*

(1) What the papers need. [2021, 194(2), no. 1] (Threshold and Dichotomy Theorems) uses only "topologically trivial", i.e. $[a]=[0]$, and $\chi$, for $\mathbf{G}$ compact and non-commutative. By 48.5(i) a formaliser may take "gauge equivalent to an $\dot H^1$ connection" as the definition of topological triviality, which avoids $\pi_3$ entirely.
(2) Relation to bundles over $S^4$ (the classical instanton number). For a finite-energy Yang–Mills connection ($D^\ell f_{\ell j}=0$), Uhlenbeck's removable singularity theorem (Comm. Math. Phys. 1982) applies after stereographic projection, using conformal invariance of the energy in dimension $4$. It extends $a$, up to gauge, to a smooth connection on a principal $\mathbf{G}$-bundle $P\to S^4$. Such bundles are classified by their clutching class in $\pi_3(\mathbf{G})$, which corresponds to $[a]$; for $SU(2)$, $c_2(P)=\chi(a)/8\pi^2$. A general finite-energy connection need not extend in this way, which is why Definition 48.4 goes through Theorem 48.2.
(3) Disconnected $\mathbf{G}$. Constant gauge transformations are admissible and send $O_{(\infty)}$ to $gO_{(\infty)}$, while $O_{(\infty)}g$ gives the same $\tilde a$. So the class lives in the set of free homotopy classes $[S^3,\mathbf{G}]$ modulo left and right translations by constants, which is $\pi_3(\mathbf{G}_0)$ modulo conjugation by $\pi_0(\mathbf{G})$. "Topologically trivial" still means that $O_{(\infty)}|_{S^3}$ is null-homotopic.
(4) For compact connected $\mathbf{G}$, $\pi_3(\mathbf{G})\cong\mathbb{Z}^s$, where $s$ is the number of simple ideals of $[\mathfrak{g},\mathfrak{g}]$. So for $s\ge2$ the number $\chi$, a weighted sum depending on $\langle\cdot,\cdot\rangle$, only partially determines $[a]$, as the paper notes.

# Geometry & topology

## 49. Second fundamental form, principal curvatures and mean curvature of a hypersurface

*Chapter context.* A chapter on submanifold geometry in a graduate Riemannian geometry text. The reader knows smooth manifolds (possibly with boundary), immersions and embeddings, vector bundles and their pullbacks, Riemannian metrics, the Levi-Civita connection and the Riemann curvature tensor, and normal spaces of immersed submanifolds; the extrinsic curvature of a hypersurface is introduced here.

Throughout, $(M,g)$ is a smooth Riemannian manifold of dimension $n+1\ge 2$ with Levi-Civita connection $\bar\nabla$, $\Sigma$ is a smooth $n$-manifold and $F\colon\Sigma\to M$ is a smooth immersion (an *immersed hypersurface*; when $F$ is an embedding we identify $\Sigma$ with $F(\Sigma)$). The induced metric on $\Sigma$ is $F^*g$, and $\langle\cdot,\cdot\rangle$ denotes $g$ on the fibres of $F^*TM$.

**Proposition 49.1 (pullback connection).** There is a unique connection $\nabla^F$ on the pullback bundle $F^*TM\to\Sigma$ such that $\nabla^F_X(V\circ F)=\bar\nabla_{dF(X)}V$ for every vector field $V$ on $M$ and every $X\in T\Sigma$. It is compatible with $g$, i.e. $X\langle\xi,\eta\rangle=\langle\nabla^F_X\xi,\eta\rangle+\langle\xi,\nabla^F_X\eta\rangle$ for sections $\xi,\eta$ of $F^*TM$, and torsion-free in the sense $\nabla^F_X\big(dF(Y)\big)-\nabla^F_Y\big(dF(X)\big)=dF([X,Y])$ for vector fields $X,Y$ on $\Sigma$. (If $F$ restricts to an embedding on an open $U\ni p$ and $\tilde\xi$ is any smooth vector field near $F(p)$ with $\tilde\xi\circ F=\xi$ on $U$, then $\nabla^F_X\xi=\bar\nabla_{dF(X)}\tilde\xi$ for $X\in T_p\Sigma$.)

**Definition 49.2 (unit normal, two-sidedness).** A *unit normal field* along $F$ on an open set $U\subseteq\Sigma$ is a smooth section $\nu$ of $F^*TM|_U$ with $\langle\nu,\nu\rangle=1$ and $\langle\nu(p),dF_p(v)\rangle=0$ for all $p\in U$, $v\in T_p\Sigma$. Unit normal fields always exist locally, and on a connected $U$ there are either none or exactly two, $\pm\nu$. The hypersurface is *two-sided* if a unit normal field exists on all of $\Sigma$ (equivalently, the normal line bundle is trivial; if $M$ is orientable this holds iff $\Sigma$ is orientable). If $\Sigma=\partial\Omega$ for an open $\Omega\subseteq M$ with smooth boundary, or $\Sigma=\partial M$ for a Riemannian manifold with boundary, the *outward unit normal* is the unit normal pointing out of $\Omega$ (resp. $M$).

**Proposition 49.3.** Let $\nu$ be a unit normal field on $U$ and $p\in U$. For each $X\in T_p\Sigma$ the vector $\nabla^F_X\nu$ is orthogonal to $\nu(p)$, hence lies in $dF_p(T_p\Sigma)$. For vector fields $X,Y$ on $U$,
$$\langle\nabla^F_X\nu,\,dF(Y)\rangle=-\langle\nu,\,\nabla^F_X\big(dF(Y)\big)\rangle,$$
and this expression is symmetric in $X,Y$ and $C^\infty(U)$-bilinear. (Differentiate $\langle\nu,\nu\rangle=1$ and $\langle\nu,dF(Y)\rangle=0$, and use torsion-freeness in 49.1.)

**Definition 49.4.** Let $\nu$ be a unit normal field along $F$ on $U\subseteq\Sigma$, and $p\in U$.

1. The *shape operator* (Weingarten map) is the linear map $S_p\colon T_p\Sigma\to T_p\Sigma$ determined by $dF_p(S_pX)=\nabla^F_X\nu$; it is self-adjoint for $(F^*g)_p$.
2. The *second fundamental form* is the symmetric bilinear form $A_p=\mathrm{I\!I}_p$ on $T_p\Sigma$,
$$A_p(X,Y)=\langle\nabla^F_X\nu,\,dF_p(Y)\rangle=(F^*g)_p(S_pX,Y)=-\langle\nu(p),\nabla^F_X\big(dF(Y)\big)(p)\rangle .$$
Then $A$ is a smooth symmetric $(0,2)$-tensor field on $U$.

3. The *principal curvatures* at $p$ are the eigenvalues of $S_p$ (all real, since $S_p$ is self-adjoint), repeated according to multiplicity and ordered $\kappa_1(p)\le\kappa_2(p)\le\dots\le\kappa_n(p)$; an orthonormal eigenbasis is a basis of *principal directions*. Each $\kappa_i$ is a continuous function on $U$.
4. The *norm* of the second fundamental form is $|A|(p)\ge0$ with
$$|A|^2(p)=\sum_{i,j=1}^nA_p(e_i,e_j)^2=\operatorname{tr}(S_p^2)=\sum_{i=1}^n\kappa_i(p)^2,$$
for any $(F^*g)_p$-orthonormal basis $e_1,\dots,e_n$ of $T_p\Sigma$.

5. The *mean curvature* is $H(p)=\operatorname{tr}S_p=\sum_{i=1}^nA_p(e_i,e_i)=\sum_{i=1}^n\kappa_i(p)$ (the trace with respect to $F^*g$, not divided by $n$), and the *mean curvature vector* is $\vec H(p)=-H(p)\,\nu(p)\in(F^*TM)_p$.
6. With respect to $\nu$, $\Sigma$ is *convex* (resp. *strictly convex*) at $p$ if $A_p$ is positive semi-definite (resp. positive definite), *mean convex* if $H(p)\ge0$, and for $1\le k\le n$ *$k$-convex* if $\kappa_1(p)+\dots+\kappa_k(p)\ge0$. A family is *uniformly $k$-convex* if there is $\beta>0$ with $\kappa_1+\dots+\kappa_k\ge\beta H$ everywhere. For $\Sigma=\partial\Omega$ or $\Sigma=\partial M$ these notions are always taken with respect to the outward unit normal.

Replacing $\nu$ by $-\nu$ replaces $S,A,H$ by $-S,-A,-H$ and $\kappa_i$ by $-\kappa_{n+1-i}$, while $|A|$ and $\vec H$ are unchanged; hence $|A|$ and $\vec H$ are defined on all of $\Sigma$ even when it is not two-sided.

**Proposition 49.5 (useful formulas).** (a) In local coordinates $x^1,\dots,x^n$ on $\Sigma$, with $h_{ij}=(F^*g)(\partial_i,\partial_j)$ and $A_{ij}=A(\partial_i,\partial_j)$: $H=h^{ij}A_{ij}$ and $|A|^2=h^{ik}h^{jl}A_{ij}A_{kl}$; if $M=\mathbb{R}^{n+1}$ is Euclidean, $A_{ij}=-\langle\nu,\partial_i\partial_jF\rangle$. (b) If $f\in C^\infty(M)$, $c$ is a regular value and $\Sigma=f^{-1}(c)$ with $\nu=\bar\nabla f/|\bar\nabla f|$, then $A(X,Y)=\bar\nabla^2f(X,Y)/|\bar\nabla f|$ for $X,Y\in T\Sigma$ and $H=\operatorname{div}_g\big(\bar\nabla f/|\bar\nabla f|\big)$ on $\Sigma$. (c) (Gauss equation) For linearly independent $X,Y\in T_p\Sigma$, the sectional curvatures of $F^*g$ and $g$ satisfy
$$\sec_{F^*g}(X,Y)=\sec_g\big(dF(X),dF(Y)\big)+\frac{A(X,X)A(Y,Y)-A(X,Y)^2}{|X|^2|Y|^2-(F^*g)(X,Y)^2};$$
in particular for $n=2$ the Gauss curvature is $K=\sec_g(dF_p(T_p\Sigma))+\kappa_1\kappa_2$.

*Remarks.* Sign conventions vary: many texts (e.g. Lee, *Introduction to Riemannian Manifolds*) define the scalar second fundamental form as $\langle\nabla^F_XdF(Y),\nu\rangle=-A(X,Y)$ and the shape operator as $-S$; others define a vector-valued second fundamental form $\mathrm{I\!I}(X,Y)=\big(\nabla^F_XdF(Y)\big)^\perp$, valid in any codimension, related to ours by $\mathrm{I\!I}(X,Y)=-A(X,Y)\nu$ and $\vec H=\operatorname{tr}_{F^*g}\mathrm{I\!I}$. The convention above is chosen so that the round sphere of radius $r$ in $\mathbb{R}^{n+1}$ with outward normal has $A=r^{-1}F^*g$, $\kappa_i=1/r$, $H=n/r$, matching mean curvature flow $\partial_tF=-H\nu$ with outward $\nu$ [2020, 192(2), no. 2]; some authors normalise $H$ by $1/n$. For $\Sigma=\partial M$ the definitions only involve $g$ on $M$. Uses: $|A|^2$ in the stability inequality and Jacobi operator of minimal hypersurfaces in Euclidean space or closed manifolds [2023, 197(3), no. 4], [2020, 192(3), no. 3]; the curvature estimate for level sets of Allen–Cahn solutions [2020, 191(1), no. 4], where the paper uses the "enhanced" form $\mathcal{A}=\bar\nabla(\bar\nabla u/|\bar\nabla u|)$ on $M$, whose norm dominates $|A|$ of the level sets (cf. 49.5(b)); uniform 2-convexity of ancient ovals in $\mathbb{R}^{n+1}$ [2020, 192(2), no. 2]; strict convexity of $\partial M$ (positive definite $A$ with outward normal; see Definition #66) and of level sets "strictly concave from the superlevel sets" (positive definite $A$ with respect to $\nu=\bar\nabla\mathsf{x}/|\bar\nabla\mathsf{x}|$) in boundary rigidity [2021, 194(1), no. 1]; surfaces in $\mathbb{H}^3$ with $|A|^2=\kappa_1^2+\kappa_2^2$ and $K=-1+\kappa_1\kappa_2$ [2025, 202(1), no. 2]. Minimal hypersurfaces ($H\equiv0$) are Definition #52.

## 50. Lorentzian manifold, time orientation and spacetime

*Chapter context.* The opening chapter of a text on Lorentzian geometry and general relativity. The reader knows smooth manifolds (with boundary or corners), tensor fields and their regularity classes $C^k$, $C^{k,\alpha}$ in charts, nondegenerate symmetric bilinear forms and Sylvester's law of inertia, and Riemannian metrics with their Levi-Civita connection and curvature; metrics of Lorentzian signature are introduced here.

**Definition 50.1 (Lorentzian scalar products).** Let $V$ be a real vector space of dimension $n+1\ge2$. A *Lorentzian scalar product* on $V$ is a symmetric bilinear form $b$ that is nondegenerate and has *index* $1$, i.e. the maximal dimension of a subspace on which $b$ is negative definite is $1$. Equivalently, $V$ has a basis $e_0,\dots,e_n$ with $b(e_i,e_j)=\eta_{ij}$, where $\eta=\operatorname{diag}(-1,1,\dots,1)$ (signature $(-,+,\dots,+)$). A vector $v\in V$ is *timelike* if $b(v,v)<0$, *null* (or *lightlike*) if $b(v,v)=0$ and $v\ne0$, *causal* if it is timelike or null, and *spacelike* if $b(v,v)>0$ or $v=0$.

**Proposition 50.2.** Let $b$ be a Lorentzian scalar product on $V$. (a) The set of timelike vectors is open and has exactly two connected components (the *timelike cones*); each is a convex cone and they are exchanged by $v\mapsto-v$. (b) Timelike $v,w$ lie in the same timelike cone iff $b(v,w)<0$. (c) If $v$ is timelike then $b$ is positive definite on $v^{\perp}$ and $V=\mathbb{R}v\oplus v^{\perp}$. (d) Every causal vector lies in the closure of exactly one timelike cone; for a timelike $v$ and a causal $w$, $w$ lies in the closure of the cone of $v$ iff $b(v,w)<0$. (Standard; see O'Neill, *Semi-Riemannian Geometry with Applications to Relativity*.)

**Definition 50.3 (Lorentzian manifold).** Let $M$ be a smooth manifold of dimension $n+1\ge2$, possibly with boundary or corners, and let $\mathcal{R}$ be a regularity class ($C^\infty$ by default; also $C^k$, $C^{k,\alpha}$ with $k\ge0$, $0<\alpha\le1$). A *Lorentzian metric of class $\mathcal{R}$* on $M$ is a section $g$ of the bundle $\operatorname{Sym}^2T^*M$ of symmetric bilinear forms on $TM$ whose components $g_{\mu\nu}=g(\partial_\mu,\partial_\nu)$ in every chart are of class $\mathcal{R}$, such that $g_p$ is a Lorentzian scalar product on $T_pM$ for every $p\in M$. (Pointwise this is equivalent to: $\det(g_{\mu\nu})<0$ everywhere and $g_p$ is not negative definite on any $2$-dimensional subspace.) A *Lorentzian manifold* is a pair $(M,g)$. A tangent vector $v\in T_pM$ is timelike/null/causal/spacelike if it is so for $g_p$; a vector field or a piecewise $C^1$ curve is timelike (etc.) if all its values, resp. all its one-sided tangent vectors, are.

**Definition 50.4 (time orientation; spacetime).** Let $(M,g)$ be a Lorentzian manifold with $g$ at least continuous.

1. Two continuous timelike vector fields $T,T'$ on $M$ are *equivalent* if $g(T,T')<0$ at every point. A *time orientation* is an equivalence class $\mathfrak{t}=[T]$; $(M,g)$ is *time-orientable* if a continuous timelike vector field exists. If $M$ is connected and time-orientable it has exactly two time orientations, $[T]$ and $[-T]$. (Every class contains a smooth representative, by convexity of timelike cones and a partition of unity.)
2. Given $\mathfrak{t}=[T]$, a causal vector $v\in T_pM$ is *future-directed* if $g(v,T_p)<0$ and *past-directed* if $g(v,T_p)>0$ (independent of the representative $T$, by 50.2). A piecewise $C^1$ (or locally Lipschitz) curve is *future-directed timelike* (resp. *causal*) if its tangent vectors (existing almost everywhere in the Lipschitz case) are future-directed timelike (resp. causal).
3. A *time-oriented Lorentzian manifold* is a triple $(M,g,\mathfrak{t})$. A *spacetime* is a connected time-oriented Lorentzian manifold; a *$(3+1)$-dimensional spacetime* (the default in general relativity) is one with $\dim M=4$.

**Definition 50.5 (extensions).** Let $(M,g)$ be a connected Lorentzian manifold without boundary. A *$C^k$-extension* ($k\ge0$) of $(M,g)$ is a connected Lorentzian manifold $(\tilde M,\tilde g)$ without boundary, of the same dimension, with $\tilde g$ of class $C^k$, together with a smooth embedding $\iota\colon M\to\tilde M$ with $\iota^*\tilde g=g$ and $\iota(M)\ne\tilde M$. $(M,g)$ is *$C^k$-extendible* if such an extension exists, and *$C^k$-inextendible* otherwise.

*Remarks.* For a formaliser: a Lorentzian metric is the same data as a Riemannian one (Mathlib's `Bundle.RiemannianMetric`) except that positive definiteness is replaced by nondegeneracy plus index $1$; it is convenient to store a time orientation as a chosen timelike vector field up to the equivalence above. Some texts use signature $(+,-,\dots,-)$; all Annals papers listed use $(-,+,\dots,+)$. For $g$ of class $C^k$, $k\ge1$, the Levi-Civita connection exists and is unique, with Christoffel symbols $\Gamma^\lambda_{\mu\nu}=\frac12g^{\lambda\sigma}(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu})$ of class $C^{k-1}$, and Riemann, Ricci and scalar curvature are classically defined for $k\ge2$ by the same formulas as in the Riemannian case; geodesics are unique when $g\in C^{1,1}$ but uniqueness may fail for $C^{1,\alpha}$, $\alpha<1$. Typical examples: Minkowski space $(\mathbb{R}^{n+1},\eta)$ time-oriented by $\partial_t$; a double null metric $g=-2\Omega^2(du\otimes dv+dv\otimes du)+g\mkern-9mu/_{AB}(d\theta^A-b^Adu)\otimes(d\theta^B-b^Bdu)$ with $\Omega>0$ and $g\mkern-9mu/$ positive definite on the spheres (Lorentzian since, in the coframe $du,dv,d\theta^A-b^Adu$, it is block diagonal with blocks of signatures $(1,1)$ and $(0,2)$), as in [2023, 198(1), no. 3] (where $g$ is only $C^{1,c\epsilon^2}$ across $\{\hat v=0\}$ and $\mathcal{M}$ has boundary) and [2025, 201(3), no. 3]; the $(2+1)$-dimensional acoustical metric $g=-c^2dt^2+\sum_i(dx^i-v^idt)^2$ ($c>0$) of the compressible Euler equations, time-oriented by $\partial_t+v^i\partial_i$ (which has $g$-length squared $-c^2$), in [2025, 202(2), no. 2] and [2025, 202(2), no. 3]. The statement "the metric is continuously extendible across the Cauchy horizon" in [2025, 202(2), no. 1] concerns $C^0$-extensions in the sense of 50.5 (with $\dim=4$); there $(\mathcal{M},g)$ is a smooth vacuum spacetime, $\operatorname{Ric}(g)=0$.

## 51. Null (characteristic) hypersurface of a Lorentzian manifold

*Chapter context.* A chapter on submanifolds of Lorentzian manifolds in a text on Lorentzian geometry and hyperbolic PDE. The reader knows Lorentzian manifolds, causal character of vectors and time orientations (Definition #50), embedded and immersed $C^1$ hypersurfaces, and the Levi-Civita connection and geodesics of a pseudo-Riemannian metric; the causal type of a hypersurface is introduced here.

Throughout, $(M,g)$ is a Lorentzian manifold of dimension $n+1\ge2$ (Definition #50) with $g$ at least continuous; $g^{-1}$ denotes the inverse metric on $T^*M$, so $g^{-1}(\xi,\xi)=g^{\mu\nu}\xi_\mu\xi_\nu$, and $\xi^\sharp\in T_pM$ is the vector with $g(\xi^\sharp,\cdot)=\xi$.

**Proposition 51.1 (hyperplanes in a Lorentzian vector space).** Let $(V,b)$ be a Lorentzian scalar product space of dimension $n+1$, let $\xi\in V^*\setminus\{0\}$ and $W=\ker\xi$, a hyperplane. Then $W^{\perp}=\mathbb{R}\,\xi^\sharp$ is a line and $b(\xi^\sharp,\xi^\sharp)=b^{-1}(\xi,\xi)$. Exactly one of the following holds:

1. $b^{-1}(\xi,\xi)<0$, $\xi^\sharp$ is timelike, and $b|_W$ is positive definite (*$W$ is spacelike*);
2. $b^{-1}(\xi,\xi)>0$, $\xi^\sharp$ is spacelike, and $b|_W$ is nondegenerate of index $1$, equivalently $W$ contains a timelike vector (*$W$ is timelike*);
3. $b^{-1}(\xi,\xi)=0$, $\xi^\sharp$ is null and lies in $W$, and $b|_W$ is degenerate (*$W$ is null*). In this case $b|_W$ is positive semi-definite with radical $W\cap W^\perp=\mathbb{R}\,\xi^\sharp$, $W$ contains no timelike vector, and the null vectors in $W$ are exactly the nonzero multiples of $\xi^\sharp$.

In particular $W$ is null iff $W$ contains a null vector but no timelike vector, i.e. $W$ is tangent to the light cone.

**Definition 51.2.** Let $\Sigma\subseteq M$ be an embedded $C^1$ hypersurface (more generally, let $F\colon\Sigma\to M$ be a $C^1$ immersion of an $n$-manifold and put $T_p\Sigma:=dF_p(T_p\Sigma)$). At $p\in\Sigma$, $\Sigma$ is *spacelike*, *timelike* or *null* if the hyperplane $T_p\Sigma\subseteq T_{p}M$ is so for $g_p$ in the sense of 51.1. The hypersurface $\Sigma$ is a *null hypersurface* (also *lightlike*, or *characteristic* for $g$) if it is null at every point. Equivalently, each of the following holds for every $p\in\Sigma$:

- the induced symmetric form $g|_{T_p\Sigma}$ is degenerate;
- the normal line $(T_p\Sigma)^\perp$ is spanned by a null vector;
- $(T_p\Sigma)^{\perp}\subseteq T_p\Sigma$;
- if near $p$ we have $\Sigma=\{u=c\}$ for a $C^1$ function $u$ with $du_p\ne0$, then $g^{-1}(du,du)(p)=0$.

A *null normal* of a null hypersurface $\Sigma$ is a continuous nowhere-vanishing vector field $L$ along $\Sigma$ with $L_p\in(T_p\Sigma)^\perp$ for all $p$; it is null and tangent to $\Sigma$, and is unique up to multiplication by a nowhere-vanishing function. If $M$ is time-oriented, $L$ can be (and is usually) chosen future-directed. A $C^1$ function $u$ on an open $U\subseteq M$ with $du\ne0$ and $g^{-1}(du,du)=0$ on $U$ (the *eikonal equation*) is an *optical function*; its level sets are null hypersurfaces foliating $U$.

**Proposition 51.3 (null generators).** Suppose $g$ is $C^1$ and $\Sigma$ is a $C^2$ null hypersurface with a $C^1$ null normal $L$. Then $\nabla_LL=\kappa L$ along $\Sigma$ for a continuous function $\kappa$, so the integral curves of $L$ are, after reparametrisation, null geodesics contained in $\Sigma$ (the *null generators* of $\Sigma$). If $u$ is a $C^2$ optical function and $L=-\operatorname{grad}_g u=-(du)^\sharp$, then $\nabla_LL=0$. (For $X$ tangent to $\Sigma$: $g(\nabla_LL,X)=-g(L,[L,X])-\tfrac12X\,g(L,L)=0$, so $\nabla_LL\in(T\Sigma)^\perp=\mathbb{R}L$; for an optical function, $\nabla_{(du)^\sharp}(du)^\sharp=\tfrac12\operatorname{grad}_g\big(g^{-1}(du,du)\big)=0$.)

*Remarks.* The definition is pointwise, so it applies verbatim to merely continuous metrics and $C^1$ hypersurfaces, which is the situation for the characteristic hypersurfaces across which a solution fails to be $C^1$. "Characteristic" comes from PDE: the principal symbol of the wave operator $\Box_g$ at $\xi$ is $\pm g^{-1}(\xi,\xi)$ (sign depending on convention), so a hypersurface $\{\phi=0\}$, $d\phi\ne0$, is characteristic for $\Box_g$ iff it is null for $g$. In [2025, 202(2), no. 2] and [2025, 202(2), no. 3] the metric is the $(2+1)$-dimensional acoustical metric $g=-c^2dt^2+\sum_{i=1}^2(dx^i-v^idt)^2$ of the irrotational isentropic Euler flow; since $B=\partial_t+v^i\partial_i,\partial_1,\partial_2$ is a $g$-orthogonal frame with $g(B,B)=-c^2$, one has $g^{-1}=-c^{-2}B\otimes B+\sum_i\partial_i\otimes\partial_i$, and the eikonal equation reads $(\partial_tu+v\cdot\nabla_xu)^2=c^2|\nabla_xu|^2$. The papers state explicitly that the characteristic hypersurfaces (the rarefaction fronts $C_u$, and $C_0,\underline{C}_0,H,\underline{H}$) are the null hypersurfaces of this acoustical metric, with $C_u$ the level sets of an optical (acoustical) function $u$ and $L$ the null generator normalised by $L(t)=1$. Double null foliations in general relativity (level sets of two optical functions $u,\underline{u}$, as in Definition #50's examples) consist of null hypersurfaces in the same sense. Achronal boundaries such as $\partial I^+(S)$, and Cauchy horizons, are Lipschitz hypersurfaces which away from $\overline{S}$ (resp. the edge) are ruled by null geodesics; wherever they are $C^1$ they are null hypersurfaces (see Hawking–Ellis, *The Large Scale Structure of Space-Time*).

## 52. Minimal hypersurface in a Riemannian manifold

*Chapter context.* A chapter on minimal submanifolds in a text on geometric analysis. The reader knows Riemannian geometry (Levi-Civita connection, Ricci curvature, exponential map, Riemannian measure, Laplace–Beltrami operator, divergence theorem) and the extrinsic geometry of hypersurfaces: second fundamental form $A$, $|A|$, mean curvature $H$, mean curvature vector $\vec H=-H\nu$ and two-sidedness (Definition #49, whose sign conventions are used here); minimality, the first and second variation of area and the Morse index are introduced here.

Throughout, $(M,g)$ is a smooth Riemannian manifold of dimension $n+1\ge2$ without boundary, $\Sigma$ is a smooth $n$-manifold without boundary (not necessarily compact or connected), and $F\colon\Sigma\to M$ is a smooth immersion with induced metric $F^*g$ and Riemannian measure $\mu_F$. For compact $K\subseteq\Sigma$ write $\operatorname{Area}_K(F)=\mu_F(K)$ (the $n$-dimensional volume). The *normal bundle* $N\Sigma\subseteq F^*TM$ is the rank-one bundle of vectors orthogonal to $dF(T\Sigma)$; $\nabla^\perp$ is the connection on $N\Sigma$ obtained by orthogonally projecting the pullback connection $\nabla^F$, and $\Gamma_c(N\Sigma)$ is the space of smooth compactly supported sections.

**Definition 52.1 (variations).** A *compactly supported variation* of $F$ is a smooth map $\Phi\colon\Sigma\times(-\varepsilon,\varepsilon)\to M$ with $\Phi(\cdot,0)=F$ for which there is a compact $K\subseteq\Sigma$ with $\Phi(x,t)=F(x)$ for all $x\notin K$ and all $t$. For $|t|$ small, $F_t=\Phi(\cdot,t)$ is an immersion. Its *variation field* is the compactly supported section $X=\partial_t\Phi(\cdot,0)$ of $F^*TM$.

**Proposition 52.2 (first variation of area).** For a compactly supported variation with variation field $X$ (supported in $K$),
$$\frac{d}{dt}\Big|_{t=0}\operatorname{Area}_K(F_t)=\int_\Sigma\operatorname{div}_\Sigma X\,d\mu_F=-\int_\Sigma\langle\vec H,X\rangle\,d\mu_F,$$
where $\operatorname{div}_\Sigma X=\sum_{i=1}^n\langle\nabla^F_{e_i}X,dF(e_i)\rangle$ for any $F^*g$-orthonormal frame $(e_i)$. Where a unit normal $\nu$ is chosen, $-\langle\vec H,X\rangle=H\langle X,\nu\rangle$.

**Definition 52.3 (minimal hypersurface).** The immersion $F$ is *minimal* if its mean curvature vector vanishes identically, $\vec H\equiv0$; equivalently $H\equiv0$ for every local unit normal field, i.e. $\kappa_1+\dots+\kappa_n\equiv0$; equivalently (by 52.2) $\frac{d}{dt}|_{t=0}\operatorname{Area}_K(F_t)=0$ for every compactly supported variation. An embedded $n$-dimensional submanifold $\Sigma\subseteq M$ is a *minimal hypersurface* if its inclusion is minimal. Standard qualifiers: *closed* ($\Sigma$ compact), *properly embedded* (the inclusion is a proper map), *two-sided* (Definition #49). Two minimal hypersurfaces are *geometrically distinct* if their images $F(\Sigma)$ differ.

**Definition 52.4 (second variation, index, nullity, stability).** Let $F$ be minimal, and write $\operatorname{Ric}(\nu,\nu)$ for $\operatorname{Ric}_g(\nu,\nu)$ computed with either local unit normal (it does not depend on the choice). For $X\in\Gamma_c(N\Sigma)$ and $F_t(x)=\exp_{F(x)}(tX(x))$,
$$\frac{d^2}{dt^2}\Big|_{t=0}\operatorname{Area}_K(F_t)=Q(X,X):=\int_\Sigma\Big(|\nabla^\perp X|^2-\big(|A|^2+\operatorname{Ric}(\nu,\nu)\big)|X|^2\Big)\,d\mu_F .$$
The *Jacobi operator* is $LX=\Delta^\perp X+(|A|^2+\operatorname{Ric}(\nu,\nu))X$, where $\Delta^\perp=\operatorname{tr}_{F^*g}(\nabla^\perp)^2$ is the rough Laplacian (with $\Delta=\operatorname{div}\operatorname{grad}$, a non-positive operator), so that $Q(X,X)=-\int_\Sigma\langle X,LX\rangle\,d\mu_F$. If $\Sigma$ is two-sided with unit normal $\nu$ and $X=\varphi\nu$, $\varphi\in C^\infty_c(\Sigma)$, this reads
$$Q(\varphi,\varphi)=\int_\Sigma\big(|\nabla\varphi|^2-(|A|^2+\operatorname{Ric}(\nu,\nu))\varphi^2\big)\,d\mu_F,\qquad L\varphi=\Delta_\Sigma\varphi+(|A|^2+\operatorname{Ric}(\nu,\nu))\varphi .$$

1. The *(Morse) index* $\operatorname{ind}(\Sigma)\in\{0,1,2,\dots\}\cup\{\infty\}$ is the supremum of the dimensions of linear subspaces of $\Gamma_c(N\Sigma)$ on which $Q$ is negative definite. If $\Sigma$ is closed it is finite and equals the number of negative eigenvalues, counted with multiplicity, of the self-adjoint elliptic operator $-L$.
2. A *Jacobi field* is a smooth section $X$ of $N\Sigma$ with $LX=0$. For closed $\Sigma$ the *nullity* is $\operatorname{nul}(\Sigma)=\dim\ker L<\infty$, and $\Sigma$ is *non-degenerate* if $\operatorname{nul}(\Sigma)=0$.
3. $\Sigma$ is *stable* if $Q(X,X)\ge0$ for all $X\in\Gamma_c(N\Sigma)$, i.e. $\operatorname{ind}(\Sigma)=0$.
4. The metric $g$ on $M$ is *bumpy* if every closed immersed minimal hypersurface in $(M,g)$ is non-degenerate, i.e. has no non-zero Jacobi field.

*Remarks.* Because $N\Sigma$ need not be trivial, index and nullity are defined on normal sections, not functions; for two-sided $\Sigma$ the two agree. Bumpy metrics are generic in the Baire sense among smooth metrics on a closed manifold (B. White, *The space of minimal submanifolds for varying Riemannian metrics*; *On the bumpy metrics theorem for minimal submanifolds*). Locally, a minimal hypersurface in $\mathbb{R}^{n+1}$ written as a graph $x_{n+1}=u(x)$ is exactly a solution of the minimal surface equation $\operatorname{div}\big(\nabla u/\sqrt{1+|\nabla u|^2}\big)=0$. An embedded hypersurface is minimal iff the associated multiplicity-one varifold is stationary (Definition #53); strict stability in Simon's sense is Definition #65. Uses: closed embedded minimal hypersurfaces in closed $(M^{n+1},g)$, $3\le n+1\le7$, with "infinitely many" meaning geometrically distinct [2023, 197(3), no. 1]; closed, embedded, two-sided minimal hypersurfaces with index bounds for bumpy metrics [2020, 192(3), no. 3] and in dimension $3$ also nullity and positive Ricci curvature [2020, 191(1), no. 4]; properly embedded, possibly non-compact minimal surfaces in $\mathbb{H}^3$, where minimality means $\kappa_1=-\kappa_2$ and so $K=-1-\kappa_1^2$ by the Gauss equation, and finite total curvature means $\int_S|A|^2\,d\mu<\infty$ [2025, 202(1), no. 2].

## 53. Stationary varifold

*Chapter context.* The chapter on varifolds in a text on geometric measure theory. The reader knows Radon measures on locally compact spaces and their weak-* convergence, Hausdorff measure $\mathcal{H}^k$, countably $k$-rectifiable sets and their approximate tangent planes (which exist $\mathcal{H}^k$-a.e.), the area formula, Riemannian manifolds, and minimal hypersurfaces with their mean curvature vector $\vec H$ (Definitions #49, #52); varifolds are introduced here.

Throughout, $(M,g)$ is a smooth Riemannian manifold of dimension $N$, $W\subseteq M$ is open and $1\le k\le N$ (in the papers $k=N-1$, and $M$ is $\mathbb{R}^N$ or an open subset, with the Euclidean metric or a smooth metric $g$). The *Grassmann bundle* $G_k(M)=\{(x,S):x\in M,\ S\subseteq T_xM\text{ a $k$-dimensional linear subspace}\}$ is a smooth fibre bundle over $M$ with compact fibre $G(N,k)$, hence locally compact, Hausdorff and second countable; for $W\subseteq\mathbb{R}^N$, $G_k(W)=W\times G(N,k)$, where $G(N,k)$ (unoriented $k$-planes) carries the metric $\|P_S-P_T\|$, $P_S$ the orthogonal projection onto $S$. $\mathcal{H}^k$ is taken with respect to the Riemannian distance of $g$, and $\pi(x,S)=x$.

**Definition 53.1 (varifolds).** A *$k$-varifold* in $W$ is a Radon measure $V$ on $G_k(W)$. Its *weight* (mass measure) is the Radon measure $\|V\|=\pi_\#V$ on $W$, i.e. $\|V\|(A)=V(\pi^{-1}(A))$; its *mass* is $\mathbf{M}(V)=\|V\|(W)$ and its *support* is $\operatorname{spt}\|V\|$. A sequence $V_i$ *converges to $V$ (as varifolds)* if $\int\varphi\,dV_i\to\int\varphi\,dV$ for every $\varphi\in C_c(G_k(W))$. For $A\subseteq W$ open, $V\llcorner A$ is the restriction of $V$ to $\pi^{-1}(A)$.

**Definition 53.2 (rectifiable and integral varifolds).** Let $\Gamma\subseteq W$ be countably $k$-rectifiable and $\mathcal{H}^k$-measurable, and $\theta\colon\Gamma\to(0,\infty)$ be $\mathcal{H}^k$-measurable with $\int_{\Gamma\cap K}\theta\,d\mathcal{H}^k<\infty$ for every compact $K\subseteq W$. The varifold $\mathbf{v}(\Gamma,\theta)$ is
$$\int\varphi\,d\mathbf{v}(\Gamma,\theta)=\int_\Gamma\varphi(x,T_x\Gamma)\,\theta(x)\,d\mathcal{H}^k(x)\qquad(\varphi\in C_c(G_k(W))),$$
where $T_x\Gamma$ is the approximate tangent plane. A varifold of this form is *rectifiable*; it is *integral* if $\theta$ takes values in $\{1,2,3,\dots\}$ $\mathcal{H}^k$-a.e., and of *multiplicity one* if $\theta=1$ a.e. If $\Sigma\subseteq W$ is a $C^1$ embedded $k$-submanifold with $\mathcal{H}^k(\Sigma\cap K)<\infty$ for all compact $K\subseteq W$, then $[\Sigma]:=\mathbf{v}(\Sigma,1)$ is *the (multiplicity-one) varifold associated to $\Sigma$*; here $T_x\Sigma$ is the classical tangent space.

**Definition 53.3 (push-forward).** If $f\colon W\to W'$ is a $C^1$ map into a Riemannian manifold whose restriction to $\operatorname{spt}\|V\|$ is proper, then $f_\#V$ is the $k$-varifold in $W'$ with
$$\int\varphi\,d(f_\#V)=\int\varphi\big(f(x),df_x(S)\big)\,J_Sf(x)\,dV(x,S),$$
where $J_Sf(x)=\sqrt{\det\big((df_x|_S)^*(df_x|_S)\big)}$ is the $k$-Jacobian of $df_x|_S$ (the integrand is $0$ where $J_Sf(x)=0$). For $W=\mathbb{R}^N$ and $\eta_{x,r}(y)=(y-x)/r$, this gives $\int\varphi\,d(\eta_{x,r})_\#V=r^{-k}\int\varphi\big((y-x)/r,S\big)\,dV(y,S)$.

**Definition 53.4 (first variation; stationarity).** For a $C^1$ vector field $X$ on $W$ and $(x,S)\in G_k(W)$ put $\operatorname{div}_SX(x)=\sum_{i=1}^kg(\nabla_{e_i}X,e_i)$, with $\nabla$ the Levi-Civita connection and $e_1,\dots,e_k$ any $g_x$-orthonormal basis of $S$ (in Euclidean space, $\operatorname{div}_SX=\operatorname{tr}(P_S\,DX(x))$); this is continuous on $G_k(W)$. The *first variation* of a $k$-varifold $V$ in $W$ is the linear functional
$$\delta V(X)=\int_{G_k(W)}\operatorname{div}_SX(x)\,dV(x,S),\qquad X\in C^1_c(W;TW).$$
$V$ is *stationary in $W$* (with respect to $g$) if $\delta V(X)=0$ for every compactly supported $C^1$ vector field $X$ on $W$. $V$ has *generalized mean curvature* $\vec H_V\in L^1_{\mathrm{loc}}(\|V\|)$ and no generalized boundary if $\delta V(X)=-\int g(\vec H_V,X)\,d\|V\|$ for all such $X$.

**Proposition 53.5.** (a) If $X$ is a compactly supported $C^1$ vector field with flow $\phi_t$ and $K\subseteq W$ is compact with $\operatorname{spt}X\subseteq K$, then $\frac{d}{dt}\big|_{t=0}\|(\phi_t)_\#V\|(K)=\delta V(X)$; thus stationary varifolds are the critical points of mass under compactly supported deformations. (b) If $\Sigma\subseteq W$ is a $C^2$ embedded hypersurface that is closed in $W$, with locally finite area, then $\delta[\Sigma](X)=-\int_\Sigma g(\vec H,X)\,d\mathcal{H}^k$; hence $[\Sigma]$ is stationary iff $\Sigma$ is minimal (Definition #52).

**Proposition 53.6 (monotonicity; tangent cones).** Let $V$ be stationary in an open $W\subseteq\mathbb{R}^N$ and $x\in W$. Then $r\mapsto\|V\|(B_r(x))/(\omega_kr^k)$ ($\omega_k$ the volume of the unit $k$-ball) is non-decreasing on $(0,\operatorname{dist}(x,\partial W))$, so the density $\Theta^k(\|V\|,x)$ exists. If moreover $V$ is integral, then for every sequence $r_j\downarrow0$ some subsequence of $(\eta_{x,r_j})_\#V$ converges to a stationary integral varifold $\mathbf{C}$ in $\mathbb{R}^N$ with $(\eta_{0,\lambda})_\#\mathbf{C}=\mathbf{C}$ for all $\lambda>0$; such limits are the *tangent cones* of $V$ at $x$ (Allard, *On the first variation of a varifold*; Simon, *Lectures on Geometric Measure Theory*).

For a varifold $V$, $x\in\operatorname{spt}\|V\|$ is a *regular point* if there is an open $O\ni x$ such that $\operatorname{spt}\|V\|\cap O$ is a smooth embedded $k$-submanifold closed in $O$; $\operatorname{reg}V$ is the set of regular points and $\operatorname{sing}V=\operatorname{spt}\|V\|\setminus\operatorname{reg}V$.

*Remarks.* The space of varifolds does not depend on $g$, but $[\Sigma]$ (via $\mathcal{H}^k_g$) and $\delta V$ (via $\nabla$ and $g$-orthonormal bases) do. For a smooth hypersurface $\Sigma$ with $\overline{\Sigma}\setminus\Sigma\neq\emptyset$ inside $W$, stationarity of $[\Sigma]$ tests vector fields that do not vanish near $\overline{\Sigma}\setminus\Sigma$ and is strictly stronger than minimality of $\Sigma$ (an open half-hyperplane is minimal, but its varifold is not stationary in $\mathbb{R}^N$). This is how [2023, 197(3), no. 4] uses it: "minimal" there means that the multiplicity-one varifold of the embedded hypersurface $M\subseteq\mathbb{R}^{n+m+\ell}$ (with its singular closure points $\{0\}\times\{0\}\times K$) is stationary for the metric $g=\sum dx_i^2+f\sum d\xi_j^2+\sum dy_k^2$. [2023, 198(3), no. 2] works with stationary integral $n$-varifolds in $B_1\subseteq\mathbb{R}^{n+1}$ (Euclidean), varifold convergence, tangent cones as above, and "regular away from $0$" meaning $\operatorname{sing}V\subseteq\{0\}$. In min-max theory one often embeds $M$ isometrically in some $\mathbb{R}^L$ and regards varifolds in $M$ as varifolds in $\mathbb{R}^L$ supported in $M$, stationarity being tested on vector fields tangent to $M$; this agrees with the intrinsic definition above.

## 54. Character variety of a surface group in a real reductive group

*Chapter context.* A chapter on representation varieties in a text on surface group representations and Higgs bundles. The reader knows fundamental groups of surfaces, Lie groups and Lie algebras, the adjoint representation, complex reductive Lie groups (equivalently, complex reductive linear algebraic groups, the complexifications of compact Lie groups) and complete reducibility of representations; real forms, reductive representations and the character variety are introduced here.

**Definition 54.1 (real forms).** Let $G$ be a connected complex reductive Lie group with Lie algebra $\mathfrak{g}$. A *real form* of $G$ is an anti-holomorphic involutive automorphism $\tau\colon G\to G$, or its fixed-point group $G^{\mathbb{R}}=G^\tau=\{g\in G:\tau(g)=g\}$, a closed real Lie subgroup (possibly disconnected) whose Lie algebra $\mathfrak{g}^{\mathbb{R}}=\mathfrak{g}^{d\tau}$ satisfies $\mathfrak{g}=\mathfrak{g}^{\mathbb{R}}\oplus i\,\mathfrak{g}^{\mathbb{R}}$. A *Cartan involution* for $\tau$ is a holomorphic involution $\sigma$ of $G$ with $\sigma\tau=\tau\sigma$ such that $G^{\sigma\tau}$ is compact; one exists, and $H^{\mathbb{R}}=G^{\mathbb{R}}\cap G^\sigma$ is a maximal compact subgroup of $G^{\mathbb{R}}$. In this chapter a *real reductive group* means such a $G^{\mathbb{R}}$; the definitions below apply verbatim to complex reductive groups (regarded as real Lie groups) and to compact Lie groups. Examples: $\mathrm{SL}_n\mathbb{R}$, $\mathrm{PSL}_2\mathbb{R}$, $\mathrm{SO}_{p,q}$, $\mathrm{Sp}_{2n}\mathbb{R}$, $\mathrm{SU}_{p,q}$.

Throughout, $\Sigma$ is a closed connected orientable surface of genus $g\ge2$, $\pi_1\Sigma=\pi_1(\Sigma,x_0)$, and $G^{\mathbb{R}}=G^\tau$ is as above.

**Definition 54.2 (representation space).** $\operatorname{Hom}(\pi_1\Sigma,G^{\mathbb{R}})$ is the set of group homomorphisms $\rho\colon\pi_1\Sigma\to G^{\mathbb{R}}$ with the topology of pointwise convergence (the subspace topology of the product $\prod_{\gamma\in\pi_1\Sigma}G^{\mathbb{R}}$). Choosing standard generators, $\pi_1\Sigma=\langle a_1,b_1,\dots,a_g,b_g\mid\prod_{i=1}^g[a_i,b_i]\rangle$, the map $\rho\mapsto(\rho(a_1),\rho(b_1),\dots,\rho(a_g),\rho(b_g))$ is a homeomorphism onto the closed subset $\{(A_i,B_i)\in(G^{\mathbb{R}})^{2g}:\prod_{i=1}^g[A_i,B_i]=1\}$. The group $G^{\mathbb{R}}$ acts continuously by conjugation, $(h\cdot\rho)(\gamma)=h\,\rho(\gamma)\,h^{-1}$.

**Definition 54.3 (reductive representation).** A representation $\rho\in\operatorname{Hom}(\pi_1\Sigma,G^{\mathbb{R}})$ is *reductive* if the real representation $\operatorname{Ad}\circ\rho\colon\pi_1\Sigma\to\mathrm{GL}(\mathfrak{g}^{\mathbb{R}})$ is completely reducible, i.e. $\mathfrak{g}^{\mathbb{R}}$ is a direct sum of $\operatorname{Ad}\rho(\pi_1\Sigma)$-invariant subspaces each of which has no non-trivial proper invariant subspace. Write $\operatorname{Hom}^{\mathrm{red}}(\pi_1\Sigma,G^{\mathbb{R}})$ (also written $\operatorname{Hom}^+$) for the subset of reductive representations, with the subspace topology; it is $G^{\mathbb{R}}$-invariant.

**Proposition 54.4.** For $\rho\in\operatorname{Hom}(\pi_1\Sigma,G^{\mathbb{R}})$ the following are equivalent: (i) $\rho$ is reductive; (ii) the complex representation $\operatorname{Ad}\circ\rho$ on $\mathfrak{g}$ is completely reducible; (iii) the Zariski closure of $\rho(\pi_1\Sigma)$ in $G$ is a reductive (possibly disconnected) algebraic group; (iv) the orbit $G^{\mathbb{R}}\cdot\rho$ is closed in $\operatorname{Hom}(\pi_1\Sigma,G^{\mathbb{R}})$. ((i)$\Leftrightarrow$(ii)$\Leftrightarrow$(iii) is linear algebra over a field of characteristic $0$; (iii)$\Leftrightarrow$(iv) combines Richardson's theorem for $G$ acting on $G^{2g}$ with the fact that a real point has closed $G^{\mathbb{R}}$-orbit iff it has closed $G$-orbit, see Richardson–Slodowy, *Minimum vectors for real reductive algebraic groups*.) Moreover the orbit space of the reductive representations is Hausdorff (same reference).

**Definition 54.5 (character variety).** The *$G^{\mathbb{R}}$-character variety* of $\Sigma$ is the orbit space
$$\mathcal{X}(G^{\mathbb{R}})=\mathcal{X}(\Sigma,G^{\mathbb{R}})=\operatorname{Hom}^{\mathrm{red}}(\pi_1\Sigma,G^{\mathbb{R}})\big/G^{\mathbb{R}},$$
the set of $G^{\mathbb{R}}$-conjugacy classes $[\rho]$ of reductive representations, with the quotient topology from $\operatorname{Hom}^{\mathrm{red}}(\pi_1\Sigma,G^{\mathbb{R}})$. It is a Hausdorff topological space, independent of the base point $x_0$ up to canonical homeomorphism (changing base point composes $\rho$ with an inner automorphism of $\pi_1\Sigma$, which does not change $[\rho]$).

*Remarks.* Despite the name, $\mathcal{X}(G^{\mathbb{R}})$ is treated as a topological space; for complex $G$ it is (the space of complex points of) the affine GIT quotient $\operatorname{Hom}(\pi_1\Sigma,G)/\!\!/G$, each fibre of $\operatorname{Hom}\to\operatorname{Hom}/\!\!/G$ containing exactly one closed orbit. Restricting to reductive representations is what makes the quotient Hausdorff: e.g. in $\operatorname{Hom}(\pi_1\Sigma,\mathrm{SL}_2\mathbb{R})$ a non-trivial representation into the upper unipotent matrices has the trivial representation in its orbit closure. Some authors instead use all representations and the non-Hausdorff quotient, or quotient only the irreducible ones; these differ from Definition 54.5. In [2024, 200(3), no. 1], $G$ is complex simple, $G^{\mathbb{R}}$ is the canonical real form attached to a magical $\mathfrak{sl}_2$-triple, $\mathcal{X}(G^{\mathbb{R}})$ is exactly Definition 54.5 (their Definition 8.1, using the adjoint representation on $\mathfrak{g}^{\mathbb{R}}$), Teichmüller space appears as the Fuchsian (discrete faithful) classes in $\mathcal{X}(\mathrm{PSL}_2\mathbb{R})$, and the non-abelian Hodge correspondence identifies $\mathcal{X}(G^{\mathbb{R}})$ homeomorphically with the moduli space of polystable $G^{\mathbb{R}}$-Higgs bundles. The centraliser of $\rho$ is $Z_{G^{\mathbb{R}}}(\rho)=\{h\in G^{\mathbb{R}}:h\rho(\gamma)h^{-1}=\rho(\gamma)\ \forall\gamma\}$; parabolic subgroups are Definition #4.

## 55. Gaussian $q$-cluster

*Chapter context.* A chapter on weighted isoperimetric problems in a text on sets of finite perimeter. The reader knows the standard Gaussian measure, sets of (locally) finite perimeter in $\mathbb{R}^n$, the perimeter measure $|D\chi_E|$, the reduced boundary $\partial^*E$ and De Giorgi's structure theorem $|D\chi_E|=\mathcal{H}^{n-1}\llcorner\partial^*E$; Gaussian perimeter and clusters are introduced here.

Throughout, $n\ge1$, $\gamma=\gamma^n$ is the standard Gaussian probability measure $d\gamma=e^{-W(x)}dx$ on $\mathbb{R}^n$ with $W(x)=\frac{|x|^2}{2}+\frac n2\log(2\pi)$ (so $\nabla W(x)=x$), and $\gamma^{n-1}:=e^{-W}\mathcal{H}^{n-1}$ is the Gaussian-weighted $(n-1)$-dimensional Hausdorff measure.

**Definition 55.1 (Gaussian perimeter).** For a Borel set $U\subseteq\mathbb{R}^n$,
$$P_\gamma(U)=\sup\Big\{\int_U\big(\operatorname{div}X-\langle\nabla W,X\rangle\big)\,d\gamma\;:\;X\in C_c^\infty(\mathbb{R}^n;\mathbb{R}^n),\ |X|\le1\text{ pointwise}\Big\}\in[0,\infty].$$

**Proposition 55.2.** Since $(\operatorname{div}X-\langle\nabla W,X\rangle)e^{-W}=\operatorname{div}(e^{-W}X)$, $P_\gamma(U)$ is the total variation of $D\chi_U$ weighted by $e^{-W}$. Consequently: if $P_\gamma(U)<\infty$ then $U$ has locally finite perimeter and $P_\gamma(U)=\int e^{-W}\,d|D\chi_U|=\gamma^{n-1}(\partial^*U)$; $P_\gamma(U)=\gamma^{n-1}(\partial U)$ for open $U$ with Lipschitz boundary; $P_\gamma(U)=P_\gamma(U')$ whenever $\gamma(U\triangle U')=0$; $P_\gamma(\mathbb{R}^n\setminus U)=P_\gamma(U)$; and $P_\gamma$ is lower semicontinuous under $L^1(\gamma)$-convergence of indicator functions.

**Definition 55.3 (Gaussian $q$-cluster).** Let $q\ge2$ be an integer. A *$q$-cluster* (in Gaussian space) is a $q$-tuple $\Omega=(\Omega_1,\dots,\Omega_q)$ of Borel sets $\Omega_i\subseteq\mathbb{R}^n$, the *cells*, such that

1. the cells are pairwise disjoint: $\Omega_i\cap\Omega_j=\emptyset$ for $i\ne j$;
2. $P_\gamma(\Omega_i)<\infty$ for every $i$;
3. they cover $\mathbb{R}^n$ up to a null set: $\gamma\big(\mathbb{R}^n\setminus\bigcup_{i=1}^q\Omega_i\big)=0$.

Cells need not be connected and may be empty. The *total Gaussian perimeter* of $\Omega$ is the number $P_\gamma(\Omega)=\frac12\sum_{i=1}^qP_\gamma(\Omega_i)$, and its *Gaussian measure* is the vector
$$\gamma(\Omega)=(\gamma(\Omega_1),\dots,\gamma(\Omega_q))\in\Delta^{(q-1)}:=\Big\{v\in\mathbb{R}^q:v_i\ge0,\ \sum_{i=1}^qv_i=1\Big\}.$$
Two clusters $\Omega,\Omega'$ *agree up to null sets* if $\gamma(\Omega_i\triangle\Omega'_i)=0$ for all $i$; then $P_\gamma(\Omega)=P_\gamma(\Omega')$ and $\gamma(\Omega)=\gamma(\Omega')$.

**Proposition 55.4 (interfaces).** For a $q$-cluster put $\Sigma_{ij}=\partial^*\Omega_i\cap\partial^*\Omega_j$ ($i\ne j$). Then $\mathcal{H}^{n-1}$-almost every point of $\partial^*\Omega_i$ lies in $\Sigma_{ij}$ for exactly one $j\ne i$, so $P_\gamma(\Omega_i)=\sum_{j\ne i}\gamma^{n-1}(\Sigma_{ij})$ and $P_\gamma(\Omega)=\sum_{1\le i<j\le q}\gamma^{n-1}(\Sigma_{ij})$ (cf. Maggi, *Sets of Finite Perimeter and Geometric Variational Problems*, chapter on clusters). In particular, for $q=2$, $P_\gamma(\Omega)=P_\gamma(\Omega_1)=P_\gamma(\Omega_2)$.

**Definition 55.5 (isoperimetric profile; simplicial clusters).** The *Gaussian isoperimetric profile for $q$-clusters* is $I^{(q-1)}\colon\Delta^{(q-1)}\to[0,\infty)$, $I^{(q-1)}(v)=\inf\{P_\gamma(\Omega):\Omega\text{ a $q$-cluster in }\mathbb{R}^n,\ \gamma(\Omega)=v\}$; a cluster attaining the infimum is an *isoperimetric minimiser*. For $2\le q\le n+1$, let $x_1,\dots,x_q\in\mathbb{R}^n$ be *equidistant* ($|x_i-x_j|$ the same positive number for all $i\ne j$). Their Voronoi cells
$$\Omega_i=\operatorname{int}\{x\in\mathbb{R}^n:|x-x_i|=\min_{1\le j\le q}|x-x_j|\},\qquad i=1,\dots,q,$$
form a $q$-cluster, called a *simplicial $q$-cluster*. For every $v\in\operatorname{int}\Delta^{(q-1)}$ there is a simplicial cluster with $\gamma(\Omega)=v$, and all such have the same perimeter (they differ by orthogonal maps of $\mathbb{R}^n$); this defines the *model profile* $I^{(q-1)}_m(v)$, which extends continuously to $\Delta^{(q-1)}$.

*Remarks.* Each cell of a simplicial cluster is a convex polyhedral cone with vertex $c=\frac1q\sum_ix_i$, invariant under translations orthogonal to the affine span of the $x_i$; scaling the $x_i$ about $c$ does not change the cells, so they are determined by $c$ and the unit vectors $(x_i-c)/|x_i-c|$. For $q=2$ they are complementary half-spaces, for $q=3$ a "tripod" whose three half-hyperplane interfaces meet at $120^\circ$ angles. Many sources (e.g. Maggi) define clusters as tuples of disjoint finite-measure sets with an unconstrained exterior chamber; in the Gaussian setting the measure is finite and all $q$ cells, including the "exterior" one, are listed, so $q$ cells correspond to $q-1$ bubbles. In [2022, 195(1), no. 2] the Gaussian Multi-Bubble Theorem states $I^{(q-1)}=I^{(q-1)}_m$ on $\Delta^{(q-1)}$ for $2\le q\le n+1$, and simplicial clusters are, up to null sets, the unique minimisers for $v\in\operatorname{int}\Delta^{(q-1)}$.

## 56. Linearized Cauchy–Riemann operator at a J-holomorphic curve

*Chapter context.* A chapter on the local theory of moduli spaces in a text on pseudoholomorphic curves. The reader knows almost complex and symplectic manifolds, closed Riemann surfaces, $J$-holomorphic maps, pullback bundles and connections, Sobolev spaces $W^{k,p}$ of sections over a closed surface, Fredholm operators and the first Chern class; real Cauchy–Riemann operators and the linearization at a $J$-holomorphic curve are introduced here.

Throughout, $(\Sigma,j)$ is a closed connected Riemann surface, $(M,J)$ is a smooth almost complex manifold of real dimension $2n$, and for a complex vector bundle $(E,J_E)\to\Sigma$ we write $\Omega^{0,1}(\Sigma,E)=\Gamma(\overline{\operatorname{Hom}}_{\mathbb{C}}(T\Sigma,E))$ for the smooth complex-antilinear $E$-valued $1$-forms, i.e. $\alpha\circ j=-J_E\circ\alpha$. For a smooth map $u\colon\Sigma\to M$, the nonlinear Cauchy–Riemann operator is
$$\bar\partial_J(u)=du+J(u)\circ du\circ j\in\Omega^{0,1}(\Sigma,u^*TM),$$
and $u$ is *$J$-holomorphic* iff $\bar\partial_J(u)=0$.

**Definition 56.1 (real Cauchy–Riemann operators).** Let $(E,J_E)\to\Sigma$ be a smooth complex vector bundle of complex rank $m$. A *(real) Cauchy–Riemann operator* on $E$ is an $\mathbb{R}$-linear map $D\colon\Gamma(E)\to\Omega^{0,1}(\Sigma,E)$ satisfying the Leibniz rule
$$D(f\eta)=(\bar\partial f)\,\eta+f\,D\eta\qquad\text{for all }f\in C^\infty(\Sigma,\mathbb{R}),\ \eta\in\Gamma(E),$$
where $(\bar\partial f)\eta$ denotes the form $X\mapsto df(X)\,\eta+df(jX)\,J_E\eta$. Such $D$ is a first-order differential operator; the set of all of them is an affine space over $\Gamma(\operatorname{Hom}_{\mathbb{R}}(E,\overline{\operatorname{Hom}}_{\mathbb{C}}(T\Sigma,E)))$ (zeroth-order terms), and $D$ is *complex-linear* if $D(J_E\eta)=J_ED\eta$.

**Proposition 56.2 (Riemann–Roch).** Every real Cauchy–Riemann operator $D$ on $E$ extends to a bounded Fredholm operator $W^{k,p}(\Sigma,E)\to W^{k-1,p}(\Sigma,\overline{\operatorname{Hom}}_{\mathbb{C}}(T\Sigma,E))$ for all integers $k\ge1$ and $p\in(1,\infty)$, whose kernel and cokernel consist of smooth sections and are independent of $(k,p)$, and
$$\operatorname{ind}_{\mathbb{R}}D=m\,\chi(\Sigma)+2\langle c_1(E),[\Sigma]\rangle .$$
(See McDuff–Salamon, *J-holomorphic Curves and Symplectic Topology*.)

**Definition 56.3 (linearized operator).** Let $u\colon(\Sigma,j)\to(M,J)$ be $J$-holomorphic. The *linearized Cauchy–Riemann operator* at $u$ is the $\mathbb{R}$-linear operator
$$D_u\colon\Gamma(u^*TM)\to\Omega^{0,1}(\Sigma,u^*TM),\qquad D_u\eta=\nabla\eta+J(u)\circ\nabla\eta\circ j+(\nabla_\eta J)\circ du\circ j,$$
where $\nabla$ is any torsion-free connection on $TM$, $\nabla\eta\in\Omega^1(\Sigma,u^*TM)$ is the covariant derivative of $\eta$ with respect to the pullback connection, and $(\nabla_\eta J)(z)=(\nabla_{\eta(z)}J)\in\operatorname{End}(T_{u(z)}M)$.

**Proposition 56.4 (well-definedness).** (a) For any smooth family of maps $u_t\colon\Sigma\to M$, $t\in(-\varepsilon,\varepsilon)$, with $u_0=u$ and $\partial_tu_t|_{t=0}=\eta$, and any connection $\tilde\nabla$ on $TM$, one has $D_u\eta=\tilde\nabla_t\big(\bar\partial_J(u_t)\big)\big|_{t=0}$, the covariant $t$-derivative of the family of sections $\bar\partial_J(u_t)$ of $\overline{\operatorname{Hom}}_{\mathbb{C}}(T\Sigma,u_t^*TM)$. Because $\bar\partial_J(u_0)=0$ the right side does not depend on $\tilde\nabla$; hence $D_u$ is independent of the torsion-free $\nabla$ in 56.3, and it is the vertical differential at the zero $u$ of the section $\bar\partial_J$ of the Banach bundle of $W^{k-1,p}$ antilinear forms over the Banach manifold $W^{k,p}(\Sigma,M)$, $kp>2$. (b) $D_u$ takes values in $\Omega^{0,1}(\Sigma,u^*TM)$ and is a real Cauchy–Riemann operator on the complex bundle $(u^*TM,J(u))$; it is complex-linear if $J$ is integrable. By 56.2, $\operatorname{ind}_{\mathbb{R}}D_u=n\chi(\Sigma)+2\langle c_1(TM,J),u_*[\Sigma]\rangle$.

*Remarks.* Conventions differ by a factor: many texts (e.g. McDuff–Salamon) use $\bar\partial_J(u)=\frac12(du+J\circ du\circ j)$ and then $D_u$ is half of the operator above; kernels, cokernels and indices are unaffected (their zeroth-order term $-\frac12J(\nabla_\eta J)\partial_J(u)$ agrees with half of ours at a $J$-holomorphic $u$). If $\nabla J=0$ for the chosen torsion-free $\nabla$ (e.g. the Levi-Civita connection of a Kähler metric) the last term vanishes. A $J$-holomorphic curve $u$ is usually called *regular* (for fixed $j$) if $D_u$ is surjective; for the moduli space $\mathcal{M}_g(A,J)$ of unparametrized curves with varying domain, the virtual dimension is $\operatorname{ind}(u)=(n-3)\chi(\Sigma)+2\langle c_1(TM,J),[u]\rangle$, i.e. $\operatorname{ind}D_u+(6g-6)$ with $g$ the genus of $\Sigma$, where $6g-6=-3\chi(\Sigma)$ accounts for varying $j$ (Teichmüller space) modulo reparametrizations, and *Fredholm regularity* (transversality of the section cutting out $\mathcal{M}_g(A,J)$) is implied by surjectivity of $D_u$. For a multiple cover $\tilde u=u\circ\varphi$ with $\varphi\colon(\tilde\Sigma,\tilde\jmath)\to(\Sigma,j)$ holomorphic, $D_{\tilde u}$ is the pullback $\varphi^*D_u$, characterised by $(\varphi^*D_u)(\eta\circ\varphi)=\varphi^*(D_u\eta)$. These are the conventions of [2023, 198(1), no. 2] (Wendl), where $D_u$ is restricted to the generalized normal bundle to give the normal Cauchy–Riemann operator $\mathbf{D}^N_u$ (Definition #60); super-rigidity and Fredholm regularity are phrased in terms of it.

## 57. Lipschitz singular chains and their mass

*Chapter context.* A chapter on filling invariants in a text on geometric group theory or metric geometry. The reader knows singular chain complexes with integer coefficients, Lipschitz maps between metric spaces, Hausdorff measure, Rademacher's theorem and the area formula, and Riemannian manifolds and (locally finite, piecewise Euclidean) simplicial complexes viewed as metric spaces; Lipschitz chains, their mass and filling volumes are introduced here.

Throughout, $(Y,\mathsf{d})$ is a metric space and $d\ge0$ an integer. $\Delta^d=\{t\in\mathbb{R}^{d+1}:t_i\ge0,\ \sum_it_i=1\}$ is the standard $d$-simplex with the Euclidean metric, and $\delta_i\colon\Delta^{d-1}\to\Delta^d$ ($0\le i\le d$) are the affine face maps (inserting $0$ in position $i$). $\mathcal{H}^d$ denotes the $d$-dimensional Hausdorff measure on $Y$, *normalised* so that on Euclidean $\mathbb{R}^d$ it equals Lebesgue measure, i.e. for $A\subseteq Y$, $\mathcal{H}^d(A)=\lim_{\varepsilon\to0}\inf\{\sum_k\omega_d(\operatorname{diam}A_k/2)^d:A\subseteq\bigcup_kA_k,\ \operatorname{diam}A_k<\varepsilon\}$ (countable covers), $\omega_d$ the volume of the Euclidean unit $d$-ball.

**Definition 57.1 (Lipschitz chains).** A *Lipschitz $d$-simplex* in $Y$ is a Lipschitz map $\sigma\colon\Delta^d\to Y$. The group $C^{\mathrm{Lip}}_d(Y)$ of *Lipschitz $d$-chains* is the free abelian group on the set of Lipschitz $d$-simplices, i.e. the subgroup of the singular chain group $C_d(Y;\mathbb{Z})$ spanned by them. Every $\alpha\in C^{\mathrm{Lip}}_d(Y)$ has a unique expression $\alpha=\sum_{k=1}^mc_k\sigma_k$ with $m\ge0$, $c_k\in\mathbb{Z}\setminus\{0\}$ and pairwise distinct Lipschitz simplices $\sigma_k$. Since each $\delta_i$ is affine, the singular boundary
$$\partial\sigma=\sum_{i=0}^d(-1)^i\,\sigma\circ\delta_i$$
maps $C^{\mathrm{Lip}}_d(Y)$ to $C^{\mathrm{Lip}}_{d-1}(Y)$, so $(C^{\mathrm{Lip}}_\bullet(Y),\partial)$ is a subcomplex of the singular chain complex. A *Lipschitz cycle* is an $\alpha$ with $\partial\alpha=0$. The *support* of $\alpha$ is $\operatorname{supp}\alpha=\bigcup_k\sigma_k(\Delta^d)$.

**Definition 57.2 (volume and mass).** The *$d$-volume* of a Lipschitz simplex $\sigma\colon\Delta^d\to Y$ is
$$\operatorname{vol}_d(\sigma)=\int_Y\#\big(\sigma^{-1}(y)\big)\,d\mathcal{H}^d(y)\in[0,\infty),$$
the $\mathcal{H}^d$-measure of the image counted with multiplicity (finite, indeed at most $\operatorname{Lip}(\sigma)^d\mathcal{H}^d(\Delta^d)$). The *mass* of $\alpha=\sum_kc_k\sigma_k$ (unique expression as above) is
$$\operatorname{mass}\alpha=\sum_{k=1}^m|c_k|\operatorname{vol}_d(\sigma_k).$$
More generally, for a bounded Borel function $f$ on $Y$ put $\int_\alpha f=\sum_k|c_k|\int_Y f(y)\,\#\sigma_k^{-1}(y)\,d\mathcal{H}^d(y)$, so $\int_\alpha1=\operatorname{mass}\alpha$, and $\operatorname{mass}_Z\alpha=\int_\alpha\mathbf{1}_Z$ for Borel $Z\subseteq Y$.

**Proposition 57.3 (area formula).** If $Y$ is a Riemannian manifold (or a piecewise Euclidean simplicial complex, simplex by simplex), a Lipschitz $\sigma\colon\Delta^d\to Y$ is differentiable at almost every $x$ in the interior of $\Delta^d$, and
$$\operatorname{vol}_d(\sigma)=\int_{\Delta^d}J\sigma(x)\,dx,\qquad J\sigma(x)=\sqrt{\det\big(D\sigma_x^{*}D\sigma_x\big)},$$
where $dx$ is $d$-dimensional Lebesgue measure on the affine hyperplane containing $\Delta^d$ and $D\sigma_x$ is the derivative from its tangent space $\{\sum_it_i=0\}$ to $T_{\sigma(x)}Y$. For a general metric space the same holds with $J\sigma$ the Jacobian of Kirchheim's metric differential (B. Kirchheim, *Rectifiable metric spaces: local structure and regularity of the Hausdorff measure*). By Definition 57.2 itself, $\operatorname{vol}_d$ does not depend on the choice of affine model for the simplex; moreover $\operatorname{mass}(\alpha+\beta)\le\operatorname{mass}\alpha+\operatorname{mass}\beta$ and $\operatorname{mass}(f_\#\alpha)\le\operatorname{Lip}(f)^d\operatorname{mass}\alpha$ for Lipschitz $f\colon Y\to Y'$.

**Definition 57.4 (filling volume).** For a Lipschitz cycle $\alpha\in C^{\mathrm{Lip}}_{d-1}(Y)$, $d\ge1$, the *filling volume* is $\operatorname{FV}^d(\alpha)=\inf\{\operatorname{mass}\beta:\beta\in C^{\mathrm{Lip}}_d(Y),\ \partial\beta=\alpha\}\in[0,\infty]$ ($\inf\emptyset=\infty$), and the *$d$-dimensional filling volume function* of $Y$ is
$$\operatorname{FV}^d_Y(V)=\sup\{\operatorname{FV}^d(\alpha):\alpha\in C^{\mathrm{Lip}}_{d-1}(Y),\ \partial\alpha=0,\ \operatorname{mass}\alpha\le V\},\qquad V\ge0 .$$

*Remarks.* Mass is not a norm on chains: degenerate simplices (e.g. constant maps, or maps factoring through a lower-dimensional space) have volume $0$, and distinct simplices with the same image are not identified. Mathlib's `MeasureTheory.Measure.hausdorffMeasure` is unnormalised (built from $\operatorname{diam}^d$), so the $\mathcal{H}^d$ above is $\omega_d/2^d$ times it; it agrees with Lebesgue measure on $\iota\to\mathbb{R}$ with the sup metric (`hausdorffMeasure_pi_real`) but not on Euclidean $\mathbb{R}^d$ for $d\ge2$. For Riemannian manifolds and locally finite simplicial complexes the Lipschitz chains compute singular homology (standard), so $\operatorname{FV}^d(\alpha)<\infty$ for every Lipschitz $(d-1)$-cycle when $Y$ is $(d-1)$-connected. In [2021, 193(3), no. 2] $Y$ is a simplicial complex or Riemannian manifold (in practice the thick part $X_0$ of a symmetric space $X=G/K$), coefficients are integers, and $\operatorname{vol}_d\sigma=\int_{\Delta^d}|J\sigma|$ as in 57.3; $\operatorname{FV}^n_\Gamma$ and the Dehn function $\delta_\Gamma$ (defined with $\operatorname{vol}_2\beta=\int_{D^2}|J\beta|$ for Lipschitz discs $\beta$) are then defined via a $(d-1)$-connected $Y$ of bounded geometry with a geometric $\Gamma$-action, and are well defined only up to the equivalence $F\preceq F'$ iff $F(t)\le CF'(Ct+C)+Ct+C$ for some $C$; the asymptotics $\approx$ in the main theorems are read in that sense.

## 58. MCG-finite representation of a surface group

*Chapter context.* Chapter on representations of surface groups and the dynamics of the mapping class group on them, in a book on surface groups and their representations. Assumed known: the punctured surface $\Sigma_{g,n}$ and its mapping class group $\operatorname{Mod}_{g,n}$ (Definition #59), and the action of $\operatorname{Mod}_{g,n}$ on the set $\mathcal{X}_r$ of $\mathrm{GL}_r(\mathbb{C})$-conjugacy classes of representations $\pi_1(\Sigma_{g,n},x)\to\mathrm{GL}_r(\mathbb{C})$ (Definition #61). Recall that $\pi_1(\Sigma_{g,n},x)$ is finitely generated: it is free of rank $2g+n-1$ if $n\ge1$, and has the presentation $\langle a_1,b_1,\dots,a_g,b_g\mid \prod_i[a_i,b_i]\rangle$ if $n=0$.

**Definition 58.1.** Let $g,n,r\ge0$ be integers and $x\in\Sigma_{g,n}$. A *representation* is a group homomorphism $\rho\colon\pi_1(\Sigma_{g,n},x)\to\mathrm{GL}_r(\mathbb{C})$. It is *MCG-finite* if the orbit of its conjugacy class $[\rho]\in\mathcal{X}_r$ under the action of $\operatorname{Mod}_{g,n}$ of Definition #61 is finite:
$$\#\,\operatorname{Mod}_{g,n}\cdot[\rho]<\infty .$$
Unwinding: $\rho$ is MCG-finite if and only if the set
$$\Big\{\{P(\rho\circ f_\delta)P^{-1}:P\in\mathrm{GL}_r(\mathbb{C})\}\ :\ f\in\operatorname{Homeo}^+(\Sigma_{g,n}),\ \delta\text{ a path from }x\text{ to }f(x)\Big\}$$
of conjugacy classes is finite, where $f_\delta[\gamma]=[\delta\cdot(f\circ\gamma)\cdot\bar\delta]$. Equivalently (orbit–stabiliser), the stabiliser
$$\operatorname{Stab}[\rho]=\{[f]\in\operatorname{Mod}_{g,n}:\ \rho\circ f_\delta \text{ is } \mathrm{GL}_r(\mathbb{C})\text{-conjugate to }\rho\}$$
has finite index in $\operatorname{Mod}_{g,n}$.

**Proposition 58.2.** (a) Being MCG-finite depends only on the conjugacy class of $\rho$. It does not depend on the basepoint $x$, nor on the chosen model of $\Sigma_{g,n}$ (transport $\rho$ along the canonical identifications of Definition #61, Remarks).

(b) $\operatorname{Mod}_{g,n}$ may be replaced by any finite-index subgroup, e.g. the pure mapping class group $\operatorname{PMod}_{g,n}$, without changing the notion. Since every mapping class has a representative fixing $x$, $\rho$ is MCG-finite if and only if $\{[\rho\circ f_*]: f\in\operatorname{Homeo}^+(\Sigma_{g,n}),\ f(x)=x\}$ is finite.
(c) Every representation with finite image is MCG-finite. Indeed, if $H=\rho(\pi_1)$ is finite, then each $\rho\circ\varphi$ ($\varphi\in\operatorname{Aut}\pi_1$) is a homomorphism to $H$, and there are only finitely many such since $\pi_1$ is finitely generated.

*Remarks.*

- The condition is on conjugacy classes $[\rho]$, i.e. on points of the quotient set $\operatorname{Hom}(\pi_1,\mathrm{GL}_r(\mathbb{C}))/\mathrm{GL}_r(\mathbb{C})$ (isomorphism classes of rank-$r$ local systems). It is not a condition on points of the representation variety, on which $\operatorname{Mod}_{g,n}$ does not act. For semisimple $\rho$ it is the same as finiteness of the orbit of the corresponding point of the character variety, since closed orbits correspond to semisimple representations.
- Nothing about $\rho$ beyond being a homomorphism is assumed: it need not be irreducible or semisimple, and the cases $r=0$ and $(g,n)$ with $2g-2+n\le0$ are allowed (trivially or degenerately).
- Equivalent formulations used in [2024, 199(2), no. 6]: the conjugacy class of $\rho$ is fixed by a finite-index subgroup of $\operatorname{PMod}_{g,n}$, or of $\operatorname{PMod}_{g,n+1}\subset\operatorname{Aut}(\pi_1(\Sigma_{g,n},x))$ (point-pushing/Birman exact sequence). Theorem 1.2.1 there: for all $g,n,r\ge0$, an MCG-finite $\rho$ with $r<\sqrt{g+1}$ has finite image. By 58.2(c), in this range MCG-finite is therefore equivalent to finite image.
- For formalisation, 58.2(b) avoids paths: quantify over basepoint-fixing homeomorphisms and their induced automorphisms $f_*$ of $\pi_1(\Sigma_{g,n},x)$, and ask that $\{[\rho\circ f_*]\}$ be a finite subset of the quotient by conjugation.

## 59. Mapping class group of a punctured surface

*Chapter context.* Opening chapter on mapping class groups in a book on the topology of surfaces. The reader knows topological surfaces and the classification of closed surfaces, orientations of topological manifolds (via local homology) and orientation-preserving homeomorphisms, the compact-open topology, and isotopies; the surfaces $\Sigma_{g,n}$, their homeomorphism groups and mapping class groups are introduced here.

**Definition 59.1 (the punctured surface).** Let $g,n\ge 0$ be integers. Fix a closed (compact, without boundary) connected oriented topological surface $\Sigma_g$ of genus $g$ and a set $P\subset\Sigma_g$ of exactly $n$ points, the *punctures*. Put
$$\Sigma_{g,n}:=\Sigma_g\setminus P,$$
an oriented connected surface (non-compact if $n\ge 1$). Since $\Sigma_g$ is unique up to orientation-preserving homeomorphism (classification of surfaces), and the orientation-preserving homeomorphisms of $\Sigma_g$ act transitively on $n$-element subsets, $\Sigma_{g,n}$ is well defined up to orientation-preserving homeomorphism.

**Definition 59.2 (homeomorphisms and isotopy).** $\operatorname{Homeo}^+(\Sigma_{g,n})$ is the group, under composition, of orientation-preserving homeomorphisms $f\colon\Sigma_{g,n}\to\Sigma_{g,n}$. Two elements $f_0,f_1$ are *isotopic*, written $f_0\simeq f_1$, if there is a continuous map $H\colon \Sigma_{g,n}\times[0,1]\to\Sigma_{g,n}$ such that every $H_t:=H(\cdot,t)$ is a homeomorphism, $H_0=f_0$ and $H_1=f_1$. Put $\operatorname{Homeo}_0(\Sigma_{g,n}):=\{f : f\simeq \mathrm{id}\}$.

**Proposition 59.3.** (a) If $H$ is an isotopy and $H_0$ preserves orientation, then every $H_t$ does. (b) Isotopy is an equivalence relation on $\operatorname{Homeo}^+(\Sigma_{g,n})$, and if $f_0\simeq f_1$ and $h_0\simeq h_1$ then $f_0\circ h_0\simeq f_1\circ h_1$ and $f_0^{-1}\simeq f_1^{-1}$. (Continuity of $(y,t)\mapsto H_t^{-1}(y)$ follows from invariance of domain.) Hence $\operatorname{Homeo}_0(\Sigma_{g,n})$ is a normal subgroup of $\operatorname{Homeo}^+(\Sigma_{g,n})$, and $f\simeq f'$ if and only if $f^{-1}f'\in \operatorname{Homeo}_0(\Sigma_{g,n})$. (c) As $\Sigma_{g,n}$ is locally compact Hausdorff, isotopies are the same as continuous paths $[0,1]\to\operatorname{Homeo}^+(\Sigma_{g,n})$ for the compact-open topology; so isotopy classes are the path components of $\operatorname{Homeo}^+(\Sigma_{g,n})$.

**Proposition 59.4 (punctures as marked points).** Every $f\in\operatorname{Homeo}^+(\Sigma_{g,n})$ extends uniquely to a homeomorphism $\bar f$ of $\Sigma_g$; $\bar f$ preserves orientation and $\bar f(P)=P$. Restriction is an isomorphism from $\operatorname{Homeo}^+(\Sigma_g,P):=\{F\in\operatorname{Homeo}^+(\Sigma_g): F(P)=P\}$ onto $\operatorname{Homeo}^+(\Sigma_{g,n})$, and isotopies of $\Sigma_{g,n}$ correspond exactly to isotopies of $\Sigma_g$ through elements of $\operatorname{Homeo}^+(\Sigma_g,P)$. Along such an isotopy the induced permutation of $P$ is constant. (See Farb–Margalit, *A Primer on Mapping Class Groups*, Chapter 1.)

**Definition 59.5 (mapping class group).** The *mapping class group* of $\Sigma_{g,n}$ is the group
$$\operatorname{Mod}_{g,n}:=\operatorname{Homeo}^+(\Sigma_{g,n})\big/\operatorname{Homeo}_0(\Sigma_{g,n})=\pi_0\operatorname{Homeo}^+(\Sigma_{g,n}).$$
Its elements are isotopy classes $[f]$ (*mapping classes*), with product $[f][h]:=[f\circ h]$, identity $[\mathrm{id}]$ and inverse $[f]^{-1}=[f^{-1}]$. By Proposition 59.4 there is a homomorphism $\operatorname{Mod}_{g,n}\to\operatorname{Sym}(P)\cong S_n$, $[f]\mapsto \bar f|_P$. It is surjective, and its kernel is the *pure mapping class group* $\operatorname{PMod}_{g,n}$, a normal subgroup of index $n!$. Equivalently, $\operatorname{Mod}_{g,n}$ is the group of orientation-preserving homeomorphisms of $\Sigma_g$ preserving the set $P$, modulo isotopy through such homeomorphisms. A different choice of $(\Sigma_g,P)$ gives an isomorphic group: conjugation by an orientation-preserving homeomorphism gives the isomorphism, which is canonical up to inner automorphisms.

*Remarks.*

- For a formaliser, the marked-point model (Proposition 59.4) stays entirely within compact surfaces: take $\operatorname{Homeo}^+(\Sigma_g,P)$ modulo isotopy through homeomorphisms preserving $P$. One may also use diffeomorphisms and smooth isotopies of a smooth $\Sigma_g$, which gives an isomorphic group (Farb–Margalit, Chapter 1).
- Puncture permutations are allowed in $\operatorname{Mod}_{g,n}$. Orientation-reversing homeomorphisms are excluded; including them gives the extended group $\operatorname{Mod}^{\pm}_{g,n}\supset \operatorname{Mod}_{g,n}$ (index 2). Some authors use $S_{g,n}$ or $\Sigma_{g,n}$ for surfaces with $n$ *boundary components*. Then isotopies must fix the boundary pointwise, which gives a different group (it contains the boundary Dehn twists).
- Sanity checks: $\operatorname{Mod}_{0,0}$ and $\operatorname{Mod}_{0,1}$ are trivial, $\operatorname{Mod}_{0,2}\cong\mathbb{Z}/2$, $\operatorname{Mod}_{0,3}\cong S_3$, $\operatorname{Mod}_{1,0}\cong\mathrm{SL}_2(\mathbb{Z})$ (Farb–Margalit, Chapter 2).
- In [2024, 199(2), no. 6] (Landesman–Litt), $\operatorname{Mod}_{g,n}$ is exactly this group (all $g,n\ge0$, punctures may be permuted), and $\operatorname{PMod}_{g,n}=\pi_1(\mathscr{M}_{g,n})$ is the index-$n!$ pure subgroup. It acts on $\pi_1(\Sigma_{g,n},x)$ by outer automorphisms (Definition #61). Since $\operatorname{PMod}_{g,n}$ has finite index, finiteness of orbits is the same for $\operatorname{Mod}_{g,n}$ and $\operatorname{PMod}_{g,n}$.

## 60. Normal Cauchy–Riemann operator of a J-holomorphic curve

*Chapter context.* Chapter on transversality for closed $J$-holomorphic curves in a book on pseudoholomorphic curves in symplectic topology. Assumed known: almost complex manifolds, closed Riemann surfaces, $J$-holomorphic maps ($du\circ j=J\circ du$), complex vector bundles and their first Chern numbers, Sobolev completions of spaces of sections, and real linear Cauchy–Riemann operators with their Fredholm theory (Riemann–Roch). Also the linearized Cauchy–Riemann operator $\mathbf{D}_u$ of Definition #56.

*Setting.* $(M,J)$ is a smooth almost complex manifold of real dimension $2n$, $(\Sigma,j)$ a closed connected Riemann surface, and $u\colon\Sigma\to M$ a smooth nonconstant $J$-holomorphic map. For a complex vector bundle $(E,J_E)\to\Sigma$, $\Omega^{0,1}(\Sigma,E)$ denotes smooth sections of $\overline{\operatorname{Hom}}_{\mathbb{C}}(T\Sigma,E)=\{A\colon T_z\Sigma\to E_z \text{ real linear}: A\circ j=-J_E\circ A\}$. As in Definition #56 (normalised as in [2023, 198(1), no. 2]), $\mathbf{D}_u\colon\Gamma(u^*TM)\to\Omega^{0,1}(\Sigma,u^*TM)$ is the linearisation at $u$ of $\bar\partial_J(u)=du+J\circ du\circ j$ with $j$ fixed. For any symmetric connection $\nabla$ on $TM$,
$$\mathbf{D}_u\eta=\nabla\eta+J(u)\circ\nabla\eta\circ j+(\nabla_\eta J)\circ du\circ j .$$
It satisfies $\mathbf{D}_u(f\eta)=f\,\mathbf{D}_u\eta+df\otimes\eta+(df\circ j)\otimes J\eta$ for $f\in C^\infty(\Sigma,\mathbb{R})$.

**Proposition 60.1 (critical points; generalised tangent bundle).** (a) Each $du(z)$ is complex linear from a complex line, so it is either $0$ or injective. The critical set $\operatorname{Crit}(u)=\{z:du(z)=0\}$ is finite.

(b) There is a unique smooth $J$-complex line subbundle $T_u\subset u^*TM$ with $T_u(z)=\operatorname{im}du(z)$ for all $z\notin\operatorname{Crit}(u)$.
(c) $du$ is a section of $\operatorname{Hom}_{\mathbb{C}}(T\Sigma,T_u)$ whose zeros are isolated and of positive order. Writing $Z(du)\ge0$ for their algebraic count, $c_1(T_u)=\chi(\Sigma)+Z(du)$.
(See Wendl, *Automatic transversality and orbifolds of punctured holomorphic curves in dimension four*, Comment. Math. Helv. 2010, §3.3; cited as [Wen10, §3.3] in the paper.)

**Definition 60.2 (generalised normal bundle).** A *generalised normal bundle* of $u$ is a smooth $J$-invariant (complex) subbundle $N_u\subset u^*TM$, of complex rank $n-1$, with
$$u^*TM=T_u\oplus N_u .$$
$\pi_N\colon u^*TM\to N_u$ denotes the projection along $T_u$. It is complex linear. For example, one may take $N_u=T_u^{\perp}$ for any Hermitian metric on $(u^*TM,J)$, e.g. $\omega(\cdot,J\cdot)$ if $J$ is $\omega$-compatible. If $u$ is an immersion, $T_u=\operatorname{im}du$ and $N_u$ is a normal bundle in the usual sense. If $u=v\circ\varphi$ with $v$ an immersed $J$-holomorphic curve and $\varphi$ a holomorphic map of positive degree (possibly branched), then $T_u=\varphi^*T_v$ and one takes $N_u=\varphi^*N_v$.

**Proposition 60.3 (independence of the complement).** $\mathbf{D}_u$ maps $\Gamma(T_u)$ into $\Omega^{0,1}(\Sigma,T_u)$. Indeed, for vector fields $X$ on $\Sigma$ one has $\mathbf{D}_u(du(X))=du\circ\bar\partial X$, with $\bar\partial$ the natural Cauchy–Riemann operator of $(T\Sigma,j)$ (differentiate $\bar\partial_J(u\circ\phi_t)$ along the flow $\phi_t$ of $X$). With the Leibniz rule this gives the claim off $\operatorname{Crit}(u)$, and continuity gives it everywhere. Consequently, if $N_u,N'_u$ are two generalised normal bundles and $\psi=\pi_{N'}|_{N_u}\colon N_u\to N'_u$, then $\pi_{N'}\circ\mathbf{D}_u\circ\psi=\psi\circ\pi_N\circ\mathbf{D}_u$ on $\Gamma(N_u)$. Thus the operator below is canonically an operator on the quotient bundle $u^*TM/T_u$.

**Definition 60.4.** (a) The *normal Cauchy–Riemann operator* of $u$ (with respect to $N_u$) is
$$\mathbf{D}^N_u:=\pi_N\circ\mathbf{D}_u|_{\Gamma(N_u)}\colon\Gamma(N_u)\to\Omega^{0,1}(\Sigma,N_u),\qquad \eta\mapsto\pi_N\circ(\mathbf{D}_u\eta).$$
It is a real linear Cauchy–Riemann operator on $(N_u,J)$. For $k\in\mathbb{N}$ and $p\in(1,\infty)$ it extends to a bounded Fredholm operator $W^{k,p}(N_u)\to W^{k-1,p}(\overline{\operatorname{Hom}}_{\mathbb{C}}(T\Sigma,N_u))$ of index
$$\operatorname{ind}\mathbf{D}^N_u=(n-1)\chi(\Sigma)+2c_1(N_u)=\operatorname{ind}(u)-2Z(du),\qquad \operatorname{ind}(u):=(n-3)\chi(\Sigma)+2\langle c_1(TM,J),u_*[\Sigma]\rangle .$$
Its kernel consists of smooth sections and is independent of $(k,p)$, and so is surjectivity. A *nontrivial solution of the normal linearized equation* is $0\neq\eta\in\Gamma(N_u)$ with $\mathbf{D}^N_u\eta=0$.

(b) A closed connected *simple* $J$-holomorphic curve $u$ (nonconstant, and not of the form $v\circ\varphi$ with $\deg\varphi\ge2$) is *super-rigid* if: (1) $\operatorname{ind}(u)=0$; (2) $u$ is an immersion; (3) for every closed connected Riemann surface $(\widetilde\Sigma,\tilde\jmath)$ and every holomorphic $\varphi\colon\widetilde\Sigma\to\Sigma$ of positive degree, $\ker\mathbf{D}^N_{u\circ\varphi}=0$, where $N_{u\circ\varphi}=\varphi^*N_u$.

*Remarks.*

- By Proposition 60.3, $\ker\mathbf{D}^N_u$, $\operatorname{coker}\mathbf{D}^N_u$ and the index are independent of the choice of $N_u$. An overall factor (some authors use $\tfrac12(du+J\,du\,j)$) or the choice of symmetric connection does not change $\mathbf{D}_u$ at a $J$-holomorphic $u$ beyond scaling. Some sources (Ivashkovich–Shevchishin, Wendl) define the normal operator directly on $u^*TM/T_u$.
- $u$ is *Fredholm regular* (transversely cut out in the moduli space of unparametrised curves) if and only if $\mathbf{D}^N_u$ is surjective for some, equivalently all, $(k,p)$ ([2023, 198(1), no. 2, Prop. 2.2], from [Wen10, Cor. 3.13]). The tangential part of $\mathbf{D}_u$ only accounts for reparametrisations and variations of $j$.
- In [2023, 198(1), no. 2] (Wendl), $\dim M=2n\ge4$, $J$ is $\omega$-compatible, and $\mathbf{D}^N$ is applied to multiple covers $\tilde u=u\circ\varphi$ of immersed simple curves, so $N_{\tilde u}=\varphi^*N_u$. Then $Z(d\tilde u)=Z(d\varphi)$ is the number of branch points of $\varphi$ counted with multiplicity, and it vanishes for unbranched covers (Theorem B). Theorem A uses (b).

## 61. Outer action of the mapping class group on the fundamental group

*Chapter context.* Chapter on mapping class groups and surface groups in a book on the topology of surfaces. The reader knows fundamental groups and change of basepoint, path homotopy and the lemma comparing $H_0\circ\gamma$ and $H_1\circ\gamma$ for a homotopy $H$, group automorphisms, and representations of groups. The surface $\Sigma_{g,n}$ and $\operatorname{Mod}_{g,n}$ are Definition #59. Here we construct the outer action and the induced action on conjugacy classes of representations.

*Conventions.* For paths $\alpha,\beta$ with $\alpha(1)=\beta(0)$, $\alpha\cdot\beta$ traverses $\alpha$ first; $\bar\alpha(t)=\alpha(1-t)$. For a group $\Gamma$ and $h\in\Gamma$, $c_h(\gamma)=h\gamma h^{-1}$.

**Definition 61.1 (outer automorphisms).** For a group $\Gamma$, $\operatorname{Inn}(\Gamma)=\{c_h:h\in\Gamma\}$ is a normal subgroup of $\operatorname{Aut}(\Gamma)$, since $\varphi\circ c_h\circ\varphi^{-1}=c_{\varphi(h)}$. The *outer automorphism group* is $\operatorname{Out}(\Gamma):=\operatorname{Aut}(\Gamma)/\operatorname{Inn}(\Gamma)$.

**Proposition 61.2.** Let $X$ be a path-connected space, $x\in X$, $\pi=\pi_1(X,x)$. For a homeomorphism $f\colon X\to X$ and a path $\delta$ from $x$ to $f(x)$, define
$$f_\delta\colon \pi\to\pi,\qquad [\gamma]\mapsto[\delta\cdot(f\circ\gamma)\cdot\bar\delta].$$
(a) $f_\delta\in\operatorname{Aut}(\pi)$. For another such path $\delta'$, $f_{\delta'}=c_{[\delta'\cdot\bar\delta]}\circ f_\delta$.
(b) For homeomorphisms $f,h$ and paths $\delta_f$ (from $x$ to $f(x)$), $\delta_h$ (from $x$ to $h(x)$): $(f\circ h)_{\delta_f\cdot(f\circ\delta_h)}=f_{\delta_f}\circ h_{\delta_h}$.
(c) If $H$ is a homotopy (in particular an isotopy) from $f_0$ to $f_1$ and $\beta(t)=H_t(x)$, then $(f_1)_{\delta\cdot\beta}=(f_0)_\delta$.
Hence the class $\langle f\rangle:=f_\delta\operatorname{Inn}(\pi)\in\operatorname{Out}(\pi)$ is independent of $\delta$, depends only on the isotopy class of $f$, and $\langle f\circ h\rangle=\langle f\rangle\langle h\rangle$. If $f(x)=x$, then $\langle f\rangle$ is the class of the induced automorphism $f_*$ (take $\delta$ constant).

**Lemma 61.3.** Every $f\in\operatorname{Homeo}^+(\Sigma_{g,n})$ is isotopic to an element of $\operatorname{Homeo}^+(\Sigma_{g,n},x):=\{f: f(x)=x\}$. (Push $f(x)$ back to $x$ along a path by a homeomorphism isotopic to the identity.)

**Definition 61.4 (outer action; action on representations).** Let $g,n\ge0$ and $x\in\Sigma_{g,n}$.

(a) The *outer action* of the mapping class group is the group homomorphism
$$\Psi\colon\operatorname{Mod}_{g,n}\to\operatorname{Out}\big(\pi_1(\Sigma_{g,n},x)\big),\qquad [f]\mapsto\langle f\rangle=f_\delta\operatorname{Inn}(\pi_1(\Sigma_{g,n},x)),$$
for any representative $f\in\operatorname{Homeo}^+(\Sigma_{g,n})$ and any path $\delta$ from $x$ to $f(x)$. It is well defined by Proposition 61.2. By Lemma 61.3 one may instead take $f(x)=x$ and $\Psi[f]=[f_*]$.

(b) For $r\ge0$ let $\mathcal{R}_r:=\operatorname{Hom}\big(\pi_1(\Sigma_{g,n},x),\mathrm{GL}_r(\mathbb{C})\big)$, the set of group homomorphisms. $\mathrm{GL}_r(\mathbb{C})$ acts on it by $(P\cdot\rho)(\gamma)=P\rho(\gamma)P^{-1}$. The orbit $[\rho]$ is the *conjugacy class* of $\rho$, and $\mathcal{X}_r:=\mathcal{R}_r/\mathrm{GL}_r(\mathbb{C})$ is the set of conjugacy classes. $\operatorname{Aut}(\pi_1)$ acts on $\mathcal{R}_r$ on the left by $\varphi\cdot\rho:=\rho\circ\varphi^{-1}$, commuting with conjugation. Since $\rho\circ c_h^{-1}=\rho(h)^{-1}\cdot\rho$, inner automorphisms act trivially on $\mathcal{X}_r$, so $\operatorname{Out}(\pi_1)$ acts on $\mathcal{X}_r$. Composing with $\Psi$ gives the *action of $\operatorname{Mod}_{g,n}$ on conjugacy classes of representations*:
$$[f]\cdot[\rho]:=\big[\rho\circ f_\delta^{-1}\big]\qquad([f]\in\operatorname{Mod}_{g,n},\ \rho\in\mathcal{R}_r).$$

*Remarks.*

- Basepoint: a path $\tau$ from $x$ to $x'$ gives an isomorphism $\pi_1(\Sigma_{g,n},x')\to\pi_1(\Sigma_{g,n},x)$, $[\gamma]\mapsto[\tau\cdot\gamma\cdot\bar\tau]$, which is well defined up to inner automorphisms. So the induced identifications of $\operatorname{Out}$ and of $\mathcal{X}_r$ are canonical and intertwine the two actions. This is why [2024, 199(2), no. 6] writes $\pi_1(\Sigma_{g,n})$ without a basepoint.
- $\operatorname{Mod}_{g,n}$ does not act on $\mathcal{R}_r$ itself, only on $\mathcal{X}_r$. The group that does act on $\pi_1(\Sigma_{g,n},x)$ by genuine automorphisms is the mapping class group of $(\Sigma_{g,n},x)$, i.e. with $x$ as an extra marked point. Its pure version is $\operatorname{PMod}_{g,n+1}\subset\operatorname{Aut}(\pi_1(\Sigma_{g,n},x))$, which the paper uses via the Birman exact sequence.
- Using $\rho\mapsto\rho\circ f_\delta$ gives the corresponding right action, with the same orbits. The same construction applied to all homeomorphisms gives $\operatorname{Mod}^{\pm}_{g,n}\to\operatorname{Out}(\pi_1)$. By the Dehn–Nielsen–Baer theorem and its version for punctured surfaces (Farb–Margalit, *A Primer on Mapping Class Groups*, Chapter 8), $\Psi$ is injective when $2g-2+n>0$.
- Lean: Mathlib has $\operatorname{Aut}$ as `MulAut` and conjugation `MulAut.conj`, so $\operatorname{Inn}$ is the range of `MulAut.conj` and $\operatorname{Out}$ is the quotient by this normal subgroup. Using Lemma 61.3, $\Psi$ can be defined on basepoint-fixing representatives.

## 62. Riemannian symmetric space of a semisimple Lie group

*Chapter context.* Chapter on symmetric spaces of non-compact type in a book on Lie groups and their geometry. Assumed known: real semisimple Lie algebras and the Killing form $B(X,Y)=\operatorname{tr}(\operatorname{ad}X\operatorname{ad}Y)$ (non-degenerate by Cartan's criterion), Lie groups and closed subgroups, homogeneous manifolds $G/H$, Riemannian metrics, geodesics and Riemannian distance. Cartan involutions, the Cartan decomposition and the symmetric space $G/K$ are introduced here.

Throughout, $G$ is a connected real Lie group with semisimple Lie algebra $\mathfrak{g}$ and finite centre $Z(G)$ (e.g. centre-free).

**Definition 62.1 (Cartan involution).** A *Cartan involution* of $\mathfrak{g}$ is a Lie algebra automorphism $\theta$ with $\theta^2=\mathrm{id}$ such that $B_\theta(X,Y):=-B(X,\theta Y)$ is positive definite. Its $(\pm1)$-eigenspaces give the *Cartan decomposition* $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$. Then $[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k}$, $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$, $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}$, $B(\mathfrak{k},\mathfrak{p})=0$, $B$ is negative definite on $\mathfrak{k}$ and positive definite on $\mathfrak{p}$.

**Theorem 62.2 (Cartan).** (a) Cartan involutions of $\mathfrak{g}$ exist, and any two are conjugate by an inner automorphism of $\mathfrak{g}$.

(b) Let $K$ be the connected Lie subgroup with Lie algebra $\mathfrak{k}$. Then $K$ is closed, contains $Z(G)$, is compact and is a maximal compact subgroup of $G$. The map $\mathfrak{p}\times K\to G$, $(Y,k)\mapsto\exp(Y)k$, is a diffeomorphism.
(c) Every compact subgroup of $G$ lies in a conjugate of $K$. Every maximal compact subgroup $K'$ is $gKg^{-1}$ for some $g$, and is the group $K$ attached to the unique Cartan involution with $\mathfrak{p}'=(\mathfrak{k}')^{\perp_B}$.
(Knapp, *Lie Groups Beyond an Introduction*, Ch. VI; Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Ch. III and VI.)

**Proposition 62.3 (the invariant metric).** Let $K\le G$ be a maximal compact subgroup with Lie algebra $\mathfrak{k}$, put $\mathfrak{p}:=\mathfrak{k}^{\perp_B}$, $X:=G/K$, $o:=eK$, and let $\pi\colon G\to X$ be the projection. Then $d\pi_e|_{\mathfrak{p}}\colon\mathfrak{p}\to T_oX$ is an isomorphism. Under it, the isotropy action of $k\in K$ on $T_oX$ is $\operatorname{Ad}(k)|_{\mathfrak{p}}$. Since $B|_{\mathfrak{p}}$ is positive definite and $\operatorname{Ad}(K)$-invariant, there is a unique Riemannian metric $g_X$ on $X$ that is invariant under the left action $h\cdot(aK)=haK$ of $G$ and satisfies
$$g_X\big(d\pi_e Y,d\pi_e Z\big)_o=B(Y,Z)\qquad(Y,Z\in\mathfrak{p}).$$
Explicitly, $(g_X)_{h\cdot o}(dL_h u,dL_h v)=B\big((d\pi_e|_{\mathfrak{p}})^{-1}u,(d\pi_e|_{\mathfrak{p}})^{-1}v\big)$ for $u,v\in T_oX$.

**Proposition 62.4.** $(X,g_X)$ is complete, simply connected, and has sectional curvature $\le0$: for a $B$-orthonormal pair $Y,Z\in\mathfrak{p}$ the curvature of the plane they span at $o$ is $B([Y,Z],[Y,Z])\le0$. For $Y\in\mathfrak{p}$ the curve $t\mapsto\exp(tY)\cdot o$ is a geodesic, and every geodesic through $o$ is of this form. Hence $X\cong\mathfrak{p}$ via $Y\mapsto\exp(Y)\cdot o$, and
$$d_X(g\cdot o,h\cdot o)=B(Y,Y)^{1/2}\quad\text{where } g^{-1}h=\exp(Y)k,\ Y\in\mathfrak{p},\ k\in K .$$

**Definition 62.5.** (a) The *Riemannian symmetric space* of $G$ is the Riemannian manifold $(X,g_X)=(G/K,g_X)$ of Proposition 62.3, with base point $o=eK$ and the isometric left action of $G$. Here $K$ is a maximal compact subgroup and the metric is induced by the Killing form on $\mathfrak{p}=\mathfrak{k}^{\perp_B}$. The geodesic symmetry at $o$, $aK\mapsto\Theta(a)K$ with $\Theta$ the automorphism of $G$ integrating $\theta$, is an isometry with differential $-\mathrm{id}$ at $o$.

(b) Its *distance function* $d_X\colon X\times X\to[0,\infty)$ is the Riemannian distance: $d_X(p,q)$ is the infimum of the lengths $\int_0^1 g_X(\dot c,\dot c)^{1/2}dt$ of piecewise $C^1$ paths $c$ from $p$ to $q$. It is $G$-invariant and given by the formula in 62.4.
(c) For a discrete subgroup $\Lambda\le G$ (which acts properly discontinuously on $X$, as $K$ is compact) and $p\in\Lambda\backslash X$ with a lift $\tilde p\in X$, the *injectivity radius* is
$$\operatorname{InjRad}_{\Lambda\backslash X}(p):=\tfrac12\min_{\gamma\in\Lambda\setminus\{1\}}d_X(\tilde p,\gamma\tilde p)\in[0,\infty],$$
with the convention that it equals $\infty$ if $\Lambda=\{1\}$. The minimum exists by proper discontinuity and is independent of the lift.

*Remarks.*

- Choices: a different maximal compact $K'=hKh^{-1}$ gives a $G$-equivariant isometry $G/K\to G/K'$, $aK\mapsto ah^{-1}K'$. Since $Z(G)\subseteq K$, $X=\operatorname{Ad}(G)/\operatorname{Ad}(K)$ depends only on $\mathfrak{g}$. If $G$ is centre-free and has no compact factors (e.g. simple non-compact, as in [2023, 197(1), no. 6]), $G$ acts faithfully on $X$.
- Normalisation: $B|_{\mathfrak{p}}$ equals $B_\theta|_{\mathfrak{p}}$. Other sources use a trace form, or rescale each simple factor so that the minimal curvature is $-1$. If $\mathfrak{g}$ is simple, $\operatorname{Ad}(K)$ acts irreducibly on $\mathfrak{p}$, so every $G$-invariant metric on $X$ is a constant multiple of $g_X$. For $G=\mathrm{SL}_n(\mathbb{R})$, $B(Y,Z)=2n\operatorname{tr}(YZ)$, and $\mathrm{SL}_2(\mathbb{R})/\mathrm{SO}(2)$ is the hyperbolic plane with curvature $-\tfrac12$.
- The real rank of $G$ (Definition #1), $\dim\mathfrak{a}$ for a maximal abelian $\mathfrak{a}\subseteq\mathfrak{p}$, equals the maximal dimension of a flat totally geodesic submanifold of $X$.
- If $\Lambda$ is torsion-free, $\Lambda\backslash X$ is a complete locally symmetric manifold, and since $X$ has no conjugate points, 62.5(c) is its usual Riemannian injectivity radius. With torsion, $\Lambda\backslash X$ is an orbifold, and (c) is the definition used (it vanishes at singular points). "Infinite covolume" ($G/\Lambda$ of infinite Haar measure) is equivalent to $\operatorname{vol}(\Lambda\backslash X)=\infty$. Theorem 1.1 of [2023, 197(1), no. 6] is invariant under rescaling the metric, so the normalisation of $B$ is immaterial there.

## 63. Space of compatible almost complex structures

*Chapter context.* Chapter on almost complex structures and genericity in a book on symplectic topology and $J$-holomorphic curves. Assumed known: symplectic manifolds $(M,\omega)$, almost complex structures (smooth sections $J$ of $\operatorname{End}(TM)$ with $J^2=-\mathrm{1}$), Riemannian metrics and connections, smooth sections of vector bundles with their $C^k$ seminorms over compact sets, Fréchet spaces, and the Baire category theorem.

Throughout, $(M,\omega)$ is a symplectic manifold of dimension $2n$ (second countable, without boundary, not necessarily compact).

**Definition 63.1 (tame and compatible).** An almost complex structure $J$ on $M$ is *$\omega$-tame* if $\omega(v,Jv)>0$ for all $x\in M$ and $0\neq v\in T_xM$. It is *$\omega$-compatible* if it is $\omega$-tame and $\omega(Jv,Jw)=\omega(v,w)$ for all $v,w\in T_xM$, $x\in M$. Equivalently, $g_J(v,w):=\omega(v,Jw)$ is a Riemannian metric, i.e. symmetric and positive definite: given $J^2=-\mathrm{1}$, symmetry of $g_J$ is equivalent to $J$-invariance of $\omega$, and positivity to tameness.

**Definition 63.2 (the $C^\infty$ topology).** Fix an auxiliary Riemannian metric $h$ on $M$ and let $\nabla$ be the induced connection on the tensor bundles. For $A\in\Gamma(\operatorname{End}TM)$, a compact $K\subseteq M$ and $k\ge0$ put
$$\|A\|_{C^k(K)}:=\max_{0\le i\le k}\ \sup_{x\in K}\ |\nabla^iA(x)|_h .$$
The *$C^\infty$ topology* on $\Gamma(\operatorname{End}TM)$ is the locally convex topology defined by these seminorms, for all compact $K$ and all $k$. It is independent of $h$. A sequence converges if and only if, in local charts, all partial derivatives of all matrix entries converge uniformly on compact subsets of chart domains. With this topology $\Gamma(\operatorname{End}TM)$ is a Fréchet space.

**Definition 63.3.** (a) $\mathcal{J}(M,\omega)$ is the set of smooth $\omega$-compatible almost complex structures on $M$ with the subspace topology from Definition 63.2. (Likewise $\mathcal{J}_\tau(M,\omega)\supseteq\mathcal{J}(M,\omega)$ is the space of smooth $\omega$-tame ones.)

(b) Let $J_{\mathrm{fix}}\in\mathcal{J}(M,\omega)$ and let $\mathcal{U}\subseteq M$ be an open subset with compact closure $\overline{\mathcal{U}}$. Then
$$\mathcal{J}(M,\omega;\mathcal{U},J_{\mathrm{fix}}):=\{J\in\mathcal{J}(M,\omega): J(x)=J_{\mathrm{fix}}(x)\ \text{for all }x\in M\setminus\mathcal{U}\},$$
with the subspace topology (the "natural $C^\infty$ topology").

**Proposition 63.4.** (a) For $J,J'\in\mathcal{J}(M,\omega;\mathcal{U},J_{\mathrm{fix}})$ the difference $J-J'$ vanishes on $M\setminus\mathcal{U}$. So the topology is given by the metric
$$d(J,J')=\sum_{k\ge0}2^{-k}\min\big\{1,\ \|J-J'\|_{C^k(\overline{\mathcal{U}})}\big\},$$
and it agrees with the restriction of the strong (Whitney) $C^\infty$ topology.

(b) $\mathcal{J}(M,\omega;\mathcal{U},J_{\mathrm{fix}})$ is a closed subset of the complete affine space $J_{\mathrm{fix}}+\{A\in\Gamma(\operatorname{End}TM):A|_{M\setminus\mathcal{U}}=0\}$. The conditions $J^2=-\mathrm{1}$ and $J^*\omega=\omega$ are closed. A limit of compatible $J$'s has $g_J$ positive semidefinite and nondegenerate, hence positive definite. Therefore $(\mathcal{J}(M,\omega;\mathcal{U},J_{\mathrm{fix}}),d)$ is a complete metric space, in particular a Baire space. The same holds for $\mathcal{J}(M,\omega)$ with the topology of 63.2.
(c) $\mathcal{J}(M,\omega)$ and $\mathcal{J}(M,\omega;\mathcal{U},J_{\mathrm{fix}})$ are nonempty and contractible. A fibrewise convex parametrisation of the compatible structures on a symplectic vector space (Cayley transform) gives a contraction to $J_{\mathrm{fix}}$ that fixes $M\setminus\mathcal{U}$; see McDuff–Salamon, *Introduction to Symplectic Topology*.

*Remarks.*

- *Baire subsets, genericity.* Following [2023, 198(1), no. 2], a *Baire subset* of a topological space is a countable intersection of open dense subsets (a set containing one is called comeagre). Theorems in [2023, 198(1), no. 2] produce a Baire subset $\mathcal{J}^{\mathrm{reg}}\subseteq\mathcal{J}(M,\omega;\mathcal{U},J_{\mathrm{fix}})$. Countable intersections of Baire subsets are Baire, and by 63.4(b) and the Baire category theorem they are dense. "For generic $J$" means "for all $J$ in some Baire subset".
- That paper takes $\dim M=2n\ge4$, $J_{\mathrm{fix}}$ smooth and $\omega$-compatible, and $\mathcal{U}$ open with compact closure. Its Remark 1.3 notes that the results hold equally for tame $J$, or for arbitrary almost complex structures on a manifold without symplectic form; the definitions are the same with the compatibility condition changed or dropped. If $M$ is closed one may take $\mathcal{U}=M$, giving $\mathcal{J}(M,\omega)$.
- On non-compact $M$, the weak topology (63.2) and the strong (Whitney) $C^\infty$ topology on $\mathcal{J}(M,\omega)$ differ. The compactness of $\overline{\mathcal{U}}$ is what makes the choice irrelevant in (b).
- Sign conventions relating $\omega$, $J$ and the metric differ between sources ($\omega(\cdot,J\cdot)$ versus $\omega(J\cdot,\cdot)$, which amounts to replacing $\omega$ by $-\omega$); the paper uses $g_J=\omega(\cdot,J\cdot)$, so care is needed when matching with a library. Tau Ceti's `TauCeti.SmoothAlmostComplexStructure` and `TauCeti.SmoothTwoForm.Compatible` give the underlying set; only the topology of 63.2 has to be added.

## 64. Spin$^c$ structure on an oriented manifold

*Chapter context.* Chapter on $\mathrm{Spin}^c$ structures in a book on low-dimensional topology and gauge or Floer theory. Assumed known: the groups $\mathrm{Spin}(n)\subset\mathrm{Cl}_n$ and the double cover $\lambda\colon\mathrm{Spin}(n)\to\mathrm{SO}(n)$ with kernel $\{\pm1\}$, principal bundles and associated bundles, the oriented orthonormal frame bundle, Stiefel–Whitney classes, the classification of principal $U(1)$-bundles by $c_1\in H^2(-;\mathbb{Z})$, and the boundary orientation convention ("outward normal first").

**Definition 64.1 (the group).** For $n\ge1$ put $\mathrm{Spin}^c(n):=\big(\mathrm{Spin}(n)\times U(1)\big)/\{(1,1),(-1,-1)\}$, with elements written $[a,z]$. It has homomorphisms
$$\lambda^c\colon[a,z]\mapsto\lambda(a)\in\mathrm{SO}(n),\qquad \det\colon[a,z]\mapsto z^2\in U(1).$$
$(\lambda^c,\det)$ is a double cover of $\mathrm{SO}(n)\times U(1)$, and $\ker\lambda^c=\{[1,z]\}\cong U(1)$ is central. The inclusion $\mathrm{Cl}_{n-1}\to\mathrm{Cl}_n$, $e_i\mapsto e_{i+1}$, induces $\mathrm{Spin}^c(n-1)\hookrightarrow\mathrm{Spin}^c(n)$ covering $A\mapsto\operatorname{diag}(1,A)$.

**Definition 64.2 (main).** Let $M$ be an oriented smooth $n$-manifold, possibly with boundary, with a Riemannian metric $g$. Let $F=F_{\mathrm{SO}}(M,g)\to M$ be the principal $\mathrm{SO}(n)$-bundle of positively oriented orthonormal frames. A *$\mathrm{Spin}^c$ structure* on $M$ is a pair $(P,\Phi)$ consisting of a principal $\mathrm{Spin}^c(n)$-bundle $P\to M$ and a smooth map $\Phi\colon P\to F$ covering $\mathrm{id}_M$ with
$$\Phi(p\cdot b)=\Phi(p)\cdot\lambda^c(b)\qquad(p\in P,\ b\in\mathrm{Spin}^c(n)).$$
Two such pairs $(P,\Phi)$, $(P',\Phi')$ are *isomorphic* if there is a $\mathrm{Spin}^c(n)$-equivariant bundle isomorphism $\psi\colon P\to P'$ over $\mathrm{id}_M$ with $\Phi'\circ\psi=\Phi$. $\operatorname{Spin}^c(M)$ denotes the set of isomorphism classes. The *determinant line bundle* is $\det(P):=P\times_{\det}U(1)$, and the *first Chern class* of $\mathfrak{s}=[(P,\Phi)]$ is $c_1(\mathfrak{s}):=c_1(\det P)\in H^2(M;\mathbb{Z})$.

**Proposition 64.3.** (a) (*Metric independence.*) For metrics $g_0,g_1$ there is a canonical bijection $\operatorname{Spin}^c(M,g_0)\cong\operatorname{Spin}^c(M,g_1)$: restrict structures on $M\times[0,1]$ with the metric $(1-t)g_0+tg_1$ to the two ends. It is compatible with everything below, so we write $\operatorname{Spin}^c(M)$.

(b) (*Existence.*) $\operatorname{Spin}^c(M)\ne\emptyset$ if and only if $w_2(TM)$ is the mod 2 reduction of an integral class. In particular every oriented manifold of dimension $\le4$ admits $\mathrm{Spin}^c$ structures (for closed 4-manifolds this is due to Hirzebruch–Hopf).
(c) (*Affine structure.*) Let $\mathfrak{s}=[(P,\Phi)]$ and let $Q$ be a principal $U(1)$-bundle with $c_1(Q)=a$. Put $P_Q:=(P\times_MQ)/U(1)$, where $w\in U(1)$ acts by $(p,q)\mapsto(p\cdot[1,w],q\cdot w^{-1})$, with the induced $\mathrm{Spin}^c(n)$-action and $\Phi_Q[p,q]=\Phi(p)$. Setting $\mathfrak{s}+a:=[(P_Q,\Phi_Q)]$ defines a free and transitive action of $H^2(M;\mathbb{Z})$ on $\operatorname{Spin}^c(M)$ (when nonempty). Moreover $\det P_Q\cong\det P\otimes Q^{\otimes2}$, so $c_1(\mathfrak{s}+a)=c_1(\mathfrak{s})+2a$, and $c_1(\mathfrak{s})\equiv w_2(TM)\pmod 2$.
(d) (*Restriction.*) Restriction to an open subset or to a codimension-0 submanifold is pullback. Let $N\subset M$ be a hypersurface with unit normal field $\nu$, oriented so that $(\nu,e_1,\dots,e_{n-1})$ is positive in $M$ exactly when $(e_1,\dots,e_{n-1})$ is positive in $N$. Let $\iota_\nu\colon F_{\mathrm{SO}}(N)\to F|_N$, $(e_i)\mapsto(\nu,e_1,\dots,e_{n-1})$. Then $\Phi^{-1}(\iota_\nu F_{\mathrm{SO}}(N))\subset P|_N$ is a principal $\mathrm{Spin}^c(n-1)$-bundle, and together with $\Phi$ it defines $\mathfrak{s}|_N\in\operatorname{Spin}^c(N)$. For $N=\partial M$ take $\nu$ outward. For a cobordism $W$ from $Y_1$ to $Y_2$ ($\partial W=-Y_1\sqcup Y_2$) take $\nu$ inward at $Y_1$ and outward at $Y_2$. Restriction is equivariant for $H^2(M)\to H^2(N)$, and $c_1(\mathfrak{s}|_N)=c_1(\mathfrak{s})|_N$.

**Proposition 64.4 (three-manifolds: Turaev's model).** Let $Y$ be a closed oriented 3-manifold. Call nowhere-vanishing vector fields $v,w$ on $Y$ *homologous* if, for some open 3-ball $B$ in each component of $Y$, $v|_{Y\setminus B}$ and $w|_{Y\setminus B}$ are homotopic through nowhere-vanishing vector fields. A unit field $v$ reduces $F$ to $F_v=\{(v,e_2,e_3)\}$, an $\mathrm{SO}(2)=U(1)$-bundle. The homomorphism $U(1)\to\mathrm{SO}(3)\times U(1)$, $z\mapsto(\operatorname{diag}(1,R_z),z)$, with $R_z$ the rotation by $\arg z$, lifts uniquely to $\sigma\colon U(1)\to\mathrm{Spin}^c(3)$. Then $\mathfrak{s}_v:=F_v\times_\sigma\mathrm{Spin}^c(3)$ has $c_1(\mathfrak{s}_v)=c_1(v^\perp)$, where the 2-plane field $v^\perp$ is oriented so that $(v,e_2,e_3)$ is positive. The map $v\mapsto\mathfrak{s}_v$ induces a bijection from homology classes of nowhere-vanishing vector fields onto $\operatorname{Spin}^c(Y)$ (Turaev, *Torsion invariants of Spin$^c$-structures on 3-manifolds*, Math. Res. Lett. 1997).

*Remarks.*

- Metric-free variant: $\mathrm{Spin}^c$ structures are equivalently lifts of the oriented frame bundle $F_{\mathrm{GL}^+}(M)$ along $(\widetilde{\mathrm{GL}}{}^+_n\times U(1))/\{\pm(1,1)\}\to\mathrm{GL}^+_n$, with $\widetilde{\mathrm{GL}}{}^+_n$ the connected double cover ($n\ge2$).
- $\mathfrak{s}\mapsto c_1(\mathfrak{s})$ has image the classes reducing to $w_2$ mod 2, and it is injective if and only if $H^2(M;\mathbb{Z})$ has no 2-torsion. An almost complex structure $J$ determines a canonical $\mathfrak{s}_J$ with $c_1(\mathfrak{s}_J)=c_1(TM,J)$. Conjugation $\bar{\mathfrak{s}}$ satisfies $c_1(\bar{\mathfrak{s}})=-c_1(\mathfrak{s})$.
- In [2025, 201(1), no. 1] (Manolescu–Ozsváth–Thurston), $\mathrm{Spin}^c$ structures are used on closed 3-manifolds $S^3_\Lambda(L)$, identified there with the quotient $\mathbb{H}(L)/H(L,\Lambda)$ of an affine lattice by the lattice spanned by the framing vectors. They are also used on 2-handle cobordisms $W_\Lambda(L',L)$, with restriction to both ends as in 64.3(d), and on closed oriented 4-manifolds $X$ with $b_2^+(X)>1$, with restrictions to the pieces $W_1,W_2$ and to the cut $N$. The quantities used there are $c_1(\mathfrak{u})$ and $d(\mathfrak{u})=\gcd_{\xi\in H_2}\langle c_1(\mathfrak{u}),\xi\rangle$, and $c_1(\mathfrak{t})^2$ in the grading shift $(c_1(\mathfrak{t})^2-2\chi(X)-3\sigma(X))/4$.

## 65. Strict stability of a minimal cone/hypersurface (Simon's inequality)

*Chapter context.* Chapter on stability of singular minimal hypersurfaces and minimal cones in a book on geometric measure theory and minimal surfaces. Assumed known: the second fundamental form $A_M$ and its norm $|A_M|$ (Definition #49, with its conventions), minimal hypersurfaces and the second variation of area (Definition #52), stationary varifolds (Definition #53), Hausdorff measure, and the tangential gradient on a submanifold.

*Setting.* $N\ge2$, $U\subseteq\mathbb{R}^{N+1}$ is open, and $M\subset U$ is a smooth embedded hypersurface: an $N$-dimensional smooth embedded submanifold of $\mathbb{R}^{N+1}$ contained in $U$, not necessarily closed in $U$. Write $\operatorname{sing}M:=(U\cap\overline{M})\setminus M$, assuming as in the source that every point of $U\cap\overline M$ near which $\overline M$ is a smooth embedded hypersurface already lies in $M$. Let $\mu=\mathcal{H}^N\llcorner M$ (Euclidean $N$-dimensional Hausdorff measure on $M$, equal to the Riemannian measure of the induced metric). Assume $M$ has locally finite area: $\mu(M\cap K)<\infty$ for compact $K\subset U$ (automatic if $M$ is stationary as a multiplicity-one varifold in $U$). For $\zeta\in C^1(U)$, $\nabla_M\zeta(X)$ is the orthogonal projection of $D\zeta(X)$ onto $T_XM$. Further, $|A_M|^2(X)=\sum_{i,j}A_M(\tau_i,\tau_j)^2$ for an orthonormal basis $(\tau_i)$ of $T_XM$, i.e. the sum of squares of the principal curvatures. It is independent of the local choice of unit normal, so $M$ need not be orientable. Finally fix a continuous *weight* $\tilde r\colon\mathbb{R}^{N+1}\to[0,\infty)$ that is positive on $M$.

**Definition 65.1 (stability form).** For $\zeta\in C^1_c(U)$ put
$$Q_M(\zeta):=\int_M\big(|\nabla_M\zeta|^2-|A_M|^2\zeta^2\big)\,d\mu .$$
If $M$ is minimal and two-sided with unit normal $\nu$, and $\zeta$ vanishes near $\operatorname{sing}M$, then $Q_M(\zeta)=\frac{d^2}{dt^2}\big|_{t=0}\mu(M_t)$ for $M_t=\{X+t\zeta(X)\nu(X):X\in M\}$.

**Definition 65.2.** (a) $M$ is *stable* if $\int_M|A_M|^2\zeta^2\,d\mu\le\int_M|\nabla_M\zeta|^2\,d\mu$ for all $\zeta\in C^\infty_c(U)$.

(b) $M$ is *strictly stable* (with respect to the weight $\tilde r$) if there is a constant $\kappa=\kappa(M)>0$ such that for every $\zeta\in C^\infty_c(U)$
$$\kappa\int_M\big(|\nabla_M\zeta|^2+\tilde r^{-2}\zeta^2\big)\,d\mu\ \le\ \int_M\big(|\nabla_M\zeta|^2-|A_M|^2\zeta^2\big)\,d\mu .\tag{S}$$
To avoid $\infty-\infty$, (S) is read as $\int_M|A_M|^2\zeta^2\,d\mu+\kappa\int_M(|\nabla_M\zeta|^2+\tilde r^{-2}\zeta^2)\,d\mu\le\int_M|\nabla_M\zeta|^2\,d\mu$, with all terms in $[0,\infty]$ and the right side finite. The test functions are *not* required to vanish near $\operatorname{sing}M$. Necessarily $\kappa\le1$.

(c) The two standard weights are: for a cone with vertex $0$, $\tilde r(X)=|X|$; for $\mathbb{R}^{N+1}=\mathbb{R}^n\times\mathbb{R}^m\times\mathbb{R}^\ell$ with points $(x,\xi,y)$, $\tilde r(x,\xi,y)=|x|+|\xi|$. The latter is comparable to the distance to the axis $\{0\}\times\{0\}\times\mathbb{R}^\ell$, which lies between $\tilde r/\sqrt2$ and $\tilde r$.

**Proposition 65.3.** (a) If $|A_M|^2\le C\tilde r^{-2}$ on $M$, then $M$ is strictly stable if and only if there is $\lambda>0$ with $Q_M(\zeta)\ge\lambda\int_M\tilde r^{-2}\zeta^2\,d\mu$ for all $\zeta$. Indeed the weak inequality gives $(1+C/\lambda)Q_M(\zeta)\ge\int_M|\nabla_M\zeta|^2$, so (S) holds with $\kappa=\frac12\min\{\lambda,(1+C/\lambda)^{-1}\}$.

(b) Let $N\ge3$ and let $\mathbf{C}=\{t\omega:t>0,\ \omega\in\Sigma\}$ be a minimal cone over a closed embedded minimal hypersurface $\Sigma\subset S^N$, with $\tilde r=|X|$. Then $|A_{\mathbf C}|^2(X)=|X|^{-2}|A_\Sigma|^2(X/|X|)$. By separation of variables and the sharp Hardy inequality, $\mathbf C$ is strictly stable if and only if $\lambda_1+\big(\tfrac{N-2}{2}\big)^2>0$, where $\lambda_1$ is the lowest eigenvalue of $-\Delta_\Sigma-|A_\Sigma|^2$ on $\Sigma$. It is stable if and only if $\lambda_1+\big(\tfrac{N-2}{2}\big)^2\ge0$. For example, the Simons cone $\{|x|=|\xi|\}\subset\mathbb{R}^4\times\mathbb{R}^4$ has $\lambda_1=-6>-\tfrac{25}{4}$, so it is strictly stable.

*Remarks.*

- (S) is homogeneous of degree $N-2$ under dilations when $\tilde r$ is 1-homogeneous, so $\kappa$ is scale-invariant. By density, $C^\infty_c$ may be replaced by $C^1_c$ test functions, provided $\int_{M\cap K}\tilde r^{-2}\,d\mu<\infty$ for compact $K$. This holds e.g. when $\operatorname{sing}M$ lies in the axis, which has codimension $\ge3$ in $M$, and $M$ has the area bounds of a stationary varifold.
- (S) uses Euclidean quantities even if $M$ is minimal for another metric. For a Riemannian metric $g$ the second variation is $\int_M\big(|\nabla^g_M\zeta|^2-(|A^g_M|^2+\operatorname{Ric}_g(\nu,\nu))\zeta^2\big)d\mu_g$, and the $g$-version of strict stability replaces $Q_M$ by this.
- In [2023, 197(3), no. 4] (Simon): $N+1=n+m+\ell$ with $n\ge3$, $m\ge2$, $n+m\ge8$, $\ell\ge1$; $U=\mathbb{R}^{n+m+\ell}$; $\tilde r=|x|+|\xi|$; and $\mu$ is $(n+m+\ell-1)$-dimensional Euclidean Hausdorff measure. $M$ is minimal (stationary) for $g=\sum dx_i^2+f(x,y)\sum d\xi_j^2+\sum dy_k^2$ but not for the Euclidean metric. "Strictly stable" means (S) (the paper's inequality (1.2)), which differs from the $g$-second variation by at most $C\tau\int_M(\tilde r^{-2}\zeta^2+|\nabla_M\zeta|^2)\,d\mu$; so (S) gives strict stability for $g$ when $\tau$ is small. The cones there are $\mathbf C_0=\{(n-1)|\xi|^2=(m-1)|x|^2\}$ and $\mathbf C_0\times\mathbb{R}^\ell$. Localised versions of (S) on $M\cap\{|y_j|<R\}$ with $\zeta\in C^1_c$ also appear in the paper.

## 66. Strictly convex boundary of a Riemannian manifold

*Chapter context.* Chapter on Riemannian manifolds with boundary (geodesics near the boundary, boundary normal coordinates) in a book on Riemannian geometry and geometric inverse problems. Assumed known: smooth manifolds with boundary, Riemannian metrics smooth up to the boundary, the Levi-Civita connection, Hessians, and the second fundamental form of a hypersurface (Definition #49) with its sign convention $A(X,Y)=\langle\nabla_X\nu,Y\rangle$, under which the unit sphere in $\mathbb{R}^{n}$ with its outward normal has $A$ equal to the induced metric.

Throughout, $(M,g)$ is a smooth Riemannian manifold of dimension $n\ge2$ with nonempty boundary $\partial M$, and $\nabla$ is its Levi-Civita connection. $\partial M$ is a smooth embedded hypersurface, and $\nu_{\mathrm{out}}$, $\nu_{\mathrm{in}}=-\nu_{\mathrm{out}}$ are the outward and inward unit normal fields along $\partial M$. Here $\nu_{\mathrm{in}}(p)$ is the unit vector orthogonal to $T_p\partial M$ pointing into $M$.

**Definition 66.1 (second fundamental form of the boundary).** For $p\in\partial M$ and $X,Y\in T_p\partial M$, let $\mathrm{I\!I}_p(X,Y)$ be the second fundamental form of the hypersurface $\partial M$ (Definition #49) computed with the *outward* unit normal. Equivalently, it is the scalar second fundamental form with respect to the *inward* normal in the "$\langle\nabla_XY,\nu\rangle$" convention:
$$\mathrm{I\!I}_p(X,Y)=\big\langle\nabla_X\nu_{\mathrm{out}},Y\big\rangle=\big\langle\nabla_X\tilde Y,\ \nu_{\mathrm{in}}\big\rangle(p),$$
where $\tilde Y$ is any vector field tangent to $\partial M$ along $\partial M$ with $\tilde Y(p)=Y$. This is a smooth symmetric 2-tensor on $\partial M$. It depends only on $g$ near $\partial M$.

**Proposition 66.2 (computations).** (a) If $\rho\in C^\infty(M)$ is a boundary defining function ($\rho>0$ on $M\setminus\partial M$, $\rho=0$ and $d\rho\ne0$ on $\partial M$), then
$$\mathrm{I\!I}_p(X,Y)=-\frac{\operatorname{Hess}_g\rho\,(X,Y)}{|d\rho|_g}\qquad(X,Y\in T_p\partial M),\qquad \operatorname{Hess}_g\rho(X,Y)=X(Y\rho)-(\nabla_XY)\rho .$$
(b) In boundary normal coordinates, $g=dr^2+h_r$ near $\partial M$, with $r$ the distance to $\partial M$ and $h_r$ a family of metrics on $\partial M$. There $\mathrm{I\!I}=-\tfrac12\,\partial_rh_r|_{r=0}$.
(c) Suppose $M\subset\widetilde M$ with $g$ extended smoothly to an open manifold $\widetilde M$, and $\rho$ extended. If $\gamma$ is a $\widetilde M$-geodesic with $\gamma(0)=p\in\partial M$ and $\dot\gamma(0)=v\in T_p\partial M$, then $(\rho\circ\gamma)''(0)=-|d\rho|_g\,\mathrm{I\!I}_p(v,v)$.

**Definition 66.3.** Let $p\in\partial M$.

- $\partial M$ is *strictly convex at $p$* (with respect to $g$) if $\mathrm{I\!I}_p$ is positive definite: $\mathrm{I\!I}_p(X,X)>0$ for all $0\ne X\in T_p\partial M$.
- $\partial M$ is *convex at $p$* if $\mathrm{I\!I}_p$ is positive semidefinite, and *strictly concave at $p$* if $\mathrm{I\!I}_p$ is negative definite.
- $\partial M$ is *strictly convex* (everywhere) if it is strictly convex at every $p\in\partial M$.

Equivalently, by 66.2(a), $\partial M$ is strictly convex at $p$ if and only if $\operatorname{Hess}_g\rho|_{T_p\partial M}$ is negative definite for one, equivalently every, boundary defining function $\rho$. By 66.2(c), every geodesic of $\widetilde M$ tangent to $\partial M$ at $p$ then leaves $M$ to second order, i.e. $\rho(\gamma(t))<0$ for small $t\ne0$.

*Remarks.*

- Strict convexity at $p$ is an open condition on $\partial M$ (by continuity it holds near $p$). If $\partial M$ is compact and strictly convex, then $\mathrm{I\!I}\ge c\,g|_{\partial M}$ for some $c>0$. The notion depends on the metric, which is why [2021, 194(1), no. 1] assumes it separately for $g$ and $\hat g$. Example: the closed unit ball in $\mathbb{R}^n$ has $\mathrm{I\!I}=g|_{S^{n-1}}$, so it is strictly convex.
- Sign conventions: authors using $\mathrm{I\!I}(X,Y)=\langle\nabla_XY,\nu\rangle$ take $\nu$ inward, and authors using $\langle\nabla_X\nu,Y\rangle$ (as in Definition #49) take $\nu$ outward. Both give the same form 66.1, so "positive definite second fundamental form with respect to the inward normal" in the first convention means the same as positivity in Definition #49 with the outward normal. The stated test is that balls in $\mathbb{R}^n$ are strictly convex.
- In [2021, 194(1), no. 1] (Stefanov–Uhlmann–Vasy), $n\ge3$, metrics are smooth, and "strictly convex" means positive definite second fundamental form, pointwise at $p$ in Theorem 1.1(i) and everywhere in 1.1(ii) and 1.3. The companion hypothesis that a function $\mathsf{x}$ with $d\mathsf{x}\ne0$ has level sets *strictly concave from the superlevel sets* means the following. For each level set, the second fundamental form with respect to $\nu=\nabla\mathsf{x}/|\nabla\mathsf{x}|$ (Definition #49) is positive definite, i.e. $\operatorname{Hess}_g\mathsf{x}(v,v)>0$ for $0\ne v\in\ker d\mathsf{x}$. Thus each sublevel set $\{\mathsf{x}\le c\}$ has strictly convex boundary, and $\mathsf{x}=-\rho$ is an example near a strictly convex $\partial M$. Strict convexity also makes the exit time and hence the scattering relation $\mathcal{L}$ well defined and continuous near tangential directions.

# Number theory

## 67. Local components of an automorphic representation (restricted tensor product)

*Chapter context.* The chapter on the tensor product theorem in a book on automorphic representations of reductive groups over number fields. The reader knows: number fields and adeles; connected reductive groups $G$ over $F$ and the restricted product $G(\mathbb{A}_F)$; smooth and admissible representations of the $p$-adic groups $G(F_v)$; admissible $(\mathfrak{g}_v,K_v)$-modules at archimedean places; admissible $(\mathfrak{g}_\infty,K_\infty)\times G(\mathbb{A}_F^\infty)$-modules and automorphic representations; spherical Hecke algebras and the Satake isomorphism. The restricted tensor product and local components are defined here.

**Setting.** $F$ is a number field and $G$ a connected reductive group over $F$. Fix a finite set $S_0$ of places of $F$, containing all archimedean places, and a smooth affine group scheme $\mathcal{G}$ over $\mathcal{O}_{F,S_0}$ with generic fibre $G$ and reductive fibres. Such data exist: any $G$ spreads out to a reductive group scheme over $\mathcal{O}_F[1/M]$ for some $M\ge 1$. For finite $v\notin S_0$, put $K_v:=\mathcal{G}(\mathcal{O}_v)$. This is a hyperspecial maximal compact open subgroup of $G(F_v)$, and $G(\mathbb{A}_F^\infty)$ is the restricted product of the $G(F_v)$, $v<\infty$, with respect to these $K_v$. For $v\mid\infty$, fix a maximal compact subgroup $K_v\subset G(F_v)$ and let $\mathfrak{g}_v=\operatorname{Lie}G(F_v)\otimes_{\mathbb{R}}\mathbb{C}$. Then $K_\infty=\prod_{v\mid\infty}K_v$ and $\mathfrak{g}_\infty=\bigoplus_{v\mid\infty}\mathfrak{g}_v$. By a *representation of $G(F_v)$* we mean a smooth representation if $v$ is finite and a $(\mathfrak{g}_v,K_v)$-module if $v$ is archimedean.

**Proposition 67.1.** Let $v\notin S_0$ be finite and let $\pi_v$ be an irreducible admissible representation of $G(F_v)$. Then $\dim_{\mathbb{C}}\pi_v^{K_v}\le 1$.

(The algebra $C_c(K_v\backslash G(F_v)/K_v)$ is commutative by the Satake isomorphism, and $\pi_v^{K_v}$ is a finite-dimensional simple module over it.) We call $\pi_v$ *unramified* (or *$K_v$-spherical*) if $\pi_v^{K_v}\neq0$.

**Definition 67.2 (restricted tensor product).** Suppose given:

* for every place $v$, an admissible representation $(\pi_v,V_v)$ of $G(F_v)$;
* a finite set $S_1\supseteq S_0$ of places and, for every $v\notin S_1$, a nonzero vector $x_v^0\in V_v^{K_v}$.

For finite sets $S$ of places with $S\supseteq S_1$, put $V_S:=\bigotimes_{v\in S}V_v$ (algebraic tensor product over $\mathbb{C}$). For $S\subseteq S'$, let $j_{S,S'}\colon V_S\to V_{S'}$ be the map $x\mapsto x\otimes\bigotimes_{v\in S'\setminus S}x_v^0$. These maps form a directed system, and
$$\textstyle\bigotimes'_v(V_v,x_v^0):=\varinjlim_{S}V_S$$
is the colimit of $\mathbb{C}$-vector spaces. It is spanned by the images of the pure tensors $\otimes_v x_v$ with $x_v\in V_v$ for all $v$ and $x_v=x_v^0$ for almost all $v$. It carries the following actions:

* $g=(g_v)_v\in G(\mathbb{A}_F^\infty)$ acts by $g\cdot(\otimes_v x_v)=\otimes_v\, y_v$, where $y_v=\pi_v(g_v)x_v$ for finite $v$ and $y_v=x_v$ for $v\mid\infty$. This is well defined because $g_v\in K_v$, and hence $\pi_v(g_v)x_v^0=x_v^0$, for almost all $v$.
* $X\in\mathfrak{g}_v$ and $k\in K_v$ ($v\mid\infty$) act on the $v$-th tensor factor only.

This makes $\bigotimes'_v\pi_v:=\bigotimes'_v(V_v,x_v^0)$ a $(\mathfrak{g}_\infty,K_\infty)\times G(\mathbb{A}_F^\infty)$-module, the *restricted tensor product* of the $\pi_v$ with respect to the $x_v^0$.

**Proposition 67.3.** In Definition 67.2, if every $\pi_v$ is irreducible, then $\bigotimes'_v\pi_v$ is irreducible and admissible. Its isomorphism class does not depend on the choice of the vectors $x_v^0$, nor on $(S_0,\mathcal{G})$: any two choices of $K_v$ agree at almost all $v$.

**Theorem 67.4 (tensor product theorem; Flath).** Let $\pi$ be an irreducible admissible $(\mathfrak{g}_\infty,K_\infty)\times G(\mathbb{A}_F^\infty)$-module. Then:

(a) For every place $v$ there is an irreducible admissible representation $\pi_v$ of $G(F_v)$, with $\pi_v$ unramified for almost all finite $v\notin S_0$, such that $\pi\cong\bigotimes'_v\pi_v$ (for any choice of the $x_v^0$).

(b) The $\pi_v$ are unique up to isomorphism: if $\pi\cong\bigotimes'_v\pi_v\cong\bigotimes'_v\pi'_v$ with all $\pi_v,\pi'_v$ irreducible admissible, then $\pi_v\cong\pi'_v$ for every $v$.

(Reference: D. Flath, *Decomposition of representations into tensor products*, Proc. Sympos. Pure Math. 33 (Corvallis), 1979; for $\mathrm{GL}_2$ see D. Bump, *Automorphic Forms and Representations*, Ch. 3.)

**Definition 67.5 (local components).** Let $\pi$ be an irreducible admissible $(\mathfrak{g}_\infty,K_\infty)\times G(\mathbb{A}_F^\infty)$-module. Typically $\pi$ is an automorphic representation, e.g. a cuspidal one. For a place $v$ of $F$:

* the *local component of $\pi$ at $v$* is the isomorphism class of the irreducible admissible representation $\pi_v$ of $G(F_v)$ given by Theorem 67.4. We write $\pi=\otimes_v\pi_v$ or $\pi=\otimes'_v\pi_v$;
* $\pi_\infty:=\bigotimes_{v\mid\infty}\pi_v$ is the archimedean component, an irreducible admissible $(\mathfrak{g}_\infty,K_\infty)$-module;
* $\pi$ is *unramified at* a finite place $v\notin S_0$ if $\pi_v^{K_v}\ne0$. This holds for all but finitely many $v$.

Two such modules $\pi,\pi'$ are *nearly equivalent* if $\pi_v\cong\pi'_v$ for all but finitely many places $v$.

*Remarks.*

(1) Intrinsic description. Let $v$ be finite. Let $K^v=\prod_{w<\infty,\,w\ne v}K'_w$ be a compact open subgroup of $G(\mathbb{A}_F^{\infty,v})$ with $K'_w=K_w$ for almost all $w$ and $\pi^{K^v}\ne0$. Then $\pi^{K^v}$ is a smooth $G(F_v)$-representation isomorphic to a direct sum of copies of $\pi_v$, since it is $\cong\pi_v\otimes\pi_\infty\otimes\bigotimes_{w\ne v}\pi_w^{K'_w}$. Hence $\pi_v$ is the unique irreducible smooth representation $W$ of $G(F_v)$ with $\operatorname{Hom}_{G(F_v)}(W,\pi^{K^v})\neq0$. This gives a definition of $\pi_v$ that avoids choosing an isomorphism $\pi\cong\bigotimes'_v\pi_v$. Similarly, $\pi^{K^\infty}$ for a compact open $K^\infty\subset G(\mathbb{A}_F^\infty)$ is a direct sum of copies of $\pi_\infty$.
(2) Unitary version. Irreducible unitary representations of $G(\mathbb{A}_F)$ on Hilbert spaces, e.g. the irreducible closed subrepresentations $\tilde\pi\subset L^2_{\mathrm{cusp}}$ in [2021, 194(2), no. 5], are admissible. Their local components are by definition those of the irreducible admissible module of smooth $K_\infty$-finite vectors. Equivalently, $\tilde\pi$ is a restricted Hilbert tensor product of irreducible unitary representations of the $G(F_v)$ with respect to unit vectors $x_v^0$.
(3) At archimedean places, $\pi_v$ is a Harish-Chandra module. Some papers instead use the Casselman--Wallach globalisation, a smooth admissible Fréchet representation of $G(F_v)$, e.g. [2021, 194(2), no. 5, Section 2]. The two categories are equivalent via $K_v$-finite vectors, so local components can be read either way.
(4) Uses in the Annals papers. In [2020, 191(2), no. 1], $\pi=\otimes\pi_v$ is the cuspidal automorphic representation of $\mathrm{GL}_2(\mathbb{A}_{\mathbb{Q}})$ attached to the newform $f\in S_2(\Gamma_0(N))$, normalised by $L(\pi,s-\tfrac12)=L(f,s)$. For $\ell\,\Vert\, N$, the component $\pi_\ell$ is either the Steinberg ("special") representation $\mathrm{St}_\ell$ or its twist $\mathrm{St}_\ell\otimes(\xi_\ell\circ\det)$ by the unramified quadratic character $\xi_\ell$ of $\mathbb{Q}_\ell^\times$. The two cases correspond to Atkin--Lehner eigenvalue $w_\ell=-1$ and $w_\ell=+1$ respectively. Nearly equivalent representations ("$\tilde\pi_v\simeq\pi_v$ for all but finitely many $v$") define the $\pi$-nearly isotypic subspace in [2021, 194(2), no. 5]. Weak functorial transfer ([2024, 200(3), no. 2]) and weak base change are conditions on $\pi_v$ for almost all $v$. In [2026, 203(1), no. 4] the local components at every place, archimedean ones included, are fed into the local Langlands correspondence $\operatorname{rec}_{F_v}$.

## 68. Arithmetic lattice in a semisimple Lie group

*Chapter context.* The chapter on arithmetic groups in a book on lattices in semisimple Lie groups. The reader knows: Lie groups and Haar measure; lattices, i.e. discrete subgroups $\Gamma<G$ for which $G/\Gamma$ carries a finite $G$-invariant measure; linear algebraic groups over $\mathbb{Q}$ and their real points; arithmetic subgroups of $\mathbf{H}(\mathbb{Q})$ for a linear algebraic $\mathbb{Q}$-group $\mathbf{H}$. Arithmetic lattices in an abstract Lie group are defined here.

**Recollection 68.1.** Let $\mathbf{H}$ be a linear algebraic group over $\mathbb{Q}$. Choose a faithful $\mathbb{Q}$-representation $\rho\colon\mathbf{H}\hookrightarrow\mathrm{GL}_N$ and put $\mathbf{H}(\mathbb{Z}):=\rho^{-1}(\mathrm{GL}_N(\mathbb{Z}))\subseteq\mathbf{H}(\mathbb{Q})$. The commensurability class of $\mathbf{H}(\mathbb{Z})$ does not depend on $\rho$. Its members are the *arithmetic subgroups* of $\mathbf{H}(\mathbb{Q})$. Two subgroups $\Gamma_1,\Gamma_2$ of a group are *commensurable* if $\Gamma_1\cap\Gamma_2$ has finite index in both $\Gamma_1$ and $\Gamma_2$. This is an equivalence relation, and it is preserved by images under group homomorphisms. $\mathbf{H}(\mathbb{R})$ is a real Lie group with finitely many connected components, and $\mathbf{H}(\mathbb{R})^0$ denotes its identity component (real topology).

**Theorem 68.2 (Borel--Harish-Chandra).** If $\mathbf{H}$ is semisimple, then every arithmetic subgroup of $\mathbf{H}(\mathbb{Q})$ is a lattice in $\mathbf{H}(\mathbb{R})$. (A. Borel, *Introduction aux groupes arithmétiques*.)

**Definition 68.3.** Let $G$ be a connected semisimple real Lie group and $\Gamma<G$ a lattice. $\Gamma$ is *arithmetic* if there exist

1. a connected semisimple linear algebraic group $\mathbf{H}$ over $\mathbb{Q}$, and
2. a continuous surjective homomorphism $p\colon\mathbf{H}(\mathbb{R})^0\to G$ with compact kernel,

such that $p\big(\mathbf{H}(\mathbb{Z})\cap\mathbf{H}(\mathbb{R})^0\big)$ is commensurable with $\Gamma$. A lattice that is not arithmetic is *non-arithmetic*.

For a Lie group $G$ with finitely many components and $G^0$ semisimple, a lattice $\Gamma<G$ is called arithmetic if the lattice $\Gamma\cap G^0$ of $G^0$ is arithmetic in the above sense.

*Remarks.*

(1) Well-definedness and invariance. By Recollection 68.1 the condition does not depend on the choice of $\mathbf{H}(\mathbb{Z})$ within its commensurability class. Composing $p$ with an automorphism of $G$, e.g. conjugation by $g\in G$, shows that the set of arithmetic lattices is stable under $\mathrm{Aut}(G)$. Arithmeticity is also a property of the commensurability class of $\Gamma$. No separate clause "up to conjugation" is needed.
(2) Variant with all real points. [2023, 197(1), no. 3] requires a surjective $p\colon\mathbf{H}(\mathbb{R})\to G$ with compact kernel such that $\Gamma$ is commensurable with $p(\mathbf{H}(\mathbb{Z}))$. For connected $G$ the two definitions are equivalent:
* Given such a $p$, the image $p(\mathbf{H}(\mathbb{R})^0)$ is an open subgroup of finite index, hence equals $G$. Moreover $\mathbf{H}(\mathbb{Z})\cap\mathbf{H}(\mathbb{R})^0$ has finite index in $\mathbf{H}(\mathbb{Z})$. So such a $p$ gives a $p$ as in Definition 68.3.
* Conversely, given $p$ as in 68.3, replace $\mathbf{H}$ by its simply connected cover $\tilde{\mathbf{H}}\to\mathbf{H}$. Then $\tilde{\mathbf{H}}(\mathbb{R})$ is connected (E. Cartan), and it maps onto $\mathbf{H}(\mathbb{R})^0$ with finite kernel. Isogenies carry arithmetic subgroups to arithmetic subgroups (Borel), so the composite $\tilde{\mathbf{H}}(\mathbb{R})\to G$ has the required properties.

"Semisimple Lie group" in that paper means $G=\mathrm{PU}(1,n)$, $n>1$.

(3) Equivalent formulation via number fields (restriction of scalars). If $\mathbf{H}=\mathrm{Res}_{k/\mathbb{Q}}\mathbf{H}'$ for an absolutely simple group $\mathbf{H}'$ over a number field $k$, then $\mathbf{H}(\mathbb{R})=\prod_{\tau}\mathbf{H}'^{\tau}(\mathbb{R}\text{ or }\mathbb{C})$, over the archimedean places $\tau$ of $k$. For $G$ simple, compactness of $\ker p$ forces all factors but one to be compact, and $\mathbf{H}(\mathbb{Z})$ corresponds to $\mathbf{H}'(\mathcal{O}_k)$. In particular one has the Mostow--Vinberg criterion, as used in [2023, 197(1), no. 3]. Let $k\subset\mathbb{R}$ be totally real and $\mathbf{G}/k$ a group with $\mathbf{G}(\mathbb{R})^0\cong G$. Let $\Gamma\subseteq\mathbf{G}(\mathcal{O}_k)$ be a lattice in $G$, with $\mathbf{G}(\mathcal{O}_k)$ taken via a $k$-embedding into some $\mathrm{GL}_N$. Then $\Gamma$ is arithmetic if and only if $\mathbf{G}^{\sigma}(\mathbb{R})$ is compact for every embedding $\sigma\colon k\to\mathbb{R}$ that does not restrict to the identity on the trace field $\mathbb{Q}(\operatorname{tr}\operatorname{Ad}\gamma:\gamma\in\Gamma)$. [2021, 193(3), no. 4] uses the equivalent criterion "$\Gamma$ is contained in $\mathbf{G}(\ell)$ for its adjoint trace field $\ell$, and its image in $\mathbf{G}(\ell_v)$ is precompact for every place $v$ of $\ell$ other than the given real one".
(4) Examples. For $G=\mathrm{SO}_0(n,1)$: let $k$ be totally real and $f$ a quadratic form over $k$ in $n+1$ variables, of signature $(n,1)$ at the identity embedding and definite at all other real embeddings. Then $\mathrm{SO}(f)(\mathcal{O}_k)\cap G$ is an arithmetic lattice. These are the lattices "of simplest type", and for $n$ even all arithmetic lattices are commensurable with conjugates of these. Non-arithmetic lattices exist in $\mathrm{SO}_0(n,1)$ for all $n\ge2$ (e.g. Gromov--Piatetski-Shapiro) and in $\mathrm{PU}(1,n)$ for $n\le 3$. By Margulis arithmeticity, and by Corlette and Gromov--Schoen for $\mathrm{Sp}(n,1)$ and $F_{4(-20)}$, every irreducible lattice in any other $G$ without compact factors is arithmetic.
(5) In the Annals papers, $G=\mathrm{SO}_0(n,1)$ ([2021, 193(3), no. 4]) and $G=\mathrm{PU}(1,n)$, $n>1$ ([2023, 197(1), no. 3]). Both are connected, linear, centre-free, simple and without compact factors. Lattices there are of finite covolume but need not be cocompact.

## 69. Galois representation attached to a cuspidal Hecke eigenform

*Chapter context.* The chapter "Galois representations attached to modular forms" in a book on modular forms and Galois representations. The reader knows: the spaces $S_k(\Gamma_1(N))$, their Hecke operators $T_n$ and diamond operators $\langle d\rangle$, eigenforms and newforms; continuous representations of $G_{\mathbb{Q}}=\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ over finite extensions of $\mathbb{Q}_p$, ramification and Frobenius elements; the $p$-adic cyclotomic character $\chi_p$. The representation $\rho_{f,\lambda}$ is defined here.

**Setting.** Let $k\ge2$, $N\ge1$, and $\varepsilon\colon(\mathbb{Z}/N\mathbb{Z})^\times\to\mathbb{C}^\times$ a character. Let $0\ne f\in S_k(\Gamma_1(N))$ satisfy $\langle d\rangle f=\varepsilon(d)f$ for all $d$ and $T_\ell f=a_\ell(f)f$ for every prime $\ell\nmid N$; that is, $f$ is an eigenform away from the level, with nebentypus $\varepsilon$. If $f$ is a normalised eigenform for all $T_n$ (e.g. a newform), then $a_\ell(f)$ is the $\ell$-th Fourier coefficient. The *coefficient field* $K_f:=\mathbb{Q}(a_\ell(f),\varepsilon(d):\ell\nmid N,\ d\in(\mathbb{Z}/N)^\times)\subset\mathbb{C}$ is a number field. For a newform, $K_f=\mathbb{Q}(a_n(f):n\ge1)$. Let $\lambda$ be a finite place of $K_f$, of residue characteristic $p$, and let $K_{f,\lambda}$ be the completion, with ring of integers $\mathcal{O}_\lambda$ and residue field $k_\lambda$. We regard $\varepsilon$ as a character of $G_{\mathbb{Q}}$ with values in $K_f^\times\subset K_{f,\lambda}^\times$, via $G_{\mathbb{Q}}\to\mathrm{Gal}(\mathbb{Q}(\zeta_N)/\mathbb{Q})\cong(\mathbb{Z}/N)^\times$, $\sigma(\zeta_N)=\zeta_N^{a(\sigma)}$. For $\ell\nmid Np$, $\mathrm{Frob}_\ell\in G_{\mathbb{Q}}$ denotes an *arithmetic* Frobenius at $\ell$, which is well defined up to conjugation and inertia. Then $\varepsilon(\mathrm{Frob}_\ell)=\varepsilon(\ell)$ and $\chi_p(\mathrm{Frob}_\ell)=\ell$.

**Definition 69.1.** A *$\lambda$-adic Galois representation attached to $f$* is a continuous homomorphism $\rho\colon G_{\mathbb{Q}}\to\mathrm{GL}_2(K_{f,\lambda})$ such that for every prime $\ell\nmid Np$:

1. $\rho$ is unramified at $\ell$, i.e. $\rho(I_\ell)=1$ for an inertia group $I_\ell$ at $\ell$; and
2. $\det\big(X-\rho(\mathrm{Frob}_\ell)\big)=X^2-a_\ell(f)X+\varepsilon(\ell)\ell^{k-1}$.

Equivalently, one may use a $2$-dimensional $K_{f,\lambda}$-vector space $V$ with a continuous linear $G_{\mathbb{Q}}$-action.

**Theorem 69.2 (Eichler--Shimura for $k=2$; Deligne for $k\ge2$; Ribet).** A $\lambda$-adic Galois representation attached to $f$ exists and is unique up to isomorphism. It is absolutely irreducible, $\det\rho=\varepsilon\,\chi_p^{\,k-1}$, and $\rho$ is odd: $\det\rho(c)=-1$ for complex conjugation $c$.

Uniqueness: such $\rho$ factor through the Galois group of the maximal extension of $\mathbb{Q}$ unramified outside $Np\infty$. By Chebotarev the conjugates of the $\mathrm{Frob}_\ell$, $\ell\nmid Np$, are dense in that group, so any two such $\rho$ have equal traces. By Brauer--Nesbitt their semisimplifications are isomorphic. Since that semisimplification is irreducible (Ribet), so is every such $\rho$. Construction: for $k=2$, from the $\ell$-adic Tate module of the abelian variety $A_f$ (Definition #71 when $\varepsilon=1$); for $k>2$, from the $f$-part of the étale cohomology of the modular curve with coefficients in $\mathrm{Sym}^{k-2}$ of the universal elliptic curve's $H^1$ (P. Deligne, *Formes modulaires et représentations $\ell$-adiques*, Sém. Bourbaki 355).

**Definition 69.3.** $\rho_{f,\lambda}\colon G_{\mathbb{Q}}\to\mathrm{GL}_2(K_{f,\lambda})$ denotes the representation of Theorem 69.2, well defined up to isomorphism. It is *the* $\lambda$-adic Galois representation attached to $f$.

The *residual representation* $\bar\rho_{f,\lambda}\colon G_{\mathbb{Q}}\to\mathrm{GL}_2(k_\lambda)$ is defined as follows. Choose a $G_{\mathbb{Q}}$-stable $\mathcal{O}_\lambda$-lattice $T\subset V$; one exists by compactness of $G_{\mathbb{Q}}$. Let $\bar\rho_{f,\lambda}$ be the semisimplification of $T/\lambda T$. By Brauer--Nesbitt it is independent of $T$ up to isomorphism, and it is characterised by: unramified outside $Np$, with $\det(X-\bar\rho_{f,\lambda}(\mathrm{Frob}_\ell))\equiv X^2-a_\ell X+\varepsilon(\ell)\ell^{k-1}\bmod\lambda$.

More generally, for a finite extension $E/\mathbb{Q}_p$ and an embedding $\iota\colon K_f\to E$, one writes $\rho_{f,\iota}$ for $\rho_{f,\lambda}\otimes_{K_{f,\lambda},\iota}E$, where $\lambda$ is the place induced by $\iota$. A continuous $\rho\colon G_{\mathbb{Q}}\to\mathrm{GL}_2(E)$ *arises from a cuspidal eigenform of weight $k$* if $\rho\otimes_E\overline{E}\cong\rho_{f,\iota}\otimes_E\overline E$ for some $N$, some $f$ as above of weight $k$, and some $\iota\colon K_f\to\overline E$. Here the normalisation is fixed by the source, see Remark (2).

*Remarks.*

(1) Further properties, not needed for the definition. $\rho_{f,\lambda}|_{G_{\mathbb{Q}_p}}$ is de Rham with Hodge--Tate weights $\{0,k-1\}$, where $\chi_p$ has weight $1$, and it is crystalline if $p\nmid N$. At $\ell\ne p$, the Frobenius-semisimplified Weil--Deligne representation of $\rho_{f,\lambda}|_{G_{\mathbb{Q}_\ell}}$ is attached by local Langlands to the local component $\pi_\ell$ of the automorphic representation of $f$ (Carayol), with a twist depending on normalisations. Coefficients: some authors use $\overline{\mathbb{Q}}_p$ together with an isomorphism $\iota\colon\overline{\mathbb{Q}}_p\cong\mathbb{C}$ instead of $K_{f,\lambda}$. Such an $\iota$ determines a place $\lambda$ of $K_f$, and then $\rho_{f,\iota}=\rho_{f,\lambda}\otimes\overline{\mathbb{Q}}_p$.
(2) Conventions. If $\mathrm{Frob}_\ell$ denotes *geometric* Frobenius, the representation satisfying 69.1(2) is $\rho_{f,\lambda}^\vee\cong\rho_{f,\lambda}\otimes\varepsilon^{-1}\chi_p^{1-k}$, and it is the one that occurs in étale $H^1$. Always check which normalisation a paper uses.
* In [2020, 191(2), no. 1], $f\in S_2(\Gamma_0(N))$ is a newform with trivial character, $K_f=M_f$ is totally real, $L=M_{f,\lambda}$, and $V=V_p(A_f)\otimes_{M_f\otimes\mathbb{Q}_p}L$. This is $\rho_{f,\lambda}$ in the arithmetic normalisation of 69.1, with $\det=\chi_p$ and $V^\vee\cong V(-1)$. Its $L$-function $L(V^\vee,s)=L(f,s)$ is formed with geometric Frobenius. The paper also uses $\bar\rho_{f,\lambda}$ as in 69.3.
* In [2026, 203(1), no. 3], Frobenius elements are geometric and $\chi_p$ has Hodge--Tate weight $-1$. There, "$\rho$ with Hodge--Tate weights $0,k$ arises from a cuspidal eigenform of weight $k+1$" amounts to $\rho\cong\rho_{f,\iota}^\vee$ for an eigenform $f$ of weight $k+1$ and some tame level. Equivalently, the geometric Frobenius at $\ell$ has characteristic polynomial $X^2-a_\ell(f)X+\varepsilon(\ell)\ell^{k}$. In terms of the paper's big Hecke algebra, this says the Hecke eigensystem of $\rho$ occurs in $M_{k+1}(K^p)$.
(3) For $k=1$, Deligne--Serre attach an Artin representation (finite image). It is excluded here.

## 70. Abelian scheme with complex multiplication by $\mathcal{O}_L$ of CM type $\Sigma$

*Chapter context.* The chapter on CM abelian schemes in a book on complex multiplication and special values of Hecke $L$-functions. The reader knows: abelian schemes $A/S$, their duals $A^\vee$ and endomorphism rings; the Lie algebra $\operatorname{Lie}(A/S)$ and the invariant differentials $\omega_{A/S}=e^*\Omega^1_{A/S}$, which are dual locally free $\mathcal{O}_S$-modules; number fields, CM fields and Galois closures. CM types of non-CM fields and CM abelian schemes are defined here.

Fix $\overline{\mathbb{Q}}\subset\mathbb{C}$ and, for a number field $L$, put $J_L:=\operatorname{Hom}(L,\overline{\mathbb{Q}})$. For $\sigma\in J_L$ let $\bar\sigma:=c\circ\sigma$, where $c$ is complex conjugation, and for $\Xi\subseteq J_L$ put $\overline{\Xi}:=\{\bar\sigma:\sigma\in\Xi\}$. Let $L^{\mathrm{Gal}}\subset\overline{\mathbb{Q}}$ be the Galois closure of $L$ and $d_L$ its discriminant.

**Definition 70.1 (CM types).** (a) Let $K$ be a CM field, i.e. a totally imaginary quadratic extension of a totally real field. A *CM type* of $K$ is a subset $\Sigma_K\subseteq J_K$ with $\Sigma_K\cap\overline{\Sigma_K}=\emptyset$ and $\Sigma_K\cup\overline{\Sigma_K}=J_K$.

(b) Let $L$ be a number field containing a CM field. Then $L$ contains a unique maximal CM subfield $K$, the compositum of all CM subfields, and $L$ is totally imaginary. A *CM type of $L$* is a subset of the form
$$\Sigma=\{\sigma\in J_L:\ \sigma|_K\in\Sigma_K\}$$
for a CM type $\Sigma_K$ of $K$; we say $\Sigma$ is *lifted from $\Sigma_K$*. Then $J_L=\Sigma\sqcup\overline{\Sigma}$ and $|\Sigma|=[L:\mathbb{Q}]/2$. If $L$ is itself CM, every $\Sigma$ with $J_L=\Sigma\sqcup\overline\Sigma$ is a CM type; in general not every such $\Sigma$ is one.

**Lemma 70.2.** Let $R$ be an $\mathcal{O}_{L^{\mathrm{Gal}}}[1/d_L]$-algebra. Then $\ell\otimes r\mapsto(\sigma(\ell)r)_{\sigma}$ is an isomorphism $\mathcal{O}_L\otimes_{\mathbb{Z}}R\cong\prod_{\sigma\in J_L}R$. Hence every $\mathcal{O}_L\otimes_{\mathbb{Z}}R$-module $M$ decomposes canonically as $M=\bigoplus_{\sigma\in J_L}M(\sigma)$, where $M(\sigma)=\{m:(\ell\otimes1)m=\sigma(\ell)m\ \forall\ell\in\mathcal{O}_L\}$. For $\Xi\subseteq J_L$ put $M(\Xi):=\bigoplus_{\sigma\in\Xi}M(\sigma)$; e.g. $(\mathcal{O}_L\otimes R)(\Sigma)\cong R^{\Sigma}$. The same holds for quasi-coherent sheaves on $\operatorname{Spec}R$.

**Definition 70.3.** Let $L$ be a number field containing a CM field, $[L:\mathbb{Q}]=2d$, and $S$ a scheme.

(a) An *abelian scheme with complex multiplication (CM) by $\mathcal{O}_L$* over $S$ is a pair $(A,\iota)$, where $A/S$ is an abelian scheme of relative dimension $d$ and $\iota\colon\mathcal{O}_L\to\operatorname{End}_S(A)$ is an injective unital ring homomorphism. It is required that $\operatorname{Lie}(A/S)$, with $\mathcal{O}_L$ acting through $\operatorname{Lie}(\iota(\ell))$, is Zariski-locally on $S$ a finitely generated projective $\mathcal{O}_L\otimes_{\mathbb{Z}}\mathcal{O}_S$-module.

(b) Let $S$ be a scheme over $\mathcal{O}_{L^{\mathrm{Gal}}}[1/d_L]$ and $\Sigma$ a CM type of $L$. Then $(A,\iota)$ has *CM by $\mathcal{O}_L$ of (CM) type $\Sigma$* if, in the decomposition of Lemma 70.2, $\operatorname{Lie}(A/S)(\sigma)$ is locally free of rank $1$ for $\sigma\in\Sigma$ and $\operatorname{Lie}(A/S)(\sigma)=0$ for $\sigma\notin\Sigma$. Equivalently, Zariski-locally on $S$ there is an $\mathcal{O}_L\otimes\mathcal{O}_S$-linear isomorphism $\operatorname{Lie}(A/S)\cong(\mathcal{O}_L\otimes_{\mathbb{Z}}\mathcal{O}_S)(\Sigma)$. In words: $\mathcal{O}_L$ acts on $\operatorname{Lie}(A/S)$ through the embeddings in $\Sigma$, each with multiplicity one.

**Proposition 70.4.** Let $R\subset\mathbb{C}$ be an $\mathcal{O}_{L^{\mathrm{Gal}}}[1/d_L]$-algebra and $(A,\iota)$ an abelian scheme over $R$ with CM by $\mathcal{O}_L$.

(i) There is a unique CM type $\Sigma$ of $L$ (lifted from the maximal CM subfield) such that $A$ has CM of type $\Sigma$, the *CM type of $A$*.

(ii) Dually, $\omega_{A/R}=\bigoplus_{\sigma\in\Sigma}\omega_{A/R}(\sigma)$ with each summand locally free of rank $1$, where $\iota(\ell)^*$ acts on $\omega_{A/R}(\sigma)$ by $\sigma(\ell)$.

(iii) With $\iota^\vee(\ell):=\iota(\ell)^\vee$, the dual $(A^\vee,\iota^\vee)$ has CM by $\mathcal{O}_L$ of type $\overline{\Sigma}$.

(iv) $H_1(A(\mathbb{C}),\mathbb{Z})$ is an invertible $\mathcal{O}_L$-module, so it is isomorphic to a fractional ideal $\mathfrak{a}$. Thus $A(\mathbb{C})\cong\mathbb{C}^\Sigma/\Phi_\Sigma(\mathfrak{a})$ with $\Phi_\Sigma(x)=(\sigma(x))_{\sigma\in\Sigma}$, and $\mathcal{O}_L$ acts through $\Phi_\Sigma$.

(Kings--Sprang [2025, 202(1), no. 1, Section 1.3]; for (iv), the classical theory of Shimura--Taniyama, see S. Lang, *Complex Multiplication*.)

*Remarks.*

(1) Conventions. In [2025, 202(1), no. 1] the torus $\mathrm{Res}_{\mathcal{O}_L/\mathbb{Z}}\mathbb{G}_m$ acts on $\omega_{A/R}$ through the inverse, so the summand $\omega_{A/R}(\sigma)$ of 70.4(ii) is written $\omega_{A/R}(-\sigma)$ there. The CM type of $A$ is always the set of embeddings through which $\mathcal{O}_L$ acts on $\operatorname{Lie}(A)$; equivalently, on $\omega_{A^\vee}$ it acts through $\overline\Sigma$. Some older sources attach the type to the action on $H^0(A,\Omega^1)$. Over $\mathbb{C}$ this is the same set $\Sigma$, but one must check whether pull-back or its contragredient is meant.
(2) General bases. Over a base on which $d_L$ is not invertible, one replaces 70.3(b) by the determinant (Kottwitz) condition $\det_{\mathcal{O}_S}(T-\iota(\ell)\mid\operatorname{Lie}(A/S))=\prod_{\sigma\in\Sigma}(T-\sigma(\ell))$ in $\mathcal{O}_S[T]$. Over $\mathcal{O}_{L^{\mathrm{Gal}}}[1/d_L]$ this agrees with 70.3(b) when required for all $\ell\in\mathcal{O}_L\otimes R'$ and all $R$-algebras $R'$. The Annals paper only needs $\mathcal{O}_{L^{\mathrm{Gal}}}[1/d_L]$-algebras $R\subset\mathbb{C}$.
(3) The case $L=K$ CM is the classical notion of a CM abelian scheme of type $(K,\Sigma)$. For $L\supsetneq K$, examples are the Serre tensor constructions $\mathcal{O}_L\otimes_{\mathcal{O}_K}A_0$ of abelian schemes $A_0$ with CM by $\mathcal{O}_K$. Such $A$ are isogenous to powers of simple CM abelian varieties; they need not be simple.
(4) A CM abelian scheme over $R\subset\mathbb{C}$ exists for every CM type: $\mathbb{C}^\Sigma/\Phi_\Sigma(\mathfrak{a})$ is algebraic, has CM by $\mathcal{O}_L$, and descends to $\mathcal{O}_k[1/M]$ for a number field $k$ and some $M$. Kings--Sprang fix such an $\mathcal{A}/\mathcal{R}$ with an $\mathcal{O}_L$-structure, $H_1(\mathcal{A}(\mathbb{C}),\mathbb{Z})\cong\mathcal{O}_L$, as a reference object, whose periods are Definition #74.
(5) In [2025, 202(1), no. 1], $\Sigma$ is also the CM type attached to a critical infinity type $\mu$ ($\Sigma=\{\sigma:\mu(\sigma)<0\}$). Given $\iota_p\colon\overline{\mathbb{Q}}\to\mathbb{C}_p$, $\Sigma$ is *$p$-ordinary* if the sets $\Sigma_p$ and $\overline{\Sigma}_p$ of primes of $L$ induced by $\iota_p\circ\sigma$, for $\sigma\in\Sigma$ resp. $\sigma\in\overline\Sigma$, are disjoint.

## 71. Abelian variety $A_f$ attached to a weight-2 newform

*Chapter context.* The chapter on the Eichler--Shimura construction in a book on modular curves and modular forms. The reader knows: the modular curve $X_0(N)$ over $\mathbb{Q}$ and its Jacobian $J_0(N)$; abelian varieties over $\mathbb{Q}$, abelian subvarieties, quotients and isogenies; the space $S_2(\Gamma_0(N))$ with its Hecke operators $T_n$ ($n\ge1$) and newforms; the identification $S_2(\Gamma_0(N))\cong H^0(X_0(N)_{\mathbb{C}},\Omega^1)$, $f\mapsto 2\pi i f(\tau)\,d\tau$; and the isomorphism $H^0(J_0(N)_{\mathbb{C}},\Omega^1)\cong H^0(X_0(N)_{\mathbb{C}},\Omega^1)$ given by pull-back along an Abel--Jacobi map. Through these we identify $H^0(J_0(N)_{\mathbb{C}},\Omega^1)=S_2(\Gamma_0(N))$.

**Proposition 71.1 (Hecke operators on $J_0(N)$).** For every $n\ge1$ there is a unique endomorphism $T_n\in\operatorname{End}_{\mathbb{Q}}(J_0(N))$ whose pull-back action $T_n^*$ on $H^0(J_0(N)_{\mathbb{C}},\Omega^1)=S_2(\Gamma_0(N))$ is the classical Hecke operator $T_n$. For $p\mid N$ this is $U_p$.

Uniqueness holds because an endomorphism of a complex abelian variety is determined by its action on invariant differentials. Existence: $T_p$ is induced by the Hecke correspondence on $X_0(N)$, which is defined over $\mathbb{Q}$ through the two degeneracy maps $X_0(Np)\rightrightarrows X_0(N)$, and $T_n$ is then given by the usual recursion. The subring
$$\mathbb{T}:=\mathbb{Z}[T_n:n\ge1]\subseteq\operatorname{End}_{\mathbb{Q}}(J_0(N))$$
is commutative and finite free over $\mathbb{Z}$, and $t\mapsto t^*$ identifies it with the $\mathbb{Z}$-algebra of Hecke operators on $S_2(\Gamma_0(N))$.

**Setting.** Let $f=\sum_{n\ge1}a_nq^n\in S_2(\Gamma_0(N))$ be a newform, so $a_1=1$ and $T_nf=a_nf$ for all $n$. Its *Hecke field* $K_f:=\mathbb{Q}(a_n:n\ge1)\subset\mathbb{C}$ is a totally real number field. Let $\theta_f\colon\mathbb{T}\to\mathbb{C}$ be the ring homomorphism with $t^*f=\theta_f(t)f$, so $\theta_f(T_n)=a_n$ and $\theta_f(\mathbb{T})=\mathbb{Z}[a_n:n\ge1]$ is an order in $K_f$. Put
$$I_f:=\ker\theta_f=\{t\in\mathbb{T}:t^*f=0\},$$
the annihilator of $f$ in $\mathbb{T}$.

**Definition 71.2.** Let $I_fJ_0(N)$ be the abelian subvariety of $J_0(N)$ (over $\mathbb{Q}$) given by $\sum_{t\in I_f}t(J_0(N))$. This is the image of $J_0(N)^r\to J_0(N)$, $(x_i)\mapsto\sum_i t_i(x_i)$, for any generators $t_1,\dots,t_r$ of the ideal $I_f$. The *abelian variety attached to $f$* is the quotient abelian variety over $\mathbb{Q}$
$$A_f:=J_0(N)/I_fJ_0(N),$$
together with the quotient map $J_0(N)\twoheadrightarrow A_f$ and the action of $\mathbb{T}$ on $A_f$ induced from $J_0(N)$. This action is well defined because $\mathbb{T}$ is commutative.

**Theorem 71.3 (Shimura; Eichler--Shimura; Ribet).**

(a) The $\mathbb{T}$-action on $A_f$ factors through $\mathbb{T}/I_f\cong\mathbb{Z}[a_n:n\ge1]$, which acts faithfully. Thus $K_f=(\mathbb{T}/I_f)\otimes\mathbb{Q}\hookrightarrow\operatorname{End}^0_{\mathbb{Q}}(A_f):=\operatorname{End}_{\mathbb{Q}}(A_f)\otimes\mathbb{Q}$, and this is an equality (Ribet).
(b) Pull-back along $J_0(N)\to A_f$ identifies $H^0(A_{f,\mathbb{C}},\Omega^1)$ with $S_2(\Gamma_0(N))[I_f]=\bigoplus_{\sigma\colon K_f\to\mathbb{C}}\mathbb{C}f^{\sigma}$. Here $f^\sigma=\sum\sigma(a_n)q^n$ are the Galois conjugates of $f$, again newforms of level $N$. Hence $\dim A_f=[K_f:\mathbb{Q}]$.
(c) For every prime $p$, $V_p(A_f)$ is free of rank $2$ over $K_f\otimes\mathbb{Q}_p$. For $\lambda\mid p$, $V_p(A_f)\otimes_{K_f\otimes\mathbb{Q}_p}K_{f,\lambda}$ is the representation $\rho_{f,\lambda}$ (Definition #69, arithmetic Frobenius, $\det=\chi_p$). This follows from the Eichler--Shimura congruence relation $T_\ell=F+V$ (Frobenius plus Verschiebung) on the reduction of $J_0(N)$ mod $\ell$, for $\ell\nmid N$.
(d) $A_f$ has good reduction at all $\ell\nmid N$, and $L(A_f,s)=\prod_{\sigma\colon K_f\to\mathbb{C}}L(f^\sigma,s)$.

*Remarks.*

(1) Up to isogeny. By Faltings' isogeny theorem, $A_f$ is determined up to $\mathbb{Q}$-isogeny by $L(A_f,s)=\prod_\sigma L(f^\sigma,s)$; this is how [2020, 191(2), no. 1] introduces it ("up to isogeny"). Isogenous variants also appear in the literature. One is the abelian subvariety $J_0(N)[I_f]^0\subseteq J_0(N)$, the identity component of the kernel of $I_f$; it is isogenous to $A_f$. Another uses Albanese instead of Picard functoriality for the Hecke correspondences, which replaces $T_n$ by its Rosati transpose. Statements such as "$\operatorname{rank}A_f(\mathbb{Q})=[K_f:\mathbb{Q}]$", finiteness of the Tate--Shafarevich group $\mathrm{Sha}(A_f)$, and $L(A_f/K,s)$ are isogeny-invariant. Integral statements, for instance about $\mathrm{Sha}(A_f)[p^\infty]$ for small $p$, may depend on the model. The quotient of Definition 71.2 is the *optimal quotient*: its kernel $I_fJ_0(N)$ is connected.
(2) Elliptic curves: if $K_f=\mathbb{Q}$, $A_f$ is the optimal (strong Weil) elliptic curve of conductor $N$ in the isogeny class attached to $f$.
(3) $\operatorname{End}^0_{\overline{\mathbb{Q}}}(A_f)$ can be larger than $K_f$, through inner twists. It equals $K_f$ when, for instance, $N$ is squarefree, the case of [2020, 191(2), no. 1]. In that paper the notation is $M_f=K_f=\operatorname{End}^0_{\mathbb{Q}}(A_f)$, and the Mordell--Weil, Selmer and Tate--Shafarevich groups are those of $A_f$ over $\mathbb{Q}$ and over an imaginary quadratic field $K$.
(4) The construction generalises to newforms on $\Gamma_1(N)$ with character, using $J_1(N)$. There $K_f$ is a CM or totally real field and $\operatorname{End}^0_{\mathbb{Q}}(A_f)=K_f$ still holds (Ribet). This generality is not needed here.

## 72. CM automorphic representation

*Chapter context.* The chapter on twisting and dihedral (CM) forms in a book on automorphic representations of $\mathrm{GL}_2$ over number fields. The reader knows: Hecke characters $F^\times\backslash\mathbb{A}_F^\times\to\mathbb{C}^\times$ and global class field theory; cuspidal automorphic representations of $\mathrm{GL}_n(\mathbb{A}_F)$, as irreducible admissible $(\mathfrak{g}_\infty,K_\infty)\times\mathrm{GL}_n(\mathbb{A}_F^\infty)$-modules realised in the space of cusp forms, and their isomorphism classes; local components $\pi_v$ (Definition #67); strong multiplicity one for $\mathrm{GL}_n$. Twisting and CM representations are defined here.

**Definition 72.1 (twist by a character).** Let $\pi$ be a cuspidal automorphic representation of $\mathrm{GL}_n(\mathbb{A}_F)$, with space $V_\pi$ of cusp forms, and $\chi\colon F^\times\backslash\mathbb{A}_F^\times\to\mathbb{C}^\times$ a Hecke character, i.e. a continuous homomorphism. The *twist* $\pi\otimes\chi:=\pi\otimes(\chi\circ\det)$ is the space
$$V_{\pi\otimes\chi}:=\{\varphi(g)\,\chi(\det g):\varphi\in V_\pi\},$$
with the right-translation action of $(\mathfrak{g}_\infty,K_\infty)\times\mathrm{GL}_n(\mathbb{A}_F^\infty)$. It is again a cuspidal automorphic representation. Abstractly, it is the tensor product of $\pi$ with the one-dimensional module $\chi\circ\det$: $g\in\mathrm{GL}_n(\mathbb{A}_F^\infty)$ acts by $\chi(\det g)\pi(g)$, $k\in K_\infty$ by $\chi_\infty(\det k)\pi(k)$, and $X\in\mathfrak{g}_\infty$ by $\pi(X)+d\chi_\infty(\operatorname{tr}X)$. Locally, $(\pi\otimes\chi)_v\cong\pi_v\otimes(\chi_v\circ\det)$ for every place $v$.

**Definition 72.2.** A cuspidal automorphic representation $\pi$ of $\mathrm{GL}_2(\mathbb{A}_F)$ *has CM* (is a *CM automorphic representation*, or is *dihedral*) if there is a Hecke character $\eta\colon F^\times\backslash\mathbb{A}_F^\times\to\mathbb{C}^\times$ with $\eta\ne1$ and
$$\pi\cong\pi\otimes(\eta\circ\det)$$
as $(\mathfrak{g}_\infty,K_\infty)\times\mathrm{GL}_2(\mathbb{A}_F^\infty)$-modules. Otherwise $\pi$ is *without CM* (*non-CM*).

**Proposition 72.3.** Let $\pi$ be cuspidal on $\mathrm{GL}_2(\mathbb{A}_F)$ and $1\ne\eta$ a Hecke character with $\pi\cong\pi\otimes\eta$.

(a) $\eta^2=1$, by comparing central characters: $\omega_\pi=\omega_\pi\eta^2$. So $\eta=\eta_{E/F}$ is the quadratic character attached by class field theory to a unique quadratic extension $E/F$, with kernel $F^\times N_{E/F}(\mathbb{A}_E^\times)$.
(b) (Labesse--Langlands) $\pi\cong\pi_\theta:=\mathrm{AI}_{E/F}(\theta)$ is the automorphic induction of a Hecke character $\theta\colon E^\times\backslash\mathbb{A}_E^\times\to\mathbb{C}^\times$ with $\theta\neq\theta\circ c$, where $c$ generates $\mathrm{Gal}(E/F)$. That is, $L(s,\pi)=L(s,\theta)$, and for every place $v$ the local Langlands parameter of $\pi_v$ is the representation of $W_{F_v}$ induced from $\theta_v$. If $v$ splits in $E$, this is the sum of the two characters $\theta_w$, $w\mid v$. Conversely, every such $\pi_\theta$ is cuspidal and satisfies $\pi_\theta\cong\pi_\theta\otimes\eta_{E/F}$.
(c) If $F$ is totally real and $\pi_v$ is essentially square-integrable for every $v\mid\infty$, then $E$ is a CM field, i.e. totally imaginary. Indeed, at a real place split in $E$ the component $\pi_v$ would be a principal series.

*Remarks.*

(1) Equivalent tests. By strong multiplicity one, $\pi\cong\pi\otimes\eta$ if and only if $\pi_v\cong\pi_v\otimes\eta_v$ for almost all $v$. For finite $v$ where $\pi$ and $\eta$ are unramified and $v$ is inert in $E$, this says that the Hecke eigenvalue at $v$ vanishes: $\operatorname{tr}$ of the Satake parameter is $0$. Thus $\pi$ has CM if and only if there is a quadratic extension $E/F$ such that $a_v(\pi)=0$ for almost all primes $v$ inert in $E$. On the Galois side, for $\pi$ regular algebraic, $\pi$ has CM if and only if $r_{\pi,\iota}\cong\operatorname{Ind}_{G_E}^{G_F}\psi$ for a quadratic $E/F$ and a character $\psi$ of $G_E$. Equivalently, the projective image of $r_{\pi,\iota}$ is dihedral, or $r_{\pi,\iota}|_{G_{F'}}$ is reducible for some finite extension $F'/F$ (failure of strong irreducibility).
(2) Normalisation. One may quantify over all nontrivial Hecke characters, as in [2026, 203(1), no. 4] ("$\pi\not\cong\pi\otimes(\chi\circ\det)$ for every non-trivial $\chi\colon F^\times\backslash\mathbb{A}_F^\times\to\mathbb{C}^\times$"), or only over quadratic ones. By 72.3(a) the two definitions agree. The notion is unchanged by twisting $\pi$ by any Hecke character.
(3) Hilbert modular forms. For $F$ totally real and $\pi$ generated by a Hilbert modular newform $f$ of weights $k_v\ge2$, $\pi$ has CM if and only if $f$ has CM in the classical sense, i.e. $f$ is a theta series of a Hecke character of a CM quadratic extension $E/F$. Equivalently, $f\otimes\eta_{E/F}=f$ away from finitely many places. In [2026, 203(1), no. 4] Theorem A excludes this case. In the CM case the symmetric power lifts exist by the theory of Eisenstein series, but they are not cuspidal for $n>2$ (footnote to Theorem A there).
(4) $\mathrm{GL}_n$, $n>2$. The condition $\pi\cong\pi\otimes(\eta\circ\det)$ with $\eta\ne1$ makes sense for $\mathrm{GL}_n$. It forces $\eta^n=1$, and for $\eta$ of prime order $d$ it makes $\pi$ automorphically induced from the cyclic extension cut out by $\eta$ (Arthur--Clozel). For $n>2$, "CM" is usually reserved for representations automorphically induced from an algebraic Hecke character of a CM extension of degree $n$. Only the $\mathrm{GL}_2$ notion of Definition 72.2 is needed here.

## 73. Central character of an automorphic representation

*Chapter context.* The chapter on automorphic representations in a book on automorphic forms on reductive groups. The reader knows: a number field $F$, a connected reductive group $G$ over $F$ with centre $Z_G$ (a group of multiplicative type), and the adelic groups $G(\mathbb{A}_F)\supseteq Z_G(\mathbb{A}_F)$; the space $\mathcal{A}(G)$ of automorphic forms and automorphic representations, as irreducible admissible $(\mathfrak{g}_\infty,K_\infty)\times G(\mathbb{A}_F^\infty)$-modules, with $K_\infty$ a maximal compact subgroup of $G(F_\infty)=\prod_{v\mid\infty}G(F_v)$; Schur's lemma for irreducible admissible modules. Central characters are defined here.

Put $\mathfrak{z}_\infty:=\operatorname{Lie}Z_G(F_\infty)\otimes_{\mathbb{R}}\mathbb{C}\subseteq\mathfrak{g}_\infty$.

**Lemma 73.1.** $Z_G(F_\infty)=\big(Z_G(F_\infty)\cap K_\infty\big)\cdot Z_G(F_\infty)^0$. More precisely, the maximal compact subgroup of the abelian Lie group $Z_G(F_\infty)$ is central and compact in $G(F_\infty)$, so it lies in every maximal compact subgroup of $G(F_\infty)$. The remaining factor is a vector group contained in $Z_G(F_\infty)^0=\exp(\operatorname{Lie}Z_G(F_\infty))$.

**Proposition 73.2.** Let $\pi$ be an irreducible admissible $(\mathfrak{g}_\infty,K_\infty)\times G(\mathbb{A}_F^\infty)$-module. There is a unique continuous homomorphism $\omega_\pi\colon Z_G(\mathbb{A}_F)\to\mathbb{C}^\times$ such that:

1. every $z\in Z_G(\mathbb{A}_F^\infty)$ acts on $\pi$ as the scalar $\omega_\pi(z)$;
2. every $z\in Z_G(F_\infty)\cap K_\infty$ acts as $\omega_\pi(z)$;
3. every $X\in\mathfrak{z}_\infty$ acts as $d\omega_\pi(X)$, the derivative of $\omega_\pi|_{Z_G(F_\infty)}$ extended $\mathbb{C}$-linearly.

Schur's lemma gives the scalars in (1)--(3). They glue to a character of $Z_G(F_\infty)$ by Lemma 73.1 and the compatibility axiom of $(\mathfrak{g},K)$-modules. Uniqueness also follows from Lemma 73.1.

**Definition 73.3.** (a) The character $\omega_\pi$ of Proposition 73.2 is the *central character* of $\pi$. For a closed subgroup $Z\subseteq Z_G$, e.g. the maximal $F$-split torus in $Z_G$, $\pi$ *has central character $\omega$ on $Z$* if $\omega_\pi|_{Z(\mathbb{A}_F)}=\omega$.

(b) A continuous character $\omega\colon Z(\mathbb{A}_F)\to\mathbb{C}^\times$ is *automorphic* if it is trivial on $Z(F)$, i.e. a character of $Z(F)\backslash Z(\mathbb{A}_F)$. It is *unitary* if $|\omega|=1$.

(c) Locally: for an irreducible admissible representation $\pi_v$ of $G(F_v)$, $v$ finite, the *central character* $\omega_{\pi_v}\colon Z_G(F_v)\to\mathbb{C}^\times$ is the character by which $Z_G(F_v)$ acts (Schur). For archimedean $v$ it is defined as in 73.2. If $\pi=\otimes'_v\pi_v$ (Definition #67), then $\omega_\pi=\prod_v\omega_{\pi_v}$. Here $\omega_{\pi_v}$ is trivial on $Z_G(F_v)\cap K_v$ for almost all $v$, so the product is finite on each element.

**Proposition 73.4.** If $\pi$ is an automorphic representation, then $\omega_\pi$ is automorphic. If $\pi$ is realised on a subspace $V\subseteq\mathcal{A}(G)$, then $\varphi(zg)=\omega_\pi(z)\varphi(g)$ for all $\varphi\in V$, $z\in Z_G(\mathbb{A}_F)$ and $g\in G(\mathbb{A}_F)$. If $\pi$ occurs in $L^2(G(F)\backslash G(\mathbb{A}_F),\omega)$ (Definition 73.5), then $\omega_\pi|_{Z(\mathbb{A}_F)}=\omega$ is unitary. In general $\omega_\pi$ need not be unitary, even for cuspidal $\pi$: twist by $|\det|^s$ with $s\notin i\mathbb{R}$.

(Right translation by $z$ commutes with $\pi$, so it acts by $\omega_\pi(z)$. Then $\varphi(gz)=\varphi(zg)$, and left $G(F)$-invariance gives triviality on $Z_G(F)$.)

**Definition 73.5 ($L^2$ with central character).** Let $Z\subseteq Z_G$ be a closed $F$-subgroup containing the maximal $F$-split torus of $Z_G$; in [2021, 194(2), no. 5], $Z$ equals that torus. Let $\omega\colon Z(F)\backslash Z(\mathbb{A}_F)\to\mathbb{C}^\times$ be unitary. Then $L^2(G(F)\backslash G(\mathbb{A}_F),\omega)$ is the completion of the space of smooth $\varphi\colon G(\mathbb{A}_F)\to\mathbb{C}$ such that:

* $\varphi(z\gamma g)=\omega(z)\varphi(g)$ for all $z\in Z(\mathbb{A}_F)$, $\gamma\in G(F)$, $g\in G(\mathbb{A}_F)$;
* $|\varphi|^2$, a function on $Z(\mathbb{A}_F)G(F)\backslash G(\mathbb{A}_F)$, is integrable for a fixed invariant measure. The quotient has finite volume by the assumption on $Z$.

$G(\mathbb{A}_F)$ acts by right translation $R$. $L^2_{\mathrm{cusp}}(\ldots,\omega)$ is the closed subspace of cuspidal functions, and $L^2(G(F)\backslash G(\mathbb{A}_F)/K,\omega)$ denotes the $R(K)$-invariants.

*Remarks.*

(1) For $G=\mathrm{GL}_n$, $Z_G=\mathbb{G}_m$ and $\omega_\pi$ is a Hecke character of $F^\times\backslash\mathbb{A}_F^\times$. For $\pi$ attached to $f\in S_k(\Gamma_1(N),\varepsilon)$, $\omega_\pi$ is the adelisation of $\varepsilon$ or of $\varepsilon^{-1}$, times a power of $|\cdot|$, depending on normalisations.
(2) Conventions on $Z$. [2021, 194(2), no. 5] fixes $Z$ to be the maximal $F$-split torus in $Z_G$. There, "unitary automorphic central character $\omega$" means a unitary character of $Z(F)\backslash Z(\mathbb{A}_F)$ through which $Z(\mathbb{A}_F)$ acts, and Theorem 1.1 applies to arbitrary irreducible admissible $\pi$ of $G(\mathbb{A}_F)$ with that property. Other sources use all of $Z_G$, or only $A_G=A_{G,\infty}$, the identity component of the real points of the maximal $\mathbb{Q}$-split torus in $\mathrm{Res}_{F/\mathbb{Q}}Z_G$. By restriction, a central character on $Z_G(\mathbb{A}_F)$ determines the others. For representations realised in $L^2(\ldots,\omega)$, $\omega$ is the restriction of the true central character.
(3) In [2021, 194(2), no. 5] the central character also enters the cuspidal data. Cuspidal automorphic representations $\sigma$ of Levi subgroups $M$ have central characters $\omega_M$ on $Z_M(\mathbb{A}_F)$ restricting to $\omega$, and [2024, 200(3), no. 2] prescribes the central characters of the local components $\Pi_\nu$ of the transfer in terms of those of $\pi_\nu$.

## 74. Complex CM periods of a CM abelian scheme

*Chapter context.* The chapter on periods in a book on complex multiplication and special values of Hecke $L$-functions; it continues the chapter containing Definition #70. The reader knows: abelian schemes with CM by $\mathcal{O}_L$ of CM type $\Sigma$ and their duals (Definition #70); for a complex abelian variety $B$, the exact sequence $0\to H_1(B(\mathbb{C}),\mathbb{Z})\to\operatorname{Lie}(B/\mathbb{C})\xrightarrow{\exp}B(\mathbb{C})\to0$, the Hodge filtration $\omega_{B/\mathbb{C}}\subset H^1_{\mathrm{dR}}(B/\mathbb{C})$ and the integration pairing $H^1_{\mathrm{dR}}(B/\mathbb{C})\times H_1(B(\mathbb{C}),\mathbb{C})\to\mathbb{C}$; and the canonical perfect Betti pairing $\langle\cdot,\cdot\rangle_{\mathrm{top}}\colon H_1(B(\mathbb{C}),\mathbb{Z})\times H_1(B^\vee(\mathbb{C}),\mathbb{Z})\to2\pi i\mathbb{Z}$, compatible with the de Rham pairing (Deligne). The periods are defined here.

**Setting.** $L$ is a number field containing a CM field, $[L:\mathbb{Q}]=2d$, and $\Sigma$ is a CM type of $L$ (Definition #70). $R\subset\mathbb{C}$ is an $\mathcal{O}_{L^{\mathrm{Gal}}}[1/d_L]$-algebra, and $(A,\iota)$ is an abelian scheme over $R$ with CM by $\mathcal{O}_L$ of type $\Sigma$. Thus $(A^\vee,\iota^\vee)$, with $\iota^\vee(\ell)=\iota(\ell)^\vee$, has type $\overline\Sigma$. For $\Xi\subseteq J_L$ put $\mathbb{C}^{\Xi}:=\prod_{\sigma\in\Xi}\mathbb{C}=(L\otimes_{\mathbb{Q}}\mathbb{C})(\Xi)$. For an $\mathcal{O}_L$-module $M$ (with $\mathcal{O}_L$ acting through $\iota$, resp. $\iota^\vee$, on differentials by pull-back), $M(\sigma)$ denotes the $\sigma$-eigenspace as in Definition #70.

**Definition 74.1 (bases).** A *basis* $\omega(A)$ of $\omega_{A/R}$ is a family $(\omega(A)_\sigma)_{\sigma\in\Sigma}$ with $\omega(A)_\sigma\in H^0(\operatorname{Spec}R,\omega_{A/R}(\sigma))$ generating the invertible $R$-module $\omega_{A/R}(\sigma)$ for each $\sigma$. Here $\iota(\ell)^*$ acts on $\omega_{A/R}(\sigma)$ by $\sigma(\ell)$; Kings--Sprang write $\omega_{A/R}(-\sigma)$. Equivalently, a basis is an isomorphism $\operatorname{Lie}(A/R)\cong(\mathcal{O}_L\otimes R)(\Sigma)$. A basis $\omega(A^\vee)=(\omega(A^\vee)_\tau)_{\tau\in\overline\Sigma}$ of $\omega_{A^\vee/R}$ is defined in the same way. Bases exist after shrinking $\operatorname{Spec}R$ or enlarging $R$.

**Definition 74.2 (lattice structures).** Let $\mathfrak{a}$ be a fractional ideal of $L$. An *$\mathfrak{a}$-structure* on $A$ is an $\mathcal{O}_L$-linear isomorphism $\xi\colon\mathfrak{a}\xrightarrow{\sim}H_1(A(\mathbb{C}),\mathbb{Z})$. An *$\mathcal{O}_L$-structure* is the case $\mathfrak{a}=\mathcal{O}_L$. An *$L$-structure* is an $L$-linear isomorphism $L\xrightarrow{\sim}H_1(A(\mathbb{C}),\mathbb{Q})$; every $\mathfrak{a}$-structure induces one by $\otimes\mathbb{Q}$. Given an $L$-structure $\xi$, the *induced $L$-structure* $\xi^\vee\colon L\xrightarrow{\sim}H_1(A^\vee(\mathbb{C}),\mathbb{Q})$ on $A^\vee$ is characterised by
$$\langle\xi(x),\xi^\vee(y)\rangle_{\mathrm{top}}=2\pi i\operatorname{Tr}_{L/\mathbb{Q}}(xy)\qquad(x,y\in L).$$
It is $L$-linear because $\langle\iota(\ell)_*u,w\rangle_{\mathrm{top}}=\langle u,\iota^\vee(\ell)_*w\rangle_{\mathrm{top}}$. If $\xi$ is an $\mathfrak{a}$-structure, $\xi^\vee$ restricts to an $\mathfrak{a}^{-1}\mathfrak{d}_L^{-1}$-structure on $A^\vee$, where $\mathfrak{d}_L$ is the different.

**Definition 74.3 (period pairing).** Let $B/\mathbb{C}$ be an abelian variety with $\mathcal{O}_L$-action $j$. Define the $L\otimes\mathbb{C}$-valued pairing $\langle\cdot,\cdot\rangle_B\colon H^1_{\mathrm{dR}}(B/\mathbb{C})\times H_1(B(\mathbb{C}),\mathbb{Z})\to L\otimes\mathbb{C}=\mathbb{C}^{J_L}$ by
$$\langle\eta,\gamma\rangle_B(\sigma):=\int_\gamma\eta_\sigma,$$
where $\eta=\sum_\sigma\eta_\sigma$ is the decomposition into eigencomponents, $j(\ell)^*\eta_\sigma=\sigma(\ell)\eta_\sigma$. Equivalently, $\langle\cdot,\cdot\rangle_B$ is the unique $L\otimes\mathbb{C}$-bilinear pairing with $\operatorname{Tr}_{L\otimes\mathbb{C}/\mathbb{C}}\langle\eta,\gamma\rangle_B=\int_\gamma\eta$. For $B=A_{\mathbb{C}}$ its restriction to $\omega_{A/\mathbb{C}}$ takes values in $\mathbb{C}^\Sigma$, and for $B=A^\vee_{\mathbb{C}}$ in $\mathbb{C}^{\overline\Sigma}$. It extends $\mathbb{Q}$-linearly to rational homology.

**Definition 74.4 (CM periods).** Let $(A/R,\omega(A),\omega(A^\vee))$ be as above, with an $\mathcal{O}_L$-structure $\xi\colon\mathcal{O}_L\xrightarrow{\sim}H_1(A(\mathbb{C}),\mathbb{Z})$ and induced $\xi^\vee$. The *complex periods* are
$$\Omega:=\langle\omega(A),\xi(1)\rangle_A\in\mathbb{C}^{\Sigma},\qquad \Omega^\vee:=\langle\omega(A^\vee),\xi^\vee(1)\rangle_{A^\vee}\in\mathbb{C}^{\overline\Sigma},$$
that is, $\Omega(\sigma)=\int_{\xi(1)}\omega(A)_\sigma$ for $\sigma\in\Sigma$ and $\Omega^\vee(\tau)=\int_{\xi^\vee(1)}\omega(A^\vee)_\tau$ for $\tau\in\overline\Sigma$. All $\Omega(\sigma),\Omega^\vee(\tau)$ lie in $\mathbb{C}^\times$. *Multi-index notation*: for $\alpha=\sum_{\sigma\in\Sigma}\alpha(\sigma)\sigma\in I_\Sigma:=\mathbb{Z}[\Sigma]$ and $\beta\in I_{\overline\Sigma}$,
$$\Omega^\alpha:=\prod_{\sigma\in\Sigma}\Omega(\sigma)^{\alpha(\sigma)},\qquad\Omega^{\vee\beta}:=\prod_{\tau\in\overline\Sigma}\Omega^\vee(\tau)^{\beta(\tau)},\qquad|\beta|:=\sum_{\tau\in\overline\Sigma}\beta(\tau).$$
If $\alpha(\sigma)\ge1$ for all $\sigma$, put $(\alpha-\underline1)!:=\prod_{\sigma\in\Sigma}(\alpha(\sigma)-1)!$.

**Proposition 74.5.** (a) Use the coordinates $v\mapsto(\omega(A)_\sigma(v))_{\sigma\in\Sigma}$, an isomorphism $\operatorname{Lie}(A/\mathbb{C})\cong\mathbb{C}^\Sigma$. In them, $\xi(x)\in H_1(A(\mathbb{C}),\mathbb{Z})\subset\operatorname{Lie}(A/\mathbb{C})$ is $(\Omega(\sigma)\sigma(x))_{\sigma\in\Sigma}$. So the period lattice is $\Omega\cdot\Phi_\Sigma(\mathcal{O}_L)$ and $A(\mathbb{C})\cong\mathbb{C}^\Sigma/\Omega\,\Phi_\Sigma(\mathcal{O}_L)$.

(b) Changes of choices. Replacing $\omega(A)$ by $u\,\omega(A)$, with $u=(u_\sigma)\in((\mathcal{O}_L\otimes R)(\Sigma))^\times=\prod_\sigma R^\times$, multiplies $\Omega(\sigma)$ by $u_\sigma$; similarly for $\omega(A^\vee)$. Replacing $\xi$ by $\xi\circ\varepsilon$ with $\varepsilon\in\mathcal{O}_L^\times$ multiplies $\Omega(\sigma)$ by $\sigma(\varepsilon)$ and $\Omega^\vee(\tau)$ by $\tau(\varepsilon)^{-1}$. Hence $\Omega^\alpha\Omega^{\vee\beta}$ changes by $\prod_{\sigma\in J_L}\sigma(\varepsilon)^{(\alpha-\beta)(\sigma)}$, which is $1$ when the infinity type $\beta-\alpha$ is trivial on $\varepsilon$.

*Remarks.*

(1) Source and conventions. Definitions 74.1--74.4 follow Kings--Sprang [2025, 202(1), no. 1, Definition 1.15, Corollary 1.13, Definitions 4.3 and 4.5]. The displayed characterisation of $\xi^\vee$ is our explicit reading of their "induced $L$-structure": $H_1(A^\vee(\mathbb{C}),\mathbb{Q})$ is the $L$-dual of $H_1(A(\mathbb{C}),\mathbb{Q})$ via $\frac{1}{2\pi i}\langle\cdot,\cdot\rangle_{\mathrm{top}}$ and the trace form. A formaliser should fix the sign conventions of $\langle\cdot,\cdot\rangle_{\mathrm{top}}$ together with those of the de Rham pairing. Their Proposition 4.6 expresses $\Omega^\vee$ as $2\pi i$ times a de Rham pairing of $\omega(A)$ with $\omega(A^\vee)$, divided by the complex conjugate of $\Omega$; so $\Omega^\vee$ is essentially determined by $\Omega$, $\omega(A^\vee)$ and $2\pi i$.
(2) The papers fix a reference object $(\mathcal{A}/\mathcal{R},\omega(\mathcal{A}),\omega(\mathcal{A}^\vee))$ with an $\mathcal{O}_L$-structure, which exists by Definition #70, Remark (4). For a fractional ideal $\mathfrak{a}$ they also use $\mathcal{A}(\mathfrak{a})=\mathfrak{a}\otimes_{\mathcal{O}_L}\mathcal{A}$ with the induced $\mathfrak{a}$-structure and basis $\mathfrak{a}\otimes\omega(\mathcal{A})$. The algebraicity and integrality results (Theorems 4.10 and 5.27 there) concern $\frac{(\alpha-\underline1)!\,(2\pi i)^{|\beta|}}{\Omega^\alpha\Omega^{\vee\beta}}L_{\mathfrak{f}}(\chi,0)$ for critical infinity type $\mu=\beta-\alpha$, where $\beta\in I^+_{\overline\Sigma}$ and $\alpha-\underline1\in I^+_\Sigma$. The $p$-adic periods $\Omega_p,\Omega_p^\vee$ of Theorem 5.27 are defined analogously, comparing $\omega(\mathcal{A})$ with a canonical differential. They are not covered here.
(3) Classical case. For $L=K$ imaginary quadratic, $\Sigma=\{\sigma\}$ and an elliptic curve $E$ with CM by $\mathcal{O}_K$ and $H_1(E(\mathbb{C}),\mathbb{Z})=\mathcal{O}_K\gamma$, $\Omega=\int_\gamma\omega$ is the usual CM period, with period lattice $\Omega\,\mathcal{O}_K$. By Proposition 4.6 of the paper, $\Omega^\vee$ is then $2\pi i$ times a de Rham pairing divided by $\overline{\Omega}$.

## 75. Critical infinity types $\mathrm{Crit}_L(\Gamma)$ and the attached CM type

*Chapter context.* A chapter on algebraic Hecke characters and their critical $L$-values in a book on CM abelian varieties and special values. The reader knows number fields, their unit groups and embeddings, CM fields (totally imaginary quadratic extensions of totally real fields), and algebraic Hecke characters and their infinity types. CM types and the critical set are defined here.

**Conventions.** Fix an algebraic closure $\overline{\mathbb{Q}}\subset\mathbb{C}$ and write $c$ for complex conjugation. For a number field $L$ let $J_L=\operatorname{Hom}(L,\overline{\mathbb{Q}})$, a finite set of size $[L:\mathbb{Q}]$, with the involution $\sigma\mapsto\overline{\sigma}:=c\circ\sigma$. For $\Xi\subseteq J_L$ let $I_\Xi=\mathbb{Z}[\Xi]$ be the free abelian group on $\Xi$; we identify $\mu\in I_\Xi$ with the function $\Xi\to\mathbb{Z}$, $\xi\mapsto\mu(\xi)$, so that $\mu=\sum_{\xi\in\Xi}\mu(\xi)\xi$. Put $|\mu|=\sum_{\xi}\mu(\xi)$, let $I_\Xi^+=\{\mu\in I_\Xi:\mu(\xi)\ge 0\ \forall\xi\}$, and $I_L:=I_{J_L}$. We regard $I_\Xi\subseteq I_L$ by extension by zero. An element $\mu\in I_L$ defines a homomorphism $L^\times\to\overline{\mathbb{Q}}^\times$,
$$x\mapsto x^\mu:=\prod_{\sigma\in J_L}\sigma(x)^{\mu(\sigma)} .$$
For an extension $L/K$ let $N_{L/K}^*:I_K\to I_L$, $N_{L/K}^*(\mu_0)(\sigma)=\mu_0(\sigma|_K)$; then $x^{N^*_{L/K}\mu_0}=(N_{L/K}x)^{\mu_0}$.

**Definition 75.1 (CM types).** Let $K$ be a CM field. A *CM type* of $K$ is a subset $\Phi\subseteq J_K$ such that $J_K=\Phi\sqcup\overline{\Phi}$, where $\overline\Phi=\{\overline\sigma:\sigma\in\Phi\}$; equivalently $\Phi$ contains exactly one element of each pair $\{\sigma,\overline\sigma\}$ (these pairs have two elements because $K$ is totally imaginary).

**Proposition 75.2.** If a number field $L$ contains a CM field, then the compositum of all CM subfields of $L$ is a CM field. Hence $L$ has a unique maximal CM subfield $K$, and $L$ is totally imaginary. (Proof: if $K_i=F_i(\sqrt{-a_i})$ with $a_i\in F_i$ totally positive, then $K_1K_2$ is a totally imaginary quadratic extension of the totally real field $F_1F_2(\sqrt{a_1a_2})$.)

**Definition 75.3 (CM types of $L$).** Let $L$ contain a CM field and let $K$ be its maximal CM subfield. A *CM type of $L$* is a subset of $J_L$ of the form $\Sigma=\{\sigma\in J_L:\sigma|_K\in\Phi\}$ for a CM type $\Phi$ of $K$ (the type *lifted* from $\Phi$). Then $J_L=\Sigma\sqcup\overline\Sigma$ and $\overline\Sigma=\{\sigma:\sigma|_K\in\overline\Phi\}$. A subset $\Sigma\subseteq J_L$ with $J_L=\Sigma\sqcup\overline\Sigma$ need not be lifted from $K$, and such subsets are *not* called CM types of $L$.

**Definition 75.4 (Hecke character types).** Let $L$ and $K$ be as in 75.3. An element $\mu\in I_L$ is *of (algebraic) Hecke character type* if there are $\mu_0\in I_K$ and $w\in\mathbb{Z}$ with $\mu=N^*_{L/K}(\mu_0)$ and $\mu_0(\tau)+\mu_0(\overline\tau)=w$ for all $\tau\in J_K$. (Since $J_L\to J_K$, $\sigma\mapsto\sigma|_K$, is surjective, $\mu_0$ and $w$ are determined by $\mu$.) For a subgroup $\Gamma\subseteq\mathcal{O}_L^\times$ of finite index put
$$\mathrm{HChar}_L(\Gamma):=\{\mu\in I_L:\ \mu\text{ is of Hecke character type and }\varepsilon^\mu=1\text{ for all }\varepsilon\in\Gamma\}.$$

**Proposition 75.5 (Weil).** Let $L$ and $K$ be as in 75.3 and $\mu\in I_L$. Then $\mu$ is of Hecke character type if and only if $\varepsilon^\mu=1$ for all $\varepsilon$ in some finite-index subgroup of $\mathcal{O}_L^\times$; so $\mathrm{HChar}_L(\Gamma)=\{\mu\in I_L:\varepsilon^\mu=1\ \forall\varepsilon\in\Gamma\}$. If $\chi$ is an algebraic Hecke character of $L$ of conductor dividing $\mathfrak{f}$ with infinity type $\mu$ (so $\chi((\lambda))=\lambda^\mu$ for $\lambda\equiv1\bmod^\times\mathfrak{f}$), then $\mu\in\mathrm{HChar}_L(\mathcal{O}_{\mathfrak{f}}^\times)$, where $\mathcal{O}_{\mathfrak{f}}^\times=\{\varepsilon\in\mathcal{O}_L^\times:\varepsilon\equiv 1\bmod \mathfrak{f}\}$. (See Serre, *Abelian $\ell$-adic representations and elliptic curves*, Ch. II.)

**Definition 75.6 (critical types; attached CM type; decomposition).** Let $L$ contain a CM field, with maximal CM subfield $K$, and let $\Gamma\subseteq\mathcal{O}_L^\times$ have finite index.

(a) An element $\mu\in\mathrm{HChar}_L(\Gamma)$ is *critical* if
$$\Sigma_\mu:=\{\sigma\in J_L:\mu(\sigma)<0\}$$
is a CM type of $L$ in the sense of 75.3. Then $\Sigma_\mu$ is the *CM type attached to $\mu$*, and
$$\mathrm{Crit}_L(\Gamma):=\{\mu\in\mathrm{HChar}_L(\Gamma):\mu\text{ is critical}\}.$$
Equivalently, writing $\mu=N^*_{L/K}\mu_0$: for every $\tau\in J_K$ exactly one of $\mu_0(\tau),\mu_0(\overline\tau)$ is negative.

(b) Let $\mu\in\mathrm{Crit}_L(\Gamma)$ with $\Sigma=\Sigma_\mu$. Then $\mu(\sigma)\le-1$ for $\sigma\in\Sigma$ and $\mu(\sigma)\ge0$ for $\sigma\in\overline\Sigma$. Put $\underline{1}=\underline 1_\Sigma:=\sum_{\sigma\in\Sigma}\sigma\in I_\Sigma$. With $I_L=I_{\overline\Sigma}\oplus I_\Sigma$ there are unique $\beta,\alpha\in I_L$ with
$$\mu=\beta-\alpha,\qquad \beta\in I^+_{\overline\Sigma},\qquad \alpha-\underline 1\in I^+_\Sigma ,$$
namely $\beta=\sum_{\sigma\in\overline\Sigma}\mu(\sigma)\sigma$ and $\alpha=-\sum_{\sigma\in\Sigma}\mu(\sigma)\sigma$. Equivalently $\mu=\beta-\alpha'-\underline 1$ with $\beta\in I^+_{\overline\Sigma}$, $\alpha'=\alpha-\underline1\in I^+_\Sigma$. The notation "$\mu=\beta-\alpha\in\mathrm{Crit}_L(\Gamma)$" means that $\mu$ is critical and $(\beta,\alpha)$ is this decomposition relative to $\Sigma_\mu$.

(c) An algebraic Hecke character $\chi$ of $L$ is *critical* if its infinity type $\mu$ is critical. Its *attached CM type* is $\Sigma_\mu$.

*Remarks.* (1) In [2025, 202(1), no. 1] $L$ is any number field containing a CM field, and $\Gamma=\mathcal{O}_{\mathfrak{f}}^\times$ for the conductor $\mathfrak{f}$ of $\chi$ (Theorem 4.10). Theorem 5.27 there fixes a $p$-ordinary CM type $\Sigma$ and uses all critical $\chi$ with $\Sigma_\mu=\Sigma$ and conductor dividing $p^\infty\mathfrak{f}$. The paper states, citing Deligne, that $s=0$ is a critical point of $L_{\mathfrak{f}}(\chi,s)$ exactly when $\mu$ is critical. Totally imaginary fields with no CM subfield have no critical characters.

(2) Sign convention: here $\chi((\lambda))=\prod_\sigma\sigma(\lambda)^{\mu(\sigma)}$, with no inverse. Some sources (e.g. Katz's and Hida–Tilouine's $p$-adic interpolation papers) instead fix $\Sigma$ in advance, parametrise the critical range by other pairs of integers, and may use the inverse sign convention. Before reusing Tau Ceti's `AlgebraicInfinityType`, check which sign convention it uses.
(3) The weight $w$ can be any integer. For fixed $\Sigma$, the critical $\mu$ with $\Sigma_\mu=\Sigma$ are exactly the $\beta-\alpha$ with $\beta\in I^+_{\overline\Sigma}$ and $\alpha-\underline1\in I^+_\Sigma$ that are lifted from $K$, have constant $\mu_0(\tau)+\mu_0(\overline\tau)$, and are trivial on $\Gamma$. If $\Gamma'\subseteq\Gamma$ then $\mathrm{Crit}_L(\Gamma)\subseteq\mathrm{Crit}_L(\Gamma')$.
(4) The main theorems use multi-index notation: for $x=(x(\sigma))_{\sigma\in\Xi}\in\mathbb{C}^\Xi$ and $\gamma\in I_\Xi$, $x^\gamma=\prod_{\sigma\in\Xi}x(\sigma)^{\gamma(\sigma)}$, and $\gamma!=\prod_\sigma\gamma(\sigma)!$ for $\gamma\in I_\Xi^+$. So $(\alpha-\underline1)!=\prod_{\sigma\in\Sigma}(\alpha(\sigma)-1)!$ and $|\beta|=\sum_{\sigma\in\overline\Sigma}\beta(\sigma)$. Here $\Omega\in\mathbb{C}^\Sigma$ and $\Omega^\vee\in\mathbb{C}^{\overline\Sigma}$.
(5) The paper writes $J_L=\operatorname{Hom}(L,\overline{\mathbb{Q}})$ with $\overline{\mathbb{Q}}\subset\mathbb{C}$. This is the same as the ring maps $L\to\mathbb{C}$, and $\overline\sigma$ is then composition with complex conjugation.

## 76. The cuspidal automorphic representation $\pi_f$ attached to a newform

*Chapter context.* A chapter on "from modular forms to automorphic representations" in a book on automorphic forms on $\mathrm{GL}_2$. The reader knows classical cusp forms, newforms and their $L$-functions; adeles and ideles of $\mathbb{Q}$; the space $\mathcal{A}_0(\mathrm{GL}_2(\mathbb{Q})\backslash\mathrm{GL}_2(\mathbb{A}),\omega)$ of cuspidal automorphic forms with central character $\omega$, with its $(\mathfrak{gl}_2,\mathrm{O}(2))\times\mathrm{GL}_2(\mathbb{A}_f)$-action; and the local representation theory of $\mathrm{GL}_2(\mathbb{Q}_p)$ and $\mathrm{GL}_2(\mathbb{R})$ (unramified principal series, Steinberg, discrete series, local $L$-factors).

**Set-up.** Let $k\ge1$, $N\ge1$, and let $\chi$ be a Dirichlet character modulo $N$. Let $f(z)=\sum_{n\ge1}a_nq^n$ be a newform of weight $k$, level $N$ and character $\chi$, normalised so that $a_1=1$. Here $f|_k\gamma=\chi(d)f$ for $\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma_0(N)$, where for $g=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\mathrm{GL}_2^+(\mathbb{R})$
$$(f|_kg)(z)=\det(g)^{k/2}(cz+d)^{-k}f(gz).$$
This is a right action of $\mathrm{GL}_2^+(\mathbb{R})$, and positive scalars act trivially. Write $L(f,s)=\sum_n a_nn^{-s}$, so that $L(f,s)=\prod_p L_p(f,s)$ with $L_p(f,s)=(1-a_pp^{-s}+\chi(p)p^{k-1-2s})^{-1}$ for $p\nmid N$ and $L_p(f,s)=(1-a_pp^{-s})^{-1}$ for $p\mid N$.

**Definition 76.1 (adelic character and level).** Let $\widehat{\mathbb{Z}}=\prod_p\mathbb{Z}_p$. Since $\mathbb{A}^\times=\mathbb{Q}^\times\times\mathbb{R}_{>0}\times\widehat{\mathbb{Z}}^\times$, there is a unique continuous character $\omega_\chi:\mathbb{Q}^\times\backslash\mathbb{A}^\times\to\mathbb{C}^\times$ that is trivial on $\mathbb{R}_{>0}$ and satisfies $\omega_\chi(u)=\chi(u\bmod N)^{-1}$ for $u\in\widehat{\mathbb{Z}}^\times$. Then $\omega_\chi(\varpi_p)=\chi(p)$ for $p\nmid N$, where $\varpi_p$ is the idele equal to $p$ at $p$ and $1$ elsewhere. Let
$$K_0(N)=\Bigl\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\mathrm{GL}_2(\widehat{\mathbb{Z}}):c\equiv0\bmod N\Bigr\},\qquad \lambda_\chi\begin{pmatrix}a&b\\c&d\end{pmatrix}=\chi(d\bmod N)^{-1},$$
so that $\lambda_\chi$ is a character of $K_0(N)$.

**Proposition 76.2 (strong approximation).** $\mathrm{GL}_2(\mathbb{A})=\mathrm{GL}_2(\mathbb{Q})\cdot\bigl(\mathrm{GL}_2^+(\mathbb{R})\times K_0(N)\bigr)$, and $\mathrm{GL}_2(\mathbb{Q})\cap(\mathrm{GL}_2^+(\mathbb{R})\times K_0(N))=\Gamma_0(N)$, embedded diagonally. (This follows from strong approximation for $\mathrm{SL}_2$ and $\det K_0(N)=\widehat{\mathbb{Z}}^\times$.)

**Definition 76.3 (adelic lift).** The *adelic lift* of $f$ is the function $\varphi_f:\mathrm{GL}_2(\mathbb{A})\to\mathbb{C}$ given by
$$\varphi_f(\gamma\,g_\infty\,\kappa)=(f|_kg_\infty)(i)\,\lambda_\chi(\kappa)\qquad(\gamma\in\mathrm{GL}_2(\mathbb{Q}),\ g_\infty\in\mathrm{GL}_2^+(\mathbb{R}),\ \kappa\in K_0(N)).$$
This is well defined by 76.2 and the transformation law of $f$. Then $\varphi_f\in\mathcal{A}_0(\mathrm{GL}_2(\mathbb{Q})\backslash\mathrm{GL}_2(\mathbb{A}),\omega_\chi)$. It satisfies $\varphi_f(g\kappa)=\lambda_\chi(\kappa)\varphi_f(g)$ for $\kappa\in K_0(N)$, and $\varphi_f(gr_\theta)=e^{ik\theta}\varphi_f(g)$ for $r_\theta=\begin{pmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{pmatrix}$.

**Definition 76.4 (the representation $\pi_f$).** The *cuspidal automorphic representation attached to $f$*, written $\pi_f$ (or $\pi$), is the smallest subspace of $\mathcal{A}_0(\mathrm{GL}_2(\mathbb{Q})\backslash\mathrm{GL}_2(\mathbb{A}),\omega_\chi)$ that contains $\varphi_f$ and is stable under $\mathfrak{gl}_2(\mathbb{R})$, $\mathrm{O}(2)$ and right translation by $\mathrm{GL}_2(\mathbb{A}_f)$. It is a $(\mathfrak{gl}_2,\mathrm{O}(2))\times\mathrm{GL}_2(\mathbb{A}_f)$-module.

**Theorem 76.5.** Let $f$ be as above.

(a) $\pi_f$ is irreducible, so it is a cuspidal automorphic representation with central character $\omega_\chi$. Hence $\pi_f\cong\bigotimes'_v\pi_v$ (restricted tensor product).
(b) $\pi_\infty$ is the discrete series representation $D_k$ of weight $k$ (a limit of discrete series if $k=1$), with central character $\mathrm{sgn}^k$.
(c) For $p\nmid N$, $\pi_p$ is the unramified principal series $\pi(\mu_1,\mu_2)$ with $\mu_1(p)+\mu_2(p)=p^{(1-k)/2}a_p$ and $\mu_1(p)\mu_2(p)=\chi(p)$. The conductor of $\pi_f$ is $N$, and $\varphi_f$ is its new vector.
(d) $L(\pi_p,s)=L_p(f,s+\tfrac{k-1}{2})$ for every prime $p$. Hence the finite $L$-function satisfies
$$L(\pi_f,s)=\prod_pL(\pi_p,s)=L\bigl(f,s+\tfrac{k-1}{2}\bigr),\qquad\text{in particular } L(\pi_f,s-\tfrac12)=L(f,s)\text{ if }k=2 .$$
(e) By strong multiplicity one, $\pi_f$ is the unique cuspidal automorphic representation of $\mathrm{GL}_2(\mathbb{A})$ such that $L(\pi_p,s)=L_p(f,s+\frac{k-1}{2})$ for almost all $p$. The map $f\mapsto\pi_f$ is a bijection from newforms of weight $k$ (all levels and characters) onto cuspidal automorphic representations with $\pi_\infty\cong D_k$.
(References: Gelbart, *Automorphic forms on adele groups*; Bump, *Automorphic forms and representations*, Ch. 3. For (c) at $p\mid N$ use Casselman's theory of local newforms.)

*Remarks.* (1) [2020, 191(2), no. 1] uses only $k=2$ and $\chi$ trivial, so $\omega_\chi=1$ and $\lambda_\chi=1$. There $\pi$ is characterised by $L(\pi,s-\frac12)=L(f,s)$, and the conductor is $N$. When $N$ is squarefree and the central character is trivial, each $\pi_\ell$ with $\ell\mid N$ is $\mathrm{St}_\ell\otimes\mu$, with $\mathrm{St}_\ell$ the Steinberg ("special") representation and $\mu$ unramified with $\mu^2=1$. Since $L(\mathrm{St}_\ell\otimes\mu,s)=(1-\mu(\ell)\ell^{-1/2-s})^{-1}$, (d) gives $\mu(\ell)=a_\ell=-w_\ell$, where $w_\ell$ is the Atkin–Lehner eigenvalue. So $\pi_\ell$ is special iff $w_\ell=-1$, and is the twist by the unramified quadratic character iff $w_\ell=+1$, as in Theorems A and B.

(2) Conventions matter when $\chi\ne1$. Some sources use the character $\kappa\mapsto\chi(a\bmod N)$ of $K_0(N)$ instead; it agrees with $\lambda_\chi$ on $\Gamma_0(N)$. That lift has central character $\omega_\chi^{-1}$ and generates the contragredient $\pi_{\overline f}\cong\pi_f^\vee$, where $\overline f=\sum\overline{a_n}q^n$, not $\pi_f$. With the choices above, the unramified Hecke operator $\mathbf{1}_{K_p\operatorname{diag}(p,1)K_p}$ acts on $\varphi_f$ by $p^{1-k/2}a_p$, and $\varphi_f(g\varpi_p)=\chi(p)\varphi_f(g)$.
(3) Some authors use the unitary Hilbert space closure of $\pi_f$ in $L^2_0(\mathrm{GL}_2(\mathbb{Q})\backslash\mathrm{GL}_2(\mathbb{A}),\omega_\chi)$, a unitary representation of $\mathrm{GL}_2(\mathbb{A})$. Its $K$-finite vectors recover $\pi_f$. The "unitary" normalisation $L(\pi,s)$ makes the functional equation relate $s$ and $1-s$.

## 77. Emerton's completed cohomology of modular curves

*Chapter context.* A chapter on completed cohomology in a book on the $p$-adic Langlands programme for $\mathrm{GL}_2(\mathbb{Q})$. The reader knows modular curves $Y_K$ over $\mathbb{Q}$ for open compact $K\subseteq\mathrm{GL}_2(\mathbb{A}_f)$, their compactifications $X_K$, and their complex uniformisation $Y_K(\mathbb{C})=\mathrm{GL}_2(\mathbb{Q})\backslash(\mathbb{H}^{\pm}\times\mathrm{GL}_2(\mathbb{A}_f)/K)$, where $\mathbb{H}^\pm=\mathbb{C}\smallsetminus\mathbb{R}$ carries the Möbius action. The reader also knows neat level, singular and étale cohomology with finite coefficients and the comparison between them, and Hecke correspondences. Completed cohomology is defined here.

**Notation.** Fix a prime $p$ and an open compact subgroup $K^p=\prod_{\ell\ne p}K_\ell\subseteq\mathrm{GL}_2(\mathbb{A}_f^p)$ (the *tame level*). For an open compact subgroup $K_p\subseteq\mathrm{GL}_2(\mathbb{Q}_p)$ write $K^pK_p\subseteq\mathrm{GL}_2(\mathbb{A}_f)$. The set $\mathcal{K}_p$ of open compact subgroups of $\mathrm{GL}_2(\mathbb{Q}_p)$, ordered by reverse inclusion, is directed (closed under finite intersections). The subgroups $K_p$ for which $K^pK_p$ is neat are cofinal in it. If $K_p'\subseteq K_p$, the map $[x,h]\mapsto[x,h]$ is a finite map $\pi_{K_p',K_p}:Y_{K^pK_p'}\to Y_{K^pK_p}$ defined over $\mathbb{Q}$.

**Definition 77.1 (the $p$-power tower at finite coefficients).** For $i\ge0$ and $n\ge1$ put
$$\widetilde H^i(K^p,\mathbb{Z}/p^n):=\varinjlim_{K_p\in\mathcal{K}_p}H^i\bigl(Y_{K^pK_p}(\mathbb{C}),\mathbb{Z}/p^n\bigr),$$
where the colimit is formed along the pull-back maps $\pi_{K_p',K_p}^*$ and $H^i$ is singular (equivalently sheaf) cohomology of the constant sheaf. It carries the following commuting actions.

- *$\mathrm{GL}_2(\mathbb{Q}_p)$:* for $g\in\mathrm{GL}_2(\mathbb{Q}_p)$ and $K=K^pK_p$, right multiplication gives an isomorphism $r_g:Y_{gKg^{-1}}\to Y_K$, $[x,h]\mapsto[x,hg]$. Note that $gKg^{-1}=K^p(gK_pg^{-1})$. Set $g\cdot c:=r_g^*(c)$ for $c\in H^i(Y_K(\mathbb{C}),\mathbb{Z}/p^n)$. The $r_g^*$ are compatible with the transition maps, and $r_g^*r_h^*=r_{gh}^*$, so this is a left action on the colimit. It is smooth: a class coming from level $K^pK_p$ is fixed by $K_p$.
- *$G_{\mathbb{Q}}=\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$, with $\overline{\mathbb{Q}}\subset\mathbb{C}$:* via $H^i(Y_K(\mathbb{C}),\mathbb{Z}/p^n)\cong H^i_{\mathrm{\acute et}}(Y_{K,\overline{\mathbb{Q}}},\mathbb{Z}/p^n)$ (Artin comparison and invariance under change of algebraically closed field) and transport of structure. Each $H^i$ at finite level is a finite discrete $G_{\mathbb{Q}}$-module. Since the $\pi_{K_p',K_p}$ and $r_g$ are defined over $\mathbb{Q}$, this action commutes with that of $\mathrm{GL}_2(\mathbb{Q}_p)$.
- Hecke operators $T_\ell,S_\ell$ for $\ell\ne p$ with $K_\ell=\mathrm{GL}_2(\mathbb{Z}_\ell)$, commuting with both.

**Definition 77.2 (completed cohomology).** The *completed cohomology of tame level $K^p$* is
$$\widetilde H^i(K^p,\mathbb{Z}_p):=\varprojlim_{n}\widetilde H^i(K^p,\mathbb{Z}/p^n)=\varprojlim_n\varinjlim_{K_p}H^i\bigl(Y_{K^pK_p}(\mathbb{C}),\mathbb{Z}/p^n\bigr),$$
the limit taken along the maps induced by $\mathbb{Z}/p^{n+1}\to\mathbb{Z}/p^n$. It is a $\mathbb{Z}_p$-module with the inverse-limit topology of the discrete groups $\widetilde H^i(K^p,\mathbb{Z}/p^n)$, together with the induced action of $\mathrm{GL}_2(\mathbb{Q}_p)\times G_{\mathbb{Q}}$ and of the Hecke operators away from $p$. For a finite extension $E/\mathbb{Q}_p$ put $\widetilde H^i(K^p,E):=\widetilde H^i(K^p,\mathbb{Z}_p)\otimes_{\mathbb{Z}_p}E$. The *compactified variant* is defined in the same way with $X_{K^pK_p}(\mathbb{C})$ in place of $Y_{K^pK_p}(\mathbb{C})$.

**Proposition 77.3 (Emerton).** (a) For each $n$ there is a natural short exact sequence $0\to\widetilde H^i(K^p,\mathbb{Z}_p)/p^n\to\widetilde H^i(K^p,\mathbb{Z}/p^n)\to\widetilde H^{i+1}(K^p,\mathbb{Z}_p)[p^n]\to0$. In particular $\widetilde H^i(K^p,\mathbb{Z}_p)$ is $p$-adically complete and separated, and its inverse-limit topology is the $p$-adic topology.

(b) The action of $\mathrm{GL}_2(\mathbb{Q}_p)\times G_{\mathbb{Q}}$ on $\widetilde H^i(K^p,\mathbb{Z}_p)$ is continuous.
(c) $\widetilde H^i(K^p,E)$ is an $E$-Banach space (unit ball the image of $\widetilde H^i(K^p,\mathbb{Z}_p)$), and it is an admissible continuous representation of $\mathrm{GL}_2(\mathbb{Q}_p)$. Its reduction satisfies $(\widetilde H^i(K^p,\mathbb{Z}_p)/p)^{K_p}$ finite for all $K_p$.
(d) For modular curves, $\widetilde H^i(K^p,\mathbb{Z}_p)$ is $p$-torsion free.
(References: Emerton, *On the interpolation of systems of eigenvalues attached to automorphic Hecke eigenforms*, Invent. Math. 2006; Calegari–Emerton, *Completed cohomology — a survey*.)

*Remarks.* (1) [2026, 203(1), no. 3] uses $i=1$. The introduction states Theorem 1.1.2 with the open curves $Y_{K^pK_p}$; the body (Theorem 7.1.2) uses the complete curves $X_{K^pK_p}$. "$\rho$ appears in $\widetilde H^1(K^p,E)$" means $\operatorname{Hom}_{E[G_{\mathbb{Q}}]}(\rho,\widetilde H^1(K^p,E))\ne0$. A formaliser should fix which of the two versions is meant.

(2) The order of limits matters. $\varprojlim_n\varinjlim_{K_p}$ is in general different from $\varinjlim_{K_p}H^i(Y_{K^pK_p}(\mathbb{C}),\mathbb{Z}_p)$, which is not $p$-adically complete. For modular curves the integral cohomology at finite level is torsion free, and then completed cohomology is the $p$-adic completion of the latter.
(3) One may take the colimit only over a cofinal family, for example $K_p=1+p^m\mathrm{M}_2(\mathbb{Z}_p)$ with $m\ge 2$ (or $m\ge1$ for $p$ odd), for which $K^pK_p$ is neat and $Y_{K^pK_p}$ is a smooth affine curve over $\mathbb{Q}$.
(4) The same recipe defines $\widetilde H^i(K^p,\mathbb{Z}_p)=\varprojlim_n\varinjlim_{K_p}H^i(Y(K^pK_p),\mathbb{Z}/p^n)$ for any locally symmetric space $Y(K)=G(\mathbb{Q})\backslash(X_\infty\times G(\mathbb{A}_f)/K)$ of a reductive group $G$ over $\mathbb{Q}$, with an action of $G(\mathbb{Q}_p)$. A Galois action exists only when $Y(K)$ is a Shimura variety.
(5) Some authors use $r_{g^{-1}}^*$, or a right action. Any convention works if it is used consistently. The planned finite-level cohomology of modular curves (PR #871, ModularCurves roadmap) would supply the terms of the colimit.

## 78. Good reduction of a hypersurface in an abelian variety

*Chapter context.* A chapter on integral models and reduction of subvarieties in a book on arithmetic geometry of abelian varieties. The reader knows abelian varieties and abelian schemes, Néron models, scheme-theoretic images (closures), smooth morphisms, effective Cartier divisors and the Néron–Severi group. Good reduction of subvarieties is defined here.

**Set-up.** Let $K$ be a number field with ring of integers $\mathcal{O}_K$, and let $S$ be a finite set of maximal ideals of $\mathcal{O}_K$. Put $\mathcal{O}_{K,S}=\mathcal{O}_K[1/S]$, the ring of $S$-integers, and $B=\operatorname{Spec}\mathcal{O}_{K,S}$. Let $A$ be an abelian variety over $K$ with good reduction at every prime $\mathfrak{p}\notin S$. A *hypersurface* in $A$ is an effective Cartier divisor $H\subseteq A$, that is, a closed subscheme whose ideal sheaf is invertible. It is *smooth* if $H\to\operatorname{Spec}K$ is smooth. It *represents* $\phi\in\mathrm{NS}(A_{\overline K})$ if the class of $\mathcal{O}_A(H)$ in $\mathrm{NS}(A_{\overline K})$ equals $\phi$.

**Proposition 78.1 (the model).** There is an abelian scheme $\mathcal{A}\to B$ with generic fibre $A$, and it is the Néron model of $A$ over $B$. In particular, it is unique up to unique isomorphism. Any smooth proper $B$-scheme with generic fibre $A$ is isomorphic to $\mathcal{A}$, so $\mathcal{A}$ is "the unique smooth projective model" of $A$. It is projective over $B$. (See Bosch–Lütkebohmert–Raynaud, *Néron Models*, Ch. 1.) For each $\mathfrak{p}\notin S$, $\mathcal{A}\times_B\operatorname{Spec}\mathcal{O}_{K,(\mathfrak{p})}$ is the abelian scheme over the discrete valuation ring $\mathcal{O}_{K,(\mathfrak{p})}$ extending $A$.

**Definition 78.2 (closure).** Let $Z\subseteq A$ be a closed subscheme and $j:A=\mathcal{A}\times_B\operatorname{Spec}K\to\mathcal{A}$ the inclusion of the generic fibre. The *closure* $\mathcal{Z}$ of $Z$ in $\mathcal{A}$ is the scheme-theoretic image of $Z\hookrightarrow A\xrightarrow{j}\mathcal{A}$. Concretely, on an affine open $\operatorname{Spec}R\subseteq\mathcal{A}$, with $Z\cap\operatorname{Spec}(R\otimes_{\mathcal{O}_{K,S}}K)=V(J)$, the closure is $V(J\cap R)$, where $J\cap R$ means the preimage of $J$ under $R\to R\otimes_{\mathcal{O}_{K,S}}K$.

**Proposition 78.3.** $\mathcal{Z}$ is flat over $B$, and $\mathcal{Z}\times_B\operatorname{Spec}K=Z$. It is the unique closed subscheme of $\mathcal{A}$ that is flat over $B$ and has generic fibre $Z$. Its formation commutes with flat base change $B'\to B$, for example localisation at $\mathfrak{p}$ or completion. (Flatness holds because $\mathcal{O}_{\mathcal{Z}}$ is torsion free over the Dedekind ring $\mathcal{O}_{K,S}$; scheme-theoretic images of quasi-compact morphisms commute with flat base change.)

**Definition 78.4 (good reduction).** Let $H\subseteq A$ be a hypersurface (more generally, any closed subscheme), let $\mathcal{H}$ be its closure in $\mathcal{A}$, and let $\mathfrak{p}\notin S$.

(a) $H$ has *good reduction at $\mathfrak{p}$* if the structure morphism $\mathcal{H}\to B$ is smooth at every point of $\mathcal{H}$ lying over $\mathfrak{p}$. Equivalently, any one of the following holds:

- $\mathcal{H}\times_B\operatorname{Spec}\mathcal{O}_{K,(\mathfrak{p})}\to\operatorname{Spec}\mathcal{O}_{K,(\mathfrak{p})}$ is smooth;
- the special fibre $\mathcal{H}_{\mathfrak{p}}=\mathcal{H}\times_B\operatorname{Spec}k(\mathfrak{p})$ is smooth over $k(\mathfrak{p})$ (and then $H$ is smooth over $K$);
- the closure of $H_{K_{\mathfrak{p}}}$ in the abelian scheme over $\mathcal{O}_{K_{\mathfrak{p}}}$ is smooth over $\mathcal{O}_{K_{\mathfrak{p}}}$.

(b) $H$ has *good reduction outside $S$* if it has good reduction at every $\mathfrak{p}\notin S$, that is, if $\mathcal{H}\to B$ is smooth.

Then $\mathcal{H}$ is smooth and proper over $B$ of relative dimension $\dim A-1$. It is a relative effective Cartier divisor in $\mathcal{A}/B$, and for each $\mathfrak{p}\notin S$ its fibre $\mathcal{H}_{\mathfrak{p}}$ is a smooth hypersurface in the abelian variety $\mathcal{A}_{\mathfrak{p}}$ over $k(\mathfrak{p})$.

*Remarks.* (1) The equivalences in (a) hold for these reasons. Points of $\mathcal{H}$ over $\mathfrak{p}$ are exactly the points of $\mathcal{H}\times_B\operatorname{Spec}\mathcal{O}_{K,(\mathfrak{p})}$ not in the generic fibre. A flat morphism of finite presentation is smooth at a point iff its fibre through that point is smooth there. Smoothness descends along the faithfully flat map $\mathcal{O}_{K,(\mathfrak{p})}\to\mathcal{O}_{K_{\mathfrak{p}}}$, and closure commutes with flat base change (78.3). Being smooth at all points of the closed fibre is an open condition and $\mathcal{H}$ is proper over $B$, so good reduction at $\mathfrak{p}$ gives smoothness over a neighbourhood of $\mathfrak{p}$.

(2) The notion depends only on $H$, $A$ and $\mathfrak{p}$. It is defined at every prime where $A$ has good reduction and does not depend on the choice of $S$. Good reduction of $H$ at $\mathfrak{p}$ is not a property of $H$ as an abstract $K$-variety: it refers to the embedding $H\subseteq A$.
(3) [2025, 202(3), no. 1] (Theorem 1.1 = 9.4) uses smooth hypersurfaces $H\subseteq A$ defined over $K$ that represent a fixed ample class $\phi\in\mathrm{NS}(A)$ and have good reduction outside $S$, counted up to translation by $A(K)$. In its proof, such an $H$ gives an $\mathcal{O}_{K,S}$-point of the Hilbert scheme of smooth hypersurfaces of class $\phi$ in $\mathcal{A}/\mathcal{O}_{K,S}$, namely $\mathcal{H}$. Conversely, an $\mathcal{O}_{K,S}$-point $\mathcal{H}'\subseteq\mathcal{A}$ that is smooth over $B$ is flat, so it is the closure of its generic fibre. Hence "good reduction outside $S$" is the same as "extends to a smooth relative divisor of $\mathcal{A}/B$".
(4) For formalisation, $\mathcal{A}$ can come from the planned abelian-scheme models (PR #849/#852) and $\mathcal{H}$ from Tau Ceti's scheme-theoretic image. Mathlib's `AlgebraicGeometry.Scheme.Hom.smoothLocus` (an open subscheme, defined for morphisms locally of finite presentation) then gives a direct formulation. Condition (a) says that the preimage of $\mathfrak{p}$ under $\mathcal{H}\to B$ lies in the smooth locus. Condition (b) is `AlgebraicGeometry.Smooth` for $\mathcal{H}\to B$.

## 79. Minimal parabolic subgroups and the Langlands decomposition (real rank one)

*Chapter context.* A chapter on parabolic subgroups in a book on the structure of real semisimple Lie groups. The reader knows Lie groups and Lie algebras, Cartan involutions and the Cartan decomposition, maximal compact subgroups, restricted roots with respect to a maximal abelian subspace of $\mathfrak{p}$, and the Iwasawa decomposition. Minimal parabolic subgroups and their Langlands decomposition are defined here.

**Set-up.** Let $G$ be a connected semisimple Lie group with finite centre, for example $G=\mathbf{G}(\mathbb{R})^0$ for a semisimple algebraic group $\mathbf{G}$ over $\mathbb{R}$. Let $\mathfrak{g}$ be its Lie algebra and $\theta$ a Cartan involution, with $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$. Let $\Theta$ be the global Cartan involution with $d\Theta=\theta$, and $K=G^\Theta$ the corresponding maximal compact subgroup. Fix a maximal abelian subspace $\mathfrak{a}\subseteq\mathfrak{p}$; its dimension is the *real rank* of $G$. Let $\Sigma=\Sigma(\mathfrak{g},\mathfrak{a})$ be the restricted roots, so $\mathfrak{g}=\mathfrak{m}\oplus\mathfrak{a}\oplus\bigoplus_{\lambda\in\Sigma}\mathfrak{g}_\lambda$ with $\mathfrak{m}=Z_{\mathfrak{k}}(\mathfrak{a})$. Fix a positive system $\Sigma^+\subseteq\Sigma$ and put $\mathfrak{n}=\bigoplus_{\lambda\in\Sigma^+}\mathfrak{g}_\lambda$.

**Definition 79.1.** Put
$$M:=Z_K(\mathfrak{a})=\{k\in K:\operatorname{Ad}(k)H=H\ \text{for all }H\in\mathfrak{a}\},\qquad A:=\exp\mathfrak{a},\qquad N:=\exp\mathfrak{n},\qquad P:=MAN .$$

**Proposition 79.2.** (a) $M$ is a compact subgroup (possibly disconnected) with Lie algebra $\mathfrak{m}$. $A$ is a closed subgroup and $\exp:\mathfrak{a}\to A$ is an isomorphism of Lie groups, so $A\cong\mathbb{R}^{\dim\mathfrak a}$. $N$ is a closed, simply connected, nilpotent subgroup and $\exp:\mathfrak{n}\to N$ is a diffeomorphism.

(b) $M$ and $A$ commute, $M\cap A=\{1\}$, and $MA=Z_G(\mathfrak{a})\cong M\times A$. Both $M$ and $A$ normalise $N$.
(c) $P$ is a closed subgroup of $G$ and $N$ is normal in $P$. Multiplication $M\times A\times N\to P$ is a diffeomorphism. Moreover $P=N_G(\mathfrak{n})=N_G(P)$, and $P\cap\Theta(P)=MA$.
(d) $G=KAN=KP$, so $G/P\cong K/M$ is compact.
(e) Any two choices of $(\theta,\mathfrak{a},\Sigma^+)$ are conjugate under $G$. For fixed $\theta$, any two choices of $(\mathfrak{a},\Sigma^+)$ are conjugate under $K$.
(f) If $G=\mathbf{G}(\mathbb{R})^0$, then $P=G\cap\mathbf{P}(\mathbb{R})$ for a minimal $\mathbb{R}$-parabolic subgroup $\mathbf{P}$ of $\mathbf{G}$, and $N=R_u(\mathbf{P})(\mathbb{R})$. Also $A=\mathbf{S}(\mathbb{R})^0$ for the maximal $\mathbb{R}$-split torus $\mathbf{S}$ with Lie algebra $\mathfrak{a}$, and $MA=G\cap Z_{\mathbf{G}}(\mathbf{S})(\mathbb{R})$.
(See Knapp, *Lie groups beyond an introduction*, Ch. VII; Borel–Tits, *Groupes réductifs*, for (f).)

**Definition 79.3 (minimal parabolic; Langlands decomposition).** A *minimal parabolic subgroup* of $G$ is a subgroup $P=MAN$ obtained as in 79.1 from some choice of $(\theta,\mathfrak{a},\Sigma^+)$. By 79.2(e) these subgroups form a single conjugacy class: the conjugates of one of them. The decomposition $P=MAN$ is the *Langlands decomposition* of $P$. Here $M$ is compact, $A$ is a vector group (the identity component of the real points of a maximal $\mathbb{R}$-split torus), $N$ (also written $U$) is the *unipotent radical* of $P$, and $MA=Z_G(A)$ is the *Levi factor*. Given $P$, the group $N$ depends only on $P$. Given $P$ and $\theta$, one has $MA=P\cap\Theta(P)$, $\mathfrak{a}=\operatorname{Lie}(P\cap\Theta P)\cap\mathfrak{p}$ and $M=Z_K(\mathfrak{a})$, so the decomposition relative to $K$ is unique.

*Real rank one.* If $\dim\mathfrak{a}=1$, then $\Sigma\subseteq\{\pm\lambda,\pm2\lambda\}$, $\Sigma^+=\Sigma\cap\{\lambda,2\lambda\}$ and $\mathfrak{n}=\mathfrak{g}_\lambda\oplus\mathfrak{g}_{2\lambda}$. For fixed $A$ there are exactly two maximal unipotent subgroups normalised by $A$, namely $N$ and $\Theta(N)$, giving two minimal parabolics containing $MA$. Every proper parabolic subgroup is minimal, so "minimal" and "maximal" parabolic coincide.

**Example 79.4 ($G=\mathrm{SO}_0(n,1)$, $n\ge2$).** Let $J=\operatorname{diag}(1,\dots,1,-1)$ ($n$ entries $1$), $\mathrm{SO}(n,1)=\{g\in\mathrm{SL}_{n+1}(\mathbb{R}):g^{\mathsf T}Jg=J\}$, and let $G$ be its identity component. Take $\Theta(g)=(g^{\mathsf T})^{-1}$, so $K=\{\operatorname{diag}(k,1):k\in\mathrm{SO}(n)\}$. Write matrices in blocks of sizes $(n-1,1,1)$. Put $\mathfrak{a}=\mathbb{R}H_0$ with $H_0=E_{n,n+1}+E_{n+1,n}$. Then $A=\{a_t\}$, where $a_t$ is the identity on $e_1,\dots,e_{n-1}$ and acts on $\langle e_n,e_{n+1}\rangle$ by $\begin{pmatrix}\cosh t&\sinh t\\ \sinh t&\cosh t\end{pmatrix}$. Next, $M=\{\operatorname{diag}(m,1,1):m\in\mathrm{SO}(n-1)\}$. The roots are $\pm\lambda$ with $\lambda(H_0)=1$ and multiplicity $n-1$, and there is no $2\lambda$. Finally $N=\{u_v:v\in\mathbb{R}^{n-1}\}\cong\mathbb{R}^{n-1}$ is abelian with $u_vu_w=u_{v+w}$, where
$$u_v=\exp\begin{pmatrix}0&v&-v\\-v^{\mathsf T}&0&0\\-v^{\mathsf T}&0&0\end{pmatrix}=\begin{pmatrix}I_{n-1}&v&-v\\-v^{\mathsf T}&1-\tfrac12|v|^2&\tfrac12|v|^2\\-v^{\mathsf T}&-\tfrac12|v|^2&1+\tfrac12|v|^2\end{pmatrix}.$$
Then $P=MAN$ is the stabiliser in $G$ of the isotropic line $\mathbb{R}(e_n+e_{n+1})$, and $a_t(e_n+e_{n+1})=e^t(e_n+e_{n+1})$. Equivalently, $P$ is the stabiliser of a point of the sphere at infinity of hyperbolic $n$-space, and $G/P\cong K/M\cong S^{n-1}$.

*Remarks.* (1) In [2021, 193(3), no. 4] $G=\mathrm{SO}_0(n,1)$ with $n\ge3$, so $M\cong\mathrm{SO}(n-1)$ is connected. $A$ is a maximal $\mathbb{R}$-split torus chosen inside a given noncompact simple subgroup $W$, and $U$ is a maximal unipotent subgroup normalised by $A$ (one of the two in the rank-one paragraph above). $M$ is the compact factor of $Z_G(A)^0=M^0\times A$, and $P=MAU$. The paper calls $P$ both "minimal" and "maximal" parabolic. The compatibility condition in Theorem 1.6 uses only $P$, $U$ and the nontrivial subgroups $U'<U$. Remark 1.7 there notes that the result extends to all connected simple real-rank-one groups, which is why the general definition is given.

(2) For non-minimal parabolics the Langlands decomposition $P=MAN$ has noncompact reductive $M$. Here only the minimal case is needed.
(3) Tau Ceti's dynamic Levi decomposition attached to a cocharacter gives the algebraic version. A cocharacter $\nu:\mathbb{G}_m\to\mathbf{S}$ with $d\nu(1)=H$, where $\lambda(H)>0$ for all $\lambda\in\Sigma^+$, gives $\mathbf{P}=\mathbf{P}(\nu)$ with $\mathbf{U}(\nu)(\mathbb{R})=N$. Here $\mathbf{P}(\nu)$ is the set of $g$ for which $\lim_{t\to0}\nu(t)g\nu(t)^{-1}$ exists. If the library uses $t\to\infty$, replace $\nu$ by $\nu^{-1}$. Taking real points and the identity component of $G$ recovers 79.2(f).

## 80. The Néron–Tate (canonical) height on an abelian variety

*Chapter context.* A chapter on canonical heights in a book on heights in Diophantine geometry that treats number fields and function fields of one variable together. The reader knows absolute Weil heights on projective space and the Weil height machine $L\mapsto h_L$ for line bundles on projective varieties, defined up to bounded functions. The reader also knows abelian varieties (theorem of the cube, symmetric line bundles, $\mathrm{Pic}^0$, Néron–Severi group) and Jacobians with their theta divisors.

**Normalisation.** $K$ is either a number field or a *function field of one variable* over a field $k$, that is, a finitely generated extension of $k$ of transcendence degree $1$. For a finite extension $K'/K$, let $M_{K'}$ be its set of places, normalised as follows.

- *Number field case:* $\|\cdot\|_v$ is the usual absolute value at a real place and its square at a complex place. At a finite place it is $N_v^{-\mathrm{ord}_v(\cdot)}$, where $N_v$ is the size of the residue field.
- *Function field case:* places are the discrete valuations of $K'$ trivial on $k$, with $\|\cdot\|_v=e^{-[k(v):k]\,\mathrm{ord}_v(\cdot)}$, where $k(v)$ is the residue field. The factor is $[k(v):k]$ even if $K'$ contains a larger constant field.

The absolute height on $\mathbb{P}^n(\overline K)$ is $h(x)=\frac{1}{[K':K_0]}\sum_{v\in M_{K'}}\log\max_i\|x_i\|_v$, where $K'\ni x_0,\dots,x_n$ and $K_0=\mathbb{Q}$ (resp. $K_0=K$). For a projective $K$-variety $X$ and a line bundle $L$ on $X$, a *Weil height* $h_L:X(\overline K)\to\mathbb{R}$ is any representative of the height-machine class of $L$. Two Weil heights differ by a bounded function.

**Proposition 80.1 (Tate's limit lemma).** Let $S$ be a set, $\phi:S\to S$ a map, $d>1$ a real number, and $h:S\to\mathbb{R}$ a function with $\sup_{x\in S}|h(\phi(x))-d\,h(x)|=C<\infty$. Then $\hat h(x)=\lim_{n\to\infty}d^{-n}h(\phi^n(x))$ exists for all $x$, and $|\hat h-h|\le C/(d-1)$. Moreover $\hat h\circ\phi=d\,\hat h$, and $\hat h$ is the unique function with these last two properties.

**Recall.** For a line bundle $L$ on an abelian variety $A$ and $m\in\mathbb{Z}$, $[m]^*L\cong L^{\otimes(m^2+m)/2}\otimes([-1]^*L)^{\otimes(m^2-m)/2}$. So $[m]^*L\cong L^{\otimes m^2}$ if $L$ is *symmetric* ($[-1]^*L\cong L$), and $[m]^*L\cong L^{\otimes m}$ if $L$ is *antisymmetric* ($[-1]^*L\cong L^{-1}$, for example $L\in\mathrm{Pic}^0(A)$).

**Definition 80.2 (Néron–Tate height).** Let $A$ be an abelian variety over $K$, $L$ a line bundle on $A$, and $h_L$ any Weil height for $L$. For $x\in A(\overline K)$:

(a) if $L$ is symmetric, $\displaystyle\hat h_L(x):=\lim_{n\to\infty}4^{-n}\,h_L([2^n]x)$;
(b) if $L$ is antisymmetric, $\displaystyle\hat h_L(x):=\lim_{n\to\infty}2^{-n}\,h_L([2^n]x)$;
(c) in general, $L^{\otimes2}\cong(L\otimes[-1]^*L)\otimes(L\otimes[-1]^*L^{-1})$, where the first factor is symmetric and the second antisymmetric. Put $\hat h_L:=\frac12\bigl(\hat h_{L\otimes[-1]^*L}+\hat h_{L\otimes[-1]^*L^{-1}}\bigr)$.

The limits exist by 80.1 applied to $\phi=[2]$, since $h_L\circ[2]=h_{[2]^*L}+O(1)=4h_L+O(1)$ (resp. $2h_L+O(1)$). They do not depend on the choice of $h_L$ or on $L$ within its isomorphism class. The function $\hat h_L:A(\overline K)\to\mathbb{R}$ is the *Néron–Tate* (or *canonical*) *height* attached to $L$.

*Jacobians.* Let $C/K$ be a geometrically integral smooth projective curve of genus $g>1$, with Jacobian $J$, so $J(\overline K)=\mathrm{Pic}^0(C_{\overline K})$. For $x_0\in C(\overline K)$ let $\theta_{x_0}$ be the image of $C^{g-1}_{\overline K}\to J_{\overline K}$, $(x_1,\dots,x_{g-1})\mapsto\sum x_i-(g-1)x_0$, and let $\Theta=\mathcal{O}(\theta_{x_0}+[-1]^*\theta_{x_0})$. Then $\Theta$ is symmetric and ample, its isomorphism class does not depend on $x_0$, and it descends to $J$ over $K$. The *Néron–Tate height on $J$* is $\hat h:=\frac12\hat h_\Theta:J(\overline K)\to\mathbb{R}$.

**Proposition 80.3.** Let $L$ be symmetric.

(i) $\hat h_L-h_L$ is bounded, and $\hat h_L([m]x)=m^2\hat h_L(x)$ for all $m\in\mathbb{Z}$.
(ii) $\hat h_L$ is a quadratic form on the abelian group $A(\overline K)$. It satisfies $\hat h_L(x+y)+\hat h_L(x-y)=2\hat h_L(x)+2\hat h_L(y)$, and $\langle x,y\rangle_L=\frac12(\hat h_L(x+y)-\hat h_L(x)-\hat h_L(y))$ is symmetric $\mathbb{Z}$-bilinear with $\langle x,x\rangle_L=\hat h_L(x)$.
(iii) $\hat h_{L\otimes M}=\hat h_L+\hat h_M$, and $\hat h_{f^*L}=\hat h_L\circ f$ for homomorphisms $f:B\to A$ of abelian varieties. $\hat h_L$ is unchanged by replacing $K$ by a finite extension.
(iv) If $L$ is ample, then $\hat h_L\ge0$. In the number field case $\hat h_L(x)=0$ iff $x$ is torsion. In the function field case torsion points have height $0$, but the kernel can be larger; it is governed by the $\overline K/\overline k$-trace (Lang–Néron).

(v) If $L$ is antisymmetric, $\hat h_L$ is a homomorphism $A(\overline K)\to\mathbb{R}$.
(References: Bombieri–Gubler, *Heights in Diophantine geometry*, Ch. 9; Hindry–Silverman, *Diophantine geometry*, Part B; Lang, *Fundamentals of Diophantine geometry*.)

*Remarks.* (1) [2026, 203(1), no. 2] (Theorem 1.1) uses exactly the normalisation above (§4.3.1) and $\hat h=\frac12\hat h_\Theta$ on $J(\overline K)$. It evaluates $\hat h$ at $x-\alpha$ and at $(2g-2)\alpha-\omega_{C/K}$, both in $\mathrm{Pic}^0(C_{\overline K})$, where $\alpha\in\mathrm{Pic}(C_{\overline K})$ has degree $1$. If $\theta$ is a symmetric theta divisor then $\Theta\cong\mathcal{O}(2\theta)$, so $\hat h=\hat h_{\mathcal{O}(\theta)}$. In general $\hat h$ is the quadratic part of $\hat h_{\mathcal{O}(\theta)}$.

(2) The bilinear "Néron–Tate pairing" is normalised in two ways in the literature, with or without the factor $\frac12$ in (ii). For elliptic curves, $h(x(P))$ is a Weil height for $\mathcal{O}(2[O])$, so $\lim 4^{-n}h(x([2^n]P))$ equals $\hat h_{\mathcal{O}(2[O])}=2\hat h_{\mathcal{O}([O])}$. Both conventions occur. Compare with Tau Ceti's `WeierstrassCurve.Affine.Point.canonicalHeight` before identifying it with $\hat h_L$ for a specific $L$.
(3) Theorem 1.3 of the same paper uses the canonical adelic line bundle $\overline\Theta$ (Yuan–Zhang). It is obtained by running Tate's limit on metrics, or models, of a symmetric relatively ample bundle, and $\hat h_\Theta(x)$ is the height of $x$ with respect to $\overline\Theta$. That refinement is not needed to define $\hat h$.

## 81. The prismatic site and prismatic cohomology

*Chapter context.* A chapter on the relative prismatic site in a book on prismatic cohomology, following Bhatt–Scholze. The reader knows $\delta$-rings with Frobenius lift $\phi(x)=x^p+p\delta(x)$; derived $J$-completeness; prisms $(A,I)$ and bounded, perfect and crystalline prisms; $p$-adic formal schemes; Grothendieck sites and derived global sections; and derived categories $D(A)$. The fixed base is a bounded prism $(A,I)$. The ideal $(p,I)$ is finitely generated, $A/I$ has the $p$-adic topology, and $\phi_A$ is the Frobenius of $A$.

**Definition 81.1 (complete flatness; flat maps of prisms).** Let $J$ be a finitely generated ideal of a ring $R$. A complex $M\in D(R)$ is *$J$-completely flat* if $M\otimes^L_RN$ is concentrated in degree $0$ for every $R$-module $N$ killed by a power of $J$. Equivalently, $M\otimes^L_RR/J$ is concentrated in degree $0$ and is a flat $R/J$-module. It is *$J$-completely faithfully flat* if moreover $M\otimes^L_RR/J$ is faithfully flat over $R/J$. A map of prisms $(B,J)\to(C,J')$ is *(faithfully) flat* if $C$ is $(p,J)$-completely (faithfully) flat over $B$.

**Proposition 81.2 (rigidity).** If $(B,J)\to(C,J')$ is a map of prisms, then $J\otimes_BC\xrightarrow{\sim}J'$, so $J'=JC$. Conversely, let $(B,J)$ be a prism, $B\to C$ a map of $\delta$-rings and $C$ derived $(p,J)$-complete. Then $(C,JC)$ is a prism iff $C[J]=0$. If $(B,J)$ is bounded and $C$ is $(p,J)$-completely flat over $B$, then $C$ is discrete and $C[J]=0$, so $(C,JC)$ is a bounded prism. (Bhatt–Scholze, Lemmas 3.5 and 3.7.)

**Proposition 81.3 (the flat topology).** Let $(B,J)\to(C,JC)$ be a faithfully flat map of bounded prisms and $(B,J)\to(D,JD)$ any map of bounded prisms. Then the derived $(p,J)$-completion $E$ of $C\otimes^L_BD$ is discrete. Moreover $(E,JE)$ is a bounded prism, it is the pushout in the category of bounded prisms, and $(D,JD)\to(E,JE)$ is faithfully flat. Hence faithfully flat maps define a Grothendieck topology on the opposite of the category of bounded prisms, and $B\mapsto B$ and $B\mapsto B/J$ are sheaves with vanishing higher Čech cohomology. (Bhatt–Scholze, Corollary 3.12.)

**Definition 81.4 (prismatic site, structure sheaves, prismatic cohomology).** Let $X$ be a $p$-adic formal scheme over $\operatorname{Spf}(A/I)$.

(a) Let $\mathcal{C}_X$ be the category whose objects are pairs $(B,f)$ consisting of

- a bounded prism $(B,IB)$ with a map of prisms $(A,I)\to(B,IB)$, that is, a $\delta$-$A$-algebra $B$ (the ideal is forced to be $IB$ by 81.2), and
- a morphism of formal schemes $f:\operatorname{Spf}(B/IB)\to X$ over $\operatorname{Spf}(A/I)$.

A morphism $(B,f)\to(C,g)$ is a map of $\delta$-$A$-algebras $u:B\to C$ with $g=f\circ\operatorname{Spf}(\bar u)$, where $\bar u:B/IB\to C/IC$. The *prismatic site* $(X/A)_\Delta$ is the opposite category $\mathcal{C}_X^{\mathrm{op}}$. An object is often written $(\operatorname{Spf}B\leftarrow\operatorname{Spf}(B/IB)\to X)$.

(b) *Topology.* A covering is a single morphism of $(X/A)_\Delta$ given by some $u:B\to C$ such that $C$ is $(p,I)$-completely faithfully flat over $B$ (a *flat cover*). By 81.2 and 81.3, with the pushout $E$ equipped with $\operatorname{Spf}(E/IE)\to\operatorname{Spf}(C/IC)\to X$, this is a site.
(c) *Structure sheaves.* $\mathcal{O}_\Delta(B,f)=B$ and $\overline{\mathcal{O}}_\Delta(B,f)=B/IB$. These are sheaves by 81.3: $\mathcal{O}_\Delta$ is a sheaf of $I$-torsion-free $\delta$-$A$-algebras, $\overline{\mathcal{O}}_\Delta$ is a sheaf of $\mathcal{O}(X)$-algebras, and $\overline{\mathcal{O}}_\Delta=\mathcal{O}_\Delta\otimes_AA/I$. The Frobenius lifts $\phi_B$ commute with maps of $\delta$-rings, so they define a ring endomorphism $\phi:\mathcal{O}_\Delta\to\mathcal{O}_\Delta$. It is $\phi_A$-semilinear: $\phi(ab)=\phi_A(a)\phi(b)$ for $a\in A$.
(d) *Prismatic cohomology.* $R\Gamma_\Delta(X/A):=R\Gamma((X/A)_\Delta,\mathcal{O}_\Delta)\in D(A)$, the derived global sections of the sheaf of $A$-modules $\mathcal{O}_\Delta$, with $H^i_\Delta(X/A):=H^i(R\Gamma_\Delta(X/A))$. The map $\phi$ induces a $\phi_A$-linear endomorphism $\phi$ of $R\Gamma_\Delta(X/A)$, that is, an $A$-linear map $R\Gamma_\Delta(X/A)\to\phi_{A*}R\Gamma_\Delta(X/A)$. Its *linearisation* is the adjoint map $\phi_A^*R\Gamma_\Delta(X/A):=R\Gamma_\Delta(X/A)\otimes^L_{A,\phi_A}A\to R\Gamma_\Delta(X/A)$. Also $R\Gamma((X/A)_\Delta,\overline{\mathcal{O}}_\Delta)\cong R\Gamma_\Delta(X/A)\otimes^L_AA/I$ (*Hodge–Tate cohomology*).

*Smoothness.* $X$ is a *smooth $p$-adic formal scheme over $A/I$* if it is locally $\operatorname{Spf}R$ with $R$ a $p$-completely smooth $A/I$-algebra. This means $R$ is derived $p$-complete and $R\otimes^L_{A/I}A/(p,I)$ is concentrated in degree $0$ and smooth over $A/(p,I)$. Equivalently, by Elkik, $R$ is the $p$-adic completion of a smooth $A/I$-algebra.

*Remarks.* (1) In [2022, 196(3), no. 5] all main comparison theorems (Theorem 1.8) take $(A,I)$ bounded and $X$ smooth over $A/I$. Definition 4.1 there allows any $p$-adic formal $X$ and requires the $(B,IB)$ to be bounded; the introduction's Definition 1.6 suppresses "bounded". Prismatic cohomology of non-smooth $X$ is defined later in that paper by left Kan extension from the smooth case, rather than via this site.

(2) If $X=\operatorname{Spf}R$, then a morphism $\operatorname{Spf}(B/IB)\to X$ over $A/I$ is the same as an $A/I$-algebra map $R\to B/IB$; any such map is automatically continuous for the $p$-adic topologies. For smooth affine $X$, $R\Gamma_\Delta(X/A)$ is computed by the Čech–Alexander complex built from prismatic envelopes (Bhatt–Scholze, §4.3). This is the practical route to concrete statements.
(3) Using the étale, Nisnevich or Zariski topology on the same category gives the same cohomology of $\mathcal{O}_\Delta$ and $\overline{\mathcal{O}}_\Delta$ (Bhatt–Scholze, Remark 4.5). Variants include the absolute site, which drops $(A,I)$, and the perfect site, which uses only perfect prisms.
(4) $(X/A)_\Delta$ is a large category. A formalisation must bound the size of the prisms (a universe or cardinal cutoff); for smooth $X$ the result does not depend on this choice, as the Čech–Alexander description shows. $R\Gamma_\Delta(X/A)$ is derived $(p,I)$-complete and is a commutative algebra object of $D(A)$. The completed tensor products in Theorem 1.8 are derived $(p,I)$-adic, respectively $p$-adic, completions.
(5) The paper's subscript is a blackboard-bold prism symbol. Here it is written $\Delta$.

## 82. The quasi-split unitary group of a self-dual hermitian lattice

*Chapter context.* A chapter on integral models of unitary groups in a book on unitary Shimura varieties and locally symmetric spaces. The reader knows CM fields, hermitian and skew-hermitian forms and their unitary groups over fields, lattices and the different, Weil restriction, affine group schemes over $\mathbb{Z}$, quasi-split groups, and the real groups $\mathrm{U}(p,q)$. The integral group $G$ is defined here.

**Set-up.** Let $F$ be a CM field with maximal totally real subfield $F^+$, and write $x\mapsto\overline x$ for the nontrivial automorphism of $F/F^+$. Let $\mathfrak{d}^{-1}=\{x\in F:\operatorname{tr}_{F/\mathbb{Q}}(x\mathcal{O}_F)\subseteq\mathbb{Z}\}$ be the inverse different. Fix $n\ge1$ and let $V=F^{2n}$ with standard basis $e_1,\dots,e_{2n}$.

**Definition 82.1 (the forms).** Define $\langle\cdot,\cdot\rangle:V\times V\to F$ and $(\cdot,\cdot):V\times V\to\mathbb{Q}$ by
$$\langle x,y\rangle=\sum_{i=1}^n\bigl(x_i\overline{y}_{2n+1-i}-x_{2n+1-i}\overline{y}_i\bigr),\qquad (x,y)=\operatorname{tr}_{F/\mathbb{Q}}\langle x,y\rangle .$$
Then $\langle\cdot,\cdot\rangle$ is nondegenerate, $F$-linear in $x$ and conjugate-linear in $y$. It is *skew-hermitian*: $\langle y,x\rangle=-\overline{\langle x,y\rangle}$. The subspaces $\langle e_1,\dots,e_n\rangle$ and $\langle e_{n+1},\dots,e_{2n}\rangle$ are totally isotropic. The form $(\cdot,\cdot)$ is $\mathbb{Q}$-bilinear, alternating and nondegenerate, with $(ax,y)=(x,\overline ay)$ for $a\in F$. It determines $\langle\cdot,\cdot\rangle$, because $(ax,y)=\operatorname{tr}_{F/\mathbb{Q}}(a\langle x,y\rangle)$ for all $a\in F$.

**Definition 82.2 (self-dual lattices).** An *$\mathcal{O}_F$-lattice* in $V$ is a finitely generated $\mathcal{O}_F$-submodule $L\subseteq V$ with $FL=V$. Its dual is $L^\vee=\{v\in V:(v,L)\subseteq\mathbb{Z}\}$, and $L$ is *self-dual* if $L^\vee=L$. Equivalently, $(\cdot,\cdot)$ restricts to a perfect pairing $L\times L\to\mathbb{Z}$, so $L\to\operatorname{Hom}_{\mathbb{Z}}(L,\mathbb{Z})$ is bijective. Also equivalently, $\langle L,L\rangle\subseteq\mathfrak{d}^{-1}$ and $v\mapsto\langle\cdot,v\rangle$ is a bijection $L\to\operatorname{Hom}_{\mathcal{O}_F}(L,\mathfrak{d}^{-1})$.

**Example 82.3.** $L_0=\mathcal{O}_F^{\,n}\oplus(\mathfrak{d}^{-1})^{n}$ is self-dual: the first $n$ coordinates lie in $\mathcal{O}_F$ and the last $n$ in $\mathfrak{d}^{-1}$. This uses $\overline{\mathfrak{d}^{-1}}=\mathfrak{d}^{-1}$ and the fact that the trace dual of $\mathfrak{d}^{-1}$ is $\mathcal{O}_F$.

**Definition 82.4 (the group scheme $G$).** Fix a self-dual $\mathcal{O}_F$-lattice $L\subseteq V$. Let $(\cdot,\cdot)_R$ be the $R$-bilinear extension of $(\cdot,\cdot)|_{L\times L}$ to $L\otimes_{\mathbb{Z}}R$. The *(quasi-split) unitary group of $L$* is the functor on commutative rings
$$G(R)=\bigl\{g\in\operatorname{Aut}_{\mathcal{O}_F\otimes_{\mathbb{Z}}R}(L\otimes_{\mathbb{Z}}R):\ (gv,gw)_R=(v,w)_R\ \text{for all }v,w\in L\otimes_{\mathbb{Z}}R\bigr\}.$$
By bilinearity it suffices to take $v,w\in L$. Choose a $\mathbb{Z}$-basis of $L$, with Gram matrix $\Phi$ of $(\cdot,\cdot)$. Then $G$ is the closed subgroup scheme of $\mathrm{GL}_{\mathbb{Z}}(L)\cong\mathrm{GL}_{2n[F:\mathbb{Q}]}$ cut out by $g^{\mathsf T}\Phi g=\Phi$ together with commutation with the matrices of a $\mathbb{Z}$-basis of $\mathcal{O}_F$. So $G$ is an affine group scheme of finite type over $\mathbb{Z}$.

**Proposition 82.5.** (a) $G_{\mathbb{Q}}=\operatorname{Res}_{F^+/\mathbb{Q}}\mathrm{U}(V,\langle\cdot,\cdot\rangle)$, where for $F^+$-algebras $R'$ one sets $\mathrm{U}(V,\langle\cdot,\cdot\rangle)(R')=\{g\in\mathrm{GL}_{F\otimes_{F^+}R'}(V\otimes_{F^+}R'):\langle gv,gw\rangle=\langle v,w\rangle\}$. This is a connected reductive group. It is quasi-split, because $V$ has an $n$-dimensional totally isotropic subspace. For any $\delta\in F^\times$ with $\overline\delta=-\delta$, $\delta\langle\cdot,\cdot\rangle$ is hermitian with the same unitary group.

(b) $G(\mathbb{R})\cong\prod_{\tau:F^+\hookrightarrow\mathbb{R}}\mathrm{U}(n,n)$, since at each $\tau$ the hermitian form $\delta\langle\cdot,\cdot\rangle$ on $V\otimes_{F^+,\tau}\mathbb{R}\cong\mathbb{C}^{2n}$ has signature $(n,n)$.
(c) For every prime $p$, $G(\mathbb{Z}_p)=\{g\in G(\mathbb{Q}_p):g(L\otimes\mathbb{Z}_p)=L\otimes\mathbb{Z}_p\}$, a compact open subgroup of $G(\mathbb{Q}_p)$.
(d) Let $p$ split in an imaginary quadratic subfield $F_0\subseteq F$, as $p=\mathfrak{p}\overline{\mathfrak{p}}$. Then $L\otimes\mathbb{Z}_p=L_{\mathfrak{p}}\oplus L_{\overline{\mathfrak{p}}}$, where $L_{\mathfrak{p}}=\bigoplus_{w\mid\mathfrak{p}}L_w$ over the places $w$ of $F$ above $\mathfrak{p}$. The two summands are totally isotropic and in perfect duality under $(\cdot,\cdot)$. Restriction $g\mapsto g|_{L_{\mathfrak{p}}}$ gives isomorphisms
$$G(\mathbb{Z}_p)\cong\prod_{w\mid\mathfrak{p}}\mathrm{GL}_{2n}(\mathcal{O}_{F_w}),\qquad G(\mathbb{Q}_p)\cong\prod_{w\mid\mathfrak{p}}\mathrm{GL}_{2n}(F_w).$$
(e) If $p$ is unramified in $F$, then $G_{\mathbb{Z}_p}$ is a reductive group scheme, so $G(\mathbb{Z}_p)$ is hyperspecial. All self-dual lattices in $V\otimes\mathbb{Q}_p$ are $G(\mathbb{Q}_p)$-conjugate, so $G_{\mathbb{Z}_p}$ does not depend on $L$ up to isomorphism. The choice of $L$ matters only at primes ramified in $F$.

*Remarks.* (1) In [2024, 199(2), no. 1], $F$ contains an imaginary quadratic $F_0$, so $F=F^+F_0$, and the introduction's $G$ is exactly 82.4. The body uses the similitude group $\{(g,c)\in\mathrm{GL}_{\mathcal{O}_F}(L)(R)\times\mathbb{G}_m(R):(gv,gw)=c(v,w)\}$ and calls 82.4 $G^0$. The Hecke algebra $\bigotimes_{p\notin S,\ p\text{ split in }F_0}\mathbb{Z}[G(\mathbb{Q}_p)/\!/G(\mathbb{Z}_p)]$ is computed through 82.5(d). There $X_K=G(\mathbb{Q})\backslash(X\times G(\mathbb{A}_f)/K)$ has complex dimension $[F^+:\mathbb{Q}]n^2$, where $X=\prod_\tau X_{\tau,+}$ and $X_{\tau,+}$ is the space of positive definite $n$-dimensional subspaces of $V\otimes_{F^+,\tau}\mathbb{R}$.

(2) The paper gives "$L=\mathcal{O}_F^n\oplus I$" with $I$ the inverse different as an example of a self-dual lattice. For $L$ to be a lattice in $F^{2n}$ this must be read as $\mathcal{O}_F^n\oplus I^{\oplus n}$, as in 82.3.
(3) At primes ramified in $F$, $G_{\mathbb{Z}_p}$ need not be reductive. The theorems put these primes into $S$ and use only $G(\mathbb{Z}_p)$ for $p\notin S$.
(4) Formalisation: $G$ can be built as an affine group scheme in Tau Ceti's sense, from a hermitian lattice (PR #851), as the closed subgroup of $\mathrm{GL}(L)$ above. The functor-of-points description in 82.4 is the definition, and 82.5 consists of checkable properties.

## 83. Schwartz (Hecke) algebra of an adelic reductive group

*Chapter context.* A chapter on test functions for the trace formula in a book on automorphic forms. The reader knows connected reductive groups over a number field $F$ and their adelic points, Haar measures on $G(\mathbb{A}_F)$, the Hecke algebras $C_c^\infty(G(F_v))$ of $p$-adic groups acting on smooth representations, Lie groups and $U(\mathfrak{g})$, Casselman--Wallach representations of real reductive groups, and the space $L^2(G(F)\backslash G(\mathbb{A}_F),\omega)$ with its right regular representation $\mathrm{R}$; the archimedean Schwartz algebra and the adelic Schwartz algebra are defined here.

Throughout, $F$ is a number field, $G$ a connected reductive group over $F$, $F_\infty=F\otimes_{\mathbb{Q}}\mathbb{R}$, $\mathbf{G}:=(\mathrm{Res}_{F/\mathbb{Q}}G)_{\mathbb{R}}$ (an affine algebraic group over $\mathbb{R}$), $G_\infty:=G(F_\infty)=\mathbf{G}(\mathbb{R})=\prod_{v\mid\infty}G(F_v)$, so that $G(\mathbb{A}_F)=G_\infty\times G(\mathbb{A}_F^\infty)$. We fix Haar measures $dg_\infty$ on $G_\infty$ and $dg^\infty$ on $G(\mathbb{A}_F^\infty)$ and put $dg=dg_\infty\times dg^\infty$. All functions are complex-valued.

**Definition 83.1 (algebraic differential operators).** Let $\mathbb{C}[G_\infty]$ be the algebra of functions $G_\infty\to\mathbb{C}$ obtained by restricting elements of $\mathcal{O}(\mathbf{G})\otimes_{\mathbb{R}}\mathbb{C}$ to $\mathbf{G}(\mathbb{R})$. Let $\mathfrak{g}=\mathrm{Lie}(G_\infty)\otimes_{\mathbb{R}}\mathbb{C}$; $X\in\mathrm{Lie}(G_\infty)$ acts on $C^\infty(G_\infty)$ by $(Xf)(g)=\frac{d}{dt}f(g\exp(tX))|_{t=0}$, which extends to an action of $U(\mathfrak{g})$ by left-invariant differential operators. The algebra $\mathcal{D}(G_\infty)$ of *algebraic differential operators* on $G_\infty$ is the subalgebra of $\mathrm{End}_{\mathbb{C}}(C^\infty(G_\infty))$ generated by multiplication by elements of $\mathbb{C}[G_\infty]$ and by $U(\mathfrak{g})$. Every $D\in\mathcal{D}(G_\infty)$ is a finite sum $\sum_i \varphi_i\,u_i$ with $\varphi_i\in\mathbb{C}[G_\infty]$, $u_i\in U(\mathfrak{g})$; using right-invariant instead of left-invariant operators gives the same algebra (it is the complexified algebra of algebraic differential operators on the smooth affine $\mathbb{R}$-variety $\mathbf{G}$).

**Definition 83.2 (Schwartz functions on $G_\infty$).** A *Schwartz function* on $G_\infty$ is an $f\in C^\infty(G_\infty)$ such that
$$p_D(f):=\sup_{g\in G_\infty}|(Df)(g)|<\infty\qquad\text{for every }D\in\mathcal{D}(G_\infty).$$
The space $\mathcal{S}(G_\infty)$ of Schwartz functions is given the (Fr\'echet) topology defined by the seminorms $p_D$, $D\in\mathcal{D}(G_\infty)$.

**Proposition 83.3.** (i) $C_c^\infty(G_\infty)\subseteq\mathcal{S}(G_\infty)\subseteq L^1(G_\infty)$, and $C_c^\infty(G_\infty)$ is dense in $\mathcal{S}(G_\infty)$. (ii) For $f_1,f_2\in\mathcal{S}(G_\infty)$ the convolution $(f_1*f_2)(g)=\int_{G_\infty}f_1(gh^{-1})f_2(h)\,dh$ converges absolutely and lies in $\mathcal{S}(G_\infty)$; this makes $\mathcal{S}(G_\infty)$ an associative Fr\'echet algebra with continuous multiplication. (iii) For every Casselman--Wallach representation $(\pi,V)$ of $G_\infty$ and $f\in\mathcal{S}(G_\infty)$, $\pi(f)v:=\int_{G_\infty}f(g)\pi(g)v\,dg$ converges absolutely and defines a continuous operator on $V$, and $\pi(f_1*f_2)=\pi(f_1)\pi(f_2)$. (Schwartz functions decay faster than every power of an algebraic norm on $G_\infty$, while Haar measure and matrix coefficients of $\pi$ grow at most polynomially; see Wallach, *Real reductive groups II*, and Aizenbud--Gourevitch, *Schwartz functions on Nash manifolds*.)

**Definition 83.4 (the adelic Schwartz algebra).** Let $\mathcal{H}(G(\mathbb{A}_F^\infty))=C_c^\infty(G(\mathbb{A}_F^\infty))$ be the space of locally constant compactly supported functions on $G(\mathbb{A}_F^\infty)$ under convolution with respect to $dg^\infty$ (it is the restricted tensor product $\bigotimes'_{v\nmid\infty}C_c^\infty(G(F_v))$ with respect to the functions $\mathbf{1}_{K_v}$, $K_v$ hyperspecial of volume $1$ for almost all $v$). The *space of Schwartz test functions* on $G(\mathbb{A}_F)$ is the algebraic tensor product
$$\mathcal{S}(G(\mathbb{A}_F)):=\mathcal{S}(G_\infty)\otimes_{\mathbb{C}}C_c^\infty(G(\mathbb{A}_F^\infty)),$$
viewed as a space of functions on $G(\mathbb{A}_F)$ via $(f_\infty\otimes f^\infty)(g_\infty,g^\infty)=f_\infty(g_\infty)f^\infty(g^\infty)$; thus its elements are exactly the finite sums $\sum_i f_{\infty,i}\otimes f^\infty_i$. It is an associative $\mathbb{C}$-algebra under $(f_1*f_2)(g)=\int_{G(\mathbb{A}_F)}f_1(gh^{-1})f_2(h)\,dh$, and $(a\otimes b)*(c\otimes d)=(a*c)\otimes(b*d)$. For an open compact subgroup $K\subseteq G(\mathbb{A}_F^\infty)$ (acting on the finite-adelic factor), the *Schwartz--Hecke algebra of level $K$* is the subalgebra
$$\mathcal{S}(G(\mathbb{A}_F))_K:=\{f\in\mathcal{S}(G(\mathbb{A}_F)) : f(kgk')=f(g)\ \text{for all }k,k'\in K,\ g\in G(\mathbb{A}_F)\}=\mathcal{S}(G_\infty)\otimes_{\mathbb{C}}C_c(K\backslash G(\mathbb{A}_F^\infty)/K).$$

**Definition 83.5 (actions).** (a) Let $Z$ be the maximal $F$-split torus in the centre of $G$ and $\omega:Z(F)\backslash Z(\mathbb{A}_F)\to\mathbb{C}^\times$ a unitary character. For $f\in\mathcal{S}(G(\mathbb{A}_F))$ and $\phi\in L^2(G(F)\backslash G(\mathbb{A}_F),\omega)$ put $(\mathrm{R}(f)\phi)(x)=\int_{G(\mathbb{A}_F)}f(g)\phi(xg)\,dg$. Then $\mathrm{R}(f)$ is bounded with $\|\mathrm{R}(f)\|\le\|f\|_{L^1}$ and $\mathrm{R}(f_1*f_2)=\mathrm{R}(f_1)\mathrm{R}(f_2)$. If $f\in\mathcal{S}(G(\mathbb{A}_F))_K$, then $\mathrm{R}(f)$ maps $L^2$ into the closed subspace $L^2(G(F)\backslash G(\mathbb{A}_F)/K,\omega)$ of $\mathrm{R}(K)$-invariants and vanishes on its orthogonal complement. (b) For an admissible representation $\pi=\pi_\infty\otimes\pi^\infty$ of $G(\mathbb{A}_F)$, with $\pi_\infty$ a Casselman--Wallach representation of $G_\infty$ and $\pi^\infty$ a smooth admissible representation of $G(\mathbb{A}_F^\infty)$, put $\pi(f_\infty\otimes f^\infty)=\pi_\infty(f_\infty)\otimes\pi^\infty(f^\infty)$ and extend linearly; for $f\in\mathcal{S}(G(\mathbb{A}_F))_K$ the image of $\pi(f)$ lies in $\pi_\infty\otimes(\pi^\infty)^K$.

**Definition 83.6 (multipliers).** For an associative $\mathbb{C}$-algebra $\mathcal{S}$, a *multiplier* of $\mathcal{S}$ is a $\mathbb{C}$-linear map $\mu\star:\mathcal{S}\to\mathcal{S}$, $f\mapsto\mu\star f$, such that $\mu\star(f*g)=(\mu\star f)*g=f*(\mu\star g)$ for all $f,g\in\mathcal{S}$. Under composition the multipliers form a unital $\mathbb{C}$-algebra $\mathrm{Mul}(\mathcal{S})$.

*Remarks.* (1) $\mathcal{S}(G_\infty)$ is *not* the Harish-Chandra Schwartz space: it is contained in $\bigcap_{p>0}\mathcal{C}^p(G_\infty)$, where $\mathcal{C}^p$ is Harish-Chandra's $L^p$-Schwartz space, with equality iff the centre of $G_\infty$ is compact. It is also not the Schwartz space of a real vector space (as in Mathlib) transported along a chart. Example: for $G=\mathrm{GL}_1$ over $\mathbb{Q}$, $\mathbb{C}[G_\infty]=\mathbb{C}[x,x^{-1}]$ and $\mathcal{S}(\mathbb{R}^\times)$ consists of the smooth $f$ with $x^m(x\,d/dx)^kf$ bounded for all $m\in\mathbb{Z}$, $k\ge0$ (rapid decay at $0$ and at $\infty$). (2) Equivalently (Sobolev), $\mathcal{S}(G_\infty)=\{f\in L^2(G_\infty): Df\in L^2(G_\infty)\ \forall D\in\mathcal{D}(G_\infty)\}$ with $Df$ taken distributionally, and the seminorms $f\mapsto\|Df\|_{L^2}$ define the same topology. (3) Only the archimedean component is allowed to be non-compactly supported; $\mathcal{S}(G(\mathbb{A}_F))_K$ contains $C_c^\infty(G_\infty)\otimes C_c(K\backslash G(\mathbb{A}^\infty_F)/K)$. The tensor product is algebraic (no completion). The algebra is in general non-unital and non-commutative. Changing Haar measures rescales the product only. (4) In [2021, 194(2), no. 5] (Definition 3.1 and Section 3.1) $dg=\prod_v dg_v$ with $\mathrm{vol}(K_{0,v})=1$ at the unramified primes; Theorem 1.1 there produces, for any open compact $K$, a multiplier $\mu\star\in\mathrm{Mul}(\mathcal{S}(G(\mathbb{A}_F))_K)$ such that $\mathrm{R}(\mu\star f)$ has image in the $\pi$-nearly isotypic cuspidal subspace (Definition #90) and $\pi(\mu\star f)=\pi(f)$. The archimedean parts of these multipliers act by $\pi(\mu\star f)=\mu(\chi_\pi)\pi(f)$ through infinitesimal characters, and the authors stress that the method fails for compactly supported test functions.

## 84. Selmer sections and the localisation map

*Chapter context.* A chapter on local-to-global conditions in a book on the arithmetic of fundamental groups (Grothendieck's section conjecture). The reader knows the \'etale fundamental group, the fundamental exact sequence of a geometrically connected variety over a field, the set of Galois sections up to conjugacy, the section attached to a rational point, and decomposition groups $G_{K_u}\hookrightarrow G_K$; the Selmer condition and the localisation maps are defined here.

*Notation recalled from earlier chapters.* For a field $k$ of characteristic $0$ with algebraic closure $\bar k$, $G_k=\mathrm{Gal}(\bar k/k)$, a geometrically connected variety $X/k$ and a geometric point $\bar x$ of $X_{\bar k}$, there is an exact sequence of profinite groups
$$1\to\pi_1^{\mathrm{\acute et}}(X_{\bar k},\bar x)\to\pi_1^{\mathrm{\acute et}}(X,\bar x)\xrightarrow{\ \mathrm{pr}\ }G_k\to1.$$
$\mathrm{Sec}(X/k)$ is the set of continuous homomorphisms $s:G_k\to\pi_1^{\mathrm{\acute et}}(X,\bar x)$ with $\mathrm{pr}\circ s=\mathrm{id}$, modulo conjugation by $\pi_1^{\mathrm{\acute et}}(X_{\bar k},\bar x)$; up to canonical bijection it does not depend on $\bar x$. Each $a\in X(k)$ gives a class $s_a\in\mathrm{Sec}(X/k)$ (functoriality for $a:\mathrm{Spec}\,k\to X$, transported along an \'etale path), and we write $\kappa_{X/k}:X(k)\to\mathrm{Sec}(X/k)$, $a\mapsto s_a$.

Now let $K$ be a number field with algebraic closure $\bar K$, and $Y/K$ a smooth projective geometrically connected curve of genus $g\ge2$. For a place $u$ of $K$ let $K_u$ be the completion, $\bar K_u$ an algebraic closure, and fix a $K$-embedding $\iota_u:\bar K\hookrightarrow\bar K_u$; restriction along $\iota_u$ identifies $G_u:=\mathrm{Gal}(\bar K_u/K_u)$ with a decomposition subgroup of $G_K$.

**Proposition 84.1 (restriction of sections).** Let $\bar\eta$ be a geometric point of $Y_{\bar K_u}$, also viewed (via $\iota_u$) as a geometric point of $Y_{\bar K}$ and of $Y$. The base change morphisms induce a commutative diagram with exact rows
$$\begin{tikzcd} 1\arrow[r] & \pi_1^{\mathrm{\acute et}}(Y_{\bar K_u},\bar\eta)\arrow[r]\arrow[d,"\sim"] & \pi_1^{\mathrm{\acute et}}(Y_{K_u},\bar\eta)\arrow[r]\arrow[d] & G_u\arrow[r]\arrow[d,hook] & 1\\ 1\arrow[r] & \pi_1^{\mathrm{\acute et}}(Y_{\bar K},\bar\eta)\arrow[r] & \pi_1^{\mathrm{\acute et}}(Y,\bar\eta)\arrow[r] & G_K\arrow[r] & 1 \end{tikzcd}$$
in which the left arrow is an isomorphism (invariance of the fundamental group of a proper variety under extension of algebraically closed fields of characteristic $0$, SGA 1, Exp. X). Hence $\pi_1^{\mathrm{\acute et}}(Y_{K_u},\bar\eta)\cong\pi_1^{\mathrm{\acute et}}(Y,\bar\eta)\times_{G_K}G_u$, and every section $s$ of the lower row restricts to a unique section $s|_{G_u}$ of the upper row lifting $s|_{G_u}:G_u\to\pi_1^{\mathrm{\acute et}}(Y,\bar\eta)$. This gives a well-defined map
$$\mathrm{res}_u:\mathrm{Sec}(Y/K)\to\mathrm{Sec}(Y_{K_u}/K_u),\qquad [s]\mapsto[s|_{G_u}].$$
Replacing $\iota_u$ by $\iota_u\circ\sigma$ ($\sigma\in G_K$) or changing $\bar\eta$ changes $\mathrm{res}_u$ only by the canonical bijections of the section sets.

**Proposition 84.2 (local injectivity).** If $u$ is a finite place, $\kappa_{Y_{K_u}/K_u}:Y(K_u)\to\mathrm{Sec}(Y_{K_u}/K_u)$ is injective. (If $s_y=s_{y'}$, the Kummer class of the divisor class $[y]-[y']\in J(K_u)$, $J$ the Jacobian, vanishes in $H^1(K_u,\widehat{T}J)$; the Kummer map is injective because the compact $p$-adic Lie group $J(K_u)$ has no non-zero divisible elements, and Abel--Jacobi is injective as $g\ge1$.)

**Definition 84.3 (Selmer sections; localisation).** A class $s\in\mathrm{Sec}(Y/K)$ is *Selmer* if for every place $u$ of $K$, archimedean or not, $\mathrm{res}_u(s)$ lies in the image of $\kappa_{Y_{K_u}/K_u}$, i.e. there is $y_u\in Y(K_u)$ with $\mathrm{res}_u(s)=s_{y_u}$. The set of Selmer sections is
$$\mathrm{Sec}^{\mathrm{Sel}}(Y/K):=\{s\in\mathrm{Sec}(Y/K): s\text{ is Selmer}\}\subseteq\mathrm{Sec}(Y/K).$$
For a finite place $u$, the *localisation map* is
$$\mathrm{loc}_u:\mathrm{Sec}^{\mathrm{Sel}}(Y/K)\to Y(K_u),\qquad \mathrm{loc}_u(s)=\text{the unique }y_u\in Y(K_u)\text{ with }\mathrm{res}_u(s)=s_{y_u},$$
which is well defined by Proposition 84.2. By Proposition 84.1, neither the Selmer condition nor $\mathrm{loc}_u$ depends on the choices of $\iota_u$ and base points.

*Remarks.* (1) For $y\in Y(K)$, $s_y$ is Selmer and $\mathrm{loc}_u(s_y)$ is the image of $y$ in $Y(K_u)$; so $Y(K)\to\mathrm{Sec}^{\mathrm{Sel}}(Y/K)$, and the section conjecture predicts $Y(K)\cong\mathrm{Sec}(Y/K)$ (hence $\mathrm{Sec}^{\mathrm{Sel}}=\mathrm{Sec}$). $\mathrm{Sec}(Y/K)$ may be empty. (2) At a complex place $G_u=1$ and the condition is vacuous. At a real place the condition is non-trivial, but points in one connected component of $Y(K_u)$ give the same section class, so $y_u$ is determined at most up to its component; this is why $\mathrm{loc}_u$ is only defined at finite places. Collecting all places gives the total localisation $\mathrm{Sec}^{\mathrm{Sel}}(Y/K)\to\prod_{u\nmid\infty}Y(K_u)\times\prod_{u\mid\infty}\pi_0(Y(K_u))$, whose image is the finite descent locus by a theorem of Harari and Stix. (3) For formalisation: $\mathrm{Sec}(Y/K)$ is a quotient of a set of continuous sections by a conjugation action; "Selmer" is a predicate on it, defined via the restriction map of Proposition 84.1, and $\mathrm{loc}_u$ needs the injectivity of Proposition 84.2 (or, without it, can be defined as a relation). The definition makes sense for any geometrically connected smooth projective curve of genus $\ge1$ (more generally, the Selmer condition makes sense for any geometrically connected proper variety). (4) In [2025, 201(1), no. 2] (Definition 1.1, Theorem A) $Y$ is a smooth projective (geometrically connected) curve of genus $\ge2$ over a number field $K$ with no CM subfield, and the theorem asserts that $\mathrm{loc}_v(\mathrm{Sec}^{\mathrm{Sel}}(Y/K))$ is finite for every finite place $v$.

## 85. Stable Faltings height of an abelian variety

*Chapter context.* A chapter on heights of abelian varieties in a book on Arakelov geometry and Diophantine geometry. The reader knows abelian varieties, N\'eron models over Dedekind schemes (with identity section and the N\'eron mapping property), the definition of semistable reduction, rings of integers and regular projective curves over a field, and holomorphic forms on complex tori. Arakelov degrees on $\mathrm{Spec}\,\mathcal{O}_L$ and the Faltings height are defined here.

**Definition 85.1 (metrised line bundles and arithmetic degree).** Let $L$ be a number field. A *metrised line bundle* $\overline{\mathcal{L}}=(\mathcal{L},(\|\cdot\|_\sigma)_\sigma)$ on $\mathrm{Spec}\,\mathcal{O}_L$ is a projective $\mathcal{O}_L$-module $\mathcal{L}$ of rank $1$ together with, for every field embedding $\sigma:L\hookrightarrow\mathbb{C}$, a norm $\|\cdot\|_\sigma$ on the one-dimensional complex vector space $\mathcal{L}_\sigma:=\mathcal{L}\otimes_{\mathcal{O}_L,\sigma}\mathbb{C}$. Its *arithmetic degree* is
$$\widehat{\deg}(\overline{\mathcal{L}}):=\log\#(\mathcal{L}/\mathcal{O}_Ls)-\sum_{\sigma:L\hookrightarrow\mathbb{C}}\log\|s\otimes1\|_\sigma\in\mathbb{R}$$
for any $0\ne s\in\mathcal{L}$; the sum runs over all $[L:\mathbb{Q}]$ embeddings (both members of each complex-conjugate pair).

**Proposition 85.2.** (i) $\widehat{\deg}(\overline{\mathcal{L}})$ does not depend on $s$ (product formula). (ii) If $L'/L$ is finite and $\overline{\mathcal{L}}'$ is $\mathcal{L}\otimes_{\mathcal{O}_L}\mathcal{O}_{L'}$ with $\|\cdot\|_{\sigma'}:=\|\cdot\|_{\sigma'|_L}$ (via $\mathcal{L}'_{\sigma'}=\mathcal{L}_{\sigma'|_L}$), then $\widehat{\deg}(\overline{\mathcal{L}}')=[L':L]\,\widehat{\deg}(\overline{\mathcal{L}})$. (iii) If $\mathcal{L}'\subseteq\mathcal{L}$ is a submodule of finite index with the same norms, $\widehat{\deg}(\overline{\mathcal{L}}')=\widehat{\deg}(\overline{\mathcal{L}})-\log\#(\mathcal{L}/\mathcal{L}')$.

**Definition 85.3 (function field case).** Let $k$ be a field and $K$ a *function field of one variable over $k$*, i.e. a finitely generated field extension of transcendence degree $1$. For a finite extension $K'/K$ let $B'$ be the regular projective integral curve over $k$ with function field $K'$ (unique up to unique isomorphism), and for a line bundle $\mathcal{L}\cong\mathcal{O}_{B'}(\sum_v n_v v)$ put $\deg_{B'/k}(\mathcal{L})=\sum_v n_v[k(v):k]$, with $k(v)$ the residue field of the closed point $v$. (Even if $k$ is not algebraically closed in $K'$, degrees are taken relative to $k$.) If $K''/K'$ is finite with curve $f:B''\to B'$, then $\deg_{B''/k}(f^*\mathcal{L})=[K'':K']\deg_{B'/k}(\mathcal{L})$.

**Theorem 85.4 (Grothendieck, SGA 7, Exp. IX).** Let $K$ be a number field or a function field of one variable, and $A/K$ an abelian variety of dimension $g$. (i) There is a finite separable extension $K'/K$ such that $A_{K'}$ has semistable reduction at every finite place of $K'$ (resp. every closed point of $B'$). (ii) If $A_{K'}$ has semistable reduction everywhere and $K''/K'$ is finite, the canonical morphism from the base change of the N\'eron model $\mathcal{A}'$ of $A_{K'}$ to the N\'eron model $\mathcal{A}''$ of $A_{K''}$ restricts to an isomorphism of identity components.

**Definition 85.5 (Hodge bundle; Faltings metric).** Let $B$ be $\mathrm{Spec}\,\mathcal{O}_{K'}$ or $B'$, let $\mathcal{A}\to B$ be the N\'eron model of $A_{K'}$ with identity section $e:B\to\mathcal{A}$. The *Hodge bundle* is the invertible $\mathcal{O}_B$-module
$$\omega_{\mathcal{A}/B}:=e^*\Omega^g_{\mathcal{A}/B}=\det\big(e^*\Omega^1_{\mathcal{A}/B}\big)=\det\big(\mathrm{Lie}(\mathcal{A}/B)^\vee\big).$$
In the number field case, for $\sigma:K'\hookrightarrow\mathbb{C}$ let $A_\sigma=A_{K'}\otimes_{K',\sigma}\mathbb{C}$; then $\omega_{\mathcal{A}/B}\otimes_\sigma\mathbb{C}\cong H^0(A_\sigma,\Omega^g)$, and the *Faltings metric* is
$$\|\alpha\|_{\mathrm{Fal},\sigma}^2:=\frac{i^{g^2}}{2^g}\int_{A_\sigma(\mathbb{C})}\alpha\wedge\bar\alpha=\Big(\frac{i}{2}\Big)^g(-1)^{g(g-1)/2}\int_{A_\sigma(\mathbb{C})}\alpha\wedge\bar\alpha>0\qquad(\alpha\neq0).$$

**Definition 85.6 (stable Faltings height).** Let $A$ be an abelian variety of dimension $g\ge1$ over $K$ and choose $K'$ as in Theorem 85.4(i). Define
$$h_{\mathrm{Fal}}(A):=\frac{1}{[K':\mathbb{Q}]}\,\widehat{\deg}\big(\omega_{\mathcal{A}/\mathcal{O}_{K'}},\|\cdot\|_{\mathrm{Fal}}\big)\quad(K\text{ a number field}),\qquad h_{\mathrm{Fal}}(A):=\frac{1}{[K':K]}\deg_{B'/k}\big(\omega_{\mathcal{A}/B'}\big)\quad(K\text{ a function field}).$$
By Proposition 85.2(ii), Definition 85.3 and Theorem 85.4(ii) (the Hodge bundle only depends on the identity component), $h_{\mathrm{Fal}}(A)$ is independent of $K'$, and $h_{\mathrm{Fal}}(A_L)=h_{\mathrm{Fal}}(A)$ for every finite extension $L/K$ (in the function field case, $L$ is regarded as a function field over the same $k$). For a smooth projective geometrically connected curve $C/K$ of genus $g\ge1$ put $h_{\mathrm{Fal}}(C):=h_{\mathrm{Fal}}(\mathrm{Jac}(C))$.

*Remarks.* (1) Normalisations differ in the literature: some authors drop the factor $2^{-g}$ or insert powers of $2\pi$. If $\|\cdot\|'^2=\lambda\|\cdot\|^2$ at every $\sigma$ for a constant $\lambda>0$, then $h'=h-\frac12\log\lambda$. The convention above is that of [2026, 203(1), no. 2, Section 4.3.1]. Since that paper's Theorem 1.1 uses $\max\{h_{\mathrm{Fal}}(C),1\}$ with constants depending only on $g$, such shifts are harmless there. (2) "Stable" refers to the base change to $K'$. Computing with the N\'eron model over $K$ itself gives the naive height $h(A/K)$, and Proposition 85.2(iii) applied to $\omega_{\mathcal{A}_{K'}}\hookrightarrow\omega_{\mathcal{A}_K}\otimes\mathcal{O}_{K'}$ shows $h_{\mathrm{Fal}}(A)\le h(A/K)$, with equality if $A$ is already semistable over $K$. (3) For a curve $C$ with stable model $\mathcal{C}'\to B'$ over $K'$, $\omega_{\mathcal{A}/B'}\cong\det\pi_*\omega_{\mathcal{C}'/B'}$ canonically, since $\mathrm{Pic}^0_{\mathcal{C}'/B'}$ is the identity component of the N\'eron model. In the number field case, the Faltings metric corresponds to the determinant of the metric $\|\beta\|^2=\frac{i}{2}\int_{C_\sigma(\mathbb{C})}\beta\wedge\bar\beta$ on $H^0(C_\sigma,\Omega^1)$ ([2026, 203(1), no. 2], Lemma 3.4). (4) In that paper's Theorem 1.1, $K$ is a number field or a function field of one variable over an arbitrary field $k$, $C$ is a geometrically integral smooth projective curve of genus $g>1$, and heights are normalised "absolutely" as above (division by $[K':\mathbb{Q}]$, resp. $[K':K]$ with $\|\cdot\|_v=e^{-[k(v):k]\mathrm{ord}_v}$).

## 86. Symmetric power of a Weil--Deligne representation

*Chapter context.* A chapter on operations on Langlands parameters in a book on the local Langlands correspondence for $\mathrm{GL}_n$. The reader knows Weil groups $W_K$ of local fields and Weil--Deligne representations $(r,N)$ with their isomorphisms, direct sums, tensor products, duals and Frobenius-semisimplification; algebraic representations of $\mathrm{GL}_d$ and symmetric powers of vector spaces; and the correspondences $\mathrm{rec}_K$. Composition of Weil--Deligne representations with algebraic representations, in particular symmetric powers, is defined here.

*Conventions recalled.* Let $K$ be a non-archimedean local field with residue field of order $q$ and $\Omega$ a field of characteristic $0$. A Weil--Deligne representation over $\Omega$ is a pair $(r,N)$ consisting of a finite-dimensional $\Omega$-vector space $V$, a homomorphism $r:W_K\to\mathrm{GL}(V)$ trivial on an open subgroup of the inertia group $I_K$, and a nilpotent $N\in\mathrm{End}_\Omega(V)$ such that $r(w)Nr(w)^{-1}=|w|\,N$ for all $w\in W_K$. Here $|\cdot|:W_K\to q^{\mathbb{Z}}$ is the norm pulled back along $\mathrm{Art}_K^{-1}$. With the normalisation in which $\mathrm{Art}_K$ sends uniformisers to geometric Frobenius elements, $|\Phi|=q^{-1}$ for a geometric Frobenius $\Phi$.

**Definition 86.1 (composition with an algebraic representation).** Let $(r,N)$ be a Weil--Deligne representation on $V$, $\dim V=d$, and let $\rho:\mathrm{GL}(V)\to\mathrm{GL}(W)$ be a morphism of algebraic groups over $\Omega$ with differential $d\rho:\mathfrak{gl}(V)\to\mathfrak{gl}(W)$. Define
$$\rho\circ(r,N):=(\rho\circ r,\ d\rho(N)),$$
a pair on $W$.

**Proposition 86.2.** (i) $\rho\circ(r,N)$ is a Weil--Deligne representation. Indeed, $\rho\circ r$ is trivial on the same open subgroup of $I_K$. The element $d\rho(N)$ is nilpotent, since algebraic representations preserve Jordan decompositions, and $\rho(g)\,d\rho(X)\,\rho(g)^{-1}=d\rho(gXg^{-1})$ gives $\rho(r(w))\,d\rho(N)\,\rho(r(w))^{-1}=|w|\,d\rho(N)$. (ii) An isomorphism $(r,N)\cong(r',N')$ induces $\rho\circ(r,N)\cong\rho\circ(r',N')$. (iii) If $(r,N)$ is Frobenius-semisimple, so is $\rho\circ(r,N)$. (iv) Equivalently, $\rho\circ(r,N)$ is the Weil--Deligne representation attached to the representation $w\exp(tN)\mapsto\rho(r(w))\exp(t\,d\rho(N))$ of the Weil--Deligne group, since $\rho(\exp(tN))=\exp(t\,d\rho(N))$.

**Definition 86.3 (symmetric powers).** Let $m\ge0$ and let $\mathrm{Sym}^mV$ be the $m$-th symmetric power of $V$ over $\Omega$. Let $\mathrm{Sym}^m:\mathrm{GL}(V)\to\mathrm{GL}(\mathrm{Sym}^mV)$ be the algebraic representation $g(v_1\cdots v_m)=gv_1\cdots gv_m$. Its differential is
$$d\,\mathrm{Sym}^m(X)(v_1\cdots v_m)=\sum_{j=1}^m v_1\cdots v_{j-1}(Xv_j)v_{j+1}\cdots v_m.$$
For a Weil--Deligne representation $(r,N)$ on $V$, the *$m$-th symmetric power* is
$$\mathrm{Sym}^m\circ(r,N):=\big(\mathrm{Sym}^m\circ r,\ d\,\mathrm{Sym}^m(N)\big),$$
of dimension $\binom{d+m-1}{m}$. For $d=2$ and $n\ge1$, $\mathrm{Sym}^{n-1}\circ(r,N)$ is $n$-dimensional. Explicitly, if $e_1,e_2$ is a basis of $V$ and $\mathrm{Sym}^{n-1}V$ is given the basis $f_j=e_1^{\,n-1-j}e_2^{\,j}$ ($0\le j\le n-1$), then $N=\left(\begin{smallmatrix}a&b\\ c&-a\end{smallmatrix}\right)$, i.e. $Ne_1=ae_1+ce_2$, $Ne_2=be_1-ae_2$, gives
$$d\,\mathrm{Sym}^{n-1}(N)f_j=(n-1-2j)a\,f_j+(n-1-j)c\,f_{j+1}+j\,b\,f_{j-1}.$$
Here $f_{-1}=f_n=0$. (Nilpotent $N$ is trace-free; $\mathrm{Sym}^{n-1}(g)$ for $g\in\mathrm{GL}_2(\Omega)$ is the matrix of $f_j\mapsto(ge_1)^{n-1-j}(ge_2)^{j}$.) In particular $N=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)$ gives a single nilpotent Jordan block of size $n$.

**Definition 86.4 (archimedean case).** For $K=\mathbb{R}$ or $\mathbb{C}$, a "Weil--Deligne representation" means a continuous semisimple representation $r:W_K\to\mathrm{GL}(V)$ on a finite-dimensional complex vector space (with $N=0$). Then $\mathrm{Sym}^m\circ r$ is again such a representation.

*Remarks.* (1) Examples: $\mathrm{Sym}^{n-1}$ of the special representation $\mathrm{Sp}_2=(|\cdot|^{1/2}\oplus|\cdot|^{-1/2},N)$ is $\mathrm{Sp}_n$. Up to normalisation of the twist, this is the Steinberg parameter of $\mathrm{GL}_n$. If $(r,N)=(r,0)$ then $\mathrm{Sym}^m\circ(r,0)=(\mathrm{Sym}^m\circ r,0)$. Also $\mathrm{Sym}^m((r,N)\otimes\chi)=\mathrm{Sym}^m(r,N)\otimes\chi^m$ for a character $\chi$. (2) In characteristic $0$, $\mathrm{Sym}^mV$ may be taken either as the quotient of $V^{\otimes m}$ by the symmetric group action or as the symmetric tensors; the two are isomorphic as $\mathrm{GL}(V)$-representations. (3) In [2026, 203(1), no. 4], Theorem A, $\Omega=\mathbb{C}$, $\pi$ is a cuspidal automorphic representation of $\mathrm{GL}_2(\mathbf{A}_F)$ ($F$ totally real, no CM, $\pi_\infty$ essentially square-integrable), and one asks for $\Pi_n$ on $\mathrm{GL}_n(\mathbf{A}_F)$ with $\mathrm{rec}_{F_v}(\Pi_{n,v})\cong\mathrm{Sym}^{n-1}\circ\mathrm{rec}_{F_v}(\pi_v)$ at every place $v$. This uses the unitary normalisation $\mathrm{rec}$ at finite $v$ (Frobenius-semisimple parameters; Artin map sending uniformisers to geometric Frobenius), and Definition 86.4 at archimedean $v$. By the twisting formula in (1), the condition is unchanged if both sides use the Tate normalisation $\mathrm{rec}^T_K(\pi)=\mathrm{rec}_K(\pi\otimes|\det|^{(1-n)/2})$, since $(1-2)(n-1)/2=(1-n)/2$.

## 87. Tate--Shafarevich group of an abelian variety over a number field

*Chapter context.* A chapter on descent in a book on the arithmetic of abelian varieties. The reader knows abelian varieties and isogenies over a field, cohomology of profinite groups with coefficients in discrete modules, principal homogeneous spaces, completions $K_v$ and decomposition groups, and the weak Mordell--Weil theorem; Selmer groups and the Tate--Shafarevich group are defined here.

Let $K$ be a number field with algebraic closure $\bar K$ and $G_K=\mathrm{Gal}(\bar K/K)$, and let $A/K$ be an abelian variety. For each place $v$ of $K$ (finite, real or complex) fix an algebraic closure $\bar K_v$ of $K_v$ and a $K$-embedding $\iota_v:\bar K\hookrightarrow\bar K_v$; restriction along $\iota_v$ identifies $G_v:=\mathrm{Gal}(\bar K_v/K_v)$ with a decomposition subgroup of $G_K$, and $A(\iota_v):A(\bar K)\to A(\bar K_v)$ is $G_v$-equivariant.

**Definition 87.1 (Weil--Ch\^atelet groups and restriction).** Put $H^1(K,A):=H^1(G_K,A(\bar K))$, continuous cohomology with $A(\bar K)$ a discrete $G_K$-module, and $H^1(K_v,A):=H^1(G_v,A(\bar K_v))$. The *restriction map* $\mathrm{res}_v:H^1(K,A)\to H^1(K_v,A)$ is the composite of restriction along $G_v\hookrightarrow G_K$ with the map induced by $A(\iota_v)$. It does not depend on $\iota_v$. $H^1(K,A)$ is in bijection with the set of isomorphism classes of principal homogeneous spaces (torsors) for $A$ over $K$, with $0$ corresponding to the trivial torsor $A$, and $\mathrm{res}_v$ corresponds to $X\mapsto X_{K_v}$.

**Definition 87.2 (Tate--Shafarevich group).** The *Tate--Shafarevich group* of $A/K$ is the subgroup
$$\mathrm{Sha}(A/K):=\ker\Big(H^1(K,A)\xrightarrow{\ (\mathrm{res}_v)_v\ }\prod_{v}H^1(K_v,A)\Big),$$
the product running over all places of $K$, archimedean ones included. Equivalently, it is the group of isomorphism classes of $A$-torsors $X$ over $K$ with $X(K_v)\neq\emptyset$ for every place $v$. It is an abelian group, usually denoted by the Cyrillic letter Sha.

**Definition 87.3 (Selmer groups).** For an isogeny $\phi:A\to B$ over $K$, consider the Kummer sequences $0\to A[\phi](\bar K)\to A(\bar K)\xrightarrow{\phi}B(\bar K)\to0$ over $K$ and over each $K_v$, with connecting maps $\delta$. The *$\phi$-Selmer group* is
$$\mathrm{Sel}^{\phi}(A/K):=\ker\Big(H^1(G_K,A[\phi](\bar K))\to\prod_vH^1(K_v,A)\Big)=\{c:\ \mathrm{res}_v(c)\in\delta(B(K_v))\ \forall v\}.$$

**Proposition 87.4.** Let $\phi:A\to B$ be an isogeny over $K$.

(i) There is an exact sequence $0\to B(K)/\phi A(K)\to\mathrm{Sel}^\phi(A/K)\to\ker\big(\phi_*:\mathrm{Sha}(A/K)\to\mathrm{Sha}(B/K)\big)\to0$.

(ii) $\mathrm{Sel}^\phi(A/K)$ is finite. This is the weak Mordell--Weil theorem.

(iii) $\mathrm{Sha}(A/K)$ is a torsion group and $\mathrm{Sha}(A/K)[n]$ is finite for every $n\ge1$.

(iv) $\mathrm{Sha}(A/K)$ is finite if and only if $\mathrm{Sha}(B/K)$ is finite. Indeed, $\ker\phi_*$ is finite by (i) and (ii), and there is an isogeny $\psi:B\to A$ with $\psi\circ\phi=[\deg\phi]$, to which the same argument applies.

*Remarks.* (1) It is conjectured (Tate--Shafarevich) that $\mathrm{Sha}(A/K)$ is always finite. By (iv), finiteness is an invariant of the $K$-isogeny class. This is exactly what is needed in [2020, 191(2), no. 1], Theorems A and B, where $A_f$ is only defined up to isogeny and $\mathrm{Sha}(A_f)=\mathrm{Sha}(A_f/\mathbb{Q})$. There, $\mathrm{Sha}(A_f/K)$ means $\mathrm{Sha}((A_f)_K/K)$ for an imaginary quadratic $K$. (2) The local terms use $A(\bar K_v)$, not $A(\bar K)$. The Tate--Shafarevich group of the discrete $G_K$-module $M=A(\bar K)$, in the sense of Galois modules, has local terms $H^1(G_v,M)$ and is a priori a different construction. Identifying the two requires comparing $A(\bar K)$ and $A(\bar K_v)$ as $G_v$-modules. For a finite module, e.g. $A[n]$, the Galois-module group differs from $\mathrm{Sha}(A/K)[n]$; the latter is a quotient of $\mathrm{Sel}^{[n]}(A/K)$ by (i). (3) Archimedean places: $H^1(\mathbb{C},A)=0$, and $H^1(\mathbb{R},A)$ is a finite elementary abelian $2$-group, so real places only affect the $2$-primary part. (4) For elliptic curves this specialises to the classical $\mathrm{Sha}(E/K)$. For abelian varieties, the Cassels--Tate pairing $\mathrm{Sha}(A/K)\times\mathrm{Sha}(A^\vee/K)\to\mathbb{Q}/\mathbb{Z}$ is non-degenerate modulo maximal divisible subgroups.

## 88. Weak functorial transfer to $\mathrm{GL}_N$

*Chapter context.* A chapter on Langlands functoriality in a book on automorphic representations. The reader knows L-groups, the Satake isomorphism and Satake parameters of unramified representations, automorphic representations and their local components (Definition #67), and infinitesimal characters with the Harish-Chandra isomorphism (Definition #5). The local transfers and the weak global transfer are defined here.

*Setting.* $F$ is a number field and $G$ a connected reductive group over $F$ with complex dual group $\widehat G$. $E/F$ is a finite Galois extension such that $\mathrm{Gal}(\bar F/F)$ acts on $\widehat G$ (by pinned automorphisms) through $\mathrm{Gal}(E/F)$, and ${}^LG=\widehat G\rtimes\mathrm{Gal}(E/F)$. An *L-representation* is a homomorphism $r:{}^LG\to\mathrm{GL}_N(\mathbb{C})$ whose restriction $r|_{\widehat G}$ is algebraic; write $dr:\widehat{\mathfrak g}\to\mathfrak{gl}_N(\mathbb{C})$ for the differential of $r|_{\widehat G}$. If $G$ is split we take $E=F$, so that ${}^LG=\widehat G$ and $r$ is just an algebraic representation of $\widehat G$. The hyperspecial subgroups $K_v$, $v\notin S_0$, are as in Definition #67. The Satake isomorphism is normalised in the same way for $G$ and for $\mathrm{GL}_N$.

**Definition 88.1 (unramified transfer).** Let $v$ be a finite place with $v\notin S_0$, $G_{F_v}$ unramified and $v$ unramified in $E$, and let $\pi_v$ be an irreducible $K_v$-spherical representation of $G(F_v)$. Its Satake parameter is a $\widehat G$-conjugacy class of semisimple elements $t_v\rtimes\mathrm{Frob}_v\in{}^LG$. The element $r(t_v\rtimes\mathrm{Frob}_v)\in\mathrm{GL}_N(\mathbb{C})$ is semisimple and its conjugacy class does not depend on the choices. The *unramified transfer* $r_*(\pi_v)$ is the unique (up to isomorphism) irreducible unramified representation of $\mathrm{GL}_N(F_v)$ whose Satake parameter is the conjugacy class of $r(t_v\rtimes\mathrm{Frob}_v)$.

Explicitly, for split $G$: let $T\subset B$ be a split maximal torus and Borel subgroup compatible with $K_v$. Write $\pi_v$ as the unramified subquotient of the normalised induction $\mathrm{Ind}_B^G(\chi)$, with $\chi:T(F_v)\to\mathbb{C}^\times$ unramified; $\chi$ is unique up to the Weyl group. Let $t_\chi\in\widehat T$ be defined by $\lambda(t_\chi)=\chi(\lambda(\varpi_v))$ for all $\lambda\in X_*(T)=X^*(\widehat T)$, where $\varpi_v$ is a uniformiser. If $\alpha_1,\dots,\alpha_N$ are the eigenvalues of $r(t_\chi)$, then $r_*(\pi_v)$ is the unramified subquotient of $\mathrm{Ind}_{B_N}^{\mathrm{GL}_N}(\chi_1\otimes\cdots\otimes\chi_N)$, where $\chi_i$ is unramified with $\chi_i(\varpi_v)=\alpha_i$.

**Definition 88.2 (archimedean matching of infinitesimal characters).** Let $v\mid\infty$. Then $\mathfrak g_v=\mathrm{Lie}\,G(F_v)\otimes_{\mathbb{R}}\mathbb{C}=\bigoplus_{\tau}\mathrm{Lie}(G\otimes_{F,\tau}\mathbb{C})$, where $\tau$ runs over the one (real $v$) or two (complex $v$) embeddings $F\hookrightarrow\mathbb{C}$ inducing $v$; the same holds for $\mathrm{GL}_N$. The dual $\mathfrak h^*$ of the abstract Cartan subalgebra of $\mathrm{Lie}(G_{\mathbb{C}})$ is $X^*(T_{\mathrm{abs}})\otimes\mathbb{C}=X_*(\widehat T)\otimes\mathbb{C}=\widehat{\mathfrak t}$, the Lie algebra of a maximal torus of $\widehat G$, compatibly with Weyl groups. Hence, via the ($\rho$-shifted) Harish-Chandra isomorphism of Definition #5, the infinitesimal character of an irreducible admissible representation $\pi_v$ of $G(F_v)$ is a family $(\lambda_\tau)_\tau$ with $\lambda_\tau\in\widehat{\mathfrak t}/W$. Define
$$r_*\big((\lambda_\tau)_\tau\big):=\big(dr(\lambda_\tau)\big)_\tau,\qquad dr(\lambda_\tau)\in\mathfrak{gl}_N(\mathbb{C})_{\mathrm{ss}}/\mathrm{GL}_N(\mathbb{C})=\mathbb{C}^N/S_N,$$
i.e. the unordered $N$-tuple of eigenvalues of $dr(\lambda_\tau)$. Equivalently, these are the values $\langle\mu,\lambda_\tau\rangle$ for $\mu$ running over the weights of $r|_{\widehat G}$ with multiplicity. This is independent of the representative of $\lambda_\tau$.

**Definition 88.3 (weak functorial transfer).** Let $\pi$ be an irreducible automorphic representation of $G(\mathbb{A}_F)$ and $\Pi$ an irreducible automorphic representation of $\mathrm{GL}_N(\mathbb{A}_F)$, with local components $\pi_v,\Pi_v$ (Definition #67). $\Pi$ is a *weak functorial transfer of $\pi$ along $r$* if both of the following hold.

(a) For all but finitely many finite places $v$ at which $\pi_v$ is unramified (so that Definition 88.1 applies), $\Pi_v\cong r_*(\pi_v)$.

(b) For every archimedean place $v$, the infinitesimal character of $\Pi_v$ equals $r_*$ of the infinitesimal character of $\pi_v$.

$\pi$ *has a weak functorial transfer to $\mathrm{GL}_N(\mathbb{A}_F)$* if such a $\Pi$ exists.

*Remarks.* (1) Since $\pi_v$ is unramified for almost all $v$, (a) says: there is a finite set $S$ of places such that $\Pi_v\cong r_*(\pi_v)$ for all $v\notin S$. Changing the normalisation of the Satake isomorphism (uniformiser versus its inverse, arithmetic versus geometric Frobenius) on both groups simultaneously does not change the notion. (2) $\Pi$ is not unique. By Jacquet--Shalika it is unique if one also requires $\Pi$ to be an isobaric sum of cuspidal representations; the transfer need not satisfy local--global compatibility at the ramified places. (3) If the archimedean L-parameter $\phi_v$ of $\pi_v$ is known and $\Pi_v$ has parameter $r\circ\phi_v$, then (b) holds: the infinitesimal character is encoded in $\phi_v|_{\mathbb{C}^\times}$. (b) is strictly weaker. (4) In [2024, 200(3), no. 2] (Definition 2.2, Theorem 0.1), $G$ is split: $\mathrm{Sp}_{2n}$, $\mathrm{SO}_{2n+1}$, $\mathrm{SO}_{2n}$, or $\mathrm{GSpin}_{2n+1}$, $\mathrm{GSpin}_{2n}$ (rank $n+1$). The dual groups are $\mathrm{SO}_{2n+1}(\mathbb{C})$, $\mathrm{Sp}_{2n}(\mathbb{C})$, $\mathrm{SO}_{2n}(\mathbb{C})$, $\mathrm{GSp}_{2n}(\mathbb{C})$, $\mathrm{GSO}_{2n}(\mathbb{C})$, and $r=r_G$ is the standard embedding into $\mathrm{GL}_N(\mathbb{C})$, with $N=2n+1$ for $\mathrm{Sp}_{2n}$ and $N=2n$ otherwise. Every irreducible cuspidal $\pi$ there has such a $\Pi$, and the $\Pi$ constructed has $\Pi_\infty$ equal to the archimedean Langlands transfer of $\pi_\infty$. Sanity check: for $G=\mathrm{Sp}_{2n}$ the trivial representation has infinitesimal character $\rho=(n,\dots,1)$, and $dr(\rho)$ has eigenvalues $n,\dots,1,0,-1,\dots,-n$, which is $\rho$ for $\mathrm{GL}_{2n+1}$.

## 89. $\ell$-adic Galois representation with values in the Mumford--Tate group

*Chapter context.* A chapter on absolute Hodge cycles and Galois representations of abelian varieties, in a book on Hodge theory and arithmetic geometry. The reader knows abelian varieties over number fields, Betti and $\ell$-adic \'etale cohomology with the Artin comparison isomorphism, rational Hodge structures and the Mumford--Tate group (Definition #13), reductive groups and their invariant theory, and geometric Frobenius elements. The Mumford--Tate-valued Galois representations and their Frobenius classes are defined here.

*Setting.* $E\subset\mathbb{C}$ is a number field, $\bar E$ its algebraic closure in $\mathbb{C}$, $\Gamma_E=\mathrm{Gal}(\bar E/E)$, and $A/E$ an abelian variety of dimension $g$. Put $V_B:=H^1_B(A(\mathbb{C}),\mathbb{Q})$ with its Hodge structure of weight $1$, and let $\mathbf{G}=\mathrm{MT}(V_B)\subseteq\mathrm{GL}(V_B)$ be its Mumford--Tate group (Definition #13), a connected reductive group over $\mathbb{Q}$ containing the homotheties. For a prime $\ell$, $\rho_\ell:\Gamma_E\to\mathrm{GL}(H^1_{\mathrm{\acute et}}(A_{\bar E},\mathbb{Q}_\ell))$ is the continuous Galois action. The comparison isomorphisms $H^1_{\mathrm{\acute et}}(A_{\bar E},\mathbb{Q}_\ell)\cong H^1_{\mathrm{\acute et}}(A_{\mathbb{C}},\mathbb{Q}_\ell)\cong V_B\otimes_{\mathbb{Q}}\mathbb{Q}_\ell$ identify $\mathrm{GL}(H^1_{\mathrm{\acute et}})$ with $\mathrm{GL}(V_B)(\mathbb{Q}_\ell)$, and hence $\mathbf{G}(\mathbb{Q}_\ell)$ with a closed subgroup of it.

**Theorem 89.1 (Deligne).** There is a finite extension $E'/E$ inside $\bar E$ such that $\rho_\ell(\Gamma_{E'})\subseteq\mathbf{G}(\mathbb{Q}_\ell)$. Moreover, for a closed subgroup $H\subseteq\Gamma_E$, the condition $\rho_\ell(H)\subseteq\mathbf{G}(\mathbb{Q}_\ell)$ holds for one prime $\ell$ iff it holds for all primes $\ell$. (Deligne, *Hodge cycles on abelian varieties*, LNM 900: every Hodge cycle on $A$ is absolutely Hodge. $\mathbf{G}$ is the stabiliser of finitely many Hodge tensors $s_\alpha\in V_B^{\otimes r}\otimes(V_B^\vee)^{\otimes r}$. $\Gamma_E$ permutes the tuples $(s_{\alpha,\ell})_\ell$ of their \'etale realisations through a finite quotient, and an absolute Hodge cycle is determined by any one of its $\ell$-adic components.)

Consequently $\Gamma_E^{\mathbf G}:=\rho_\ell^{-1}(\mathbf{G}(\mathbb{Q}_\ell))$ is an open subgroup of $\Gamma_E$, independent of $\ell$. Its fixed field $E^{\mathbf G}$ is the smallest extension of $E$ in $\bar E$ over which the Galois action lands in $\mathbf{G}$.

**Definition 89.2 ($\mathbf{G}$-valued $\ell$-adic representation).** Suppose $\rho_\ell(\Gamma_E)\subseteq\mathbf{G}(\mathbb{Q}_\ell)$, i.e. $E^{\mathbf G}=E$, which can always be achieved by replacing $E$ by $E^{\mathbf G}$. The *$\ell$-adic representation with values in the Mumford--Tate group* is the unique continuous homomorphism
$$\rho^{\mathbf G}_\ell:\Gamma_E\to\mathbf{G}(\mathbb{Q}_\ell)\qquad\text{with}\qquad\iota_\ell\circ\rho^{\mathbf G}_\ell=\rho_\ell,$$
where $\iota_\ell:\mathbf{G}(\mathbb{Q}_\ell)\hookrightarrow\mathrm{GL}(V_B)(\mathbb{Q}_\ell)\cong\mathrm{GL}(H^1_{\mathrm{\acute et}}(A_{\bar E},\mathbb{Q}_\ell))$ is the inclusion. Uniqueness holds because $\iota_\ell$ is injective. Continuity holds because $\mathbf{G}(\mathbb{Q}_\ell)$ carries the subspace topology.

**Definition 89.3 (variety of semisimple conjugacy classes).** For a reductive group $H$ over a field $k$ of characteristic $0$, let $\mathrm{Conj}_H:=\mathrm{Spec}\,\mathcal{O}(H)^{H}$ be the quotient of $H$ by its conjugation action (invariant regular functions). Let $\chi_H:H\to\mathrm{Conj}_H$ be the quotient morphism. For $\bar k$ algebraically closed, $\mathrm{Conj}_H(\bar k)$ is the set of semisimple $H(\bar k)$-conjugacy classes, and $\chi_H(h)$ is the class of the semisimple part of $h$. For $k'/k$, the map $\chi_H:H(k')\to\mathrm{Conj}_H(k')$ is constant on $H(\bar k')$-conjugacy classes. (For $H=\mathrm{GL}_n$, $\chi_H$ is the characteristic polynomial.)

**Definition 89.4 (Frobenius classes).** In the situation of Definition 89.2, let $v$ be a finite place of $E$ above $p$ at which $A$ has good reduction, and $\ell\ne p$. Then $\rho_\ell$, hence $\rho^{\mathbf G}_\ell$, is unramified at $v$ (N\'eron--Ogg--Shafarevich). For a geometric Frobenius $\mathrm{Frob}_v\in\Gamma_E$ at $v$ (for some decomposition group at $v$), put
$$\gamma_\ell(v):=\chi_{\mathbf G}\big(\rho^{\mathbf G}_\ell(\mathrm{Frob}_v)\big)\in\mathrm{Conj}_{\mathbf G}(\mathbb{Q}_\ell).$$
It is independent of the choice of decomposition group and Frobenius lift, since these change $\rho^{\mathbf G}_\ell(\mathrm{Frob}_v)$ by $\mathbf{G}(\mathbb{Q}_\ell)$-conjugation and by elements of $\rho^{\mathbf G}_\ell(I_v)=1$.

*Remarks.* (1) $\mathbf{G}$ depends on the embedding $E\subset\mathbb{C}$. Another embedding replaces $\mathbf{G}$ by an inner form, canonically over $\bar{\mathbb{Q}}$, and $\mathrm{Conj}_{\mathbf G}$ and $\gamma_\ell(v)$ are unchanged. (2) $\mathbf{G}(\mathbb{Q}_\ell)$-conjugacy classes are finer than $\mathrm{Conj}_{\mathbf G}(\mathbb{Q}_\ell)$, and $\mathrm{Conj}_{\mathbf G}(\mathbb{Q})\to\mathrm{Conj}_{\mathrm{GL}(V_B)}(\mathbb{Q})$ need not be injective. So $\gamma_\ell(v)$ carries more information than the characteristic polynomial $P_v(t)$ of $\mathrm{Frob}_v$, which lies in $\mathbb{Z}[t]$ and is independent of $\ell$. (3) [2025, 202(3), no. 3] uses $H^1_{\mathrm{\acute et}}(A_{\bar E},\mathbb{Q}_\ell)$ in the introduction but $T_\ell A^\vee\otimes\mathbb{Q}_\ell=H^1_{\mathrm{\acute et}}(A_{\bar E},\mathbb{Q}_\ell)(1)$ in Section 6 (comparison via $2\pi i$). The two representations differ by the cyclotomic character times the homotheties, which lie in $\mathbf{G}$. Both factor through $\mathbf{G}(\mathbb{Q}_\ell)$ over the same field, and their Frobenius classes differ by a fixed central factor, so the $\ell$-independence statement is unaffected; a formaliser should fix one. (4) In that paper's Theorem 1.1, $E$ is replaced by $E^{\mathbf G}$, $p>2$, and the claim is that there is $\gamma\in\mathrm{Conj}_{\mathbf G}(\mathbb{Q})$ with image $\gamma_\ell(v)$ in $\mathrm{Conj}_{\mathbf G}(\mathbb{Q}_\ell)$ for all $\ell\ne p$. (5) The existence of $\rho^{\mathbf G}_\ell$ after finite extension would follow from the Hodge conjecture; Deligne's theorem makes it unconditional for abelian varieties.

## 90. The $\pi$-nearly isotypic cuspidal subspace

*Chapter context.* A chapter on the cuspidal spectrum in a book on automorphic forms and the trace formula. The reader knows $L^2(G(F)\backslash G(\mathbb{A}_F),\omega)$ and its cuspidal subspace with the right regular representation $\mathrm{R}$, the discreteness of the cuspidal spectrum, automorphic representations and their local components (Definition #67), and the Schwartz--Hecke algebra (Definition #83). Near equivalence and the nearly isotypic subspaces are defined here.

*Setting.* $F$ is a number field and $G$ a connected reductive group over $F$. $Z$ is the maximal $F$-split torus in the centre of $G$, and $\omega:Z(F)\backslash Z(\mathbb{A}_F)\to\mathbb{C}^\times$ is a unitary character. $K\subseteq G(\mathbb{A}_F^\infty)$ is an open compact subgroup. Write $L^2_{\mathrm{cusp}}:=L^2_{\mathrm{cusp}}(G(F)\backslash G(\mathbb{A}_F),\omega)$ and $L^2_{\mathrm{cusp}}(G(F)\backslash G(\mathbb{A}_F)/K,\omega):=(L^2_{\mathrm{cusp}})^{\mathrm{R}(K)}$.

**Theorem 90.1 (recalled; Gelfand--Graev--Piatetski-Shapiro, Langlands).** $L^2_{\mathrm{cusp}}$ is the Hilbert direct sum of closed irreducible $G(\mathbb{A}_F)$-invariant subspaces, each occurring with finite multiplicity. For such a subspace $H$, the subspace $H^{\mathrm{fin}}$ of smooth, $K_\infty$-finite vectors that are fixed by some open compact subgroup of $G(\mathbb{A}_F^\infty)$ is an irreducible admissible $(\mathfrak g_\infty,K_\infty)\times G(\mathbb{A}_F^\infty)$-module, namely a cuspidal automorphic representation. By Definition #67 it has local components $H_v$, $v$ a place of $F$, and these are unramified for almost all finite $v$. (The space $H^K$ of $\mathrm{R}(K)$-fixed vectors is in general infinite-dimensional, because of the archimedean component.)

We call such an $H$ an *irreducible subrepresentation* of $L^2_{\mathrm{cusp}}$ and write $\tilde\pi$ for it, with local components $\tilde\pi_v:=H_v$.

**Definition 90.2 (near equivalence).** Let $\pi=\otimes'_v\pi_v$ be an irreducible admissible representation of $G(\mathbb{A}_F)$. It need not be automorphic, and only its local components at finite places will matter. An irreducible subrepresentation $\tilde\pi$ of $L^2_{\mathrm{cusp}}$ is *nearly equivalent* to $\pi$ if there is a finite set $S$ of places of $F$, containing the archimedean ones, such that $\tilde\pi_v\cong\pi_v$ as smooth representations of $G(F_v)$ for every $v\notin S$. Equivalently, $\tilde\pi_v\cong\pi_v$ for all but finitely many places $v$.

**Definition 90.3 ($\pi$-nearly isotypic subspace).** With $\pi$ as in Definition 90.2, the *$\pi$-nearly isotypic subspace* of $L^2_{\mathrm{cusp}}$ is the closed subspace
$$L^2_{\mathrm{cusp}}(G(F)\backslash G(\mathbb{A}_F),\omega)_\pi:=\overline{\sum\big\{\tilde\pi\subseteq L^2_{\mathrm{cusp}}:\ \tilde\pi\text{ an irreducible subrepresentation nearly equivalent to }\pi\big\}},$$
and its level-$K$ part is
$$L^2_{\mathrm{cusp}}(G(F)\backslash G(\mathbb{A}_F)/K,\omega)_\pi:=\big(L^2_{\mathrm{cusp}}(G(F)\backslash G(\mathbb{A}_F),\omega)_\pi\big)^{\mathrm{R}(K)}=\widehat{\bigoplus_{\tilde\pi}}\ \tilde\pi^{K}.$$
In the last expression $\tilde\pi$ runs over the irreducible summands nearly equivalent to $\pi$ in any decomposition as in Theorem 90.1, and $\widehat\bigoplus$ is the Hilbert direct sum. Both are closed $G(\mathbb{A}_F)$-invariant, resp. $\mathcal{S}(G(\mathbb{A}_F))_K$-invariant, subspaces.

**Proposition 90.4.** (i) The subspace in Definition 90.3 depends only on the near-equivalence class of $\pi$. It is the orthogonal sum of the full isotypic components $L^2_{\mathrm{cusp}}[\tilde\pi]$, over the isomorphism classes $\tilde\pi$ nearly equivalent to $\pi$. Different near-equivalence classes give mutually orthogonal subspaces, whose Hilbert sum is $L^2_{\mathrm{cusp}}$. (ii) With $K_v$ ($v\notin S_0$) the hyperspecial subgroups of Definition #67, $\tilde\pi$ is nearly equivalent to $\pi$ iff there is a finite set $S\supseteq S_0$ such that for all $v\notin S$ both $\tilde\pi_v$ and $\pi_v$ are $K_v$-spherical and the spherical Hecke algebra $C_c(K_v\backslash G(F_v)/K_v)$ acts on the lines $\tilde\pi_v^{K_v}$ and $\pi_v^{K_v}$ by the same character. This holds because an irreducible unramified representation is determined by its Hecke eigencharacter (Satake).

*Remarks.* (1) The sum is over subspaces, not over isomorphism classes, so multiplicities are kept. Near equivalence ignores the archimedean components and finitely many finite ones; it uses only the isomorphism classes of local components. (2) For $G=\mathrm{GL}_n$ and $\pi$ cuspidal automorphic, strong multiplicity one gives $L^2_{\mathrm{cusp}}(\ldots/K,\omega)_\pi=\pi^K$, embedded once. For unitary groups a near-equivalence class can contain several non-isomorphic $\tilde\pi$, e.g. members of one (global) packet. (3) The subspace may be zero, e.g. if no cuspidal $\tilde\pi$ is nearly equivalent to $\pi$, even when $\pi^K\neq0$. (4) In [2021, 194(2), no. 5], Theorem 1.1, $\pi$ is an irreducible admissible representation of $G(\mathbb{A}_F)$ with unitary automorphic central character $\omega$. It is assumed that there is no pair $(P,\sigma)$, with $P\subsetneq G$ a parabolic subgroup over $F$ and $\sigma$ a cuspidal automorphic representation of its Levi quotient, such that $\pi_v$ is a constituent of $\mathrm{Ind}_P^G(\sigma_v)$ for almost all $v$. A multiplier $\mu\star$ of $\mathcal{S}(G(\mathbb{A}_F))_K$ is constructed with $\mathrm{R}(\mu\star f)(L^2(G(F)\backslash G(\mathbb{A}_F)/K,\omega))\subseteq L^2_{\mathrm{cusp}}(G(F)\backslash G(\mathbb{A}_F)/K,\omega)_\pi$. The proof actually lands in the smaller subspace on which $\mathcal{Z}(\mathfrak g_\infty)$ and the spherical Hecke algebras away from a finite set $S$ act by the characters attached to $\pi$ (their Theorem 3.6 with $\mathrm{T}=S$), i.e. it also matches infinitesimal characters.

# Probability, combinatorics, dynamics & logic

## 91. Anosov flow

*Chapter context.* A chapter on uniformly hyperbolic flows in a graduate text on smooth dynamical systems. The reader knows compact smooth manifolds, the tangent bundle and continuous vector subbundles, Riemannian metrics, $C^r$ maps and $C^r$ flows with their generating vector fields; Anosov flows are defined here.

Throughout, $M$ is a compact connected smooth manifold without boundary, of dimension $m \ge 2$, and $r \in \{1, 2, \dots\} \cup \{\infty\}$.

**Definition 91.1 (flow and generator).** A *$C^r$ flow* on $M$ is a $C^r$ map $g\colon \mathbb{R}\times M\to M$, $(t,x)\mapsto g^t(x)$, such that $g^0=\mathrm{id}_M$ and $g^{s+t}=g^s\circ g^t$ for all $s,t\in\mathbb{R}$. Each $g^t$ is then a $C^r$ diffeomorphism with inverse $g^{-t}$. The *generator* of $g$ is the continuous vector field
$$X(x)=\frac{\partial}{\partial t}\Big|_{t=0} g^t(x)\in T_xM ,$$
and it satisfies $Dg^t(x)\,X(x)=X(g^t x)$ for all $t$ and $x$.

**Definition 91.2 (Anosov flow).** Fix a Riemannian metric on $M$, with norm $\|\cdot\|$ on each $T_xM$. A $C^r$ flow $g=\{g^t\}_{t\in\mathbb{R}}$ on $M$ with generator $X$ is an *Anosov flow* if:

1. $X(x)\neq 0$ for every $x\in M$;
2. there are continuous vector subbundles $E^s, E^u\subseteq TM$ such that for every $x\in M$
$$T_xM = E^s(x)\oplus \mathbb{R}X(x)\oplus E^u(x)\qquad(\text{direct sum of vector spaces});$$
3. the splitting is invariant: $Dg^t(x)\,E^s(x)=E^s(g^tx)$ and $Dg^t(x)\,E^u(x)=E^u(g^tx)$ for all $t\in\mathbb{R}$, $x\in M$;
4. there are constants $C>0$ and $\kappa>0$ such that for all $t> 0$, all $x\in M$,
$$\|Dg^t(x)v\|\le Ce^{-\kappa t}\|v\| \quad (v\in E^s(x)),\qquad \|Dg^{-t}(x)w\|\le Ce^{-\kappa t}\|w\| \quad (w\in E^u(x)).$$

Equivalently, in operator-norm form: $\sup_{x\in M}\|Dg^t(x)|_{E^s(x)}\|\le Ce^{-\kappa t}$ and $\sup_{x\in M}\|Dg^{-t}(x)|_{E^u(x)}\|\le Ce^{-\kappa t}$ for all $t>0$. The bundles $E^s$, $E^u$ are the *stable* and *unstable bundles*, $E^c=\mathbb{R}X$ the *flow (centre) direction*, and $E^{cs}=E^s\oplus E^c$, $E^{cu}=E^c\oplus E^u$ the *centre-stable* and *centre-unstable* bundles. The property "Anosov" is a property of the flow $g$ alone: the bundles are not part of the data (see Proposition 91.3).

**Proposition 91.3.** Let $g$ be an Anosov flow.

(a) (Independence of the metric.) Condition 4 holds for one Riemannian metric on $M$ if and only if it holds for every Riemannian metric (with a different $C$, the same $\kappa$), since any two Riemannian metrics on a compact manifold are uniformly equivalent.

(b) (Uniqueness.) $E^s(x)=\{v\in T_xM : \|Dg^t(x)v\|\to 0 \text{ as } t\to+\infty\}$ and $E^u(x)=\{v\in T_xM : \|Dg^{-t}(x)v\|\to 0 \text{ as } t\to+\infty\}$; in particular the splitting in Definition 91.2 is unique.

(c) (Continuity is automatic.) If conditions 1, 2 (without continuity), 3 and 4 hold for some family of subspaces, then these subspaces automatically form continuous subbundles of locally constant rank.

(d) (Adapted metric.) There is a (continuous) Riemannian metric on $M$, an *adapted* or *Lyapunov* metric, for which condition 4 holds with $C=1$, possibly after decreasing $\kappa$.

(These are standard; see e.g. Katok and Hasselblatt, *Introduction to the Modern Theory of Dynamical Systems*, ch. 6 and 17, or Fisher and Hasselblatt, *Hyperbolic Flows*.)

*Remarks.*

- Strict versus non-strict inequalities in condition 4 (the Annals paper writes $\|Dg^t|_{E^s}\|<Ce^{-\kappa t}$) give the same notion after enlarging $C$. Many texts write $\lambda^t$ with $0<\lambda<1$ instead of $e^{-\kappa t}$.
- In [2023, 197(1), no. 2] the condition is phrased as a continuous invariant splitting $TM=E^s\oplus N\oplus E^u$ with "$N$ tangent to the flow lines"; this is exactly $N=\mathbb{R}X$ with $X$ nowhere zero, as above. On a compact manifold of dimension $m\ge 2$, both $E^s$ and $E^u$ are automatically nonzero (if, say, $E^s=0$, then $|\det Dg^{-t}|\to 0$ uniformly, contradicting the fact that $g^{-t}$ preserves the total volume of $M$). On a compact manifold of dimension $3$ this forces $\dim E^s=\dim E^u=1$.
- That paper uses $r=\infty$, $\dim M=3$, and the hypotheses *transitive* (some orbit $\{g^tx\}_{t\in\mathbb{R}}$ is dense in $M$) and *topologically mixing* (for all non-empty open $U,V\subseteq M$ there is $T$ with $g^t(U)\cap V\neq\emptyset$ for all $t\ge T$). Its equilibrium measures (Definition #96) are taken with respect to the time-one map $g^1$.
- Standard examples: geodesic flows of compact Riemannian manifolds of negative sectional curvature (on the unit tangent bundle) and suspension flows of Anosov diffeomorphisms. A formaliser should note that the definition only uses the first derivative $Dg^t$, so $r=1$ suffices for the definition; higher $r$ is a hypothesis of the theorems.

## 92. Billiard ball map of a convex billiard table

*Chapter context.* The chapter on convex (Birkhoff) billiards in a text on Hamiltonian and area-preserving dynamics. The reader knows plane curves (arclength, curvature, the Jordan curve theorem), convex sets, homeomorphisms and diffeomorphisms of surfaces, and circle homeomorphisms with their rotation numbers; the billiard ball map and its phase cylinder are defined here.

**Setup 92.1 (billiard table).** Fix $k\ge 2$ (or $k=\infty$). A *convex billiard table* is a $C^k$ map $\gamma\colon \mathbb{R}\to\mathbb{R}^2$ which is periodic of some period $\ell>0$ (so $\ell$ is the length of the curve), is injective on $[0,\ell)$, satisfies $|\gamma'(s)|=1$ for all $s$ (arclength parametrisation), and has positive curvature
$$\kappa(s)=\det\big(\gamma'(s),\gamma''(s)\big)>0\qquad\text{for all } s.$$
The sign condition means $\gamma$ is oriented counterclockwise. We identify $\gamma$ with the closed curve $\gamma(\mathbb{R})$, and write $\tau(s)=\gamma'(s)$ for the unit tangent and $R_\theta$ for the counterclockwise rotation of $\mathbb{R}^2$ by angle $\theta$.

**Proposition 92.2.** Under 92.1, $\gamma(\mathbb{R})$ is the boundary of a compact, strictly convex set $\Omega\subset\mathbb{R}^2$ with non-empty interior, lying to the left of $\tau$: $R_{\pi/2}\tau(s)$ is the inward unit normal at $\gamma(s)$. Every line meets $\gamma$ in at most two points. Consequently, for every $s\in\mathbb{R}$ and $\delta\in(0,\pi)$ the ray $\{\gamma(s)+tR_\delta\tau(s): t>0\}$ meets $\gamma$ in exactly one point. (Standard; e.g. do Carmo, *Differential Geometry of Curves and Surfaces*, on convex curves.)

**Definition 92.3 (phase cylinder and billiard ball map).** The *phase cylinder* of $\gamma$ is
$$\mathbf{A}=(\mathbb{R}/\ell\mathbb{Z})\times(0,\pi),$$
where $(s,\delta)\in\mathbf{A}$ is identified with the oriented line through $\gamma(s)$ with direction $u=R_\delta\tau(s)$. This is a bijection between $\mathbf{A}$ and the set of oriented lines meeting the interior of $\Omega$: $\gamma(s)$ is the point where the oriented line enters $\Omega$, and $\delta$ is the angle from $\tau(s)$ to the line. The *billiard ball map* is $T\colon\mathbf{A}\to\mathbf{A}$, $T(s,\delta)=(s_1,\delta_1)$, where:

1. $\gamma(s_1)$ is the unique point of $\gamma$ on the ray $\{\gamma(s)+tu : t>0\}$ (Proposition 92.2), i.e. the point where the line leaves $\Omega$;
2. $\delta_1\in(0,\pi)$ is determined by $\cos\delta_1=\langle u,\tau(s_1)\rangle$.

Equivalently, $T(s,\delta)$ is the oriented line through $\gamma(s_1)$ with direction $u_1=R_{\delta_1}\tau(s_1)=2\langle u,\tau(s_1)\rangle\tau(s_1)-u$, the mirror image of $u$ in the tangent line at $\gamma(s_1)$: the angle of incidence equals the angle of reflection. The *boundary* of the phase cylinder is $\{\delta=0\}\cup\{\delta=\pi\}$ (the oriented lines tangent to $\gamma$); $T$ extends to the closed cylinder $(\mathbb{R}/\ell\mathbb{Z})\times[0,\pi]$ by the identity on the boundary.

**Proposition 92.4.** (a) $T$ is a homeomorphism of $\mathbf{A}$ (a $C^{k-1}$ diffeomorphism), and its extension to the closed cylinder is a homeomorphism. (b) With $L(s,s_1)=|\gamma(s)-\gamma(s_1)|$ one has $\partial L/\partial s=-\cos\delta$ and $\partial L/\partial s_1=\cos\delta_1$ whenever $T(s,\delta)=(s_1,\delta_1)$; hence $T$ preserves the area form $\sin\delta\, d\delta\wedge ds$ ($=ds\wedge d(\cos\delta)$). (c) (Twist.) $T$ is a monotone twist map: for fixed $s$, a lift of $s_1$ to $\mathbb{R}$ is strictly increasing in $\delta$, tending to $s$ as $\delta\to 0$ and to $s+\ell$ as $\delta\to\pi$. (d) $T^{-1}=I\circ T\circ I$ with $I(s,\delta)=(s,\pi-\delta)$ (time reversal).

**Definition 92.5 (rotational invariant curves).** A *rotational invariant curve* of $T$ is a subset $\alpha\subset\mathbf{A}$ homeomorphic to a circle, not null-homotopic in $\mathbf{A}$ (it winds once around the cylinder), with $T(\alpha)=\alpha$. Lift $T$ to $\tilde T(\tilde s,\delta)=(\tilde s_1,\delta_1)$ on $\mathbb{R}\times(0,\pi)$ with $\tilde s<\tilde s_1<\tilde s+\ell$. The *rotation number* of $\alpha$ is
$$\rho(\alpha)=\lim_{n\to\infty}\frac{\tilde s_n-\tilde s_0}{n\ell}\in(0,1),\qquad (\tilde s_n,\delta_n)=\tilde T^n(\tilde s_0,\delta_0),\ (\tilde s_0,\delta_0)\text{ over }\alpha,$$
which exists and is independent of the starting point (rotation number of the circle homeomorphism $T|_\alpha$). An orbit $\{T^n x\}$ is *$q$-periodic* if $T^qx=x$.

*Remarks.*

- Conventions differ: many texts use $(s,\cos\delta)$ or $(s,-\cos\delta)$ (Birkhoff coordinates; then $T$ preserves $ds\wedge d(\cos\delta)$ and the boundary is $\{\cos\delta=\pm1\}$), or record the incoming rather than the outgoing angle; for the reflection law these agree, since the incoming and outgoing angles at $\gamma(s_1)$ with $\tau(s_1)$ are equal.
- [2022, 196(1), no. 2] takes $\gamma$ $C^2$, centrally symmetric ($-\gamma(\mathbb{R})=\gamma(\mathbb{R})$ after translation), counterclockwise, and uses exactly the coordinates $(s,\delta)$ above, where $\gamma(s)$ is the "incoming point" of the line; it also uses the coordinates $(p,\varphi)$ of an oriented line ($\varphi$ the angle of its right unit normal with the horizontal, $p$ its signed distance to the origin), identifying the space of oriented lines with $T^*S^1$, with the same invariant area form. Its "domain between $\alpha$ and $\{\delta=0\}$" is the component of $\mathbf{A}\setminus\alpha$ adjacent to $\{\delta=0\}$; orbits there have rotation numbers near $0$.
- By Birkhoff's theorem, every rotational invariant curve of a monotone twist map is the graph $\delta=f(s)$ of a Lipschitz function; a formaliser may take "graph of a continuous function" as the definition of rotational invariant curve in this setting. For the circle (radius $r$), every horizontal circle $\{\delta=c\}$ is invariant with rotation number $c/\pi$, and $T(s,\delta)=(s+2r\delta,\delta)$.

## 93. Billiard flow in a polygon

*Chapter context.* The chapter on polygonal billiards in a text on ergodic theory of geometric dynamical systems. The reader knows simple polygons in $\mathbb{R}^2$, Lebesgue measure, measurable flows and measure-preserving flows on probability spaces (ergodicity, eigenfunctions, weak mixing); the billiard flow and its Liouville measure are defined here.

Throughout, $P\subset\mathbb{R}^2$ is a *polygon*: the compact region bounded by a simple closed polygonal curve with vertices $w_1,\dots,w_n$ ($n\ge 3$) and sides $S_i=[w_i,w_{i+1}]$ (indices mod $n$). Write $P^\circ$ for its interior, $V=\{w_1,\dots,w_n\}$, and $S^1=\{v\in\mathbb{R}^2:|v|=1\}$ with arclength measure $d\theta$. For a side $S$ let $e_S\in S^1$ be a direction of $S$, $n_S$ the unit normal to $S$ pointing into $P$, and $\sigma_S(v)=2\langle v,e_S\rangle e_S-v$ the reflection in the line of $S$ (so $\langle\sigma_S v,n_S\rangle=-\langle v,n_S\rangle$). Every $p\in\partial P\setminus V$ lies in the relative interior of exactly one side, written $S(p)$.

**Definition 93.1 (phase space).** Let $\sim$ be the equivalence relation on $P\times S^1$ generated by $(p,v)\sim(p,\sigma_{S(p)}v)$ for $p\in\partial P\setminus V$ (elastic reflection: an outgoing unit vector at a boundary point is identified with its mirror image, the incoming angle with the side being $\pi$ minus the outgoing one). The *phase space* (unit tangent bundle of the table) is $T_1(P)=(P\times S^1)/\sim$, with quotient map $\pi$. Each class not over $V$ has a unique *inward representative* $(p,v)$: $p\in P^\circ$, or $p\in\partial P\setminus V$ with $\langle v,n_{S(p)}\rangle\ge 0$, the case of equality (vectors tangent to a side) being a self-identification.

**Definition 93.2 (billiard trajectory).** Let $(p_0,v_0)$ be an inward representative with $\langle v_0,n_{S(p_0)}\rangle>0$ if $p_0\in\partial P$. Put $t_0=0$ and recursively, while defined:
$$\tau_k=\sup\{t>0:\ p_k+sv_k\in P^\circ\text{ for all }s\in(0,t)\},\qquad q_{k+1}=p_k+\tau_kv_k\in\partial P,\qquad t_{k+1}=t_k+\tau_k .$$
If $q_{k+1}\in V$ the trajectory *hits a vertex* and stops. Otherwise set $p_{k+1}=q_{k+1}$ and $v_{k+1}=\sigma_{S(q_{k+1})}v_k$ (one checks $\langle v_k,n_{S(q_{k+1})}\rangle<0$, so $v_{k+1}$ points strictly inward and $\tau_{k+1}\in(0,\infty)$). The *forward billiard trajectory* is $t\mapsto(p_k+(t-t_k)v_k,\ v_k)$ for $t\in[t_k,t_{k+1})$.

**Proposition 93.3.** (a) If the forward trajectory never hits a vertex, then $t_k\to\infty$ (finitely many reflections in finite time: near a vertex of interior angle $\beta$, unfolding by reflections turns the trajectory into a straight line, which crosses at most $\lceil\pi/\beta\rceil+1$ copies of the corner). (b) Let $\Sigma\subset T_1(P)$ be the set of classes lying over $V$ or over a vector tangent to a side, or such that the forward trajectory of $x$ or of its time reversal $J(x)$ hits a vertex, where $J[(p,v)]=[(p,-v)]$ (well defined since $\sigma_S$ is linear). Then $\pi^{-1}(\Sigma)$ is a Borel set of Lebesgue measure zero: after unfolding, the states whose trajectory hits a vertex after a prescribed sequence of sides form a $2$-dimensional set $\{(p,v): v=(w'-p)/|w'-p|\}$ ($w'$ a reflected image of a vertex), and there are countably many sequences.

**Definition 93.4 (billiard flow and Liouville measure).** Let $X_P=T_1(P)\setminus\Sigma$. For $x=[(p_0,v_0)]\in X_P$ (inward representative) and $t\ge0$ put $F^t(x)=\pi(p_k+(t-t_k)v_k,v_k)$ for the unique $k$ with $t\in[t_k,t_{k+1})$; for $t<0$ put $F^t=J\circ F^{-t}\circ J$. The family $\{F^t\}_{t\in\mathbb{R}}$ is the *billiard flow* of $P$. It satisfies: $F^t(X_P)=X_P$, $F^0=\mathrm{id}$, $F^{s+t}=F^s\circ F^t$ on $X_P$ for all $s,t\in\mathbb{R}$, and $(t,x)\mapsto F^t(x)$ is Borel on $\mathbb{R}\times X_P$. The *Liouville measure* is the Borel probability measure on $T_1(P)$
$$\mu_P=\frac{1}{2\pi\,\mathrm{Area}(P)}\ \pi_*\big(\mathrm{Leb}_P\otimes d\theta\big),$$
which gives $\Sigma$ measure $0$. Each $F^t$ preserves $\mu_P$: between collisions $F^t$ acts by $(p,v)\mapsto(p+tv,v)$, a translation in $p$ for fixed $v$, and collisions act by the isometry $\sigma_S$ of $S^1$. Thus $(T_1(P),\mu_P,\{F^t\})$ is a measure-preserving flow, defined $\mu_P$-almost everywhere.

*Remarks.*

- A formaliser may avoid the quotient: by Definition 93.1, $X_P$ is in measurable bijection with a full-measure Borel subset of $\{(p,v):p\in P^\circ\}\cup\{(p,v):p\in\partial P\setminus V,\ \langle v,n_{S(p)}\rangle>0\}$, and $\mu_P$ corresponds to normalised $\mathrm{Leb}_{P^\circ}\otimes d\theta$ (the boundary part is null). Equivalently one may study the *billiard map* (first return to the inward boundary vectors), but [2026, 203(3), no. 1] works with the flow.
- That paper uses the unnormalised measure $\mathrm{Leb}\otimes d\theta$ pushed forward by $\sim$ (normalisation is irrelevant for ergodic properties), arbitrary simple polygons with $n\ge3$ sides, and "weakly mixing" in the usual sense for flows: no non-constant measurable $f$ with $f\circ F^t=e^{2\pi i\alpha t}f$ a.e. for all $t$; equivalently $F^t\times F^t$ is ergodic for $\mu_P\otimes\mu_P$.
- For a rational polygon (all angles in $\pi\mathbb{Q}$) the directions $v$ visited by one orbit form a finite set (orbit of the finite dihedral group generated by the linear parts $\sigma_S$), so $F^t$ is not ergodic on $T_1(P)$; restricted to the invariant surface of one direction-orbit it is the straight-line flow on the translation surface obtained by unfolding $P$ (Katok and Zemlyakov). Theorem 1.3 of the paper concerns those translation flows.
- Polygons with polygonal holes are also standard tables; the definitions above apply verbatim with $\partial P$ a finite union of disjoint simple closed polygonal curves.

## 94. Borel complete class of countable structures

*Chapter context.* The chapter on Borel reducibility of isomorphism relations in a text on invariant descriptive set theory. The reader knows standard Borel spaces and Borel maps, analytic sets, Polish group actions and the space $\mathrm{Mod}_L(\omega)$ of $L$-structures with universe $\omega$, its logic action of $S_\infty$, the isomorphism relation $\cong_K$ and Borel classes $K$ (Definition #98); Borel completeness is defined here.

**Definition 94.1 (Borel reducibility).** Let $X,Y$ be standard Borel spaces and $E\subseteq X^2$, $F\subseteq Y^2$ equivalence relations. A *Borel reduction* of $E$ to $F$ is a Borel map $\beta\colon X\to Y$ such that for all $x,x'\in X$
$$x\,E\,x'\iff \beta(x)\,F\,\beta(x').$$
Write $E\le_B F$ if one exists. The relation $\le_B$ is reflexive and transitive (a preorder on equivalence relations on standard Borel spaces).

**Definition 94.2 (Borel complete).** Let $L$ be a countable language and $K\subseteq\mathrm{Mod}_L(\omega)$ a Borel class, i.e. an isomorphism-invariant Borel set, with isomorphism relation $\cong_K$ (Definition #98). Then $K$ is *Borel complete* if for every countable language $L'$ and every Borel class $K'\subseteq\mathrm{Mod}_{L'}(\omega)$,
$$\cong_{K'}\ \le_B\ \cong_K ,$$
i.e. there is a Borel map $\beta\colon K'\to K$ such that for all $\mathcal{A},\mathcal{B}\in K'$: $\mathcal{A}\cong\mathcal{B}\iff\beta(\mathcal{A})\cong\beta(\mathcal{B})$. Equivalently, $\cong_K$ is a $\le_B$-greatest element among isomorphism relations of Borel classes of countable structures. For an isomorphism-closed class $\mathbf{K}$ of $L$-structures with $\mathbf{K}_\omega$ Borel, "$\mathbf{K}$ is Borel complete" means "$\mathbf{K}_\omega$ is Borel complete".

**Theorem 94.3 (Friedman and Stanley).** The class $\mathrm{Graph}_\omega$ of graphs (an irreflexive symmetric binary relation $E$) on $\omega$ is Borel complete; so are countable linear orders and countable trees. (H. Friedman and L. Stanley, *A Borel reducibility theory for classes of countable structures*, J. Symbolic Logic, 1989.)

**Proposition 94.4.** For a Borel class $K\subseteq\mathrm{Mod}_L(\omega)$ the following are equivalent:

1. $K$ is Borel complete;
2. $\cong_{\mathrm{Graph}_\omega}\ \le_B\ \cong_K$;
3. for every countable language $L'$, $\cong_{L'}\ \le_B\ \cong_K$ on all of $\mathrm{Mod}_{L'}(\omega)$;
4. for every Borel (not necessarily invariant) $Y\subseteq\mathrm{Mod}_{L'}(\omega)$, $L'$ countable, the restriction of $\cong_{L'}$ to $Y$ is $\le_B\ \cong_K$;
5. ($S_\infty$-completeness) for every standard Borel space $X$ with a Borel action of $S_\infty$, the orbit equivalence relation $E_X$ satisfies $E_X\le_B\ \cong_K$.

(1)$\Leftrightarrow$(2)$\Leftrightarrow$(3)$\Leftrightarrow$(4) follow from 94.3 by composing and restricting reductions; (5)$\Rightarrow$(3) is trivial and (3)$\Rightarrow$(5) uses the Becker–Kechris theorem that every Borel $S_\infty$-space Borel-embeds equivariantly into some $\mathrm{Mod}_{L'}(\omega)$ (Becker and Kechris, *The Descriptive Set Theory of Polish Group Actions*).

*Remarks.*

- Borel reducibility here is for the relations on the spaces themselves (domain $X$), not reducibility of the sets $E\subseteq X^2$ as subsets (a map with domain $X^2$); [2024, 199(3), no. 4] stresses this distinction (its Definitions 1.2, 1.4, Remark 1.5).
- In that paper (Definition 1.6) a Borel class is "a Borel class of structures with domain $\omega$" and the defining condition quantifies over all Borel classes $K_2$, of arbitrary countable language; by Proposition 94.4(4) it does not matter whether $K_2$ is required to be invariant. Modern terminology: "$\cong_K$ is $S_\infty$-complete". The Main Theorem there gives a reduction as in 94.4(2) for $K=\mathrm{TFAB}_\omega$ (torsion-free abelian groups, in the language $\{e,\cdot,{}^{-1}\}$) which is even continuous.
- Borel completeness implies that $\cong_K$ is complete analytic as a subset of $K\times K$, and that $\cong_K$ is not Borel; the converse of the first implication fails (Friedman–Stanley: torsion abelian groups). A Borel reduction $\beta$ induces an injection on isomorphism types; it need not be injective as a map of structures, nor have invariant image.

## 95. Dynamical degree of a dominant rational self-map

*Chapter context.* A chapter on degree growth in a text on algebraic dynamics. The reader knows projective varieties over a field, rational and dominant rational maps (domain of definition, composition), the graph of a rational map, intersection numbers $(D_1\cdots D_d)$ of Cartier divisors on a $d$-dimensional projective variety, the real Néron–Severi space $N^1(X)_{\mathbb{R}}$ of numerical classes, ample, nef and big classes, pull-back of divisor classes by morphisms and the projection formula; the degrees $\deg_{k,\omega}(f)$ and dynamical degrees $\lambda_k(f)$ are defined here.

Throughout, $K$ is a field, $X$ is a normal projective variety (integral, projective over $K$) of dimension $d\ge1$, and $f\colon X\dashrightarrow X$ is a dominant rational map with domain of definition $U\subseteq X$ (a dense open set). The iterates $f^n=f\circ\dots\circ f$ ($n\ge1$) are again dominant rational self-maps of $X$, and $f^0=\mathrm{id}_X$.

**Definition 95.1 (graph).** The *graph* of $f$ is the closed subvariety $\Gamma_f\subseteq X\times_K X$ defined as the Zariski closure of $\{(x,f(x)):x\in U\}$. It is an integral projective variety of dimension $d$; the first projection $\pi_1\colon\Gamma_f\to X$ is birational and the second projection $\pi_2\colon\Gamma_f\to X$ is surjective and generically finite.

**Definition 95.2 ($k$-th degree).** Let $\omega\in N^1(X)_{\mathbb{R}}$ be an ample class (more generally a big and nef class) and $0\le k\le d$. The *$k$-th degree of $f$ with respect to $\omega$* is the real number
$$\deg_{k,\omega}(f)=\big((\pi_2^*\omega)^{k}\cdot(\pi_1^*\omega)^{d-k}\big)_{\Gamma_f},$$
the intersection number on $\Gamma_f$ of $k$ copies of $\pi_2^*\omega$ and $d-k$ copies of $\pi_1^*\omega$ (extended $\mathbb{R}$-multilinearly from Cartier divisors). Equivalently it may be computed on any projective variety $\widetilde\Gamma$ with a birational morphism $\mu\colon\widetilde\Gamma\to\Gamma_f$ (e.g. a resolution of singularities), replacing $\pi_i$ by $\pi_i\circ\mu$: by the projection formula the value does not change. Writing $f^*=\pi_{1*}\circ\pi_2^*$ on numerical cycle classes, $\deg_{k,\omega}(f)=(f^*\omega^k\cdot\omega^{d-k})_X$. One has $\deg_{k,\omega}(f)>0$, $\deg_{0,\omega}(f)=(\omega^d)$, and if $\omega=c_1(L)$ for a line bundle $L$ then $\deg_{k,\omega}(f)$ is a positive integer.

**Theorem 95.3 (sub-multiplicativity and comparison).** (a) There is a constant $C=C(X,\omega)>0$ such that for all dominant rational maps $f,g\colon X\dashrightarrow X$ and all $k$,
$$\deg_{k,\omega}(f\circ g)\le C\,\deg_{k,\omega}(f)\,\deg_{k,\omega}(g).$$
(b) For big and nef classes $\omega,\omega'$ there is $C'=C'(\omega,\omega')\ge1$ with $C'^{-1}\deg_{k,\omega}(f)\le\deg_{k,\omega'}(f)\le C'\deg_{k,\omega}(f)$ for all dominant $f$. (Dinh and Sibony over $\mathbb{C}$; Truong, and Dang, over arbitrary fields.)

**Definition 95.4 (dynamical degrees).** For $0\le k\le d$, the *$k$-th dynamical degree* of $f$ is
$$\lambda_k(f)=\lim_{n\to\infty}\deg_{k,\omega}(f^n)^{1/n}\in[1,\infty).$$
By 95.3(a) the sequence $a_n=C\deg_{k,\omega}(f^n)$ is sub-multiplicative, so by Fekete's lemma the limit exists and equals $\inf_n a_n^{1/n}$; by 95.3(b) it does not depend on $\omega$.

**Proposition 95.5.** (a) $\lambda_0(f)=1$, and $\lambda_d(f)$ is the topological degree $[K(X):f^*K(X)]$. (b) (Birational invariance.) If $\varphi\colon X\dashrightarrow Y$ is birational, $Y$ normal projective, then $\lambda_k(\varphi\circ f\circ\varphi^{-1})=\lambda_k(f)$. (c) (Log-concavity, from the Khovanskii–Teissier inequalities.) $\lambda_k(f)^2\ge\lambda_{k-1}(f)\lambda_{k+1}(f)$ for $0<k<d$; in particular $\lambda_1(f)^2\ge\lambda_2(f)$. (d) If $X$ is geometrically integral (e.g. $K$ algebraically closed), $\lambda_k(f)$ is unchanged by extension of the base field.

*Remarks.*

- The dependence on $f$ is only through $\Gamma_f\subseteq X\times X$: $\deg_{k,\omega}(f)=\big([\Gamma_f]\cdot \mathrm{pr}_1^*\omega^{d-k}\cdot\mathrm{pr}_2^*\omega^{k}\big)_{X\times X}$. In general $\deg_{k,\omega}(f^n)\neq\deg_{k,\omega}(f)^n$ (already on $\mathbb{P}^d$ when $f$ has indeterminacy points, and for automorphisms of other varieties), which is why the limit is needed; for an endomorphism of $\mathbb{P}^d$ of degree $e$ (a morphism), $\deg_{k,\omega}(f^n)=e^{nk}$ and $\lambda_k(f)=e^k$.
- For $X=\mathbb{P}^d$ and $\omega$ the hyperplane class, $\deg_{1,\omega}(f)$ is the common degree of homogeneous polynomials $f_0,\dots,f_d$ without common factor with $f=[f_0:\dots:f_d]$, and $\lambda_1(f)=\lim_n(\deg f^n)^{1/n}$.
- [2021, 194(1), no. 5] uses $X$ normal projective over a field of characteristic $0$ (algebraically closed in its Section 1), $\omega$ ample or big and nef, and defines $\deg_{k,\omega}(f)=(\pi_2^*\omega^k\cdot\pi_1^*\omega^{d-k})$ on a resolution of the graph, as above. Its Theorem 2 concerns a proper polynomial map $f\colon\mathbb{A}^d_K\to\mathbb{A}^d_K$ (automatically finite and surjective, hence dominant); there $\lambda_k(f)$ means $\lambda_k$ of the induced dominant rational self-map of $\mathbb{P}^d_K\supseteq\mathbb{A}^d_K$.

## 96. Equilibrium state (measure) of a Hölder potential

*Chapter context.* The chapter on thermodynamic formalism in a text on ergodic theory of smooth and hyperbolic dynamical systems. The reader knows invariant Borel probability measures, the Kolmogorov–Sinai entropy $h_\mu(T)$ of a measure-preserving map (as recalled in the background to Definition #97), topological entropy, Hölder spaces $C^\theta(M)$ (Definition #32) and Anosov flows (Definition #91); topological pressure and equilibrium states are defined here.

**Setup 96.1.** Let $(X,d)$ be a compact metric space. For a continuous map $T\colon X\to X$ let $\mathcal{M}(T)$ be the set of $T$-invariant Borel probability measures on $X$ (non-empty, convex and weak-$*$ compact). For a continuous flow $g=\{g^t\}_{t\in\mathbb{R}}$ on $X$ let $\mathcal{M}(g)=\bigcap_{t\in\mathbb{R}}\mathcal{M}(g^t)$, the *flow-invariant* probability measures; for $\nu\in\mathcal{M}(g)$ write $h_\nu(g^1)$ for the Kolmogorov–Sinai entropy of the time-one map $g^1$ (then $h_\nu(g^t)=|t|\,h_\nu(g^1)$ by Abramov's formula). A continuous function $\varphi\colon X\to\mathbb{R}$ is called a *potential*. Assume $h_{\mathrm{top}}(T)<\infty$, resp. $h_{\mathrm{top}}(g^1)<\infty$ (true for Lipschitz maps and $C^1$ flows on compact manifolds).

**Definition 96.2 (pressure).** The *pressure* of a potential $\varphi$ is
$$P_T(\varphi)=\sup_{\mu\in\mathcal{M}(T)}\Big(h_\mu(T)+\int_X\varphi\,d\mu\Big)\in\mathbb{R},$$
and for a flow and a potential $F$,
$$P_g(F)=\sup_{\nu\in\mathcal{M}(g)}\Big(h_\nu(g^1)+\int_X F\,d\nu\Big)\in\mathbb{R}.$$

**Theorem 96.3 (variational principle).** $P_T(\varphi)$ equals the topological pressure
$$\lim_{\varepsilon\to0}\limsup_{n\to\infty}\frac1n\log\sup\Big\{\sum_{x\in E}e^{\sum_{j=0}^{n-1}\varphi(T^jx)}:\ E\subseteq X\ (n,\varepsilon)\text{-separated}\Big\},$$
where $E$ is $(n,\varepsilon)$-separated if $\max_{0\le j<n}d(T^jx,T^jy)>\varepsilon$ for all distinct $x,y\in E$. Similarly $P_g(F)$ equals the analogous quantity with $\sum_{j<n}\varphi\circ T^j$ replaced by $\int_0^tF\circ g^s\,ds$ and $(t,\varepsilon)$-separation measured by $\max_{0\le s\le t}d(g^sx,g^sy)$, $t\to\infty$. Moreover $P_g(F)=P_{g^1}(F_1)$ with $F_1=\int_0^1F\circ g^s\,ds$. (Walters, *An Introduction to Ergodic Theory*; Bowen and Ruelle, *The ergodic theory of Axiom A flows*, 1975.)

**Definition 96.4 (equilibrium state).** An *equilibrium state* (or *equilibrium measure*) for $T$ with potential $\varphi$ is a measure $\mu\in\mathcal{M}(T)$ attaining the supremum in 96.2:
$$h_\mu(T)+\int_X\varphi\,d\mu=P_T(\varphi).$$
An equilibrium state for the flow $g$ with potential $F$ is a measure $\nu\in\mathcal{M}(g)$ (invariant under every $g^t$) with
$$h_\nu(g^1)+\int_XF\,d\nu=P_g(F).$$
When $X=M$ is a compact Riemannian manifold and $F\in C^\theta(M)$ for some $\theta\in(0,1]$, one speaks of an equilibrium state of a *Hölder potential*.

**Theorem 96.5 (Bowen–Ruelle).** Let $g$ be a transitive Anosov flow (of class $C^2$, say) on a compact Riemannian manifold $M$, and let $F$ be Hölder continuous. Then $F$ has exactly one equilibrium state $\nu_{g,F}$. It is ergodic, gives positive mass to every non-empty open set, and $\nu_{g,F}=\nu_{g,F'}$ whenever $F'-F$ is the sum of a constant and the derivative $Xu$ along the flow of a function $u$ that is $C^1$ along flow lines with $u$ and $Xu$ continuous. The analogous statement holds for transitive Anosov diffeomorphisms.

*Remarks.*

- In [2023, 197(1), no. 2] (Definition 3.5 there) the pressure is $\mathrm{Pr}_g(F)=\sup_\nu[\int F\,d\nu+h_\nu(g^1)]$ over $g$-invariant probability measures, the flow being $C^\infty$ transitive Anosov on a compact $3$-manifold, and $\nu_{g,F}$ is the unique maximiser of 96.5. A formaliser should note that the supremum is over *flow*-invariant measures; with $\mathcal{M}(g^1)$ in place of $\mathcal{M}(g)$ one must replace $F$ by $F_1$.
- Sign conventions differ: some authors write potentials as $-\varphi$, or call $\mu$ an equilibrium state for $-\beta\varphi$ ("inverse temperature" $\beta$). Special cases: $F=0$ gives the measure of maximal entropy (Definition #97; for Anosov flows, the Bowen–Margulis measure), and $F=-\frac{d}{dt}\big|_{t=0}\log|\det Dg^t|_{E^u}|$ gives the SRB measure (the Liouville measure if $g$ preserves a smooth volume).
- Existence of equilibrium states holds whenever $\mu\mapsto h_\mu$ is upper semicontinuous on $\mathcal{M}(T)$ (e.g. for expansive maps, by weak-$*$ compactness); uniqueness genuinely needs hyperbolicity plus a regularity condition such as the Hölder property of the potential.

## 97. Measure of maximal entropy

*Chapter context.* The chapter on entropy in a graduate text on ergodic theory and smooth dynamics. The reader knows measure-preserving transformations, finite measurable partitions and their joins, conditional expectation, the ergodic decomposition, and the topological entropy $h_{\mathrm{top}}(f)$ of a continuous self-map of a compact metric space (via $(n,\varepsilon)$-separated sets, or equivalently open covers); Kolmogorov–Sinai entropy, the variational principle and measures of maximal entropy are treated here.

**Definition 97.1 (Kolmogorov–Sinai entropy).** Let $(X,\mathcal{B},\mu)$ be a probability space and $f\colon X\to X$ a measurable map with $f_*\mu=\mu$. For a finite measurable partition $\xi=\{A_1,\dots,A_k\}$ of $X$ put $H_\mu(\xi)=-\sum_i\mu(A_i)\log\mu(A_i)$ (with $0\log0=0$), and let $\xi^n=\xi\vee f^{-1}\xi\vee\dots\vee f^{-(n-1)}\xi$ be the partition into the non-empty sets $A_{i_0}\cap f^{-1}A_{i_1}\cap\dots\cap f^{-(n-1)}A_{i_{n-1}}$. Then
$$h_\mu(f,\xi)=\lim_{n\to\infty}\frac1n H_\mu(\xi^n)=\inf_{n\ge1}\frac1nH_\mu(\xi^n)$$
(the limit exists since $n\mapsto H_\mu(\xi^n)$ is subadditive), and the *(measure-theoretic, metric or Kolmogorov–Sinai) entropy* of $\mu$ is
$$h_\mu(f)=\sup\{h_\mu(f,\xi):\ \xi\text{ a finite measurable partition}\}\in[0,\infty].$$
It is an invariant of measure-theoretic isomorphism.

**Proposition 97.2.** Let $f\colon X\to X$ be a continuous map of a compact metric space, and $\mathcal{M}(f)$ the (non-empty, convex, weak-$*$ compact) set of $f$-invariant Borel probability measures, with $\mathcal{M}_e(f)$ its ergodic elements (the extreme points). Then:

(a) (Variational principle; Dinaburg, Goodman, Goodwyn, Misiurewicz.)
$$h_{\mathrm{top}}(f)=\sup_{\mu\in\mathcal{M}(f)}h_\mu(f)=\sup_{\mu\in\mathcal{M}_e(f)}h_\mu(f).$$

(b) (Affinity; Jacobs.) If $\mu=\int\mu_x\,d\mu(x)$ is the ergodic decomposition of $\mu\in\mathcal{M}(f)$, then $h_\mu(f)=\int h_{\mu_x}(f)\,d\mu(x)$; in particular $\mu\mapsto h_\mu(f)$ is affine on $\mathcal{M}(f)$.

(See Walters, *An Introduction to Ergodic Theory*, chapters 4 and 8.)

**Definition 97.3 (measure of maximal entropy).** Let $f\colon X\to X$ be a continuous map of a compact metric space with $h_{\mathrm{top}}(f)<\infty$. A *measure of maximal entropy* (m.m.e.) of $f$ is a measure $\mu\in\mathcal{M}(f)$, i.e. an $f$-invariant Borel probability measure, such that
$$h_\mu(f)=h_{\mathrm{top}}(f).$$
Write $\mathrm{MME}(f)\subseteq\mathcal{M}(f)$ for the set of measures of maximal entropy. An *ergodic m.m.e.* is an element of $\mathrm{MME}(f)\cap\mathcal{M}_e(f)$; $f$ has a *unique m.m.e.* if $\mathrm{MME}(f)$ is a singleton.

**Proposition 97.4.** Assume $h_{\mathrm{top}}(f)<\infty$. (a) $\mathrm{MME}(f)$ is convex, and if $\mu\in\mathrm{MME}(f)$ then $\mu$-almost every ergodic component of $\mu$ is an ergodic m.m.e. (by 97.2(b)); hence the ergodic m.m.e.'s are exactly the extreme points of $\mathrm{MME}(f)$, and $f$ has a unique m.m.e. iff $\mathrm{MME}(f)\neq\emptyset$ and there is exactly one ergodic m.m.e. (b) If $\mu\mapsto h_\mu(f)$ is upper semicontinuous on $\mathcal{M}(f)$ (e.g. $f$ expansive, or $f$ a $C^\infty$ map of a compact manifold by Newhouse's theorem), then $\mathrm{MME}(f)$ is non-empty and weak-$*$ compact. (c) $\mathrm{MME}(f)$ may be empty in general (Misiurewicz constructed $C^r$ diffeomorphisms, $r<\infty$, without m.m.e.).

*Remarks.*

- $\mathrm{MME}(f)$ coincides with the set of equilibrium states of the potential $0$ (Definition #96).
- [2022, 195(2), no. 2] writes $h(f,\nu)$ for $h_\nu(f)$ and $\mathcal{P}(f)$, $\mathcal{P}_e(f)$ for $\mathcal{M}(f)$, $\mathcal{M}_e(f)$, and uses Definition 97.3 for a $C^\infty$ diffeomorphism $f$ of a closed surface (compact $2$-dimensional $C^\infty$ Riemannian manifold without boundary), where $h_{\mathrm{top}}(f)<\infty$ automatically. There, $f$ is *topologically transitive* if some $x\in M$ has both $\{f^n x\}_{n\ge0}$ and $\{f^{-n}x\}_{n\ge0}$ dense in $M$, and *topologically mixing* if for all non-empty open $U,V$ one has $f^n(U)\cap V\neq\emptyset$ for all sufficiently large $n$. "Isomorphic to a Bernoulli scheme" means measure-theoretically isomorphic to the shift on $(A^{\mathbb{Z}},p^{\otimes\mathbb{Z}})$ for a probability vector $p$ on a finite or countable set $A$.
- The topological entropy may be defined with $(n,\varepsilon)$-spanning or separated sets (Bowen–Dinaburg) or with open covers (Adler–Konheim–McAndrew); all agree on compact metric spaces, and depend only on the topology. For a homeomorphism, $h_\mu(f)=h_\mu(f^{-1})$, so $\mathrm{MME}(f)=\mathrm{MME}(f^{-1})$.

## 98. Polish space of countable structures $\mathrm{Mod}_L(\omega)$

*Chapter context.* The opening chapter on spaces of countable structures in a text on invariant descriptive set theory. The reader knows first-order languages and structures, isomorphisms, Polish spaces, standard Borel spaces (Cantor space $2^\omega$, Baire space $\omega^\omega$, countable products, the fact that a Borel subset of a standard Borel space is standard Borel) and continuous actions of Polish groups; the space of $L$-structures on $\omega$ is defined here.

Throughout, $\omega=\{0,1,2,\dots\}$, $L$ is a *countable* first-order language consisting of relation symbols $R$ of arity $n_R\ge 1$ and function symbols $f$ of arity $m_f\ge 0$ (constant symbols being $0$-ary function symbols), and $S_\infty$ is the Polish group of all bijections $\omega\to\omega$ (topology of pointwise convergence, i.e. as a $G_\delta$ subspace of $\omega^\omega$).

**Definition 98.1 (the space $\mathrm{Mod}_L(\omega)$).** Let
$$\mathrm{Mod}_L(\omega)=\prod_{R\in L}2^{\,\omega^{n_R}}\times\prod_{f\in L}\omega^{\,\omega^{m_f}},$$
where $2=\{0,1\}$ and $\omega$ carry the discrete topology, each factor carries the product topology, and the whole the product topology. A point $x=((x_R)_R,(x_f)_f)$ is identified with the $L$-structure $\mathcal{M}_x$ with universe $\omega$ in which $R^{\mathcal{M}_x}=\{\bar a\in\omega^{n_R}: x_R(\bar a)=1\}$ and $f^{\mathcal{M}_x}=x_f\colon\omega^{m_f}\to\omega$. This is a bijection between $\mathrm{Mod}_L(\omega)$ and the set of all $L$-structures whose universe is the set $\omega$. A basis of the topology consists of the sets
$$\{\mathcal{M}\in\mathrm{Mod}_L(\omega):\ \mathcal{M}\models\varphi_1(\bar a_1)\wedge\dots\wedge\varphi_k(\bar a_k)\},$$
with $\varphi_i$ atomic formulas of the form $R(\bar v)$, $\neg R(\bar v)$ or $f(\bar v)=w$ (variables only) and $\bar a_i$ tuples from $\omega$.

**Proposition 98.2.** (a) $\mathrm{Mod}_L(\omega)$ is a Polish space (a countable product of Polish spaces; if $L$ is relational and non-empty it is homeomorphic to the Cantor space $2^\omega$), hence a standard Borel space. (b) The Borel $\sigma$-algebra is generated by the sets $\{\mathcal{M}:\mathcal{M}\models\varphi(\bar a)\}$, $\varphi$ atomic, $\bar a\in\omega^{<\omega}$. (c) For every formula $\varphi(\bar v)$ of $L_{\omega_1\omega}$ (in particular every first-order formula) and every $\bar a$, the set $\{\mathcal{M}:\mathcal{M}\models\varphi(\bar a)\}$ is Borel; for quantifier-free first-order $\varphi$ it is clopen.

**Definition 98.3 (logic action and isomorphism).** $S_\infty$ acts on $\mathrm{Mod}_L(\omega)$ by transport of structure: for $g\in S_\infty$,
$$R^{g\cdot\mathcal{M}}(\bar a)\iff R^{\mathcal{M}}(g^{-1}\bar a),\qquad f^{g\cdot\mathcal{M}}(\bar a)=g\big(f^{\mathcal{M}}(g^{-1}\bar a)\big),$$
where $g^{-1}$ acts coordinatewise on tuples; thus $g$ is an isomorphism $\mathcal{M}\to g\cdot\mathcal{M}$. This *logic action* is continuous. For $\mathcal{M},\mathcal{N}\in\mathrm{Mod}_L(\omega)$ one has $\mathcal{M}\cong\mathcal{N}$ iff $\mathcal{N}=g\cdot\mathcal{M}$ for some $g\in S_\infty$; the *isomorphism relation* $\cong_L\ \subseteq\mathrm{Mod}_L(\omega)^2$ is this orbit equivalence relation. It is an analytic subset of $\mathrm{Mod}_L(\omega)^2$, in general not Borel.

**Definition 98.4 (invariant and Borel classes).** A set $K\subseteq\mathrm{Mod}_L(\omega)$ is *invariant* (isomorphism-invariant) if $\mathcal{M}\in K$ and $\mathcal{N}\cong\mathcal{M}$ imply $\mathcal{N}\in K$, i.e. $K$ is a union of $S_\infty$-orbits. A *Borel class of countable $L$-structures* is an invariant Borel subset $K\subseteq\mathrm{Mod}_L(\omega)$, regarded as a standard Borel space with the induced $\sigma$-algebra, together with the restriction $\cong_K$ of $\cong_L$ to $K\times K$. If $\mathbf{K}$ is a class of $L$-structures closed under isomorphism (e.g. graphs, groups, torsion-free abelian groups), write $\mathbf{K}_\omega=\{\mathcal{M}\in\mathrm{Mod}_L(\omega):\mathcal{M}\in\mathbf{K}\}$, the members of $\mathbf{K}$ with universe $\omega$; this is invariant, and it is Borel whenever $\mathbf{K}$ is axiomatised by a sentence of $L_{\omega_1\omega}$, by 98.2(c).

**Theorem 98.5 (Lopez-Escobar).** An invariant set $K\subseteq\mathrm{Mod}_L(\omega)$ is Borel if and only if $K=\{\mathcal{M}:\mathcal{M}\models\sigma\}$ for some sentence $\sigma$ of $L_{\omega_1\omega}$. (See Kechris, *Classical Descriptive Set Theory*; Gao, *Invariant Descriptive Set Theory*.)

*Remarks.*

- Many texts take $L$ relational only, with $X_L=\prod_R 2^{\omega^{n_R}}$; a function symbol may be replaced by the relation symbol for its graph, which identifies $\omega^{\omega^m}$ homeomorphically with a $G_\delta$ subset of $2^{\omega^{m+1}}$, so the two conventions give the same Polish topology (on structures with functions) and the same Borel classes. Some sources also allow $0$-ary relation symbols (a factor $2$).
- $\mathrm{Mod}_L(\omega)$ contains only countably *infinite* structures; finite ones, if needed, are coded on universes $n=\{0,\dots,n-1\}$ separately.
- In [2024, 199(3), no. 4] (Fact 1.1 and Notation 1.8 there, with $K^L_\omega$ for $\mathrm{Mod}_L(\omega)$), the classes used are $\mathrm{Graph}_\omega$ for $L=\{E\}$ (irreflexive symmetric $E$; a closed set) and $\mathrm{TFAB}_\omega$ for the group language (a closed set: the group axioms, commutativity and $nx\neq 0$ for $x\neq 0$, $n\ge1$, are each closed conditions).

## 99. Scaling limit of lattice $\phi^4$ fields (reachable random field)

*Chapter context.* The chapter on scaling limits in a text on lattice models of Euclidean field theory and critical phenomena. The reader knows probability measures on $\mathbb{R}^n$, convergence in distribution (weak convergence) of random vectors, the Kolmogorov extension theorem, Gaussian random vectors, and finite-volume Gibbs measures of lattice spin systems; the scaling limits of lattice $\phi^4$ and Ising fields are defined here.

Throughout, $d\ge1$, $\Lambda_R=[-R,R]^d$ for $R>0$, $V_R=\Lambda_R\cap\mathbb{Z}^d$, $x\sim y$ means $x,y\in\mathbb{Z}^d$ with $\|x-y\|_1=1$, and $C_0(\mathbb{R}^d)$ is the space of continuous real functions of compact support.

**Definition 99.1 (finite-volume lattice $\phi^4$ and Ising measures).** A *single-site measure* is either a $\phi^4$ measure $\rho_{\lambda,b}(d\varphi)=e^{-\lambda\varphi^4+b\varphi^2}\,d\varphi$ on $\mathbb{R}$ ($\lambda>0$, $b\in\mathbb{R}$, $d\varphi$ Lebesgue measure) or the Ising measure $\rho_{\mathrm{Is}}=\frac12(\delta_{-1}+\delta_{+1})$. Given a coupling $J\ge0$, a single-site measure $\rho$ and $R>0$, the *lattice system with free boundary conditions* is the probability measure on $\mathbb{R}^{V_R}$
$$\langle F\rangle_{J,\rho,R}=\frac{1}{Z}\int_{\mathbb{R}^{V_R}}F(\phi)\,\exp\Big(\sum_{\{x,y\}\subseteq V_R,\ x\sim y}J\,\phi_x\phi_y\Big)\prod_{x\in V_R}\rho(d\phi_x),$$
$Z$ being the value of the integral for $F=1$. That is, $H(\phi)=-\sum_{\{x,y\}\subseteq V_R,\,x\sim y}J\phi_x\phi_y$ and the density is $e^{-H}$. Since $\rho_{\lambda,b}$ has tails $e^{-\lambda\varphi^4}$, $0<Z<\infty$ and all moments of $\phi$ are finite; the measure is invariant under $\phi\mapsto-\phi$, so odd moments vanish. (The Ising model at inverse temperature $\beta$ is the case $\rho=\rho_{\mathrm{Is}}$, $J=\beta J_0$; $\rho_{\mathrm{Is}}$ is the $\lambda\to\infty$ limit of normalised $e^{-\lambda(\varphi^2-1)^2}d\varphi$.)

**Definition 99.2 (rescaled smeared field).** For $1\le L\le R$ put
$$\Sigma_L=\Big\langle\Big(\sum_{x\in V_L}\phi_x\Big)^2\Big\rangle_{J,\rho,R}>0,\qquad T_{f,L}(\phi)=\Sigma_L^{-1/2}\sum_{x\in V_R}f(x/L)\,\phi_x\quad(f\in C_0(\mathbb{R}^d)),$$
a real random variable on $(\mathbb{R}^{V_R},\langle\cdot\rangle_{J,\rho,R})$. Thus the lattice has spacing $1/L$ and the field is normalised so that the block sum over $\Lambda_L$ has variance $1$.

**Definition 99.3 (random fields).** A *random field* on $\mathbb{R}^d$ is a family $\Phi=(T_f(\Phi))_{f\in C_0(\mathbb{R}^d)}$ of real random variables on one probability space such that for all $f,g$ and $a,c\in\mathbb{R}$, $T_{af+cg}(\Phi)=aT_f(\Phi)+cT_g(\Phi)$ almost surely; it is considered up to equality of all finite-dimensional distributions (the laws of $(T_{f_1}(\Phi),\dots,T_{f_k}(\Phi))$). One writes formally $T_f(\Phi)=\int f(x)\Phi(x)\,dx$. If all $T_f(\Phi)$ have finite $n$-th moments, an *$n$-point Schwinger function* of $\Phi$ is a locally integrable $S_n\colon(\mathbb{R}^d)^n\to\mathbb{R}$ with
$$\mathbb{E}\Big[\prod_{j=1}^nT_{f_j}(\Phi)\Big]=\int_{(\mathbb{R}^d)^n}S_n(x_1,\dots,x_n)\prod_{j=1}^nf_j(x_j)\,dx_1\cdots dx_n\qquad\text{for all }f_j\in C_0(\mathbb{R}^d);$$
it is unique almost everywhere if it exists. $\Phi$ is a *generalized Gaussian process* if every vector $(T_{f_1}(\Phi),\dots,T_{f_k}(\Phi))$ is (jointly) Gaussian; for centred fields with all moments this is equivalent to Wick's law $S_{2n}(x_1,\dots,x_{2n})=\sum_\pi\prod_{j=1}^nS_2(x_{\pi(2j-1)},x_{\pi(2j)})$, the sum over pairings $\pi$ of $\{1,\dots,2n\}$, and vanishing odd Schwinger functions.

**Definition 99.4 (reachable random field).** A random field $\Phi$ on $\mathbb{R}^d$ is *reachable* (by lattice $\phi^4$ or Ising constructions) if there exist couplings $J_n\ge0$, single-site measures $\rho_n$, scales $L_n\to\infty$ and, for each $n$, volumes $R_{n,m}\to\infty$ ($m\to\infty$), such that for every $k\ge1$ and all $f_1,\dots,f_k\in C_0(\mathbb{R}^d)$:

1. (infinite-volume limit) for each $n$, the law of $(T_{f_1,L_n},\dots,T_{f_k,L_n})$ under $\langle\cdot\rangle_{J_n,\rho_n,R_{n,m}}$ (with $\Sigma_{L_n}$ computed in the same measure) converges weakly, as $m\to\infty$, to a probability measure $\mu_n^{f_1,\dots,f_k}$ on $\mathbb{R}^k$;
2. (continuum limit) $\mu_n^{f_1,\dots,f_k}$ converges weakly, as $n\to\infty$, to the law of $(T_{f_1}(\Phi),\dots,T_{f_k}(\Phi))$.

This is the double limit $\lim_{L\to\infty}\lim_{R/L\to\infty}$ along sequences, the parameters $(J,\rho)$ being allowed to vary with $L$.

**Proposition 99.5.** If (1) holds for all finite families and the measures $\mu_n^{f_1,\dots,f_k}$ converge weakly for all finite families, then the limits form a consistent family, and by the Kolmogorov extension theorem there is a random field $\Phi$, unique up to finite-dimensional distributions, with these limit laws; linearity holds since $T_{af+cg,L}=aT_{f,L}+cT_{g,L}$ identically and weak limits of measures carried by a closed hyperplane are carried by it. All $T_f(\Phi)$ are symmetric (law invariant under $t\mapsto -t$).

*Remarks.*

- This is Definition 1.1 of [2021, 194(1), no. 3], used in its Theorem 1.2 with $d=4$: every reachable $\Phi$ for which $S_2$ exists as a function with $\lim_{|x-y|\to\infty}S_2(x,y)=0$ is a generalized Gaussian process. The hypothesis on $S_2$ presupposes that the second moments of the limit exist and are given by a function; in the paper this comes from uniform local integrability of the rescaled correlation functions (infrared bound), and a formaliser stating the theorem should include "$S_2$ exists" explicitly.
- The paper states its results for single-site measures in the Griffiths–Simon class (its Definition 2.1), which contains all $\rho_{\lambda,b}$ and $\rho_{\mathrm{Is}}$; replacing "single-site measure" in 99.1 by "Griffiths–Simon measure" gives the more general notion. Its inner limit is meant to produce the infinite-volume Gibbs state $\langle\cdot\rangle_{J,\rho}$ as the limit of free-boundary states (for parameters below the critical point the infinite-volume state is unique and is such a limit, its Proposition 5.2).
- The paper sums over $x\in\mathbb{Z}^d$ in $T_{f,L}$; since $f$ has compact support and $R\to\infty$ first, summing over $V_R$ is the same for all large $R$.

## 100. Translation-invariant ergodic Gibbs measure on lozenge tilings of given slope

*Chapter context.* The chapter on infinite-volume lozenge tilings in a text on random tilings and dimer models. The reader knows graphs and perfect matchings, compact metrizable spaces and their Borel probability measures, conditional expectations, and measure-preserving actions of $\mathbb{Z}^2$ with their ergodic (equivalently, extremal invariant) measures; the space of tilings of the plane, height functions, the Gibbs property, slope and the measures $\mu_{s,t}$ are defined here.

**Definition 100.1 (triangular lattice and tilings of the plane).** The *triangular lattice* $\mathbb{T}$ is the graph with vertex set $\mathbb{Z}^2$ and an edge between $u$ and $v$ iff $v-u\in\{\pm(1,0),\pm(0,1),\pm(1,1)\}$. Its *faces* are the triangles $\{u,u+(1,0),u+(1,1)\}$ and $\{u,u+(0,1),u+(1,1)\}$, $u\in\mathbb{Z}^2$; each edge lies in exactly two faces. A *lozenge* (tile) is the union of two faces sharing an edge, its *inner edge*. A *lozenge tiling of the plane* is a set $M$ of edges of $\mathbb{T}$ such that every face contains exactly one edge of $M$; equivalently, a perfect matching (dimer covering) of the dual hexagonal graph, the tiles being the pairs of faces glued along the edges of $M$. A tile is of *type 1, 2 or 3* according as its inner edge is a translate of $\{0,(1,0)\}$, $\{0,(0,1)\}$ or $\{0,(1,1)\}$. Let $\mathfrak{E}(\mathbb{T})\subseteq\{0,1\}^{E(\mathbb{T})}$ be the set of tilings, with the product topology: it is a closed subset of a Cantor space (the condition is local), hence compact metrizable, and its Borel $\sigma$-algebra is generated by the events $\{e\in M\}$. Let $\mathfrak{P}(\mathbb{T})$ be the set of Borel probability measures on $\mathfrak{E}(\mathbb{T})$. For $w\in\mathbb{Z}^2$ the *shift* $\mathfrak{S}_w$ translates a tiling by $-w$, $\mathfrak{S}_wM=M-w$, and acts on $\mathfrak{P}(\mathbb{T})$ by push-forward.

**Proposition 100.2 (height function).** For each $M\in\mathfrak{E}(\mathbb{T})$ there is a unique $H=H_M\colon\mathbb{Z}^2\to\mathbb{Z}$ with $H(0,0)=0$ such that for all $u\in\mathbb{Z}^2$
$$H(u+(1,0))-H(u)=\mathbf{1}[\{u,u+(1,0)\}\in M],\quad H(u+(0,1))-H(u)=\mathbf{1}[\{u,u+(0,1)\}\in M],$$
$$H(u+(1,1))-H(u)=1-\mathbf{1}[\{u,u+(1,1)\}\in M].$$
(These increments sum consistently around every face because each face has exactly one edge in $M$.) The map $M\mapsto H_M$ is a bijection from $\mathfrak{E}(\mathbb{T})$ onto the set of $H\colon\mathbb{Z}^2\to\mathbb{Z}$ with $H(0,0)=0$ and $H(v)-H(u)\in\{0,1\}$ whenever $v-u\in\{(1,0),(0,1),(1,1)\}$.

**Definition 100.3 (Gibbs, translation-invariant, ergodic, slope).** Let $\mu\in\mathfrak{P}(\mathbb{T})$.

1. $\mu$ is a *Gibbs measure* if for every finite set $A$ of faces the following holds. Let $E_A$ be the set of edges both of whose faces lie in $A$, $\mathcal{F}_A$ the $\sigma$-algebra generated by the events $\{e\in M\}$, $e\notin E_A$, and $\Omega_A(M)=\{M'\in\mathfrak{E}(\mathbb{T}):M'\setminus E_A=M\setminus E_A\}$ (a finite set containing $M$). Then for every Borel $B\subseteq\mathfrak{E}(\mathbb{T})$,
$$\mu(B\mid\mathcal{F}_A)(M)=\frac{|B\cap\Omega_A(M)|}{|\Omega_A(M)|}\qquad\text{for }\mu\text{-a.e. }M,$$
i.e. conditionally on the tiling outside $A$, the tiling inside $A$ is uniform among the compatible ones.

2. $\mu$ is *translation-invariant* if $\mathfrak{S}_w\mu=\mu$ for all $w\in\mathbb{Z}^2$, and a translation-invariant $\mu$ is *ergodic* (*extremal*) if it is not a convex combination $p\mu_1+(1-p)\mu_2$, $0<p<1$, of translation-invariant $\mu_1\neq\mu_2$; equivalently every $\mathbb{Z}^2$-invariant Borel set has $\mu$-measure $0$ or $1$.
3. If $\mu$ is translation-invariant, its *slope* is
$$(s,t)=\Big(\mathbb{E}_\mu\big[H_M(1,0)-H_M(0,0)\big],\ \mathbb{E}_\mu\big[H_M(0,1)-H_M(0,0)\big]\Big)\in\overline{\mathcal{T}},\qquad \mathcal{T}=\{(s,t)\in\mathbb{R}_{>0}^2:s+t<1\};$$
by translation invariance $s$, $t$, $1-s-t$ are the densities of tiles of types $1$, $2$, $3$ (e.g. $s=\mu(\{0,(1,0)\}\in M)$).

**Theorem 100.4 (Sheffield).** For every $(s,t)\in\mathcal{T}$ there exists a unique translation-invariant ergodic Gibbs measure $\mu_{s,t}\in\mathfrak{P}(\mathbb{T})$ of slope $(s,t)$. (S. Sheffield, *Random Surfaces*, Astérisque 304, 2005; existence also follows from Kenyon, Okounkov and Sheffield, *Dimers and amoebae*, where $\mu_{s,t}$ arises as a limit of uniform tilings of large tori with height change approximately $(s,t)$ per period.)

**Definition 100.5.** For $(s,t)\in\mathcal{T}$, *the translation-invariant ergodic Gibbs measure of slope $(s,t)$* is the measure $\mu_{s,t}$ of Theorem 100.4.

*Remarks.*

- [2023, 198(3), no. 1] uses exactly these conventions (vertex set $\mathbb{Z}^2$; types 1, 2 for tiles whose inner edges are horizontal, vertical; extremality among translation-invariant measures; $\mathfrak{S}_w(v)=v-w$), and there $\lim_N\mathfrak{S}_{v_N}\mu_N=\mu_{s,t}$ "in distribution" means convergence of local statistics: for each finite set $F$ of edges and $B\subseteq F$, $\mathbb{P}_{\mathfrak{S}_{v_N}\mu_N}(M\cap F=B)\to\mu_{s,t}(M\cap F=B)$ (tilings of the finite domains $R_N$ are again sets of inner edges, and $F$ eventually lies inside $R_N-v_N$).
- Explicit description: with $X(M)=\{(x,y)\in\mathbb{Z}^2:\{(x,y),(x+1,y)\}\in M\}$ (positions of type 1 tiles), under $\mu_{s,t}$ the point process $X(M)$ is determinantal, $\mathbb{P}\big[(x_k,y_k)\in X(M)\ \forall k\le m\big]=\det[K_\xi(x_i,y_i;x_j,y_j)]_{i,j\le m}$, with $\xi=e^{\pi is}\sin(\pi t)/\sin(\pi-\pi s-\pi t)$ in the upper half-plane and the incomplete beta kernel $K_\xi(x_1,y_1;x_2,y_2)=\frac{1}{2\pi i}\int_{\bar\xi}^{\xi}(1-z)^{y_1-y_2}z^{x_2-x_1-1}\,dz$, the contour crossing $\mathbb{R}$ in $(0,1)$ if $y_1\ge y_2$ and in $(-\infty,0)$ if $y_1<y_2$ (Okounkov and Reshetikhin; Kenyon; as quoted in the paper's (1.2) and Definition 1.3). A formaliser may take this as an alternative definition, avoiding Theorem 100.4.
- For slopes on $\partial\mathcal{T}$ (frozen phases) uniqueness may fail; the Annals paper only uses $(s,t)\in\mathcal{T}$ (the liquid region). Other sources draw the lattice as the hexagonal lattice with angles $\pi/3$, or normalise heights so that they change by $\pm 1/3$ or $\pm 2/3$; slopes then differ by a fixed affine change of variables.

# Appendix: points flagged for review by the writers

Each entry was drafted by an AI agent, which then listed the claims and conventions a reviewer should check (statements derived by the writer rather than copied from a source, references cited from memory, convention clashes with the papers or with Tau Ceti). They are collected here by entry number.

### Definitions 1–11 (writer's notes)
- 1 Real rank: check rank of reductive = rank of derived group + split central torus, and the Borel–Tits / maximal-flat equivalences in the remarks.
- 2 p-block: the independence of the partition of Irr(G) from the maximal ideal is attributed to Osima from memory.
- 3 Defect group: check remarks on Green's S ∩ gS and Brauer's First Main Theorem; the Brauer correspondent is added (needed for Alperin–McKay).
- 4 Parabolic subgroups: check that every subgroup containing P is closed (writer-derived), the Langlands decomposition of Q_{Π'} and the formula for M_{Π'}, the dynamical description, and the remark on disconnected real forms.
- 5 Infinitesimal character: ρ-shifted Harish-Chandra parametrisation; sl_2 Casimir normalisation (verified against Nelson [2026, 203(3), no. 3]); check the L-packet infinitesimal-character statement.
- 6 Convergence of a spectral sequence: check the summary of Weibel's terminology and the reading of [2020, 191(3), no. 4].
- 7 Discrete series of GL_2(R): sign conventions in the reducibility statement are writer-derived; check the Langlands parameter.
- 8 Glauberman correspondence: check the exact form of Isaacs' theorem (cited Ch. 13 from memory) and the cyclic-S character formula.
- 9 Height zero characters: low risk.
- 10 HKR map: check the HKR isomorphism in positive characteristic (unnormalised map) and multiplicativity of the 1/n! version when Q ⊆ k.
- 11 Split Sp_2n, SO_l, GSpin_l: check that the Clifford model matches the root-datum GSpin_l (Asgari–Shahidi, Hundley–Sayag not verified), the computed spinor norm, and the low-rank isomorphisms.

### Definitions 12–21 (writer's notes)
- 12 Hodge structure on H^1 of an abelian variety: check the sign convention (iQ(α, ᾱ) > 0) and the reading of Kisin–Zhou's type remark; Masser–Zannier's conventions unchecked (paper unavailable).
- 13 Mumford–Tate group: tensor characterisation stated only for polarizable V (writer's sketch); check the GL_V × G_m variant and claims about Hg(A); DMOS cited without section.
- 14 Volume form ω^n: covers Hermitian (not only Kähler) forms; check the factors n! 2^n against Tau Ceti's `riemannianVolume` normalisation.
- 15 Ball quotient: existence/uniqueness extended to lattices with torsion via a finite quotient (standard, but not in the paper).
- 16 Rational Chow groups of a DM stack: check that Vistoli's rational equivalence is the naive one, the claim deg(V/p(V)) = 1/e_V in char 0, and the Kresch/Edidin–Graham comparison.
- 17 Cohomologically affine morphism: base-change statements in Prop. 17.4(b) deliberately weak; Alper's Prop. 3.10 not cited by number.
- 18 Cup product in étale cohomology: check sign conventions and the Ext/Yoneda sign remark.
- 19 Enriques surface: follows Schröer; standard.
- 20 Family of Enriques surfaces: check the attribution to Artin that a smooth proper 2-dimensional algebraic space over a field is a scheme, and the fppf-stack sketch in Prop. 20.3(a).
- 21 Fppf cohomology with supports: standard definition (the paper never defines it).

### Definitions 22–31 (writer's notes)
- 22 Galois action on étale cohomology of the geometric fibre: check the left-action convention, continuity via Huber's limit theorem for qcqs X, the comparison remark, and finiteness attributions (Scholze for ℓ = p; Huber/Berkovich for ℓ ≠ p).
- 23 Hodge-generic abelian variety: written WITHOUT the paper (Masser–Zannier not available); check whether the paper uses the pointwise or family notion, independence of the embedding (via Deligne's absolute Hodge theorem), and the Cattani–Deligne–Kaplan / André citations.
- 24 Moduli of stable maps: char 0; β as a homomorphism Pic(X) → Z (H_2 version as remark); check the virtual dimension formula and the char-p remark.
- 25 Nash blowup: intrinsic Grassmannian definition; check Remark 2 (blow-up of (∧^d Ω)/torsion) and the EGA I citation.
- 26 Normalized Nash blowup: paper writes "η∘ν" in reversed order (noted); check 26.3(e) and the locality argument in 26.3(d).
- 27 Perfect obstruction theory: Behrend–Fantechi; check φ maps to τ^{≥−1}L, the relative intrinsic normal cone description, and the global-resolution claim for GW obstruction theory.
- 28 Points of an algebraic stack: check the density argument for finite-type points and the loosely cited "group algebraic space locally of finite type over a field is a scheme".
- 29 Residual gerbe: Stacks Project lemmas checked online; the derivation Z_x ≃ BG_x (29.4) is the writer's own.
- 30 Theta divisor of a Jacobian: check the sign convention in Θ ≅ (id,φ)^*P (the paper writes Δ^*P^∨) and the normalisation ĥ = ½ĥ_Θ.
- 31 Totally geodesic subvariety of a ball quotient: "maximal" taken among strict ones (the paper, read literally, also counts S_Γ); check 31.5(b) and the Goldman reference.

### Definitions 32–40 (writer's notes)
- 32 C^k and Hölder spaces on a compact manifold: norm independence (Prop. 32.3) has only a proof hint; reading of the naked-singularity paper's C^{1,cε^2} regularity as a local statement in coordinates.
- 33 Domain of dependence for compressible Euler: Prop. 33.4 (uniqueness/union of developments) only sketched (Christodoulou); the claim about null generators of the characteristic boundary is hedged.
- 34 Neumann eigenvalues: check Prop. 34.3(iii) and its converse (polygon regularity; classical vs weak formulation on triangles via a logarithmic cut-off); u ∈ H^1 in Judge–Mondal's classical definition is the writer's reading.
- 35 Absolutely continuous spectrum: standard, low risk.
- 36 Amenable trace: check the equivalences in Prop. 36.4 (cited to Brown's memoir and Brown–Ozawa Ch. 6 without theorem numbers).
- 37 Caloric gauge: taken from Oh–Tataru arXiv:1709.08599; check the definition of an "Ḣ^1 solution" against their Lemma 5.26; the Annals paper's informal description omits Q < ∞.
- 38 Complex Hessian-type equation: the structural condition is restated as ∏ ∂f/∂λ_j ≥ γ (writer-derived equivalence); permutation-invariance of Γ made explicit.
- 39 Hard sphere dynamics: check the measure-theoretic form of Alexander's theorem (Thm 39.3); the paper's printed scattering formula seems to have lost a 1/ε^2 in extraction.
- 40 Laplace–Beltrami on L^2: check Prop. 40.4(ii) (σ_ess = [1/4,∞) for finite-area cusped hyperbolic surfaces); sign convention is opposite to the planned Tau Ceti `laplaceBeltrami := div ∘ grad`.

### Definitions 49–57 (writer's notes)
- 49 Second fundamental form: sign convention A(X,Y) = g(∇_X ν, Y), H = tr S (not divided by n); check 49.4(6) (convex, k-convex, uniformly k-convex) and 49.5 (level-set formula, Gauss equation); must agree with #66.
- 50 Lorentzian manifold: check the pointwise characterisation and the double-null/acoustical examples; `\slashed` unavailable, sphere metric written with a manual slash.
- 51 Null hypersurface: check Prop. 51.3 and the remark on achronal boundaries/Cauchy horizons (Hawking–Ellis).
- 52 Minimal hypersurface: also defines first/second variation, Jacobi operator, index, nullity, stability, bumpy metrics (on normal sections, covering one-sided hypersurfaces); decide whether these belong here; White's bumpy-metric theorem cited by title only.
- 53 Stationary varifold: check the remark that stationarity is metric-dependent.
- 54 Character variety of a surface group: check Prop. 54.4 carefully (closed orbits for real groups, Hausdorffness), attributed to Richardson / Richardson–Slodowy from memory.
- 55 Gaussian q-cluster: check uniqueness of simplicial clusters up to orthogonal maps (derived from the paper's Lemma 2.1) and the interface decomposition (Maggi, no chapter number).
- 56 Linearized Cauchy–Riemann operator: Wendl's conventions (no 1/2 in ∂̄_J); check the remark on the McDuff–Salamon factor-1/2 difference.
- 57 Lipschitz singular chains: normalised Hausdorff measure (differs from Mathlib's `hausdorffMeasure` by ω_d/2^d); check the Kirchheim citation and "Lipschitz chains compute singular homology".

### Definitions 58–66 (writer's notes)
- 58 MCG-finite representation: check that for semisimple ρ this equals finiteness of the orbit in the character variety.
- 59 Mapping class group: check the sanity-check list (Mod_{0,2}, Mod_{0,3}, Mod_{1,0}) and the inverse-isotopy continuity argument.
- 60 Normal Cauchy–Riemann operator: Wendl's normalisation; check D_u(du X) = du∘∂̄X (writer-derived), the index formula, and consistency with #56.
- 61 Outer action of MCG on π_1: check the Dehn–Nielsen–Baer citation (Farb–Margalit Ch. 8).
- 62 Riemannian symmetric space: check the curvature formula and the normalisation example (SL_2(R)/SO(2) curvature −1/2 under the Killing metric).
- 63 Compatible almost complex structures: check the contractibility claim (Cayley transform, McDuff–Salamon).
- 64 Spin^c structure: check restriction orientation conventions and the attribution of existence on 4-manifolds to Hirzebruch–Hopf.
- 65 Strict stability (Simon's inequality): check the spectral criterion λ_1 + ((N−2)/2)^2 > 0 and the C^1_c vs C^∞_c density remark.
- 66 Strictly convex boundary: sign conventions follow #49; check consistency.

### Definitions 67–74 (writer's notes)
- 67 Local components (restricted tensor product): Bump cited by chapter; reductive model over O_{F,S_0} and dim π_v^{K_v} ≤ 1 via Satake; the Steinberg/Atkin–Lehner sign matching for the 2020 paper was copied from the input, not re-derived.
- 68 Arithmetic lattice: Remark 2 (equivalence with the 2023 paper's version using all of H(R)) sketched by the writer; Mostow–Vinberg criterion restated relative to the trace field; check the claims about SO_0(n,1) (n even) and PU(1,n), n ≤ 3.
- 69 Galois representation of a cuspidal eigenform: arithmetic-Frobenius normalisation; check the reading of Pan [2026, 203(1), no. 3] (geometric Frobenius, so the relevant representation is the dual); coefficient field includes values of the nebentypus.
- 70 CM abelian scheme: ω(σ) vs Kings–Sprang's ω(−σ) labelling; the dual's O_L-action convention and its type Σ̄ are writer-derived; Kottwitz-condition equivalence hedged.
- 71 A_f of a weight-2 newform: End^0_Q(A_f) = K_f attributed to Ribet without a specific paper; End^0 over Q̄ = K_f for squarefree N is the writer's own argument.
- 72 CM automorphic representation: GL_n remark (Arthur–Clozel; different usage for n > 2) hedged.
- 73 Central character: Lemma 73.1 is the writer's own argument; the source paper uses the maximal F-split central torus; check the finite-volume claim.
- 74 Complex CM periods: check ⟨ξ(x), ξ^∨(y)⟩ = 2πi Tr(xy) (sign/normalisation vs Kings–Sprang Prop. 4.6) and Prop. 74.5(b) (writer-derived).

### Definitions 75–82 (writer's notes)
- 75 Critical infinity types: the Weil statement (Prop. 75.5, Serre "Abelian ℓ-adic representations" Ch. II) is quoted from memory; sign convention χ((λ)) = ∏σ(λ)^{μ(σ)} not checked against Tau Ceti's `AlgebraicInfinityType`.
- 76 π_f attached to a newform: adelic-lift conventions derived by hand (central character, K_0(N)-character, Hecke eigenvalue p^{1−k/2}a_p, L(π_f,s) = L(f,s+(k−1)/2)); check a_ℓ = −w_ℓ.
- 77 Emerton's completed cohomology: check attributions in Prop. 77.3; the paper's intro uses Y but its body uses X.
- 78 Good reduction of a hypersurface in an abelian variety: uniqueness of the smooth proper model cited only to BLR Ch. 1.
- 79 Minimal parabolic and Langlands decomposition (real rank one): check the explicit SO_0(n,1) matrices (computed by hand), P ∩ Θ(P) = MA, and the sign convention vs Tau Ceti's dynamic Levi decomposition.
- 80 Néron–Tate height: normalisation as in Yuan §4.3.1; the factor 1/2 in the pairing and O(2[O]) vs O([O]) must be matched to Tau Ceti's `canonicalHeight`.
- 81 Prismatic site: bounded prisms required (paper's intro omits "bounded"); check the characterisation of (p,I)-complete flatness and the size-cutoff remark (writer's own assertion).
- 82 Quasi-split unitary group of a self-dual hermitian lattice: the paper's "L = O_F^n ⊕ I" read as O_F^n ⊕ I^{⊕n}; Prop. 82.5(e) from general knowledge; the split-case isomorphism is writer-derived.

### Definitions 83–90 (writer's notes)
- 83 Schwartz algebra of an adelic reductive group: Prop. 83.3 (density, convolution, continuity) cited loosely to Wallach / Aizenbud–Gourevitch; π(f) assumes π_∞ Casselman–Wallach.
- 84 Selmer sections: real-place remark and the "theorem of Harari and Stix" lack exact references.
- 85 Stable Faltings height: metric convention as in Yuan §4.3.1; check base change of semistable Néron identity components (SGA 7 IX) and h_Fal(A) ≤ h(A/K) (writer's own derivation).
- 86 Symmetric power of a Weil–Deligne representation: check the explicit coefficient formula for d Sym^{n-1}(N) and normalisation-independence of the theorem.
- 87 Tate–Shafarevich group: kernel over all places with A(K̄_v); the existing Galois-module Ш (local terms H^1(G_v, A(K̄))) may be a different construction — agreement not claimed.
- 88 Weak functorial transfer: assumes the ρ-shifted Harish-Chandra isomorphism in Definition on infinitesimal characters.
- 89 ℓ-adic representation valued in Mumford–Tate group: H^1_et vs T_ℓA^∨⊗Q_ℓ = H^1(1) differ by a central twist; one convention should be fixed.
- 90 π-nearly isotypic subspace: the paper's proof lands in a smaller subspace (also matching infinitesimal characters).

### Definitions 91–100 (writer's notes)
- 91 Anosov flow: check 91.3 (metric independence, uniqueness, automatic continuity, adapted metric — only continuity claimed) and the volume argument that E^s, E^u ≠ 0.
- 92 Billiard ball map: rotational invariant curves added (needed by the theorem); check the rotation-number normalisation and twist/time-reversal claims.
- 93 Billiard flow in a polygon: check the one-line proofs in 93.3 (finitely many collisions in finite time; null singular set).
- 94 Borel complete class: check attribution of the S_∞ step to Becker–Kechris.
- 95 Dynamical degree: check 95.5(d) (base-field extension, geometrically integral X).
- 96 Equilibrium state: check hypotheses of Theorem 96.5 ("C^2, say").
- 97 Measure of maximal entropy: check the Misiurewicz example attribution and the Newhouse upper-semicontinuity claim.
- 98 Mod_L(ω): check that TFAB_ω is closed.
- 99 Reachable random field: needs the closest look — the paper's double limit is formalised as an iterated sequential limit; Theorem 1.2's S_2 condition presupposes S_2 exists.
- 100 Ergodic Gibbs measure on lozenge tilings: check height-increment sign conventions (derived from the paper's type 1/2/3 description) and the transcribed determinantal kernel.
