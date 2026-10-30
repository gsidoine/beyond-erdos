# P033 — Does the first prime after n connect the prime-sum graph?

<!-- DOSSIER-SUMMARY -->
> **Research question:** If q is the smallest prime greater than n, is the graph on [n] joining a,b when a+b is prime and at most q always connected?
> **Formulation:** candidate. **Novelty:** not certified; prime-sum graph connectivity may subsume this restriction.
> **Verified/known progress:** q is an information-theoretic sharp lower bound on the largest edge-sum in any spanning tree; limited-sum graph connectivity is the exact target.
> **Finite evidence:** Exact connected-component searches for finite n, with a reproducible standard-library checker.
> **Navigation:** [Full problem catalogue](../../README.md#problem-catalogue) · [Status and scope](../../README.md#status-and-scope) · [Literature and audits](../../README.md#literature-and-audits)
<!-- /DOSSIER-SUMMARY -->

**Area:** graph theory and additive prime number theory. **Status:** candidate under historical review.

## The question

Let q(n) be the **smallest prime strictly greater than n**. Join distinct i,j∈[n] whenever i+j is prime and i+j≤q(n).

**P033.** Is this graph connected for every n≥2?

Equivalently, can one always find a spanning tree on [n] whose edge sums are prime and **at most the first prime after n**?

## Sharp necessary threshold

Any spanning tree uses at least one edge incident to n. Such an edge has sum n+j>n, hence a *prime* sum must be at least q(n). Therefore **no smaller maximum edge-sum can ever suffice**. The problem asks whether this obvious extremal lower bound is always attained.

Bertrand's postulate ensures q(n)<2n for n≥2, so an edge with sum q(n) is available; it does not by itself imply the entire restricted graph is connected.

The [exact finite verifier](../../experiments/P033_first_prime_connectivity.py) tests the connectivity claim, with a separate check that every spanning tree must include an edge whose sum exceeds n. These are finite observations, not a proof for all n.

## Historical boundaries

- [Chen–Fu–Guo, *Hamiltonicity in Prime Sum Graphs*](https://doi.org/10.1007/s00373-020-02241-1): stronger spanning-cycle existence in the *unrestricted* graph, but not necessarily with sums ≤q(n).
- [Croot–Jin, *Prime Sum Graphs and the Induced Trees They Contain*](https://doi.org/10.1007/s00373-025-02999-2): established graph structure.
- [Brendan McKay's prime-sum Hamiltonian path question](https://mathoverflow.net/questions/450427/hamiltonian-paths-in-the-prime-sum-graph): similar host graph and substantially stronger unrestricted path properties.

**Source hazard:** search prime-sum *tree bottlenecks* and bounded-sum connectivity explicitly. If a general spanning-tree construction with sums at most the least prime above n is already known, this entry should be marked proved/known instead of advertised as an open problem.
