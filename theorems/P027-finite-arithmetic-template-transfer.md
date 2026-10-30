# P027 — Every finite divisibility model reappears as an isolated arithmetic block

**Claim status:** an internal theorem with a constructive proof. It is a structural reduction, **not a proof that the P027 mixing time exceeds every multiple of n log n**. The use of finite arithmetic blocks in primitive-set counting has significant prior art; see [Liu–Pach–Palincza (2021)](https://doi.org/10.1017/S0963548321000018).

## The transfer theorem

Let F(T) denote the number of *maximum* primitive subsets of [T], for any integer T≥2. Let Q_T be the unnormalised single-coordinate heat-bath generator on their dyadic-chain exponent configurations,

$$
Q_T=\sum_{\substack{1\le a\le T\\a\text{ odd}}}(H_a-I),
$$

where H_a resamples the a-coordinate conditionally and uniformly. Write λ_T>0 for the smallest positive eigenvalue of −Q_T.

For n≥1, set N=2n. Put B_T=ceil(3(T+1)^2) and let

$$
D_T=\prod_{\substack{p\le B_T\\p\text{ prime}}}p,\qquad
k_T(n)=\#\{u:N/(T+1)<u\le N/T,\ \gcd(u,D_T)=1\}.
$$

**Theorem.** For each *fixed* T≥2:

1. The maximum-primitive-set configuration space on [2n] factors as

   $$
   \Omega_n\cong \Omega_T^{\,k_T(n)}\times\Omega_n^{\mathrm{rest}}.
   $$

   Each copy is preserved by the heat-bath transitions, with conditional updates exactly the heat bath on Ω_T.
2. The number of copies is **linear**:

   $$
   k_T(n)=c_T n+O_T(1),\qquad
   c_T=\frac{2\varphi(D_T)}{T(T+1)D_T}>0.
   $$

3. The projection onto these copies has total-variation cutoff at

   $$
   \frac n{2\lambda_T}\log k_T(n)
   $$

   with an O_T(n) window. In particular, for each fixed ε∈(0,1),

   $$
   \boxed{\liminf_{n\to\infty}
   \frac{t_{\mathrm{mix}}(n,\varepsilon)}{n\log n}
   \ge\frac1{2\lambda_T}.}
   $$

4. If f(n) counts maximum primitive subsets of [2n], then

   $$
   F(T)^{\,k_T(n)}\mid f(n).
   $$

Consequently,

$$
\boxed{\liminf_{n\to\infty}
\frac{t_{\mathrm{mix}}(n,\varepsilon)}{n\log n}
\ge \sup_{T\ge2}\frac1{2\lambda_T}.}
$$

**Conditional breakthrough criterion.** If inf_T λ_T=0, then the full P027 heat-bath mixing time is **ω(n log n)**. This implication is proved, but its hypothesis is **not established**. A failure of λ_T→0 would not establish an O(n log n) upper bound for the full chain.

## Proof of exact isolation

The dyadic-chain representation of maximum primitive sets has one exponent e_v for every odd v≤N, with bounds

$$
m_v=\lfloor\log_3(N/v)\rfloor
\le e_v\le L_v=\lfloor\log_2(N/v)\rfloor
$$

and strict inequalities e_a>e_b when b is a proper odd multiple of a.

Fix u in the stated interval, coprime to D_T. Then t=N/u∈[T,T+1), and every odd multiple au≤N has a≤T. For a odd ≤T,

$$
m_{au}=\lfloor\log_3(t/a)\rfloor
=\lfloor\log_3(T/a)\rfloor,\qquad
L_{au}=\lfloor\log_2(T/a)\rfloor.
$$

The equalities follow because a power of 2 or 3 times an integer a is an integer, and t lies strictly below T+1. Comparabilities among these multiples are exactly those among the odd indices ≤T. Thus their *internal* configuration space is Ω_T.

Consider a proper divisor d of au not itself divisible by u. Such a d misses at least one prime factor q of u; since gcd(u,D_T)=1, q>B_T and d≤au/q. Put x=N/(au)=t/a∈[1,T+1]. Then

$$
\frac Nd\ge qx>3(T+1)^2x
\ge 3x^{\log_2 3}.
$$

Because 3^{floor(log_2 x)+1}≤3x^{log_2 3}, this implies m_d>L_{au}. Consequently the inequality e_d>e_{au} is automatic for all exponent choices.

There is no proper odd multiple of au outside the listed block but still ≤N: every odd multiple is bu with odd b≤T. All cross-boundary divisibility comparisons are therefore automatically strict. The block is independent of the remaining coordinates both for the uniform stationary law and every heat-bath update.

If au=bv for two qualifying roots u,v and odd a,b≤T, then because u and v are coprime to every prime ≤B_T≥T, the small-prime part of au equals a and that of bv equals b. It follows that a=b and u=v. Distinct blocks are disjoint.

Counting integers coprime to fixed D_T in an interval of length N/(T(T+1)) by periodic residue classes gives the displayed c_T and O_T(1). This proves (1) and (2).

## Proof of spectral and divisibility transfer

The projected heat-bath operator is exactly

$$
P_n^{(T)}=I+\frac1n\sum_{i=1}^{k_T(n)}Q_T^{(i)}.
$$

The finite heat-bath chain is irreducible by the exchange-connectivity theorem, and Q_T is a sum of self-adjoint conditional-expectation generators. Let λ_T>0 be its smallest positive eigenvalue. Tensor products of the local eigenbasis diagonalize the projected walk; the finite-dimensional χ² upper bound and a sum of independent-copy λ_T eigenfunctions give total-variation cutoff at n(log k)/(2λ_T), with an O_T(n) window. The argument is identical to the complete spectral proof given for the [23-state instance](P027-five-site-arithmetic-blocks-and-mixing-lower-bound.md). Eigenvalues of the projected kernel are nonnegative since it is a convex combination of conditional expectations and the identity. Projection cannot increase total-variation distance, giving (3).

Every configuration of the remaining coordinates extends to exactly F(T)^{k_T(n)} full configurations, proving (4). Taking the supremum over fixed T in the lower bound proves the final inequality. If the infimum of the positive λ_T is zero, the supremum is infinite. □

## Numerical exploration, not an asymptotic claim

The optional SciPy eigenvalue checker enumerates Ω_T exactly, constructs its heat-bath matrix, and computes λ_T numerically; representative values are:

| T | States F(T) | Approx. λ_T |
|---:|---:|---:|
| 6 | 3 | 0.500000 |
| 12 | 6 | 0.500000 |
| 20 | 26 | 0.380383 |
| 36 | 168 | 0.354503 |
| 48 | 816 | 0.381623 |
| 54 | 2208 | 0.270868 |
| 60 | 5056 | 0.279074 |

The sequence **is not monotone** and this finite table does **not** prove inf λ_T=0. The previous exact five-site Rayleigh certificate λ_54≤101/363 supplies a rigorous lower-mixing coefficient, whereas these decimals are exploratory only.

The transfer theorem makes the central research target particularly simple:

> **Do the spectral gaps λ_T of the unnormalised primitive-set heat baths tend to zero along some sequence T→∞?**

This is not a rephrasing of the full-chain mixing question as a tautology: the isolated-copy theorem makes any such sequence into a *rigorous* super-n log n obstruction for the original chain. It does not prove that one exists.

## Source-level caution

The count F(T) and finite arithmetic-template method are strongly connected to [Liu–Pach–Palincza, *The number of maximum primitive sets of integers*](https://doi.org/10.1017/S0963548321000018). The present transfer of a *specific heat-bath spectrum* is internally proved but its originality has not been certified by exhaustive literature review. Compare [Propp–Wilson exact sampling](https://doi.org/10.1002/(SICI)1098-2418(199608/09)9:1/2%3C223::AID-RSA14%3E3.0.CO;2-O) and general distributive-lattice sampling before a separate publication claim.
