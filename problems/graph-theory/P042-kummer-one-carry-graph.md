# P042 — Hamiltonian paths in one-carry graphs

<!-- DOSSIER-SUMMARY -->
> **Research question:** Can the integers 1,...,2^m-1 be ordered so that the sum of each adjacent pair has exactly one binary carry, for every m>=4?
> **Formulation:** candidate. **Novelty:** unverified; Kummer's theorem and binary carry automata are classical, the exact Hamiltonian question needs specialist comparison.
> **Verified/known progress:** Internally proved connectivity for m>=4, exactly two leaves, and an exact edge count ((m+2)3^(m-2)-m)/2.
> **Finite evidence:** Complete graph checks for 2<=m<=8 and independently verified Hamiltonian path witnesses for m=4,5.
> **Navigation:** [Full problem catalogue](../../README.md#problem-catalogue) · [Status and scope](../../README.md#status-and-scope) · [Literature and audits](../../README.md#literature-and-audits)
<!-- /DOSSIER-SUMMARY -->

For $m\ge2$, form the graph on $\{1,\ldots,2^m-1\}$, joining distinct $a,b$ if

$$
v_2\binom{a+b}{a}=1.
$$

By Kummer's theorem, the condition says that **adding $a$ and $b$ in binary produces exactly one carry**.

**Question.** Does this graph have a Hamiltonian path for every $m\ge4$?

## Known results

The [structural theorem](../../theorems/P042-kummer-one-carry-graph.md) establishes that the graph is connected for all $m\ge4$, has exactly two leaves, and has

$$
\frac{(m+2)3^{m-2}-m}{2}
$$

edges. Its only degree-one vertices are $2^{m-1}-1$ and $2^m-1$, necessarily the endpoints of any Hamiltonian path. In particular, a Hamiltonian *cycle* is impossible.

The cases $m=2,3$ are disconnected; complete paths are certified for $m=4,5$. The finite computation does not establish Hamiltonicity for every $m$.

## Computation

The [verifier](../../experiments/P042_kummer_carry_graph.py) checks the exact edge formula, connectivity, and degree-one vertices for $2\le m\le8$, plus the complete Hamiltonian paths for $m=4,5$.

## Prior art

Kummer's theorem identifies $v_2\binom{a+b}{a}$ with the number of binary carries, and the zero-carry case is exactly disjointness of binary supports. These are classical facts, not new results. See A. Granville, *Arithmetic properties of binomial coefficients. I* (1997), [author's publication list](https://dms.umontreal.ca/~andrew/1997.php), and [Kummer's theorem](https://www.cecm.sfu.ca/organics/papers/granville/paper/binomial/html/node3-an.shtml).

The one-carry Hamiltonian problem has not been identified in the targeted searches. Historical novelty and unresolved status are **unverified**.
