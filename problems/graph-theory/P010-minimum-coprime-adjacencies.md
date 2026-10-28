# P010 — How few coprime adjacencies can a permutation have?

**Area:** arithmetic graph theory, Hamiltonian path cover, prime distribution  
**First proposed:** 2026-10-28  
**Status:** candidate extremal question, **novelty and unresolved status unverified**

## Statement

For any permutation \((a_1,\ldots,a_n)\) of \([n]=\{1,\ldots,n\}\), call an adjacent pair *coprime* if \(\gcd(a_i,a_{i+1})=1\). Define
\[
h(n)=\min_{(a_1,\ldots,a_n)}
\left|\{i:1\le i<n,\ \gcd(a_i,a_{i+1})=1\}\right|.
\]

**Main question:** Determine the asymptotic growth of \(h(n)\). In particular, does the limit
\[
\lim_{n\to\infty}\frac{h(n)\log n}{n}
\]
exist, and if so is it \(7/12\)? This sharp-constant guess is **speculative**, not established by small data.

## Graph-theoretic reformulation

Let \(H_n\) have vertices \([n]\), joining distinct \(a,b\) iff \(\gcd(a,b)>1\). In the sequence \(a_1,\ldots,a_n\), delete every adjacent coprime edge. What remains is a cover of all vertices by \(h(n)+1\) vertex-disjoint paths in \(H_n\) (single vertices count as paths).

Conversely, joining any minimum path cover of \(H_n\) into one permutation uses at most one coprime edge per join. Hence
\[
\boxed{h(n)=\operatorname{pc}(H_n)-1},
\]
where \(\operatorname{pc}\) is the minimum vertex-disjoint path-cover number. This equality is an elementary reformulation, **not a new general graph theorem**.

## A rigorous prime-obstruction bound

Let \(\pi(x)\) be the prime-counting function and put
\[
A_n=\pi(n)-\pi(n/2),\qquad
B_n=\pi(n/2)-\pi(n/3).
\]

**Theorem (elementary bounds).** For every \(n\ge2\),
\[
\boxed{A_n+\left\lceil B_n/2\right\rceil\le h(n)\le\pi(n).}
\]
In particular, by the prime number theorem,
\[
\boxed{
\left(\frac7{12}+o(1)\right)\frac{n}{\log n}
\le h(n)\le
(1+o(1))\frac{n}{\log n}.
}
\]

**Proof (lower bound).** In \(H_n\), vertex \(1\) is isolated. Every prime \(p\in(n/2,n]\) is also isolated, since there is no second multiple of \(p\) in \([n]\). Thus these vertices alone force \(1+A_n\) separate paths in any path cover.

Every prime \(q\in(n/3,n/2]\) has **exactly one neighbor** in \(H_n\), namely \(2q\): since \(3q>n\), no other positive multiple of \(q\) can appear. There are \(B_n\) such degree-one vertices, which are distinct from the isolated vertices. Each additional path can contain at most two of them, as they must be endpoints of their paths. Hence every path cover has at least \(1+A_n+\lceil B_n/2\rceil\) paths. Subtracting one gives \(h(n)\ge A_n+\lceil B_n/2\rceil\).

**Proof (upper bound).** Partition \(\{2,\ldots,n\}\) into classes by **largest prime divisor**. Every pair of integers in the same class shares that prime divisor, so each class can be written as one non-coprime path. There are exactly \(\pi(n)\) nonempty classes, one for each prime \(p\le n\). Add the singleton path \(\{1\}\). Joining these \(\pi(n)+1\) paths requires at most \(\pi(n)\) coprime adjacencies. The prime number theorem converts the inequalities into the displayed asymptotic bounds. \(\square\)

## Exact optimization

The program [`experiments/minimum_coprime_adjacencies.py`](../../experiments/minimum_coprime_adjacencies.py) solves a binary Hamiltonian-tour MILP on the complete graph \(\{0,1,\ldots,n\}\), with dummy vertex \(0\) and objective
\[
\min\sum_{1\le i<j\le n:\,\gcd(i,j)=1}x_{ij}.
\]
Degree-two constraints, iterative subtour-elimination cuts, and a final connected-tour check certify the global optimum when the solver returns status 0. The two dummy edges have zero cost.

| \(n\) | Rigorous lower bound | Certified minimum \(h(n)\) |
|---:|---:|---:|
| 5 | 3 | 3 |
| 9 | 2 | 3 |
| 12 | 3 | 3 |
| 21 | 4 | 5 |
| 30 | 5 | 5 |
| 50 | 8 | 8 |
| 60 | 8 | 8 |
| 80 | 12 | 12 |
| 100 | 12 | 12 |
| 120 | 16 | 16 |
| 150 | 17 | 17 |
| 200 | 25 | 25 |

Thus the finite lower bound is **not** universally exact: \(n=9\) and \(n=21\) are explicit failures. These exceptions are why the asymptotic constant, rather than an unqualified exact formula, is the research target.

Use
```sh
python experiments/minimum_coprime_adjacencies.py --n 80 --seconds 120
```
to recompute an instance (requires SciPy and NumPy). Solver time may increase greatly with \(n\); timeouts are *not* optimality certificates.

## Crucial prior art

**This is firmly in an existing mathematical tradition.**

- **P. Erdős, R. Freud and N. Hegyvári**, [*Arithmetical properties of permutations of integers*](https://users.renyi.hu/~p_erdos/1983-02.pdf), *Acta Mathematica Hungarica* **41** (1983), 169–176, study gcd and lcm of *successive entries of permutations*. They optimize the **sizes** of adjacent lcm/gcd values, rather than this exact **number of coprime adjacencies**; nevertheless this is the closest historical antecedent and requires checking the whole paper and its citations before asserting novelty.
- [*Non-Coprime Graph of Integers*](https://ijmttjournal.org/archive/ijmtt-v66i2p513) (2020) defines the noncoprime graph with isolated vertices removed and studies standard invariants such as girth, chromatic number and domination. Our \(H_n\) retains the isolated vertices and asks for its minimum path-cover number. The underlying graph is **not new**.
- [OEIS A076220](https://oeis.org/A076220) counts permutations in which **every** adjacent pair is coprime; this is the opposite optimization extreme, not the minimum-count sequence defined here.

**Status:** no direct resolution of the asymptotic constant was located in targeted queries, but a definitive literature novelty check has not been completed. A comprehensive search should include "path cover of noncoprime graph", "fewest relatively prime adjacencies", "maximum noncoprime adjacent pairs" and the 1983 paper's citations.

## Possible proof program

- Analyze primes in \((n/(k+1),n/k]\), where a prime \(p\) has precisely \(k-1\) neighbors in the noncoprime graph; determine which degree constraints cause further asymptotic path-cover obstructions.
- Construct a path decomposition with \((7/12+o(1))n/\log n\) components, or find a stronger universal lower constant by graph cut/leaf-capacity arguments.
- Derive dual certificates from the Hamiltonian-path MILP and identify structural families explaining the finite exceptions \(n=9,21\).
- Explore whether smooth-number distribution and Euler's totient estimates control the middle-sized-number component.
