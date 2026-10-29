# Discovery screen — P017 and P018 (29 October 2026)

**Purpose.** Generate distinct, structurally meaningful problems without reopening the original theorem-first research cycle. This report separates mathematically exact preliminary findings, finite observations and claims requiring genuine historical priority review.

## Candidate P017 — Percolation on the divisibility order

**Question.** If each integer in $[N]$ is independently retained with probability $p\in(0,1)$, and $L_N(p)$ is the length of the longest strict divisibility chain of retained integers, does

$$
\frac{L_N(p)}{\log_2 N}\xrightarrow{\mathbb P}c(p)
$$

for a deterministic nontrivial $c(p)$?

**Elementary validation:** the powers of two form a chain whose retained length is binomial with $\lfloor\log_2N\rfloor+1$ trials. Therefore

$$
p-o_{\mathbb P}(1)\le\frac{L_N(p)}{\log_2 N}\le1+o(1).
$$

The lower bound is not necessarily sharp, because a chain may use different prime coordinates. The finite-sample dynamic program at $N=2^{16}$ gives approximate mean normalized heights $0.50,0.747,0.934$ for $p=0.2,0.5,0.8$ respectively (20 samples each). This does **not** imply convergence.

**Nearest published mathematics, and the exact gap:**
- **Kohayakawa, Kreuter and Osthus** (2000), [*The length of random subsets of Boolean lattices*](https://doi.org/10.1002/%28SICI%291098-2418%28200003%2916%3A2%3C177%3A%3AAID-RSA4%3E3.0.CO;2-9), studies random **Boolean** inclusion chains. Prime exponent vectors embed the integer divisibility poset in a product of chains, but the product bound $m\le N$ imposes a highly nonrectangular constraint.
- **Lewis–Souza**, [*The order dimension of divisibility* (2021)](https://www.sciencedirect.com/science/article/pii/S0097316520301837), and [*Improved bounds for the dimension of divisibility* (2023)](https://doi.org/10.1016/j.ejc.2023.103912), study a **different deterministic invariant** of the same divisibility partial order.
- [OEIS A394685](https://oeis.org/A394685) counts order-convex subsets of the integer divisibility poset, again not longest chains after independent site thinning.
- [Huber, *Antichains among Divisor Sums of Divisors* (October 2026)](https://arxiv.org/abs/2610.02264) illustrates very active current research in divisibility-poset width; it is not this random height process.

**Novelty:** exact Bernoulli-thinned integer divisor-chain limit not found in targeted accessible sources. **No claim of certified originality.** Risk: closely related random poset height theory may supply an existing answer after a more complete citation search.

## Candidate P018 — Fixed-XOR binary-matroid basis fibers

**Question.** For $W\subset\mathbb F_2^d\setminus\{0\}$ and fixed nonzero $s$, consider all vector-space bases $B\subseteq W$ with XOR of the members equal to $s$. Connect bases by replacing **exactly two** vectors at a time while keeping both independence and XOR. Characterize when the fiber graph is connected. What larger uniform exchange size ensures connectivity for arbitrary $W$? Under random deletion of available vectors, how does connectivity differ from existence?

**Important triviality removed:** single-vector exchanges cannot change a basis while conserving total XOR (the replacement would be forced to equal the removed vector). Two-vector exchanges are the minimal meaningful local move.

**Verified finite structural contrast:**
- $d=4$: for a fixed nonzero total $s$, 56 full-ground-set bases have that label, and the two-exchange graph of their restriction to **every one** of $2^{15}=32,768$ available-vector sets $W$ was connected whenever it contained at least two bases. By linear symmetry the same statement holds for any nonzero $s$.
- $d=5$: the explicit ten-vector set

$$
W=\{2,5,8,11,21,22,24,26,27,30\}
$$

with binary-vector encoding and total XOR $1$ has six valid bases in **two components of sizes four and two**. This is a rigorous finite counterexample to universal two-exchange connectivity, fully listed in the dossier. The exact test is independently reproducible.

**Closest published mathematics:**
- **Hörsch, Imolay, Mizutani, Oki and Schwarcz**, [*Problems on Group-labeled Matroid Bases* (2024)](https://arxiv.org/abs/2402.16259): **central predecessor**, studies bases with a prescribed or restricted group-sum label. The *definition of group-conserved bases is not original*.
- [*Towards the Proximity Conjecture on Group-Labeled Matroids* (ICALP 2025)](https://doi.org/10.4230/LIPIcs.ICALP.2025.85): proximity bounds for groups of allowable labels. Does not evidently address this precise conserved-XOR **fiber connectivity** problem.
- **Lubiw and Pathak** (2016), [*Reconfiguring Ordered Bases of a Matroid*](https://arxiv.org/abs/1612.00958): basis reconfiguration with **positional labels**, a distinct constraint.
- [*Reconfiguration of basis pairs in regular matroids* (2026)](https://doi.org/10.1016/j.jctb.2025.10.009), related to **White's matroid basis exchange conjecture**, concerns sequences/pairs of bases, not automatically a single basis with fixed XOR.

**Novelty:** the particular two-element conserved-XOR fiber and d4–d5 threshold were not found stated in these sources. They may be an easy consequence of algebraic statistics, coding theory or matroid toric ideals; do not claim they are historically new until full papers have been checked.

## Why these two are provisionally worth listing

P017 crosses probabilistic combinatorics with the arithmetic geometry of the divisibility poset. P018 crosses matroid exchange and a conserved algebraic statistic, showing an **actual low-dimensional obstruction** and asking for a classification rather than extrapolating connectivity. Their main problems differ from the original prime-sum/coprime/Sidon cluster.

Each problem has precise quantifiers, the strongest obvious easy theorem or counterexample included, a direct nearest-literature section, a reproducible test script, and explicit unresolved questions. They fit the plan to reach **around 25 selectively chosen entries**, then freeze and consolidate.

## Editorial recommendation for the next passes

Advance in batches of **two to three**; keep mathematical status and priority separate. Reject:
- known statements dressed in new notation;
- statements solved immediately by a generic theorem;
- dependent-model "threshold" claims for **nonmonotone events** stated without the requisite conditioning;
- numerical patterns without a coherent structural question;
- variants that only relabel P001–P016.

When the total reaches roughly 23–25, suspend new submissions and conduct a problem-by-problem contradiction, bibliography and Markdown audit before selecting a smaller flagship set. The number 25 is a **ceiling, not a required quota**.
