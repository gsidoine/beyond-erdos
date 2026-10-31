# Second consolidation pass — close-predecessor and obstruction checks

**Date:** 29 October 2026  
**Coverage:** P008, P015, P018, P020; directly related [P010 manuscript policy audit](../manuscripts/P010-2026-10-29-submission-snapshot-and-policy-audit.md).  
**Scope:** Mathematical and bibliographic comparisons for the indicated entries.

## P015: distinction from recent colored-triangulation theorems

**Problem under consideration:** any strictly convex lattice polygon with an **arbitrary** cyclic sequence of the four parity classes in $(\mathbb Z/2\mathbb Z)^2$. All triangular faces must have **three different** parity classes. Edges of the configuration graph are **diagonal flips** preserving the three-distinct-class constraint.

**Nearest direct results:**

1. **Baur–Bergerova–Voon–Xu (2024), [*Flip graphs of coloured triangulations of convex polygons*](https://arxiv.org/abs/2402.06546)**. This paper examines *colored triangulations and colored flips*, with an emphasis on connected components. Its model is not automatically the same as static four-color vertex constraints.
2. **Acharya–Mütze–Verciani (2025), [*Flips in colorful triangulations*](https://doi.org/10.20382/jocg.v16i1a9)**, permits **arbitrary binary vertex colorings** subject to the weaker constraint that every triangle has **both** colors; it even proves Hamiltonicity for arbitrary patterns with sufficiently many changes. Our **four-valued, all-distinct-on-triples** condition does not follow from that theorem as stated.
3. **Debrohim–Sasaki–Nunes (submitted August 26, 2026), [*Cyclically Colored Triangulations: Enumeration and Connectedness of Reconfiguration Graphs*](https://arxiv.org/abs/2608.26006)**. This is the **closest predecessor**. Its abstract says the vertex-color pattern is **periodically cyclic** in $j$ colors. It reports connectedness of the valid-flip graph whenever valid triangulations exist for $j\ge4$. Our arbitrary parity patterns need not be periodic. In the sources accessible during this review the **full new preprint text was not retrieved**, so we cannot certify whether the proofs extend or implicitly cover arbitrary patterns.

**Editorial decision:** **hold / high overlap risk**, not demote as known and not promote as original. At a minimum, explicitly compare its arbitrary-color formulation with the conditions of Theorem(s) in the August 2026 preprint *once the full text is accessible*. Previous exhaustive tests up to ten vertices support the statement only for small cases, not novelty or a proof.

## P018: independently reproduced obstruction and sharpened finite datum

Let $W=\{2,5,8,11,21,22,24,26,27,30\}\subset\mathbb F_2^5\setminus\{0\}$ (vectors encoded by integers in binary), with total XOR label $s=1$.

A **separate implementation** enumerated all $\binom{10}{5}=252$ candidate five-element subsets, computed their XORs and ranks over $\mathbb F_2$, and recovered **exactly six** valid bases. Their simultaneous **two-vector replacement graph** has component sizes **4 and 2** as claimed in P018.

**Additional exact finding:** allowing exchanges of *up to three* vectors connects all six bases. A concrete cross-component 3-exchange is

$$
\{2,5,8,21,27\}\longrightarrow\{8,21,24,26,30\}.
$$

The two bases share $\{8,21\}$ and both have XOR total $1$, so this changes **three** vectors. Consequently the **minimum connecting exchange size for this particular $W$ is exactly $3$**. This does **not** establish the universal value of $t(5)$ for all available sets; other $W$ could require more.

The historical anchor is **Hörsch–Imolay–Mizutani–Oki–Schwarcz (2024), [*Problems on Group-labeled Matroid Bases*](https://arxiv.org/abs/2402.16259)**. Its abstract explicitly covers group-sum constraints, allowed/forbidden basis labels and exchange-proximity conjectures. **The group-labelled-bases framework is known**; our fixed-label solution-fiber connectivity is a more specific reconfiguration observable. The accessible abstract does not establish an exact theorem for this observable. A full theorem-level comparison is still outstanding.

**Editorial decision:** retain as provisional flagship with **very high conceptual overlap risk**; preserve the explicit $d=5$ counterexample and the independently checked three-exchange bridge. The numerical datum is reproducible but not a general theorem.

## P020: separate rank from full $p$-adic cokernel structure

The **mod-$p$ Hankel corank formula** is known (Dwivedi–Grinberg 2022 and earlier). It gives $\Pr(\mathrm{corank}\ge k)=p^{-(2k-1)}$ and trivial cokernel probability $1-p^{-1}$, so the independent-entry Cohen–Lenstra distribution is **not** a valid limiting guess.

The genuine P020 question concerns **all invariant-factor exponents** in the Smith normal form and the **distribution over isomorphism classes of finite $p$-groups**; the rank law alone cannot recover this.

Additional recent nearby sources:

- **Jang–Kaplan–Lee–Yu (2026), [*A mod p determinant criterion for Cohen–Lenstra convergence of random p-adic matrices with prescribed zero patterns*](https://arxiv.org/abs/2606.06993)**. They treat matrices with **independent free entries** and structural *zeros*, which is different from a Hankel matrix's **repeated anti-diagonal variables**.
- **Jungin Lee–Myungjun Yu (September 2026), [*Cokernels of random p-adic orthogonal matrices and their linearizations*](https://arxiv.org/abs/2609.26404)**. This recent paper demonstrates that **structured algebraic random matrices can have parity-dependent distinct cokernel limits**, but the orthogonal/alternating matrix model is not a Hankel model.
- **Van Peski (2024), [*Local limits in p-adic random matrix theory*](https://doi.org/10.1112/plms.12626)**, provides a general reference for random $p$-adic Smith forms and local distribution questions, not an exact identified match to the Hankel model.

**Editorial decision:** retain P020 as high-upside conditional flagship, but *do not* claim that its full distribution is novel until specialists rule out known random-Hankel / linear-recurrence / moment-matrix Smith forms.

## P008: precision of the formulation

An implicit critical center $b_n$ defined by

$$
\sum_{v=1}^n (1-b_n)^{d_n(v)}=1
$$

is already a valid deterministic specification, so **"find an explicit center" is not a well-posed standalone conjecture**.

A rigorous replacement should demand an explicit **restricted asymptotic expression class**. One possible editorial specification (still to be reviewed mathematically) would ask for a finite elementary expression $B(n)$ involving only $n$, iterated logarithms, *specified numerical constants* and standard arithmetic functions, but **not** a root of the isolation equation, such that

$$
b_n-B(n)=o\!\left(\frac{\log\log n}{n}\right).
$$

An alternative is a finite closed form in *explicit prime-counting quantities*, with a quantified asymptotic error. It is essential to define what "explicit" means and which operations/number-theoretic functions are permitted. **No candidate formula $B(n)$ is asserted or proved in this audit.**

**Editorial decision:** keep "needs specification" and postpone flagship status. The existing internally claimed Poisson/Gumbel proof should be independently refereed before being cited as a published or externally verified result.

## Overall decision

- **No additions** (P001–P020 freeze maintained).
- **P015**: no originality promotion; the exact cyclic-color preprint comparison remains outstanding.
- **P018**: independently validated explicit obstruction, sharpened its exact finite minimum to three for the specified ten-vector set.
- **P020**: expanded the adjacent random-$p$-adic distribution literature with careful model distinctions.
- **P008**: proposed a precise research rephrasing *without* pretending it is already present or proved.
- **P010**: separate manuscript snapshot, citation check and urgent INTEGERS journal-policy warning.

This is a **second risk-focused pass**, not a full specialist refereeing of twenty results.
