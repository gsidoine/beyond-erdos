# Translation and divisibility avoidance in Sidon sets

**Status:** elementary internally proved proposition and corollary; historical priority of this particular combination is **not certified**. This note records a useful additive–multiplicative compatibility observation associated with [P035](../problems/number-theory/P035-primitive-sidon-coloring.md). It does **not** solve the P035 coloring conjecture or P031's pairwise-coprime Sidon problem.

## Translation lemma

For a finite set of positive integers $A\subseteq[1,M]$, let $\Delta(A)=\{b-a:a,b\in A,\ a<b\}$ denote its set of positive differences, with multiplicity $r_A(d)=|\{(a,b)\in A^2:a<b,\ b-a=d\}|$. Let $\tau(d)$ denote the number of positive divisors of $d$.

**Proposition.** For every $L\ge0$, there exists an integer $t\in[0,L]$ such that $A+t$ has at most

$$
\frac{1}{L+1}\sum_{d=1}^{M-1}r_A(d)\tau(d)
$$

ordered pairs $(a+t,b+t)$ of distinct elements for which $a+t$ divides $b+t$. Consequently, deleting at most this many elements produces a divisibility antichain of size at least

$$
|A|-\frac1{L+1}\sum_{d=1}^{M-1}r_A(d)\tau(d).
$$

**Proof.** For fixed $a<b$, the divisibility condition is

$$
a+t\mid b+t\quad\Longleftrightarrow\quad a+t\mid b-a.
$$

As $t$ runs through $[0,L]$, the number of possible $t$ is at most $\tau(b-a)$, since $a+t$ must be a positive divisor of the fixed integer $b-a$. Sum over all pairs, then average over the $L+1$ translations. One member from each offending pair can be removed, without increasing the number of violations. QED.

**Sidon specialization.** If $A$ is Sidon, every positive difference has multiplicity at most one; therefore

$$
\sum_{d=1}^{M-1}r_A(d)\tau(d)
\le\sum_{d=1}^{M-1}\tau(d)
\le M(1+\log M).
$$

Translation and deletion preserve Sidonicity.

## Corollary: primitive Sidon sets have the optimal leading constant

Let $F_{\mathrm{PS}}(N)$ be the maximum size of a set $S\subseteq[N]$ such that the unordered two-term sums in $S$ (including diagonal sums) are distinct and no distinct $a,b\in S$ satisfy $a\mid b$.

Then

$$
\boxed{F_{\mathrm{PS}}(N)=(1+o(1))\sqrt N.}
$$

**Proof.** Put $L=\lfloor N^{3/4}\rfloor$, $M=N-L$. Classical Singer/Bose–Chowla Sidon constructions yield $A\subseteq[1,M]$ with $|A|=(1-o(1))\sqrt M$. The proposition gives a translation $t\in[0,L]$ whose translated Sidon set contains at most

$$
O\left(\frac{M\log M}{L+1}\right)
=O(N^{1/4}\log N)=o(\sqrt N)
$$

divisibility violations. Delete one endpoint of every violating pair. Since $A+t\subseteq[N]$ and $\sqrt M\sim\sqrt N$, the resulting primitive Sidon set has cardinality $(1-o(1))\sqrt N$. The converse is the classical maximal Sidon-set bound $|S|\le(1+o(1))\sqrt N$. QED.

## Further consequence: finitely many forbidden ratios

Fix a finite set $R\subseteq\mathbb Q_{>1}$. For any $A\subseteq[1,M]$, each distinct ordered pair $a<b$ and each fixed ratio $r\in R$ admit **at most one** translation $t$ with $b+t=r(a+t)$, since $(r-1)t=b-ra$. Therefore some shift $t\in[0,L]$ creates at most

$$
\frac{|R|\binom{|A|}{2}}{L+1}
$$

pairs with a forbidden ratio. In particular, taking $|A|=(1-o(1))\sqrt M$ and $L=\lfloor N^{3/4}\rfloor$ shows that for every **fixed finite $R$**, there is an asymptotically optimal Sidon subset of $[N]$ whose pairwise larger/smaller ratios avoid $R$.

This last corollary is substantially weaker than excluding **all** integer ratios, which is handled by the divisor-sum proposition.

## Significance and prior-art comparison

The sharp leading constant for Sidon sets is classical. Divisibility antichains and primitive integer sets are classical. The argument uses the classical identity

$$
\sum_{d\le M}\tau(d)=M\log M+O(M)
$$

and the elementary translation invariance of Sidonicity. The specific combined asymptotic was not located in targeted searches under *primitive Sidon*, *Sidon divisibility antichain*, *Sidon no divisible pairs*, and *divisibility-avoiding Golomb ruler*. This is a **bounded negative search, not proof of historical novelty**. In particular, the phrase *multiplicative Sidon* describes a different, well-established constraint and should not be treated as an equivalent formulation.

A further terminological caveat is essential: in some additive-combinatorics literature, a *primitive Sidon set* means an additively indecomposable Sidon set over a finite field, not an antichain in the integer divisibility poset. For example, [an *Integers* article (2015)](https://www2.math.ethz.ch/EMIS/journals/INTEGERS/papers/p6erdos/p6erdos.pdf) uses this different meaning of *primitive*. The present result always uses **primitive under divisibility**, as explicitly defined above.

The result is short and rigorous, but its conclusion chiefly shows that one multiplicative restriction incurs no first-order loss in an established extremal problem. Its current editorial placement is **The Seedbed, as a resolved lemma supporting P035**, rather than a new high-consequence Acorn.

### References

- [Ruzsa, *Sumsets of Sidon sets* (1996)](https://doi.org/10.4064/aa-77-4-353-359): classical leading-order Sidon constructions and related additive questions.
- [Carter–O'Bryant–Tao, *On the diameter and distribution of Sidon sets* (2026)](https://arxiv.org/abs/2610.36207): current improvements to the sharp Sidon upper error term, not a source for the primitive-divisibility corollary.
- [Liu–Pach–Palincza, *The number of maximum primitive sets of integers* (2021)](https://doi.org/10.1017/S0963548321000018): established divisibility-antichain theory.
- [*Finding large additive and multiplicative Sidon sets in sets of integers* (2024)](https://doi.org/10.1007/s00208-024-02932-7): an adjacent but **different** simultaneous additive/multiplicative Sidon problem.
