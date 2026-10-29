"""Ensure all mathematical Markdown uses GitHub-supported MathJax notation.

GitHub renders inline $...$ and display $$...$$, but legacy \\(...\\)
and \\[...\\] are not reliably recognized in repository Markdown.

Math delimiters inside fenced/inline *code* are intentionally ignored.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
LEGACY = re.compile(r"\\[()\[\]]")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
INLINE_CODE = re.compile(r"(`+).*?\1")


class MathMarkdownTests(unittest.TestCase):
    def test_compatible_math_delimiters(self):
        checked = 0
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts:
                continue
            with self.subTest(markdown=str(path.relative_to(ROOT))):
                lines = path.read_text(encoding="utf-8").splitlines()
                fenced = False
                math_block = False
                for i, line in enumerate(lines):
                    if FENCE.match(line):
                        fenced = not fenced
                        continue
                    if fenced:
                        continue
                    stripped = INLINE_CODE.sub("", line)
                    self.assertIsNone(
                        LEGACY.search(stripped),
                        f"Legacy math delimiters at {path}:{i+1}. "
                        "Use $...$ or a standalone $$ block.")
                    if stripped.strip() == "$$":
                        if not math_block:
                            self.assertTrue(
                                i == 0 or not lines[i-1].strip(),
                                f"Missing blank line before $$ at {path}:{i+1}")
                        else:
                            self.assertTrue(
                                i == len(lines)-1 or not lines[i+1].strip(),
                                f"Missing blank line after $$ at {path}:{i+1}")
                        math_block = not math_block
                self.assertFalse(math_block, f"Unclosed $$ block in {path}")
                checked += 1
        self.assertGreaterEqual(checked, 30)

    def test_p008_equation_source(self):
        file = ROOT / "problems/probability/P008-coprime-percolation-critical-window.md"
        source = file.read_text(encoding="utf-8")
        self.assertIn(r"$\\gamma$", source)
        self.assertIn(r"\\mu_n(p)=\\sum_{v=1}^n(1-p)^{d_n(v)}.", source)
        self.assertIn("$$\n\\mu_n(p)", source)


if __name__ == "__main__":
    unittest.main()
