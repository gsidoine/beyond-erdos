# Consolidated research portfolio — P001–P030

**Scope.** The canonical [catalogue](../README.md#problem-catalogue) has exactly 30 numbered entries P001–P030. This report independently evaluates their *formulation*, *mathematical evidence*, *closest historical relationships*, *portfolio overlap* and *next falsification target*. It supersedes older catalogue-ranking snapshots **as editorial guidance**, but it does not overwrite their historical source records.

**Interpretation.** A permanent catalogue ID means only that a research question or resolved result is documented. It is **not** certification that its mathematical formulation is new, is open in the literature, or merits journal publication. An internally proved theorem is distinguished from a theorem independently refereed; a finite computation is not a universal proof.

## Current catalogue integrity

The canonical index has **26 candidates, 2 reformulation flags (P007, P025), 1 specification flag (P008), and 1 internally proved/resolved entry (P010)**. All 30 IDs are ordered, and the public README and browser metadata are generated or cross-checked from one canonical JSON file.

P010 is a **resolved numbered research entry**, with a mathematically complete manuscript [submitted to *Integers*](../manuscripts/P010/README.md). Submission is not acceptance, and the source-priority check is a separate obligation. P020 and P027 have substantial theorem notes while their larger proposed problems remain open *within the repository*.

The portfolio includes several **different** levels of evidence:
- **Written internal proofs:** P010; P020 cyclic, two-generator and elementary-abelian probabilities; P027 exchange distance, autonomous-coordinate factor, projected cutoff and mixing lower bound; interval-sum factor saturation (unnumbered result). P004's eventual connectivity bound, P017's elementary height bounds and P018's exact counterexample are additional scoped results.
- **Exhaustive finite certification, no general conclusion:** P002, P003, P005, P007, P009, P014–P016, P018–P020, P026, P029, P030, each within the limits documented in the relevant scripts.
- **Preliminary models or minimal observations:** P011–P013, P021–P024. These need stronger mathematical or computational evidence before flagship promotion.

## Portfolio tiers (editorial priorities, not mathematical rankings)

**A — Theorem-building core (6):** P003, P005, P017, P018, P020, P027. Each has a precise open target and either serious finite evidence, a genuine structural obstruction, or an internally proved theorem offering an extension path.

**B — Promising alternatives (8):** P004, P006, P014, P016, P023, P026, P028, P030. Retain as independent directions, but prioritize one *new general theorem* or robust counterexample before investing in publication packaging.

**C — Incubation / dependency-rich (10):** P001, P002, P011, P012, P013, P015, P019, P021, P022, P024. Valid investigative entries, often closely tied to a stronger host problem; some need more exact experiments or sharper target invariants.

**D — Reframe/source gate (5):** P007, P008, P009, P025, P029. These have a known solved subproblem, an insufficiently precise current formulation, a particularly strong historical collision, or a likely subsumption by existing general methods. D is **not** proof they lack value.

**R — Resolved/paper track (1):** P010. Keep its theorem and PDF prominently available, but never count it among open conjectures.

## Entry-by-entry decision matrix

| ID | Portfolio tier | Research object | Strongest evidence in repository | Nearest source or relation | Next decisive gate |
|---|---|---|---|---|---|
| [P001](../problems/number-theory/P001-prime-spectrum.md) | **C** | Prime-sum matching spectrum | Partial matching construction; endpoint completion unresolved | Greenfield–Greenfield prime pairings; P003 | Find a sharp completion obstruction; compare spectrum with factor packing |
| [P002](../problems/graph-theory/P002-prime-matching-reconfiguration.md) | **C** | Prime-sum perfect-matching switch graph | One finite connected component at n≤12 | General four-cycle matching switch theory; P005/P029 | Seek a prime-specific 4-cycle switch invariant or prove connectedness |
| [P003](../problems/graph-theory/P003-prime-matching-packing.md) | **A** | Packing disjoint prime-sum matchings | Min-cut equivalence; exact finite max-flow tests | Prime-sum graph and standard bipartite factor theorems | Identify which prime-sum vertex subsets force the extremal cut |
| [P004](../problems/number-theory/P004-sidon-exchange-connectivity.md) | **B** | Sidon exchange connectivity | Elementary eventual connectivity bound for N>2(2k−1)^3 | Golomb-ruler reconfiguration; P013/P016 | Tighten N(k); characterize disconnected finite regime |
| [P005](../problems/graph-theory/P005-coprime-permutation-switches.md) | **A** | Coprime permutation four-cycle switches | Extensive exact connectivity tests; generic universal-row proof fails | General switch chains and coprime permutation enumeration | Find arithmetic augmenting/switch lemma not implied by arbitrary graph |
| [P006](../problems/number-theory/P006-prime-avoiding-sidon-sets.md) | **B** | Prime-difference-free Sidon extremal sets | Bounds 1/√2≤liminf≤limsup≤1 | Sidon extremal bounds; prime-difference restrictions | Improve leading constant beyond dilation |
| [P007](../problems/graph-theory/P007-coprime-difference-spectrum.md) | **D** | Coprime path gap spectrum | Prime-graceful existence iff n≤5 is published | Panma–Rochanakul (2021) prime-graceful paths | Isolate genuinely unproved extremal *partial* gap spectrum |
| [P008](../problems/probability/P008-coprime-percolation-critical-window.md) | **D** | Coprime edge-percolation centering | Internal random-threshold argument needs specification/audit | Hladký–Viswanathan graphon connectivity; arithmetic deterministic host | State one exact limit theorem, hypotheses, centering and exceptional subsequences |
| [P009](../problems/number-theory/P009-two-prime-palette-pairings.md) | **D** | Two-prime-sum pairings | One-color criterion; million-case two-color certificates | Maillet prime-difference conjecture; reflection pairing | Separate necessary condition from one sufficient prime-gap certificate |
| [P010](../problems/graph-theory/P010-minimum-coprime-adjacencies.md) | **R** | Minimum coprime adjacencies | Exact constructive proof and asymptotic; manuscript submitted to Integers | 1983 Erdős–Freud–Hegyvári adjacent extremal arithmetic | Publication follow-through and independent source-priority audit; not open |
| [P011](../problems/probability/P011-random-sum-diagonal-matchings.md) | **C** | Random sum-diagonal factors | Nonmonotonicity example; threshold unknown | Random sum-graphs and arithmetic matchings; P003 | Specify phase observable not implied by edge monotonicity |
| [P012](../problems/probability/P012-coprime-matching-space-percolation.md) | **C** | Percolated coprime matching-switch space | Reconfiguration event is nonmonotone | Switch-chain literature; P005 and P008 | Define meaningful conditioned phase statistic and barrier |
| [P013](../problems/probability/P013-random-sidon-reconfiguration.md) | **C** | Sidon exchanges under random site deletion | Basic small-size degeneracy; no theorem | Random Sidon sets; P004 and P016 | Find nontrivial k scaling with provable component statistic |
| [P014](../problems/topology/P014-random-cayley-sum-flag-homology.md) | **B** | Cayley-sum flag-complex homology | Triangle and four-clique moment comparison | Random flag complexes; Cayley sum correlations; P021 | Prove a non-ER homology window beyond motif moments |
| [P015](../problems/geometry/P015-odd-area-lattice-triangulations.md) | **C** | Odd-area colored triangulation flips | Parity equivalence; small flip graphs | Debrohim–Sasaki–Nunes 2026 cyclically colored flips | Prove arbitrary mod-2 color-pattern case not covered by cyclic-color results |
| [P016](../problems/topology/P016-sidon-complex-homology.md) | **B** | Sidon complex homology | Nonface classification; finite Betti migrations | Independence complexes; additive-combinatorial topology | Prove asymptotic Betti growth or persistent-homology window |
| [P017](../problems/probability/P017-random-divisibility-chain-height.md) | **A** | Height of randomly thinned divisibility posets | p≤liminf≤limsup≤1 in probability; DP verified | Random posets and divisibility-chain theory; P028 | Prove normalized limiting constant or exhibit failure |
| [P018](../problems/matroid-theory/P018-conserved-xor-basis-fibers.md) | **A** | Conserved-XOR matroid basis fibers | d=4 exhaustive positive; d=5 explicit disconnected fiber | Hörsch et al. 2024 group-labeled matroid bases | Prove dimension-dependent minimal exchange size / obstruction theorem |
| [P019](../problems/geometry/P019-no-three-line-exchange.md) | **C** | Optimal no-three-in-line exchanges | Single-point rigidity and rectangle switches | No-three-in-line optima; constrained reconfiguration | Give non-computational infinite lower bound for coordinated exchange |
| [P020](../problems/number-theory/P020-random-hankel-padic-cokernels.md) | **A** | Random p-adic Hankel cokernel groups | Exact cyclic, rank-two, all-k elementary abelian laws | Yiasemides 2024 Hankel kernels; classical finite rank counts | Resolve 3-generator higher-exponent law or full limit; adversarial proof audit |
| [P021](../problems/probability/P021-cayley-sum-sandpile-laws.md) | **C** | Cayley-sum graph sandpile groups | Precisely defined group model; no asymptotic law | Random graph sandpile universality; P014 motif correlations | Compute small Smith normal forms and find forced torsion obstruction |
| [P022](../problems/geometry/P022-random-unimodular-triangle-complex.md) | **C** | Random unimodular triangle complex | N=1 tetrahedral boundary example | Random lattice complexes and TDA | Produce reproducible Betti phase plot before proposing a threshold |
| [P023](../problems/probability/P023-random-prime-incidence-rank.md) | **B** | Random prime incidence rank over F2 | Parity-character obstruction and exact zero-row probabilities | Random arithmetic incidence matrices and sparse GF(2) ranks | Decide whether small-prime zero rows govern the full rank threshold |
| [P024](../problems/graph-theory/P024-zero-forcing-divisor-graph.md) | **C** | Zero forcing on divisor-comparability graphs | Large-prime twin-leaf lower bound | Zero forcing and divisibility graph theory | Compute exact Z(D_N) and prove second-order or matching upper bound |
| [P025](../problems/number-theory/P025-lcm-hamiltonian-bottleneck.md) | **D** | Cyclic minimum adjacent lcm bottleneck | Linear-path main asymptotic established in 1983 | Erdős–Freud–Hegyvári Theorem 1; OEIS A064764 | Check whether closing the tour changes constant; discard if easy corollary |
| [P026](../problems/graph-theory/P026-prime-sum-square-cycle-generation.md) | **B** | Four-cycle homology of prime-sum graphs | GF(2) square rank exact for n≤60 | Bipartite graph toric-ideal quadratic generators; P003 | Find proof of universal generation or first nonzero H1 example |
| [P027](../problems/number-theory/P027-primitive-set-exchange-mixing.md) | **A** | Mixing of maximum primitive-set exchanges | Diameter, free-bit factor, spectral reduction, projected cutoff, lower bound | Liu–Pach–Palincza 2021; Propp–Wilson and heat-bath walks | Bound core mixing/gap; verify originality of linear 2-adic divisibility |
| [P028](../problems/number-theory/P028-random-divisor-complex-mobius-deformation.md) | **B** | Random divisor-complex Euler characteristic | Exact weighted chain/Möbius Dirichlet identity | Philip Hall’s theorem, Dirichlet inversion and ordered factorizations | Prove nontrivial p-dependent asymptotic or fluctuation law |
| [P029](../problems/graph-theory/P029-prime-sum-permutation-xray-fibers.md) | **D** | Prime-supported permutation X-ray fibers | Two-swap obstruction, finite 4-coordinate fiber | Del Lungo 2002 and Bebeacua et al. 2005 tomography | Check known Markov bases before claiming bounded exchange question |
| [P030](../problems/number-theory/P030-double-prime-perfect-matchings.md) | **B** | Simultaneously prime sums and differences | Perfect matching for even N=8..400; parity obstruction | OEIS A227050; prime sum/difference Hamiltonian cycles | Use Hall cuts or arithmetic prime patterns; distinguish Hamiltonian cycles |

## Research programs rather than accidental duplication

### Program I — Prime-sum graph and matching geometry

**P001, P002, P003, P026, P029** use essentially the same arithmetic bipartite graph with left/right copies of [n] and an edge when the sum is prime. They ask genuinely different things: prime-color spectrum, switch connectivity, edge-disjoint perfect matching factors, four-cycle generation of binary homology, and constrained sum-histogram *fibers*. A single host-graph spectral or expansion lemma could transfer across several IDs. Their distinct statements should be retained; source checks for classical matching switches and toric ideals should be shared.

**P011** randomly retains sum diagonals and therefore correlates edges within the same host; it is not an ordinary independent-edge percolation question. **P030** instead uses one undirected copy of [N] and demands *both* sum and difference primality: it is **not equivalent to** P003 or P029. OEIS A227050 studies the stronger Hamiltonian circular arrangement; a positive Hamiltonian instance implies a matching, but a failed Hamiltonian instance need not lack a matching.

### Program II — Coprimality and exchange

**P005, P008, P010, P012** share gcd-defined host edges but ask, respectively, deterministic permutation switching, random-edge connectivity/centering, an **already resolved** permutation extremum, and percolated matching-space reconfiguration. Their status should not be pooled. **P024** is a different divisor comparability graph; **P027** studies maximum antichains in the divisibility poset, not coprime permutations.

### Program III — Sidon restrictions and topology

**P004, P006, P013, P016** share additive Sidon constraints, but their observables are deterministic state connectivity, an extremal density with forbidden prime differences, random feasible-state components, and simplicial homology. They are not four formulations of the same conjecture. P016's minimal-nonface results and P004's coarse connectivity theorem are the strongest rigorous starting points. Any future new question should explicitly contrast with these four.

### Program IV — Divisibility structures

**P017, P024, P027, P028** are linked by divisibility. P017 asks for the height of a random induced divisibility poset; P028 asks for the reduced Euler characteristic of its order complex after *excluding 1*; P024 asks for zero forcing in the deterministic comparability graph; P027 studies **maximum** antichains and their heat-bath reconfiguration. The different quantifiers (random size, maximum size, homological expectation, graph forcing) are essential. P028's baseline zeta expression is simply a weighted Möbius/ordered-factorization identity; its **asymptotic fluctuations**, not the existence of a Dirichlet inverse, are the research target.

### Program V — Random correlated arithmetic topology and algebra

**P014 and P021** start with correlated Cayley-sum graphs but study different higher-order invariants: flag-complex homology and sandpile groups. **P020** involves random *Hankel matrices* rather than these graph Laplacians, and published Hankel kernel classifications are a core input. **P022** is a site-thinned lattice triangle complex, genuinely different from the sum-graph models. **P023** is a random binary incidence rank problem, closer in technique to P018's finite-field linear algebra than to graph percolation.

## Publication and proof-maturity register

- **P010:** a complete submitted short paper. Keep the author's exact [PDF](../manuscripts/P010/coprime_adjacencies.pdf), source-priority distinctions and submission status; no suggestion that acceptance occurred.
- **P020:** internal results cover specified families of finite p-groups, not the full higher-exponent, at-least-three-generator law. The corank enumeration and finite-field kernel structure are **published inputs**, not new theorems. A specialist should audit the conditional mod-p lifting and higher-order boundary before manuscript-level claims.
- **P027:** exact arithmetic free-coordinate factor, diameter and full-chain *lower* mixing bound are internally proved. The projected hypercube has cutoff; **the whole heat-bath chain does not yet have an upper bound or proved cutoff**. The factorization gives a 2-adic divisibility statement for the primitive-set counting sequence, but its historical novelty is unchecked.
- **P018:** the d=5 counterexample to two-exchange connectivity is a finite structural result, while complete characterization of the minimal exchange radius in all dimensions remains open within the project.
- **P026/P030:** finite positive instances are valuable falsification evidence only; they cannot support an eventual/infinite statement.
- **P007/P025:** the exact predecessor theorems must accompany the residual formulation. P025's **linear-path** minimum adjacent-lcm asymptotic is due to Erdős–Freud–Hegyvári (1983), not a conjectural new result.

## Nearest source-level boundaries and additional reading

The following primary records were rechecked in the course of this consolidation or in its immediate predecessor reviews. Their **specific theorems** matter more than titles:

1. [Liu–Pach–Palincza, *The number of maximum primitive sets of integers* (2021)](https://doi.org/10.1017/S0963548321000018) gives the maximum primitive-set counting framework and exponential limit, **not a verified mixing-time theorem for the specific P027 chain**.
2. [Yiasemides (2024), *The variance and correlations of the divisor function in F_q[T], and Hankel matrices*](https://doi.org/10.1007/s40687-023-00418-7) explicitly treats finite-field Hankel rank/kernel structure. P020 cannot claim this finite-field structure as original; its remaining target is the p-adic finite-group law.
3. [Hörsch–Imolay–Mizutani–Oki–Schwarcz, *Problems on Group-labeled Matroid Bases*](https://arxiv.org/abs/2402.16259) already studies group-label-constrained bases. P018 must isolate its special equal-XOR *reconfiguration graph* rather than claim the concept of group-labeled bases.
4. [Croot–Jin, *Prime Sum Graphs and the Induced Trees They Contain*](https://doi.org/10.1007/s00373-025-02999-2) provides modern substantive prime-sum graph theory. It does not, on its stated main result, settle edge-disjoint prime-sum matchings or square-generated binary cycle spaces.
5. [Debrohim–Sasaki–Nunes, *Cyclically Colored Triangulations*](https://arxiv.org/abs/2608.26006) proves diagonal-flip connectivity for cyclic coloring patterns with at least four colors. P015 must target **arbitrary** prescribed parity-class sequences and check whether they reduce to that theorem.
6. [Hladký–Viswanathan, *Connectivity of Inhomogeneous Random Graphs II* (2026)](https://doi.org/10.1002/rsa.70098) proves graphon-generated inhomogeneous random-graph connectivity criteria; P008 concerns a deterministic arithmetic host thinned independently. Neither direct equivalence nor non-overlap follows from the title.
7. [Del Lungo, *Reconstructing permutation matrices from diagonal sums* (2002)](https://doi.org/10.1016/S0304-3975(02)00015-4) establishes the classical anti-diagonal X-ray problem, so P029 must audit bounded-support Markov bases before a novelty claim.
8. [OEIS A227050](https://oeis.org/A227050) records circular arrangements with simultaneous adjacent prime sums and differences: a stronger finite object than P030 pairings. The sequence has zero entries even at some moderately large values, so avoid deducing pairing nonexistence from a failed Hamiltonian arrangement.
9. [Bolognini–Macchia–Ventura–Welker, *The Poset of Proper Divisibility* (2017)](https://doi.org/10.1137/15M1049142) investigates a distinct *proper-divisibility* poset over monomial degrees. It is a conceptual predecessor of P028, but not an exact match to the independently thinned integer divisibility poset.
10. [Erdős–Freud–Hegyvári (1983), *Arithmetical properties of permutations of integers*](https://users.renyi.hu/~p_erdos/1983-02.pdf) establishes the older linear-path lcm asymptotic that forces P025 to be cyclic-only.

**Scope boundary:** this is a repository-wide synthesis of existing literature reports plus targeted source-level confirmation of consequential overlaps; it is **not** 30 independent exhaustive MathSciNet/zbMATH searches or an external referee report. The historical literature may still subsume candidate questions. If a conflict is discovered, update the canonical status and dossier with a precise source-based correction.

## Recommended research sequence

1. **P027:** find a uniform contraction, comparison or entropy inequality for the *interacting core*. If a matching O(n log n) upper bound emerges, compare publication potential against primitive-set counting and lattice Glauber dynamics. Do not package the projected cutoff as a full cutoff.
2. **P020:** attack the first genuinely open higher-exponent, three-generator cokernel case; use mod-p^3 enumeration and the existing kernel-span theorem as the adversarial baseline.
3. **P018:** classify minimal exchange radius as dimension grows and identify a general obstruction/coordination theorem; this could be a publishable finite matroid-reconfiguration result.
4. **P003/P026:** search for a shared arithmetic four-cycle/cut-expansion structure that can both decompose cycles and improve factor packing; rank via exact finite checks before proposing a universal theorem.
5. **P017/P028:** coordinate random-divisibility methods, but keep height and Euler fluctuations separate. In P028, pursue cancellation/variance rather than restating the classical Dirichlet-inverse identity.

**Catalogue policy:** No renumbering or deleting established problem IDs, no artificial freeze on community additions, and no adding new problems merely to reach a count. Promote only statements with exact quantifiers, a robust adversarial attempt, and close-source distinctions.