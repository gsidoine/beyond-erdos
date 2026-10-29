# Contributing to Meta Erdős

This is a **curated exploratory research notebook**, not an official catalogue of Erdős problems and not a claim of original published open questions. The collection is currently **frozen at P001–P010**; do not introduce P011 until the audit gate is explicitly lifted.

## A change worth submitting

1. **Locate the closest work**: at least one primary source or explicit description of why none could be located. Search mathematical synonyms and equivalent formulations, not just the proposed title.
2. **State a precise result**: definitions, quantifiers, ranges, and exceptions; mark each assertion as a proved proposition, finite computation, heuristic, or open candidate.
3. **Challenge your own claim**: small counterexamples, invariants, reduction to a known theorem, and any failed proof attempts.
4. **Record evidence**: reproducible code or proof, environment/solver status, cases tested, finite limits. Integer-programming termination is "optimal" only with an optimal solver status.
5. **Write a dated audit entry**: citations with DOI or stable links, exact mathematical overlap, status decision, and outstanding questions.
6. **Update the canonical catalogue**: edit \`data/problems.json\` and run \`python scripts/generate_catalog.py\`, then \`python -m unittest discover -s tests -v\`. Do **not** hand-edit the generated table or \`docs/problems.json\`.

## Status policy

- **candidate** — mathematically stated but not certified novel/unresolved.
- **reframe** — a known theorem or ambiguous formulation forces a narrower question.
- **needs specification** — not yet a precise mathematical yes/no problem.
- **proved internally** — a complete written mathematical argument has been produced within this project, **not** independently refereed or certified novel; preserve original question and cite the proof.

The **novelty field** is separate. Never equate failure to find a source with evidence of originality. A confirmed earlier result must carry precise attribution in the dossier; for example, the full prime-graceful path theorem (P007 subproblem) is due to Panma and Rochanakul (2021).

## Problem dossier

Follow [PROBLEM_TEMPLATE.md](PROBLEM_TEMPLATE.md), and ensure links remain valid. Do not erase rejected ideas; document them in \`research-notes/\`.

## Pull requests

Prefer one conceptual change per PR: a corrected proof, a counterexample, an improved bound, or an audit. Link directly to the relevant problem ID, provide expected versus observed finite outputs, and list remaining mathematical objections. No automated pass makes a paper peer-reviewed or novel.
