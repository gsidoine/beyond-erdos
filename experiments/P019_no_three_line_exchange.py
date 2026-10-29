#!/usr/bin/env python3
"""Exact small-grid no-three-in-line optimum reconfiguration.

For n=3,...,7, the known optimum equals 2n. Enumerates all 2n-point
solutions by choosing two cells per row, enforcing two per column, and
checking every selected triple for collinearity. Computes connectivity
of the at-most-t simultaneous replacement graph.

Standard library only. Usage:
 python experiments/P019_no_three_line_exchange.py --max-n 7
"""
import argparse
from itertools import combinations


def collinear(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) == (b[1]-a[1])*(c[0]-a[0])


def configurations(n):
    solutions = []
    pairs = tuple(combinations(range(n), 2))

    def extend(row, chosen, columns):
        if row == n:
            if all(count == 2 for count in columns):
                solutions.append(frozenset(chosen))
            return
        for c, d in pairs:
            if columns[c] >= 2 or columns[d] >= 2:
                continue
            u, v = (row, c), (row, d)
            # Check all triples containing at least one freshly inserted point.
            valid = not any(collinear(x,y,u) or collinear(x,y,v)
                            for x,y in combinations(chosen, 2))
            if valid and not any(collinear(x,u,v) for x in chosen):
                updated = list(columns)
                updated[c] += 1
                updated[d] += 1
                extend(row + 1, chosen + [u,v], updated)

    extend(0, [], [0] * n)
    return solutions


def component_sizes(solutions, t):
    remaining = set(solutions)
    sizes = []
    while remaining:
        stack = [remaining.pop()]
        count = 0
        while stack:
            a = stack.pop()
            count += 1
            adjacent = [b for b in remaining if len(a-b) <= t]
            for b in adjacent:
                remaining.remove(b)
            stack.extend(adjacent)
        sizes.append(count)
    return sorted(sizes, reverse=True)


def run(limit):
    expected = {
        3: (2, 1, 2),
        4: (11, 7, 4),
        5: (32, 12, 3),
        6: (50, 46, 5),
        7: (132, 92, 6),
    }
    for n in range(3, limit + 1):
        sols = configurations(n)
        assert len(sols) == len(set(sols))
        t = next(k for k in range(1,2*n+1) if len(component_sizes(sols,k)) == 1)
        outcome=(len(sols),len(component_sizes(sols,2)),t)
        assert outcome == expected[n], (n,outcome,expected[n])
        print(f"n={n}, configurations={outcome[0]}, "
              f"components_t2={outcome[1]}, min_connecting_exchange={t}")
    print("PASS: exact collinearity and exchange-connectivity checks")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-n",type=int,default=7)
    args = ap.parse_args()
    if not 3 <= args.max_n <= 7:
        ap.error("Use 3<=max-n<=7 for the exhaustively calibrated instances.")
    run(args.max_n)
