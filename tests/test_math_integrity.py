r"""Guard against malformed TeX in mathematics-bearing GitHub Markdown.

This supplements tests/test_math_markdown.py, which checks Markdown delimiters.
It specifically prevents P010 regressions that the original tests missed:
- '#' treated as a TeX macro-parameter character;
- unmatched \boxed{...} and \left/\right pairs;
- corrupted LaTeX cases row separators, e.g. '\$$2mm]'.
Standard-library only, run by unittest discovery in CI.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
P010_FILES = [
    "problems/graph-theory/P010-minimum-coprime-adjacencies.md",
    "theorems/P010-exact-coprime-adjacencies.md",
    "audits/2026-10-28-P010-resolution-proof-and-novelty.md",
    "audits/2026-10-29-P010-publishability-priority-review.md",
]
MATH_BLOCK_RE = re.compile(r"(?ms)^\$\$[ \t]*\n(.*?)\n\$\$[ \t]*$")


def tex_groups_balanced(expression):
    r"""Validate literal { } nesting, excluding escaped \{ and \} characters."""
    depth = 0
    pos = 0
    while pos < len(expression):
        c = expression[pos]
        if c == "\\":
            pos += 2  # TeX escape or beginning of a named command.
            continue
        if c == "{":
            depth += 1
        if c == "}":
            depth -= 1
            if depth < 0:
                return False
        pos += 1
    return depth == 0


class P010MathIntegrityTests(unittest.TestCase):
    def test_p010_latex_is_well_formed(self):
        for name in P010_FILES:
            with self.subTest(file=name):
                data = (ROOT / name).read_text(encoding="utf-8")
                math = MATH_BLOCK_RE.findall(data)
                self.assertGreater(len(math), 0)
                self.assertEqual(
                    len(re.findall(r"(?m)^\$\$[ \t]*$", data)),
                    2 * len(math), "Unpaired display-math delimiters")
                for formula in math:
                    self.assertNotIn("#", formula, "TeX macro parameter # inside math")
                    self.assertNotIn(r"\$$", formula, "Corrupted Markdown-to-TeX conversion")
                    self.assertTrue(tex_groups_balanced(formula),
                                    "Unbalanced LaTeX grouping braces")
                    self.assertEqual(formula.count(r"\left"), formula.count(r"\right"),
                                     "Mismatched scalable delimiters")
                    self.assertEqual(formula.count(r"\begin{cases}"),
                                     formula.count(r"\end{cases}"))

    def test_exact_p010_statement_and_count(self):
        dossier = (ROOT / P010_FILES[0]).read_text(encoding="utf-8")
        theorem = (ROOT / P010_FILES[1]).read_text(encoding="utf-8")
        self.assertIn(r"\mathbf{1}_{\gcd(a_i,a_{i+1})=1}", dossier)
        self.assertIn(r"\mathbf{1}_{\gcd(a_i,a_{i+1})=1}", theorem)
        self.assertIn(r"\boxed{h(n)=A_n+", dossier)
        self.assertIn(r"\boxed{h(n)=A_n+", theorem)

    def test_cases_separator_not_corrupted(self):
        audit = (ROOT / P010_FILES[2]).read_text(encoding="utf-8")
        self.assertIn(r"\begin{cases}", audit)
        self.assertIn(r"\end{cases}", audit)
        self.assertIn("n-1,&n=1,2,3,\\\\", audit)
        self.assertNotIn(r"\$$2mm]", audit)


if __name__ == "__main__":
    unittest.main()
