# Additive complete mappings and multiplicative image defects

**Status:** internally proved. The additive complete-mapping condition and multiplicative orthomorphisms have established prior art; historical priority of the combined extremum is unverified.

For an odd prime $p$ define

$$
D(p)=\max_f\left|\{xf(x):x\in\mathbb F_p\}\right|,
$$

where the maximum is over permutations $f$ of $\mathbb F_p$ for which $x\mapsto x+f(x)$ is also a permutation. Such maps $f$ are additive *complete mappings*.

## Theorem

For every prime $p\ge5$,

$$
\boxed{D(p)\le p-2.}
$$

Equality holds for $p=5,7,11,13$. For $p=3$, $D(3)=2$.

### Proof

Let $f$ be a complete mapping, $g(x)=x+f(x)$, and $h(x)=xf(x)$. Since $f$ and $g$ both permute $\mathbb F_p$,

$$
\sum_x(x+f(x))^2=\sum_x x^2
=\sum_xf(x)^2.
$$

Consequently

$$
2\sum_xxf(x)=-\sum_x x^2=0,
$$

the last equality holding for every prime $p\ge5$. Thus

$$
\sum_{x\in\mathbb F_p}h(x)=0. \tag{1}
$$

Suppose $f(0)\ne0$. Let $a\ne0$ be the unique solution of $f(a)=0$. Then $h(0)=h(a)=0$, so $h$ has at most $p-1$ distinct values. If it had exactly $p-1$, its nonzero values would be all elements of $\mathbb F_p^\times$ except one value $v\ne0$, each occurring once. Therefore $\sum_xh(x)=-v\ne0$, contradicting (1).

Suppose now $f(0)=0$. For $x\ne0$, $h(x)\ne0$. Since both $x$ and $f(x)$ permute the nonzero field elements,

$$
\prod_{x\ne0}h(x)
=\left(\prod_{x\ne0}x\right)
\left(\prod_{x\ne0}f(x)\right)
=(-1)^2=1. \tag{2}
$$

If $h$ were a permutation, (2) would instead give $-1$, a contradiction. Thus $h$ has at most $p-1$ distinct values. If it had exactly $p-1$, the multiset of $h(x)$ for $x\ne0$ would contain every nonzero field element except one $v$, with exactly one other value $u$ repeated. By (2),

$$
1=\left(\prod_{y\ne0}y\right)\frac uv=-\frac uv,
\qquad\text{hence}\quad u=-v.
$$

But then

$$
\sum_xh(x)=-v+u=-2v\ne0,
$$

contradicting (1). Hence $h$ assumes at most $p-2$ distinct values in both cases. $\square$

The following exact witnesses attain $p-2$; in each row, the entries list $f(0),\ldots,f(p-1)$:

| $p$ | Complete mapping $f$ | Distinct products |
|---:|---|---:|
| 5 | $(0,1,2,3,4)$ | 3 |
| 7 | $(0,4,6,1,2,5,3)$ | 5 |
| 11 | $(8,4,7,1,10,2,5,6,9,3,0)$ | 9 |
| 13 | $(0,1,10,3,4,6,12,2,8,5,7,9,11)$ | 11 |

All witnesses and the $p=3$ exception are checked by the [standard-library exact verifier](../experiments/P045_additive_multiplicative_permutations.py). Optimality for the listed primes follows from the general upper bound, not from finite optimization.

## Question

**Does $D(p)=p-2$ hold for every prime $p\ge5$?** More generally, construct families of additive complete mappings whose multiplicative image misses only two elements. The theorem leaves their existence for arbitrary prime order unresolved.

## Previous work

- A. Bors and Q. Wang, *Compositions and parities of complete mappings and of orthomorphisms*, **Journal of Combinatorial Theory, Series A** 195 (2023), 105723, [DOI](https://doi.org/10.1016/j.jcta.2022.105723).
- A. Muratović-Ribić and S. Surdulli, *On strong complete monomials and its multiplicative analogue over finite fields*, **Sarajevo Journal of Mathematics** 16 (2020), 137–144, [DOI](https://doi.org/10.5644/SJM.16.01.10).
- M. E. Zieve, *Permutation polynomials induced from permutations of subfields, and some complete sets of mutually orthogonal Latin squares*, [author's page](https://websites.umich.edu/~zieve/papers/pp-complete.html).

The present condition asks to maximize the **image cardinality** of $xf(x)$ while $f$ and $x+f(x)$ are permutations. This is not the same as requiring a multiplicative complete mapping, which cannot exist on the cyclic group $\mathbb F_p^\times$ of even order. A theorem-level search of near-complete mappings remains necessary. No originality claim is made.
