#!/usr/bin/env python3
"""Finite arithmetic set-pair construction for P038 (standard library)."""
from itertools import combinations, product
from math import gcd, comb, prod, isqrt

def primes(k):
    a=[]
    i=2
    while len(a)<k:
        if all(i%d for d in range(2,isqrt(i)+1)): a.append(i)
        i+=1
    return a

def matching(t,B):
    assert B%2==0 and t%B==0
    ps=primes(t)
    blocks=[ps[i:i+B] for i in range(0,t,B)]
    options=[list(combinations(block,B//2)) for block in blocks]
    all_selections=[frozenset(sum((list(p) for p in picks),[])) for picks in product(*options)]
    universe=set(ps)
    selected=set()
    pairs=[]
    for s in all_selections:
        if s in selected: continue
        selected.add(s)
        selected.add(frozenset(universe-s))
        pairs.append((prod(s),prod(universe-s)))
    assert len(pairs)==comb(B,B//2)**(t//B)//2
    return pairs

def main():
    for t,B in [(4,2),(6,2),(8,4),(12,4)]:
        pairs=matching(t,B)
        n=max(max(a,b) for a,b in pairs)
        assert len(set(x for pair in pairs for x in pair))==2*len(pairs)
        for i,(a,b) in enumerate(pairs):
            assert gcd(a,b)==1
            for c,d in pairs[:i]:
                assert all(gcd(x,y)>1 for x in (a,b) for y in (c,d))
        print("t=%d B=%d induced matching size=%d N=%d"%(t,B,len(pairs),n))
    print("P038 explicit prime-factor induced-matching certificates passed.")

if __name__=="__main__":
    main()
