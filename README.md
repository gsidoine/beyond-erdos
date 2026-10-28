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

| [P007](problems/graph-theory/P007-coprime-difference-spectrum.md) | Graph labeling / number theory | Does a coprime Hamiltonian path attain the parity upper bound on its number of distinct gaps? | **Full graceful case already known (2021)**; extremal extension unverified |
| [P008](problems/probability/P008-coprime-percolation-critical-window.md) | Random graphs / number theory | Can the connectivity window of a percolated coprime graph be centered by an **explicit arithmetic expansion**? | Candidate centering question; leading threshold + Gumbel law proved here, novelty unverified |

### Highlight of research pass 3

P008 contains a complete, independently auditable proof of a sharp asymptotic connectivity transition at \(e^\gamma\log n\log\log n/n\), a Poisson limit for isolated vertices, and a Gumbel connectivity window at an implicitly defined center. **This is an internally derived mathematical result, not a certified novelty or priority claim.** The remaining question asks for an explicit arithmetic centering to the much finer window scale \(\log\log n/n\).

P007 also records a **previously known** fully resolved result of Panma–Rochanakul (2021): coprime graceful permutations exist only for \(n\le5\) and retains a sharper extremal problem with exact MILP evidence through many finite cases.

## Literature audit (all selected problems)

The [comprehensive P001–P008 audit (28 October 2026)](literature-audits/2026-10-28-comprehensive-P001-P008.md) identifies direct precedents, general equivalences, verified prior-art collisions, and unresolved novelty questions. **None of the eight exact candidate questions is yet certified genuinely novel**; in particular P007's complete prime-graceful path existence theorem was published in 2021.

| [P009](problems/number-theory/P009-two-prime-palette-pairings.md) | Additive number theory | Can every prime-sum perfect matching problem be solved using at most two distinct prime values? | Candidate; linked to classical prime-difference questions |
| [P010](problems/graph-theory/P010-minimum-coprime-adjacencies.md) | Arithmetic graph theory | What is the smallest possible number of coprime adjacencies in a permutation of `[n]`? | Candidate; rigorous asymptotic bounds and exact finite tests |

### New research, pass 4

[P009/P010 literature audit](literature-audits/2026-10-28-pass-4.md) records known antecedents (including **Erdős–Freud–Hegyvári 1983**, on arithmetic of adjacent permutation entries), a finite failed generalization relevant to P005, and a solved/triaged gcd-spectrum idea. P009 has explicit prime-pair witnesses for every `2<=n<=100000`; P010 has rigorous prime-obstruction and prime-factor-grouping bounds
\[
(7/12+o(1))n/\log n\le h(n)\le(1+o(1))n/\log n.
\]
**No claim that either exact problem is newly discovered and open has been independently certified.**

## Working standards

1. **State the problem precisely.** Record quantifiers, definitions and exceptional cases.
2. **Try to disprove before promoting.** Search for easy contradictions, counterexamples and known equivalents.
3. **Separate evidence from proof.** A numerical pattern is never a theorem.
4. **Reproduce computations.** Include source code and parameters for every published computational claim.
5. **Audit the literature.** Record related references and exact overlap. Do not infer novelty from a failure to find search hits.
6. **Preserve corrections.** False conjectures and known equivalent problems are archived rather than erased.

**Status vocabulary:** *candidate (unverified)*, *credible unresolved (literature-audited)*, *conjecture (evidence-backed)*, *proved*, *disproved*, or *previously known*.

## Computation

Research pass 3 adds a coprime difference-spectrum MILP and two percolation samplers, including a numerical solver for the exact critical center. Install the optional Python dependencies from [requirements-experiments.txt](requirements-experiments.txt) and see each problem page for commands.

Research pass 2 adds an exact C++17 coprime-permutation connectivity check and an exact SciPy MILP for prime-difference-free Sidon sets. Consult their problem pages for bounds and solver-status caveats.

The included standard-library script enumerates prime-sum perfect matchings and four-cycle swaps for small instances:

```bash
python experiments/reconfiguration_small.py --max-n 10
```

See [literature-audits](literature-audits/README.md) for novelty-review standards.

## Scope

The aim is not to accumulate speculative conjectures. It is to ask concise, consequential mathematical questions, refine them adversarially and identify structural discoveries worth presenting to other mathematicians.
