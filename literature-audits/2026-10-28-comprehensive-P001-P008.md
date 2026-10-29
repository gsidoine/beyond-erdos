# Comprehensive prior-art audit: P001–P008

**Date:** 28 October 2026  
**Purpose:** Adversarial literature review of the eight candidate questions selected for Beyond Erdős.  
**Scope:** Targeted searches across publisher articles, arXiv, proceedings, OEIS, Erdős Problems, reference lists, and terminology/equivalence checks. This is a **substantial but non-exhaustive** audit. No systematic subscription-only MathSciNet/zbMATH search or independent specialist assessment is represented as completed.

> **Key correction:** Part of P007 was **already proved in 2021**. The full coprime-graceful path problem is identical to Panma–Rochanakul, Theorem 2.1. P007's *extremal count of distinct gaps* remains a separate candidate question. This is a factual prior-art collision, not just a similarity.

## Executive classification

| ID | Verdict as of this audit | Most important predecessor | Exact formulation found settled? |
|---|---|---|---|
| P001 | Keep as **unverified arithmetic rainbow-matching question** | Greenfield–Greenfield (1998), prime-sum pairings; rainbow matchings literature | No |
| P002 | Keep as **unverified arithmetic switch-connectivity question** | Dyer–Jerrum–Müller (2016/17) and Bonamy et al. (2019) | No |
| P003 | Keep as **unverified arithmetic factor-packing question** | Prime-sum graph Hamiltonicity (2021) and standard bipartite $k$-factor cut criteria | No |
| P004 | Keep as **unverified Golomb-ruler exchange question** | Sidon/Golomb ruler constructions and one-mark local-search algorithms | No |
| P005 | Keep as **unverified coprime matching-switch question** | Pomerance and Sah–Sawhney (2022); switch-chain literature | No |
| P006 | Keep as **unverified forbidden-prime-difference Sidon extremal question** | Classical Sidon bounds; Sidon ruler and forbidden-difference work | No |
| P007 | **Known** for full gracefulness; **unverified** for maximum distinct gap count | **Panma–Rochanakul (2021), Thm. 2.1** | Yes, full-graceful iff $n\le5$; not the extremal formula |
| P008 | Specific arithmetic centering **unverified**; proposed threshold/window proofs need external audit | Gupta–Lee–Li (2021), Penrose (2018), Hladký–Viswanathan (2026), Qi (2026) | No direct arithmetic centering formula found |

"Not found settled" means **the audit did not discover a settling source**, not that an open status or originality has been verified.

---

## P001 — Bounded deficit in distinct prime pair sums

**Exact problem.** In prime-sum perfect matchings of $[2n]$, maximize the number of distinct prime values used. Ask whether all but $O(1)$ prime sums in the available interval can be realized.

**Primary historical source.** Lawrence E. Greenfield and Stephen J. Greenfield, *Some Problems of Combinatorial Number Theory Related to Bertrand's Postulate*, *Journal of Integer Sequences* **1** (1998), Article 98.1.2: https://cs.uwaterloo.ca/journals/JIS/green.html. They prove the classical prime-pairing property and formulate additional generalizations. The paper predates our problem by nearly three decades; prime-sum pairing is **not our invention**.

