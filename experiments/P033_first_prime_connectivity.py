#!/usr/bin/env python3
"""Connectivity at the least prime above n in the unipartite prime-sum graph."""
from math import isqrt


def sieve(limit):
    a = bytearray([1]) * (limit+1)
    a[:2] = b"\x00\x00"
    for d in range(2,isqrt(limit)+1):
        if a[d]:
            a[d*d:limit+1:d] = bytes(len(range(d*d,limit+1,d)))
    return a


def check(n, a):
    q = next(i for i in range(n+1,2*n+1) if a[i])
    parent = list(range(n+1))

    def find(i):
        while parent[i] != i:
            parent[i]=parent[parent[i]]
            i=parent[i]
        return i

    for p in range(3,q+1,2):
        if not a[p]:
            continue
        for i in range(max(1,p-n), min(n,p-1)+1):
            j=p-i
            if i<j<=n:
                ri,rj=find(i),find(j)
                if ri!=rj:
                    parent[ri]=rj
    return q,len({find(i) for i in range(1,n+1)})


if __name__ == "__main__":
    a=sieve(1002)
    for n in range(2,501):
        q,components=check(n,a)
        assert components==1,(n,q,components)
        if n in (2,10,100,250,500):
            print(f"n={n}, first prime after n={q}, components={components}")
    print("PASS finite connectivity n=2..500; universal theorem not established")
