#!/usr/bin/env python3
"""Exact coefficient-rank check for P036's separated Pasch witness."""
from itertools import combinations
from fractions import Fraction

V = [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(1,1,1)]

def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for col in range(3):
        pivot = next((i for i in range(r,len(a)) if a[i][col]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        z=a[r][col]
        a[r]=[x/z for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                z=a[i][col]
                a[i]=[u-z*v for u,v in zip(a[i],a[r])]
        r+=1
        if r==len(a): break
    return r

expected={1:1,2:2,3:2,4:3,5:3,6:3}
for k in range(1,7):
    observed=min(rank([V[i] for i in idx]) for idx in combinations(range(6),k))
    assert observed==expected[k],(k,observed)
print("P036 six-form overlap ranks verified:", expected)
