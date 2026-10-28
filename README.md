# Beyond Erdős

**Original candidate mathematical questions in the spirit of Paul Erdős.**

This research notebook explores questions in number theory, graph theory and additive combinatorics through exact definitions, proofs, counterexample searches, reproducible computation and historical literature checks.

> **Attribution:** These questions were independently formulated in an AI-assisted brainstorming session on 28 October 2026, inspired by the tradition of Paul Erdős. They are **not** claimed to have been posed by Erdős or to be new and unresolved. This repository is not affiliated with [erdosproblems.com](https://www.erdosproblems.com/) or [teorth/erdosproblems](https://github.com/teorth/erdosproblems).

## Research questions

| ID | Area | Question | Status |
|---|---|---|---|
| [P001](problems/number-theory/P001-prime-spectrum.md) | Additive number theory | Can prime-sum perfect matchings realize all but a bounded number of available prime sums? | Candidate; novelty unverified |
| [P002](problems/graph-theory/P002-prime-matching-reconfiguration.md) | Graph reconfiguration | Are prime-sum perfect matchings connected by four-vertex switches? | Candidate; novelty unverified |
| [P003](problems/graph-theory/P003-prime-matching-packing.md) | Extremal graph theory | Does the prime-sum graph have as many edge-disjoint perfect matchings as its minimum degree? | Candidate; novelty unverified |
| [P004](problems/number-theory/P004-sidon-exchange-connectivity.md) | Additive combinatorics | Are Sidon sets connected by single-element exchanges below the square-root scale? | Candidate; novelty unverified |

| [P005](problems/graph-theory/P005-coprime-permutation-switches.md) | Arithmetic graph reconfiguration | Are coprime permutations connected under validity-preserving value swaps? | Candidate; novelty unverified |
| [P006](problems/number-theory/P006-prime-avoiding-sidon-sets.md) | Additive number theory | What is the maximum size of a Sidon set with no prime differences? | Candidate; novelty unverified |

## Working standards

1. **State the problem precisely.** Record quantifiers, definitions and exceptional cases.
2. **Try to disprove before promoting.** Search for easy contradictions, counterexamples and known equivalents.
3. **Separate evidence from proof.** A numerical pattern is never a theorem.
4. **Reproduce computations.** Include source code and parameters for every published computational claim.
5. **Audit the literature.** Record related references and exact overlap. Do not infer novelty from a failure to find search hits.
6. **Preserve corrections.** False conjectures and known equivalent problems are archived rather than erased.

**Status vocabulary:** *candidate (unverified)*, *credible unresolved (literature-audited)*, *conjecture (evidence-backed)*, *proved*, *disproved*, or *previously known*.

## Computation

Research pass 2 adds an exact C++17 coprime-permutation connectivity check and an exact SciPy MILP for prime-difference-free Sidon sets. Consult their problem pages for bounds and solver-status caveats.

The included standard-library script enumerates prime-sum perfect matchings and four-cycle swaps for small instances:

```bash
python experiments/reconfiguration_small.py --max-n 10
```

See [literature-audits](literature-audits/README.md) for novelty-review standards.

## Scope

The aim is not to accumulate speculative conjectures. It is to ask concise, consequential mathematical questions, refine them adversarially and identify structural discoveries worth presenting to other mathematicians.
