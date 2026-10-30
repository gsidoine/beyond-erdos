#!/usr/bin/env python3
"""Exact Fano-plane test of Singer-translate forbidden-edge incidence.

Standard library only. Every pair of vertices belongs to exactly one
Singer translate. Exhaustively test every single-edge graph and a
deterministic collection of multi-edge graphs.
"""
from itertools import combinations
from random import Random


def main():
    v = 7
    base = (0, 1, 3)
    translates = [{(x + t) % v for x in base} for t in range(v)]
    pairs = list(combinations(range(v), 2))
    incidence = {edge: sum(set(edge) <= block for block in translates)
                 for edge in pairs}
    assert len(pairs) == 21
    assert all(n == 1 for n in incidence.values())

    rng = Random(20261030)
    graphs = [set(), set(pairs)]
    graphs.extend([{edge} for edge in pairs])
    for _ in range(250):
        graphs.append({edge for edge in pairs if rng.getrandbits(1)})

    for edges in graphs:
        counts = [sum(set(edge) <= block for edge in edges)
                  for block in translates]
        assert sum(counts) == len(edges)
        assert min(counts) <= len(edges) / v
        assert any(len(block) - counts[t] >= 3 - len(edges) / v
                   for t, block in enumerate(translates))
    print("Fano/Singer incidence verified on", len(graphs),
          "graphs and all 21 vertex pairs.")


if __name__ == "__main__":
    main()
