#!/usr/bin/env python3
"""Independent exact arithmetic checks for random divisor-order-complex Euler means."""
from fractions import Fraction
from itertools import combinations


def expected_via_subsets(N, p):
    elements = range(2, N+1)
    q = 1-p
    total = Fraction(0)
    for mask in range(1 << (N-1)):
        verts = [x for i, x in enumerate(elements) if mask & (1 << i)]
        prob = p**len(verts)*q**(N-1-len(verts))
        # Count strict divisor chains by terminal vertex.
        chains = {}
        for v in verts:
            chains[v] = 1-sum(chains[d] for d in verts if d<v and v % d == 0)
        euler = -1+sum(chains.values())
        total += prob*euler
    return total


def via_dirichlet_recurrence(N, p):
    phi = [Fraction(0)]*(N+1)
    for m in range(2, N+1):
        phi[m] = p*(1-sum(phi[d] for d in range(2, m) if m % d == 0))
    return -1+sum(phi[2:]), phi


if __name__ == "__main__":
    for p in [Fraction(0), Fraction(1, 4), Fraction(1, 2),
              Fraction(3, 4), Fraction(1)]:
        for N in range(2, 10):
            exact = expected_via_subsets(N, p)
            formula, _ = via_dirichlet_recurrence(N, p)
            assert exact == formula, (p, N, exact, formula)
        print(f"p={p}: exact subset enumeration agrees through N=9")
    print("PASS: all exact finite divisor-complex Euler means")
