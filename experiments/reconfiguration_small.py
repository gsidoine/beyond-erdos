#!/usr/bin/env python3
"""Enumerate prime-sum matchings and alternating 4-cycle switches.

Standard library only. This exhaustive method is intended for small n.
"""
import argparse
from functools import lru_cache
from itertools import combinations


def prime_flags(limit):
    prime = [True] * (limit + 1)
    prime[:2] = [False, False]
    for p in range(2, int(limit**0.5) + 1):
        if prime[p]:
            for v in range(p*p, limit + 1, p):
                prime[v] = False
    return prime


def all_matchings(n):
    prime = prime_flags(4*n)

    @lru_cache(None)
    def extend(remaining):
        if not remaining:
            return ((),)
        a = remaining[0]
        result = []
        for j in range(1, len(remaining)):
            b = remaining[j]
            if prime[a+b]:
                leftover = remaining[1:j] + remaining[j+1:]
                for tail in extend(leftover):
                    result.append(((a,b),) + tail)
        return tuple(result)

    return extend(tuple(range(1, 2*n+1))), prime


def reconfiguration(n):
    matchings, prime = all_matchings(n)
    index = {matching: i for i, matching in enumerate(matchings)}
    parent = list(range(len(matchings)))
    size = [1] * len(matchings)

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]

    edge_count = 0
    for i, matching in enumerate(matchings):
        for j,k in combinations(range(n),2):
            a,b = matching[j]
            c,d = matching[k]
            for e,f in [((a,c),(b,d)),((a,d),(b,c))]:
                x,y = tuple(sorted(e)), tuple(sorted(f))
                if prime[x[0]+x[1]] and prime[y[0]+y[1]]:
                    swapped = list(matching)
                    swapped[j],swapped[k] = x,y
                    swapped.sort()
                    other = index.get(tuple(swapped))
                    if other is None:
                        raise AssertionError("Generated matching was not enumerated")
                    if i < other:
                        edge_count += 1
                        union(i,other)
    return len(matchings), len({find(i) for i in range(len(matchings))}), edge_count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=9)
    args = parser.parse_args()
    if args.max_n < 1:
        parser.error("--max-n must be >=1")
    print("n,matchings,components,edges")
    for n in range(1,args.max_n+1):
        count,components,edges = reconfiguration(n)
        print(f"{n},{count},{components},{edges}")


if __name__ == "__main__":
    main()
