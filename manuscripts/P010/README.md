# P010 — Manuscript submitted to *Integers*

**Title:** *The Minimum Number of Coprime Adjacencies in a Permutation*  
**Author:** G. Sidoine (Independent Researcher, France; ORCID 0009-0005-4525-1182)  
**Journal:** *Integers*  
**Publication status:** **Submitted**. This does not indicate acceptance, peer review completion or publication.

[Read the submitted manuscript (PDF)](coprime_adjacencies.pdf)

## Main theorem

For a permutation $a=(a_1,\ldots,a_n)$ of $[n]$, let $h(n)$ be the minimum number of consecutive coprime pairs across all such permutations. The manuscript proves that, for every $n\ge4$,

$$
h(n)=\pi(n)-\pi(n/2)+
\max\{1,\lceil(\pi(n/2)-\pi(n/3))/2\rceil\}.
$$

In particular, $h(n)\sim 7n/(12\log n)$.

The proof interprets $h(n)$ as the minimum path-cover number of the non-coprime graph minus one. It derives a matching lower bound from isolated vertices and prime leaves and constructs an optimal path cover by grouping vertices according to largest prime factor.

## Mathematical documentation

- [P010 research entry](../../problems/graph-theory/P010-minimum-coprime-adjacencies.md)
- [Constructive proof](../../theorems/P010-exact-coprime-adjacencies.md)
- [Publication and historical-priority review](../../audits/2026-10-29-P010-publishability-priority-review.md)

The manuscript is the submitted version. The repository proof and computation files provide supplementary detail; no journal acceptance or historical originality is claimed.

## File integrity

The original PDF is maintained unchanged at `manuscripts/P010/coprime_adjacencies.pdf`. Its SHA-256 checksum is

```text
3aae034589f58b9593891a53ee5d54ea20f1106c774364e1ff564df417837737

```

A local copy can be verified with `sha256sum manuscripts/P010/coprime_adjacencies.pdf`.