# Research selection — discovery pass 3 (2026-10-28)

## Discarded as open: coprime graceful permutations

**Literature correction:** This complete iff theorem is *previously known*: Panma and Rochanakul, [*Prime-Graceful Graphs* (2021), Theorem 2.1](https://thaijmath.com/index.php/thaijmath/article/view/1264), explicitly prove that the path \(P_n\) is prime-graceful iff \(n\le5\). Our parity proof is an independent rederivation only. The remaining extremal problem has not been matched to a published answer.

A permutation of \(\{1,\ldots,n\}\) with all adjacent entries coprime and all \(n-1\) consecutive gaps distinct exists **iff \(n\le5\)**. A complete parity proof is in [P007](../problems/graph-theory/P007-coprime-difference-spectrum.md).

For \(n\ge6\), too many distinct even gaps would need to arise from adjacent pairs of odd vertices, but parity and the need to separate even vertices permit at most one odd–odd adjacency when \(n\) is even and at most two when \(n\) is odd.

**Outcome:** the original yes/no problem was completely solved in a few lines. It was replaced with an extremal question maximizing the total number of distinct gaps, which is less trivial.

## P007 retained as a candidate

The rigorous parity bound is
\[
D(n)\le \min\left(n-1,\left\lfloor(n+3)/2\right\rfloor\right).
\]
An exact integer-programming formulation saturates this bound for \(n=3,\ldots,30\) and selected \(n\le120\). The all-\(n\) equality remains a candidate conjecture, not a verified new open problem.

## P008: deeper theorem replaced successive open questions

1. Initial idea: determine the leading connectivity threshold of a Bernoulli-percolated coprime graph.
2. **Resolved:** an independent family of low-degree vertices forces a lower threshold \(e^\gamma\log n\log\log n/n\); a two-scale cut union bound gives the matching upper threshold.
3. Next idea: determine the isolated-vertex Poisson limit and connectivity Gumbel law.
4. **Resolved:** factorial moments and exclusion of connected components of intermediate sizes prove the window law when centered at \(\mu_n(b_n)=1\).
5. **Still a candidate problem:** give an **explicit number-theoretic asymptotic center** \(B(n)\) with \(b_n-B(n)=o(\log\log n/n)\).

This is a genuine theorem-first outcome, but its possible prior existence in general graph-percolation literature remains to be audited independently. See [P008](../problems/probability/P008-coprime-percolation-critical-window.md).

## Evidence standards

No numerical experiment is being used to assert an infinite theorem. Theoretical results are stated with complete proof arguments and caveats, and experiments are attached only to check finite instances and make the work reproducible.
