# P010 manuscript snapshot, reference check, and submission-policy gate

**Date:** 29 October 2026  
**Related problem:** [P010 — Minimum coprime adjacencies](../problems/graph-theory/P010-minimum-coprime-adjacencies.md)  
**Author:** G. Sidoine, Independent Researcher, France; ORCID 0009-0005-4525-1182.  
**Manuscript title:** *The Minimum Number of Coprime Adjacencies in a Permutation*.  
**Submitted journal contemplated/reported by the author:** *Integers: The Electronic Journal of Combinatorial Number Theory*. **No submission receipt, editorial decision or journal acceptance was available to verify in this audit.**

## Exact supplied submission snapshot

The author supplied a **two-page PDF** in the project's conversation on 29 October 2026, named \`coprime_adjacencies(1).pdf\`.

- Size: **214,297 bytes**, A4, 2 pages, produced by pdfTeX.
- SHA-256: \`3aae034589f58b9593891a53ee5d54ea20f1106c774364e1ff564df417837737\`.
- Content: abstract, exact formula for $h(n)$, constructive proof using noncoprime-graph path covers, small witnesses $n=4,\ldots,11$, nonmonotonicity remark, eight references, an AI-use declaration, and author affiliation/ORCID.
- The user-supplied **binary PDF itself is not committed in this PR**; this record preserves its identity and audit context without creating an altered or falsely attributed manuscript file. If the author wants the PDF publicly archived, commit the *unaltered source PDF*, checking applicable publication/preprint permissions first. The authoritative author-supplied PDF remains with the original project conversation.

The mathematical theorem agrees with [the canonical proof](../theorems/P010-exact-coprime-adjacencies.md):

$$
h(n)=\pi(n)-\pi(n/2)+
\max\left(1,\left\lceil\frac{\pi(n/2)-\pi(n/3)}2\right\rceil\right)
\quad(n\ge4),
$$

with $h(1)=0,h(2)=1,h(3)=2$ and $h(n)\sim 7n/(12\log n)$. The PDF proof uses prime-factor classes, 2/3-multiple connections, the Rosser–Schoenfeld/Dusart inequality $\pi(2x)\le 2\pi(x)$ for $x\ge3$, and an explicit list of optimal short permutations. This source comparison is **not** an independent refereeing of the full argument.

## Critical journal-policy conflict: official guidance checked 29 October 2026

**[INTEGERS author instructions](https://math.colgate.edu/~integers/submit.html)** explicitly state that manuscripts making use of **artificial intelligence in the production of mathematics, code, bibliography, or other content** will **not be considered**, although basic grammar/spelling assistance is exempt. The accompanying submission email is also required to confirm compliance with this policy.

The author-supplied PDF explicitly discloses that ChatGPT assisted **preliminary mathematical exploration, proof construction, verification code, early drafts, and literature/reference checks**, well beyond the policy's grammar/spelling exception.

**Consequence:** On the stated facts, this manuscript appears **incompatible with the INTEGERS submission policy**, despite its transparent and responsible disclosure. This is a policy/eligibility warning, not a claim of a journal rejection or a mathematical defect. The author should **contact the editorial office and obtain clarification**, and must not remove or weaken the disclosure to evade the rule. If the journal confirms the incompatibility, withdraw or redirect appropriately rather than making a knowingly false compliance statement. Rewriting the prose does **not erase historical AI assistance in the mathematical research**.

No submission, withdrawal or editor contact is performed by this repository change.

## Independent source-level reference checks (manuscript numbering)

| Manuscript citation | Source verification | Relevance and distinction |
|---|---|---|
| [1] Erdős–Freud–Hegyvári (1983) | [Archived article](https://users.renyi.hu/~p_erdos/1983-02.pdf) | Neighboring gcd/lcm *magnitudes* in permutations, not this exact minimum coprime count in accessible evidence |
| [2] Pomerance (2022), *Coprime permutations* | [arXiv record](https://arxiv.org/abs/2203.03085) | Coprime permutations, not path-cover minimum |
| [3] Melotti–Saias (2020), *On path partitions of the divisor graph* | [Official Acta Arithmetica metadata](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/192/4/113319/on-path-partitions-of-the-divisor-graph) | **Directly related path-partition topic, but divisor graph is not the noncoprime graph**; official pages verify pages 329–339 |
| [4] McNew (2021), primitive subsets and divisor graph | [DOI / journal record](https://doi.org/10.1016/j.ejc.2020.103237) | Divisor graph rather than all gcd-positive edges |
| [5] McNew (2023), *Permutations and the divisor graph of [1,n]* | [Official Mathematika publisher page](https://doi.org/10.1112/mtk.12177) | Studies divisor-graph cycle covers / arithmetically constrained permutations, not the same objective |
| [6] OEIS A297616 | [OEIS sequence page](https://oeis.org/A297616) | **Correct match**: connected-component count of the noncoprime graph is $1+\pi(n)-\pi(n/2)+[n\ge4]$ |
| [7] Rosser–Schoenfeld (1975) | [Rosser–Schoenfeld inequality discussion](https://math.colgate.edu/~integers/u103/u103.pdf) | Confirms the classical $\pi(2x)<2\pi(x)$ inequality for $x\ge3$ |
| [8] Dusart (2002) | [Dusart bibliographic and inequality reference](https://erdosproblems.ai/wiki/library/primes/dusart_2002_sur_la_conjecture_pi_x_y_pi_x_y) | Related prime-counting inequalities, including the relevant special case |

**Source-check scope:** bibliography identities, stated abstracts/results, and the graph-distinction logic were reviewed. The **full text** of all eight papers has **not** been exhaustively compared; the exact P010 theorem's **historical originality remains unverified**.

## Publication recommendation

The mathematical content is a defensible **short arithmetic-combinatorics note**, conditional on independent human proof verification and complete priority review. *INTEGERS* is **not an appropriate confirmed outlet under its posted AI policy**. Prefer a journal whose verified editorial policy permits AI-assisted mathematical exploration with transparent disclosure and rigorous human accountability. Any alternative must be evaluated against its current rules rather than assumed acceptable.

This record is **not** a new manuscript, a publication claim, or a source substitution for the user's original PDF.
