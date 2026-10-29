#!/usr/bin/env python3
"""Exhaustive finite-field test of Hankel-kernel product-space dimensions.

No external dependencies. Only computational evidence for equality 2k-1;
a rigorous universal lower bound is in the associated P020 research note.
"""
from collections import Counter, defaultdict
from itertools import product


def kernel_basis(matrix, p):
    n = len(matrix)
    a = [[x % p for x in row] for row in matrix]
    pivots = []
    row = 0
    for col in range(n):
        pivot = next((i for i in range(row, n) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, p)
        a[row] = [(x * inv) % p for x in a[row]]
        for i in range(n):
            if i != row and a[i][col]:
                factor = a[i][col]
                a[i] = [(u - factor * v) % p for u, v in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
    basis = []
    for col in range(n):
        if col in pivots:
            continue
        vec = [0] * n
        vec[col] = 1
        for i, pivot_col in enumerate(pivots):
            vec[pivot_col] = (-a[i][col]) % p
        basis.append(vec)
    return basis


def rank(matrix, p):
    if not matrix:
        return 0
    a = [list(row) for row in matrix]
    pivot_row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(pivot_row, len(a)) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[pivot], a[pivot_row] = a[pivot_row], a[pivot]
        inv = pow(a[pivot_row][col], -1, p)
        a[pivot_row] = [x * inv % p for x in a[pivot_row]]
        for i in range(pivot_row + 1, len(a)):
            factor = a[i][col]
            a[i] = [(u - factor * v) % p
                    for u, v in zip(a[i], a[pivot_row])]
        pivot_row += 1
    return pivot_row


def convolution(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def check(p, n):
    table = defaultdict(Counter)
    for diagonal in product(range(p), repeat=2 * n - 1):
        basis = kernel_basis([[diagonal[i + j] for j in range(n)]
                              for i in range(n)], p)
        k = len(basis)
        if not k:
            continue
        products = [convolution(basis[i], basis[j], p)
                    for i in range(k) for j in range(i, k)]
        product_rank = rank(products, p)
        table[k][product_rank] += 1
        assert product_rank == 2 * k - 1, (p, n, diagonal, k, product_rank)
    print("p", p, "n", n, {k: dict(row) for k, row in table.items()})


if __name__ == "__main__":
    for p, sizes in [(2, (3, 4, 5, 6)), (3, (3, 4, 5))]:
        for n in sizes:
            check(p, n)
    print("PASS (finite cases only)")
