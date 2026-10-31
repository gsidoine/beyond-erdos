# P040 — Local resilience of coprime perfect matchings

Let $B_n$ be the balanced bipartite graph with parts

$$
E_n=\{2,4,\ldots,2n\},\qquad O_n=\{1,3,\ldots,2n-1\},
$$

where $eo$ is an edge if $\gcd(e,o)=1$. Define its **local matching resilience**

$$
\rho_n=\min_{\substack{F\subseteq E(B_n)\\B_n-F\text{ has no perfect matching}}}
\max_{v\in V(B_n)}\frac{d_F(v)}{d_{B_n}(v)}.
$$

Here $E(B_n)$ denotes the **edge set** of the graph (the notation $E_n$ above is the even-vertex class).

## Research question

**Does $\rho_n\to\frac12$?**

Equivalently, for every fixed $\varepsilon>0$, does every subgraph obtained by retaining more than $(1/2+\varepsilon)$ of each vertex's original coprime neighbors still admit a perfect matching, for all sufficiently large $n$?

The target is sharp if true; the elementary upper-bound argument below gives $\limsup\rho_n\le1/2$.

## A proved universal obstruction

**Proposition.** $\displaystyle \limsup_{n\to\infty}\rho_n\le\frac12$.

**Proof.** For any positive integer $m\le2n$, inclusion–exclusion gives, uniformly,

$$
\#\{k\le n:\gcd(k,m)=1\}
=n\frac{\varphi(m)}m+O(2^{\omega(m)}).
$$

The standard estimates $\varphi(m)/m\gg1/\log\log(3m)$ and $2^{\omega(m)}=m^{o(1)}$ show that every vertex of $B_n$ has degree $\gg n/\log\log(3n)$. For an odd vertex $o$ this follows directly from $\gcd(2k,o)=1\iff\gcd(k,o)=1$. For an even vertex $e$, the same estimate applies to odd numbers up to $2n$ coprime to $e$.

Choose independently, uniformly sized vertex subsets $S\subset E_n$ and $T\subset O_n$, where $|S|=\lceil n/2\rceil$ and $|T|=|S|-1$. Delete **all edges from $S$ to $O_n\setminus T$**. The resulting graph violates Hall's condition because the neighborhood of $S$ is contained in the smaller set $T$.

For each affected vertex, the number of deleted incident edges is a hypergeometric random variable whose expectation is $(1/2+O(1/n))$ times its original degree. Since the minimum degree is $\gg n/\log\log n$, the hypergeometric concentration inequality and a union bound imply the existence of such $S,T$ with all relative deleted degrees at most $1/2+o(1)$. QED.

## Exact finite Hall search

Hall's criterion reduces the resilience parameter to an explicit minimax problem over $S\subseteq E_n$, $T\subseteq O_n$ with $|T|=|S|-1$. It is sufficient to remove exactly the edges between $S$ and $O_n\setminus T$. The accompanying exhaustive search finds:

| $n$ | $\rho_n$ |
|---:|---:|
| 2 | $1$ |
| 3 | $2/3$ |
| 4 | $3/4$ |
| 5 | $3/5$ |
| 6 | $3/5$ |
| 7 | $1/2$ |
| 8 | $4/7$ |
| 9 | $1/2$ |
| 10 | $1/2$ |

These are **exact finite computations**, not an asymptotic proof. No asymptotic lower bound near $1/2$ is established.

## Prior art and consequence

- Pomerance, [*Coprime Matchings*](https://math.dartmouth.edu/~carlp/coprime_int.pdf), *Integers* **21** (2021), proves perfect coprime matchings between sufficiently long intervals and, more strongly, the existence of at least one coprime edge between arbitrary large vertex sets satisfying a Hall-type sum condition. In particular, **plain existence of a matching is already a classical consequence**. That theorem does *not* assert survival after deleting nearly half of every vertex's edges.
- Bohman and Peng's earlier interval-matching results, discussed in Pomerance (2021), are direct predecessors.
- Ben-Shimon, Krivelevich and Sudakov, [*Local Resilience and Hamiltonicity Maker–Breaker Games in Random Regular Graphs*](https://doi.org/10.1017/S0963548310000685), develop the classical local-resilience framework for different graph families.
- The 2023 paper [*On sufficient conditions for spanning structures in dense graphs*](https://doi.org/10.1112/plms.12552) discusses robust expansion and degree-sensitive Hamiltonicity conditions in general dense graphs.

A positive resolution at the sharp constant would require genuinely **quantitative arithmetic Hall expansion** robust under adversarial deletions. It would strengthen the known coprime matching existence results rather than restate them.

**Novelty gate:** the exact degree-relative resilience limit for this balanced arithmetic bipartite graph was not located in targeted searches. That does **not** establish historical originality. **Editorial placement: The Acorns**, selected because the question has a sharp benchmark, a short statement, explicit finite evidence and structural implications connecting sieve theory to extremal matching resilience.
