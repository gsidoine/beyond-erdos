#!/usr/bin/env python3
"""Exact minimum coprime-adjacency count in a permutation of [1,n].

Binary Hamiltonian-cycle MILP on {0,...,n}; vertex 0 is a dummy.
The dummy's incident edges have zero cost. Iteratively remove subtours.

Dependencies: numpy, scipy>=1.11.
Usage:
    python experiments/minimum_coprime_adjacencies.py --n 100 --seconds 120

Only status=optimal certifies global optimality. The script checks the
permutation witness as well as all degree and connectivity constraints.
"""
import argparse
import math
import time

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix


def prime_pi(x):
    if x < 2:
        return 0
    count = 0
    for p in range(2, int(x) + 1):
        if all(p % d for d in range(2, math.isqrt(p) + 1)):
            count += 1
    return count


def elementary_lower_bound(n):
    a = prime_pi(n) - prime_pi(n//2)
    b = prime_pi(n//2) - prime_pi(n//3)
    return a + (b+1)//2


def solve(n, seconds=120.0):
    if n < 3:
        raise ValueError("The augmented cycle formulation requires n>=3")
    edges = [(i,j) for i in range(n+1)
             for j in range(i+1,n+1)]
    m = len(edges)
    costs = np.array([int(i>0 and math.gcd(i,j)==1)
                      for i,j in edges], dtype=float)
    rows = []
    lows = []
    highs = []

    for v in range(n+1):
        rows.append({k:1 for k,(a,b) in enumerate(edges) if a==v or b==v})
        lows.append(2)
        highs.append(2)

    start = time.monotonic()
    for iteration in range(300):
        remaining = seconds-(time.monotonic()-start)
        if remaining <= 0:
            return {"n":n,"status":"timeout","iterations":iteration}
        matrix = lil_matrix((len(rows),m),dtype=float)
        for i,terms in enumerate(rows):
            for j,value in terms.items():
                matrix[i,j] = value
        res = milp(costs,integrality=np.ones(m),
                   bounds=Bounds(np.zeros(m),np.ones(m)),
                   constraints=LinearConstraint(matrix.tocsr(),lows,highs),
                   options={"time_limit":remaining,"mip_rel_gap":0})
        if res.x is None:
            return {"n":n,"status":f"solver_{res.status}",
                    "message":res.message}

        chosen = [e for k,e in enumerate(edges) if res.x[k]>.5]
        adjacency = [[] for _ in range(n+1)]
        for a,b in chosen:
            adjacency[a].append(b)
            adjacency[b].append(a)
        if not all(len(ngh)==2 for ngh in adjacency):
            raise AssertionError("Wrong degree: MILP did not return a 2-factor")

        remainder=set(range(n+1))
        components=[]
        while remainder:
            seed=next(iter(remainder))
            component={seed}
            remainder.remove(seed)
            stack=[seed]
            while stack:
                u=stack.pop()
                for v in adjacency[u]:
                    if v in remainder:
                        component.add(v)
                        remainder.remove(v)
                        stack.append(v)
            components.append(component)

        if len(components)==1:
            if res.status!=0:
                return {"n":n,"status":f"solver_{res.status}",
                        "reason":"Feasible connected tour not certified optimal"}
            sequence=[]
            previous=-1
            vertex=0
            while True:
                next_v=next(x for x in adjacency[vertex] if x!=previous)
                previous,vertex=vertex,next_v
                if vertex==0:
                    break
                sequence.append(vertex)
            if sorted(sequence)!=list(range(1,n+1)):
                raise AssertionError("Tour did not include each integer once")
            count=sum(math.gcd(a,b)==1
                      for a,b in zip(sequence,sequence[1:]))
            if count!=round(res.fun):
                raise AssertionError("Objective and witnessed coprime count disagree")
            return {"n":n,"status":"optimal","minimum":count,
                    "lower_bound":elementary_lower_bound(n),
                    "upper_bound":prime_pi(n),"path":sequence,
                    "iterations":iteration+1,
                    "seconds":round(time.monotonic()-start,3)}

        # A proper connected component of a 2-factor is an invalid subtour.
        for component in components:
            rows.append({k:1 for k,(a,b) in enumerate(edges)
                         if a in component and b in component})
            lows.append(-np.inf)
            highs.append(len(component)-1)

    return {"n":n,"status":"subtour_cut_iteration_limit"}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n",type=int,default=60)
    parser.add_argument("--seconds",type=float,default=120)
    args=parser.parse_args()
    print(solve(args.n,args.seconds))
