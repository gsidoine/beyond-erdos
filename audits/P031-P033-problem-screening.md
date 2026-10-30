# Source screening: three short arithmetic and graph-theoretic questions

This is a *bounded* historical-priority and mathematical screening, not a claim that all three candidate questions are certified novel or unresolved. Each question is stated in one sentence in the catalogue and has a full linked dossier and reproducible finite verifier. The main research portfolio remains [P001–P030](portfolio-consolidation-P001-P030.md) as an **archived assessment of its first thirty entries**; the catalogue is open to further contributions.

## Selected

| Entry | Short question | Strongest baseline | Literature hazard |
|---|---|---|---|
| [P031](../problems/number-theory/P031-coprime-sidon-extremum.md) | How large can a pairwise-coprime Sidon set be? | Established leading upper constant 1; lower bound ≫√(N/log N) from prime sets and arbitrary-subset Sidon extraction | [Bailleul–Riblet 2026](https://arxiv.org/abs/2605.03181); [modern Sidon distribution](https://arxiv.org/abs/2610.36207) |
| [P032](../problems/graph-theory/P032-prime-sum-bipartite-diameter.md) | Does the two-copy prime-sum graph eventually have diameter seven? | Unique sum-two bridge and a reduction to prime-difference witnesses; diameters computed through n=250 | [Erdős #17](https://www.erdosproblems.com/17), prime-difference coverage; [Croot–Jin](https://doi.org/10.1007/s00373-025-02999-2) |
| [P033](../problems/graph-theory/P033-prime-sum-three-palette.md) | Can three prime sums connect all integers [n]? | Exact twin-prime characterization when two colors suffice; verified κ(n)≤3 through n=120 | [Prime-sum Hamiltonian paths / twin-prime reflections](https://mathoverflow.net/questions/241569/for-which-n-is-there-a-permutation-such-that-the-sum-of-any-two-adjacent-eleme); [Chen–Fu–Guo](https://doi.org/10.1007/s00373-020-02241-1) |

The P032 and P033 formulations share the prime-sum host with earlier entries but study *different invariants*: graph diameter under two-copy parity constraints versus connectivity after selecting at most three **edge-sum colors**. They do not solve P001/P003 prime-sum matching packing or P026 four-cycle homology.

## Three attractive-sounding candidates discarded

**The next prime connects the graph.** Let q(n) be the smallest prime >n and retain all prime-sum edges a+b≤q(n) on [n]. The graph is **always connected** for n≥2: from n to n+1 the allowable prime ceiling never decreases, and Bertrand's postulate gives an edge from the new vertex n+1 to q(n+1)−(n+1)∈[1,n]. Base case n=2 is the edge 1–2 with sum 3. This is a short proof, so the question must **not** be advertised as open.

**Prime-sum rainbow forests.** One might ask for a forest containing an edge with sum q for every prime q appearing among sums of distinct numbers in [n]. This is **immediate**: take exactly those consecutive edges {i,i+1} for which 2i+1 is prime. They form a subgraph of the path 1–2–…–n and realize every relevant odd prime q≤2n−1. No new open problem remains.

**Edge coloring the coprime graph.** The graph on [n] with ij adjacent when gcd(i,j)=1 has the universal vertex 1 and Δ=n−1. A general [universal-vertex edge-coloring theorem](https://www.sciencedirect.com/science/article/abs/pii/S0166218X23004468) says that such a graph is Class 1 exactly when it is **not overfull**. For odd n=2k+1≥7, its k even vertices already yield at least C(k,2)≥k missing edges, so it is not overfull. For even n, a 1-factorization of K_n gives a Δ-edge coloring. The cases n=3,5 are overfull. Thus the tempting conjecture that the coprime graph is Class 1 for every n≥7 is **already an easy consequence of published theory**, and is not a new catalogue candidate.

## P027: structural result and its limitation

The [finite-template transfer theorem](../theorems/P027-finite-arithmetic-template-transfer.md) proves that every fixed maximum primitive-set model on [T] appears in linearly many independent copies within sufficiently large [2n]. It transfers the unnormalised finite-model heat-bath gap λ_T to a global lower bound t_mix(n,ε)/(n log n)≥1/(2λ_T) in liminf. If inf_T λ_T=0, the full chain necessarily mixes in super-n log n time. The theorem **does not establish that infimum condition**, nor a full-chain upper bound or cutoff.

Numerical state enumerations for T≤60 have no monotone spectral trend and should not be promoted to a conjecture without further evidence. The [Liu–Pach–Palincza maximum primitive-set counting paper](https://doi.org/10.1017/S0963548321000018) is a crucial predecessor for finite arithmetic configurations.

## Standards for follow-up

Before elevating a candidate: identify any exact historical equivalent, check all small obstructions and parity constraints, and prove something that is not already an immediate corollary of a named theorem. A finite verification range is evidence against small counterexamples, **not an infinite proof**. Contributions may add further problems without a fixed numerical cap.
