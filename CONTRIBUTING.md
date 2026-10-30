# Contributing to Meta Erdős

**Contributions are welcome.** Meta Erdős is a public mathematical research catalogue. Its 25 existing entries span open candidates, questions needing reformulation, and proved results. Contributions can propose additional questions, refine existing statements, give proofs or counterexamples, supply verifiable computations, and correct bibliographic claims.

The catalogue is independent of the official Erdős Problems collection. Inclusion does not imply that a problem was posed by Erdős, is historically novel, or is known to be open.

## Proposing a problem

Open an issue or pull request describing the mathematical question and how it differs from the closest known work. New identifiers are assigned consecutively during review; **the current count of 25 is not a cap on contributions**.

A useful submission includes:

1. **A precise statement:** definitions, ranges, quantifiers, boundary cases and an unambiguous conjecture or question.
2. **Mathematical motivation:** why an answer would clarify a structural phenomenon or connect established fields.
3. **Prior art:** primary citations and a precise account of what their theorems already settle. Search equivalent terminology, not only the proposed title.
4. **Evidence and falsification:** rigorous partial results, counterexamples, computational experiments, or clear explanations of what has not been checked.
5. **Reproducibility:** code, instructions, mathematical certificates and solver status where applicable. Finite tests must not be reported as general proofs.

Use [the problem template](PROBLEM_TEMPLATE.md) for a full dossier. Research notes and failed approaches are welcome when they sharpen the surviving question.

## Improving an existing entry

Refer to its permanent ID and identify the assertion being modified. Separate a new proof from an experimental observation and a historical correction. Preserve attribution when the same result is known in published work. When a question is resolved, update its **status and literature context**, rather than deleting the entry or presenting it as still open.

The catalogue uses these research statuses:

| Status | Meaning |
|---|---|
| `candidate` | A formulated question still under investigation, without certified novelty or unresolved status |
| `reframe` | A close predecessor or formulation issue requires the remaining question to be isolated |
| `needs specification` | A research objective without a sufficiently precise mathematical statement |
| `proved internally` | A written proof is available in the repository; external refereeing and historical priority are separate |

The `novelty` field records the scope of literature checking, **not** an originality certificate.

## Updating the catalogue

`data/problems.json` is the canonical index. Edit it and the relevant problem dossier, then regenerate the derived views:

```bash
python scripts/generate_catalog.py
python scripts/generate_catalog.py --check
python -m unittest discover -s tests -v

```

Do not hand-edit the generated table in `README.md`, the copy in `docs/problems.json`, or the generated summaries in the problem dossiers.

A pull request should state the mathematical change, evidence and known limitations. Automated checks establish repository consistency; they do not certify a conjecture or independently referee a proof.

## Mathematical Markdown

Use GitHub-compatible MathJax notation: single dollar signs for inline mathematics and double dollar signs on separate lines for display mathematics, with blank lines surrounding each display. Avoid raw hash characters in mathematical expressions and ensure LaTeX commands are compatible with the repository's rendering checks.

```markdown
Let $d_n(v)$ denote the degree of vertex $v$.

$$
\mu_n(p)=\sum_{v=1}^n(1-p)^{d_n(v)}.
$$

```

The repository's Markdown tests check syntax, local links and the integrity of the submitted P010 manuscript. See [GitHub's mathematical expression guide](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions).
## Public mathematical exposition

This repository is written **for mathematicians and independent readers**, not as a transcript of a research conversation. Every contribution should be self-contained and impersonal: state definitions, hypotheses, propositions, proofs, computational methods, counterexamples, and precise references. Distinguish proved claims, finite evidence, heuristic reasoning, and open questions. Describe authorship and assistance accurately when disclosure is required, without informal references to an interlocutor.

Avoid reader-directed or conversation-dependent phrases such as “as requested,” “you asked,” “our previous discussion,” “the user supplied,” or editorial notes addressed to an assistant. Historical audit documents may describe a research sequence, but should use archival terms such as “the submitted manuscript,” “the audit,” “the repository,” and “the earlier construction.” Keep the names *The Acorns* and *The Seedbed* for navigation; mathematical status and consequence assessments must remain explicit and neutral. Do not silently rewrite primary references or the factual AI-use disclosure in the submitted P010 materials.
