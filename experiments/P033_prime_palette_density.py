#!/usr/bin/env python3
"""P033: exact finite certificates for three-sum connectivity and prime palette density.

Standard library only. The asymptotic singular-series theorem is in the proof note;
finite tests independently check graph connectivity, arithmetic criteria and
near-n prime triples but cannot prove the universal all-n conjecture.
"""
from bisect import bisect_left
from itertools import combinations
from math import gcd, isqrt


def primes_below(limit):
    isprime = bytearray(b"\1") * (limit + 1)
    isprime[:2] = b"\0\0"
    for p in range(2, isqrt(limit) + 1):
        if isprime[p]:
            isprime[p * p:limit + 1:p] = b"\0" * (
                (limit - p * p) // p + 1)
    return [p for p in range(3, limit + 1, 2) if isprime[p]]


def connected(n, palette):
    parent = list(range(n + 1))
    components = n

    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for s in palette:
        for x in range(max(1, s - n), (s - 1) // 2 + 1):
            y = s - x
            if x < y <= n:
                a, b = root(x), root(y)
                if a != b:
                    parent[a] = b
                    components -= 1
    return components == 1


def improved_reflection_checks():
    checked = 0
    # Distinct artificial odd sums, not assumed prime. The old version only
    # required n >= 12D+10; this certifies the sharper sufficient n >= 5D.
    for D in range(2, 41):
        for n in (5 * D, 5 * D + 1, 5 * D + 9):
            below = [p for p in range(n - D, n) if p % 2]
            above = [r for r in range(n + 1, n + D + 1) if r % 2]
            for p, q in combinations(below, 2):
                for r in above:
                    a, b = (q - p) // 2, (r - p) // 2
                    if gcd(a, b) != 1:
                        continue
                    assert connected(n, (p, q, r)), (n, D, p, q, r)
                    checked += 1
    assert checked == 77795, checked
    print(f"PASS: {checked:,} artificial three-reflection triples, "
          "all n >= 5D")


def count_primitive_prime_triples(n, primes):
    # δ=1/10, with integer-only strict endpoint comparisons.
    left = [p for p in primes if 9 * n < 10 * p < 10 * n]
    right = [r for r in primes if 10 * n < 10 * r < 11 * n]
    total = len(left) * (len(left) - 1) // 2 * len(right)
    primitive = 0
    for i, p in enumerate(left):
        for q in left[i + 1:]:
            a = (q - p) // 2
            for r in right:
                primitive += gcd(a, (r - p) // 2) == 1
    return len(left), len(right), total, primitive


def finite_prime_density_checks(primes):
    expected = {
        1000: (14, 16, 1456, 784),
        3000: (37, 33, 21978, 11108),
        10000: (112, 106, 658896, 329037),
        20000: (198, 202, 3939606, 1958663),
    }
    C = 0.75
    for p in primes:
        if p > 2:
            C *= 1.0 - 1.0 / (p - 1) ** 2
    assert abs(C - 0.49512138) < 0.000001
    for n, values in expected.items():
        observed = count_primitive_prime_triples(n, primes)
        assert observed == values, (n, observed)
        ratio = observed[3] / observed[2]
        print(f"n={n}: connecting fraction={ratio:.8f}; "
              f"limit C={C:.8f}; exact numerator={observed[3]:,}")
    assert abs(expected[20000][3] / expected[20000][2] - C) < 0.01
    print("PASS: independent finite prime-triple counts and Euler-product limit")


def nearby_prime_witness(n, primes, cap=12):
    j = bisect_left(primes, n)
    before = primes[max(0, j - cap):j]
    start = j + (j < len(primes) and primes[j] == n)
    after = primes[start:start + cap]
    for q_idx in range(len(before) - 1, 0, -1):
        q = before[q_idx]
        for p in reversed(before[:q_idx]):
            a = (q - p) // 2
            for r in after:
                D = max(n - p, r - n)
                if 5 * D <= n and gcd(a, (r - p) // 2) == 1:
                    return p, q, r, D
    return None


def million_case_certificates(primes):
    # Directly searches for a prime triple meeting a PROVED sufficient
    # condition for EVERY n. The earlier exact exhaustive palette
    # verifier covers n=3..120.
    for n in range(60, 1_000_001):
        witness = nearby_prime_witness(n, primes, cap=12)
        assert witness is not None, ("missing certified witness", n)
        if n in (60, 120, 1000, 10000, 100000, 1_000_000):
            p, q, r, D = witness
            assert p < q < n < r and 5 * D <= n
            assert gcd((q - p) // 2, (r - p) // 2) == 1
            assert connected(n, (p, q, r)), (n, witness)
            print(f"n={n}: certified prime palette={p,q,r}; D={D}")
    print("PASS: every n=60..1,000,000 has an explicit three-prime "
          "witness satisfying the proved graph criterion")


if __name__ == "__main__":
    ps = primes_below(1_210_000)
    improved_reflection_checks()
    finite_prime_density_checks(ps)
    million_case_certificates(ps)
    print("PASS P033: asymptotic theorem has independent finite checks; "
          "full all-n assertion remains unproved")
