# Random-order divisibility chains and the squarefree second-order gap

**Status:** internally proved, using the known oriented-hypercube accessibility theorem of Hegarty–Martinsson for the squarefree lower bound. Historical priority of the resulting application and comparison is unverified.

Let $\sigma_N$ be a uniformly random permutation of $[N]$. A *divisibility subsequence* is a sequence

$$
\sigma_N(i_1)\mid\sigma_N(i_2)\mid\cdots\mid\sigma_N(i_r),
\qquad i_1<\cdots<i_r,
$$

whose entries are distinct. Let $D_N$ be the maximum possible $r$, and $S_N$ the maximum when all entries must be squarefree. The two variables are defined using the same random permutation.

Put $L=\log N$, $\ell=\log\log N$, and $u=\log\log\log N$; logarithms are natural.

## Theorem

For every fixed $\varepsilon>0$, the following four inequalities hold simultaneously with probability tending to one as $N\to\infty$:

$$
\frac L\ell+(1-\varepsilon)\frac{Lu}{\ell^2}
\le D_N\le
\frac L\ell+(2+\varepsilon)\frac{Lu}{\ell^2},
$$

$$
\frac L\ell-(1+\varepsilon)\frac L{\ell^2}
\le S_N\le
\frac L\ell+(1+\varepsilon)\frac L{\ell^2}.
$$

In particular,

$$
D_N\sim S_N\sim\frac{\log N}{\log\log N}
\quad\text{in probability},
$$

but their difference is of strictly larger second-order magnitude than the squarefree fluctuations around this first approximation:

$$
\Pr\left(
1-\varepsilon\le
\frac{(D_N-S_N)(\log\log N)^2}
{\log N\,\log\log\log N}
\le 2+\varepsilon
\right)\longrightarrow1.
$$

The last assertion follows from the first four inequalities, applied with a smaller positive error parameter.

### Lemma 1 — Arbitrary divisibility chains

For every $\varepsilon>0$, with probability tending to one,

$$
\frac L\ell+(1-\varepsilon)\frac{Lu}{\ell^2}
\le D_N\le
\frac L\ell+(2+\varepsilon)\frac{Lu}{\ell^2}.
$$

**Proof.** Give each element of $[N]$ an independent continuous random priority; sorting by priority produces the uniform permutation.

For the lower bound set

$$
k=\left\lfloor\frac L\ell+
(1-\varepsilon)\frac{Lu}{\ell^2}\right\rfloor.
$$

For every odd integer $a\le N/2^{k-1}$ consider the chain

$$
a,2a,4a,\ldots,2^{k-1}a.
$$

Different odd $a$ give disjoint chains. Therefore the events that their priorities increase along the displayed chains are independent, each with probability $1/k!$. The number $M$ of chains satisfies $M=(1+o(1))N/2^k$, since $k=o(L)$ and $N/2^k\to\infty$. Stirling's formula gives

$$
\log(M/k!)=(\varepsilon+o(1))\frac{Lu}{\ell}\longrightarrow\infty.
$$

Consequently the probability that no chain succeeds is at most $\exp(-M/k!)=o(1)$.

For the upper bound, let $X_k$ count divisibility chains of length $k$ whose entries appear in increasing priority order. Every numerical chain has a unique representation

$$
a,\ ab_1,\ ab_1b_2,\ldots,ab_1\cdots b_{k-1},
\qquad a\ge1,\quad b_j\ge2,\quad
a\prod_{j=1}^{k-1}b_j\le N.
$$

Each such chain appears in the required random order with probability $1/k!$. For any $s>1$, Rankin's inequality gives

$$
\mathbb E X_k\le\frac{N^s}{k!}
\left(\sum_{a\ge1}a^{-s}\right)
\left(\sum_{b\ge2}b^{-s}\right)^{k-1}.
$$

Take $s=1+1/\ell$. The integral test gives $\sum_{a\ge1}a^{-s}\le1+\ell$ and $\sum_{b\ge2}b^{-s}\le\ell$. Thus

$$
\mathbb P(D_N\ge k)\le\mathbb E X_k
\le\frac{N^{1+1/\ell}(1+\ell)\ell^{k-1}}{k!}.
$$

For

$$
k=\left\lceil\frac L\ell+
(2+\varepsilon)\frac{Lu}{\ell^2}\right\rceil
$$

Stirling's formula yields

$$
\log\mathbb E X_k
\le-(\varepsilon+o(1))\frac{Lu}{\ell}\longrightarrow-\infty.
$$

Hence $\mathbb P(D_N\ge k)=o(1)$, proving the upper bound. $\square$

### Lemma 2 — Squarefree upper bound

For every fixed $\varepsilon>0$, eventually

$$
S_N\le\frac L\ell+(1+\varepsilon)\frac L{\ell^2}
$$

for every permutation of $[N]$.

**Proof.** In a strictly increasing squarefree divisor chain, every step introduces a new prime divisor. Hence a chain of length $r$ forces the product of the first $r-1$ primes to be at most $N$.

