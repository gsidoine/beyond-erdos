#!/usr/bin/env python3
"""Exhaustive prime-sum palettes, exact through n=120 (no dependencies)."""
from itertools import combinations
from math import isqrt


def primes(limit):
    p=bytearray([1])*(limit+1)
    p[:2]=b"\x00\x00"
    for d in range(2,isqrt(limit)+1):
        if p[d]:
            p[d*d:limit+1:d]=bytes(len(range(d*d,limit+1,d)))
    return [q for q in range(3,limit+1,2) if p[q]]


def components(n, palette):
    parent=list(range(n+1))

    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x

    for q in palette:
        for a in range(max(1,q-n),min(n,q-1)+1):
            b=q-a
            if a<b<=n:
                i,j=root(a),root(b)
                if i!=j:
                    parent[i]=j
    return len({root(x) for x in range(1,n+1)})


def minimum(n, max_colors=3):
    qs=primes(2*n-1)
    for k in range(1,max_colors+1):
        for palette in combinations(qs,k):
            if components(n,palette)==1:
                return k,palette
    return None,None


def two_color_formula(n):
    return any(q>=3 and q%2==1 and q in primes(2*n-1) and
               q+2 in primes(2*n-1) for q in (n-1,n,n+1))


if __name__=="__main__":
    counts={2:0,3:0}
    for n in range(3,121):
        k,palette=minimum(n,3)
        assert k in (2,3),(n,k)
        assert (k==2)==two_color_formula(n),(n,k,palette)
        counts[k]+=1
        if n in (3,7,10,50,120):
            print(f"n={n}: minimum prime colors={k}, witness={palette}")
    assert counts=={2:28,3:90},counts
    print("PASS exact kappa(n) in {2,3} for all n=3..120")
    print("PASS twin-prime iff two-color theorem on all finite instances")
