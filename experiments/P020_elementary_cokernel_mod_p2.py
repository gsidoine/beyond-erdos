#!/usr/bin/env python3
"""Independent exact mod-p² checks of elementary abelian Hankel cokernel laws.

Each n×n Hankel matrix has 2n−1 independent parameters in Z/(p²).
For every reduction Hbar with corank k, a Z_p kernel-lift matrix V yields
Q=(V^T H V)/p mod p. Its nonsingularity is equivalent to the Smith factors
of coker(H) being exactly k copies of p. No floating point or random sample.
"""
from itertools import product
from collections import Counter
from fractions import Fraction


def kernel_basis(M, p):
    n = len(M)
    a = [[v % p for v in row] for row in M]
    pivot_cols, r = [], 0
    for c in range(n):
        t = next((i for i in range(r, n) if a[i][c]), None)
        if t is None:
            continue
        a[r], a[t] = a[t], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [v * inv % p for v in a[r]]
        for i in range(n):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [(x - factor * y) % p
                        for x, y in zip(a[i], a[r])]
        pivot_cols.append(c)
        r += 1

    out = []
    for c in range(n):
        if c in pivot_cols:
            continue
        v = [0] * n
        v[c] = 1
        for j, pc in enumerate(pivot_cols):
            v[pc] = -a[j][c] % p
        out.append(v)
    return out


def rank_mod(M, p):
    if not M:
        return 0
    a = [[v % p for v in row] for row in M]
    ncols, r = len(a[0]), 0
    for c in range(ncols):
        t = next((i for i in range(r, len(a)) if a[i][c]), None)
        if t is None:
            continue
        a[r], a[t] = a[t], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [v * inv % p for v in a[r]]
        for i in range(r + 1, len(a)):
            f = a[i][c]
            a[i] = [(x - f * y) % p for x, y in zip(a[i], a[r])]
        r += 1
    return r


def check(p, n):
    modulus = p * p
    total = modulus ** (2 * n - 1)
    counts = Counter()
    for entries in product(range(modulus), repeat=2 * n - 1):
        H = [[entries[i + j] for j in range(n)] for i in range(n)]
        V = kernel_basis(H, p)
        k = len(V)
        if k == 0:
            counts[0] += 1
            continue

        # Every entry of V^T H V is divisible by p.
        Q = [[(sum(V[i][r] * H[r][s] * V[j][s]
                   for r in range(n) for s in range(n)) // p) % p
              for j in range(k)] for i in range(k)]
        if rank_mod(Q, p) == k:
            counts[k] += 1

    z = Fraction(1, p)
    for k in range(n + 1):
        if k == 0:
            expected = 1 - z
        elif k < n:
            expected = (1 - z) * (z ** (2*k - 1) - z ** (2*k + 1))
        else:
            expected = (1 - z) * z ** (2*n - 1)
        actual = Fraction(counts[k], total)
        print(f"p={p} n={n} k={k}: {counts[k]}/{total} = {actual}; expected={expected}")
        assert actual == expected, (p, n, k, actual, expected)


if __name__ == "__main__":
    for p, n in [(2, 2), (2, 3), (2, 4), (3, 2), (3, 3)]:
        check(p, n)
    print("PASS: all exact elementary-abelian p-adic Hankel checks")
