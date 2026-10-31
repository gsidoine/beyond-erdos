# A universal positive lower bound for coprime matching resilience

**Status:** internally proved. The probabilistic-number-theoretic inputs are classical, and historical originality of their application to P040 has not been established.

Let $B_n$ be the balanced bipartite graph between the $n$ positive even integers at most $2n$ and the $n$ positive odd integers at most $2n$, with edges joining coprime numbers. As in [P040](../problems/graph-theory/P040-coprime-matching-local-resilience.md), let

$$
\rho_n=
\min_{\substack{F\subseteq E(B_n)\\B_n-F\text{ has no perfect matching}}}
\max_{v\in V(B_n)}
\frac{d_F(v)}{d_{B_n}(v)}.
$$

## Theorem (two-sided nontrivial resilience bounds)

$$
\boxed{
\frac{16}{\pi^2}-\frac32
\le\liminf_{n\to\infty}\rho_n
\le\limsup_{n\to\infty}\rho_n
\le\frac5{12}.
}
$$

The lower constant is $16/\pi^2-3/2=0.1211389\ldots>0$.
The upper bound follows from the [fractional-sieve reduction and exact three-prime certificate](P040-fractional-sieve-variational.md). The earlier integral constructions remain in the [finite-prime Hall-cut note](P040-finite-prime-hall-obstructions.md).
Neither convergence of $\rho_n$ nor optimality of either constant is asserted.

### Lemma 1: edge density

$$
|E(B_n)|=\left(\frac8{\pi^2}+o(1)\right)n^2.
$$

**Proof.** Writing an even vertex as $2i$, and using Möbius inversion over odd divisors of $2i$ and the odd vertex $2j-1$, gives

$$
|E(B_n)|
=\sum_{\substack{d\ge1\\d\text{ odd}}}\mu(d)
  \left\lfloor\frac nd\right\rfloor
  \left(\frac nd+O(1)\right)
=n^2\sum_{\substack{d\ge1\\d\text{ odd}}}\frac{\mu(d)}{d^2}
+O(n\log n).
$$

The Euler product over odd primes equals
$\prod_{p\ge3}(1-p^{-2})=(6/\pi^2)/(1-1/4)=8/\pi^2$. QED.

### Lemma 2: degree density and its fourth inverse moment

For $v$ in either part define

$$
\theta(v)=\prod_{\substack{p\mid v\\p\text{ odd prime}}}
\left(1-\frac1p\right).
$$

Uniformly for $v\le2n$, its degree in the other part is

$$
d_{B_n}(v)=n\theta(v)+O(2^{\omega(v)}),
\qquad 2^{\omega(v)}=n^{o(1)}.
$$

Moreover for each of the even and odd vertex classes,

$$
\boxed{
\frac1n\sum_{v}\theta(v)^{-4}\le C_4+o(1),
\qquad
C_4:=\prod_{p\ge3}
\left(1+\frac{(1-1/p)^{-4}-1}{p}\right)<6.
}
$$

**Proof.** The degree identity follows from inclusion–exclusion of the odd prime divisors of $v$. For the moment bound, set
$\eta(p)=(1-1/p)^{-4}-1>0$ for odd primes, extending $\eta$ multiplicatively to odd squarefree integers. Then

$$
\theta(v)^{-4}=
\sum_{\substack{d\mid v\\d\text{ odd squarefree}}}\eta(d).
$$

For even $v=2i$, the proportion divisible by an odd $d$ is at most $1/d$. For odd $v=2i-1$, that proportion is $1/d+O(1/n)$. Since $\eta(p)\ll1/p$ and $\sum_{d\le2n}\eta(d)=n^{o(1)}$, summing the divisor expansion gives the stated bound on both sides.

To verify the explicit bound $C_4<6$ without a numerical Euler-product assumption, note that

$$
1+\frac{\eta(3)}3=\frac{113}{48},\qquad
1+\frac{\eta(5)}5=\frac{1649}{1280},
$$

and $\eta(p)\le7/p$ for every prime $p\ge7$. Hence

$$
C_4\le
\frac{113}{48}\frac{1649}{1280}
\exp\!\left(7\sum_{\substack{m\ge7\\m\ \mathrm{odd}}}\frac1{m^2}\right)
\le
\frac{113}{48}\frac{1649}{1280}
\exp\!\left(7\left(\frac1{49}+\frac1{14}\right)\right)
<6.
$$

The tail bound compares the decreasing sequence $1/(7+2j)^2$ with its integral. QED.

### Proof of the theorem: Hall obstructions of every size

Write

$$
q=\frac8{\pi^2},\qquad a=1-q,\qquad
c=\frac12-2a=\frac{16}{\pi^2}-\frac32.
$$

In particular $0<c<1/5$ and $a<1/5$.

