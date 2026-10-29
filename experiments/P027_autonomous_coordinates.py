#!/usr/bin/env python3
"""P027: exact free-coordinate classification, product factors and heat-bath eigenvectors.

Entirely standard library. Tests finite instances only; the infinite proofs
are in the corresponding theorem note.
"""
from collections import defaultdict
from fractions import Fraction
from math import gcd


def cap(N, u, base):
    """Largest nonnegative j with u * base**j <= N."""
    k = 0
    while u * base <= N:
        u *= base
        k += 1
    return k


def smallest_odd_prime_factor(u):
    if u == 1:
        return None
    p = 3
    while p * p <= u:
        if u % p == 0:
            return p
        p += 2
    return u


def autonomous_by_endpoints(N, u):
    m, L = cap(N, u, 3), cap(N, u, 2)
    if m == L:
        return False
    p = smallest_odd_prime_factor(u)
    if p is not None and cap(N, u // p, 3) <= L:
        return False
    if 3 * u <= N and cap(N, 3 * u, 2) >= m:
        return False
    return True


def autonomous_by_five_bands(N, u):
    assert u % 2 == 1 and 1 <= u <= N
    return bool(
        (3 * u > N and 2 * u <= N and gcd(u, 6) == 1)
        or (6 * u > N and 4 * u <= N and gcd(u, 30) == 1)
        or (6 * u > N and 27 * u <= 5 * N
            and gcd(u, 6) == 1 and u % 5 == 0)
        or (12 * u > N and 9 * u <= N and gcd(u, 210) == 1)
        or (12 * u > N and 81 * u <= 7 * N
            and gcd(u, 30) == 1 and u % 7 == 0)
    )


def feasible_exponents(n):
    """All maximum primitive sets as exponent tuples, in ascending odd-u order."""
    N = 2 * n
    odd = tuple(range(1, N + 1, 2))
    limits = {u: cap(N, u, 2) for u in odd}
    vals = {}
    results = []

    def visit(i):
        if i == len(odd):
            results.append(tuple(vals[u] for u in odd))
            return
        u = odd[-i - 1]
        lo = 1 + max((vals[v] for v in vals if v % u == 0), default=-1)
        for e in range(lo, limits[u] + 1):
            vals[u] = e
            visit(i + 1)
        del vals[u]

    visit(0)
    return odd, results


def check_product(n):
    N = 2 * n
    odd, configs = feasible_exponents(n)
    free = tuple(i for i, u in enumerate(odd)
                 if autonomous_by_five_bands(N, u))
    core = tuple(i for i in range(n) if i not in free)
    signatures = defaultdict(set)
    for exps in configs:
        bits = 0
        for j, i in enumerate(free):
            u = odd[i]
            m = cap(N, u, 3)
            assert exps[i] in (m, m + 1)
            bits |= (exps[i] - m) << j
        signatures[tuple(exps[i] for i in core)].add(bits)
    expected = set(range(1 << len(free)))
    for values in signatures.values():
        assert values == expected, (n, len(values), len(expected))
    assert len(configs) == len(signatures) * (1 << len(free))
    return len(configs), len(free), len(signatures)


def check_eigenvalue(n):
    """Independently enumerate conditional transitions for a free-site character."""
    N = 2 * n
    odd, configs = feasible_exponents(n)
    free = [i for i, u in enumerate(odd) if autonomous_by_five_bands(N, u)]
    if not free:
        return
    idx = free[0]
    floor = cap(N, odd[idx], 3)
    state_set = set(configs)
    for s in configs:
        sign = 1 if s[idx] == floor else -1
        full_expect = Fraction(0)
        for i, u in enumerate(odd):
            choices = []
            for e in range(cap(N, u, 2) + 1):
                t = s[:i] + (e,) + s[i+1:]
                if t in state_set:
                    choices.append(t)
            assert choices
            full_expect += sum(1 if t[idx] == floor else -1
                               for t in choices) * Fraction(1, n * len(choices))
        assert full_expect == sign * Fraction(n - 1, n), (n, s, full_expect)


def main():
    for n in range(1, 1001):
        N = 2 * n
        for u in range(1, N + 1, 2):
            a = autonomous_by_endpoints(N, u)
            b = autonomous_by_five_bands(N, u)
            assert a == b, (n, u, a, b)
    print("PASS five-band theorem: independent arithmetic endpoint test for n=1..1000")

    for n in range(1, 31):
        states, free, core = check_product(n)
        if n in (10, 20, 30):
            print(f"n={n}: {states} states, {free} free bits, {core} core states")
    print("PASS: every core fiber is a full fair hypercube for n=1..30")

    for n in range(1, 13):
        check_eigenvalue(n)
    print("PASS: free-coordinate eigenvalue 1-1/n in exact transition matrices")

    from fractions import Fraction
    c = sum([Fraction(1, 9), Fraction(2, 45), Fraction(1, 405),
             Fraction(4, 315), Fraction(2, 8505)])
    assert c == Fraction(1454, 8505)
    print("PASS: exact rational autonomous-coordinate density =", c)


if __name__ == "__main__":
    main()
