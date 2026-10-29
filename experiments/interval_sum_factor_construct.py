#!/usr/bin/env python3
"""Construct a minimum-degree regular factor in any interval-sum graph.

Two bipartition classes are labelled 0..n-1 and edge (i,j) is present iff
a <= i+j <= b.  For every interval, the number of pairwise edge-disjoint
perfect matchings equals minimum degree.

This is an explicit *factor constructor*, not a max-flow numerical guess.
Standard library only.

Usage:
  python experiments/interval_sum_factor_construct.py --n 13 --a 9 --b 17
  python experiments/interval_sum_factor_construct.py --check-bands 100
  python experiments/interval_sum_factor_construct.py --check-intervals 25
"""
import argparse


def band_k_factor(n, k):
    """Set of edges (row, column) of a k-factor of |row-column| < k."""
    assert 1 <= k <= n
    q, r = divmod(n, k)
    blocks = [k] * (q - 1) + [k + r]
    edges = set()
    offset = 0
    for size in blocks:
        extra = size - k
        for i in range(k):
            for j in range(k):
                edges.add((offset + i, offset + j))
        for i in range(k, k + extra):
            for j in range(extra, k + extra):
                edges.add((offset + i, offset + j))
        for t in range(extra):
            for s in range(k - extra):
                i, old, new = t + s + 1, extra + s, k + t
                removed = (offset + i, offset + old)
                added = (offset + i, offset + new)
                assert removed in edges and added not in edges
                edges.remove(removed)
                edges.add(added)
        offset += size
    assert offset == n
    return edges


def interval_factor(n, a, b):
    """Return (delta, edge-set) of a delta-factor for the interval-sum graph."""
    if n < 1 or a > b:
        raise ValueError("Require n>=1 and a<=b")
    if a > n - 1 or b < n - 1:
        return 0, set()
    # The largest possible degree is n, and endpoint rows determine minimum.
    k = min(n, n - a, b - n + 2)
    assert k >= 1
    # Reverse column order to translate symmetric band to sum-interval support.
    return k, {(i, n - 1 - j) for i, j in band_k_factor(n, k)}


def verify(n, a, b, delta, edges):
    assert len(edges) == n * delta
    rdeg, cdeg = [0] * n, [0] * n
    for i, j in edges:
        assert 0 <= i < n and 0 <= j < n and a <= i + j <= b
        rdeg[i] += 1
        cdeg[j] += 1
    assert all(d == delta for d in rdeg)
    assert all(d == delta for d in cdeg)
    # Independently compute host degrees, not just a claimed formula.
    host_row = [sum(a <= i+j <= b for j in range(n)) for i in range(n)]
    host_col = [sum(a <= i+j <= b for i in range(n)) for j in range(n)]
    assert delta == min(host_row + host_col)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    select = parser.add_mutually_exclusive_group()
    select.add_argument("--check-bands", type=int, metavar="N")
    select.add_argument("--check-intervals", type=int, metavar="N")
    select.add_argument("--n", type=int, default=13)
    parser.add_argument("--a", type=int, default=9)
    parser.add_argument("--b", type=int, default=17)
    args = parser.parse_args()

    if args.check_bands:
        limit = args.check_bands
        assert limit >= 1
        for n in range(1, limit + 1):
            for k in range(1, n + 1):
                E = band_k_factor(n, k)
                assert len(E) == n * k
                degree_r, degree_c = [0]*n, [0]*n
                for i, j in E:
                    assert abs(i-j) < k
                    degree_r[i] += 1
                    degree_c[j] += 1
                assert all(d == k for d in degree_r + degree_c)
        print(f"PASS: all 1<=k<=n<={limit} band factors")
    elif args.check_intervals:
        limit = args.check_intervals
        assert limit >= 1
        cases = 0
        for n in range(1, limit + 1):
            for a in range(0, 2*n-1):
                for b in range(a, 2*n-1):
                    delta, E = interval_factor(n, a, b)
                    verify(n, a, b, delta, E)
                    cases += 1
        print(f"PASS: {cases} complete interval-sum factors through n={limit}")
    else:
        n, a, b = args.n, args.a, args.b
        k, E = interval_factor(n, a, b)
        verify(n, a, b, k, E)
        print(f"n={n} interval=[{a},{b}] delta={k}")
        print(f"edges_selected={len(E)}; factor verified")
        if n <= 15:
            for i in range(n):
                print(f"row {i}: {sorted(j for x, j in E if x==i)}")


if __name__ == "__main__":
    main()