**Computational enumeration.** OEIS [A000341](https://oeis.org/A000341) counts all prime-sum perfect matchings and cites Greenfield–Greenfield. The quantity counted there is **not** our maximum number of distinct sum values.

**Another literature axis.** A prime sum is an edge color; each color class is itself a matching since $a+b=p$ determines the partner uniquely. P001 is a *maximum number of colors represented by one perfect matching*, i.e., a maximum-color/multicolored matching problem rather than necessarily a fully rainbow perfect matching. General rainbow matching and colored spanning-structure work, such as Lang, *On sufficient conditions for spanning structures in dense graphs*, *Proc. London Math. Soc.* (2023), https://doi.org/10.1112/plms.12552, supplies relevant techniques but no located theorem settling this arithmetic instance.

**Assessment:** strong old foundations; exact bounded deficit not located. Must explicitly cite the 1998 paper and compare proper edge-colored matching theorems. Numerical deficit claims in earlier exploratory sessions require separately archived reproducible optimization certificates.

## P002 — Connectivity of prime-sum perfect matchings under four-cycle flips

**Exact problem.** Let $P_{2n}$ join distinct integers whose sum is prime. Are all its perfect matchings connected by alternating-four-cycle switches?

**Most important general source.** Martin Dyer, Mark Jerrum and Haiko Müller, *On the switch Markov chain for perfect matchings*, SODA 2016 / later journal treatment, https://doi.org/10.1137/1.9781611974331, and author manuscript https://eprints.whiterose.ac.uk/id/eprint/111478/1/monotone.pdf. Their work studies irreducibility/ergodicity and mixing of **exactly this local operation**. The largest **hereditary class** of bipartite graphs on which every switch chain is irreducible is chordal bipartite; this does **not** mean every non-chordal-bipartite graph has disconnected matching space.

**Other key source.** Bonamy, Bousquet, Heinrich, Ito, Kobayashi, Mary, Mühlenthaler and Wasa, *The Perfect Matching Reconfiguration Problem*, MFCS 2019, https://doi.org/10.4230/LIPIcs.MFCS.2019.80, establishes both hard instances and tractable graph classes.

**Specific host graph.** Croot and Jin, *Prime Sum Graphs and the Induced Trees They Contain*, *Graphs and Combinatorics* 42 (2026), https://doi.org/10.1007/s00373-025-02999-2; Chen, Fu and Guo, *Hamiltonicity in Prime Sum Graphs*, *Graphs and Combinatorics* 37 (2021), https://doi.org/10.1007/s00373-020-02241-1. These study the **same arithmetic graph** but not this matching flip connectivity question in their identified statements.

**Assessment:** not new as a reconfiguration *operation*; an arithmetic specialization potentially remains distinctive. Need determine whether the prime-sum graph belongs to an established sufficient class or has a bespoke canonical matching argument.

## P003 — Maximum edge-disjoint prime-sum perfect-matching packing

**Exact problem.** Is the number of edge-disjoint perfect matchings of $P_{2n}$ always its minimum degree $\delta(P_{2n})$?

**Old and new context.** Greenfield–Greenfield (1998), https://cs.uwaterloo.ca/journals/JIS/green.html, establish basic existence. Chen–Fu–Guo (2021), https://doi.org/10.1007/s00373-020-02241-1, consider the harder/different issue of Hamilton cycles; their result constructs infinitely many Hamiltonian prime-sum graphs, **not** a full minimum-degree factor packing. Croot–Jin (2026), https://doi.org/10.1007/s00373-025-02999-2, study induced trees, not $k$-factors.

**Important near-overlap.** A MathOverflow discussion of prime-sum Hamiltonicity describes making **two edge-disjoint perfect matchings** from suitable prime congruence classes: https://mathoverflow.net/questions/241569/for-which-n-is-there-a-permutation-such-that-the-sum-of-any-two-adjacent-eleme. This gives constructive precedent, not the full $\delta$-packing conjecture.

**Classical exact reduction.** In a bipartite graph $G=(U,V,E)$, a $k$-regular spanning factor exists iff, for all $X\subseteq U$, $Y\subseteq V$,

$$
e(X,V\setminus Y)\ge k(|X|-|Y|).
$$

This follows from integral max-flow/min-cut and is **standard**, not a new result. An extremal proof must show these inequalities for the arithmetic host.

**Assessment:** exact saturation conjecture not found in cited source statements, but highly vulnerable to overlooked arithmetic cut obstructions; a complete counterexample search and exact-flow benchmarks should precede promotion.

## P004 — Sidon-set one-element exchange graph

**Exact problem.** On $k$-element Sidon subsets of $[N]$, connect two sets when one mark changes and the Sidon property remains true. Does connectivity hold uniformly up to $(1-\epsilon)\sqrt N$?

**Established equivalence.** Finite Sidon sets are precisely Golomb rulers after translation. See MathWorld, https://mathworld.wolfram.com/SidonSet.html, for the correspondence and classical extremal size.

**Very close operational predecessor.** Dotú and Van Hentenryck, *A Memetic Approach to Golomb Rulers* (2005), https://cs.brown.edu/research/pubs/pdfs/2005/Dotu-2005-SHE.pdf, use changing the value of **a single mark** as a local-search move. This is structurally identical to our primitive operation, but their algorithm can visit **infeasible intermediate rulers** and often fixes endpoints. It does **not** establish that the graph of *only valid* Sidon rulers with fixed ambient interval is connected.

**Other nearby work.** Carter, Hunter and O'Bryant, *On the diameter of finite Sidon sets*, *Acta Math. Hung.* 175 (2025), https://doi.org/10.1007/s10474-024-01499-8, study the **numerical span/diameter of a Sidon set**, not the graph-theoretic diameter of its local-move reconfiguration graph. Avoid conflating them.

**Assessment:** one-mark moves well established computationally; exact valid-state connectivity result not located. The elementary $k=O(N^{1/3})$ theorem in our entry is a plausible baseline but **not independently literature-certified novel**. Check reconfiguration of Golomb rulers and sparse-Sidon transition graphs under alternate terminology.

## P005 — Coprime permutation partner-swap connectivity

**Exact problem.** Perfect matchings in the bipartite graph on copies of $[n]$, edges $i\sim j$ iff $\gcd(i,j)=1$, connected under four-cycle partner swaps?

**Direct predecessors.** Carl Pomerance, *Coprime permutations*, 2022, https://arxiv.org/abs/2203.03085; Ashwin Sah and Mehtaab Sawhney, *Enumerating coprime permutations*, *Mathematika* (2022), https://doi.org/10.1112/mtk.12159. They study existence, structure and numbers of precisely these permutations. OEIS [A005326](https://oeis.org/A005326) lists their small-case counts. **None of these objects or counts is new.**

**Switch precedent.** Dyer–Jerrum–Müller (2016/17), https://eprints.whiterose.ac.uk/id/eprint/111478/1/monotone.pdf, and Bonamy et al. (2019), https://doi.org/10.4230/LIPIcs.MFCS.2019.80, investigate general matching switches. Their results warn against treating connectivity as automatic. In particular, induced 6-cycles show the coprime bipartite graph is **not** chordal bipartite, but this alone neither proves nor disproves global switch connectivity.

**Assessment:** strongest exact-number-theory/reconfiguration bridge among our candidates; direct switch-connectivity resolution not located. Check algebraic statistics of 0–1 matrices with structural zeros/Markov bases in addition to graph-theory searches.

## P006 — Sidon sets avoiding every prime difference

**Exact problem.** Determine $F_{\neg\mathbb P}(N)$, the maximum size of a Sidon subset of $[N]$ in which no *positive difference* equals a prime. Ask whether the leading constant can be 1.

**Standard extremal context.** Singer-type constructions give Sidon sets of size $(1-o(1))\sqrt N$; current refinements are covered by MathWorld, https://mathworld.wolfram.com/SidonSet.html. The precise recent upper bound in Carter–Hunter–O'Bryant (2025) is https://doi.org/10.1007/s10474-024-01499-8. These do **not** impose forbidden prime differences.

**Old-neighbor but not equivalence.** Erdős problems on disjoint difference sets of two Sidon sets (e.g. https://www.erdosproblems.com/42) ask for a second Sidon set with few difference collisions, not for *every* difference to avoid the primes. Standard additive large-sieve/forbidden-difference approaches could nevertheless apply.

**Important exact terminology:** "prime-difference-free Sidon set", "Sidon set with composite positive differences", "Golomb ruler avoiding prime lengths", and "Sidon set excluding prime distances" should all be searched. Targeted searches returned no directly matching theorem or asymptotic formula, which is **not** affirmative evidence of novelty.

**Assessment:** possible original extremal hybrid, but the current asymptotic $1/\sqrt2$ lower bound is a simple dilation of classical Sidon sets, not claimed new. Investigate whether there is a cheap residue-class improvement or sieve-based upper bound before investing heavily.

## P007 — Maximum distinct differences in a coprime Hamiltonian path

**Definitive partial prior-art collision.**

Panma and Rochanakul, *Prime-Graceful Graphs*, *Thai Journal of Mathematics* 19(4), 1685–1697 (2021), https://thaijmath.com/index.php/thaijmath/article/view/1264, **Theorem 2.1**: the path $P_n$ has a prime-graceful labeling **if and only if $n\le5$**. Their definition requires precisely the labels $[n]$, coprimality on every path edge, and *all* edge differences distinct. Thus our "graceful coprime permutation exists iff $n\le5$" proof simply rederives a known theorem. This **must never be presented as an original result**.

**Distinguish related positive results carefully.** The same paper discusses "2-prime-graceful" labeling of paths, where the **allowed label range is enlarged**. It is not a contradiction that a path is 2-prime-graceful while it fails to be prime-graceful for $n\ge6$.

**Other related lines.** Francesco Monopoli, *Absolute Differences Along Hamiltonian Paths*, *Electronic Journal of Combinatorics* 22(3) (2015), https://doi.org/10.37236/5159, proves graceful Hamiltonian paths in complete graphs (without the coprime restriction). Gallian's *Dynamic Survey of Graph Labeling*, https://www.combinatorics.org/files/Surveys/ds6/ds6v24-2021.pdf, is crucial to detect synonymous variants.

**Remaining possible candidate:** Is the **maximum number of distinct** differences on such a coprime path equal to $\min(n-1,\lfloor(n+3)/2\rfloor)$ for every $n$? The 2021 exact iff theorem does not settle this extremal optimization, but the parameter should be searched using "partial prime-graceful", "maximum distinct edge labels", "deficiency" and "prime-graceful paths". **Originality confidence downgraded.**

## P008 — Connectivity of independently thinned coprime graphs; fine arithmetic centering

**Host and model.** The deterministic coprime graph is classical; MathWorld https://mathworld.wolfram.com/CoprimeGraph.html supplies older references. Xiang Qi, *Random Meta-Structure: A Random Graph Model Based on Abstract Binary Relations* (2026 preprint), https://doi.org/10.5281/zenodo.21737868, explicitly discusses independently retaining edges of the coprime host. **The random model itself is not novel.**

**Most important previously missing general theory:**

- Gupta, Lee and Li, *The Connectivity Threshold for Dense Graphs*, SODA 2021, in https://epubs.siam.org/doi/book/10.1137/1.9781611976465, explicitly studies **independent bond percolation on an arbitrary fixed host graph**, with thresholds described via approximate mincuts. This is directly relevant to our mechanism, though its abstract does **not** state the exact $e^\gamma$ arithmetic constant or the Poisson/Gumbel window.
- Penrose, *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, *Journal of Applied Probability* 55 (2018), https://doi.org/10.1017/jpr.2018.9, supplies general Poisson techniques for isolated vertices of inhomogeneous random graphs.
- Hladký and Viswanathan, *Connectivity of Inhomogeneous Random Graphs II*, *Random Structures & Algorithms* 69 (2026), https://doi.org/10.1002/rsa.70098, proves abstract connectivity criteria and studies the low-degree graphon profile; its sampled-vertex graphon framework is **not automatically identical** to our deterministic $[n]$ arithmetic host with $n$-dependent edge thinning.
- Martineau, *On coprime percolation, the visibility graphon, and the local limit of the GCD profile*, *Electronic Communications in Probability* 27 (2022), https://doi.org/10.1214/21-ECP381. Despite the very suggestive title, its "coprime percolation" is **a lattice gcd coloring and visibility graphon**, not the same independent edge-retention connectivity problem. It should be cited as arithmetic geometric context, not as exact prior resolution.

**Status of our internally supplied proofs.** Our P008 contains an internally derived leading-order threshold $e^\gamma\log n\log\log n/n$, Poisson isolated-vertex limit, and Gumbel window when centered by $\mu_n(b_n)=1$. The generic architecture—isolates, factorial moments, cuts—is well established. An **independent mathematical audit** and review of whether Gupta–Lee–Li or other general results subsume the argument are needed before any publication or priority claim.

**Remaining centering task is not yet a crisp yes/no conjecture.** As currently worded, "find an explicit formula for $b_n$" requires a precise admissible class of expressions and an error target, otherwise the exact implicit equation $\mu_n(b_n)=1$ itself already defines $b_n$. A meaningful task is to derive a specified elementary/logarithmic asymptotic approximation $B(n)$ satisfying

$$
b_n-B(n)=o(\log\log n/n).
$$

Before claiming openness, define the desired finite expansion class (e.g. explicit combinations of iterated logarithms with universal coefficients), and rule out tautological restatements of the exact degree sum.

**Assessment:** highest potential analytic significance, but highest burden of novelty and proof audit. The **model** is known, the **general mechanism** is known, and only the arithmetic specialisation/fine evaluation might offer novelty.

---

## Cross-problem conclusions and actions

1. **Source attribution is mandatory**: P007's iff theorem was already published in 2021; P001–P003 arise from the 1998 combinatorial Bertrand literature; P002/P005 use established switching theory.
2. **Prioritise credible exact novelty:** P005 and P006 appear most worth a separate specialized literature audit; P001 and P003 have clear arithmetic structure but need counterexample/expansion audits; P008 needs a full external probability-theory audit before any announcement.
3. **No false certification:** As of this pass, **none of the eight full candidate questions is certified as previously unknown and unresolved** by a comprehensive scholarly search. P007's full-graceful subproblem is **positively known to be resolved**.
4. **External follow-up:** search MathSciNet/zbMATH with MSC 05C70, 05C78, 05C80, 11B13, 11B30; ask a graph-labeling specialist about P007, a matching reconfiguration specialist about P002/P005, and a probabilistic combinatorialist about P008.

### Database provenance

This audit was performed 2026-10-28 from publicly accessible scholarly sources, with primary publisher pages preferred. Publication dates are taken from journal records; no private database access or specialist peer-review has been claimed.
