# P027 — Autonomous coordinates, exact hypercube projection and a mixing lower bound

**Status:** internally proved structural and mixing-time statements. These do **not** establish the mixing order, upper mixing bound or cutoff of the full P027 chain. Historical originality is **not certified**.

## Model

Let N=2n. A maximum primitive subset A of [N] has exactly one element from every dyadic chain indexed by odd u≤N. Write that element as u2^{e_u}, and let

$$
m_u=\max\{j:3^ju\le N\},\qquad
L_u=\max\{j:2^ju\le N\}.
$$

By the [exact exchange theorem](P027-primitive-set-exchange-diameter.md), valid configurations are the integer vectors satisfying

$$
0\le e_u\le L_u,\qquad
e_u>e_v\quad\text{for every proper odd multiple }v\text{ of }u,\ v\le N.
$$

Both m=(m_u) and L=(L_u) are feasible and bound every valid e coordinatewise. The heat-bath walk P_n chooses one of the n odd indices uniformly and resamples its exponent uniformly from the interval preserving all inequalities. It is reversible for the uniform distribution on maximum primitive subsets.

Call u **autonomous** when m_u<L_u and, after specifying *any* feasible values of all other coordinates, *every* integer in [m_u,L_u] remains feasible for e_u. Unlike a free variable under a particular conditioning, this is a global product-factor property.

## Theorem 1 — Exact arithmetic classification of autonomous coordinates

For N≥12 and odd u≤N, u is autonomous if and only if it belongs to one of the following five disjoint classes:

1. N/3 < u ≤ N/2 and gcd(u,6)=1.
2. N/6 < u ≤ N/4 and gcd(u,30)=1.
3. N/6 < u ≤ 5N/27, gcd(u,6)=1 and 5 divides u.
4. N/12 < u ≤ N/9 and gcd(u,210)=1.
5. N/12 < u ≤ 7N/81, gcd(u,30)=1 and 7 divides u.

Every autonomous coordinate has **exactly two** possible exponents: 0,1 in the first class; 1,2 in the second and third; 2,3 in the fourth and fifth.

If k_n is their total number, then

$$
\boxed{k_n=\frac{1454}{8505}n+O(1).}
$$

The error is bounded uniformly in n, since the count in each class involves only a fixed collection of residue classes modulo 6, 30 or 210.

### Proof

A proper odd divisor d of u imposes e_d>e_u. The smallest possible e_d equals m_d, and the largest feasible e_u equals L_u; therefore its constraint is automatically inactive precisely when m_d>L_u. Similarly, a proper odd multiple v of u imposes e_u>e_v and is automatically inactive precisely when L_v<m_u. Necessity follows by fixing the other coordinates respectively to m or L, both feasible.

For u>1 let q be its smallest odd prime factor. The largest proper odd divisor u/q minimizes m_d. Among proper odd multiples, 3u (when at most N) maximizes L_v. Consequently u is autonomous exactly when

$$
m_u<L_u,\qquad
\left\lfloor\log_3(qN/u)\right\rfloor>L_u,
\qquad
3u>N\ \ \text{or}\ \
\left\lfloor\log_2(N/(3u))\right\rfloor<m_u.
$$

When u=1 the divisor inequality is omitted; N≥12 guarantees that this coordinate is not autonomous.

Put t=N/u. An elementary examination of the last inequality together with m_u<L_u shows that the only possible bands for t are

$$
2\le t<3,\qquad 4\le t<6,\qquad 9\le t<12.
$$

Indeed, 1≤t<2 and 3≤t<4 have m_u=L_u; the descendant inequality fails for 6≤t<9 and every t≥12. For the latter claim, if t≥27 and j=floor(log_3 t)≥3, then t/3≥3^{j-1}≥2^j, so floor(log_2(t/3))≥j. On 12≤t<27 the same inequality follows from m_u=2 and t/3≥4.

In the three surviving bands, (m_u,L_u) equals respectively (0,1), (1,2), (2,3). The proper-divisor requirement becomes qt≥9, qt≥27, qt≥81. In the first band this forces q≥5. In the second, either q≥7, or q=5 with t≥27/5. In the third, either q≥11, or q=7 with t≥81/7. Writing the smallest odd prime-factor conditions as coprimality restrictions gives exactly the five classes.

Counting the classes by elementary periodic residue densities gives

$$
\begin{aligned}
k_n
&=\left(\frac19+\frac{2}{45}+\frac1{405}
+\frac4{315}+\frac2{8505}\right)n+O(1)\\
&=\frac{1454}{8505}n+O(1).
\end{aligned}
$$

