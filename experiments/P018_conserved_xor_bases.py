#!/usr/bin/env python3
"""Finite fixed-XOR basis exchange graph; standard-library exact arithmetic.

- Exhaust all W subsets of the 15 nonzero vectors in F_2^4 and verify
  that every fiber with at least 2 bases and XOR s=1 is 2-swap connected.
- Verify the explicit dimension-five disconnected fiber with 6 bases
  and connected-component sizes 4 and 2.

Using the transitive action of GL(d,2), testing s=1 suffices for every
nonzero s in the *full* vector space at a fixed dimension.

Usage: python experiments/P018_conserved_xor_bases.py
"""
from itertools import combinations
from functools import reduce


def xor_basis(vectors, d, total=1):
    if reduce(lambda x, y: x ^ y, vectors, 0) != total:
        return False
    pivots = [0] * d
    count = 0
    for value in vectors:
        while value:
            k = value.bit_length() - 1
            if pivots[k]:
                value ^= pivots[k]
            else:
                pivots[k] = value
                count += 1
                break
    return count == d


def component_sizes(bases, d, t=2):
    sets = [set(x) for x in bases]
    remaining = set(range(len(bases)))
    sizes = []
    while remaining:
        stack = [remaining.pop()]
        count = 0
        while stack:
            i = stack.pop()
            count += 1
            neighbors = [j for j in remaining
                         if 2 <= d - len(sets[i] & sets[j]) <= t]
            for j in neighbors:
                remaining.remove(j)
                stack.append(j)
        sizes.append(count)
    return sorted(sizes)


def verify_dimension_four():
    d, s = 4, 1
    universe = tuple(range(1, 1 << d))
    all_bases = [x for x in combinations(universe, d)
                 if xor_basis(x, d, s)]
    assert len(all_bases) == 56
    # Restrict the already enumerated 56 bases to each available-vector W.
    bmask = [sum(1 << (v-1) for v in B) for B in all_bases]
    nontrivial = 0
    for W in range(1 << ((1 << d) - 1)):
        indices = [i for i, m in enumerate(bmask) if (m & W) == m]
        if len(indices) < 2:
            continue
        nontrivial += 1
        # A fiber is connected iff its 2-exchange graph has one component.
        bases = [all_bases[i] for i in indices]
        comps = component_sizes(bases, d)
        assert comps == [len(bases)], (W, comps)
    print("PASS d=4: all 32768 ground-set restrictions, %d nontrivial fibers" %
          nontrivial)


def verify_dimension_five():
    d, s = 5, 1
    W = (2, 5, 8, 11, 21, 22, 24, 26, 27, 30)
    bases = [x for x in combinations(W, d) if xor_basis(x, d, s)]
    expected = [
        (2, 5, 8, 21, 27), (2, 5, 8, 22, 24),
        (2, 5, 11, 21, 24), (2, 5, 11, 22, 27),
        (8, 21, 24, 26, 30), (11, 22, 24, 26, 30),
    ]
    assert set(bases) == set(expected), bases
    sizes = component_sizes(bases, d)
    assert sizes == [2, 4], sizes
    assert component_sizes(bases, d, t=3) == [6]
    assert {8, 21} == set((2, 5, 8, 21, 27)) & set((8, 21, 24, 26, 30))
    print("PASS d=5: 10 vectors, 6 bases, t=2 components [2,4], t=3 connected")
    for B in bases:
        assert xor_basis(B, d, s)


if __name__ == "__main__":
    verify_dimension_four()
    verify_dimension_five()