Fix an edge-deletion set $F$ for which $B_n-F$ has no perfect matching, and write
$t=\max_v d_F(v)/d_{B_n}(v)$. By Hall's theorem there is a nonempty $S$ in the even vertex class whose neighborhood in $B_n-F$ has fewer than $|S|$ vertices. Choose an odd-vertex set $Y$ of size $n-|S|+1$ avoiding every surviving neighbor of $S$. **Every original coprime edge between $S$ and $Y$ was deleted.** Put $s=|S|/n$ and $y=|Y|/n=1-s+1/n$.

**Case 1: $2/5\le s\le3/5$.**
By Lemma 1, the entire graph contains $(a+o(1))n^2$ nonedges. Thus the number of original coprime edges between $S$ and $Y$ is at least

$$
(sy-a-o(1))n^2.
$$

Since all of those edges were deleted, and every vertex has degree at most $n$,

$$
t\ge \max\left\{y-\frac{a+o(1)}s,\ 
s-\frac{a+o(1)}y\right\}.
$$

The error is uniform on this middle interval. For $s\in[2/5,1/2]$, the first expression tends to
$f(s)=1-s-a/s$, a concave function whose minimum on this interval is attained at an endpoint. Its values are

$$
f(1/2)=\frac12-2a=c,\qquad
f(2/5)=\frac35-\frac52a\ge c
$$

because $a\le1/5$. For $s\in[1/2,3/5]$ the second expression yields the symmetric estimate. Consequently $t\ge c-o(1)$.

**Case 2: $0<s<2/5$.**
Fix any $\varepsilon\in(0,c)$ and set $\tau=c-\varepsilon$. Lemma 2 and Markov's inequality show that, among the even vertices, the number satisfying

$$
\theta(v)\le\frac{s}{1-\tau}
$$

is at most

$$
(C_4+o(1))n
\left(\frac{s}{1-\tau}\right)^4.
$$

This is strictly less than $sn$ uniformly over $s\le2/5$, because $C_4<6$ and

$$
6\frac{(2/5)^3}{(1-\tau)^4}
<
6\frac{(2/5)^3}{(4/5)^4}
=\frac{15}{16}<1.
$$

Therefore some $v\in S$ has $\theta(v)>s/(1-\tau)$.

If $s\ge n^{-1/4}$, the uniform error $2^{\omega(v)}=n^{o(1)}$ in Lemma 2 is $o(sn)$, so

$$
d_{B_n}(v)\ge \frac{sn}{1-\tau}-o(sn).
$$

At most $|S|-1<sn$ of its original neighbors can lie outside $Y$; every neighbor in $Y$ is deleted. Thus

$$
\frac{d_F(v)}{d_{B_n}(v)}
\ge1-\frac{sn}{d_{B_n}(v)}
\ge\tau-o(1).
$$

If $s<n^{-1/4}$, the standard totient lower bound yields
$d_{B_n}(v)\gg n/\log\log(3n)$ for **every** vertex, so the same argument gives

$$
t\ge1-O\left(\frac{\log\log(3n)}{n^{1/4}}\right)=1-o(1).
$$

**Case 3: $3/5<s\le1$.**
Exchange the even and odd vertex classes and use $Y$ as the smaller Hall-side set. Its proportion $y=1-s+1/n$ is at most $2/5+1/n$. The fourth-moment argument of Case 2 (with this harmless $O(1/n)$ enlargement) applies to an odd vertex of $Y$: its coprime neighbors in $S$ were all deleted, and the complement of $S$ contains $n-|S|=|Y|-1$ vertices. Thus again $t\ge\tau-o(1)$.

In all three cases, $t\ge c-\varepsilon-o(1)$ uniformly. Let $n\to\infty$ and then $\varepsilon\downarrow0$ to obtain

$$
\liminf_{n\to\infty}\rho_n\ge c.
$$

The matching upper bound in the displayed theorem is proved in the cited finite-prime Hall-cut note. QED.

## Interpretation and literature

The positivity result follows from a simple but useful combination: a global positive density of coprime edges controls *medium-sized* Hall cuts, while a uniform negative fourth moment of the odd-prime totient factor controls *small-sized* cuts. This does not supply a sharp Hall expansion constant.

- Pomerance, [*Coprime Matchings*](https://arxiv.org/abs/2111.07157), preprint (2021), published in *Integers* **22** (2022), #A2, proves matching existence results of a different type.
- Sah–Sawhney, [*Enumerating coprime permutations*](https://doi.org/10.1112/mtk.12159), *Mathematika* (2022), uses complementary arithmetic matching and enumeration methods.
- The elementary coprime-pair density follows from the Euler product for $\zeta(2)$, and the reciprocal-totient moment bound from a standard nonnegative divisor expansion.

**Priority caution:** This proof is internally established, not externally refereed; no originality is claimed for the classical ingredients or the resulting constant without theorem-level literature verification.
