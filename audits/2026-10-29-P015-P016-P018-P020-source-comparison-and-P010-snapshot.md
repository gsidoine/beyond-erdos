# Consolidation pass 2 — primary-source collision audit and P010 manuscript provenance

**Date:** 2026-10-29. **Status:** follow-up to [the full first-collection assessment](2026-10-29-P001-P020-first-collection-consolidation.md). **No new problems**, no claims of certified originality or independent peer review.

## Research decision

The distinctions between the P001–P020 questions and established results require theorem-level comparisons. Place **P015** under especially high source-collision risk, preserve **P018** and **P020** only as **precisely scoped** new observables, and preserve **P016** as an *apparently distinct* hereditary complex, rather than claiming to invent Sidon/topological methods.

The following comparisons were made from source-level publication text where accessible, not only title similarities. The unavailable full text of the August 2026 P015 preprint is an explicit limitation.

## P015: what the 2025 and 2026 triangulation papers do (and do not) establish

[P015](../problems/geometry/P015-odd-area-lattice-triangulations.md) asks about **arbitrary fixed four-color sequences** around a convex polygon; each triangular face must use three pairwise distinct colors. The four colors are the reductions of lattice vertices modulo 2.

1. **Debrohim, Sasaki, Nunes (26 August 2026)**, [*Cyclically Colored Triangulations: Enumeration and Connectedness of Reconfiguration Graphs*](https://arxiv.org/abs/2608.26006), establishes valid-flip connectivity for **cyclically repeated $j$-colorings, $j\ge4$**. This gives a genuine **settled subfamily** of P015. The available abstract does **not** assert arbitrary four-color patterns are connected. We could not obtain all full-text proofs in this pass; therefore the possibility that an argument extends immediately remains unresolved. **Do not claim P015 fully open or fully solved.**
2. **Acharya, Mütze, Verciani (2025)**, [*Flips in colorful triangulations*](https://doi.org/10.20382/jocg.v16i1a9), proves connectivity/Hamiltonicity for various **two-color** vertex patterns where each triangle must contain **both** colors (no monochromatic triangle). Their "arbitrary coloring pattern with at least 10 changes" result is a two-color statement; it is **not the three-distinct-out-of-four constraint** in P015.
3. **Baur, Bergerova, Voon, Xu (2025)**, [*Flip graphs of coloured triangulations of convex polygons*](https://doi.org/10.12958/adm2312), studies colored *triangulations and colored flips*, with state and move definitions that require an explicit comparison before inferential use.

**Verdict:** P015's genuinely proposed extension is **arbitrary fixed four-color pattern** beyond the proven cyclic regime; the parity translation is elementary and not claimed novel. **Flagship promotion remains on hold**, pending proof-level comparison of Debrohim et al.

## P018: group-labeled bases already exist, but fixed-fiber *connectivity* is a separate question

Directly consulted the **20-page ICALP 2024** paper by Hörsch, Imolay, Mizutani, Oki and Schwarcz, [*Problems on Group-Labeled Matroid Bases*](https://doi.org/10.4230/LIPIcs.ICALP.2024.86). Its introduction defines labels $\psi:E\to\Gamma$ on matroid bases and the **zero-basis** target label as a group-sum constraint. It explicitly observes that a nonzero target can be shifted to zero by adding a coloop.

This proves that the **fixed-sum group-label constraint itself is established mathematics**, not a new definition. Their principal results include algorithms for finding constrained bases, proximity/limited exchange results toward *some* feasible basis, and hardness results. For example, their **Theorem 3.1** characterizes the degenerate case when all bases of a matroid have the same label using **single-exchange neighborhoods**. This is **not** the same as requiring all basis-exchange intermediates to preserve a specified label, i.e., connectedness of an entire exact-label *fiber*.

**P018's surviving observable:** the least permitted simultaneous exchange cardinality $t$ required to connect the exact-XOR sum-$s$ basis fiber **inside the same available-vector set $W$**, and its behavior under random deletion. Its $d=5$ obstruction is a result about that fiber graph; it does **not** contradict 2024 proximity results allowing intermediate bases with different sums.

**Additional exact finite refinement:** for the existing ten-vector example with two 2-exchange components (sizes 4 and 2), the minimum 3-exchange distance between bases in opposite components is **3**, so allowing exchanges of sizes **up to 3 reconnects this particular six-basis fiber**. Thus its local exchange-connectivity number is exactly **3**, not an unspecified larger number. This is an exact observation, **not a general $d=5$ classification**.

**Verdict:** retain provisionally as a **high-overlap, carefully differentiated fixed-fiber reconfiguration problem**. Do not call the group-label-conservation concept itself novel.

## P016: source-level comparison distinguishes two mathematical complexes

**Superdock**, [*Simplicial complexes from finite projective planes and colored configurations*](https://doi.org/10.1016/j.disc.2022.113117), constructs complexes from **colored configurations and projective-plane incidence structures**. His work establishes correspondences between *individual Sidon sets in finite groups*, particular linear codes, and colored configurations, and proposes topological obstructions to the existence of certain difference sets.

By contrast, P016's exact object is the **hereditary complex of all Sidon subsets of the ordered interval $[N]$**, with faces defined by absence of repeated positive differences. Its minimal nonfaces encode three-term arithmetic progressions and disjoint-pair additive collisions. The objects are **not identical as stated** in Superdock's paper; however, this is not an exhaustive equivalence audit through every construction or general hypergraph independence-complex theorem.

**Verdict:** P016 remains a plausible apparent-novelty candidate, **not** a newly invented connection between Sidon sets and topology. Treat finite $\mathbb F_2$ Betti tables as evidence only, not persistence barcodes.

## P020: distinguish structured Hankel dependence from several known random-cokernel regimes

The precise P020 target is the **complete isomorphism-type law of the cokernel** of a Hankel matrix whose $2n-1$ anti-diagonal parameters are independent Haar $\mathbb Z_p$ elements.

**Already known / not claimed original:**
- **Dwivedi–Grinberg (2022)** finite-field Hankel rank counts: the exact corank tail gives $\Pr(C_n=0)=1-p^{-1}$ and rules out the **usual independent-entry Cohen–Lenstra limit**.
- **Wang–Stanley (2017)**, [*The Smith Normal Form Distribution of a Random Integer Matrix*](https://doi.org/10.1137/16M1098140), establishes random integer-matrix Smith-form distributions through polynomial congruences; this is general algebraic-statistical prior art but does not in its stated abstract give an asymptotic distribution for **Haar p-adic Hankel-specific** matrices.
- **Kovaleva (2023)**, [*On the distribution of equivalence classes of random symmetric p-adic matrices*](https://doi.org/10.1112/mtk.12212), treats **symmetric** p-adic matrices; every Hankel matrix is symmetric, but the converse is not true. Haar on the full symmetric-matrix space is **not** the Haar measure on its Hankel subspace, so this is a close *but not identical* distribution.
- **Jang–Kaplan–Lee–Yu (2026)**, [*A mod $p$ determinant criterion for Cohen–Lenstra convergence of random p-adic matrices with prescribed zero patterns*](https://arxiv.org/abs/2606.06993), studies independent entries subject to **zero masks**, not the **perfect correlation** of repeated anti-diagonal entries.
- **Van Peski (2024)**, [*Local limits in p-adic random matrix theory*](https://doi.org/10.1112/plms.12626), gives a more general modern probabilistic Smith-form framework.

**Exact scope:** knowing the rank law over $\mathbb F_p$ determines the number of invariant factors divisible by $p$, **not their higher $p$-adic valuations**. P020 asks for those complete valuations and convergence as $n\to\infty$. In accessible targeted searches, no theorem giving the exact specific Haar-Hankel finite abelian group law was located. **Absence of a search result is not priority certification**.

**Verdict:** retain as a **strong potential flagship** subject to another search on $p$-adic moment matrices, linear recurrences and rational-function/Hankel Smith forms.

## P009: an arithmetic distinction supported by an explicit witness

The known short-prime-difference certificate supplies two prime sums $q$ and $q+2n$. It is **a sufficient construction**. A two-color pairing need **not** use primes separated by $2n$.

For **$n=4$**, the perfect matching on $[8]$

$$
\{(1,6),(2,5),(3,8),(4,7)\}
$$

uses prime sums $\{7,11\}$, whose difference is **4**, while $2n=8$. Each of the eight integers is covered exactly once. This **disproves a structural converse** saying that *every* two-prime-palette solution must be of the standard $q,q+2n$ form.

**Logical caution:** this does **not** disprove equivalence between the *existence* of some two-palette matching and the *existence* of some classical short-prime-pair certificate, since a separate certificate does exist for $n=4$. The universal-existence relationship remains unresolved.

## P010: supplied two-page manuscript (not included in the public repository)

The reviewed manuscript is a **two-page A4 PDF** with title **The Minimum Number of Coprime Adjacencies in a Permutation**. It states the internally proved path-cover theorem, gives the largest-prime-factor construction and prime-counting inequality, includes eight references, and discloses substantive ChatGPT involvement in mathematical exploration, proof construction, code and literature help.

**Snapshot provenance (filename as uploaded):** `coprime_adjacencies(1).pdf`
**SHA-256:** `3aae034589f58b9593891a53ee5d54ea20f1106c774364e1ff564df417837737`
**Public PDF upload:** **not performed**. The repository has the full mathematical proof and P010 dossier. A checksum allows the author to recognize this particular manuscript without public redistribution during journal selection.

**Journal policy check, 2026-10-29:** The [official current *Integers* author instructions](https://math.colgate.edu/~integers/submit.html) state that papers are not considered if AI was used to produce mathematics, code, bibliographic information or other content; the exception is limited to grammar/spelling and analogous basic presentation assistance. The manuscript's AI disclosure expressly goes **beyond that exception**. A compliance confirmation therefore cannot be truthfully supplied under the declared provenance. The author should **clarify with the editor if already submitted**, or use a venue with a compatible AI policy. **Do not delete or narrow an accurate disclosure to force compliance.**

**Publication status:** being prepared for or considered for submission, **not independently confirmed as submitted or accepted**. This note does not assert a journal decision. It does not replace an independent mathematical referee report.

## Decision

The comparison does not identify an exact published equivalent of every remaining question. It does sharpen the distinction between a **proved known subcase**, an **existing mathematical object**, a **plausibly distinct new observable**, and a **certified historical open problem**. We have not yet certified the final category for any of the twenty.

Next source-level priorities: P008's arithmetic critical-window proof versus general deterministic-host percolation, P003's exact arithmetic factor-cut inequalities versus known prime-sum expansion, and P017's divisor-poset random height versus existing percolation time constants. **Keep P021+ frozen.**
