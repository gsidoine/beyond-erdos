#!/usr/bin/env python3
"""Independent finite verification of P020's second-order small-kernel laws.

Enumerates all 4^5 Hankel 3x3 matrices modulo 4 (p=2).
No external packages required. Does not assume the theorem's probability formula.
"""
from itertools import product


def rank_mod2(rows):
    if not rows:
        return 0
    a = [[v & 1 for v in row] for row in rows]
    m, n = len(a), len(a[0])
    pivot = 0
    for j in range(n):
        target = next((i for i in range(pivot, m) if a[i][j]), None)
        if target is None:
            continue
        a[pivot], a[target] = a[target], a[pivot]
        for i in range(m):
            if i != pivot and a[i][j]:
                a[i] = [x ^ y for x, y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == m:
            break
    return pivot


def radical_basis(A):
    n = len(A)
    basis = []
    for v in product((0, 1), repeat=n):
        if not any(v) or any(sum(A[i][h] * v[h] for h in range(n)) & 1 for i in range(n)):
            continue
        if rank_mod2(basis + [v]) > len(basis):
            basis.append(v)
    return basis


def second_order_form(A, basis):
    # A mod 2 kills each basis vector, hence all pairings are even.
    return [[(sum(u[a] * A[a][b] * v[b]
                  for a in range(3) for b in range(3)) // 2) & 1
             for v in basis] for u in basis]


def main():
    totals = [0] * 4
    full_second = {1: 0, 2: 0}
    for coefficients in product(range(4), repeat=5):
        A = [[coefficients[i + j] for j in range(3)] for i in range(3)]
        nullity = 3 - rank_mod2(A)
        totals[nullity] += 1
        if nullity in (1, 2):
            K = radical_basis(A)
            assert len(K) == nullity
            if rank_mod2(second_order_form(A, K)) == nullity:
                full_second[nullity] += 1
    print("coranks:", totals, "second-order nonsingular:", full_second)
    assert totals == [512, 384, 96, 32]
    assert full_second == {1: 192, 2: 48}
    print("P020 small-residual second-order audit passed.")


if __name__ == "__main__":
    main()
