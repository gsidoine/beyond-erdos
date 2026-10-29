# Discovery and priority audit — P015, with P010 publication review

**Date:** 29 October 2026  
**Editorial aim:** propose original, structurally meaningful mathematical problems; prove or refute obvious statements before entry; preserve the distinction between **apparent novelty** and historical certification.

## P015 geometric candidate: odd-area triangulations

**Precise object:** convex lattice polygon with cyclically ordered vertices $v_i\in\mathbb Z^2$. A valid triangulation has every face of **odd doubled area**. Connect two valid triangulations if they differ by a single valid diagonal flip. We ask whether this graph is connected whenever the vertex parities meet all four residues in $\mathbb F_2^2$ and at least two valid states exist.

**Exact arithmetic translation:** an odd-area triangle uses three distinct parity residues; a valid flip occurs if and only if its quadrilateral uses all four residues. The parity condition thus induces an arbitrary **fixed vertex four-coloring**, with every triangle required to have three different colors. Unlike coloring the *triangles* or permitting color-changing flips, vertex colors are **fixed**.

**Falsification performed:**
- For any three-color pattern, no flip can be valid, even when two distinct valid triangulations exist. Example: cyclic pattern $(0,1,0,2,1,2)$ on a hexagon, which has two isolated valid triangulations.
- Exhaustively classified **all four-color cyclic patterns up to relabeling** for polygons of sizes $5,\ldots,9$. There are respectively $5,20,70,231,735$ patterns with at least two valid states; **every** corresponding flip graph is connected. Independent implementation predated the committed reproducibility script.
- Additional finite random four-color patterns at $n=10,11$ showed no counterexample (small samples only).
- The four-color condition is mathematically essential, not an attempt to hide the simpler three-color obstruction. Patterns can all be realized by strictly convex lattice polygons after sufficiently large scaling.

**Direct historical collisions to avoid:**
1. [Baur, Bergerova, Voon, Xu, *Flip graphs of coloured triangulations of convex polygons* (2024–2025)](https://arxiv.org/abs/2402.06546): studies **colored faces and permutation-sensitive colored flips**; not automatically the vertex parity constraint.
2. [Acharya, Mütze, Verciani, *Flips in colorful triangulations*, Journal of Computational Geometry (2025)](https://doi.org/10.20382/jocg.v16i1a9): proves strong connectivity/Hamiltonicity under certain **two-color** rainbow constraints and arbitrary coloring patterns.
3. [Debrohim, Sasaki, Nunes, *Cyclically Colored Triangulations: Enumeration and Connectedness of Reconfiguration Graphs* (August 2026)](https://arxiv.org/abs/2608.26006): proves connected valid flip graphs for **cyclically repeated vertex colorings with at least four colors**. This is **the closest modern source** and may conceal a more general result; the new conjecture's *arbitrary parity sequence* is not obviously a direct consequence of the published cyclic-color statement. This requires detailed full-text proof checking.
4. The general polygon triangulation flip graph is connected (classical), but a constraint-induced subgraph can be disconnected.

**Novelty verdict:** *apparent novelty after a targeted exact-observable search*, not a certified new open problem. We intentionally do **not** assert a proof, an asymptotic theorem, or publication priority. See [P015](../problems/geometry/P015-odd-area-lattice-triangulations.md) and [reproducible exact tests](../experiments/P015_odd_area_flip_graph.py).

## P010 assessment

The [separate full publication and historical priority review](../audits/2026-10-29-P010-publishability-priority-review.md) describes P010 as a credible **short-paper candidate** if its proof survives independent human validation and its exact formula has no earlier publication. Close work by Erdős–Freud–Hegyvári (1983) optimizes adjacent gcd/lcm *magnitudes*, not the minimum **count** of gcd-one transitions; general path-cover theory and recent studies of coprime graph spectra do not immediately settle the specific problem.

**Do not equate lack of a found paper with proof of novelty.** No PR in this research pass changes the P010 theorem or attempts to add a stronger published result.
