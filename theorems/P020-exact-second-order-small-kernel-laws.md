# P020 — Exact two-layer laws with one or two second-order generators

**Status: internally proved conditional second-order lifting theorem**, based on the existing published finite-field Hankel rank enumeration and the previously established P020 first-order Hankel lifting theorem. Historical priority of this *assembled* formula remains unverified. The full three-generator exponent-$p^2$ classification and limiting distribution are **not** claimed.

## Setup

Let $H_n=(X_{i+j})_{0\le i,j<n}$ with $2n-1$ independent Haar $\mathbb Z_p$ entries, and put $C_n=\operatorname{coker}H_n$.

For $1\le k\le n$ write

$$
\rho_{n,k}=\Pr(\dim_{\mathbb F_p}\ker(\bar H_n)=k)
=\begin{cases}
p^{-(2k-1)}-p^{-(2k+1)},&k<n,\\
p^{-(2n-1)},&k=n.
\end{cases}
$$

This is **classical** finite-field Hankel rank counting, not a new theorem.

## Theorem: exact exponent-two group probabilities with at most two $p^2$ factors

For every prime $p$, $n\ge2$, $1\le k\le n$ and $j\in\{1,2\}$ satisfying $j<k$, we have

$$
\boxed{
\Pr\!\left(C_n\simeq
(\mathbb Z/p\mathbb Z)^{k-j}
\oplus(\mathbb Z/p^2\mathbb Z)^j\right)
=\rho_{n,k}
\left(p^{-(2j-1)}-p^{-(2j+1)}\right)(1-p^{-1}).
}\tag{1}
$$

In particular, for **three generators**, for all $n\ge4$, put $\rho_3=p^{-5}-p^{-7}$. Then

$$
\Pr(C_n\simeq(\mathbb Z/p)^2\oplus\mathbb Z/p^2)
=\rho_3(p^{-1}-p^{-3})(1-p^{-1})
$$

and

$$
\Pr(C_n\simeq\mathbb Z/p\oplus(\mathbb Z/p^2)^2)
=\rho_3(p^{-3}-p^{-5})(1-p^{-1}).
$$

For $n=3$, the same conditional factors hold but $\rho_{3,3}=p^{-5}$.

These are **exact dimension-stable probabilities** once $n>k$, not mere asymptotic estimates.

### Lemma: a rank-one or rank-two residual kernel has a uniform second-order form

Fix the entire first residue vector $X\bmod p$, with $\bar H_n$ of corank $k$. Choose a fixed integral basis of the mod-$p$ radical and split off the invertible $(n-k)$-block by a Schur complement. As in [the first-order theorem](P020-elementary-abelian-cokernel-laws.md), the remaining matrix is $T=pS$ for $S\in\mathrm{Sym}_k(\mathbb Z_p)$; conditional on $X\bmod p$, $\bar S=S\bmod p$ is Haar-uniform among **Hankel $k\times k$ matrices**.

Further condition on the complete first two $p$-adic digits of $X$ (so that $\bar S$ is fixed) and suppose $\operatorname{corank}(\bar S)=j\in\{1,2\}$. Split off the invertible $(k-j)$-block of $\bar S$ and divide the remaining Schur complement by $p$, producing a $j\times j$ matrix $W$ over $\mathbb Z_p$.

**Claim:** conditional on these first two digits, $W\bmod p$ is uniform in $\mathrm{Sym}_j(\mathbb F_p)$.

**Proof.** The third $p$-adic input digits are independent uniform coefficients $Z_0,\ldots,Z_{2n-2}\in\mathbb F_p$. Choose any lifts $v_1,\ldots,v_j\in\mathbb Z_p^n$ of the $j$ independent vectors obtained by mapping $\ker\bar S$ into the original radical $\ker\bar H_n$. A change in the third input digit by $\Delta Z$ changes $H_n$ by $p^2 H(\Delta Z)$ and hence changes $W\bmod p$ by the **restriction of $H(\Delta Z)$ to the $j$-dimensional residual radical**. The first Schur complement divides by $p$, the second divides by another $p$; the variations of the off-diagonal blocks and the invertible block enter only at higher order.

