#!/usr/bin/env python3
"""Exact finite prime-sum bipartite graph diameters.

The sum-two edge (L1,R1) is the sole bridge joining the two parity hosts.
The exact diameter can be checked via two BFS eccentricities when connected.
All-pairs diameter is independently checked for n up to 35.
"""
from collections import deque
from math import isqrt


def primes(limit):
    p = bytearray([1]) * (limit + 1)
    p[:2] = b"\x00\x00"
    for d in range(2, isqrt(limit) + 1):
        if p[d]:
            p[d*d:limit+1:d] = bytes(len(range(d*d, limit + 1, d)))
    return p


def graph(n, P):
    edges = [[] for _ in range(2*n)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if P[i+j]:
                u,v=i-1,n+j-1
                edges[u].append(v)
                edges[v].append(u)
    return edges


def distances(edges, start):
    dist = [-1]*len(edges)
    dist[start] = 0
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in edges[u]:
            if dist[v] == -1:
                dist[v] = dist[u]+1
                queue.append(v)
    return dist


if __name__ == "__main__":
    P = primes(700)
    for n in range(2, 251):
        G = graph(n, P)
        # Delete the unique sum-two bridge in a copy for a structural check.
        left1,right1 = 0,n
        assert right1 in G[left1]
        H = [lst.copy() for lst in G]
        H[left1].remove(right1)
        H[right1].remove(left1)
        a = distances(H,left1)
        b = distances(H,right1)
        side_a={v for v,d in enumerate(a) if d>=0}
        side_b={v for v,d in enumerate(b) if d>=0}
        assert side_a.isdisjoint(side_b) and len(side_a|side_b)==2*n
        assert max(a)==max(b)
        diameter=2*max(a)+1
        if n <= 35:
            complete=max(max(distances(G,v)) for v in range(2*n))
            assert diameter==complete,(n,diameter,complete)
        expected=3 if n==2 else (5 if n<=7 else 7)
        assert diameter==expected,(n,diameter)
        if n in (2,7,8,30,100,250):
            print(f"n={n}, diameter={diameter}, bridge-side eccentricity={max(a)}")
    print("PASS exact finite bipartite graph diameters n=2..250")
