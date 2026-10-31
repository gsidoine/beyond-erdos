#!/usr/bin/env python3
"""Exact arithmetic checks for the P045 complete-mapping witnesses."""
from itertools import permutations

WITNESSES = {
    5: (0, 1, 2, 3, 4),
    7: (0, 4, 6, 1, 2, 5, 3),
    11: (8, 4, 7, 1, 10, 2, 5, 6, 9, 3, 0),
    13: (0, 1, 10, 3, 4, 6, 12, 2, 8, 5, 7, 9, 11),
}

def diversity(p, f):
    assert sorted(f) == list(range(p))
    sums = [(x + f[x]) % p for x in range(p)]
    assert len(set(sums)) == p
    products = [(x * f[x]) % p for x in range(p)]
    assert sum(products) % p == 0 if p >= 5 else True
    return len(set(products))

def main():
    for p,f in WITNESSES.items():
        n = diversity(p,f)
        assert n == p-2,(p,n)
        print(f"p={p}, complete mapping: yes, distinct products={n}")
    for p in (3,5,7):
        vals = [
            diversity(p, f)
            for f in permutations(range(p))
            if len({(x+f[x])%p for x in range(p)})==p
        ]
        target = 2 if p==3 else p-2
        assert max(vals)==target,(p,max(vals))
        print(f"p={p}, brute-force optimum={target}, admissible maps={len(vals)}")
    print("P045 exact finite witnesses and exhaustive small cases passed.")

if __name__ == "__main__":
    main()
