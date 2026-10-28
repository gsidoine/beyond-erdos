# Beyond Erdős

**An independent notebook of ten exploratory problems in number theory, graph theory and probability, inspired by the problem-posing tradition of Paul Erdős.**

**Important:** These are **not** problems claimed to have been posed by Erdős, not part of [erdosproblems.com](https://www.erdosproblems.com/), and not certified to be new or unresolved. Our collection is independent of [teorth/erdosproblems](https://github.com/teorth/erdosproblems). We draw inspiration from that repository's clear, data-driven organization—not its problem content.

**Explore:** [Problem catalogue below](#problem-catalogue) · [Interactive searchable browser](docs/index.html) · [Research audits](#evidence-and-prior-art) · [How to contribute](CONTRIBUTING.md)

> **Research freeze:** P001–P010. No new problem IDs will be added until proof, novelty, and problem-quality reviews are complete.

## Problem catalogue

Every problem has a permanent identifier, its own self-contained statement, evidence, and nearest prior art. *Candidate* means **under investigation**, not "verified open".

<!-- CATALOG:START -->
| ID | Question | Area | Formulation | Novelty |
|---|---|---|---|---|
| [P001](problems/number-theory/P001-prime-spectrum.md) | Prime-spectrum saturation | number theory | candidate | not certified |
| [P002](problems/graph-theory/P002-prime-matching-reconfiguration.md) | Prime-sum matching reconfiguration | graph theory | candidate | not certified |
| [P003](problems/graph-theory/P003-prime-matching-packing.md) | Edge-disjoint prime-sum matchings | graph theory | candidate | not certified |
| [P004](problems/number-theory/P004-sidon-exchange-connectivity.md) | Sidon exchange connectivity | additive combinatorics | candidate | not certified |
| [P005](problems/graph-theory/P005-coprime-permutation-switches.md) | Coprime permutation switches | graph theory | candidate | not certified |
| [P006](problems/number-theory/P006-prime-avoiding-sidon-sets.md) | Sidon sets without prime differences | additive combinatorics | candidate | not certified |
| [P007](problems/graph-theory/P007-coprime-difference-spectrum.md) | Coprime path difference spectrum | graph labeling | reframe | known subproblem |
| [P008](problems/probability/P008-coprime-percolation-critical-window.md) | Arithmetic centering of coprime percolation | probability | needs specification | not certified |
| [P009](problems/number-theory/P009-two-prime-palette-pairings.md) | Two-prime palette pairings | number theory | candidate | closely related |
| [P010](problems/graph-theory/P010-minimum-coprime-adjacencies.md) | Minimum coprime adjacencies | graph theory | candidate | not certified |
<!-- CATALOG:END -->

For precise definitions, follow each ID. To filter by subject, status or title in a browser, open [the searchable catalogue](docs/index.html). If GitHub Pages is enabled for the repository's `docs/` folder, the same page can be published as a standalone website.

## How to interpret the labels

| Label | Meaning |
|---|---|
| **candidate** | A precise mathematical question, but not certified original or unresolved |
| **reframe** | Some original formulation is known or misleading; the surviving question must be isolated |
| **needs specification** | The research goal is meaningful, but its current statement is not a fully formal yes/no question |
| **not certified** | No exhaustive prior-art check or independent specialist certification |
| **known subproblem** | A specific subclaim is already established in earlier literature |
| **closely related** | Strong connection to an older question; independence is not settled |

An *internal proof* is not a published or externally verified theorem. Likewise, exact computations apply only to the stated finite instances.

## Evidence and prior art

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
