# P003 — Maximum perfect-matching packing in a prime-sum graph

**Area:** extremal graph theory, arithmetic graph factors  
**Status:** candidate conjecture; novelty and unresolved status unverified  
**Proposed:** 28 October 2026

## Definition

Let \(P_{2n}\) be the prime-sum graph from P002. Let \(\delta_n\) denote its minimum degree, and let \(\lambda(n)\) be the maximum number of pairwise **edge-disjoint perfect matchings** in \(P_{2n}\).

Necessarily \(\lambda(n)\le\delta_n\), since every perfect matching uses one edge at every vertex.

## Main conjecture

\[
\boxed{\lambda(n)=\delta_n\text{ for every }n\ge1.}
\]

Equivalently, is there a spanning \(\delta_n\)-regular subgraph of \(P_{2n}\)? This equivalence is exact: any union of \(k\) edge-disjoint perfect matchings is a \(k\)-factor; a \(k\)-regular bipartite graph admits a decomposition into \(k\) perfect matchings.

The prime number theorem gives \(\delta_n\sim 2n/\log n\), so a positive answer would imply \(\lambda(n)\sim 2n/\log n\).

## Exact flow formulation

Write \(U\) for the odd vertices and \(V\) for the even vertices, so \(|U|=|V|=n\). By integral max-flow/min-cut, a spanning \(k\)-factor exists exactly when

\[
e(X,V\setminus Y)\ge k(|X|-|Y|)
\]

for **all** \(X\subseteq U\) and \(Y\subseteq V\). For a given \(k\), use a flow network with source–\(U\) capacities \(k\), prime-sum edges capacity \(1\), and \(V\)–sink capacities \(k\).

The proposed conjecture is therefore an explicit arithmetic cut-expansion statement for \(k=\delta_n\).

## Research directions

- Find a structured cut that disproves the conjecture.
- Prove suitable uniform edge-distribution/expansion bounds.
- Audit existing results on factors in arithmetic graphs.
- Reproduce numerical max-flow tests with a committed script, exact input values and full output logs.

## Evidence and novelty

Earlier exploratory tests were reported, but the numerical claims are deliberately **not** included as verified evidence in this entry until independently reproduced in committed code. No comprehensive novelty audit has been completed.
