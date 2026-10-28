#!/usr/bin/env python3
"""Generate README catalogue and static browser data from data/problems.json.

Standard library only.
Usage:
    python scripts/generate_catalog.py
    python scripts/generate_catalog.py --check
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "problems.json"
README = ROOT / "README.md"
BROWSER_DATA = ROOT / "docs" / "problems.json"
START = "<!-- CATALOG:START -->"
END = "<!-- CATALOG:END -->"


def generate():
    obj = json.loads(DATA.read_text(encoding="utf-8"))
    records = obj["problems"]
    lines = [
        "| ID | Question | Area | Formulation | Novelty |",
        "|---|---|---|---|---|",
    ]
    for r in records:
        lines.append(
            f"| [{r['id']}]({r['file']}) | {r['title']} | "
            f"{r['area']} | {r['status']} | {r['novelty']} |"
        )
    old = README.read_text(encoding="utf-8")
    if old.count(START) != 1 or old.count(END) != 1:
        raise ValueError("README must contain exactly one catalogue marker pair")
    a = old.index(START) + len(START)
    b = old.index(END)
    if a >= b:
        raise ValueError("Catalogue markers are reversed")
    readme = old[:a] + "\n" + "\n".join(lines) + "\n" + old[b:]
    browser = json.dumps(obj, ensure_ascii=False, indent=2) + "\n"
    return readme, browser


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="Exit nonzero if generated content is stale")
    args = parser.parse_args()
    readme, browser = generate()
    if args.check:
        stale = []
        for p, expected in [(README, readme), (BROWSER_DATA, browser)]:
            if p.read_text(encoding="utf-8") != expected:
                stale.append(str(p.relative_to(ROOT)))
        if stale:
            parser.exit(1, "Outdated generated file(s): " + ", ".join(stale) + "\n")
        print("Generated catalogue and browser data are up to date.")
    else:
        README.write_text(readme, encoding="utf-8")
        BROWSER_DATA.write_text(browser, encoding="utf-8")
        print("Regenerated README catalogue and docs/problems.json.")
