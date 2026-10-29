# P020 continuation — Kernel-product rank and the obstruction to higher-rank lifting

**Date:** 29 October 2026. **Status:** one proved elementary lower bound, exact exhaustive finite evidence, a conjectural upper equality for Hankel kernels. **Not a proof of P020's full distribution.**

## A general polynomial-subspace inequality (proved, not claimed original)

Let \(F\) be any field and \(V\subseteq F[z]\) a finite-dimensional linear subspace of dimension \(k\ge1\). Put
\[
V\cdot V:=\operatorname{span}_F\{fg:f,g\in V\}.
\]
Then
\[
\boxed{\dim_F(V\cdot V)\ge2k-1.}
\]

**Proof.** Row-reduce polynomial coefficients to choose a basis \(f_1,\ldots,f_k\) with strictly increasing degrees \(d_1<\cdots<d_k\). The products
\[
f_1 f_1,\ f_1f_2,\ \ldots,\ f_1f_k,\quad
f_2f_k,\ \ldots,\ f_kf_k
\]
have the \(2k-1\) distinct degrees
\[
2d_1<d_1+d_2<\cdots<d_1+d_k<d_2+d_k<\cdots<2d_k.
\]
Distinct-degree polynomials are linearly independent. □

This is a polynomial-space product-growth inequality of classical additive-combinatorial flavor, **not certified novel**.

## Numerical exact assertion for square Hankel kernels

Let \(H=(h_{i+j})_{0\le i,j<n}\) be any square Hankel matrix over \(F\). Identify \(\ker H\subset F^n\) with polynomials of degree at most \(n-1\). If \(\dim\ker H=k\), numerical exhaustive checks suggest the **strong equality**
\[
\boxed{\dim_F((\ker H)\cdot(\ker H))=2k-1.}\tag{K}
\]

The left side is the rank of the first-order map from the \(2n-1\) independent Hankel parameters to symmetric bilinear forms on the kernel. For \(k\ge3\), equality (K) says this first-order random form lies on a lower-dimensional linear subspace, so **the Haar-symmetric-matrix lemma from P020 cannot be generalized unchanged**.

The test is exact finite-field linear algebra, exhaustive over:
- \(F=\mathbb F_2\), every Hankel matrix of sizes \(n=3,4,5,6\), i.e. \(2^{2n-1}\) matrices at each \(n\);
- \(F=\mathbb F_3\), every Hankel matrix of sizes \(n=3,4,5\), i.e. \(3^{2n-1}\) matrices at each \(n\).

All cases satisfied (K), for every observed \(k\); see [reproducible code](../experiments/P020_kernel_product_dimension.py). No evidence from finite enumerations proves (K) for all fields and sizes.

## Essential historical input newly located

[Yiasemides, *The variance and correlations of the divisor function in \(\mathbb F_q[T]\), and Hankel matrices*, Research in the Mathematical Sciences 11 (2024), article 11](https://doi.org/10.1007/s40687-023-00418-7), especially **Theorems 2.4.4 and 2.4.9**, characterizes kernels of finite-field Hankel matrices using **two characteristic polynomials** and bounded-degree polynomial multiples. This is a much closer structural predecessor than generic random matrix Smith theory. A genuine proof of (K) must be compared to this classification and could be a straightforward corollary. **Do not claim (K) or its proof concept original.**

## Next route to the full p-group distribution

1. Establish or refute (K) over **arbitrary** finite fields using the two-generator kernel structure; check any exceptional field characteristic or boundary shape.
2. Classify the **image subspace** of the first-order lifting map up to congruence, not just its dimension. A \(2k-1\)-dimensional space might be conjugate to \(k\times k\) Hankel forms or another linear series; matrix ranks alone do not establish that.
3. Examine Schur-complement nonlinear terms. Even if first-order images are Hankel-like, higher mod-\(p^r\) corrections need not be Haar in a fixed Hankel subspace.
4. Derive exact distributions of groups with **three generators**, then test whether the unresolved tail mass can be made arbitrarily small in total variation as \(n\to\infty\). The rank-two theorem already determines mass \(1-p^{-5}\) for all \(n\ge3\).

**Mathematical scope:** the previous [P020 two-generator theorem](P020-padic-hankel-cyclic-and-rank-two-laws.md) remains intact. This note introduces a new *testable conjecture* and a theorem that is valid for all polynomial subspaces, but does not extend the Haar-lifting theorem to \(k\ge3\).
