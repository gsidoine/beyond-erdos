# Sidon sets avoiding an arbitrary sparse graph: a sharp-order resilience theorem

**Mathematical status:** internally proved, using Singer's classical perfect difference sets and the classical Turán independence bound. **Historical originality of this combination is not verified.** This is a research result, not a newly certified open problem.

## Statement

For a simple graph $G$ with vertex set $[N]$, put

$$
s(G)=\max\{|A|: A\subseteq[N]\text{ is Sidon and independent in }G\}.
$$

Define the universal extremal value

$$
g(N,m)=\min_{|E(G)|\le m}s(G),\qquad 0\le m\le\binom N2.
$$

**Theorem 1 (quantitative Singer–Turán resilience).** Let $q$ be any prime power with $v=q^2+q+1\le N$, and let $G$ have $m$ edges. Then

$$
\boxed{s(G)\ge \frac{(q+1)^2}{q+1+2m/v}.}\tag{1}
$$

Furthermore, a deletion argument gives

$$
\boxed{s(G)\ge q+1-m/v.}\tag{2}
$$

In particular, choosing primes $q=(1-o(1))\sqrt N$ by the prime number theorem shows that **every** graph on $[N]$ with $m=o(N^{3/2})$ edges has a Sidon independent set of size $(1-o(1))\sqrt N$.

**Theorem 2 (sharp uniform order).** Uniformly for $0\le m\le\binom N2$,

$$
\boxed{g(N,m)=\Theta\left(\min\left\{\sqrt N,\frac{N^2}{m+N}\right\}\right).}\tag{3}
$$

The implicit positive constants are absolute. Thus $N^{3/2}$ is the exact order of the worst-case number of arbitrary forbidden pairs that can cause a first-order loss in the maximal Sidon-set size.

## Proof of Theorem 1

Singer's projective-plane construction gives a *perfect difference set* $D\subseteq\mathbb Z_v$ of cardinality $q+1$ such that every nonzero residue of $\mathbb Z_v$ occurs **exactly once** as an ordered difference of distinct elements of $D$.

For $t\in\mathbb Z_v$, let $D+t$ be the translate, viewed as a subset of $[v]\subseteq[N]$ by choosing integer representatives. Each translate is an integer Sidon set: an equality of integer sums gives an equality modulo $v$, hence an equality of nonzero ordered differences modulo $v$ and therefore the same unordered summand pair.

Each unordered pair $\{x,y\}\subseteq[v]$ appears in **exactly one** of the $v$ translates. Indeed the prescribed ordered residue difference $y-x$ is realized by one ordered pair $(d_2,d_1)$ of $D$, hence by a unique common shift $t$.

Consequently, for any graph $G$ on $[N]$, writing $G_v=G[[v]]$,

$$
\sum_{t\in\mathbb Z_v}e(G_v[D+t])=e(G_v)\le m.
$$

Some translated Singer set $D+t$ has at most $m/v$ forbidden edges. Removing one endpoint of each edge gives (2).

For (1), Turán's elementary bound says a graph on $k$ vertices with $e$ edges contains an independent set of at least $k^2/(k+2e)$ vertices. Apply it to the selected translated set with $k=q+1$ and $e\le m/v$. Its independent subset remains Sidon.

Finally choose prime $q$ with $q=(1-o(1))\sqrt N$ and $q^2+q+1\le N$, using the prime number theorem. Then $q+1\sim\sqrt N$ and $v\sim N$. If $m=o(N^{3/2})$, (2) is $\sqrt N-o(\sqrt N)$, and the classical upper bound for Sidon sets is $(1+o(1))\sqrt N$. QED.

## Proof of Theorem 2

**Lower bound.** Insert $q+1\asymp\sqrt N$ and $v\asymp N$ into (1):

$$
s(G)\gg\frac{N}{\sqrt N+m/N}
=\frac{N^2}{N^{3/2}+m}
\asymp\min\left\{\sqrt N,\frac{N^2}{m+N}\right\}.
$$

The last comparison is valid throughout $0\le m\le\binom N2$.

**Upper bound.** Since Sidon sets in $[N]$ have size $O(\sqrt N)$, $g(N,m)\ll\sqrt N$ for all $m$. If $m\ge N^{3/2}$, let $D=\lfloor m/N\rfloor$ and take $G$ joining every pair $x<y$ with $y-x\le D$. This graph has at most $ND\le m$ edges. Every independent set is $(D+1)$-separated, hence has at most $\lceil N/(D+1)\rceil$ vertices. Therefore

$$
g(N,m)\le \left\lceil\frac{N}{D+1}\right\rceil\ll\frac{N^2}{m}
$$

throughout $N^{3/2}\le m\le\binom N2$. This completes the sharp-order comparison. QED.

## Why the edge count alone ceases to characterize individual graphs

