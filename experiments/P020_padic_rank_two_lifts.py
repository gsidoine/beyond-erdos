#!/usr/bin/env python3
"""Exhaustive, dependency-free checks for P020 rank <= 2 cokernel formulas.

Enumerate all Hankel parameter vectors modulo p^e (NOT iid matrix entries).
A Smith entry with valuation e is unresolved at that precision, so exact group
types are tested only when all their exponents are strictly less than e.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def valuation(a, p, e):
    if a == 0:
        return e
    k = 0
    while a % p == 0:
        a //= p
        k += 1
    return k


def smith_exponents_mod_prime_power(matrix, p, e):
    """Smith p-valuations truncated at e, using invertible row/column moves."""
    mod = p ** e
    a = [[v % mod for v in row] for row in matrix]
    n = len(a)
    result = []
    for k in range(n):
        candidates = [(valuation(a[i][j], p, e), i, j)
                      for i in range(k, n) for j in range(k, n)]
        v, i, j = min(candidates)
        if v == e:
            result.extend([e] * (n-k))
            break
        a[k], a[i] = a[i], a[k]
        for row in a:
            row[k], row[j] = row[j], row[k]
        scale = p ** v
        reduced_mod = mod // scale
        inverse = pow((a[k][k] // scale) % reduced_mod, -1, reduced_mod)
        for i in range(k+1, n):
            mult = ((a[i][k] // scale) * inverse) % reduced_mod
            for j in range(k, n):
                a[i][j] = (a[i][j] - mult * a[k][j]) % mod
        for j in range(k+1, n):
            mult = ((a[k][j] // scale) * inverse) % reduced_mod
            for i in range(k, n):
                a[i][j] = (a[i][j] - mult * a[i][k]) % mod
        result.append(v)
    return tuple(result)


def enumerate_types(p, n, e):
    mod = p ** e
    counts = Counter()
    for diagonal in product(range(mod), repeat=2*n-1):
        matrix = [[diagonal[i+j] for j in range(n)] for i in range(n)]
        smith = smith_exponents_mod_prime_power(matrix, p, e)
        counts[tuple(v for v in smith if v > 0)] += 1
    return counts, mod ** (2*n-1)


def exact_formula(p, n, exponents):
    q = Fraction(1, p)
    if not exponents:
        return 1-q
    if len(exponents) == 1:
        (j,) = exponents
        if n == 1:
            return (1-q)*q**j
        return (q-q**3)*(1-q)*q**(j-1)
    if len(exponents) == 2:
        a,b = exponents
        rho = q**3 if n == 2 else q**3-q**5
        if a == b:
            return rho*q**(3*(a-1))*(1-q)
        return rho*q**(3*(a-1))*(q-q**3)*(1-q)*q**(b-a-1)
    raise ValueError('Theorem covers at most two positive exponents')


def run(p, n, e, targets):
    counts, total = enumerate_types(p,n,e)
    print(f'p={p}, n={n}, modulus={p**e}, total={total}')
    for target in targets:
        assert max(target, default=0) < e
        observed = Fraction(counts[target], total)
        expected = exact_formula(p,n,target)
        print(f'  type {target}: {counts[target]}/{total} = {observed}  (theory {expected})')
        assert observed == expected, (p,n,e,target,observed,expected)


if __name__ == '__main__':
    run(2,2,2,[(),(1,),(1,1)])
    run(2,3,2,[(),(1,),(1,1)])
    run(2,4,2,[(),(1,),(1,1)])
    run(3,2,2,[(),(1,),(1,1)])
    run(3,3,2,[(),(1,),(1,1)])
    # Mod p^3 distinguishes exact exponent 2 from larger exponents.
    run(2,3,3,[(1,1),(1,2),(2,2)])
    run(3,2,3,[(1,1),(1,2),(2,2)])
    print('PASS: all exact prime-power Hankel checks')