Each class has mutually compatible independent choices, since all divisibility constraints incident to its coordinates are automatically strict; the same holds simultaneously across all five classes. This proves the theorem. □

## Theorem 2 — Exact product and spectral decomposition

Let F_n be the k_n autonomous coordinates and let Ω_n^core be the feasible vectors on the remaining n−k_n odd indices. Then

$$
\boxed{\Omega_n\cong \{0,1\}^{k_n}\times\Omega_n^{\mathrm{core}}}
$$

as uniform probability spaces. The binary labels record whether each autonomous exponent is at its minimum or maximum.

Let H_k denote the random-scan heat-bath walk on k independent fair bits, and R_n the same heat-bath process normalized to select among the n−k_n *core* coordinates. The full transition kernel satisfies the **exact operator identity**

$$
P_n=\frac{k_n}{n}(H_{k_n}\otimes I)
+\frac{n-k_n}{n}(I\otimes R_n).
$$

In particular the Walsh character indexed by any subset S⊆F_n is an eigenfunction with eigenvalue 1−|S|/n. More generally the full spectrum, with multiplicities, is

$$
\left\{1-\frac{|S|}{n}
-\frac{n-k_n}{n}(1-\lambda):
S\subseteq F_n,\ \lambda\in\mathrm{Spec}(R_n)\right\}.
$$

For k_n≥1 and n−k_n≥1, if the spectral gap is 1 minus the second-largest eigenvalue, then

$$
\boxed{\gamma(P_n)=\min\left\{\frac1n,\,
\frac{n-k_n}{n}\gamma(R_n)\right\}.}
$$

### Proof

Theorem 1 makes every autonomous bit unconstrained by all other coordinates. Hence each core state extends to precisely 2^{k_n} full states; the uniform law factors. A heat-bath update of an autonomous coordinate resets an independent fair bit, while an update of a core coordinate leaves all autonomous bits alone. This proves the kernel identity.

Walsh characters diagonalize H_k and have eigenvalues 1−|S|/k. The two tensor summands commute, so tensor products of their eigenfunctions give the stated spectrum and gap formula. The residual core chain is irreducible by the exchange-connectivity theorem; all heat-bath coordinate kernels are conditional-expectation (positive semidefinite) operators. □

## Corollary — Exponentially growing power-of-two divisibility

