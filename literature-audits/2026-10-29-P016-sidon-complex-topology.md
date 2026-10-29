# P016 novelty screen — topology of the Sidon complex

**Date:** 29 October 2026  
**Category:** first-pass exact mathematical definition, targeted near-literature search, exact small homology.  
**Status:** *apparent distinctness after a targeted search* only; not verified novel or open.

## Exact complex

The vertices of $K_N$ are $[N]$, and its faces are the sets with all pairwise **positive differences distinct**. Because the property is hereditary, $K_N$ is a genuine abstract simplicial complex, and because its minimal nonfaces consist of three-term progressions and four-distinct-entry collisions, it is an **independence complex of a mixed 3/4-uniform hypergraph**.

Its one-skeleton is complete, but the complex is not flag: $\{1,2,4,5\}$ has all three-element subsets valid while the four-set violates Sidon uniqueness.

The proposed problem asks for eventual vanishing of $\widetilde H_k(K_N;\mathbb F_2)$ for fixed $k$ and the topological distribution of surviving classes as $N$ increases. **No general vanishing theorem is asserted.**

## Computational discovery, not an asymptotic proof

A separate exact GF(2) rank implementation gave:

| $N$ | $\widetilde\beta_1$ | $\widetilde\beta_2$ | $\widetilde\beta_3$ | $\widetilde\beta_4$ |
|---:|---:|---:|---:|---:|
| 5 | 1 | 1 | 0 | 0 |
| 6 | 0 | 4 | 0 | 0 |
| 9 | 0 | 15 | 1 | 0 |
| 11 | 0 | 5 | 20 | 0 |
| 12 | 0 | 0 | 51 | 0 |
| 17 | 0 | 0 | 237 | 5 |
| 20 | 0 | 0 | 81 | 416 |
| 22 | 0 | 0 | 10 | 1404 |
| 23 | 0 | 0 | 0 | 2153 |

These are ranks of exact augmented simplicial boundary maps, **not** persistent homology computed over a real-valued filtration; the nested sequence $K_N\hookrightarrow K_{N+1}$ makes a persistence interpretation possible, but the individual Betti numbers **do not determine persistence maps**. Do not claim barcode results on the basis of these tables.

Reproduction: [experiments/P016_sidon_complex_betti.py](../experiments/P016_sidon_complex_betti.py). The script checks the Euler–Poincaré identity as an independent invariant. Numerical agreement does not certify a general theorem.

## Bibliographic targets and exact overlaps

1. **Sidon/Golomb ruler extremal theory**: [MathWorld](https://mathworld.wolfram.com/SidonSet.html), and **Carter, O'Bryant and Tao**, [*On the diameter and distribution of Sidon sets*, arXiv 2610.36207 (26 October 2026)](https://arxiv.org/abs/2610.36207). The latter very recent work concerns quantitative extremal geometry, **not** the reduced homology of all Sidon subsets.
2. **Sidon-related simplicial complexes**: **Matt Superdock**, [*Simplicial complexes from finite projective planes and colored configurations*, Discrete Mathematics 346 (2023), 113117](https://doi.org/10.1016/j.disc.2022.113117). This is the most important near-collision to read deeply. It derives topological constructions from colored configurations related to Sidon sets and linear codes. The complex in that paper is built from **incidence configurations**, rather than obviously being the hereditary complex of all Sidon subsets of $[N]$. Do not infer complete novelty from this distinction alone.
3. **Hypergraph independence-complex topology**: [Berghoff (2022), *On the homology of independence complexes*](https://doi.org/10.5070/C62156880). Tools and generic constraints are established, and P016 may be a special case of powerful homological vanishing results for dense hypergraphs.
4. **Topological additive relations**: [*Persistent Homology of Additive Relations* (2026)](https://www.researchgate.net/publication/404901446_Persistent_Homology_of_Additive_Relations). A potential close neighboring concept. It defines additive-fiber relative complexes and weighted graph clique complexes, **not evidently** all Sidon subsets of a fixed integer interval. Need check original manuscript and provenance before assigning priority.

Exact search strings included: "Sidon simplicial complex homology", "Golomb ruler complex Betti numbers", "independence complex of Sidon hypergraph", "homotopy type of Sidon subsets", "simplicial complexes from Sidon sets", and "additive quadruple independence complex". **No exact predecessor located in accessible results. This is a search limitation, not a discovery certificate.**

## Structural meaning and promotion decision

If the fixed-dimensional reduced homology eventually vanishes, it may be possible to derive a connectivity law for a naturally increasing family of non-flag complexes whose forbidden faces are precisely additive collisions. The analogy with the Sidon-exchange graph (P004) is motivating but does **not** establish any implication; different state-space invariants can behave differently.

**Candidate promotion justified provisionally** by (1) a clean invariant, (2) exact reproducible experiments, (3) a crisp problem with either positive or negative answers of mathematical consequence, and (4) a bibliographic assessment identifying the most threatening predecessor. It remains *apparent novelty*, not a certified open problem.