The universal $N^{3/2}$ threshold is best possible, but above it the *placement* of forbidden edges matters.

Let $D=\lfloor N^{3/4}\rfloor$. The graph joining pairs whose integer distance is at most $D$ has $\Theta(N^{7/4})$ edges, and every independent set has $O(N^{1/4})$ elements.

By contrast, let $G$ be the complete graph on the first $\lfloor N^{7/8}\rfloor$ vertices, with the remaining vertices isolated. It also has $\Theta(N^{7/4})$ edges, but the consecutive interval

$$
\{\lfloor N^{7/8}\rfloor+1,\ldots,N\}
$$

has length $N-o(N)$ and contains a Sidon set of size $(1-o(1))\sqrt N$.

Thus graphs with the **same order of forbidden edges** can produce either a severe loss or no asymptotic loss. No necessary-and-sufficient criterion can depend *only* on the edge-count exponent.

## A refined upper bound in the critical window

Let $G_{N,D}$ join all pairs $x<y$ in $[N]$ for which $y-x\le D$. Write an independent Sidon set as $a_1<\cdots<a_k$. Its $k-1$ adjacent gaps

$$
h_i=a_{i+1}-a_i
$$

are **distinct positive integers**: equality of two different adjacent gaps would give equal sums from two different unordered pairs, contradicting Sidonicity. Independence from $G_{N,D}$ forces $h_i\ge D+1$. Therefore

$$
N-1\ge\sum_{i=1}^{k-1}h_i
\ge (k-1)(D+1)+\frac{(k-1)(k-2)}2
=(k-1)D+\frac{k(k-1)}2.
$$

Taking $D=\lfloor c\sqrt N\rfloor$ with fixed $c>0$ and writing $k=\alpha\sqrt N+o(\sqrt N)$ yields

$$
\boxed{\limsup_{N\to\infty}\frac{s(G_{N,D})}{\sqrt N}
\le\min\{1,\sqrt{c^2+2}-c\}.}
$$

(The $1$ is the classical Sidon upper bound.) In particular, **every $c>1/2$ causes a strict leading-constant loss**, while the edge count of $G_{N,D}$ is $(c+o(1))N^{3/2}$.

For $0<c\le 1/2$, this elementary adjacent-gap argument gives no loss. It is not known from the present work whether the uniform $o(N^{3/2})$ resilience theorem can be strengthened to a positive fraction of $N^{3/2}$ forbidden edges *with no asymptotic loss*. This is a candidate critical-window question, not a certified new open problem. The recent literature on the distribution and diameter of Sidon sets may provide more refined obstructions.

## Exact finite incidence check

For $q=2$, the Singer difference set $D=\{0,1,3\}\subseteq\mathbb Z_7$ has three elements. Its seven translates are the lines of the Fano plane. The 21 unordered vertex pairs are distributed **exactly once** among these seven three-element blocks. This identity is the finite combinatorial mechanism behind the averaged edge count above.

## Context and novelty boundary

The following ingredients are *established*:

- Singer (1938): perfect cyclic difference sets with parameters $(q^2+q+1,q+1,1)$, via finite projective planes.
- Turán's independence bound $k^2/(k+2e)$ and elementary alteration.
- Babai–Sós (1985), *Sidon Sets in Groups and Induced Subgraphs of Cayley Graphs*, **Proposition 4.1**, develops independent-set alteration for additive Sidon hypergraphs.
- Bollobás–Pikhurko (2005), *Integer sets with prescribed pairwise differences being distinct*, studies **Sidon-like labeling of graph edges**. Its main optimization problem differs from selecting a Sidon independent set under arbitrarily forbidden vertex pairs.
- The 2026 work *On the largest Sidon subset in a finite subset of R^N* uses Singer coverings but studies arbitrary allowed *vertex subsets*, not arbitrary forbidden *edges*.

A targeted search did not locate (1)–(3) stated as this extremal function, but the combination uses standard design-incidence averaging and Turán's theorem. **It is not historically certified original; the novelty is at most the explicit sparse-graph-resilience formulation and its sharp worst-case threshold.** This is not a solution of an existing Erdős open problem.

### References

1. J. Singer, *A theorem in finite projective geometry and some applications to number theory*, Trans. Amer. Math. Soc. **43** (1938), 377–385.
2. L. Babai and V. T. Sós, *Sidon Sets in Groups and Induced Subgraphs of Cayley Graphs*, European J. Combin. **6** (1985), 101–114. https://doi.org/10.1016/S0195-6698(85)80001-9
3. B. Bollobás and O. Pikhurko, *Integer sets with prescribed pairwise differences being distinct*, European J. Combin. **26** (2005), 607–616. https://doi.org/10.1016/j.ejc.2004.04.008
4. [Singer difference-set exposition and parameters](https://page.mi.fu-berlin.de/szabo/PDF/singer.pdf).
