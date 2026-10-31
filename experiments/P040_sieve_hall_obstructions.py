#!/usr/bin/env python3
"""Exact certificates for P040's finite-prime Hall obstructions.

Independent of numerical optimization; all key inequalities use Fraction.
The finite n=1155 check constructs actual edge deletions violating Hall.
"""
from fractions import Fraction
from math import gcd
from itertools import product


CERTIFICATES = [
    ((3, 5, 7), tuple(range(1, 8)), Fraction(19, 35), Fraction(7, 15)),
    ((3, 5, 7, 11), (1, 2, 3, 4, 5, 6, 7, 11, 13),
     Fraction(116, 231), Fraction(71, 165)),
    ((3, 5, 7, 11, 13),
     (1, 2, 3, 4, 5, 6, 7, 13, 14, 15, 17, 18, 19, 20, 21, 22, 25, 29, 31),
     Fraction(683, 1365), Fraction(914, 2145)),
    ((3, 5, 7, 11, 13, 17),
     tuple(sorted(set((1, 2, 3, 4, 5, 6, 7, 13, 14, 15, 17, 18, 20, 21,
                       22, 23, 27, 29, 30, 31)) |
                  {m + 32 for m in (1, 2, 3, 4, 5, 6, 7, 13, 14, 15, 17,
                                    18, 20, 21, 22, 23, 27, 29, 30, 31)} |
                  {19, 43})),
     Fraction(18233, 36465), Fraction(5163, 12155)),
]


def signature(x, primes):
    return sum((1 << i) for i, p in enumerate(primes) if x % p == 0)


def weights(primes):
    w = []
    for mask in range(1 << len(primes)):
        f = Fraction(1)
        for i, p in enumerate(primes):
            f *= Fraction(1, p) if mask & (1 << i) else Fraction(p-1, p)
        w.append(f)
    assert sum(w) == 1
    return w


def check_rational_certificate(primes, allowed, mass_expected, bound_expected):
    w = weights(primes)
    universe = range(len(w))
    allowed = set(allowed)
    mu = sum((w[t] for t in allowed), Fraction(0))
    assert mu == mass_expected
    assert mu > Fraction(1, 2)
    conditional = {}
    for s in allowed:
        denom = sum((w[t] for t in universe if not (s & t)), Fraction(0))
        numer = sum((w[t] for t in allowed if not (s & t)), Fraction(0))
        conditional[s] = numer / denom
    observed = max(conditional.values())
    assert observed == bound_expected, (primes, observed, bound_expected)
    print("P=%s mass=%s max-removed=%s attaining=%s" %
          (primes, mu, observed,
           tuple(s for s in conditional if conditional[s] == observed)))


def check_concrete_hall_obstruction(n=1155):
    primes = (3, 5, 7, 11)
    allowed = {1, 2, 3, 4, 5, 6, 7, 11, 13}
    even = list(range(2, 2*n+1, 2))
    odd = list(range(1, 2*n, 2))
    is_even_selected = [signature(x, primes) in allowed for x in even]
    is_odd_selected = [signature(y, primes) in allowed for y in odd]
    assert sum(is_even_selected) == 580
    assert sum(is_odd_selected) == 580
    assert sum(is_even_selected) > n - sum(is_odd_selected)
    selected_odd = [y for y, selected in zip(odd, is_odd_selected) if selected]
    selected_even = [x for x, selected in zip(even, is_even_selected) if selected]
    worst = Fraction(0)
    for x in selected_even:
        loss = sum(gcd(x, y) == 1 for y in selected_odd)
        deg = sum(gcd(x, y) == 1 for y in odd)
        worst = max(worst, Fraction(loss, deg))
    for y in selected_odd:
        loss = sum(gcd(x, y) == 1 for x in selected_even)
        deg = sum(gcd(x, y) == 1 for x in even)
        worst = max(worst, Fraction(loss, deg))
    assert worst < Fraction(1, 2)
    print("N=2n=%d, selected each side=580, exact largest deleted degree fraction=%s" %
          (2*n, worst))


if __name__ == "__main__":
    for args in CERTIFICATES:
        check_rational_certificate(*args)
    check_concrete_hall_obstruction()
    print("P040 modular Hall obstruction certificates passed.")