Let f(n) be the number of maximum primitive subsets of [2n], the established integer sequence [OEIS A174094](https://oeis.org/A174094). The exact product factorization implies the **integer divisibility**

$$
\boxed{2^{k_n}\mid f(n),\qquad
\nu_2(f(n))\ge\frac{1454}{8505}n+O(1).}
$$

This is stronger in a different direction than an exponential **lower bound on the numerical size** of f(n): it controls an arithmetic prime-power divisor of the count. The proof is immediate from Theorem 2, and **historical priority of this divisibility consequence is not established**. The counting paper of Liu–Pach–Palincza and references on OEIS A174094 must be compared before any novelty claim.

## Theorem 3 — Cutoff of the projected chain and lower bound for P027

Let Y_t be the projection of the full chain onto F_n. Start all its bits at 0, and write k=k_n. Then for every integer t≥0 the chi-squared distance from the uniform law π_k is **exactly**

$$
\boxed{\chi^2(\mathcal L(Y_t)\Vert\pi_k)
=\sum_{j=1}^k \binom kj(1-j/n)^{2t}.}
$$

The projected walk exhibits a total-variation cutoff at (n/2)log k_n with window O(n), in the sense that, for any sequence a_n→∞,

$$
\begin{aligned}
\left\|\mathcal L(Y_{\lfloor (n/2)(\log k_n-a_n)\rfloor})-\pi_k\right\|_{\mathrm{TV}}&\longrightarrow1
&&\text{when the displayed time is nonnegative},\\
\left\|\mathcal L(Y_{\lceil (n/2)(\log k_n+a_n)\rceil})-\pi_k\right\|_{\mathrm{TV}}&\longrightarrow0.
\end{aligned}
$$

In the first assertion it suffices to take a_n=o(log k_n); if a_n exceeds log k_n, replace the time by zero, where the conclusion also holds.

For the **full** walk, for every fixed 0<ε<1,

$$
\boxed{t_{\mathrm{mix}}(P_n,\varepsilon)
\ge\frac n2\log k_n-O_\varepsilon(n)
=\frac n2\log n-O_\varepsilon(n).}
$$

### Proof

Represent bits by spins X_i∈{−1,+1}, started all at +1. For a nonempty subset S of j bits, its product χ_S changes only when one of its j sites is refreshed, whereupon its conditional expectation becomes zero. Hence E χ_S(Y_t)=(1−j/n)^t. Orthogonality of Walsh characters under π_k and the definition of chi-squared distance give the exact sum.

For the upper window, use (1−j/n)^{2t}≤exp(−2jt/n):

$$
\chi^2\le (1+e^{-2t/n})^k-1
\le \exp(k e^{-2t/n})-1,
$$

and total variation is at most one half the square root of chi-squared.

For the lower window, let M_t=Σ_i X_i(t). Then

$$
\mathbb E M_t=k(1-1/n)^t,\qquad
\mathrm{Var}(M_t)\le k,
$$

because for distinct i,j,

$$
\mathrm{Cov}(X_i(t),X_j(t))
=(1-2/n)^t-(1-1/n)^{2t}\le0.
$$

Under π_k, E M=0 and Var(M)=k. Chebyshev's inequality at the midpoint of these expectations implies TV≥1−8k/(E M_t)^2. At t=(n/2)(log k−a_n)+O(1), the ratio (E M_t)^2/k tends to exp(a_n), proving the lower cutoff assertion. Because k_n/n→1454/8505>0, these estimates have window O(n).

Finally, total variation cannot increase under projection, so the full chain is at least as far from equilibrium as this projection started at a consistent full configuration. Taking fixed sufficiently large negative window constants gives the claimed mixing-time lower bound. □

## General monotone coupling: known framework, not a mixing upper bound

For a fixed configuration of all other coordinates, the allowable range for e_u is

$$
\left[
\max\left(0,1+\max_{\substack{v>u,\ u\mid v\\v\text{ odd}}}e_v\right),\
\min\left(L_u,\min_{\substack{d<u,\ d\mid u\\d\text{ odd}}}(e_d-1)\right)
\right],
$$

with absent maxima/minima omitted. Both endpoints are nondecreasing functions of other coordinates. Using the same coordinate and uniform quantile for two ordered exponent vectors gives a monotone grand coupling. This allows *exact sampling by coupling from the past* in principle, but **gives no polynomial coalescence or mixing-time bound** by itself.

This is an application of the classical [Propp–Wilson exact sampling framework](https://doi.org/10.1002/(SICI)1098-2418(199608/09)9:1/2%3C223::AID-RSA14%3E3.0.CO;2-O), whose order-ideal examples also include **exponentially slow** chains. Do not infer rapid mixing merely from distributivity or monotonicity.

## Independent checks and current research gap

The [standard-library verification program](../experiments/P027_autonomous_coordinates.py) confirms the arithmetic classification for n≤1000, checks its product-factor property by enumerating all feasible exponent configurations for n≤30, and independently verifies the Walsh eigenfunction relation and first-step distributions on small state spaces.

For extra spectral evidence, the optional [SciPy-based full-chain eigensolver](../experiments/P027_full_heatbath_spectrum.py) computes finite-n gaps. Some observed n·gap values are below 1, so the free-bit gap 1/n **does not automatically determine the full gap**.

**What remains:** Establish or disprove a polynomial upper bound on γ(R_n)^{-1}, and in particular whether the full chain has mixing time Θ(n log n) or cutoff. Theorems 1–3 prove a sharp **projection** cutoff only.

## Source and novelty gates

- [Liu, Pach, Palincza (2021), *The number of maximum primitive sets of integers*](https://doi.org/10.1017/S0963548321000018), already studies the same maximum primitive sets, their dyadic partition and counting asymptotics. **These are prior art, not original here.**
- [Propp–Wilson (1996), *Exact sampling with coupled Markov chains and applications to statistical mechanics*](https://doi.org/10.1002/(SICI)1098-2418(199608/09)9:1/2%3C223::AID-RSA14%3E3.0.CO;2-O), establishes generic distributive-lattice monotone sampling and warns of exponential bottlenecks.
- [Windisch (2018), *Heat-bath random walks with Markov bases*](https://doi.org/10.1016/j.aam.2017.08.002), treats general heat-bath dynamics; its results should not be presumed to cover this growing-dimensional arithmetic model.
- [Alexeev, Barreto, Li, Lichtman, Price, Shah, Tang, Tao (2026), *Primitive sets and von Mangoldt chains*](https://arxiv.org/abs/2605.00301), uses **different** Markov-chain methods to bound weighted primitive-set sums; not an analysis of the uniform finite primitive-set heat bath.

**Historical novelty remains unverified.** This is an internally rigorous structural pass, not a completed solution of P027 or a publication-ready originality claim.