Writing $f_i(z)=\sum_{a=0}^{n-1}\bar v_{i,a}z^a$, the entry $(i,h)$ of that linear variation is the coefficient pairing of $\Delta Z$ against $f_i(z)f_h(z)$. For $j=1$, $f_1^2\ne0$. For $j=2$, the three polynomials $f_1^2,f_1f_2,f_2^2$ are linearly independent over $\mathbb F_p$: otherwise the nonconstant rational function $f_1/f_2$ would satisfy a quadratic equation over $\mathbb F_p$ and thus be constant, contradicting independence of $v_1,v_2$. This remains valid in characteristic two. The map from the $2n-1$ free third digits to $\mathrm{Sym}_j(\mathbb F_p)$ is therefore surjective. Translation by the fixed lower-digit contribution preserves uniformity. QED.

### Proof of the theorem

Conditional on first-digit corank $k$, the uniform $k\times k$ Hankel form $\bar S$ has corank exactly $j$ with probability

$$
p^{-(2j-1)}-p^{-(2j+1)}
$$

for $j<k$, by the classical Hankel rank law. In this event the original cokernel has $k-j$ invariant factors of valuation one and $j$ factors of valuation **at least two**. Those last factors have valuation exactly two precisely when the second-order residual form $W\bmod p$ is invertible.

A uniform symmetric $1\times1$ or $2\times2$ matrix over $\mathbb F_p$ is nonsingular with probability $1-p^{-1}$. (For $2\times2$, the determinant $uw-v^2$ vanishes at exactly $p^2$ of the $p^3$ coefficient triples.) Apply the lemma, then multiply by the probability $\rho_{n,k}$ of the original corank-$k$ event. QED.

## Exact finite audit, independently coded

For $p=2$ and $n=k=3$, conditional on $H_3\bmod2=0$, one can write $H_3=2S$ with $S$ uniform Hankel modulo $4$, giving $4^5=1024$ possible anti-diagonal sequences. Direct enumeration (not using the distribution formula) gives:

| $\operatorname{corank}(S\bmod2)$ | Count of $S$ | Count with invertible second-order residual | Predicted count |
|---:|---:|---:|---:|
| 1 | 384 | 192 | $384(1-1/2)=192$ |
| 2 | 96 | 48 | $96(1-1/2)=48$ |

The remaining classes have corank zero (512 cases) or three (32 cases). Thus the proportions in the two rows agree exactly with the theorem. The script [P020 second-order two-layer audit](../experiments/P020_second_order_small_kernels.py) reproduces the table independently.

## Essential limitations

- The theorem does **not** cover $(\mathbb Z/p^2)^3$, where the second-order radical has dimension three and restricted Hankel perturbations need not span all symmetric forms.
- It does **not** imply that the complete residual $S$ is a Haar Hankel matrix at all $p$-adic orders, or that the full cokernel law converges.
- The rank-$j$ formulas above require **$j<k$**; for $j=k$ the first-order Hankel matrix is zero, whose probability is $p^{-(2k-1)}$, and nonlinear second-order corrections may influence the invertibility fraction.
- Neither the original finite-field Hankel rank enumeration nor generic Smith-form methods are claimed new; novelty of the higher-order conditional restriction theorem should be checked against random structured-matrix literature before drafting a paper.

### Primary sources

- [Dwivedi–Grinberg (2022), *On the rank of Hankel matrices over finite fields*](https://doi.org/10.1016/j.laa.2022.02.014), finite-field rank law.
- [Yiasemides (2024), Theorem 2.4.4](https://doi.org/10.1007/s40687-023-00418-7), characteristic-polynomial classification of finite-field Hankel kernels.
- [Van Peski (2024), *Local limits in p-adic random matrix theory*](https://doi.org/10.1112/plms.12626), wider structured random-matrix context.
