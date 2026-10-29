# Meta Erdős

**An independent notebook of sixteen research entries in number theory, graph theory and probability, inspired by the problem-posing tradition of Paul Erdős.**

**Important:** These are **not** problems claimed to have been posed by Erdős, not part of [erdosproblems.com](https://www.erdosproblems.com/), and not certified to be new or unresolved. Our collection is independent of [teorth/erdosproblems](https://github.com/teorth/erdosproblems). We draw inspiration from that repository's clear, data-driven organization—not its problem content.

**Explore:** [Problem catalogue below](#problem-catalogue) · [Interactive searchable browser](docs/index.html) · [Research audits](#evidence-and-prior-art) · [How to contribute](CONTRIBUTING.md)

> **Research strategy (29 October 2026):** P001–P010 are consolidated; P011–P016 inaugurate a **problem-discovery phase**. The goal is to formulate, challenge and source-audit structurally consequential questions **before** attempting general proofs.

## Problem catalogue

Every problem has a permanent identifier, its own self-contained statement, evidence, and nearest prior art. *Candidate* means **under investigation**, not "verified open".

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
<!-- CATALOG:END -->

For precise definitions, follow each ID. To filter by subject, status or title in a browser, open [the searchable catalogue](docs/index.html). If GitHub Pages is enabled for the repository's `docs/` folder, the same page can be published as a standalone website.

## How to interpret the labels

| Label | Meaning |
|---|---|
| **candidate** | A precise mathematical question, but not certified original or unresolved |
| **proved internally** | Complete argument supplied in this repository; independently verified correctness and originality are **not** yet certified |
| **reframe** | Some original formulation is known or misleading; the surviving question must be isolated |
| **needs specification** | The research goal is meaningful, but its current statement is not a fully formal yes/no question |
| **not certified** | No exhaustive prior-art check or independent specialist certification |
| **apparent novelty (targeted audit)** | An exact prior answer was not located in a dated targeted search; no assertion of genuine novelty or open status |
| **strong prior-art overlap** | A closely connected classical conjecture or sufficient condition is already known |
| **needs precise formulation** | The remaining claimed open question has not yet been made mathematically sharp |
| **internal proof; priority unverified** | A proof exists within this project, but the originality and priority are not certified |
| **known subproblem** | A specific subclaim is already established in earlier literature |
| **closely related** | Strong connection to an older question; independence is not settled |

An *internal proof* is not a published or externally verified theorem. Likewise, exact computations apply only to the stated finite instances.

## Mathematical progress

**P010 has an internally complete exact solution:** for every $n\ge4$,

$$
h(n)=\pi(n)-\pi(n/2)+\max\!\left(1,\left\lceil\frac{\pi(n/2)-\pi(n/3)}2\right\rceil\right).
$$

See the [constructive theorem](theorems/P010-exact-coprime-adjacencies.md) and [dependency-free verification program](experiments/P010_construct_optimal_permutation.py). This resolves the original P010 extremal question **within this research notebook**. A historical priority and external referee audit are still required before claiming a new published mathematical result.

## New unnumbered theorem: interval-sum factor saturation

Every bipartite graph on two copies of `{0,…,n−1}` with allowed edges satisfying `a ≤ i+j ≤ b` admits as many edge-disjoint perfect matchings as its minimum degree. The [full constructive proof](theorems/interval-sum-factor-saturation.md) and [dependency-free verification program](experiments/interval_sum_factor_construct.py) are available. This **resolves an incubator question**, not P003; no new problem identifier is added, and historical novelty remains unverified.

## Research generation and novelty tiers

- **Apparent novelty (targeted audit)** means that the listed searches have not located an exact equivalent or resolution. It **does not mean** proven new, independently verified open or original as a mathematical object.
- The newly added P011–P013 are first-stage research questions. None has a claimed asymptotic theorem, formal novelty certification, or prize attribution.
- **Structural impact takes priority over incremental computation:** ask questions whose answers would explain mechanisms, classify mathematical structures or distinguish universality classes.

Read the [29 October novelty and new-directions audit](literature-audits/2026-10-29-novelty-and-new-directions.md) for the explicit predecessor matrix and caveats.

## Recent mathematical progress and proposed discoveries

- **P010:** [Publication significance and priority audit](audits/2026-10-29-P010-publishability-priority-review.md) — exact theorem appears suitable for a short paper **if novel**, but no human referee or definitive priority certification yet.
- **P015:** [Odd-area convex lattice triangulations](problems/geometry/P015-odd-area-lattice-triangulations.md) — geometric parity becomes four fixed vertex colors; ask if all valid triangulations connect by valid diagonal flips. [Research audit](literature-audits/2026-10-29-P015-geometry-and-P010-priority.md).

## New topological research question

- [P016 — Topology of the Sidon simplicial complex](problems/topology/P016-sidon-complex-homology.md) asks whether the reduced homology of arithmetic constraint complexes eventually vanishes in each fixed dimension. [First-pass originality audit](literature-audits/2026-10-29-P016-sidon-complex-topology.md). Exact finite Betti calculations are not an asymptotic proof.

## Evidence and prior art

- [P010 publication assessment, fresh P001–P009 references, and interval-sum factor incubator](audits/2026-10-28-P010-publication-and-novelty-followup.md) — journal-policy warnings and a new unpromoted candidate.
- [New exact P010 theorem and priority audit](audits/2026-10-28-P010-resolution-proof-and-novelty.md) — independent mathematical review still pending.
- [All-ten adversarial review](audits/2026-10-28-P001-P010-adversarial-review.md) — proof checks, reproductions, explicit gaps, and selection criteria.
- [Comprehensive P001–P008 literature review](literature-audits/2026-10-28-comprehensive-P001-P008.md) — close mathematical predecessors and one confirmed prior-art collision.
- [P009/P010 literature review](literature-audits/2026-10-28-pass-4.md) — prime differences and the earlier Erdős–Freud–Hegyvári work.
- [Current novelty and quality gate](audits/2026-10-28-novelty-quality-gate.md) — precise citations and retain/reframe priorities.
- [Experiments](experiments/) — code for finite optimization, enumeration and random-graph simulations. See [dependencies](requirements-experiments.txt).

## How this repository works

```text
data/problems.json               Canonical index and status data
problems/                        Ten mathematical problem dossiers
experiments/                     Computational tests and witnesses
theorems/                        Full proof dossiers for internally resolved questions
audits/                          Proof, numerical, and novelty reviews
literature-audits/               Dated source-by-source literature surveys
docs/                            Optional searchable static catalogue
scripts/                          Generate and validate the index
tests/                           Dependency-free index checks
research-notes/                  Explored and rejected questions
```

The table above and `docs/problems.json` are **generated views** of `data/problems.json`. After changing metadata, run:

```bash
python scripts/generate_catalog.py
python -m unittest discover -s tests -v
```

Use `python scripts/generate_catalog.py --check` to verify that all generated views are current.

## Submission and credit

See [CONTRIBUTING.md](CONTRIBUTING.md) and the [problem dossier template](PROBLEM_TEMPLATE.md). Every mathematical addition should disclose its proof status, attempts at disproof, computational methodology, the *closest* previously published result, and a dated novelty assessment. Known theorems must credit their earlier authors; "not found" is never treated as "new".

This is a **research notebook**, not a prize list, journal, or official Erdős problem database.
