# Binary carry graphs: exact edge count and connectivity

**Status:** internally proved elementary structural results. The Hamiltonian-path question is unresolved; historical originality is not certified.

For $m\ge2$, let $G_m$ be the simple graph on $\{1,\ldots,2^m-1\}$ with distinct $a,b$ adjacent when

$$
v_2\binom{a+b}{a}=1.
$$

By Kummer's theorem, this is equivalent to **exactly one carry** in binary addition of $a$ and $b$. Equivalently, writing $s_2(x)$ for the binary digit sum,

$$
a\sim b \quad\Longleftrightarrow\quad
s_2(a)+s_2(b)-s_2(a+b)=1.
$$

## Theorem

For every $m\ge4$:

1. $G_m$ is connected.
2. Exactly two vertices have degree one: $2^{m-1}-1$ and $2^m-1$. Their unique neighbors are, respectively, $2^{m-2}$ and $2^{m-1}$.
3. The edge count is

$$
\boxed{|E(G_m)|=\frac{(m+2)3^{m-2}-m}{2}.}
$$

### Proof: connectivity

Let $x$ be a vertex which is not a power of two, and let $2^j$ be its highest set binary bit. Adding $2^j$ to $x$ causes precisely one carry, in position $j$, because all higher bits of $x$ are zero. Consequently $x$ is adjacent to $2^j$.

If $0\le i<j\le m-1$ and $j-i\ge2$, the vertex $2^i+2^j$ is adjacent to *both* $2^i$ and $2^j$: doubling either set bit causes exactly one carry, which stops at a zero bit. Thus all powers of two lie in one component whenever the graph on $\{0,\ldots,m-1\}$ joining positions at distance at least two is connected. The latter graph is connected for $m\ge4$ (for example, $1-3-0-2$ connects the four initial positions, and every subsequent position is adjacent to position $0$). Every non-power-of-two vertex joins this component. $\square$

### Proof: degree-one vertices

For $x=2^j$, $0\le j<m-1$, a neighbor $y$ must have bit $j$ equal to one and bit $j+1$ equal to zero. There are $2^{m-2}$ such $y$, including $y=x$, which is excluded because the graph has no loops. Hence

$$
d(2^j)=2^{m-2}-1 \qquad(0\le j<m-1).
$$

For $j=m-1$, the condition is simply that bit $m-1$ of $y$ is one, again excluding $y=x$. Thus $d(2^{m-1})=2^{m-1}-1$. All these degrees exceed one for $m\ge4$.

For $x$ not a power of two, let $j$ be the highest set bit. The vertex $2^j$ is one neighbor. Suppose first that some bit $k$ with $0\le k\le j-2$ is zero in $x$. Then $2^j+2^k$ is another neighbor: its lower set bit creates no carry, whereas its upper one creates exactly one. If no such $k$ exists but bit $j-1$ is zero, necessarily $j\ge2$ and the vertex $2^{j-2}$ is a second neighbor, because the carry from position $j-2$ stops at position $j-1$.

In the remaining case every bit from $0$ to $j$ is one, so $x=2^{j+1}-1$. If $j\le m-3$, then $2^j+2^{j+2}$ is a second neighbor. If $j=m-2$ or $j=m-1$, any neighbor $y$ must have its least set bit at position $j$: a lower least set bit would trigger at least two consecutive carries through the block of ones. For $j=m-2$, adding bit $j+1$ to $y$ would produce a second carry; for $j=m-1$, no greater bit is permitted. Hence in either case the unique neighbor is $2^j$. These are precisely the two claimed leaves. $\square$

### Proof: edge count

Count *ordered* pairs $(a,b)$ with $0\le a,b<2^m$ and exactly one binary carry. When there is no incoming carry, each bit has three possible input pairs giving no outgoing carry and one input pair giving a carry. Once a carry has occurred, precisely one next-bit input pair, $(0,0)$, stops the carry; any other input pair produces a second carry.

If the unique carry is at the most significant bit, there are $3^{m-1}$ input pairs. Otherwise, choose its location among the first $m-1$ bit positions. The preceding and following no-carry positions contribute $3^{m-2}$ possibilities, giving $(m-1)3^{m-2}$ pairs. The total ordered count is therefore $(m+2)3^{m-2}$.

No such pair contains zero. The diagonal pairs satisfying the condition are exactly $(2^j,2^j)$, $0\le j<m$: doubling a positive integer creates as many binary carries as the integer has set bits. Removing these $m$ loops and dividing by two gives the stated edge count. $\square$

## An exact finite Hamiltonian-path witness

The following path in $G_4$ uses all 15 vertices:

$$
7,4,6,5,1,13,10,3,2,11,12,9,14,8,15.
$$

A 31-vertex path in $G_5$ is

$$
15,8,14,9,12,11,2,27,20,7,4,23,24,19,28,18,
29,1,13,10,3,26,21,6,5,25,22,17,30,16,31.
$$

The [independent finite verifier](../experiments/P042_kummer_carry_graph.py) checks both paths against binomial valuations (using binary digit sums and direct binomial arithmetic), the exact edge counts and the graph connectivity for $2\le m\le8$. These are finite witnesses, not an induction proof.

## Open question

**Does $G_m$ have a Hamiltonian path for every $m\ge4$?**

A positive answer necessarily produces a Hamiltonian path from $2^{m-1}-1$ to $2^m-1$, since both are leaves. A Hamiltonian cycle is impossible. The small cases $m=2,3$ are disconnected.

For comparison, the graph obtained by requiring *zero* carries is the bit-support disjointness graph: $a\sim b$ precisely when $a\,\&\,b=0$. The vertex $2^m-1$ is isolated there. Thus permitting one carry changes disconnectedness into connectedness for all $m\ge4$.

## Prior art

Kummer's carry theorem is classical; the digit-sum identity and its applications to binomial coefficients are not new. See:

1. A. Granville, *Arithmetic properties of binomial coefficients. I. Binomial coefficients modulo prime powers*, Canadian Mathematical Society Conference Proceedings **20** (1997), 253–276. [Author's publication record](https://dms.umontreal.ca/~andrew/1997.php), [exposition of Kummer's theorem](https://www.cecm.sfu.ca/organics/papers/granville/paper/binomial/html/node3-an.shtml).
2. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, Journal für die reine und angewandte Mathematik **44** (1852), 93–146.
3. The no-carry adjacency is a standard disjointness condition on binary supports, familiar from Boolean lattice and Kneser-type graph combinatorics.

A targeted search did not identify a theorem settling Hamiltonicity of the **one-carry** graph on $\{1,\ldots,2^m-1\}$. This does **not** certify novelty: graph Hamiltonicity under restricted digital arithmetic and binomial-valuation relations require further specialist screening.
