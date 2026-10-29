# Repository Markdown rendering audit — 29 October 2026

**Scope:** all 56 Markdown files discovered in the main branch at the start of the review, including the P001–P025 dossiers, theorem statements, audit notes, research notes, README, and the P010 manuscript page.

**Method:** source-level review using the connected GitHub repository. Searched for legacy LaTeX delimiters, unsupported operator macros, malformed brace commands, literal HTML-space entities, escaped code backticks, unpaired display blocks, and invalid relative repository links. Repairs are deliberately limited to presentation and documentation consistency. This is not a pixel-perfect browser screenshot verification.

## Corrected issues

- **P010 submitted manuscript README:** GitHub had a valid PDF but the Markdown still claimed it was missing. The README now links to the actual file [coprime_adjacencies.pdf](../manuscripts/P010/coprime_adjacencies.pdf), uses a brace-safe max formula without left/right, and changes the reported unsupported operatorname command into a mathrm typeset label. Escaped source backticks are fixed.
- **P010 integrity:** the repository blob is SHA-1 1555806c0929164edbcf0a558513b5c23d6ab76e and byte count 214297, matching git hash-object on the exact submitted local file. Its independent SHA-256 is 3aae034589f58b9593891a53ee5d54ea20f1106c774364e1ff564df417837737.
- **Legacy math delimiters:** affected P020 and P016 dossiers, P020 theorem proof, flagship audit and README. Converted inline expressions to GitHub dollar notation and display equations to blank-line-separated double-dollar blocks.
- **Operator math commands:** simple names pc, span, coker, corank, diam, rank and lcm now use mathrm rather than unsupported operatorname. The P013 raw hash counting macro is replaced by readable mathematical text.
- **Contributing guidance:** now acknowledges the P001–P025 freeze and uses single backslashes in actual LaTeX example code.
- **Automated lint:** tests/test_math_markdown.py now checks all repository Markdown, excluding code examples. It tests math delimiters and display-block whitespace, high-risk macros, literal markup artifacts, relative local links, and the P010 PDF's SHA-256.

## Interpretation and remaining risks

The exact submitted P010 PDF was not changed. The static checks cannot guarantee uniform appearance in every client renderer; a manual glance at the GitHub preview remains useful after merging. Existing deliberate mathematical LaTeX such as cases environments and array row-spacing commands was preserved. The PR does not claim to verify mathematical correctness, originality or priority.

## CI commands

    python -m unittest discover -s tests -v
    python scripts/generate_catalog.py --check

These run under the existing catalogue workflow. Failures should block new malformed Markdown from being merged.
