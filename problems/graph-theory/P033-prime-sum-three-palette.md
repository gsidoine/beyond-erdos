# P033 — Can three prime sums connect all integers?

<!-- DOSSIER-SUMMARY -->
> **Research question:** Can the graph on [n] be made connected using edges with only three distinct prime sums, for every n≥3?  
> **Formulation:** candidate. **Novelty:** not certified; two-prime case overlaps known twin-prime Hamiltonian-path constructions.  
> **Verified/known progress:** Exact two-prime characterization: two colors suffice precisely for a twin-prime pair p,p+2 with n−1≤p≤n+1; three-color universality remains open in this dossier.  
> **Finite evidence:** Exhaustive prime-palette search finds exactly two or three necessary colors for every 3≤n≤120.  
> **Navigation:** [Full problem catalogue](../../README.md#problem-catalogue) · [Status and scope](../../README.md#status-and-scope) · [Literature and audits](../../README.md#literature-and-audits)
<!-- /DOSSIER-SUMMARY -->

**Area:** additive number theory, graph connectivity and edge-colored matchings. **Status:** candidate with an internally proved two-color characterization.

## The question

Color each edge {a,b} of the graph on [n] by its sum a+b, but retain an edge **only if that sum is prime**. Let κ(n) be the minimum number of distinct prime colors whose union connects all n vertices.

**P033.** Is it true that

$$
\boxed{\kappa(n)\le3\quad\text{for every }n\ge3\ ?}
$$

Each fixed sum color is a matching, so one color cannot connect three or more vertices. The question asks whether **three prime-sum matchings always suffice to make a connected graph**, regardless of prime gaps.

## Theorem — Exactly when two colors suffice

For every n≥3,

$$
\boxed{\kappa(n)=2\iff
\text{some }p\in\{n-1,n,n+1\}\text{ has }p,\ p+2\text{ prime}.}
$$

### Proof

Suppose two distinct prime colors p<q yield a connected graph. Their color classes are matchings. They cannot include 2 (the only solution a+b=2 with positive integers has a=b=1, which is excluded), so both primes are odd.

Traversing edges of sums p and q applies the involutions x↦p−x and x↦q−x. Their composition is a translation by q−p. Hence all vertices in a connected component belong to at most two residue classes modulo d=q−p: the classes of x and p−x. If d≥4, the three vertices 1,2,3 occupy three distinct residue classes, contradicting connectivity. Thus q=p+2.

Vertex n must have an incident edge, so q>n. Vertex 1 must also have an incident edge. If q>n+1, this requires p≤n+1; if q=n+1 then p=n−1. In either case n−1≤p≤n+1.

Conversely assume p,p+2 are prime with n−1≤p≤n+1. The admissible reflection edges with sums p and p+2 form one spanning alternating path:

- If p=n−1 (necessarily n even), start at n and alternately reflect through p+2=n+1 and p=n−1; successive vertices are n,1,n−2,3,n−4,5,… .
- If p=n (necessarily n odd), start at n and alternate sums n+2 and n; successive vertices are n,2,n−2,4,n−4,6,… .
- If p=n+1 (necessarily n even), start at 1 and alternate sums n+1 and n+3; successive vertices are 1,n,3,n−2,5,n−4,… .

In each case the process visits every integer in [n] exactly once (the two interleaved parity sequences exhaust the interval). Thus the graph is connected and κ(n)=2. □

**Prior-art warning:** alternating twin-prime reflections already appear in existing prime-sum Hamiltonian-path discussions, including [Douglas Zare and Zhi-Wei Sun on MathOverflow](https://mathoverflow.net/questions/241569/for-which-n-is-there-a-permutation-such-that-the-sum-of-any-two-adjacent-eleme). The argument above is included as a rigorous baseline, **not certified historically novel**.

## Evidence for the three-color question

The [exact prime-palette enumerator](../../experiments/P033_prime_sum_three_palette.py) checks every set of up to three available prime colors and determines the true minimum for all 3≤n≤120. Every tested instance needs **exactly two or three colors**; none needs more than three. There are 28 two-color and 90 three-color instances in this range.

These finite checks do not imply the global three-color conjecture. The principal challenges are arithmetic: three colors produce a graph of maximum degree three, and a uniform connectivity argument must cope with unbounded prime gaps.

## An easier question already settled

Let q(n) be the **first prime greater than n**. The graph consisting of *all* prime-sum edges whose sums are at most q(n) is connected for every n≥2.

**Proof:** for n=2, the edge 1–2 has sum 3=q(2). Suppose the claim holds for n. The threshold q(n+1) is at least q(n), so all old edges remain. Bertrand's postulate gives n+1<q(n+1)<2(n+1) for n+1≥3; therefore the new vertex n+1 has a prime-sum edge to the old vertex q(n+1)−(n+1)∈[1,n]. Induction completes the proof. □

This connectivity theorem is **not** the three-color problem: it allows all primes up to q(n), an unbounded number of colors. The easy version was therefore not entered as a separate open conjecture.

## Source/priority gate

- [Chen–Fu–Guo, *Hamiltonicity in Prime Sum Graphs*](https://doi.org/10.1007/s00373-020-02241-1): the host graph and prime-sum paths have published results.
- [Croot–Jin, *Prime Sum Graphs and the Induced Trees They Contain*](https://doi.org/10.1007/s00373-025-02999-2): structural theory of the same arithmetic graph.
- [Prime-sum Hamiltonian-path discussion](https://mathoverflow.net/questions/241569/for-which-n-is-there-a-permutation-such-that-the-sum-of-any-two-adjacent-eleme): the reflection method underlying the two-color characterization is an established construction.
- [P009 two-prime sum-palette pairings](../number-theory/P009-two-prime-palette-pairings.md): a **perfect matching** uses one or two sum colors, while this problem requires the **union** of a few prime-color matchings to be connected. These are different combinatorial questions.

An exact source collision for the three-color connectivity conjecture is still possible and must be checked before claiming it is a historically new open problem.
