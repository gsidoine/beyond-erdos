#!/usr/bin/env python3
"""Small-N exact verification of P027's arbitrary finite-template isolation."""
from math import gcd,isqrt


def cap(N,u,b):
    k=0
    while b*u<=N:
        u*=b
        k+=1
    return k


def is_prime(q):
    return q>=2 and all(q%d for d in range(2,isqrt(q)+1))


def isolate(T,N):
    bound=3*(T+1)**2
    odds=list(range(1,T+1,2))
    candidates=[u for u in range(N//(T+1)+1,N//T+1)
                if u%2==1 and is_prime(u) and u>bound]
    assert candidates, (T,N)
    u=candidates[0]
    V={a*u for a in odds}
    for a in odds:
        v=a*u
        assert cap(N,v,2)==cap(T,a,2)
        assert cap(N,v,3)==cap(T,a,3)
        # Every external divisor d of v must have an automatically
        # strict comparison with v.
        for d in range(1,isqrt(v)+1,2):
            if v%d:
                continue
            for x in (d,v//d):
                if x<v and x%2==1 and x not in V:
                    assert cap(N,x,3)>cap(N,v,2),(T,v,x)
        # All odd multiples of v within [N] stay in the local block.
        for x in range(3*v,N+1,2*v):
            assert x in V
    return u,len(odds)


if __name__=="__main__":
    for T in (6,12,20,36):
        root,number=isolate(T,2_000_000)
        print(f"T={T}: isolated root={root}, local dyadic chains={number}")
    print("PASS finite arithmetic-template isolation; asymptotic claim proved separately")
