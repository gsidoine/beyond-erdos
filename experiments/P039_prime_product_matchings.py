#!/usr/bin/env python3
"""Finite perfect matchings for the bilinear-prime P039 graph."""
from math import isqrt

def prime_sieve(limit):
    a=bytearray(b"\x01")*(limit+1)
    a[:2]=b"\x00\x00"
    for i in range(2,isqrt(limit)+1):
        if a[i]:
            a[i*i::i]=b"\x00"*(((limit-i*i)//i)+1)
    return a

def witness(n):
    assert n%2==0
    isprime=prime_sieve(n*n+1)
    adj=[[j for j in range(n//2) if isprime[(2*i+1)*(2*j+2)+1]]
         for i in range(n//2)]
    owner=[-1]*(n//2)
    def augment(i,seen):
        for j in adj[i]:
            if seen[j]:continue
            seen[j]=True
            if owner[j]<0 or augment(owner[j],seen):
                owner[j]=i
                return True
        return False
    for i in range(n//2):
        if not augment(i,[False]*(n//2)):return None
    pairs=[(2*owner[j]+1,2*j+2) for j in range(n//2)]
    assert len(set(x for a,b in pairs for x in (a,b)))==n
    assert all(isprime[a*b+1] for a,b in pairs)
    return pairs

def main():
    checks=list(range(2,202,2))+[250,300,400]
    for n in checks:
        assert witness(n) is not None,n
    print("P039 perfect prime-product-plus-one matchings verified for",
          len(checks),"even values; maximum N =",max(checks))
if __name__=="__main__":
    main()
