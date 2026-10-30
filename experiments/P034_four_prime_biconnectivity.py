#!/usr/bin/env python3
"""Reproduce P034 four-prime biconnectivity certificates for odd 7<=n<=39."""
from itertools import combinations
from math import isqrt

def primes_below(limit):
    return [v for v in range(3, limit, 2)
            if all(v % d for d in range(3, isqrt(v)+1, 2))]

def biconnected(n, sums):
    adj = [set() for _ in range(n)]
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            if a+b in sums:
                adj[a-1].add(b-1); adj[b-1].add(a-1)
    if min(map(len, adj)) < 2:
        return False
    for deleted in range(n):
        start = 1 if deleted == 0 else 0
        seen = {start}; stack = [start]
        while stack:
            for v in adj[stack.pop()]:
                if v != deleted and v not in seen:
                    seen.add(v); stack.append(v)
        if len(seen) != n-1:
            return False
    return True

def main():
    for n in range(7, 40, 2):
        witness = next((s for s in combinations(primes_below(2*n), 4)
                        if biconnected(n, s)), None)
        assert witness is not None, f"no witness at {n}"
        print(n, witness)
    assert not biconnected(5, primes_below(10))
    assert biconnected(4, (3,5,7))
    print("P034: all tested cases pass (finite evidence only).")

if __name__ == "__main__":
    main()
