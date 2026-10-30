#!/usr/bin/env python3
"""Generate all catalogue views from data/problems.json (standard library only).

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
CURATION = ROOT / "data" / "curation.json"
BROWSER_CURATION = ROOT / "docs" / "curation.json"
ACORNS_START = "<!-- ACORNS:START -->"
ACORNS_END = "<!-- ACORNS:END -->"
SEEDBED_START = "<!-- SEEDBED:START -->"
SEEDBED_END = "<!-- SEEDBED:END -->"
DOSSIER_START = "<!-- DOSSIER-SUMMARY -->"
DOSSIER_END = "<!-- /DOSSIER-SUMMARY -->"


def dossier_summary(p):
    return "\n".join([
        DOSSIER_START,
        f"> **Research question:** {p['question']}  ",
        f"> **Formulation:** {p['status']}. **Novelty:** {p['novelty']}.  ",
        f"> **Verified/known progress:** {p['result']}.  ",
        f"> **Finite evidence:** {p['verification']}.  ",
        "> **Navigation:** [Full problem catalogue](../../README.md#problem-catalogue) · "
        "[Status and scope](../../README.md#status-and-scope) · [Literature and audits](../../README.md#literature-and-audits)",
        DOSSIER_END,
    ])


def replace_marked(text, start, end, replacement):
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f"Expected exactly one marker pair: {start} / {end}")
    a = text.index(start)
    b = text.index(end) + len(end)
    if a >= b:
        raise ValueError("Marker ordering is invalid")
    return text[:a] + replacement + text[b:]


def generate():
    obj = json.loads(DATA.read_text(encoding="utf-8"))
    records = obj["problems"]
    allocation = json.loads(CURATION.read_text(encoding="utf-8"))
    ids = [r["id"] for r in records]
    buckets = [allocation[k] for k in ("primary", "secondary", "resolved")]
    combined = [id for bucket in buckets for id in bucket]
    if len(combined) != len(set(combined)) or sorted(combined) != sorted(ids):
        raise ValueError("Curated catalogues must partition the canonical IDs exactly once")
    by_id = {r["id"]: r for r in records}
    def curated_table(group):
        return "\n".join(["| ID | Problem | Area |", "|---|---|---|", *(
            f"| [{id}]({by_id[id]['file']}) | {by_id[id]['title']} | {by_id[id]['area']} |"
            for id in allocation[group]
        )])
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
    readme = replace_marked(
        old, START, END,
        START + "\n" + "\n".join(lines) + "\n" + END
    )
    readme = replace_marked(readme, ACORNS_START, ACORNS_END,
        ACORNS_START + "\n" + curated_table("primary") + "\n" + ACORNS_END)
    readme = replace_marked(readme, SEEDBED_START, SEEDBED_END,
        SEEDBED_START + "\n" + curated_table("secondary") + "\n" + SEEDBED_END)
    browser = json.dumps(obj, ensure_ascii=False, indent=2) + "\n"
    curation_view = json.dumps(allocation, ensure_ascii=False, indent=2) + "\n"
    return readme, browser, curation_view


def dossier_views():
    for r in json.loads(DATA.read_text(encoding="utf-8"))["problems"]:
        path = ROOT / r["file"]
        original = path.read_text(encoding="utf-8")
        desired = replace_marked(original, DOSSIER_START, DOSSIER_END,
                                 dossier_summary(r))
        yield path, desired


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="Exit nonzero if generated content is stale")
    args = parser.parse_args()
    readme, browser, curation_view = generate()
    views = [(README, readme), (BROWSER_DATA, browser), (BROWSER_CURATION, curation_view)] + list(dossier_views())
    if args.check:
        stale = [str(p.relative_to(ROOT)) for p, expected in views
                 if p.read_text(encoding="utf-8") != expected]
        if stale:
            parser.exit(1, "Outdated generated file(s): " + ", ".join(stale) + "\n")
        print("Catalogue, browser data and all dossier summaries are current.")
    else:
        for p, expected in views:
            p.write_text(expected, encoding="utf-8")
        print("Regenerated README, browser data and dossier summaries.")
