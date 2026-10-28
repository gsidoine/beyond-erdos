# Research audit: P010 publication assessment and remaining directions

**Date:** 2026-10-28. **Scope:** literature harvest for P001–P009, publication readiness of the internally proved P010, and a new **incubator candidate** (not P011 in the curated catalogue).

## Executive judgment — P010

**Claim:** [P010 exact theorem](../theorems/P010-exact-coprime-adjacencies.md) gives, for every \(n\ge4\),
\[
h(n)=\pi(n)-\pi(n/2)+
\max\{1,\lceil(\pi(n/2)-\pi(n/3))/2\rceil\}.
\]
The proof is an **explicit optimal path-cover construction**, not an unproved guess or an asymptotic heuristic. Its finite regression tests have passed through \(n=10\,000\).

**Importance, conditional on novelty:** a **worthwhile, clean, short exact result** in multiplicative number theory and graph extremal combinatorics. It determines an extremal quantity for every \(n\) and identifies an unexpected \(7/12\) leading constant using a constructive largest-prime-factor decomposition with gluing via multiples of 2 and 3. It is **not** a solution of a longstanding public conjecture and does not yet establish a general graph theorem; do **not** describe it as a major breakthrough.

**Where it may fit:** a roughly 5–8-page note, with a focused title, original statement, detailed proof, rigorous context and perhaps a natural extension. *Discrete Mathematics* explicitly publishes shorter **Notes** within its graph/combinatorics scope; [official journal](https://shop.elsevier.com/journals/discrete-mathematics/0012-365X). [Combinatorics and Number Theory](https://msp.org/cnt/about/journal/about.html) is also broadly appropriate if the number-theoretic content is emphasized.

**Avoid inappropriate submission channels:**
- [INTEGERS submission rules](https://math.colgate.edu/~integers/submit.html) currently explicitly state that **they will not consider articles using AI to produce mathematics, code, bibliography or other content**. P010's AI-assisted development makes that a poor/ineligible venue under the stated rules; do not submit as-is.
- [Journal of Integer Sequences instructions](https://cs.uwaterloo.ca/journals/JIS/) prohibit using LLMs to write the **actual English words** of a paper. A contributor would have to write and check the manuscript independently and follow all relevant author policies; the existing AI-produced text is not submission copy.
- [Electronic Journal of Combinatorics](https://www.combinatorics.org/ojs/index.php/eljc/about/submissions) has strict AI-proof accountability and high substantiality standards. It demands that the author can vouch for and rewrite every AI-assisted proof in their own words; a single elementary specialized exact formula may struggle on significance alone.

**Non-negotiable publication gate:** (1) independent human proof referee; (2) targeted MathSciNet/zbMATH + OEIS + noncoprime-graph/GCD-permutation literature search, including synonym and citation-chain search; (3) independent manuscript written in compliance with the target journal's AI policy; (4) clarify the main contribution relative to prior graph path-cover theorems (Gallai–Milgram does **not** by itself yield the exact result here); (5) optional strengthening by deriving a general structural arithmetic path-cover lemma.

### Novelty search and the closest actual known results

- [Erdős–Freud–Hegyvári, *Arithmetical properties of permutations of integers* (1983)](https://www.maths.tcd.ie/EMIS/classics/Erdos/cit/51810063.htm): reviewed theorem summaries concern the **size** of gcd/lcm of consecutive terms, not the **minimum number of gcd-one transitions**.
- [Gómez–Wakabayashi, *Nontrivial path covers of graphs* (2020)](https://doi.org/10.1007/s10878-019-00488-w): defines/studies generic minimum path covers; no coprime arithmetic exact formula.
- [Fomin et al., *Path Cover, Hamiltonicity, and Independence Number: An FPT Perspective* (STOC 2026)](https://doi.org/10.1145/3798129.3800747): strongly recent path-cover framework and Gallai–Milgram results. Does not state the proposed exact arithmetic formula.
- [OEIS A076220](https://oeis.org/A076220) and [A086595](https://oeis.org/A086595): enumeration of permutations with **all** consecutive gcds equal to one, not minimization of their **number**.
- Search terms: "fewest coprime adjacent pairs", "minimum number of relatively prime consecutive pairs in a permutation", "maximum adjacent noncoprime pairs", "minimum path cover noncoprime graph", formula fragments in \(\pi(n/2)\), and the 1983 citation chain. **No exact matching theorem was found in the accessible results**. This is evidence only of an *unsuccessful search*, not a proof of novelty.

## Other selected problems — closest further sources and warnings

| ID | New/important close work | What it does or does not establish |
|---|---|---|
| P001 | [Greenfield & Greenfield (1998)](https://cs.uwaterloo.ca/journals/JIS/green.html) plus rainbow-matching methods | Prime-sum pairings are old; bounded palette-deficit of a **perfect** matching is not shown by partial rainbow constructions |
| P002 | [Dyer–Jerrum–Müller (2015/17)](https://www.numdam.org/article/AFST_2015_6_24_4_885_0.pdf) and [switch-chain survey](https://doi.org/10.1016/j.ejc.2021.103421) | 4-cycle matching switches established; host-specific irreducibility not implied by induced long cycles either way |
| P003 | [Hao–Li–Yu, *Bipartite binding number, k-factor and spectral radius* (2025)](https://doi.org/10.1016/j.disc.2025.114511); [Spectral conditions for k-extendability and k-factors (2026)](https://doi.org/10.1016/j.aam.2025.103019) | Supply **general sufficient factor criteria**, not an exact conclusion for the prime-sum Hankel graph. Must explicitly test their hypotheses rather than blindly assuming they apply. |
| P004 | Golomb-ruler local searches and Sidon theory (see prior audit) | Moving one mark is established; *valid-only, fixed-N* reconfiguration is different |
| P005 | [Sah–Sawhney, *Enumerating coprime permutations* (2022)](https://doi.org/10.1112/mtk.12159), specifically their probabilistic/absorbing perfect-matching argument | Directly establishes existence and asymptotic enumeration of the gcd-one bipartite matchings, **not** connectivity of their 4-switch graph |
| P006 | [Prime-distance graph coloring](https://research.ibm.com/publications/colouring-prime-distance-graphs), classical Sidon theory | P006 asks for **Sidon independent sets in the prime-distance graph**; generic prime-distance independent sets or generic Sidon bounds do not settle intersection extremum |
| P007 | [Panma–Rochanakul, *Prime-Graceful Graphs* (2021)](https://thaijmath.com/index.php/thaijmath/article/view/1264) | The fully graceful subquestion is already proved iff \(n\le5\); **only** the coprime-restricted extremal gracesize remains a candidate |
| P008 | [Gupta–Lee–Li (2021)](https://epubs.siam.org/doi/book/10.1137/1.9781611976465) and [Penrose (2018)](https://doi.org/10.1017/jpr.2018.9) | Much of the generic connectivity/Poisson machinery is classical; an explicit arithmetic **window center** needs a non-tautological precise formulation |
| P009 | [OEIS A202472](https://oeis.org/A202472) and Maillet-prime-difference literature | Precisely the *sufficient* two-prime difference certificates are old; a necessary-and-sufficient characterization of two-color arithmetic matchings remains absent |

## A genuine new **incubator** question: interval-sum factor saturation

A natural additive generalization of the P003 host is the balanced bipartite graph \(H_n(a,b)\) with row and column vertex labels \(0,\ldots,n-1\), and an edge \((i,j)\) exactly when \(a\le i+j\le b\). Define its minimum degree \(\delta\) and maximum number \(\lambda\) of edge-disjoint perfect matchings.

**Incubator question:** does
\[
\lambda(H_n(a,b))=\delta(H_n(a,b))
\]
hold for every \(n\) and every interval of allowed sums \([a,b]\)?

- **Exact exhaustive test**: All valid intervals, all \(n\le40\), satisfy the equality by integral max flow. The numerical script [\`experiments/test_interval_sum_factors.py\`](../experiments/test_interval_sum_factors.py) reproduces this finite experiment using SciPy.
- **Why the restriction is real:** for arbitrary sets of allowed sums it fails already for \(n=3\), \(S=\{1,3\}\). The matrix \(\bigl(\begin{smallmatrix}0&1&0\\1&0&1\\0&1&0\end{smallmatrix}\bigr)\) has minimum degree 1 but no perfect matching, since rows 0 and 2 have only column 1 as neighbor.
- **Established adjacent theory:** Convex-bipartite graphs, Toeplitz and Hankel support matrices, and standard bipartite \(k\)-factors are well studied. In particular, [Hao–Li–Yu (2025)](https://doi.org/10.1016/j.disc.2025.114511) give conditions for general factors. I have **not** found the exact interval-sum assertion, but the search was not exhaustive and the assertion may follow easily from known interval-matrix theorems.

**Status: exploratory, conjectural, no new P011 ID.** Before any promotion, derive a direct analytic proof or find a counterexample at larger \(n\), then check literature under "interval Hankel matrices", "Toeplitz banded matrices", "bipartite convex graphs" and "regular factor".

## Next research gate

- **P010:** prioritize human mathematical checking and historical priority, then assess an honest independent short paper. It does not need additional million-scale brute-force checks.
- **P003/P005:** try structural theorems (P003 arithmetic cut expansion; P005 canonical reconfiguration) rather than merely larger numbers.
- **Incubator:** establish factor saturation for interval-sum graphs or kill it; it becomes a formal research problem only if a substantive theorem or novel obstruction survives the literature check.
