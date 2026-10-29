# P020 — Cokernel laws for random $p$-adic Hankel matrices

<!-- DOSSIER-SUMMARY -->
> **Research question:** Does the cokernel of an n×n Haar-random p-adic Hankel matrix converge in distribution to a describable measure on finite abelian p-groups?  
> **Formulation:** candidate. **Novelty:** apparent novelty (targeted audit).  
> **Verified/known progress:** Classical mod-p corank law; internally proved exact all cyclic and two-generator cokernel probabilities, n-stable.  
> **Finite evidence:** Exact prime-power modular enumeration; higher corank kernel-product equality checked through n=6 at p=2 and n=5 at p=3.  
> **Navigation:** [Full problem catalogue](../../README.md#problem-catalogue) · [Latest novelty audit](../../literature-audits/2026-10-29-novelty-and-new-directions.md)
<!-- /DOSSIER-SUMMARY -->

**Area:** algebraic probability, number theory, random matrices  
**Proposed:** 29 October 2026  
**Status:** exploratory mathematical question, not certified new or unresolved.

## Model and precise question

Fix a prime $p$. Let $X_0,X_1,\ldots$ be independent Haar-uniform random elements of the $p$-adic integers $\mathbb Z_p$. Define the $n\times n$ random Hankel matrix

$$
H_n=(X_{i+j})_{0\le i,j<n}.
$$

The entries on each anti-diagonal are identical, so **only $2n-1$ independent random parameters** generate the $n^2$ matrix entries.

Set

$$
C_n=\operatorname{coker}(H_n:\mathbb Z_p^n\longrightarrow\mathbb Z_p^n).
$$

With probability one, $\det(H_n)\ne0$ in $\mathbb Z_p$, so $C_n$ is a finite abelian $p$-group.

**P020.** For each finite abelian $p$-group $A$, does the limit

$$
\nu_p(A)=\lim_{n\to\infty}\Pr(C_n\cong A)
$$

exist, with $\sum_A\nu_p(A)=1$? If so, characterize this limiting law explicitly, for example by its finite-group probabilities, generating functions or moments. Does it have a natural invariance principle under replacing Haar diagonal parameters with non-Haar $p$-adically nondegenerate distributions?

The question is deliberately **not** whether the law equals ordinary Cohen–Lenstra: the established finite-field rank distribution already rules that out.

## An exact known obstruction: rank is not independent-entry universal

**Known theorem (finite-field Hankel rank counts, credited to the literature).** A uniformly sampled square $n\times n$ Hankel matrix over $\mathbb F_p$ has

$$
\Pr\bigl(\operatorname{corank} H_n\ge k\bigr)
=p^{-(2k-1)}
\quad(1\le k\le n).
$$

This follows from the classical count of rank-at-most-$r$ Hankel matrices over a finite field (for $r<n$), namely $p^{2r}$ matrices out of $p^{2n-1}$ possibilities. See Dwivedi and Grinberg (2022) for the classical count, independent earlier derivations, and refinements. **We do not claim this rank formula as an original result.**

In particular, for every $n$,

$$
\Pr(C_n=0)=\Pr(H_n\bmod p\text{ invertible})=1-\frac1p.
$$

By contrast, for fully independent Haar $p$-adic matrix entries, the large-$n$ probability of trivial cokernel is

$$
\prod_{j=1}^\infty(1-p^{-j})<1-\frac1p.
$$

Thus **the usual independent-entry Cohen–Lenstra law cannot be the limit here**. This is an exact, well-motivated reason to ask for a different law, not numerical speculation.

The corank distribution determines only the dimension of $C_n/pC_n$ over $\mathbb F_p$; it does **not** determine higher $p$-power invariant factors or the isomorphism class of $C_n$.

## New internally proved partial group law (29 October 2026)

**Important:** This is an **internal mathematical result**, not an externally refereed proof or certified originality claim. See the [complete theorem note and proof](../../theorems/P020-padic-hankel-cyclic-and-rank-two-laws.md) and the [independent exact modular checks](../../experiments/P020_padic_rank_two_lifts.py).

**Cyclic case:** For all \(n\ge2\) and \(j\ge1\),
\[
\Pr(C_n\simeq\mathbb Z/p^j\mathbb Z)
=(1-p^{-1})(1-p^{-2})p^{-j}.
\]

**Every two-generator group:** For \(n\ge3\), \(1\le a\le b\), and \(\rho_2=p^{-3}-p^{-5}\),
\[
\Pr(C_n\simeq\mathbb Z/p^a\oplus\mathbb Z/p^b)
=\begin{cases}
\rho_2 p^{-3(a-1)}(1-p^{-1}),&a=b,\\
\rho_2 p^{-3(a-1)}(p^{-1}-p^{-3})(1-p^{-1})p^{-(b-a-1)},&a<b.
\end{cases}
\]
The key conditional lifting lemma says that, after fixing a corank-one or corank-two reduction modulo \(p\), the nonunit block has the distribution of \(p\) times a Haar-uniform **symmetric** matrix of the corresponding size. In corank two, surjectivity follows from the linear independence of \(f^2,fg,g^2\) for two linearly independent polynomials \(f,g\).

**Consequence:** Exactly \(1-p^{-5}\) of the probability mass is now characterized by group-specific formulas independent of \(n\ge3\); hence the total-variation distance between **any two** such \(n\)-distributions is at most \(p^{-5}\). **This is not a full limit theorem.** For corank at least three, polynomial-product dependencies obstruct this particular argument.

**Priority caution:** The base finite-field rank formula is not new. Targeted review did not locate these precise higher-invariant-factor formulas in the cited sources, but specialist priority review of structured p-adic Smith forms remains outstanding.

## Independent finite falsification

The dependency-free [exact rank enumerator](../../experiments/P020_hankel_finite_field_ranks.py) enumerates every one of the $p^{2n-1}$ possible Hankel matrices over $\mathbb F_p$, computes row-reduced rank exactly, and verifies the classical tail formula for $1\le k\le n$.

| $p$ | $n$ | Corank counts $(0,1,\ldots,n)$ |
|---:|---:|---|
| 2 | 2 | $(4,3,1)$ |
| 2 | 3 | $(16,12,3,1)$ |
| 2 | 4 | $(64,48,12,3,1)$ |
| 3 | 2 | $(18,8,1)$ |
| 3 | 3 | $(162,72,8,1)$ |

These are checks of **known mod-$p$ mathematics** and do not establish any limit law for $p$-adic cokernels.

## Why this problem might matter

The usual Cohen–Lenstra universality proofs exploit large numbers of sufficiently independent matrix entries. Hankel matrices compress a quadratic array into only $2n-1$ independent parameters, making a natural test of **how algebraic dependence changes random finite abelian groups**.

A solution would connect structured linear algebra, finite-field rank enumeration, random $p$-groups and arithmetic statistics. If an explicit limit differs from Cohen–Lenstra, it would quantify a new dependence-sensitive universality class, rather than simply observing that rank probabilities differ.

## Nearest literature and priority caveat

- **Dwivedi and Grinberg**, [*On the rank of Hankel matrices over finite fields* (2022)](https://doi.org/10.1016/j.laa.2022.02.014): **direct prior art** proving or refining the classical finite-field rank counts. It does not, in the accessible summary, determine the full $p$-adic finite-abelian-group distribution.
- **Wood**, [*Random integral matrices and the Cohen–Lenstra heuristics*](https://doi.org/10.1353/ajm.2019.0008): canonical cokernel universality for matrices with independent entries. The independent-entry hypothesis fails spectacularly for Hankel matrices.
- **Maples**, [*Cokernels of random matrices satisfy the Cohen–Lenstra heuristics*](https://arxiv.org/abs/1301.1239): another direct baseline for independent-entry cokernels.
- **Jang, Kaplan, Lee and Yu**, [*A mod $p$ determinant criterion for Cohen–Lenstra convergence of random $p$-adic matrices with prescribed zero patterns* (2026)](https://arxiv.org/abs/2606.06993): very recent extension to matrices with **prescribed zeros** and independent free entries, conceptually different from repeated anti-diagonal entries.
- **Miller and Stanton**, [*Orthogonal polynomials and Smith normal form* (2017)](https://arxiv.org/abs/1704.03539): systematic Smith forms for several **deterministic structured Hankel matrices**, not an explicit Haar-random distribution in the accessible description.

Targeted searches for *random Hankel cokernel*, *Hankel Smith normal form probability*, *Hankel Cohen–Lenstra law* and *random p-adic Hankel matrix invariant factors* did not locate the exact limiting finite-$p$-group question. **This is not an originality certificate**; a deeper specialist citation-chain and full-text review is required.

## Screening before further work

1. Check whether finite-$p^k$ Hankel invariant-factor counts are already known under the vocabulary *Hankel forms*, *moment matrices* or *linear recurrence sequences*.
2. Test whether fixed-$n$ distributions stabilize or change as $n$ increases; do not infer this from corank alone.
3. Separate Haar-uniform diagonal parameters from Bernoulli and other discrete distributions.
4. Determine whether the resulting laws can be expressed by Hall–Littlewood, partitions or random polynomial models. Avoid an unsupported Cohen–Lenstra-type conjecture.
