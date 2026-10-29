#!/usr/bin/env python3
"""Exact F_2 Betti numbers of the complex of Sidon subsets of [N].

Faces are the subsets whose positive pairwise differences are all distinct.
This is a simplicial complex, but not a flag complex. Compute the augmented
simplicial boundary matrices as bitsets and their ranks by exact GF(2)
elimination (no floating-point solvers or third-party dependencies).

Examples:
  python experiments/P016_sidon_complex_betti.py --max-n 12
  python experiments/P016_sidon_complex_betti.py --n 23
"""
import argparse
from itertools import combinations


def is_sidon(values):
    differences = [y - x for x, y in combinations(values, 2)]
    return len(differences) == len(set(differences))


def faces_by_size(n):
    # size zero includes the empty face for *reduced* homology.
    faces = [[()]]
    for size in range(1, n + 1):
        current = [s for s in combinations(range(1, n + 1), size)
                   if is_sidon(s)]
        if not current:
            break
        faces.append(current)
    return faces


def gf2_rank(columns):
    pivots = {}
    for col in columns:
        while col:
            high = col.bit_length() - 1
            if high in pivots:
                col ^= pivots[high]
            else:
                pivots[high] = col
                break
    return len(pivots)


def compute(n):
    if n < 1:
        raise ValueError("N must be positive")
    fs = faces_by_size(n)
    # rank[k]: augmented boundary from size-k faces to size-(k-1) faces.
    ranks = [0]
    for k in range(1, len(fs)):
        row_index = {simplex: j for j, simplex in enumerate(fs[k - 1])}
        columns = []
        for simplex in fs[k]:
            boundary = 0
            for i in range(k):
                face = simplex[:i] + simplex[i + 1:]
                boundary ^= 1 << row_index[face]
            columns.append(boundary)
        ranks.append(gf2_rank(columns))
    # append 0 for boundary from nonexistent highest-dimensional faces
    ranks.append(0)
    betti = [len(fs[k]) - ranks[k] - ranks[k + 1]
             for k in range(1, len(fs))]
    assert all(b >= 0 for b in betti)
    # Augmented Euler--Poincare identity: alternating face and Betti counts.
    reduced_euler = sum((-1) ** (k - 1) * len(fs[k])
                        for k in range(len(fs)))
    homological_euler = sum((-1) ** k * b for k, b in enumerate(betti))
    assert reduced_euler == homological_euler, (
        n, reduced_euler, homological_euler
    )
    return [len(x) for x in fs[1:]], betti


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--n", type=int)
    group.add_argument("--max-n", type=int)
    args = parser.parse_args()
    maximum = args.n or args.max_n or 12
    if maximum < 1:
        parser.error("N must be positive")
    instances = [args.n] if args.n else range(2, maximum + 1)
    for n in instances:
        f, betti = compute(n)
        print(f"N={n}, faces_by_size={f}, reduced_betti_F2={betti}")


if __name__ == "__main__":
    main()
