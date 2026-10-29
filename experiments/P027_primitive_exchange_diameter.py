#!/usr/bin/env python3
"""Exhaustive primitive-set exchange graph: distances vs odd-chain Hamming metric.

Standard-library exact finite check through N=20 (n=10).
"""
from collections import deque
from itertools import combinations


def primitive(vs):
    return all(b % a for i, a in enumerate(vs) for b in vs[i+1:])


def odd_part(x):
    while x % 2 == 0:
        x //= 2
    return x


def checks(N):
    n = N//2
    states = [frozenset(c) for c in combinations(range(1, N+1), n)
              if primitive(c)]
    state_set = set(states)
    odd = tuple(range(1, N+1, 2))
    def encoded(S):
        return {odd_part(a): a for a in S}
    profiles = {S: encoded(S) for S in states}
    adjacency = {}
    for S in states:
        adjacent = set()
        for a in S:
            for b in range(1, N+1):
                if b in S:
                    continue
                T = frozenset((S-{a})|{b})
                if T in state_set:
                    adjacent.add(T)
        adjacency[S] = adjacent

    diameter = 0
    for S in states:
        dist = {S: 0}
        queue = deque([S])
        while queue:
            X = queue.popleft()
            for T in adjacency[X]:
                if T not in dist:
                    dist[T] = dist[X]+1
                    queue.append(T)
        assert len(dist) == len(states), (N, "disconnected")
        for T, steps in dist.items():
            hamming = sum(profiles[S][u] != profiles[T][u] for u in odd)
            assert steps == hamming, (N, S, T, steps, hamming)
        diameter = max(diameter, max(dist.values()))

    formula = sum((u <= N/4 or (N/3 < u <= N/2))
                  for u in odd)
    assert diameter == formula, (N, diameter, formula)
    print(f"N={N}: states={len(states)}, diameter={diameter}")


if __name__ == "__main__":
    for N in range(2, 21, 2):
        checks(N)
    print("PASS: all exchange distances and diameter through N=20")
