#!/usr/bin/env python3
"""P027 monotone grand-coupling exploratory experiment (no dependencies).

Simultaneously update the coordinatewise minimum and maximum primitive-set
states using the same coordinate and uniform quantile. Coalescence of these
extremal states couples ALL starting states, but finite simulation gives
no theorem about the asymptotic mixing or coalescence rate.
"""
import argparse
from math import log
from random import Random
from statistics import median
from P027_autonomous_coordinates import cap


def run(n, repetitions=24, seed=2026, max_steps=500000):
    N = 2 * n
    odd = list(range(1, N + 1, 2))
    index = {u: i for i, u in enumerate(odd)}
    top = [cap(N, u, 2) for u in odd]
    bottom = [cap(N, u, 3) for u in odd]
    divisors = []
    multiples = []
    for u in odd:
        divisors.append([index[v] for v in odd if v < u and u % v == 0])
        multiples.append([index[v] for v in odd if v > u and v % u == 0])
    rng = Random(seed)
    results = []
    for repetition in range(repetitions):
        low_state = bottom.copy()
        high_state = top.copy()
        t = 0
        while low_state != high_state and t < max_steps:
            i = rng.randrange(n)
            quantile = rng.random()
            for state in (low_state, high_state):
                minimum = max([0] + [state[j] + 1 for j in multiples[i]])
                maximum = min([top[i]] + [state[j] - 1 for j in divisors[i]])
                assert minimum <= maximum, (n, i, state)
                state[i] = minimum + int(quantile * (maximum - minimum + 1))
            assert all(a <= b for a, b in zip(low_state, high_state))
            t += 1
        if low_state != high_state:
            raise RuntimeError(f"n={n}, trial={repetition}: step budget exceeded")
        results.append(t)
    return median(results), min(results), max(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", default="20,40,80,160,320")
    parser.add_argument("--repetitions", type=int, default=24)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--max-steps", type=int, default=500000)
    args = parser.parse_args()
    print(" n   median coalescence   ratio T/(n log n)   min   max")
    for n in map(int, args.sizes.split(",")):
        m, minimum, maximum = run(n, args.repetitions, args.seed, args.max_steps)
        print(f"{n:4d} {m:18.1f} {m/(n*log(n)):19.3f} {minimum:5d} {maximum:5d}")
    print("Exploratory finite simulation only; no mixing-time upper bound proved.")
