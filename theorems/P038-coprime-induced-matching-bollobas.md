# P038 — Coprime induced matchings and arithmetic set pairs

**Status:** internally proved quantitative theorem. The extremal refinement remains an open **candidate**, and historical novelty of the arithmetic specialization is unverified.

Let $C_N$ be the graph on $[N]$ with an edge $xy$ exactly when $\gcd(x,y)=1$. Write $M(N)$ for its maximum induced matching size: the maximum $m$ for which $2m$ distinct integers $a_1,b_1,\ldots,a_m,b_m\in[N]$ obey

$$
\gcd(a_i,b_i)=1,\qquad
\gcd(x,y)>1\quad
\text{for }x\in\{a_i,b_i\},\ y\in\{a_j,b_j\},\ i\ne j.
$$

Let $p_i$ be the $i$-th prime and define the inverse primorial index

$$
T(N)=\max\left\{t:\prod_{i=1}^t p_i\le N^2\right\}.
$$

## Theorem: induced matching asymptotics with a sublinear logarithmic error

For sufficiently large $N$,

$$
\boxed{T(N)\log 2-O(\sqrt{T(N)\log T(N)})
\le\log M(N)\le T(N)\log 2.}
$$

Consequently,

$$
\boxed{\log M(N)\sim 2\log 2\,\frac{\log N}{\log\log N}.}
$$

### Upper bound: Bollobás's inequality

Define the prime supports $A_i=\{p:p\mid a_i\}$ and $B_i=\{p:p\mid b_i\}$. Then $A_i\cap B_i=\varnothing$ and $A_i\cap B_j\ne\varnothing$ for $i\ne j$. Bollobás's classical set-pair inequality implies

$$
\sum_{i=1}^m \binom{|A_i|+|B_i|}{|A_i|}^{-1}\le1.
$$

Since $a_ib_i\le N^2$, its squarefree prime-support product is at most $N^2$. The least product of $s$ distinct primes is the $s$-th primorial; hence $|A_i|+|B_i|\le T(N)$. It follows that $m\le2^{T(N)}$ (more precisely, $m\le\binom{T(N)}{\lfloor T(N)/2\rfloor}$).

### Lower bound: equal-sized prime blocks

Abbreviate $T=T(N)$ and choose an even integer $B$ with $B\asymp\sqrt{T\log T}$, with $2B<T$. Set

$$
t=B\left\lfloor\frac{T-B}{B}\right\rfloor,
$$

so $T-2B<t\le T-B$ and $t$ is a multiple of $B$. Divide the first $t$ primes into consecutive blocks of size $B$.

Choose exactly $B/2$ primes from each block and put the selected primes into $S$, the unselected primes into its complement $\overline S$. Define

$$
a_S=\prod_{p\in S}p,\qquad b_S=\prod_{p\in\overline S}p.
$$

Let $P_t=\prod_{i=1}^t p_i$. For any such balanced choice,

$$
\left|\log\frac{a_S}{b_S}\right|
\le\frac B2\sum_{\text{blocks}}\log\frac{p_{\max}}{p_{\min}}
\le\frac B2\log p_t.
$$

The last inequality holds because the block ranges are disjoint intervals of consecutive primes, and the sum of their log-increments is bounded by the total log-increment from $p_1$ to $p_t$.

Since $T-t\ge B$ and $P_T\le N^2$,

$$
\log\frac{N^2}{P_t}\ge\sum_{j=t+1}^T\log p_j
\ge B\log p_{t+1}
\ge B\log p_t.
$$

Therefore $a_S,b_S\le N$. They are coprime because their prime supports are disjoint.

Every choice has $|S|=t/2$. For any two distinct noncomplementary such sets $S,S'$, all four sets

$$
S\cap S',\quad S\cap\overline S',\quad
\overline S\cap S',\quad\overline S\cap\overline S'
$$

are nonempty: equality or complementarity is the only obstruction for two equal-sized subsets. Consequently **all four cross-gcds exceed one**. Taking one choice from each complementary pair gives an induced matching of size

$$
m=\frac12\binom{B}{B/2}^{\,t/B}.
$$

The elementary estimate $\log\binom{B}{B/2}=B\log2-O(\log B)$ now implies

$$
\log M(N)\ge T\log2-O\left(B+\frac{T\log B}{B}\right)
=T\log2-O(\sqrt{T\log T}).
$$

Finally the prime number theorem yields $T(N)\sim2\log N/\log\log N$. QED.

## Why the remaining question is nontrivial

The logarithmic upper-lower gap above is $O(\sqrt{T\log T})$, far smaller than $T$ but still much larger than $\log T$. It is not proved here that one can achieve a polynomial fraction of the Bollobás upper bound, nor that near-extremizers must arise from complementary prime-support partitions.

**Research question:** Determine $M(N)$ to a multiplicative subexponential factor sharper than the displayed bound, in particular whether

$$
\log M(N)=\log\binom{T(N)}{\lfloor T(N)/2\rfloor}+O(\log T(N)).
$$

The displayed $O(\log T)$ assertion is **conjectural**, not part of the theorem.

## Historical context

The main combinatorial ingredient is the classical Bollobás (1965) set-pair theorem; its extremal example already consists of complementary subsets. See Füredi–Gyárfás–Király, [*Problems and results on 1-cross intersecting set pair systems*](https://doi.org/10.1017/S0963548323000044), *Combinatorics, Probability and Computing* (2023), and [*Variations on the Bollobás set-pair theorem*](https://doi.org/10.1016/j.ejc.2024.103983) (2024). The coprime graph on $[N]$ is a classical object, studied in, e.g., Erdős–Sárközy, *On cycles in the coprime graph of integers* (1997), https://www.combinatorics.org/ojs/index.php/eljc/article/download/v4i2r8/pdf/.

Targeted searches for induced-matchings in this precise integer coprime graph did not identify the stated arithmetic asymptotic. Such a search is not a historical novelty certificate. The theorem is a comparatively short synthesis of standard set-pair inequality and elementary prime-product balancing; publication priority is unresolved.
