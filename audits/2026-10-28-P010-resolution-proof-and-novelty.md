# Adversarial proof and novelty gate — P010 exact resolution

**Date:** 2026-10-28  
**Problem:** P010, minimum coprime adjacencies among permutations of $[n]$.  
**Finding:** A complete exact all-$n$ formula with a constructive proof has been derived **within this project**. Mathematical priority is **not certified**; a specialized independent referee audit is required.

## Formula, edge cases, and proof source

$$
h(n)=
\begin{cases}
n-1,&n=1,2,3,\$$2mm]
\pi(n)-\pi(n/2)+
\max\left\{1,\left\lceil(\pi(n/2)-\pi(n/3))/2\right\rceil\right\},&n\ge4.
\end{cases}
$$

The complete written constructive proof is [here](../theorems/P010-exact-coprime-adjacencies.md).

The additional $\max\{1,\cdot\}$ is **necessary** when $B_n=\pi(n/2)-\pi(n/3)=0$, for instance $n=9$ and $n=21$. Those values were previously thought to be exceptions to the prime-leaf lower bound; they instead demonstrate the need to count at least one nonisolated path component.

## Proof review: what could go wrong?

1. **Noncoprime path-cover equivalence:** Valid. Cutting a permutation at each gcd-one transition creates paths; joining a minimum path cover uses at most one gcd-one transition per join, so $h(n)=\operatorname{pc}(H_n)-1$.
2. **Obstruction accounting:** Valid. The vertex 1 and primes $>n/2$ are isolated. Each prime $q\in(n/3,n/2]$ has the *unique* neighbor $2q$; therefore at most two such primes appear as endpoints of a path. For $n\ge4$, $\{2,4\}$ guarantees a nonempty remaining component even if there are no degree-one primes.
3. **Largest-prime-factor partition:** Classes $C_p$ are cliques. The particular multiples $2p,4p$ stay in $C_p$ because the multipliers 2 and 4 have largest prime factor at most $p$.
4. **Middle-class assumption:** For $n\ge12$ and $n/4<p\le n/3$, $p\ge5$ and $C_p=\{p,2p,3p\}$; there is no stray integer in the class. This matters because the 3-hub connector has a **non-even** endpoint $3p$.
5. **Parity correction:** Pair middle classes by a 3-divisible bridge; if their count is odd, attach the leftover middle class to $C_3$ through the $9\!-\!3p$ edge. Since $n\ge12$, $C_3$ contains 6 and 9, and the resulting unit has two even endpoints. The used class $C_3$ is **not reused** elsewhere.
6. **Even concatenation:** Every two-even-ended unit has distinct even endpoints; different units have disjoint vertices, and any two even integers have gcd at least 2. Their concatenation preserves a simple path with even endpoints.
7. **Capacity to attach leaves:** There are $u=\pi(n/4)+\lfloor(\pi(n/3)-\pi(n/4))/2\rfloor$ even-ended units and only $r=\max(1,\lceil B_n/2\rceil)$ required core paths. The known Rosser–Schoenfeld inequality $\pi(2x)\le2\pi(x)$, for $x\ge3$ (directly check $3\le x\le10$), ensures $B_n\le2\pi(n/4)$ and hence $u\ge r$. At most two leaf classes attach to each path.
8. **Small values:** Explicit permutations witness the optimum for 4 through 11; 1 through 3 have direct answers. These are checked exhaustively by a tiny dynamic program as a secondary test, but the proof itself uses the displayed witnesses plus the lower bound.

The proof has no remaining conditional arithmetic conjecture. It relies on a standard known prime-counting inequality, not on a conjecture about prime gaps.

## Independent numerical checks

- Separate Python implementation grouped the classes by the largest prime factor and checked that the resulting concatenation is a permutation with the predicted objective.
- Every $n=12,13,\ldots,10\,000$ produced a valid constructor; full gcd/coverage checks were made for all small instances and selected larger inputs.
- Independently computed minimum values by a Held–Karp-style dynamic program through $n=15$; the theorem agrees at every case.
- Earlier independent SciPy Hamiltonian MILPs returned the same values for 21, 30, 50, 100, 150 and 200.
- [Portable construction script](../experiments/P010_construct_optimal_permutation.py) tests exact witnesses and is included in the repository's GitHub Actions workflow for all $n\le500$ and a separate $n=10\,000$ instance.

These are implementation audits, **not external proof review**.

## Targeted historical novelty audit

**Primary antecedent.** P. Erdős, R. Freud and N. Hegyvári, *Arithmetical properties of permutations of integers*, *Acta Math. Hung.* 41 (1983), 169–176, https://users.renyi.hu/~p_erdos/1983-02.pdf . The located theorem statements are about the extremal *values* of adjacent gcd/lcm, not the minimum **count** of coprime adjacencies; the latter is a distinct optimization functional.

**Other known machinery.** The noncoprime graph on $[n]$ is a known integer graph, and path-cover optimization is classical, not novel. This solution makes unusual use of $\{p,2p,3p,4p\}$ inside the largest-prime-factor classes and bridge edges through common factors 2 and 3. OEIS [A076220](https://oeis.org/A076220) counts permutations of $[n]$ in which **all** adjacent entries are coprime, the opposite extremum.

**Prime count inequality.** Rosser and Schoenfeld are credited for $\pi(2x)<2\pi(x)$ for $x>10$ in [OEIS A060208](https://oeis.org/A060208); the finite residual interval down to $x=3$ is an elementary direct check. The proof does not need an effective prime number theorem; the prime number theorem is used only for the $7/12$ asymptotic corollary.

**Search terms used:** "minimum number of relatively prime consecutive pairs in a permutation", "maximum noncoprime adjacent pairs permutation", "path cover noncoprime graph integer", "7/12 coprime permutation", "prime-count formula adjacent gcd permutation", "Erdos Freud Hegyvari adjacent gcd count", and exact formula fragments. No exact previous statement or formula surfaced in this targeted search.

**Conclusion:** This is a **valid internally completed candidate theorem**, not yet a **certified original publication-level theorem**. Do not announce priority, a proof of a known open conjecture, or submission readiness without expert and bibliographic review.

## Portfolio decision

**P010 moves from 'candidate question' to 'proved internally'.** The original mathematical question has been resolved; retaining its problem ID and linking to the full proof is preferable to deleting it. P003 and P005 remain open candidates for separate theorem-first passes; no P011 is introduced. This audit supersedes older dated notes describing P010's constant as unknown.
