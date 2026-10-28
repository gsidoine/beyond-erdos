#!/usr/bin/env python3
"""Verify sufficient two-prime palette certificates for [1,2n].

The construction is fully deterministic and uses only Python standard library.
It verifies q and p=2n+q prime for each n>=2, with 3<=q<=2n-1.
For n=1 the one-color pairing {1,2} sums to prime 3.

Usage:
    python experiments/two_prime_palette.py --max-n 100000
"""
import argparse
from math import isqrt


def prime_sieve(bound):
    p = bytearray(b"\x01") * (bound + 1)
    p[0:2] = b"\x00\x00"
    for k in range(2, isqrt(bound) + 1):
        if p[k]:
            p[k * k::k] = b"\x00" * len(p[k*k::k])
    return p


def construct(n, q):
    """Return pairs with sums q (small interval) or 2n+q (large interval)."""
    assert n >= 2 and q % 2 == 1 and 3 <= q <= 2*n-1
    big = 2*n+q
    pairs = [(a, q-a) for a in range(1, (q-1)//2+1)]
    pairs += [(a, big-a) for a in range(q, (big-1)//2+1)]
    assert len(pairs) == n
    assert sorted(v for pair in pairs for v in pair) == list(range(1, 2*n+1))
    assert {a+b for a,b in pairs}.issubset({q,big})
    return pairs


def verify(max_n):
    if max_n < 2:
        raise ValueError("max_n must be at least 2")
    prime = prime_sieve(4*max_n)
    failures = []
    maximum_least_prime = (0,0)
    checkpoints = {4,7,12,57,100,1000,10000,100000}
    for n in range(2, max_n+1):
        q = next((q for q in range(3, 2*n, 2)
                  if prime[q] and prime[2*n+q]), None)
        if q is None:
            failures.append(n)
            continue
        if q > maximum_least_prime[1]:
            maximum_least_prime = (n,q)
        if n in checkpoints:
            pairs = construct(n,q)
            print(f"n={n}, q={q}, p={2*n+q}, witness_pairs={len(pairs)}, "
                  f"first_pairs={pairs[:3]}")
    print(f"checked_n=2..{max_n}, missing_certificates={len(failures)}")
    print(f"largest_least_certificate_q={maximum_least_prime[1]}, "
          f"first_attained_at_n={maximum_least_prime[0]}")
    if failures:
        print(f"failures_first_25={failures[:25]}")
        return 1
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=100000)
    args = parser.parse_args()
    raise SystemExit(verify(args.max_n))
