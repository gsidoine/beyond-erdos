"""Check GitHub-readable mathematical Markdown, relative links and P010 PDF.

Runs with Python stdlib. Source checks complement (do not replace) manual GitHub
rendering review; fenced code and inline code are not checked for LaTeX tokens.
"""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
FENCE = re.compile(r"^ {0,3}(" + chr(96) + r"{3,}|~{3,})")
INLINE_CODE = re.compile("(" + chr(96) + r"+)(?:(?!\1).)*?\1")
LEGACY_INLINE = re.compile(r"(?<!\\)\\[()]")
FORBIDDEN_MACRO = re.compile(r"(?<!\\)\\operatorname\b")
BROKEN_LEFT_RIGHT = re.compile(r"(?<!\\)\\(?:left\{|right\})")
ESCAPED_BACKTICK = re.compile(r"(?<!\\)\\" + chr(96))
HTML_SPACE = re.compile(r"&#(?:x20|32);|&nbsp;", re.I)
DANGEROUS_HASH = re.compile(r"(?<!\\)#\{")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+[^)]*)?\)")
INLINE_DOLLAR = re.compile(r"(?<!\\)\$")


def visible_lines(path):
    """Yield (index, text outside code, all lines)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    fence_char, fence_length = None, 0
    for index, line in enumerate(lines):
        match = FENCE.match(line)
        if match:
            seq = match.group(1)
            if fence_char is None:
                fence_char, fence_length = seq[0], len(seq)
            elif seq[0] == fence_char and len(seq) >= fence_length:
                fence_char, fence_length = None, 0
            yield index, "", lines
            continue
        if fence_char is not None:
            yield index, "", lines
        else:
            yield index, INLINE_CODE.sub("", line), lines


class MathMarkdownTests(unittest.TestCase):
    def test_github_math_syntax(self):
        paths = sorted(ROOT.rglob("*.md"))
        self.assertGreaterEqual(len(paths), 50)
        for path in paths:
            if ".git" in path.parts:
                continue
            with self.subTest(file=str(path.relative_to(ROOT))):
                opened = False
                for i, line, lines in visible_lines(path):
                    if not line:
                        continue
                    trimmed = line.strip()
                    if trimmed == "$$":
                        if not opened:
                            self.assertTrue(i == 0 or not lines[i-1].strip(),
                                            f"Missing blank before $$ at {path}:{i+1}")
                        else:
                            self.assertTrue(i == len(lines)-1 or not lines[i+1].strip(),
                                            f"Missing blank after $$ at {path}:{i+1}")
                        opened = not opened
                        continue
                    self.assertFalse(LEGACY_INLINE.search(line),
                                     f"Legacy inline LaTeX delimiter: {path}:{i+1}")
                    self.assertFalse(trimmed in (r"\[", r"\]"),
                                     f"Legacy display delimiter: {path}:{i+1}")
                    self.assertFalse(FORBIDDEN_MACRO.search(line),
                                     f"Unsupported operatorname: {path}:{i+1}")
                    self.assertFalse(BROKEN_LEFT_RIGHT.search(line),
                                     f"Malformed left/right delimiter: {path}:{i+1}")
                    self.assertFalse(ESCAPED_BACKTICK.search(line),
                                     f"Escaped code tick: {path}:{i+1}")
                    self.assertFalse(HTML_SPACE.search(line),
                                     f"HTML space entity: {path}:{i+1}")
                    if not opened:
                        count = len(INLINE_DOLLAR.findall(line))
                        self.assertEqual(count % 2, 0,
                                         f"Unmatched inline $: {path}:{i+1}")
                        for m in re.finditer(r"\$([^$]*)\$", line):
                            self.assertFalse(DANGEROUS_HASH.search(m.group(1)),
                                             f"Raw hash in math at {path}:{i+1}")
                self.assertFalse(opened, f"Unclosed display $$ block: {path}")

    def test_local_markdown_links_resolve(self):
        for path in sorted(ROOT.rglob("*.md")):
            if ".git" in path.parts:
                continue
            with self.subTest(file=str(path.relative_to(ROOT))):
                display = False
                for i, line, _ in visible_lines(path):
                    if line.strip() == "$$":
                        display = not display
                        continue
                    if display:
                        continue
                    no_math = re.sub(r"(?<!\\)\$[^$]*\$", "", line)
                    for match in MARKDOWN_LINK.finditer(no_math):
                        target = match.group(1)
                        if target.startswith(("https://", "http://", "mailto:",
                                              "#", "data:", "/")):
                            continue
                        relative = unquote(target.split("#")[0].split("?")[0])
                        if not relative:
                            continue
                        resolved = (path.parent / relative).resolve()
                        self.assertTrue(
                            resolved.is_relative_to(ROOT.resolve()) and resolved.exists(),
                            f"Broken local Markdown link: {path}:{i+1}: {target}")

    def test_p008_equation_source(self):
        path = ROOT / "problems/probability/P008-coprime-percolation-critical-window.md"
        source = path.read_text(encoding="utf-8")
        self.assertIn(r"$\gamma$", source)
        self.assertIn(r"\mu_n(p)=\sum_{v=1}^n(1-p)^{d_n(v)}.", source)
        self.assertIn("$$\n\\mu_n(p)", source)

    def test_p010_manuscript_link_and_formula(self):
        path = ROOT / "manuscripts/P010/README.md"
        source = path.read_text(encoding="utf-8")
        pdf = path.parent / "coprime_adjacencies.pdf"
        self.assertTrue(pdf.is_file(), "Submitted P010 manuscript missing")
        self.assertIn("(coprime_adjacencies.pdf)", source)
        self.assertIn(r"\max", source)
        self.assertIn(r"\pi(n)-\pi(n/2)", source)
        self.assertIn("Submitted", source)
        self.assertIn("Integers", source)
        expected = "3aae034589f58b9593891a53ee5d54ea20f1106c774364e1ff564df417837737"
        self.assertEqual(hashlib.sha256(pdf.read_bytes()).hexdigest(), expected)


if __name__ == "__main__":
    unittest.main()
