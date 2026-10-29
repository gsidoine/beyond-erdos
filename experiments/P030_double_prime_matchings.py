#!/usr/bin/env python3
"""Exact bipartite perfect matching checks for simultaneous prime sums/differences.

A perfect matching in the odd-even graph corresponds to an undirected pairing of
[2n]. Hopcroft-Karp is implemented with no external dependencies.
"""
from collections import deque
from math import isqrt


def primes(limit):
    sieve = [True]*(limit+1)
    sieve[:2] = [False, False]
    for p in range(2, isqrt(limit)+1):
        if sieve[p]:
            for m in range(p*p, limit+1, p):
                sieve[m] = False
    return sieve


def maximum_matching(N):
    prime = primes(2*N)
    odd = list(range(1, N+1, 2))
    even = list(range(2, N+1, 2))
    adj = {i: [j for j in even if prime[i+j] and prime[abs(i-j)]]
           for i in odd}
    left = {i: None for i in odd}
    right = {j: None for j in even}
    distance = {}

    def bfs():
        q = deque()
        for i in odd:
            if left[i] is None:
                distance[i] = 0
                q.append(i)
            else:
                distance[i] = -1
        found = False
        while q:
            i = q.popleft()
            for j in adj[i]:
                k = right[j]
                if k is None:
                    found = True
                elif distance[k] == -1:
                    distance[k] = distance[i]+1
                    q.append(k)
        return found

    def dfs(i):
        for j in adj[i]:
            k = right[j]
            if k is None or (distance[k] == distance[i]+1 and dfs(k)):
                left[i] = j
                right[j] = i
                return True
        distance[i] = -1
        return False

    size = 0
    while bfs():
        for i in odd:
            if left[i] is None and dfs(i):
                size += 1
    return size, [(i, j) for i, j in left.items() if j is not None]


if __name__ == "__main__":
    for N in range(2, 401, 2):
        size, pairs = maximum_matching(N)
        want = 0 if N == 2 else (N-2 if N in (4, 6) else N)//2
        assert size == want, (N, size, want)
        assert all(i+j > 2 and abs(i-j)>1 for i,j in pairs)
    print("PASS: all even N=8..400 admit a double-prime perfect matching")
    print("      N=2,4,6 do not; no assertion for unbounded N")
