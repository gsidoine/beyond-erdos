#!/usr/bin/env python3
"""Exact GF(2) square-boundary rank for bipartite prime-sum graphs (no dependencies).

For each n, prove the finite statement rank(square boundaries)=cycle-space
dimension, NOT the conjecture for all n.
"""
from math import isqrt


def primes_up_to(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[:2] = b"\x00\x00"
    for d in range(2, isqrt(n) + 1):
        if sieve[d]:
            sieve[d*d:n+1:d] = bytes(len(range(d*d, n+1, d)))
    return {x for x in range(2, n+1) if sieve[x]}


def analyse(n):
    primes = primes_up_to(2*n)
    edges = [(i, j) for i in range(1, n+1) for j in range(1, n+1)
             if i+j in primes]
    index = {edge: k for k, edge in enumerate(edges)}
    neighbors = [set() for _ in range(n+1)]
    parent = list(range(2*n))

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for i, j in edges:
        neighbors[i].add(j)
        a, b = find(i-1), find(n+j-1)
        if a != b:
            parent[a] = b

    components = len({find(v) for v in range(2*n)})
    cycle_rank = len(edges)-2*n+components
    pivots = {}
    squares = 0
    for i in range(1, n+1):
        for k in range(i+1, n+1):
            common = sorted(neighbors[i] & neighbors[k])
            for a in range(len(common)):
                for b in range(a+1, len(common)):
                    j, l = common[a], common[b]
                    squares += 1
                    word = ((1 << index[i, j]) ^ (1 << index[i, l])
                            ^ (1 << index[k, j]) ^ (1 << index[k, l]))
                    while word:
                        pivot = word.bit_length() - 1
                        if pivot not in pivots:
                            pivots[pivot] = word
                            break
                        word ^= pivots[pivot]
    h1 = cycle_rank - len(pivots)
    assert h1 >= 0, (n, cycle_rank, len(pivots))
    return len(edges), cycle_rank, squares, h1


if __name__ == "__main__":
    for n in range(2, 61):
        e, r, q, h = analyse(n)
        if n in (12, 20, 40, 60):
            print(f"n={n}: edges={e}, cycle_rank={r}, four_cycles={q}, H1={h}")
        assert h == 0, (n, h)
    print("PASS: all n=2..60 (finite evidence only)")
