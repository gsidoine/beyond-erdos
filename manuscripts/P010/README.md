# P010 — Exact submitted manuscript (Integers)

**Manuscript:** *The Minimum Number of Coprime Adjacencies in a Permutation*  
**Author:** G. Sidoine, Independent Researcher, France; ORCID 0009-0005-4525-1182.  
**Reported submission:** *Integers*, 29 October 2026.  
**Version:** supplied two-page final submission PDF, **not** an earlier pre-submission draft.

**Canonical PDF path intended for this repository:**

\`manuscripts/P010/coprime_adjacencies_integers_submitted_2026-10-29.pdf\`

**Status:** The exact binary is **not yet checked into this GitHub branch**. It is preserved in an external transfer ZIP supplied alongside the PR and should be added through GitHub's **Add file → Upload files** action. The connector currently used for this PR cannot read the uploaded sandbox PDF as binary bytes for a Git blob. Do not interpret this README as confirmation of a file that is not there yet.

**SHA-256 (exact original bytes):**

\`3aae034589f58b9593891a53ee5d54ea20f1106c774364e1ff564df417837737\`

**Number of PDF pages:** 2. The PDF was visually rendered and its complete text inspected.

## Theorem in the submitted version

For each $n\ge4$, the minimum number of gcd-one adjacent pairs across all permutations of $[n]$ equals

$$
h(n)=\pi(n)-\pi(n/2)+
\max\left\{1,\left\lceil\frac{\pi(n/2)-\pi(n/3)}2\right\rceil\right\},
$$

with $h(n)\sim 7n/(12\log n)$.

The manuscript proves $h(n)=\operatorname{pc}(H_n)-1$ for the non-coprime graph $H_n$, gives the lower bound using isolated vertices and prime leaves, and constructs an optimal path cover using classes by largest prime factor. It includes reference entries [1]–[8], a 2020 Mathematics Subject Classification, and an AI-use declaration stating ChatGPT assistance with preliminary exploration, proof construction, verification code, early drafts, mathematical review, grammar and literature checking.

The manuscript has **already been submitted** and must not be silently changed in the repository; future proof, priority, or copyediting amendments should receive their own version labels.

## Related files

- [P010 problem dossier](../../problems/graph-theory/P010-minimum-coprime-adjacencies.md)
- [Independent constructive theorem](../../theorems/P010-exact-coprime-adjacencies.md)
- [P010 publishability and priority audit](../../audits/2026-10-29-P010-publishability-priority-review.md)
- [Current literature status](../../audits/2026-10-29-P001-P025-literature-source-gate.md)

## Post-upload integrity check

Once the exact binary has been uploaded at the path above, verify locally:

\`\`\`sh
sha256sum manuscripts/P010/coprime_adjacencies_integers_submitted_2026-10-29.pdf
\`\`\`

The result must match the SHA-256 above. Only then should the repository claim to host the submitted PDF itself.
