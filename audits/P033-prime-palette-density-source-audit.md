# P033 — Priority and adversarial audit for prime-palette density

**Current result:** The [quantitative theorem](../theorems/P033-prime-palette-density-and-reflection-criterion.md) proves that, for any fixed $0<\delta<1/5$, the fraction of three-prime palettes with two primes in $((1-\delta)n,n)$ and one in $(n,(1+\delta)n)$ whose sum-edge graph connects [n] approaches

$$
\mathfrak C=\frac34\prod_{\ell>2\ \mathrm{prime}}
\left(1-\frac1{(\ell-1)^2}\right)\approx0.49512138.
$$

It also sharpens the graph criterion from $n\ge12D+10$ to $n\ge5D$, and includes a finite three-color witness for every n≤1,000,000. **No claim of certified historical novelty or a complete all-n proof is made.**

## Mathematical proof register

1. **Necessary condition (already proved in the previous P033 note):** connectedness with three odd sums p,q,r implies $g=\gcd((q-p)/2,(r-p)/2)=1$, since the reflection-generated component is trapped in two residue classes modulo 2g.
2. **Improved sufficiency:** if $p<q<n<r$ are odd and within D of n, $n\ge5D$ implies the odd core $I=\{x\text{ odd}:r-n\le x\le p-1\}$ has at least $a+b$ vertices, where $a=(q-p)/2$, $b=(r-p)/2$. Two-edge reflections give steps a,b on the core; the coprime interval-step lemma connects it, then tails and every even vertex attach.
3. **Fixed local prime congruences:** at odd ℓ the bad event has probability $1/(\ell-1)^2$, and at 2 it has probability 1/4 because the primes are odd but their half-differences share a factor 2 exactly when all three primes agree modulo 4. The Chinese remainder theorem and fixed-modulus PNT give the finite Euler product.
4. **Prime divisors between R and √n:** Brun–Titchmarsh gives $O(n/(\ell\log n))$ primes per class in either relative interval; the total bad-triple count is $O(n^3/(R\log^3 n))$.
5. **Prime divisors above √n:** For each left prime p, there are at most $\delta n/\ell$ possible q and $\delta n/\ell+1$ possible r in its residue class. This gives $O(n^{5/2}/\log n+n^2)=o(n^3/\log^3 n)$. No unproved independence between prime values is assumed.
6. **Only after the fixed-R limit**, take R→∞. The positive infinite Euler product converges since $\sum_\ell 1/\ell^2<\infty$.

The proof therefore avoids the preceding theorem's *uniform* Siegel–Walfisz invocation for a modulus growing with n. It still uses the **classical prime number theorem in fixed arithmetic progressions**. In particular, it has **no explicitly computed global threshold** despite the finite verification through a million. Do not describe that as a proof of every n.

## Primary-source comparisons

- [Chen–Fu–Guo (2021), *Hamiltonicity in Prime Sum Graphs*](https://doi.org/10.1007/s00373-020-02241-1): the host graph and three-color Hamiltonian-prime-set constructions are established. Their infinite-family Hamiltonicity claims do not directly assert the present connected-palette asymptotic.
- [Croot–Jin (2026), *Prime Sum Graphs and the Induced Trees They Contain*](https://doi.org/10.1007/s00373-025-02999-2): graph host, induced-tree results and prime-sum structural literature.
- [Kedlaya, prime number theorem in arithmetic progressions](https://kskedlaya.org/ant/chapter-11.html): the fixed-modulus PNT input; the original P033 paper used its uniform Siegel–Walfisz strengthening.
- [Montgomery–Vaughan Brun–Titchmarsh theorem for intervals, quoted as Lemma 2.6](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1024.pdf): classical uniform per-residue prime-count **upper** bound.
- [Twin-prime singular series](https://mathworld.wolfram.com/TwinPrimes.html): the odd-prime product is an established constant. The **fact that it also occurs in this connected-palette count** is the novel-looking combination, whose historical priority must be checked.

A targeted search of *prime sum graphs*, *three edge-sum colors*, *visible triples of primes* and *coprime prime gaps* found adjacent themes, but not the exact asymptotic connected-palette proportion. This is **not** a certified complete MathSciNet/zbMATH novelty search.

## Numeric and software checks

The [exact verifier](../experiments/P033_prime_palette_density.py) independently implements graph connectivity, gcd and prime-sieve counts and tests **77,795** triples of synthetic odd edge sums at n=5D, 5D+1 and 5D+9 for D≤40.

For δ=1/10 the exact counts of eligible triple palettes and connected palettes at finite n are:

| n | All triples | Coprime/connected triples | Fraction |
|---:|---:|---:|---:|
| 1,000 | 1,456 | 784 | 0.53846154 |
| 3,000 | 21,978 | 11,108 | 0.50541451 |
| 10,000 | 658,896 | 329,037 | 0.49937623 |
| 20,000 | 3,939,606 | 1,958,663 | 0.49717231 |

These values agree with the predicted limit ≈0.49512138 without being used in the analytic proof. A separate exact finite witness algorithm using 12 nearby primes on each side finds three primes satisfying the **proved $n\ge5D$ criterion for every $60\le n\le10^6$**; the previous exhaustive P033 test covers $3\le n\le120$. Thus P033 is computationally certified through one million but remains unproved for every integer n.

## Publication and next gate

This is a meaningful **quantitative theorem**, not merely a restatement of the previous eventual-connectivity result. It is a candidate for a short proof note only after an independent audit of the Montgomery–Vaughan tail argument, the near-interval graph lemma, and exact historical sources on visible triples of primes. The most important unresolved mathematical question remains:

> Can the all-n claim $\kappa(n)\le3$ be proved with an explicit threshold and exhaustive verification, or by a direct non-asymptotic construction?

No new catalogue problem ID is necessary: this is a stronger answer to the existing P033 direction.
