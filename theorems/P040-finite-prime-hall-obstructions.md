# Finite-prime Hall obstructions to coprime matching resilience

**Status:** internally proved counterexample to the former P040 half-resilience conjecture. Arithmetic conditions and finite rational certificates are explicit; historical originality is not certified.

Let $B_n$ be the balanced bipartite graph with even vertices $E_n=\{2,4,\ldots,2n\}$, odd vertices $O_n=\{1,3,\ldots,2n-1\}$, and adjacency $\gcd(e,o)=1$. Its degree-relative local matching resilience is

$$
\rho_n=\min_{\substack{F\subseteq E(B_n)\\ B_n-F\text{ has no perfect matching}}}
\ \max_{v\in V(B_n)}\frac{d_F(v)}{d_{B_n}(v)}.
$$

## The finite-prime obstruction theorem

Fix a finite set $P$ of **odd primes**. For $T\subseteq P$ define its biased prime-support weight

$$
\mu_P(T)=\prod_{p\in T}\frac1p
\prod_{p\in P\setminus T}\left(1-\frac1p\right).
$$

For a family $\mathcal A\subseteq2^P$, write
$\mu_P(\mathcal A)=\sum_{T\in\mathcal A}\mu_P(T)$.
Define its conditional coprime-neighbor density at prime-support type $S$ by

$$
Q_P(\mathcal A\mid S)=
\frac{\sum_{\substack{T\in\mathcal A\\T\cap S=\varnothing}}\mu_P(T)}
{\sum_{T\cap S=\varnothing}\mu_P(T)}.
$$

**Theorem.** Let $\mathcal A,\mathcal B\subseteq2^P$ have
$\mu_P(\mathcal A)+\mu_P(\mathcal B)>1$. Then

$$
\boxed{\limsup_{n\to\infty}\rho_n\le
\max\left\{
\max_{S\in\mathcal A}Q_P(\mathcal B\mid S),
\max_{T\in\mathcal B}Q_P(\mathcal A\mid T)
\right\}.}
$$

**Proof.** In each bipartition class, retain the vertices whose set of prime divisors belonging to $P$ lies in $\mathcal A$, respectively $\mathcal B$. Call these vertex sets $X\subseteq E_n$ and $Y\subseteq O_n$. By periodicity modulo $\prod_{p\in P}p$,

$$
|X|=(\mu_P(\mathcal A)+o(1))n,\qquad
|Y|=(\mu_P(\mathcal B)+o(1))n.
$$

Therefore $|X|+|Y|>n$ for all large $n$. Delete every edge between $X$ and $Y$. In the resulting graph the neighborhood of $X$ is contained in $O_n\setminus Y$, which has fewer than $|X|$ vertices. Hall's theorem rules out a perfect matching.

It remains to bound the deleted *relative* degree. For each $v\le2n$, the proportion of its coprime neighbors in a prescribed union of exact $P$-support classes is, uniformly over $v$,

$$
Q_P(\mathcal A\mid \{p\in P:p\mid v\})+o(1)
$$

when the other side is selected by $\mathcal A$. To verify uniformity, apply inclusion–exclusion to the prime factors of $v$ outside the fixed set $P$, separately in the finitely many residue classes modulo $\prod P$. The absolute error is $O_P(2^{\omega(v)})=n^{o(1)}$, while the total coprime neighborhood has size $\gg n/\log\log(3n)$ uniformly in $v\le2n$. The quotient error is thus $o(1)$. The same argument holds for the even and odd bipartition classes because all primes in $P$ are odd.

For vertices in $X$ or $Y$, the deleted fractions are bounded by the two maxima in the statement, up to $o(1)$. All other vertices lose no edges. QED.

## A three-prime disproof of the half-resilience conjecture

Take $P=\{3,5,7\}$ and
$\mathcal A=\mathcal B=2^P\setminus\{\varnothing\}$,
so a selected integer is divisible by at least one of $3,5,7$. Then

$$
\mu_P(\mathcal A)=1-\frac23\frac45\frac67
=\frac{19}{35}>\frac12.
$$

