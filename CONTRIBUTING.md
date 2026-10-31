# Contributions

Meta Erdős is an open collection of mathematical problems and results. Contributions may consist of new questions, proofs, counterexamples, computations, or corrections to existing statements and references. A permanent identifier distinguishes each problem; the complete index is maintained in [`data/problems.json`](data/problems.json).

## Problem statements

A proposed problem should contain:

1. A precise formulation, including definitions, quantifiers, parameter ranges, and exceptional cases.
2. Its mathematical context, with references to the closest established results and an explanation of the distinction.
3. Any known partial results or obstructions, with proofs or exact citations.
4. Computational evidence, when relevant, with sufficient information for reproduction.

A negative literature search is not evidence that a problem is new. The status of a claim depends on its proof and its relation to prior work, not on its placement in the catalogue.

The [problem template](PROBLEM_TEMPLATE.md) specifies the customary organization of a dossier. Proposals and corrections may be submitted by issue or pull request. Identifiers are assigned consecutively.

## Mathematical status

| Status | Interpretation |
|---|---|
| `candidate` | A stated question for which no resolution is recorded in the catalogue |
| `reframe` | A formulation requiring restriction in view of an established result or equivalent question |
| `needs specification` | An objective whose mathematical statement is incomplete |
| `proved internally` | A proof supplied in the repository; independent verification and historical priority are separate questions |

The research collections [The Acorns](README.md#the-acorns) and [The Seedbed](README.md#the-seedbed) are editorial classifications. [The Harvest](README.md#the-harvest--internally-resolved-results) contains resolved entries. These classifications do not certify priority.

## Sources and computation

References should identify the relevant theorem, not merely a related subject. Earlier proofs retain their attribution. Computational claims should state the parameters, algorithm, exact or numerical arithmetic, and any applicable solver tolerances. A finite calculation does not establish an asymptotic assertion.

For mathematical notation, use GitHub-compatible MathJax: `$...$` inline and `$$` on separate lines for displays.

## Repository files

The canonical problem metadata and research collection assignments are [`data/problems.json`](data/problems.json) and [`data/curation.json`](data/curation.json). Problem dossiers are under [`problems/`](problems/), proofs under [`theorems/`](theorems/), numerical material under [`experiments/`](experiments/), and literature comparisons under [`literature-audits/`](literature-audits/).

Derived tables and summaries are generated rather than edited individually:

```bash
python scripts/generate_catalog.py
python scripts/generate_catalog.py --check
python -m unittest discover -s tests -v
```

The source of a submitted manuscript is distinct from later repository commentary. Its bibliographic record and disclosure statements remain attached to that version.
