#!/usr/bin/env python3
"""Exhaustively enumerate prime-supported anti-diagonal permutation X-ray fibers."""
from collections import defaultdict
from math import isqrt


def primes(limit):
    return {x for x in range(2, limit+1)
            if x > 1 and all(x % d for d in range(2, isqrt(x)+1))}


def fibres(n):
    P = primes(2*n)
    admissible = {i: [j for j in range(1, n+1) if i+j in P]
                  for i in range(1, n+1)}
    result = defaultdict(list)

    def visit(i, used, values):
        if i > n:
            xray = tuple(sorted(k+values[k-1] for k in range(1, n+1)))
            result[xray].append(tuple(values))
            return
        for j in admissible[i]:
            if j not in used:
                used.add(j)
                values.append(j)
                visit(i+1, used, values)
                values.pop()
                used.remove(j)
    visit(1, set(), [])
    return result


if __name__ == "__main__":
    expected = [(2, 3, 4, 1), (4, 1, 2, 3)]
    for n in range(2, 14):
        d = fibres(n)
        if n == 4:
            assert sorted(d[(3, 5, 5, 7)]) == expected
            print("n=4: exact two-member fiber (3,5,5,7), distance=4")
        print(f"n={n}: {sum(map(len,d.values()))} matchings; "
              f"{len(d)} X-ray fibers")
    print("PASS: all finite enumerations n=2..13")
