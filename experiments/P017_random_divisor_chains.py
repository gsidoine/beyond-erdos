#!/usr/bin/env python3
"""Longest chain in a Bernoulli-random subset of the divisibility poset [N].

Exact integer dynamic programming: scan v in increasing order, and update
best[m] for all strict multiples of every retained v. Independent seeded
Bernoulli sampling; stdlib only.

Usage:
 python experiments/P017_random_divisor_chains.py --max-power 12 --samples 10
 python experiments/P017_random_divisor_chains.py --max-power 16 --samples 20
"""
import argparse
from math import log2
from random import Random
from statistics import mean


def longest_chain(n, p, seed):
    rng = Random(seed)
    best = [0] * (n + 1)
    answer = 0
    for v in range(1, n + 1):
        if rng.random() >= p:
            continue
        height = best[v] + 1
        if height > answer:
            answer = height
        for m in range(v + v, n + 1, v):
            if height > best[m]:
                best[m] = height
    return answer


def validate_small():
    # Compare DP with exhaustive subset dynamic programming for all 2^n
    # membership patterns at n<=9, independently checking the recurrence.
    for n in range(1, 10):
        proper_divisors = [
            [d for d in range(1, v) if v % d == 0]
            for v in range(n + 1)
        ]
        for mask in range(1 << n):
            dp = [0] * (n + 1)
            for v in range(1, n + 1):
                if mask & (1 << (v - 1)):
                    dp[v] = 1 + max((dp[d] for d in proper_divisors[v]), default=0)
            target = max(dp)
            best = [0] * (n + 1)
            observed = 0
            for v in range(1, n + 1):
                if not (mask & (1 << (v - 1))):
                    continue
                height = 1 + best[v]
                observed = max(observed, height)
                for m in range(2 * v, n + 1, v):
                    best[m] = max(best[m], height)
            assert observed == target, (n, mask, observed, target)
    print("PASS: all deterministic subsets for N<=9")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-power", type=int, default=12)
    parser.add_argument("--samples", type=int, default=10)
    args = parser.parse_args()
    if args.max_power < 3 or args.samples < 1:
        parser.error("Use max-power>=3 and samples>=1.")
    validate_small()
    for p in (0.2, 0.5, 0.8):
        for exponent in range(8, args.max_power + 1, 2):
            n = 1 << exponent
            heights = [longest_chain(n, p, 104729 * i + 17) for i in range(args.samples)]
            print("p=%.1f N=%d mean_height=%.3f mean_ratio=%.3f range=[%d,%d]" % (
                p, n, mean(heights), mean(heights)/log2(n), min(heights), max(heights)
            ))


if __name__ == "__main__":
    main()
