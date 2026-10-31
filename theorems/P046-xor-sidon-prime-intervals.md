# Prime-restricted binary Sidon sets

**Status:** internally proved first-order bounds using known binary Sidon/APN constructions and the prime number theorem. Neither construction nor the general Sidon inequality is claimed new.

Write $\oplus$ for bitwise XOR. For each $m\ge2$, let

$$
\mathcal P_m=\{p\text{ prime}:2^m\le p<2^{m+1}\}
$$

and let $s_m$ be the greatest size of $A\subseteq\mathcal P_m$ such that **no four distinct elements** $a,b,c,d\in A$ satisfy

$$
a\oplus b\oplus c\oplus d=0.
$$

Equivalently, the bitwise XOR values $a\oplus b$ over unordered pairs of distinct elements of $A$ are all different.

## Theorem

As $m\to\infty$,

$$
\boxed{
\frac{2^{m/2}}{m}\ll s_m\le 2^{m/2}+O(1).
}
$$

In particular, $\log_2 s_m=(1/2+o(1))m$.

### Upper bound

All primes in $\mathcal P_m$ are odd. Their most significant binary bit is $1$ and their least significant bit is $1$. Therefore the XOR of two distinct such primes is a nonzero even integer below $2^m$. There are $2^{m-1}-1$ possible values. If $|A|=s_m$, all $\binom{s_m}{2}$ pairwise XOR values are distinct, so

$$
\binom{s_m}{2}\le2^{m-1}-1.
$$

Solving this inequality gives the asserted upper bound. $\square$

### Lower bound

Identify the odd integers in $[2^m,2^{m+1})$ with the vector space $G=\mathbb F_2^{m-1}$ by deleting the constant highest and lowest binary bits. This identification preserves four-term XOR-zero relations. Put $K=m-1$ and $k=\lfloor K/2\rfloor$.

A classical binary Sidon construction gives a subset $S\subseteq G$ of size $2^k$ with no four distinct elements summing to zero. For completeness, identify a $2k$-dimensional subspace with $\mathbb F_{2^k}^2$ and take

$$
S=\{(x,x^3):x\in\mathbb F_{2^k}\}.
$$

Indeed, for each $a\ne0$, the derivative $(x+a)^3+x^3=ax^2+a^2x+a^3$ has fibers of size at most two, and its two solutions in a nonempty fiber differ by $a$. Thus there are no two disjoint unordered pairs of elements of $S$ with equal sum. If $K$ is odd, embed this construction in a codimension-one subspace of $G$. Translation preserves the Sidon property.

Let $P\subset G$ be the images of the primes in $\mathcal P_m$. Averaging over all $t\in G$ gives

$$
\frac1{|G|}\sum_{t\in G}|(S+t)\cap P|
=\frac{|S||P|}{|G|}.
$$

Hence at least one translate meets $P$ in this many points; its intersection is again Sidon. By the prime number theorem,

$$
|P|=\pi(2^{m+1})-\pi(2^m)
\sim\frac{2^m}{m\log2},
$$

and therefore

$$
s_m\ge\frac{2^{\lfloor(m-1)/2\rfloor}}{2^{m-1}}|P|
\gg\frac{2^{m/2}}m.
$$

This proves the lower bound. $\square$

## Question

**Does there exist an absolute constant $c>0$ such that**

$$
s_m\ge c\,2^{m/2}
\quad\text{for all sufficiently large }m\ ?
$$

The theorem leaves a logarithmic multiplicative gap. It uses only the density of primes in the dyadic interval, not finer distribution of primes among translated binary Sidon configurations.

## Literature

- Czerwinski and Pott, *On large Sidon sets*, **Journal of Combinatorial Theory, Series A** 220 (2026), 106129, [DOI](https://doi.org/10.1016/j.jcta.2025.106129). The general binary Sidon/APN setting is established and has recently improved constructions.
- *Sidon sets, thin sets, and the nonlinearity of vectorial Boolean functions*, **Journal of Combinatorial Theory, Series A** 212 (2025), 106001, [DOI](https://doi.org/10.1016/j.jcta.2024.106001).
- The prime number theorem supplies the only analytic number theory used here; no new prime-density theorem is asserted.

The restriction to primes in a dyadic interval is the potential source of additional difficulty. Its priority relative to the literature on binary additive energy of primes and Sidon subsets of dense sets requires specialist checking; no historical novelty is certified.

The [finite certificate](../experiments/P046_prime_xor_sidon.py) checks the binary APN construction and verifies translated prime intersections for small $m$.
