# P020 — Candidate exponent-$p^2$ law: the second-order affine-offset obstruction

**Status:** research conjecture and precise proof-obstruction audit. The proposed formula would strengthen the prior [one/two residual-factor theorem](../theorems/P020-exact-second-order-small-kernel-laws.md) to **all** residual coranks. Published finite-field Hankel-rank and kernel structure are credited below. Historical novelty unverified; **does not** settle exponents $p^3$ or the full group law.

## Statement

Let $H_n=(X_{i+j})_{0\le i,j<n}$ be a Haar-uniform $n\times n$ Hankel matrix over $\mathbb Z_p$, $C_n=\mathrm{coker}(H_n)$, and let $1\le k\le n$. Define

$$
\rho_{n,k}=
\begin{cases}
p^{-(2k-1)}-p^{-(2k+1)},&k<n,\\
p^{-(2n-1)},&k=n,
\end{cases}
\qquad
\sigma_{k,j}=
\begin{cases}
1-p^{-1},&j=0,\\
p^{-(2j-1)}-p^{-(2j+1)},&1\le j<k,\\
p^{-(2k-1)},&j=k.
\end{cases}
$$

**Conjectural formula (not proved in general).** For every $0\le j\le k$,

$$
\boxed{\Pr\!\left(C_n\simeq
(\mathbb Z/p\mathbb Z)^{k-j}\oplus
(\mathbb Z/p^2\mathbb Z)^j\right)
=\rho_{n,k}\sigma_{k,j}
\begin{cases}
1,&j=0,\\
1-p^{-1},&j\ge1.
\end{cases}}
$$

For $j=0$ this is the existing elementary-abelian law. For $1\le j<k$ the novelty in this pass is extending the *second-order residual-kernel* argument beyond dimension two. For $j=k$, in particular,

$$
\boxed{\Pr(C_n\simeq(\mathbb Z/p^2)^k)=
\rho_{n,k}\,p^{-(2k-1)}(1-p^{-1}).}
$$

Every probability is **exactly independent of $n$ for fixed $k$ as soon as $n>k$**. The theorem determines every finite $p$-group with exponent dividing $p^2$ (including the trivial group, whose probability is $1-p^{-1}$).

## Attempted proof and exact stopping point

**First layer.** Fix the anti-diagonal input modulo $p$ at a Hankel matrix with corank $k$. The [published finite-field kernel classification](../theorems/P020-hankel-kernel-product-research.md) supplies a polynomial-shift basis $A,Az,\ldots,Az^{k-1}$ of its radical. Splitting off the invertible block of $H_n$ produces a $k\times k$ Schur complement $T=pS$. By the [proved first-order lifting lemma](../theorems/P020-elementary-abelian-cokernel-laws.md), $\bar S=S\bmod p$ is a **uniform Hankel** matrix in this basis. Hence the conditional distribution of its nullity $j$ is $\sigma_{k,j}$, the classical square-Hankel corank law.

When $j=0$, all $k$ nonunit Smith factors of $H_n$ have valuation one, and the theorem follows.

**Second layer, all $1\le j\le k$.** Fix the complete first two anti-diagonal digits, so that $\bar S$ is fixed of corank $j$. By the **same published finite-field Hankel kernel classification applied to $\bar S$**, its radical in the polynomial-shift coordinates has a basis

$$
B,\ Bz,\ldots,Bz^{j-1}
$$

for a nonzero polynomial $B$ of degree at most $k-j$. Under the embedding of the first radical back into the original input space, these vectors become the polynomials

$$
AB,\ ABz,\ldots,ABz^{j-1}.
$$

Use fixed integral lifts of these vectors and eliminate the invertible block of $S$ inside the original $k$-dimensional radical. Its $j\times j$ Schur complement is divisible by $p$; write $pW$ for it. The corresponding nonunit Smith factors of the *original* matrix are $p^2$ times the Smith factors of $W$.

Now vary only the **third** anti-diagonal digits of the original $X_s$. Conditional on the first two digits, these variations are independent uniform $\Delta_s\in\mathbb F_p$. Since the original matrix changes by $p^2H(\Delta)$, after the two successive divisions by $p$ the variation of $\bar W$ is exactly its restriction to the second radical:

