# P010 — Exact submitted manuscript (Integers)

**Manuscript:** *The Minimum Number of Coprime Adjacencies in a Permutation*  
**Author:** G. Sidoine, Independent Researcher, France; ORCID 0009-0005-4525-1182.  
**Reported submission:** *Integers*, 29 October 2026.  
**Version:** supplied two-page final submission PDF, **not** an earlier pre-submission draft.

**Canonical PDF (exact submitted version):**

[Download the submitted PDF](coprime_adjacencies.pdf) (`manuscripts/P010/coprime_adjacencies.pdf`)

**Status:** The original submitted binary **is present on `main`**, and its Git blob SHA-1 (`1555806c0929164edbcf0a558513b5c23d6ab76e`) exactly matches a `git hash-object` of the author's submitted PDF. Its 214,297-byte size also matches. This is a byte-for-byte integrity check, not a claim of mathematical referee acceptance.

**SHA-256 (exact original bytes):**

`3aae034589f58b9593891a53ee5d54ea20f1106c774364e1ff564df417837737`

**Number of PDF pages:** 2. The PDF was visually rendered and its complete text inspected.

## Theorem in the submitted version

For each $n\ge4$, the minimum number of gcd-one adjacent pairs across all permutations of $[n]$ equals

$$
h(n)=\pi(n)-\pi(n/2)+
\max\{1,\lceil(\pi(n/2)-\pi(n/3))/2\rceil\},
$$

with $h(n)\sim 7n/(12\log n)$.

The manuscript proves $h(n)=\mathrm{pc}(H_n)-1$ for the non-coprime graph $H_n$, gives the lower bound using isolated vertices and prime leaves, and constructs an optimal path cover using classes by largest prime factor. It includes reference entries [1]–[8], a 2020 Mathematics Subject Classification, and an AI-use declaration stating ChatGPT assistance with preliminary exploration, proof construction, verification code, early drafts, mathematical review, grammar and literature checking.

The manuscript has **already been submitted** and must not be silently changed in the repository; future proof, priority, or copyediting amendments should receive their own version labels.

## Related files

- [P010 problem dossier](../../problems/graph-theory/P010-minimum-coprime-adjacencies.md)
- [Independent constructive theorem](../../theorems/P010-exact-coprime-adjacencies.md)
- [P010 publishability and priority audit](../../audits/2026-10-29-P010-publishability-priority-review.md)
- [Current literature status](../../audits/2026-10-29-P001-P025-literature-source-gate.md)

## Binary integrity

The repository PDF is the original author-submitted document, not a recreated PDF. To check the Git object against a local copy:

```sh
git hash-object manuscripts/P010/coprime_adjacencies.pdf
sha256sum manuscripts/P010/coprime_adjacencies.pdf

```

The expected Git blob SHA-1 is `1555806c0929164edbcf0a558513b5c23d6ab76e` and the expected file SHA-256 is `3aae034589f58b9593891a53ee5d54ea20f1106c774364e1ff564df417837737`.
