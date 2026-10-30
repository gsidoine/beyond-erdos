# P033 — Source and proof-status audit of three-prime connectivity

**Research question:** Can at most three distinct prime sums connect [n] for **every** n≥3?

**New internal theorem:** Yes for **all sufficiently large n**. The remaining universal statement is an unspecified finite-exception problem, because the analytic proof uses an ineffective threshold.

## Exact mathematical dependencies

1. **Deterministic interval-reflection lemma:** Any three odd sums p<q<n<r within distance D of n, with coprime half-differences and n≥12D+10, produce a connected graph. This is proved elementarily in [the theorem note](../theorems/P033-eventual-three-prime-sum-connectivity.md).
2. **PNT:** Two primes below n, within a fixed proportion of n, have a gap of size O(log n) by the pigeonhole principle.
3. **CRT and Siegel–Walfisz:** Choose a reduced residue class modulo that O(log n) gap to obtain a third prime just above n with coprime half-differences. No twin-prime hypothesis is used.
4. **Earlier P033 exact two-color theorem:** Two prime sums connect [n] if and only if n is within one of the smaller prime of a twin-prime pair (in the exact sense p∈{n−1,n,n+1}).
5. **Classical twin-prime sieve upper bound:** Combining the eventual theorem and two-color characterization gives κ(n)=3 for density-one n.

## Closest published predecessors and priority boundary

- [Chen–Fu–Guo (2021), *Hamiltonicity in Prime Sum Graphs*](https://doi.org/10.1007/s00373-020-02241-1) explicitly introduces Hamiltonian prime sets; in particular it proves three-color Hamiltonian constructions when n is aligned with appropriate twin primes, and infinite families from bounded gaps. **A connected three-color graph is a weaker target than a three-color Hamiltonian cycle**, and the paper's displayed theorem does not settle eventual **connectivity** for every n. These results must nevertheless be credited because they use nearly the same host graph and color-by-sum viewpoint.
- [Croot–Jin (2026), *Prime Sum Graphs and the Induced Trees They Contain*](https://doi.org/10.1007/s00373-025-02999-2) proves significant induced-tree structure of the host but does not claim that three sum colors span a connected subgraph.
- [Kedlaya, *Error bounds for primes in arithmetic progressions*](https://kskedlaya.org/ant/chapter-11.html): Siegel–Walfisz is the indispensable established analytic input. The upper/lower cutoffs cannot be made effective from this qualitative proof alone.
- [Brun–Selberg sieve explanation](https://kskedlaya.org/ant/chap-brun.html): the density-one corollary uses the standard O(X/log²X) twin-prime upper bound, **not** an originally proved sieve estimate.

The targeted searches did **not** identify a published exact version of the P033 eventual-connectivity theorem. This **does not certify historical novelty**: a full mathematical review of bounded-color prime-sum graphs, additive matchings and generalized reflection connectivity remains necessary.

## Referee questions

- Verify all intermediate reflection vertices stay in [n] when connecting the odd central core and both tails.
- Verify the coprime-step interval lemma at the exact boundary m=a+b.
- Verify the CRT-selected class p+2k is coprime to the **full** modulus 2g, including small prime factor 2.
- Verify Siegel–Walfisz is used in its uniform logarithmic-modulus range, not merely fixed-modulus Dirichlet.
- Keep eventual connectivity distinct from all-n connectivity and from three-color Hamiltonicity.
- Confirm that the pre-existing two-color characterization and its reflection proof have no missing small-n exceptions.

## Next test

A meaningful further theorem would remove the ineffective finite-exception problem, either by deriving an explicit (possibly enormous) N0 from effective prime-distribution results and performing finite verification, or by a new elementary graph extension lemma that proves three-color connectivity for every n≥3. The present analytic result does not supply either.
