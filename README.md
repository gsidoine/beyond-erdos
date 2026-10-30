# Meta Erdős

<p align="center">
  <img src="assets/erdos-portrait.jpg" alt="Paul Erdős" width="420">
</p>

<p align="center"><em>Paul Erdős</em></p>

**Meta Erdős is an open, community-contributable catalogue of mathematical research questions, conjectures and partial results.** The collection currently contains **33 numbered research entries (P001–P033)** in number theory, graph theory, probability, geometry, topology and matroid theory.

The project takes inspiration from Paul Erdős's problem-posing tradition. These entries are **not claimed to have been posed by Erdős**, do not belong to [erdosproblems.com](https://www.erdosproblems.com/) or [teorth/erdosproblems](https://github.com/teorth/erdosproblems), and are **not certified to be previously unknown or unresolved**. Established results and close predecessors are attributed in the individual dossiers.

**Browse:** [Catalogue](#problem-catalogue) · [Searchable browser](docs/index.html) · [Mathematical results](#mathematical-results) · [Literature and audits](#literature-and-audits) · [Contribute](CONTRIBUTING.md)

## Status and scope

The 33 entries have different research statuses; **they are not all open conjectures**.

| Status | Entries | Meaning |
|---|---|---|
| Candidate | 29 | A mathematical research question under investigation; historical novelty and unresolved status are not certified |
| Reframe | 2 (P007, P025) | A close or known predecessor requires the surviving question to be stated more narrowly |
| Needs specification | 1 (P008) | The intended mathematical question requires a sharper formal statement |
| Proved internally | 1 (P010) | A complete proof is supplied; independent refereeing and historical priority assessment are distinct matters |

These labels distinguish the research status of a *question* from the historical novelty of its formulation. Computations only certify the finite instances and methods specified in their dossiers.

The [consolidated P001–P030 research portfolio](audits/portfolio-consolidation-P001-P030.md) groups the questions into five mathematical programs and distinguishes publication-ready proofs from provisional candidate questions. **P003, P005, P017, P018, P020 and P027** are the current theorem-building priorities; this is an editorial research focus, **not** a certification of novelty or openness. Contributions and newly proposed IDs remain welcome.

**Contributions are welcome**, including new problem proposals, counterexamples, proof improvements, bibliographic corrections and reproducible experiments. New IDs are assigned through review rather than an arbitrary numerical target; see [CONTRIBUTING.md](CONTRIBUTING.md).

## P010 — Submitted manuscript

The original P010 question, **the minimum number of coprime adjacencies in a permutation**, has a complete constructive proof in this repository. The resulting manuscript, *The Minimum Number of Coprime Adjacencies in a Permutation*, **has been submitted to the journal _Integers_**. Submission does **not** imply acceptance or publication.

- [Submitted manuscript (PDF)](manuscripts/P010/coprime_adjacencies.pdf)
- [Manuscript information](manuscripts/P010/README.md)
- [P010 problem dossier](problems/graph-theory/P010-minimum-coprime-adjacencies.md)
- [Constructive proof and supporting argument](theorems/P010-exact-coprime-adjacencies.md)

For $n\ge4$, the established formula in the manuscript is

$$
h(n)=\pi(n)-\pi(n/2)+
\max\{1,\lceil(\pi(n/2)-\pi(n/3))/2\rceil\}.
$$

In particular, $h(n)\sim 7n/(12\log n)$. This is a **resolved entry**, not one of the currently open candidates. Any claim of historical originality remains subject to specialist comparison.

## Mathematical results

**P020 — Random $p$-adic Hankel cokernels.** The repository contains internal proofs of exact laws for cyclic and two-generator cokernels, plus every elementary abelian cokernel, with finite modular checks. The higher-exponent group distribution and the full limiting law remain unresolved. The finite-field kernel classification used in these proofs is explicitly credited to earlier literature.

- [P020 problem dossier](problems/number-theory/P020-random-hankel-padic-cokernels.md)
- [Cyclic and two-generator results](theorems/P020-padic-hankel-cyclic-and-rank-two-laws.md)
- [Elementary abelian group probabilities](theorems/P020-elementary-abelian-cokernel-laws.md)
- [Finite-field kernel structure and prior art](theorems/P020-hankel-kernel-product-research.md)

**P033 — Three prime-sum colors.** An [unconditional eventual-connectivity theorem](theorems/P033-eventual-three-prime-sum-connectivity.md) proves that three prime sums connect $[n]$ for **every sufficiently large $n$**, using an elementary graph lemma and Siegel–Walfisz. Combined with the previously proved two-color/twin-prime criterion, this implies $\kappa(n)=3$ for a density-one set of integers $n$. **The full all-$n$ conjecture remains unresolved**, because the analytic threshold is ineffective. Historical originality is not certified. [P033 dossier](problems/graph-theory/P033-prime-sum-three-palette.md).

**Interval-sum factor saturation.** A separate [constructive theorem](theorems/interval-sum-factor-saturation.md) proves that a bipartite graph with allowed sum interval $a\le i+j\le b$ contains as many edge-disjoint perfect matchings as its minimum degree. This is not claimed as a resolution of P003 and does not have a numbered open-problem entry.

## Research portfolio and source verification

The [P001–P030 consolidation](audits/portfolio-consolidation-P001-P030.md) provides a dossier-by-dossier evidence matrix, identifies shared host graphs and nonredundant observables, records close published predecessors, and prioritizes testable theorem targets. Older literature and proof reviews remain accessible as [historical research records](audits/README.md), not as the current source of catalogue status.

The submitted [P010 PDF](manuscripts/P010/coprime_adjacencies.pdf) is in this repository. *Integers* [permits supporting AI-tool use subject to its authorial-writing, accuracy and disclosure requirements](https://math.colgate.edu/~integers/submit.html); the manuscript includes an AI-use statement. Its exact eligibility and editorial outcome are for the journal to determine. Submission does **not** establish acceptance or publication.


## Arithmetic and combinatorial extensions

Several additional dossiers examine **four-cycle generation in prime-sum graphs** ([P026](problems/graph-theory/P026-prime-sum-square-cycle-generation.md)), **random walks on maximum primitive sets** ([P027](problems/number-theory/P027-primitive-set-exchange-mixing.md)), **random divisibility-complex Euler characteristics** ([P028](problems/number-theory/P028-random-divisor-complex-mobius-deformation.md)), **prime-sum permutation X-ray fibers** ([P029](problems/graph-theory/P029-prime-sum-permutation-xray-fibers.md)) and **simultaneous prime-sum/prime-difference matchings** ([P030](problems/number-theory/P030-double-prime-perfect-matchings.md)).

An [exact primitive-set exchange theorem](theorems/P027-primitive-set-exchange-diameter.md) establishes a Hamming graph metric and diameter $5n/12+O(1)$ on maximum primitive subsets of $[2n]$; its historical novelty has not been certified. Every new question has explicit predecessor citations and finite or theoretical baseline evidence. In particular, P029 reuses the previously studied discrete-tomography *X-ray* object rather than claiming to invent it.

**P027 — Uniform sampling of maximum primitive sets.** The [arithmetic-block mixing theorem](theorems/P027-five-site-arithmetic-blocks-and-mixing-lower-bound.md) isolates linearly many independent **23-state five-coordinate factors** and proves a certified full-chain lower bound of $(363/202)n\log n-O(n)$. The same factorization yields linearly growing 23-adic divisibility of the maximum-primitive-set count. An earlier [autonomous-coordinate result](theorems/P027-autonomous-coordinate-hypercube-cutoff.md) gives independent binary factors and a spectral reduction. **Only the projections have proved cutoff**; full-chain mixing order remains open. [P027 dossier](problems/number-theory/P027-primitive-set-exchange-mixing.md).

## New questions at the arithmetic–combinatorial boundary

Three short research questions extend the collection: **[P031](problems/number-theory/P031-coprime-sidon-extremum.md)** asks how large a Sidon set can be while remaining pairwise coprime; **[P032](problems/graph-theory/P032-prime-sum-bipartite-diameter.md)** asks whether a two-copy prime-sum graph eventually has diameter seven; and **[P033](problems/graph-theory/P033-prime-sum-three-palette.md)** asks whether three prime sums always suffice to connect [n]. All are **candidate questions**, subject to external novelty and existing-theorem checks.

The [P027 finite-template theorem](theorems/P027-finite-arithmetic-template-transfer.md) proves that every fixed primitive-set configuration model occurs in linearly many isolated copies inside larger models. Their finite spectral gaps yield rigorous full-chain mixing lower bounds. **It remains open whether the local gaps approach zero**, which would imply super-n log n mixing. This is a conditional route, not a new full-chain mixing theorem.

## Problem catalogue

The table below is generated from [the canonical metadata](data/problems.json). Each entry links to its full mathematical formulation, known results, finite experiments, prior-art comparison and remaining questions.

<!-- CATALOG:START -->
| ID | Question | Area | Formulation | Novelty |
|---|---|---|---|---|
| [P001](problems/number-theory/P001-prime-spectrum.md) | Prime-spectrum saturation | number theory | candidate | apparent novelty (targeted audit) |
| [P002](problems/graph-theory/P002-prime-matching-reconfiguration.md) | Prime-sum matching reconfiguration | graph theory | candidate | apparent novelty (targeted audit) |
| [P003](problems/graph-theory/P003-prime-matching-packing.md) | Edge-disjoint prime-sum matchings | graph theory | candidate | apparent novelty (targeted audit) |
| [P004](problems/number-theory/P004-sidon-exchange-connectivity.md) | Sidon exchange connectivity | additive combinatorics | candidate | apparent novelty (targeted audit) |
| [P005](problems/graph-theory/P005-coprime-permutation-switches.md) | Coprime permutation switches | graph theory | candidate | apparent novelty (targeted audit) |
| [P006](problems/number-theory/P006-prime-avoiding-sidon-sets.md) | Sidon sets without prime differences | additive combinatorics | candidate | apparent novelty (targeted audit) |
| [P007](problems/graph-theory/P007-coprime-difference-spectrum.md) | Coprime path difference spectrum | graph labeling | reframe | known subproblem; extension unverified |
| [P008](problems/probability/P008-coprime-percolation-critical-window.md) | Arithmetic centering of coprime percolation | probability | needs specification | needs precise formulation |
| [P009](problems/number-theory/P009-two-prime-palette-pairings.md) | Two-prime palette pairings | number theory | candidate | strong prior-art overlap |
| [P010](problems/graph-theory/P010-minimum-coprime-adjacencies.md) | Minimum coprime adjacencies | graph theory | proved internally | internal proof; priority unverified |
| [P011](problems/probability/P011-random-sum-diagonal-matchings.md) | Random sum-diagonal matching transitions | probability | candidate | apparent novelty (targeted audit) |
| [P012](problems/probability/P012-coprime-matching-space-percolation.md) | Coprime matching-space percolation | probability | candidate | apparent novelty (targeted audit) |
| [P013](problems/probability/P013-random-sidon-reconfiguration.md) | Random-site Sidon exchange geometry | probability | candidate | apparent novelty (targeted audit) |
| [P014](problems/topology/P014-random-cayley-sum-flag-homology.md) | Homology of random Cayley sum flag complexes | probabilistic topology | candidate | apparent novelty (targeted audit) |
| [P015](problems/geometry/P015-odd-area-lattice-triangulations.md) | Odd-area lattice triangulation flip connectivity | discrete geometry | candidate | apparent novelty (targeted audit) |
| [P016](problems/topology/P016-sidon-complex-homology.md) | Topology of the Sidon simplicial complex | topological combinatorics | candidate | apparent novelty (targeted audit) |
| [P017](problems/probability/P017-random-divisibility-chain-height.md) | Random divisibility-poset chain height | probability | candidate | apparent novelty (targeted audit) |
| [P018](problems/matroid-theory/P018-conserved-xor-basis-fibers.md) | Conserved-XOR basis exchange fibers | matroid theory | candidate | apparent novelty (targeted audit) |
| [P019](problems/geometry/P019-no-three-line-exchange.md) | Exchange complexity of optimal no-three-in-line configurations | discrete geometry | candidate | apparent novelty (targeted audit) |
| [P020](problems/number-theory/P020-random-hankel-padic-cokernels.md) | Cokernel laws of random p-adic Hankel matrices | algebraic probability | candidate | apparent novelty (targeted audit) |
| [P021](problems/probability/P021-cayley-sum-sandpile-laws.md) | Random Cayley-sum sandpile groups | algebraic probability | candidate | not certified (targeted audit) |
| [P022](problems/geometry/P022-random-unimodular-triangle-complex.md) | Random unimodular triangle complex homology | discrete geometry | candidate | not certified (targeted audit) |
| [P023](problems/probability/P023-random-prime-incidence-rank.md) | Rank of random prime-divisibility incidence matrices | probabilistic number theory | candidate | not certified (targeted audit) |
| [P024](problems/graph-theory/P024-zero-forcing-divisor-graph.md) | Zero forcing on the divisor comparability graph | graph theory | candidate | not certified (targeted audit) |
| [P025](problems/number-theory/P025-lcm-hamiltonian-bottleneck.md) | Cyclic lcm Hamiltonian bottleneck | number theory | reframe | confirmed collision for linear-path analogue |
| [P026](problems/graph-theory/P026-prime-sum-square-cycle-generation.md) | Four-cycle generation in prime-sum bipartite graphs | graph theory | candidate | not certified (specialist source check needed) |
| [P027](problems/number-theory/P027-primitive-set-exchange-mixing.md) | Mixing of maximum primitive-set exchanges | multiplicative combinatorics | candidate | not certified; closely related to counting primitive sets and distributive-lattice walks |
| [P028](problems/number-theory/P028-random-divisor-complex-mobius-deformation.md) | Möbius deformation from random divisibility complexes | analytic number theory | candidate | not certified; arithmetic Dirichlet convolution and order-complex Möbius theory are classical |
| [P029](problems/graph-theory/P029-prime-sum-permutation-xray-fibers.md) | Prime-supported permutation X-ray fiber reconfiguration | combinatorics | candidate | high overlap risk with existing permutation X-ray/discrete tomography theory |
| [P030](problems/number-theory/P030-double-prime-perfect-matchings.md) | Double-prime perfect matchings on integer intervals | number theory | candidate | not certified; prime sum/difference cycles have explicit earlier study |
| [P031](problems/number-theory/P031-coprime-sidon-extremum.md) | How large can a pairwise-coprime Sidon set be? | number theory | candidate | not certified; Sidon sets of primes and additive-multiplicative restrictions require a specialist search |
| [P032](problems/graph-theory/P032-prime-sum-bipartite-diameter.md) | Is the prime-sum bipartite diameter eventually seven? | graph theory | candidate | strong prior-art overlap risk with interval-constrained prime differences and Erdős problem 17 |
| [P033](problems/graph-theory/P033-prime-sum-three-palette.md) | Can three prime sums connect all integers? | graph theory | candidate | not certified; two-prime case overlaps known twin-prime Hamiltonian-path constructions |
<!-- CATALOG:END -->

Browse and filter the same entries in the [searchable catalogue](docs/index.html).

## Literature and audits

Historical source reviews and mathematical audits are preserved for transparency. They are **research records rather than continuously updated statements of priority**; consult the individual dossier and its references for the claims currently attached to a question.

- [Current research portfolio and priority matrix, P001–P030](audits/portfolio-consolidation-P001-P030.md)
- [Historical literature comparison, P001–P025](audits/2026-10-29-P001-P025-literature-source-gate.md)
- [Focused review of the candidate research directions](audits/2026-10-29-flagship-source-comparison-and-shortlist.md)
- [Earlier consolidation, P001–P020](audits/2026-10-29-P001-P020-first-collection-consolidation.md)
- [Literature review archive](literature-audits/README.md)
- [Proof and research audit archive](audits/)

A missing exact source in a search is **not** proof that a question is new or open. A published theorem must be attributed to its authors even when a proof is independently rediscovered.

## Reproducibility and contributions

Problem definitions and references live in `problems/`; mathematical proof notes in `theorems/`; code and finite certificates in `experiments/`; and the canonical catalogue index in `data/problems.json`. Supporting research and literature reviews are preserved in `audits/` and `literature-audits/`.

To validate a contribution:

```bash
python scripts/generate_catalog.py
python scripts/generate_catalog.py --check
python -m unittest discover -s tests -v

```

Do not edit generated catalogue tables or dossier summary blocks directly: the generator synchronizes them from the metadata. See [the contribution guide](CONTRIBUTING.md) and [problem template](PROBLEM_TEMPLATE.md) for research standards, status categories, evidence and attribution.
