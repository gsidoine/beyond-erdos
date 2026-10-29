# P013 — Reconfiguration of Sidon sets in a random ambient set

<!-- DOSSIER-SUMMARY -->
> **Research question:** When allowed integer sites are selected at random, what is the phase diagram for existence and valid one-element-exchange connectivity of size-k Sidon subsets?  
> **Formulation:** candidate. **Novelty:** apparent novelty — targeted search, exact observable unverified.  
> **Verified/known progress:** Sidon constraints and random Sidon-set phase transitions are established; valid-state exchange connectivity is a distinct proposed observable, not yet certified open.  
> **Finite evidence:** The graph of size-two subsets is trivially connected whenever at least one state exists; genuine reconfiguration questions begin at larger sizes.  
> **Navigation:** [Full catalogue](../../README.md#problem-catalogue) · [Latest novelty audit](../../literature-audits/2026-10-29-novelty-and-new-directions.md)
<!-- /DOSSIER-SUMMARY -->

**Fields:** additive combinatorics, random discrete structures, reconfiguration  
**Proposed:** 2026-10-29  
**Research status:** candidate, unproved, not certified novel.

## Model

Choose a binomial random subset \(W_N(q)\subseteq[N]\), retaining each integer independently with probability \(q\).

Let \(\mathsf{Sid}_{N,k}(W)\) be the family of **k-element Sidon sets** \(A\subseteq W\), where Sidon means that every positive difference between two elements of \(A\) occurs at most once (equivalently, unordered pair sums are distinct).

Define an exchange graph \(\mathcal E_{N,k}(W)\) with this family as vertices. Join two states \(A,B\) precisely when \(|A\setminus B|=|B\setminus A|=1\).

## Main question

For scaling regimes \(k=k(N)\), particularly \(k\) approaching a nonzero fraction of \(\sqrt N\), study the random variables
\[
X_{N,k}(q)=|\mathsf{Sid}_{N,k}(W_N(q))|,\qquad
C_{N,k}(q)=\#\text{components of }\mathcal E_{N,k}(W_N(q)).
\]

**Can the appearance of Sidon states and the emergence of a single feasible exchange component occur at parametrically different scales of \(q\)?** Determine meaningful scaling limits and/or transition regimes when the expected number of states becomes large.

To avoid trivial conventions, condition on \(X_{N,k}(q)\ge2\) when discussing connectivity. Neither this conditional event nor the connectedness of the state graph is assumed monotone in \(q\).

## Structural implications

This asks whether a *randomly diluted arithmetic constraint space* can exhibit a fragmented phase, analogous to clustering in random constraint satisfaction and the solution geometry of hard-core models. The \(q=1\) endpoint is the deterministic Sidon exchange problem P004. The random-site model may reveal an intrinsic **reconfiguration threshold** distinct from ordinary Sidon-set existence.

## Adversarial notes

When \(k=2\), every two-element set is Sidon, and the exchange graph is a Johnson graph on the selected sites, hence connected whenever it is nonempty. This is a degenerate case, not evidence for higher-\(k\) behavior.

A Sidon set cannot be arbitrarily close to \(\sqrt N\) without strong global constraints; at high \(k\), frozen isolated states or no states can dominate the ensemble. The problem should be studied with clear conditioning and fixed \(k(N)\) regimes.

## Literature context

- Luque, Torre and Lacasa, [*Phase transitions in number theory: from the birthday problem to Sidon sets* (2013)](https://doi.org/10.1103/PhysRevE.88.052119), studies a random Sidon **decision** problem and statistical-physics phase behavior, **not** this graph of feasible exchanges.
- Dotú–Van Hentenryck, [*A Memetic Approach to Golomb Rulers* (2005)](https://cs.brown.edu/research/pubs/pdfs/2005/Dotu-2005-SHE.pdf), uses local mark changes in optimization but permits intermediate constraint violations.
- [P004](../number-theory/P004-sidon-exchange-connectivity.md) addresses the full ambient set \(W=[N]\), not random availability.

The random Sidon model and the swap operation have separately appeared in the literature. A direct analysis of this **random feasible-state exchange graph** was not found in the targeted search. Broader random-constraint reconfiguration work may imply results, so no originality certificate is claimed.

## Initial falsification programme

1. Enumerate small random \(W\) and exact size-\(k\) Sidon states; compute component count.
2. Identify arithmetic cut/frozen-state invariants that survive random dilution.
3. Compare with random independent-set reconfiguration on the hypergraph of repeated-difference constraints.
4. Check known random hypergraph independent-set clustering/reconfiguration theory before making universal claims.
