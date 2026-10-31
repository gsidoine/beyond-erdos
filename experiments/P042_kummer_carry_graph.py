#!/usr/bin/env python3
"""Exact finite checks for the binary one-carry graph P042 (stdlib only)."""
from collections import deque
from math import comb

WITNESSES = {
    4: [7,4,6,5,1,13,10,3,2,11,12,9,14,8,15],
    5: [15,8,14,9,12,11,2,27,20,7,4,23,24,19,28,18,
        29,1,13,10,3,26,21,6,5,25,22,17,30,16,31],
}

def carry_count(a, b):
    return a.bit_count() + b.bit_count() - (a+b).bit_count()

def valuation_two(n):
    if n <= 0:
        raise ValueError("Positive integer required")
    return (n & -n).bit_length()-1

def graph(m):
    n=1<<m
    adj=[set() for _ in range(n)]
    for a in range(1,n):
        for b in range(a+1,n):
            if carry_count(a,b)==1:
                adj[a].add(b);adj[b].add(a)
    return adj

def components(adj):
    remaining=set(range(1,len(adj)))
    result=[]
    while remaining:
        start=next(iter(remaining))
        seen={start}
        remaining.remove(start)
        queue=deque([start])
        while queue:
            for y in adj[queue.popleft()]:
                if y in remaining:
                    remaining.remove(y);seen.add(y);queue.append(y)
        result.append(seen)
    return result

def verify():
    for m in range(2,9):
        adj=graph(m)
        n=(1<<m)-1
        edges=sum(len(adj[i]) for i in range(1,n+1))//2
        expected=((m+2)*3**(m-2)-m)//2
        assert edges==expected,(m,edges,expected)
        comps=components(adj)
        if m>=4:
            assert len(comps)==1
            leaves=[i for i in range(1,n+1) if len(adj[i])==1]
            assert leaves==[(1<<(m-1))-1,(1<<m)-1],(m,leaves)
            assert adj[leaves[0]]=={1<<(m-2)}
            assert adj[leaves[1]]=={1<<(m-1)}
        else:
            assert len(comps)>1
        if m<=5:
            for a in range(1,n+1):
                for b in range(a+1,n+1):
                    v=valuation_two(comb(a+b,a))
                    assert (b in adj[a])==(v==1),(m,a,b,v)
        print("m=%d vertices=%d edges=%d components=%d" %
              (m,n,edges,len(comps)))
    for m,path in WITNESSES.items():
        adj=graph(m)
        n=(1<<m)-1
        assert len(path)==n and set(path)==set(range(1,n+1))
        assert path[0]==(1<<(m-1))-1
        assert path[-1]==(1<<m)-1
        assert all(b in adj[a] for a,b in zip(path,path[1:]))
        print("Hamiltonian witness m=%d: verified" % m)
    print("P042 finite checks passed.")

if __name__=="__main__":
    verify()
