#!/usr/bin/env python3
"""Finite P041 random-order divisibility chain experiments."""
from random import Random

def chain_lengths(order):
    n = len(order)
    positions = [0] * (n+1)
    for j, a in enumerate(order):
        positions[a] = j
    sf = [True] * (n+1)
    sf[0] = False
    for p in range(2, int(n**0.5)+1):
        if sf[p]:
            for j in range(p*p, n+1, p*p):
                sf[j] = False
    dp = [1]*(n+1)
    ds = [int(sf[x]) for x in range(n+1)]
    for a in range(1, n//2+1):
        for b in range(a+a, n+1, a):
            if positions[a] < positions[b]:
                dp[b] = max(dp[b], dp[a]+1)
                if sf[a] and sf[b]:
                    ds[b] = max(ds[b], ds[a]+1)
    return max(dp[1:]), max(ds[1:])

def brute(order):
    n = len(order)
    sf = {a: all(a%(i*i) for i in range(2,int(a**0.5)+1)) for a in order}
    d = s = 1
    for mask in range(1, 1<<n):
        subseq = [order[i] for i in range(n) if mask>>i & 1]
        if all(b%a==0 for a,b in zip(subseq,subseq[1:])):
            d = max(d, len(subseq))
            if all(sf[a] for a in subseq):
                s = max(s, len(subseq))
    return d,s

def verify():
    for n in range(1,11):
        order = list(range(1,n+1))
        rng = Random(41000+n)
        for _ in range(32):
            rng.shuffle(order)
            assert chain_lengths(order) == brute(order)
    print("P041 finite dynamic-programming checks passed.")
    for n in (500, 2000, 10000):
        rng = Random(n+41)
        order = list(range(1,n+1))
        vals = []
        for _ in range(25):
            rng.shuffle(order)
            vals.append(chain_lengths(order))
        print(n, *(round(sum(x[j] for x in vals)/len(vals),3) for j in range(2)))

if __name__ == "__main__":
    verify()
