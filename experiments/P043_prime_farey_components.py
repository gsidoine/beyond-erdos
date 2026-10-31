#!/usr/bin/env python3
"""Exact checks of the prime-denominator Farey graph and its forest."""
from collections import Counter, deque
from math import gcd

def primes_up_to(n):
    sieve=[True]*(n+1);sieve[0:2]=[False,False]
    for p in range(2,int(n**0.5)+1):
        if sieve[p]:
            for k in range(p*p,n+1,p): sieve[k]=False
    return [p for p in range(2,n+1) if sieve[p]]

def verify(N):
    ps=primes_up_to(N)
    verts=[(a,p) for p in ps for a in range(1,p)]
    lookup={v:i for i,v in enumerate(verts)}
    adj=[set() for _ in verts]
    for ix,p in enumerate(ps):
        for q in ps[ix+1:]:
            a=pow(q,-1,p); b=(a*q-1)//p
            for x,y in (((a,p),(b,q)),((p-a,p),(q-b,q))):
                i=lookup[x];j=lookup[y]
                assert i!=j
                adj[i].add(j);adj[j].add(i)
    V=len(verts)
    E=sum(map(len,adj))//2
    pi=len(ps)
    T2=sum(p+2 in ps for p in ps)
    assert E==pi*(pi-1)
    assert V==sum(p-1 for p in ps)
    def components(blocked=None):
        remaining=set(range(V))
        if blocked is not None: remaining.remove(blocked)
        out=[]
        while remaining:
            r=next(iter(remaining));remaining.remove(r)
            seen={r};queue=deque([r])
            while queue:
                for w in adj[queue.popleft()]:
                    if w in remaining: remaining.remove(w);seen.add(w);queue.append(w)
            out.append(seen)
        return out
    cc=components()
    assert len(cc)==V-E+2*T2,(N,len(cc),V-E+2*T2)
    vhalf=lookup[(1,2)]
    # A graph is a forest iff E=V-c, checked after removing the apex.
    cc_without=components(vhalf)
    e_without=E-len(adj[vhalf])
    assert e_without==(V-1)-len(cc_without)
    # Every triangle is at the apex; count via all pairs of apex neighbors.
    nbrs=sorted(adj[vhalf])
    triangles=sum(y in adj[x] for ii,x in enumerate(nbrs) for y in nbrs[ii+1:])
    assert triangles==2*T2
    C=max(len(comp) for comp in cc)
    center=next(len(comp) for comp in cc if vhalf in comp)
    return V,E,len(cc),center,C

def main():
    checks=(5,7,11,17,29,47,73,101)
    for N in checks:
        x=verify(N)
        print(f"N={N}: V={x[0]} E={x[1]} components={x[2]} central={x[3]} largest={x[4]}")
        assert x[3]==x[4]
    print("P043 exact graph, triangle, forest and component identities passed.")

if __name__=="__main__": main()
