#!/usr/bin/env python3
"""Finite adversarial checks for P033 three-reflection lemma and prime triples.

The eventual theorem uses PNT + Siegel-Walfisz and is NOT proved by this code.
No third-party dependencies.
"""
from itertools import combinations
from math import ceil, gcd, isqrt


def sieve(limit):
    a = bytearray([1]) * (limit + 1)
    a[:2] = b"\x00\x00"
    for d in range(2, isqrt(limit) + 1):
        if a[d]:
            a[d*d:limit+1:d] = bytes(len(range(d*d, limit+1, d)))
    return a


def components(n, sums):
    parent = list(range(n + 1))

    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for s in sums:
        for x in range(max(1, s-n), (s-1)//2 + 1):
            y = s-x
            if x < y <= n:
                a, b = root(x), root(y)
                if a != b:
                    parent[a] = b
    return len({root(v) for v in range(1, n+1)})


def step_connected(a, b, m):
    parent = list(range(m+1))

    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for v in range(1, m+1):
        for d in (a, b):
            if v+d <= m:
                x, y = root(v), root(v+d)
                if x != y:
                    parent[x] = y
    return len({root(v) for v in range(1, m+1)}) == 1


def test_deterministic_reflections():
    total = 0
    for a in range(1, 23):
        for b in range(1, 23):
            if gcd(a,b) == 1:
                assert step_connected(a,b,a+b), (a,b)
                assert step_connected(a,b,a+b+1), (a,b)
    for D in range(1, 41):
        n = 12*D + 10
        lower = [s for s in range(n-D, n) if s%2]
        higher = [s for s in range(n+1, n+D+1) if s%2]
        for p,q in combinations(lower, 2):
            a=(q-p)//2
            for r in higher:
                b=(r-p)//2
                if gcd(a,b)!=1:
                    continue
                assert components(n,(p,q,r)) == 1,(D,n,p,q,r)
                total += 1
    assert total > 1000
    print(f"PASS: interval step-graph lemma (a,b <=22) and {total} "
          "adversarial three-reflection triples (D<=40)")


def find_prime_witness(n, prime, denominator=16):
    D = ceil(n/denominator)
    below = [s for s in range(n-D, n) if prime[s]]
    above = [s for s in range(n+1, n+D+1) if prime[s]]
    for p,q in combinations(below,2):
        a=(q-p)//2
        for r in above:
            if gcd(a,(r-p)//2)==1:
                return p,q,r,D
    return None


def test_prime_examples():
    prime=sieve(32000)
    for n in (500, 1000, 2000, 5000, 10000, 30000):
        witness=find_prime_witness(n,prime)
        assert witness is not None,n
        p,q,r,D=witness
        assert n>=12*D+10
        assert p<q<n<r
        assert all(prime[s] for s in (p,q,r))
        assert gcd((q-p)//2,(r-p)//2)==1
        assert components(n,(p,q,r))==1
        print(f"n={n}: prime palette {p,q,r}, D={D}, "
              f"half-difference gcd=1, connected")


if __name__=="__main__":
    test_deterministic_reflections()
    test_prime_examples()
    print("PASS finite P033 connectivity checks; eventual theorem is analytic")
