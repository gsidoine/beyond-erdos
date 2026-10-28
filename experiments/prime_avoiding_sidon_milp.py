"""Exact MILP for Sidon sets containing no prime differences.

Dependencies: numpy, scipy
Usage: python experiments/prime_avoiding_sidon_milp.py --N 48 --seconds 60
Only status=0 certifies an optimum. Status=1 may indicate a timeout.
"""
import argparse
import time
from math import isqrt

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix


def prime_flags(n):
    prime = [True] * (n + 1)
    prime[:2] = [False, False]
    for p in range(2, isqrt(n) + 1):
        if prime[p]:
            for j in range(p * p, n + 1, p):
                prime[j] = False
    return prime


def solve(N, seconds=60):
    if N < 2:
        raise ValueError("N must be at least 2")
    prime = prime_flags(N)
    # y_(a,b) is used only for composite/nonprime differences b-a.
    edges = [(a, b) for a in range(1, N+1)
             for b in range(a+1, N+1) if not prime[b-a]]
    variables = N + len(edges)
    rows, cols, vals, lower, upper = [], [], [], [], []

    def constraint(terms, lo, hi):
        row = len(lower)
        for column, coeff in terms:
            rows.append(row)
            cols.append(column)
            vals.append(coeff)
        lower.append(lo)
        upper.append(hi)

    # Translation preserves all differences; some optimum contains 1.
    constraint([(0, 1)], 1, 1)
    edges_by_difference = [[] for _ in range(N)]
    for j, (a, b) in enumerate(edges):
        edges_by_difference[b-a].append((N+j, 1))
        # y_(a,b) >= x_a + x_b - 1
        constraint([(a-1, 1), (b-1, 1), (N+j, -1)], -np.inf, 1)
    for d in range(1, N):
        if prime[d]:
            # No selected pair may have prime difference.
            for a in range(1, N-d+1):
                constraint([(a-1,1), (a+d-1,1)], -np.inf, 1)
        elif edges_by_difference[d]:
            # A Sidon set uses each positive difference at most once.
            constraint(edges_by_difference[d], 0, 1)

    matrix = coo_matrix((np.array(vals, dtype=float), (rows, cols)),
                        shape=(len(lower), variables)).tocsr()
    objective = np.zeros(variables)
    objective[:N] = -1
    start = time.monotonic()
    result = milp(objective,
                  integrality=np.ones(variables),
                  bounds=Bounds(np.zeros(variables), np.ones(variables)),
                  constraints=LinearConstraint(matrix, lower, upper),
                  options={"time_limit": seconds, "mip_rel_gap": 0})
    elapsed = time.monotonic() - start
    witness = ([i+1 for i, x in enumerate(result.x[:N]) if x > 0.5]
               if result.x is not None else [])
    differences = [b-a for i, a in enumerate(witness) for b in witness[i+1:]]
    if witness:
        assert len(differences) == len(set(differences))
        assert all(not prime[d] for d in differences)
    return result.status, witness, getattr(result, "mip_gap", None), elapsed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--N", type=int, default=48)
    parser.add_argument("--seconds", type=float, default=60)
    args = parser.parse_args()
    status, witness, gap, elapsed = solve(args.N, args.seconds)
    print(f"N={args.N} status={status} cardinality={len(witness)} "
          f"mip_gap={gap} elapsed_seconds={elapsed:.2f}")
    print("witness:", witness)
    print("exact_optimum:", status == 0)
