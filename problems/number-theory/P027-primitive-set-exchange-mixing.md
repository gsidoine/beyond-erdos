# P027 — Mixing and geometry of maximum primitive-set exchanges

<!-- DOSSIER-SUMMARY -->
> **Research question:** Determine the mixing-time order and possible cutoff for single-chain heat-bath dynamics on maximum primitive subsets of [2n].  
> **Formulation:** candidate. **Novelty:** not certified; closely related to counting primitive sets and distributive-lattice walks.  
> **Verified/known progress:** An internally proved exact Hamming-distance theorem and diameter formula give diameter 5n/12+O(1); mixing remains unproved.  
> **Finite evidence:** Exact exhaustive graph distances for 2n≤20, agreeing with the theorem.  
> **Navigation:** [Full problem catalogue](../../README.md#problem-catalogue) · [Status and scope](../../README.md#status-and-scope) · [Literature and audits](../../README.md#literature-and-audits)
<!-- /DOSSIER-SUMMARY -->

**Area:** multiplicative combinatorics, graph reconfiguration, probability. **Status:** candidate with a proved structural foundation.

## Definitions

A primitive set A⊂[2n] is one in which no two distinct elements divide one another. Its maximum size is n (the upper half {n+1,…,2n} attains this). Let M_n be the family of all size-n primitive sets. Join A,B∈M_n when they differ by exactly one element. The resulting *exchange graph* is G_n.

For every odd u≤2n, its dyadic chain C_u={u,2u,4u,…}∩[2n] meets each A∈M_n in exactly one element. The single-chain **heat-bath walk** chooses an odd u uniformly and uniformly replaces the choice in C_u by one of the choices preserving primitivity and size n, including the current choice. The chain is reversible with the uniform distribution on M_n.

**P027.** Determine the total-variation mixing-time order of this walk as n→∞; is there cutoff? Relate the spectral gap to arithmetic divisibility constraints among odd u. The question is *not* whether the exchange graph is connected: that is established below.

## Structural theorem already proved within the project

Let e_A(u)≥0 satisfy u2^{e_A(u)}∈A. For odd u<v with u|v, A is primitive precisely when

$$
e_A(u)>e_A(v).
$$

The feasible exponent vectors are closed under coordinatewise minimum and maximum. The graph distance is exactly

$$
d_{G_n}(A,B)=\#\{u\le2n:\ u\text{ odd},\ e_A(u)\ne e_B(u)\}.
$$

Consequently,

$$
\boxed{\operatorname{diam}(G_n)=
\#\{u\le n/2:\ u\text{ odd}\}+
\#\{2n/3<u\le n:\ u\text{ odd}\}
=\frac{5n}{12}+O(1).}
$$

**Proof:** see [Primitive-set exchange geometry](../../theorems/P027-primitive-set-exchange-diameter.md). The source decomposition is classical and the theorem is **internally proved**, not externally refereed or historically certified original.

## Existing literature and novelty caveat

- [Liu–Pach–Palincza, *The number of maximum primitive sets of integers* (2021)](https://doi.org/10.1017/S0963548321000018): crucial primary predecessor. They prove the exponential counting constant exists; **the family M_n and dyadic chain decomposition are known**. Do not present either as original.
- [Heat-bath random walks with Markov bases (2018)](https://doi.org/10.1016/j.aam.2017.08.002): general heat-bath dynamics on integer fibers.
- [Rowmotion Markov chains (2024)](https://www.sciencedirect.com/science/article/pii/S0196885823001847): random walks on distributive lattices; closely related abstract machinery.

A specialized mixing theorem could already apply to this arithmetic poset. The exact-diameter argument is included for transparency, not novelty certification.

## Next adversarial gate

Seek a known general mixing theorem for uniformly random order ideals or monotone functions that subsumes the exponent constraints. Compute exact spectral gaps for n with tractable |M_n|; compare two natural update rules (whole-chain heat bath versus adjacent 2-exponent toggles) rather than conflating their mixing times.
