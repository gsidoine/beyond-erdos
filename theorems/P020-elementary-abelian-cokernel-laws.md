# P020 — Exact probabilities of elementary abelian p-adic Hankel cokernels

**29 October 2026. Status:** internally proved theorem, with exact independent finite checks and **specialist historical priority still unverified**. Its key finite-field input is **Yiasemides (2024), Theorem 2.4.4**, which is explicitly credited. Classical finite-field Hankel-rank counts are also used and are not new. This does **not** establish the limiting law for all groups.

## Setup and exact result

Let $p$ be prime, $n\ge1$, and let $H_n=(X_{i+j})_{0\le i,j<n}$, where $X_0,\ldots,X_{2n-2}$ are independent Haar-uniform elements of $\mathbb Z_p$. Put $C_n=\operatorname{coker}H_n$.

**Theorem.** For every $1\le k<n$,
$$
\boxed{
\Pr(C_n\simeq(\mathbb Z/p\mathbb Z)^k)
=(1-p^{-1})\bigl(p^{-(2k-1)}-p^{-(2k+1)}\bigr).
}\tag{1}
$$
At the boundary $k=n$,
$$
\boxed{\Pr(C_n\simeq(\mathbb Z/p\mathbb Z)^n)
=(1-p^{-1})p^{-(2n-1)}.}\tag{2}
$$
The trivial group has probability $1-p^{-1}$ for all $n\ge1$.

Therefore, for each fixed $k$, the elementary abelian $p$-group probability is **exactly independent of $n$** once $n>k$.

## Proof of conditional first-order Hankel lifting

Fix any residue class of the $2n-1$ input parameters modulo $p$ for which $\bar H_n$ has corank $k\ge1$. By [Yiasemides's finite-field Hankel kernel classification, specialized to square matrices](P020-hankel-kernel-product-research.md),
$$
\ker\bar H_n=A(z)\mathbb F_p[z]_{\le k-1}
$$
for some nonzero polynomial $A$ of degree at most $n-k$.

Use the ordered basis $A,Az,\ldots,Az^{k-1}$ of the kernel, and choose **integral polynomial-shift lifts** $f_i=\widetilde A z^i\in\mathbb Z_p[z]_{<n}$ ($0\le i<k$). Extend these $k$ vectors to an invertible matrix $P\in\mathrm{GL}_n(\mathbb Z_p)$. After congruence,
$$
P^\top H_nP=\begin{pmatrix}U&B\\B^\top&D\end{pmatrix},
$$
where $U$ is invertible modulo $p$, while $B,D$ vanish modulo $p$. The cokernel is therefore the cokernel of its Schur complement
$$
T=D-B^\top U^{-1}B,\qquad T\in p\,\mathrm{Sym}_k(\mathbb Z_p).
$$
Because $B\in pM$, we have
$$
T/p\equiv D/p\pmod p.
$$

Let $\ell_X$ be the coefficient functional with $\ell_X(z^s)=X_s$. In the **shift basis**, for every $i,j$,
$$
D_{ij}=\ell_X(\widetilde A^2 z^{i+j}).
$$
Thus $D$ itself is exactly a Hankel matrix, and $D/p\bmod p$ is a well-defined **Hankel** matrix (not an arbitrary symmetric one).

Write each retained parameter as $X_s=x_s^{(0)}+pY_s$ with $Y_s$ independent uniform modulo $p$. Conditional on the prescribed residues, the entries of $D/p\bmod p$ depend affinely on the independent $Y_s$ via the $2k-1$ linear functionals
$$
Y\longmapsto\ell_Y(A^2z^t),\qquad 0\le t\le2k-2.
$$
The $2k-1$ polynomials $A^2z^t$ are linearly independent over $\mathbb F_p$ (their degrees are distinct), hence the linear map from the $2n-1$ coefficients $Y_s$ to the $2k-1$ Hankel anti-diagonal entries is **surjective**. It follows that $T/p\bmod p$, conditional on **any fixed** corank-$k$ reduction, is **uniform among all $k\times k$ Hankel matrices over $\mathbb F_p$**. Note that the constant affine shift in $D/p$ is also Hankel; it does not affect this uniformity.

The cokernel is elementary abelian of rank $k$ precisely when every nonunit Smith factor of $H_n$ has valuation one, equivalently when $T/p\bmod p$ is invertible. The classical finite-field square Hankel-rank enumeration implies that a uniform $k\times k$ Hankel matrix is invertible with probability $1-p^{-1}$, for every $k\ge1$. Thus
$$
\Pr(C_n\simeq(\mathbb Z/p)^k\mid\operatorname{corank}(\bar H_n)=k)=1-p^{-1}.\tag{3}
$$

Finally the *classical* corank tail probabilities are
$$
\Pr(\operatorname{corank}(\bar H_n)\ge j)=p^{-(2j-1)}\quad(1\le j\le n).
$$
Subtract successive tails for $k<n$ and use the last tail for $k=n$. Multiplication by (3) proves (1) and (2). $\square$

**Boundary case:** $n=1$ is also immediate from $H_1=(X_0)$, so the result is valid for every $n\ge1$.

## Exact independent checks, not merely simulations

The [dependency-free mod-$p^2$ exact enumerator](../experiments/P020_elementary_cokernel_mod_p2.py) scans every possible anti-diagonal sequence modulo $p^2$, builds a kernel basis of $\bar H_n$ by independent modular elimination, and tests the invertibility of its induced first-order form. The checks include all elementary group ranks, even when $k>2$.

| $p$ | $n$ | $k$ | Exact group count / all matrices | Formula |
|---:|---:|---:|---:|---:|
| 2 | 3 | 3 | 16/1024 | 1/64 |
| 2 | 4 | 3 | 192/16384 | 3/256 |
| 2 | 4 | 4 | 64/16384 | 1/256 |
| 3 | 3 | 3 | 162/59049 | 2/729 |

The same script checks all $0\le k\le n$ at $p=2,n=2,3,4$ and $p=3,n=2,3$, including agreement with the earlier one- and two-generator formulas.

## What this theorem does and does not settle

The formula yields probabilities for every fixed elementary abelian $p$-group, not just one- or two-generator groups. It also explains **why symmetric-Haar lifting fails at $k\ge3$**: only $2k-1$ Hankel anti-diagonal degrees of freedom occur instead of $k(k+1)/2$ independent symmetric entries.

However the Schur-complement correction $B^\top U^{-1}B$ is generally nonzero at higher orders. The argument controls $T/p\bmod p$ but **does not** prove that $T/p$ is exactly Haar-uniform in the $p$-adic Hankel subspace modulo all $p^j$. Therefore probabilities for general three-generator groups with exponent above $p$, and the full $n\to\infty$ group distribution, remain unresolved.

## Sources and priority

- [Yiasemides (2024), *The variance and correlations of the divisor function in F_q[T], and Hankel matrices*, Theorem 2.4.4 and Remark 2.4.6](https://doi.org/10.1007/s40687-023-00418-7): **published finite-field kernel classification**, not original.
- [Dwivedi–Grinberg (2022), *On the rank of Hankel matrices over finite fields*](https://doi.org/10.1016/j.laa.2022.02.014): classical finite-field Hankel rank counts and earlier references, not original.
- [Earlier internally proved cyclic/two-generator probability laws](P020-padic-hankel-cyclic-and-rank-two-laws.md): stronger than elementary-abelian statements for at most two generators, but do not extend in the same way to $k\ge3$.

No claim is made that the particular group-specific formula (1) has never appeared before. It requires specialized historical-priority review of random local Hankel/catalecticant Smith forms before being advertised as novel or publishable.
