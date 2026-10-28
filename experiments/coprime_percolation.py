#!/usr/bin/env python3
"""Monte Carlo bond percolation on the graph gcd(i,j)=1, i,j in [1,n].

Sample exact independent Bernoulli edges of the complete graph using geometric
waiting times, then reject edges whose endpoints are not coprime.
Requires numpy. These are FINITE simulations, not asymptotic proofs.

Example: python experiments/coprime_percolation.py --n 3000 --c 1.78 --trials 25
"""
import argparse
from math import gcd, log

import numpy as np


def sample(n, p, rng):
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    degree = [0] * (n + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a in range(1, n):
        b = a + 1
        while True:
            # geometric(p)-1 independent failures before next success
            b += int(rng.geometric(p)) - 1
            if b > n:
                break
            if gcd(a,b) == 1:
                degree[a] += 1
                degree[b] += 1
                root_a, root_b = find(a), find(b)
                if root_a != root_b:
                    if size[root_a] < size[root_b]:
                        root_a,root_b = root_b,root_a
                    parent[root_b] = root_a
                    size[root_a] += size[root_b]
            b += 1
    return sum(d == 0 for d in degree[1:]), size[find(1)] == n


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=3000)
    parser.add_argument("--c", type=float, default=1.78)
    parser.add_argument("--trials", type=int, default=25)
    parser.add_argument("--seed", type=int, default=90214)
    args = parser.parse_args()
    if args.n <= 2 or args.c <= 0 or args.trials <= 0:
        parser.error("n>2, c>0 and trials>0 are required")
    p = args.c * log(args.n) * log(log(args.n)) / args.n
    if p <= 0 or p >= 1:
        parser.error("Resulting edge-retention p must lie in (0,1)")
    rng = np.random.default_rng(args.seed)
    observations = [sample(args.n, p, rng) for _ in range(args.trials)]
    isolates = sum(v for v,_ in observations) / args.trials
    connected = sum(int(flag) for _,flag in observations)
    print(f"n={args.n} c={args.c} p={p:.8g} trials={args.trials} seed={args.seed}")
    print(f"mean_isolates={isolates:.6g} connected={connected}/{args.trials}")
