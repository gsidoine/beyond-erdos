#!/usr/bin/env python3
"""Exact small-N enumeration of Sidon subsets with pairwise gcd one.

Strong Sidon means diagonal sums 2a are included.
No heuristic output is presented as a proof for general N.
"""
from math import gcd


def maximum(N):
    best = []
    nodes = 0

    def search(x, chosen, sums):
        nonlocal nodes, best
        nodes += 1
        if len(chosen) + N - x + 1 <= len(best):
            return
        if x > N:
            if len(chosen) > len(best):
                best = chosen.copy()
            return
        if all(gcd(x, y) == 1 for y in chosen):
            extra = {x + y for y in chosen} | {2 * x}
            if len(extra) == len(chosen) + 1 and extra.isdisjoint(sums):
                chosen.append(x)
                search(x + 1, chosen, sums | extra)
                chosen.pop()
        search(x + 1, chosen, sums)

    search(1, [], set())
    return best, nodes


def verify(A):
    assert all(gcd(x, y) == 1 for i, x in enumerate(A) for y in A[i+1:])
    sums = [x + y for i, x in enumerate(A) for y in A[i:]]
    assert len(sums) == len(set(sums))


if __name__ == "__main__":
    checkpoints = {1: 1, 4: 3, 7: 4, 13: 5, 22: 5, 23: 6, 26: 6}
    for n in range(1, 31):
        best, nodes = maximum(n)
        verify(best)
        if n in checkpoints:
            assert len(best) == checkpoints[n], (n, best)
            print(f"N={n}, exact optimum={len(best)}, witness={best}, branches={nodes}")
    print("PASS exact coprime Sidon optima for N=1..30")
