# Induced cycles in the integer non-coprime graph

**Status:** internally proved. Historical originality of the assembled arithmetic asymptotic and exact saturation criterion is unverified.

Let $G_N$ have vertices $[N]$ and an edge $ab$ when $\gcd(a,b)>1$. Let $H(N)$ be its longest induced cycle length (zero if none exists). Let $T_N$ be the graph whose vertices are the primes at most $N$ and whose edges satisfy $pq\le N$.

## Theorem 1: exact reduction to a threshold graph

**For every integer $k\ge4$, $G_N$ contains an induced $k$-cycle if and only if $T_N$ contains a $k$-cycle.**

**Proof.** Suppose $v_1,\ldots,v_k$ is an induced cycle in $G_N$. Choose a prime $r_i$ dividing $\gcd(v_i,v_{i+1})$, with cyclic indices. The primes $r_i$ are pairwise distinct: if a prime were chosen for two adjacent edges, it would divide three consecutive vertices and create a chord; if chosen for two nonadjacent edges, it would divide all four edge endpoints and create at least one chord. Hence $r_{i-1}r_i\mid v_i\le N$, and $r_1,\ldots,r_k$ is a cycle in $T_N$.

Conversely, for a cycle of distinct primes $r_1,\ldots,r_k$ in $T_N$, take integer vertices $v_i=r_{i-1}r_i$. They lie in $[N]$, consecutive vertices have a common prime, and nonconsecutive vertices are coprime, since their prime supports are disjoint when $k\ge4$. Thus they form an induced cycle. QED.

The graph $T_N$ is a **threshold graph** with vertex weights $\log p$ and threshold $\log N$, so its longest-cycle problem has classical algorithms; see Mahadev–Peled (1994).

## Theorem 2: sharp asymptotic

$$
\boxed{H(N)\sim2\pi(\sqrt N)\sim\frac{4\sqrt N}{\log N}.}
$$

**Upper bound.** In a prime cycle in $T_N$, no two primes greater than $\sqrt N$ can be adjacent. The number of such large primes on the cycle is at most the number of smaller primes. By Theorem 1, $H(N)\le2\pi(\sqrt N)$ whenever a cycle of length at least four exists.

**Construction.** Put $x=\sqrt N$, fix $0<\delta<1/10$, and write $m=\pi(x)$. Choose $t=\lfloor(1-4\delta)m\rfloor$ smallest primes $p_1<\cdots<p_t$, and choose $t$ consecutive primes $q_1<\cdots<q_t$ starting just above $(1+\delta)x$. The prime number theorem implies, uniformly for $1\le i\le t$,

$$
p_i/x=i/m+o(1),\qquad
q_{t-i+1}/x=(2-3\delta)-i/m+o(1).
$$

The leading expression for their product is $z(2-3\delta-z)$, with $0\le z\le1-4\delta$. This is at most

$$
(1-4\delta)(1+\delta)<1.
$$

Therefore for sufficiently large $N$, all products connecting consecutive primes in the alternating cycle

$$
p_1,q_t,p_2,q_{t-1},\ldots,p_t,q_1,p_1
$$

are at most $N$ (the cyclic closing edge $p_1q_1$ is smaller as well). By Theorem 1 this produces an induced cycle in $G_N$ of length $2t\ge 2(1-4\delta)m-O(1)$. Letting $\delta$ tend to zero after taking $N\to\infty$ proves the result. QED.

## Theorem 3: exact saturation criterion

Let $m=\pi(\sqrt N)\ge2$, write $p_1<\cdots<p_m$ for the small primes and $q_1<\cdots<q_m$ for the first $m$ primes strictly larger than $\sqrt N$. For sufficiently large $N$,

$$
\boxed{H(N)=2m\quad\Longleftrightarrow\quad
p_jq_{m-j+2}\le N\text{ for all }2\le j\le m.}
$$

**Sufficiency.** Under these inequalities, the alternating cyclic sequence $p_1,q_m,p_2,q_{m-1},\ldots,p_m,q_1$ is a cycle in $T_N$. Each product $p_jq_{m-j+1}$ is bounded by $p_jq_{m-j+2}$; the remaining products are exactly those in the criterion (including $p_1q_m$ and the closing edge). Theorem 1 gives the claimed induced cycle.

**Necessity.** A cycle of length $2m$ must use all $m$ small primes and exactly $m$ primes larger than $\sqrt N$ and alternate between the two classes. Since the neighborhoods of large primes in the small primes are nested, any such cycle can replace its $m$ large primes, in increasing order, by the first $m$ large primes $q_1,\ldots,q_m$ without losing any edges.

If $p_jq_{m-j+2}>N$ for some $j\in[2,m]$, the $j-1$ large primes $q_{m-j+2},\ldots,q_m$ can only have neighbors among $p_1,\ldots,p_{j-1}$. Their total $2(j-1)$ incidences on an alternating Hamiltonian cycle would exhaust the degree-two capacity of those $j-1$ small primes. This would isolate a proper part of the cycle, impossible. QED.

This saturation theorem is an **arithmetic specialization of classical Hamiltonian threshold-graph criteria**, not a claim of a new general characterization of threshold graphs.

## Corollary: longest induced paths

Let $P(N)$ be the maximum number of vertices of an induced path in $G_N$. Then

$$
\boxed{P(N)\sim2\pi(\sqrt N).}
$$

Indeed, removing a vertex from an induced cycle of length $H(N)$ leaves an induced path on $H(N)-1$ vertices. For the reverse inequality, select a common prime witness for each of the $P(N)-1$ successive path edges. Inducedness forces these primes to be distinct, and consecutive witness primes have product at most $N$. Thus they form a path in $T_N$. Since primes above $\sqrt N$ cannot be consecutive on that path, there are at most $\pi(\sqrt N)+1$ large witnesses and at most $\pi(\sqrt N)$ small ones. Hence $P(N)\le2\pi(\sqrt N)+2$, proving the stated asymptotic.

## Arithmetic consequence and scope

For the deficit $D(N)=2\pi(\sqrt N)-H(N)$, Theorem 2 gives $D(N)=o(\pi(\sqrt N))$. Theorem 3 provides a precise prime-product test for $D(N)=0$. The unboundedness of $D(N)$ follows from Pintz's 2015 prime-gap theorem, as proved below. The **maximal growth order** of $D(N)$ remains undetermined in this dossier.

A simple lower bound is $D(N)\ge r(N)$, where $r(N)$ counts small primes $p\le\sqrt N$ with $pq_1>N$ and $q_1$ is the first prime above $\sqrt N$: such small primes cannot neighbor any large witness, so at most $m-r(N)$ large witnesses can occur on a cycle.

## Sources and verification

- [Mahadev and Peled, *Longest cycles in threshold graphs*](https://doi.org/10.1016/0012-365X(93)E0077-H), Discrete Mathematics 135 (1994), 169–176.
- [Harary and Peled, *Hamiltonian threshold graphs*](https://doi.org/10.1016/0166-218X(87)90050-3), Discrete Applied Mathematics 16 (1987), 11–15.
- [Rilwan, Sameema and Oli, *Non-Coprime Graph of Integers*](https://doi.org/10.14445/22315373/IJMTT-V66I2P513), 2020: ordinary cycles, not the above induced-cycle calculation.
- [Erdős and Sárközy, *On cycles in the coprime graph of integers*](https://doi.org/10.37236/1323), Electronic Journal of Combinatorics 4 (1997), R8, treats the complementary arithmetic adjacency.

The accompanying verifier constructs explicit prime-product induced cycles, audits the saturation inequalities and tests the upper bound in finite cases.
