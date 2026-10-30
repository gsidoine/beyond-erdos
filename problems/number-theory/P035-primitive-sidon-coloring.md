# P035 — Sidon coloring by divisibility antichains

<!-- DOSSIER-SUMMARY -->
> **Research question:** Can [N] be partitioned into (1+o(1))sqrt(N) sets, each Sidon and a divisibility antichain?  
> **Formulation:** candidate. **Novelty:** unverified; combines classical Sidon coloring and primitive sets.  
> **Verified/known progress:** sqrt(N)(1-o(1)) <= chi_PS(N) <= (2+sqrt(2)+o(1))sqrt(N) by dyadic bands and classical Sidon partitions.  
> **Finite evidence:** Proof of dyadic band upper bound; no computational all-N claim.  
> **Navigation:** [Full problem catalogue](../../README.md#problem-catalogue) · [Status and scope](../../README.md#status-and-scope) · [Literature and audits](../../README.md#literature-and-audits)
<!-- /DOSSIER-SUMMARY -->

**Status:** candidate; historical novelty and open status are not independently certified.

## Question

Color all integers in \([N]\), requiring every color class \(A\) to satisfy both:

1. **Sidon:** \(a+b=c+d\) with \(a\le b\), \(c\le d\), and all four elements in \(A\) forces \(\{a,b\}=\{c,d\}\).
2. **Primitive:** for distinct \(a,b\in A\), neither \(a\mid b\) nor \(b\mid a\).

Let \(\chi_{\mathrm{PS}}(N)\) be the minimum number of colors.

**P035.** Is \(\chi_{\mathrm{PS}}(N)=(1+o(1))\sqrt N\)?

This is a coloring question, **not** the P031 question about a single pairwise-coprime Sidon set. Incomparability under divisibility is much weaker than pairwise coprimality.

## Rigorous baseline

**Theorem (elementary reduction).**

$$
(1-o(1))\sqrt N\le \chi_{\mathrm{PS}}(N)\le
(2+\sqrt 2+o(1))\sqrt N.
$$

**Lower bound.** Every color class is Sidon in \([N]\), and the classical Erdős–Turán bound makes its size at most \((1+o(1))\sqrt N\). Thus at least \((1-o(1))\sqrt N\) classes are required.

**Upper bound.** For \(j\ge0\), let

$$
B_j=\{m\in[N]:N/2^{j+1}<m\le N/2^j\}.
$$

Every \(B_j\) is primitive: if distinct \(a<b\) in the same band had \(a\mid b\), then \(b\ge2a>N/2^j\), impossible. The length of \(B_j\) is at most \(N/2^{j+1}+1\). The classical Sidon-coloring theorem partitions any interval of \(M\) consecutive integers into \((1+o(1))\sqrt M\) Sidon classes as \(M\to\infty\); translating a Sidon partition preserves the Sidon property. Use **disjoint color palettes for different bands**, making every resulting class simultaneously Sidon and primitive.

The leading color count is therefore bounded by

$$
\sum_{j\ge0}\sqrt{\frac N{2^{j+1}}}
=\frac{1}{\sqrt2-1}\sqrt N
=(1+\sqrt2)\sqrt N.
$$

The claimed theorem uses the **weaker conservative coefficient** \(2+\sqrt2\) to absorb small bands and any finite-size overhead; an explicit tail split at \(N/2^{j+1}\ge (\log N)^4\) shows small-band contribution \(O((\log N)^4)\) if the remaining tiny integers are assigned singleton classes, while the large bands have a uniform \(1+o(1)\) Sidon-coloring bound. In fact the same argument proves the sharper \((1+\sqrt2+o(1))\sqrt N\) bound. We retain the sharper statement as the operative bound below.

**Sharper upper bound:** \(\chi_{\mathrm{PS}}(N)\le (1+\sqrt2+o(1))\sqrt N\). The initial conservative coefficient in the displayed theorem is valid but unnecessarily weak.

## Why the question is not settled by the baseline

A classical optimal Sidon partition need not respect divisibility. Conversely, using separate colors for each dyadic multiplicative antichain loses a geometric factor \(1+\sqrt2\). To obtain constant one, one must coordinate additive and multiplicative conflicts across bands. An arbitrary-Sidon-set result or a primitive-set result alone cannot provide that coordination.

## Literature and originality gate

- [Classical Sidon coloring of integer intervals](https://mathoverflow.net/questions/461551/bounds-on-how-many-sidon-sets-required-to-cover-an-integer-range-from-0-n) gives the sharp \((1+o(1))\sqrt N\) coloring rate without divisibility constraints.
- [Erdős Problems: primitive sets](https://www.erdosproblems.com/tags/primitive%20sets) documents the older divisibility-antichain literature.
- [Erdős Problems: Sidon sets](https://www.erdosproblems.com/tags/sidon%20sets) documents closely related additive extremal questions.
- [Kohayakawa–Lee–Rödl–Samotij](https://www.math.tau.ac.il/~samotij/papers/Sidon.pdf) is relevant background on Sidon subsets and colorings.

The combination is a plausible **new formulation**, not a certified new or open research problem. Exact matches may occur in the literature under *rainbow*, *harmonious*, *Sidon chromatic*, or *divisibility antichain coloring*. A specialist bibliographic search is required before asserting originality.

## Falsification

Either prove \(\liminf \chi_{\mathrm{PS}}(N)/\sqrt N>1\), or produce colorings with \((1+o(1))\sqrt N\) colors. More modestly, improve the elementary \(1+\sqrt2\) upper constant without merely changing the dyadic cutoff.
