#!/usr/bin/env python3
"""Exact K4 moment test for the random Cayley *sum* graph on Z/nZ.

Each sum s in Z/nZ is independently included with probability 1/2;
edges x--y (x != y) exist iff x+y mod n is included.

The arithmetic four-clique identity is proved for odd n (in particular
odd primes). Enumerate all 2**n sum-label subsets and check the exact
rational expectation. Standard library only, deterministic.

Usage:
    python experiments/P014_sum_flag_cliques.py
"""
from itertools import combinations
from math import comb


def k4_count_from_mask(n, mask, quads):
    count = 0
    for edge_sums in quads:
        if all((mask >> s) & 1 for s in edge_sums):
            count += 1
    return count


def validate(n):
    if n % 2 == 0 or n < 5:
        raise ValueError("Requires odd n>=5")
    quadruples = []
    special = 0
    triangles = 0
    for a, b, c in combinations(range(n), 3):
        assert len({(a+b)%n, (a+c)%n, (b+c)%n}) == 3
        triangles += 1
    for quad in combinations(range(n), 4):
        vals = tuple(sorted({(x+y)%n for x, y in combinations(quad, 2)}))
        if len(vals) == 5:
            special += 1
        else:
            assert len(vals) == 6
        quadruples.append(vals)
    assert triangles == comb(n, 3)
    predicted_special = n * (n-1) * (n-3) // 8
    assert special == predicted_special
    # At p=1/2: E K4 = (choose(n,4) + special) / 64.
    numerator = sum(
        k4_count_from_mask(n, mask, quadruples) for mask in range(1 << n)
    )
    predicted_numerator = (comb(n,4)+special) * (1<<n)
    assert 64*numerator == predicted_numerator, (
        n,numerator,predicted_numerator
    )
    print(
        f"n={n}, special_foursets={special}, mean_K4={numerator}/{1<<n}, "
        f"ER_mean_K4={comb(n,4)}/64: PASS"
    )


if __name__ == "__main__":
    for n in (5,7,9):
        validate(n)
