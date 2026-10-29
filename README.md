# Meta Erdős

**Meta Erdős is an open, community-contributable catalogue of mathematical research questions, conjectures and partial results.** The collection currently contains **30 numbered research entries (P001–P030)** in number theory, graph theory, probability, geometry, topology and matroid theory.

The project takes inspiration from Paul Erdős's problem-posing tradition. These entries are **not claimed to have been posed by Erdős**, do not belong to [erdosproblems.com](https://www.erdosproblems.com/) or [teorth/erdosproblems](https://github.com/teorth/erdosproblems), and are **not certified to be previously unknown or unresolved**. Established results and close predecessors are attributed in the individual dossiers.

**Browse:** [Catalogue](#problem-catalogue) · [Searchable browser](docs/index.html) · [Mathematical results](#mathematical-results) · [Literature and audits](#literature-and-audits) · [Contribute](CONTRIBUTING.md)

## Status and scope

The 30 entries have different research statuses; **they are not all open conjectures**.

The [29 October 2026 portfolio-wide audit](audits/2026-10-29-P001-P020-first-collection-consolidation.md) and the [second-pass source-level comparison, including the P010 manuscript snapshot](audits/2026-10-29-P015-P016-P018-P020-source-comparison-and-P010-snapshot.md) reviews **all twenty IDs** for well-posedness, closest prior art, structural significance, evidence quality and potential overlap. It gives a provisional shortlist of **P003, P005, P014, P016, P017, P018 and P020**, with **P010 on a separate theorem/publication track**. These are **editorial priorities, not certified novel/open problems**.
| Status | Entries | Meaning |
|---|---|---|
| Candidate | 26 | A mathematical research question under investigation; historical novelty and unresolved status are not certified |
| Reframe | 2 (P007, P025) | A close or known predecessor requires the surviving question to be stated more narrowly |
| Needs specification | 1 (P008) | The intended mathematical question requires a sharper formal statement |
| Proved internally | 1 (P010) | A complete proof is supplied; independent refereeing and historical priority assessment are distinct matters |

These labels distinguish the research status of a *question* from the historical novelty of its formulation. Computations only certify the finite instances and methods specified in their dossiers.

Among the earlier research candidates, **P005, P017, P018 and P020** are leading directions, with **P003 and P016** as additional subjects of interest. The newer P026–P030 questions remain candidates pending fuller historical review; the P027 exchange-graph diameter is already proved internally, whereas its mixing question is open. These are not rankings of mathematical priority or claims of external validation.

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

**Interval-sum factor saturation.** A separate [constructive theorem](theorems/interval-sum-factor-saturation.md) proves that a bipartite graph with allowed sum interval $a\le i+j\le b$ contains as many edge-disjoint perfect matchings as its minimum degree. This is not claimed as a resolution of P003 and does not have a numbered open-problem entry.

## Second consolidation pass — primary sources and submission provenance

- [P010 manuscript snapshot and reference verification](manuscripts/P010-2026-10-29-submission-snapshot-and-policy-audit.md): records the author-supplied **two-page PDF's** exact SHA-256 and bibliography checks. **Important:** the current official *INTEGERS* policy appears to exclude research developed with AI assistance in mathematics/code, as transparently disclosed in that manuscript. The PDF binary is not included in this repository change.
- [P008/P015/P018/P020 source-and-obstruction review](audits/2026-10-29-P008-P015-P018-P020-source-obstruction-pass.md): cautious distinctions from the closest colored-triangulation, group-labeled-matroid, random-matrix and host-percolation literature; independent validation of P018's exact three-exchange bridge.

The **P001–P020 discovery freeze remains active**. These updates neither certify historical originality nor alter the mathematical status of any numbered problem.

## Additional arithmetic and combinatorial research

The newest dossiers examine **four-cycle generation in prime-sum graphs** ([P026](problems/graph-theory/P026-prime-sum-square-cycle-generation.md)), **random walks on maximum primitive sets** ([P027](problems/number-theory/P027-primitive-set-exchange-mixing.md)), **random divisibility-complex Euler characteristics** ([P028](problems/number-theory/P028-random-divisor-complex-mobius-deformation.md)), **prime-sum permutation X-ray fibers** ([P029](problems/graph-theory/P029-prime-sum-permutation-xray-fibers.md)) and **simultaneous prime-sum/prime-difference matchings** ([P030](problems/number-theory/P030-double-prime-perfect-matchings.md)).

An [exact primitive-set exchange theorem](theorems/P027-primitive-set-exchange-diameter.md) establishes a Hamming graph metric and diameter $5n/12+O(1)$ on maximum primitive subsets of $[2n]$; its historical novelty has not been certified. Every new question has explicit predecessor citations and finite or theoretical baseline evidence. In particular, P029 reuses the previously studied discrete-tomography *X-ray* object rather than claiming to invent it.

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
<!-- CATALOG:END -->

Browse and filter the same entries in the [searchable catalogue](docs/index.html).

## Literature and audits

Historical source reviews and mathematical audits are preserved for transparency. They are **research records rather than continuously updated statements of priority**; consult the individual dossier and its references for the claims currently attached to a question.

- [Catalogue-wide literature comparison, P001–P025](audits/2026-10-29-P001-P025-literature-source-gate.md)
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