Write $P_k=\prod_{j=1}^k p_j$, where $p_j$ is the $j$th prime. Standard prime-number-theorem estimates, including the second term for $p_k$, give

$$
\log P_k=k\bigl(\log k+\log\log k-1+o(1)\bigr).
$$

For $k=L/\ell+O(L/\ell^2)$ this becomes

$$
\log P_k=L+\left(a-1+o(1)\right)\frac L\ell
\quad\text{if }k=\frac L\ell+a\frac L{\ell^2}.
$$

Choosing $a=1+\varepsilon/2$ shows $P_k>N$ for large $N$, and the claimed upper bound follows, allowing for integer rounding. $\square$

### Lemma 3 — Squarefree lower bound via accessible Boolean cubes

For every fixed $\varepsilon>0$, with probability tending to one,

$$
S_N\ge\frac L\ell-(1+\varepsilon)\frac L{\ell^2}.
$$

**Proof.** Let

$$
k=\left\lfloor\frac L\ell-
(1+\varepsilon)\frac L{\ell^2}\right\rfloor,
\qquad P_k=p_1\cdots p_k.
$$

The prime asymptotic used in Lemma 2 gives

$$
\log P_k=L-(2+\varepsilon+o(1))\frac L\ell.
$$

For each prime $a>p_k$ satisfying $aP_k\le N$, consider the $2^k$ squarefree integers

$$
\mathcal C_a=\left\{a\prod_{j\in J}p_j:J\subseteq[k]\right\}.
$$

These sets are pairwise disjoint for different $a$: their prime factors outside $\{p_1,\ldots,p_k\}$ identify the base prime. By the prime number theorem, the number $M$ of such prime bases satisfies

$$
\log M=(2+\varepsilon+o(1))\frac L\ell.
$$

The divisibility relation on each $\mathcal C_a$ is the Boolean lattice ordered by inclusion of $J$. Conditional on the two opposite vertices $a$ and $aP_k$ appearing respectively first and last among the elements of $\mathcal C_a$, the remaining priorities induce a uniformly random order of the other $2^k-2$ vertices. The conditioning event has probability

$$
\frac1{2^k(2^k-1)}.
$$

The established *constrained House-of-Cards* theorem for the directed Boolean hypercube states that when the bottom and top vertices are assigned respectively the smallest and largest priority, and the other vertices receive independent continuous priorities, an increasing path from bottom to top exists with probability tending to one as $k\to\infty$; see Hegarty–Martinsson [1]. Therefore the unconditional probability that a given $\mathcal C_a$ contains such a chain is at least

$$
\frac{1-o(1)}{2^k(2^k-1)}.
$$

Since the cubes are vertex-disjoint, these events are independent. The expected number of successful cubes is bounded below by

$$
M\frac{1-o(1)}{4^k}
=\exp\left(\left(2+\varepsilon-\log4+o(1)\right)\frac L\ell\right)
\longrightarrow\infty.
$$

Thus the probability that all cubes fail tends to zero. A successful cube yields $k+1$ squarefree integers in a strictly increasing divisor subsequence, giving the claimed bound. $\square$

**Proof of the theorem.** Combine Lemmas 1–3. Since $u\to\infty$, the $O(L/\ell^2)$ uncertainty in $S_N$ is negligible compared with $Lu/\ell^2$, yielding the displayed comparison of $D_N-S_N$. $\square$

## Open question

Does the normalized gap

$$
Z_N=
\frac{(D_N-S_N)(\log\log N)^2}
{\log N\,\log\log\log N}
$$

converge in probability to a constant? If so, the theorem forces this constant to lie in $[1,2]$. No convergence or value is claimed.

## Relation to known work

The result concerns increasing paths in a randomly ordered *divisibility poset*, not a random induced subposet. The squarefree proof uses the known correspondence between squarefree divisor intervals and Boolean cubes, together with the established accessibility theorem [1]. The arithmetic permutation question is distinct from the problem of arithmetic-progression subsequences, for which Goh–Zhao [2] established a leading constant of $2$ and substantially sharper concentration. The literature on divisibility poset dimension [3] studies a different invariant.

Targeted searches did not identify a previously published theorem with precisely the comparison above; this does not certify priority. The imported hypercube result is explicitly attributed.

## References

1. P. Hegarty and A. Martinsson, *On the existence of accessible paths in various models of fitness landscapes*, Annals of Applied Probability **24** (2014), 1375–1395. [DOI](https://doi.org/10.1214/13-AAP949).
2. M. K. Goh and R. Y. Zhao, *Arithmetic subsequences in a random ordering of an additive set*, Integers **21** (2021), #A89. [arXiv](https://arxiv.org/abs/2012.12339).
3. D. Lewis and V. Souza, *The order dimension of divisibility*, Journal of Combinatorial Theory, Series A **179** (2021), 105391. [DOI](https://doi.org/10.1016/j.jcta.2020.105391).
