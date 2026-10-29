# P025 — Bottleneck Hamiltonicity in least-common-multiple graphs

<!-- DOSSIER-SUMMARY -->
> **Research question:** How large must the allowed adjacent lcm be before [N] admits a Hamiltonian cycle?
> **Formulation:** candidate; minimum bottleneck exactly defined.
> **Novelty:** unverified, targeted comparison 2026-10-29.
> **Elementary bound:** normalized bottleneck at least \((1+o(1))N/(4\log N)\).
<!-- /DOSSIER-SUMMARY -->

**Area:** multiplicative combinatorics, Hamiltonian graph theory, extremal permutations. **Status:** candidate.

## Definition

For \(T\ge1\), let \(L_N(T)\) be the graph on \([N]\) with distinct \(a,b\) adjacent exactly when \(\operatorname{lcm}(a,b)\le T\). Define

$$
\Lambda(N)=\min_{\text{cyclic permutations }(a_1,\ldots,a_N)}
\ \max_{1\le i\le N}\operatorname{lcm}(a_i,a_{i+1}),
\qquad a_{N+1}=a_1.
$$

(For \(N<3\), make no cycle claim.) Put \(t_N=\Lambda(N)/N\).

**P025.** Determine the asymptotic order of \(t_N\). In particular, is \(t_N=\Theta(N/\log N)\)? If so, does \(t_N\log N/N\) tend to a positive finite constant?

The conjectural order is a **question**, not a claimed theorem.

## A rigorous nontrivial lower bound

Let \(P_N\) be the primes in \((N/2,N]\), with \(r=|P_N|=\pi(N)-\pi(N/2)\). Suppose a Hamiltonian cycle uses only edges of lcm at most \(tN\), with \(t<N/4\). No two distinct vertices in \(P_N\) can be adjacent because their lcm is their product \(>N^2/4>tN\).

For any \(q\in P_N\) and neighbor \(m\ne q\), \(m\) cannot be a multiple of \(q\) within \([N]\), hence \(\operatorname{lcm}(q,m)=qm\) and \(m\le tN/q<2t\). Therefore all \(2r\) cycle edges incident with \(P_N\) must meet the fewer than \(2t\) vertices \(m<2t\). Each such vertex has only two cycle edges, so \(2r\le 4t\) and \(t\ge r/2\).

If instead \(t\ge N/4\), that bound is even stronger asymptotically. By the prime number theorem \(r\sim N/(2\log N)\), so in all cases

$$
\boxed{t_N\ge(1+o(1))\frac{N}{4\log N}.}
$$

The trivial upper bound is \(t_N\le N\), since \(\operatorname{lcm}(a,b)\le ab\le N^2\). There is a genuine factor-\(\log N\) gap between these elementary bounds.

## Prior art and precise distinction

- [Melotti–Saias, *On path partitions of the divisor graph* (2020)](https://doi.org/10.4064/aa190516-10-9): divisibility and path partitions, not a Hamiltonian **lcm bottleneck**.
- [McNew, *Permutations and the divisor graph of [1,n]* (2023)](https://doi.org/10.1112/mtk.12215): arithmetic permutation/divisor graph results; check exact paper theorem before claiming independence.
- [Erdős–Freud–Hegyvári, *Arithmetical properties of permutations of integers* (1983)](https://users.renyi.hu/~p_erdos/1983-02.pdf): **high-risk predecessor** concerning adjacent gcd/lcm extremal functionals. Its statements must be checked closely: it may already determine this minimax quantity or a closely related path variant.
- [P010 submitted manuscript](../graph-theory/P010-minimum-coprime-adjacencies.md): counts coprime transitions, not the maximal adjacent lcm along a **cycle**.

**Priority status:** high historical-collision risk. Do **not** present this as genuinely open until the 1983 paper and McNew have been checked for this exact minimax problem. The counting lower bound is elementary and not a novelty claim.

## Next falsification gate

Compute \(\Lambda(N)\) exactly for small \(N\) by sorting distinct lcm edge weights and testing Hamiltonian cycles, with integer exactness and solver certificates. Compare Hamiltonian paths versus cycles; test whether the lower-order answer can be read directly from a known adjacent-lcm extremal theorem. If known, preserve ID as a historical note rather than claim an original problem.

## Revision history

- 2026-10-29: Proposed as prospective P025; high priority-risk tag.
