#!/usr/bin/env python3
"""Exhaustive k-factor tests for interval-sum (Hankel) bipartite graphs.

For each n and allowed sum interval [a,b] within [0,2n-2], build the
bipartite adjacency A[i,j]=1 iff a <= i+j <= b for 0<=i,j<n.
Test whether the graph has a spanning delta-regular factor using integer
maximum flow, where delta is the *actual* minimum degree.
A factor decomposes into delta edge-disjoint perfect matchings.
Requires SciPy and NumPy.

Usage:
    python experiments/test_interval_sum_factors.py --max-n 20
    python experiments/test_interval_sum_factors.py --max-n 40

This is a finite falsification program, NOT a proof of the conjecture.
"""
import argparse

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import maximum_flow


def has_min_degree_factor(n, a, b):
    pairs = [(i, j) for i in range(n) for j in range(n)
             if a <= i + j <= b]
    left = [0] * n
    right = [0] * n
    for i, j in pairs:
        left[i] += 1
        right[j] += 1
    degree = min(min(left), min(right))
    if degree == 0:
        # Empty 0-factor is permitted by convention.
        return True, degree, 0, len(pairs)
    source, sink = 0, 2 * n + 1
    rows = [source] * n + [1 + n + j for j in range(n)]
    cols = [1 + i for i in range(n)] + [sink] * n
    capacities = [degree] * (2 * n)
    for i, j in pairs:
        rows.append(1 + i)
        cols.append(1 + n + j)
        capacities.append(1)
    matrix = coo_matrix(
        (np.asarray(capacities, dtype=np.int64), (rows, cols)),
        shape=(2 * n + 2, 2 * n + 2),
    ).tocsr()
    flow = maximum_flow(matrix, source, sink, method="dinic").flow_value
    return flow == n * degree, degree, int(flow), len(pairs)


def main(max_n):
    total = 0
    nonzero = 0
    for n in range(1, max_n + 1):
        count = 0
        for a in range(2 * n - 1):
            for b in range(a, 2 * n - 1):
                success, degree, flow, edges = has_min_degree_factor(n, a, b)
                total += 1
                count += 1
                if degree:
                    nonzero += 1
                if not success:
                    print(f"COUNTEREXAMPLE n={n}, interval=[{a},{b}], "
                          f"delta={degree}, flow={flow}, edges={edges}")
                    return 1
        print(f"n={n}: passed all {count} intervals")
    print(f"All {total} interval cases passed, {nonzero} with positive minimum degree.")
    # Failure for general noninterval sum sets, n=3, S={1,3}.
    matrix = [[int(i + j in {1, 3}) for j in range(3)] for i in range(3)]
    assert matrix == [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    print("Noninterval sum set {1,3} has delta=1 but no perfect matching at n=3.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=20)
    args = parser.parse_args()
    if args.max_n < 1:
        parser.error("--max-n must be positive")
    raise SystemExit(main(args.max_n))