For any nonempty $S$, its coprime neighbors cannot be divisible by any $p\in S$. The largest conditional probability of belonging to $\mathcal A$ occurs when $S=\{7\}$, giving

$$
Q_P(\mathcal A\mid\{7\})
=1-\frac23\frac45=\frac7{15}.
$$

Therefore

$$
\boxed{\limsup_{n\to\infty}\rho_n\le\frac7{15}<\frac12.}
$$

This **disproves** the original P040 conjecture $\rho_n\to1/2$. It also invalidates any suggestion that the general randomized $1/2$-deletion obstruction is necessarily sharp for this arithmetic graph.

## Stronger exact finite-prime certificates

Encode support $S\subseteq\{p_0,\ldots,p_{k-1}\}$ by the integer bitmask
$\sum_{i:p_i\in S}2^i$, with primes in the specified order.

For the symmetric construction $\mathcal A=\mathcal B$ the theorem yields:

| Ordered prime set $P$ | Selected support masks $\mathcal A$ | Mass $\mu_P(\mathcal A)$ | Maximum $Q_P(\mathcal A\mid S)$ |
|---|---|---|---|
| $3,5,7$ | $1,2,3,4,5,6,7$ | $19/35$ | $7/15$ |
| $3,5,7,11$ | $1,2,3,4,5,6,7,11,13$ | $116/231$ | $71/165$ |
| $3,5,7,11,13$ | $1,2,3,4,5,6,7,13,14,15,17,18,19,20,21,22,25,29,31$ | $683/1365$ | $914/2145$ |
| $3,5,7,11,13,17$ | $H\cup(H+32)\cup\{19,43\}$, where $H$ is defined below | $18233/36465$ | $5163/12155$ |

For the six-prime row, put
$$
H=\{1,2,3,4,5,6,7,13,14,15,17,18,20,21,22,23,27,29,30,31\}.
$$
The expression $H+32$ means $\{h+32:h\in H\}$; the bitmask convention includes the sixth prime $17$ in bit $32$. The resulting family has $42$ support masks, mass $18233/36465>1/2$, and its largest conditional deletion fraction is $5163/12155$, attained at support mask $4$.

All four masses are strictly greater than $1/2$, and the table entries are **exact rational finite sums**, independently checked by [the certificate program](../experiments/P040_sieve_hall_obstructions.py). No global optimality of any listed family is asserted. In particular,

$$
\boxed{\limsup_{n\to\infty}\rho_n\le\frac{5163}{12155}
=0.424763\ldots.}
$$

## Surviving research question: arithmetic Hall resilience

The correct unresolved problem is to determine the asymptotic behavior of $\rho_n$, not to prove the disproved half-resilience conjecture. An associated well-defined finite-prime variational upper bound is

$$
\alpha_{\mathrm{sieve}}=
\inf_{\substack{P\text{ finite set of odd primes}\\
\mathcal A,\mathcal B\subseteq2^P\\
\mu_P(\mathcal A)+\mu_P(\mathcal B)>1}}
\max\left\{
\max_{S\in\mathcal A}Q_P(\mathcal B\mid S),
\max_{T\in\mathcal B}Q_P(\mathcal A\mid T)
\right\}.
$$

The theorem proves $\limsup_n\rho_n\le\alpha_{\mathrm{sieve}}\le5163/12155$.
**Neither convergence of $\rho_n$ nor equality with $\alpha_{\mathrm{sieve}}$ is established.** A matching lower bound would require quantitative Hall expansion beyond finite-prime-pattern obstructions.

The extremal structure links degree-relative matching resilience to disjointness in nonuniform product measures on prime-support families. This is a substantive connection, but the general literature on biased intersecting families is extensive: see the $p$-biased intersecting-family extremal tradition and [Wu–Feng (2026)](https://arxiv.org/abs/2606.26521), alongside [Pomerance, *Coprime Matchings* (2021)](https://arxiv.org/abs/2111.07157). None of these sources is asserted to prove the particular bounds above or the remaining resilience problem. Historical novelty is **unverified**.
