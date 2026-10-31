#!/usr/bin/env python3
"""Exact finite checks of APN-derived XOR Sidon sets of primes in dyadic intervals."""
from math import ceil

POLY = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011,
        5: 0b100101, 6: 0b1000011}

def mul(a,b,k):
    poly=POLY[k]
    mask=(1<<k)-1
    ans=0
    while b:
        if b&1:ans^=a
        b>>=1
        a<<=1
        if a&(1<<k):a^=poly
    return ans&mask

def sidon_construction(m):
    K=m-1
    k=K//2
    assert k in POLY
    S=[(x<<k)|mul(mul(x,x,k),x,k) for x in range(1<<k)]
    assert len(S)==len(set(S))
    pair_xors=[a^b for j,a in enumerate(S) for b in S[j+1:]]
    assert len(pair_xors)==len(set(pair_xors))
    assert all(x>0 for x in pair_xors)
    return S

def primes_interval(m):
    end=1<<(m+1)
    sieve=[True]*end
    sieve[0]=sieve[1]=False
    for p in range(2,int(end**0.5)+1):
        if sieve[p]:
            for t in range(p*p,end,p):sieve[t]=False
    return [p for p in range(1<<m,end) if sieve[p]]

def verify():
    for m in range(4,13):
        S=sidon_construction(m)
        P=[(p-(1<<m)-1)//2 for p in primes_interval(m)]
        H=1<<(m-1)
        assert all(0<=x<H for x in P)
        Pset=set(P)
        translates=[sum((x^t) in Pset for x in S) for t in range(H)]
        best=max(translates)
        assert best*H>=len(S)*len(P)
        upper_bound=(1+(1+8*(H-1))**.5)/2
        assert len(P)<=upper_bound or best<=upper_bound
        if best>=2:
            best_t=translates.index(best)
            selected=sorted(x^best_t for x in S if (x^best_t) in Pset)
            xors=[a^b for j,a in enumerate(selected) for b in selected[j+1:]]
            assert len(xors)==len(set(xors))
        print(f"m={m} primes={len(P)} translated-Sidon={best} APN-size={len(S)}")
    print("P046 finite APN, XOR Sidon and prime-translate checks passed.")

if __name__=="__main__":
    verify()