$$
(\Delta\bar W)_{uv}=\ell_\Delta\bigl((AB)^2z^{u+v}\bigr),
\qquad 0\le u,v<j.
$$

The $2j-1$ polynomials $(AB)^2z^t$ for $0\le t\le2j-2$ are linearly independent, because $AB$ is nonzero and their degrees differ. Their degrees do not exceed $2n-2$: the vectors $ABz^{j-1}$ live in the original length-$n$ polynomial space, so the products fit within its Hankel anti-diagonal range.

Thus the map from the free third digits $\Delta_s$ to the $2j-1$ anti-diagonal entries of $\bar W$ is **surjective**. The fixed contribution to $\bar W$ is also Hankel in this basis: every two coordinate vectors in the radical are shifted powers of the same product $AB$, and the original quadratic pairing and the first Schur-complement linearization depend only on the sum $u+v$; at second order a potential nonlinear correction must be handled with care. We therefore need only a *translation* of the full Hankel image to infer the determinant probability. The resulting $\bar W$ is a uniformly translated affine Hankel family. If the fixed translation is itself Hankel, this is uniform Hankel, and its invertibility probability is $1-p^{-1}$.

**Crucial audit qualification:** unlike the first layer, the *second Schur-complement correction may depend separately on $u$ and $v$*. Its affine translation has not been proved to lie in the Hankel subspace for arbitrary $j\ge3$. An arbitrary translate of the Hankel subspace need **not** have the same nonsingularity count. Therefore the displayed full theorem for $j\ge3$ is a **candidate conditional formula**, not established by this argument as written. The unconditional established cases are $j=0$ and $j=1,2$ from the preceding P020 notes, and the exceptional **full-radical boundary** described next.

**Full-radical case $j=k$: caution.** If $\bar S=0$, there is *no* nontrivial second Schur complement: $W=S/p$ itself. Since the original $k$-dimensional radical retains its shift basis $A,Az,\ldots,Az^{k-1}$, the entire second-order affine form is Hankel (the first Schur-complement's quadratic corrections are also Hankel in this shift basis modulo the required order **only after checking their dependence on the coordinate shifts**). This is a proof obligation rather than a completed higher-order argument for general $k$. In the particularly transparent boundary case $n=k$, $H_n\bmod p=0$ and the second reduction is literally a scaled Haar Hankel matrix, so the displayed full-radical formula is rigorously valid **for $n=k$**.

### Status table (do not overclaim)

| Family | Status |
|---|---|
| $j=0$ (all factors $p$) | Proven in earlier P020 note |
| $j=1,2$ with $j<k$ | Internally proved in earlier second-order note |
| $j=k=n$ (all factors $p^2$ and $n=k$) | Proven directly by factorization $H_n=p^2K$ |
| $3\le j<k$ and $j=k<n$ | **Conjectural pending affine-translation/Hankel correction check** |

**The full theorem displayed at the beginning is consequently only a research conjecture outside the verified rows of this table.** The purpose of this note is to expose the exact remaining obstruction instead of hiding it behind the linearized image dimension.

## Exact full-radical finite check

For $p=2,n=k=3$, the condition $H_3\bmod2=0$ and then $(H_3/2)\bmod2=0$ leaves $H_3=4K$ with $K\bmod2$ a uniform $3\times3$ binary Hankel matrix. Exactly **16 of 32** binary Hankel matrices are invertible. Hence

$$
\Pr(C_3\simeq(\mathbb Z/4)^3)
=(1/2)^5(1/2)^5(1/2)=1/2048.
$$

This exact case is fully proved and provides an audit target for all higher-$n$ conjectures.

## Next breakthrough target

Prove that the fixed affine offset of $\bar W$ for a second radical of polynomial-shift dimension $j\ge3$ has the appropriate Hankel structure, or directly count invertible matrices in the resulting affine family. Either outcome yields nontrivial new mathematics. A disproof would be equally useful: one might discover a genuine higher-order deviation from dimension-independent cokernel laws.

**Sources:** [Yiasemides (2024)](https://doi.org/10.1007/s40687-023-00418-7) for finite-field Hankel kernels; [Dwivedi–Grinberg (2022)](https://doi.org/10.1016/j.laa.2022.02.014) for finite-field Hankel rank distribution.
