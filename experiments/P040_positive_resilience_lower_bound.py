#!/usr/bin/env python3
"""Finite sanity checks for P040's analytic coprime-density/moment lemmas.

Not a proof of the limiting theorem: the complete argument is in
theorems/P040-positive-resilience-lower-bound.md.
"""
from math import gcd, pi, exp, prod, isqrt


def odd_prime_factors(v):
    result = []
    while v % 2 == 0:
        v //= 2
    p = 3
    while p * p <= v:
        if v % p == 0:
            result.append(p)
            while v % p == 0:
                v //= p
        p += 2
    if v > 1:
        result.append(v)
    return result


def theta(v):
    return prod((1 - 1 / p for p in odd_prime_factors(v)), start=1.0)


def density_and_moments(n):
    evens = range(2, 2*n+1, 2)
    odds = range(1, 2*n, 2)
    edges = sum(gcd(e, o) == 1 for e in evens for o in odds)
    m_even = sum(theta(e)**-4 for e in evens) / n
    m_odd = sum(theta(o)**-4 for o in odds) / n
    return edges/n**2, m_even, m_odd


def main():
    q = 8 / pi**2
    c = 16 / pi**2 - 3/2
    assert 0.12 < c < 0.122
    C4_upper = (113/48)*(1649/1280)*exp(7*(1/49 + 1/14))
    assert C4_upper < 6
    assert 6 * (2/5)**3 / (4/5)**4 == 15/16
    for n in (100, 300, 1000):
        d, a, b = density_and_moments(n)
        assert abs(d-q) < 0.02, (n, d)
        assert a < 6 and b < 6, (n, a, b)
        print("n=%d coprime-density=%.6f fourth-moments=(%.6f,%.6f)" %
              (n, d, a, b))
    print("P040 lower-bound numerical cross-checks passed")


if __name__ == "__main__":
    main()
