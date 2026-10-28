#!/usr/bin/env python3
"""Exact MILP for the maximum distinct-gap coprime Hamiltonian path.

Requires numpy + scipy >= 1.11.
Run: python experiments/coprime_gap_milp.py --n 24 --seconds 90
The dummy vertex 0 has NO difference label.  A status=0 connected
solution is an exact optimum; a timeout is NOT an optimality certificate.
"""
import argparse
import math
import time

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix


def solve(n: int, seconds: float = 90.0):
    if n < 2:
        raise ValueError("n must be >= 2")
    # Edges of an augmented coprime graph; 0 is adjacent to everyone.
    E = [(a,b) for a in range(n+1) for b in range(a+1,n+1)
         if a == 0 or math.gcd(a,b) == 1]
    m = len(E)
    var_count = m + n - 1  # edge x variables; difference-indicator z variables
    rows, lows, highs = [], [], []

    def add(terms, lo, hi):
        rows.append(terms)
        lows.append(lo)
        highs.append(hi)

    # A spanning 2-factor of the augmented graph.
    for v in range(n+1):
        add({j:1 for j,(a,b) in enumerate(E) if v in (a,b)}, 2, 2)

    # z_d = 1 is allowed iff at least one REAL edge of difference d is chosen.
    for d in range(1,n):
        t = {m+d-1:-1}
        t.update({j:1 for j,(a,b) in enumerate(E) if a>0 and b-a==d})
        add(t, 0, np.inf)

    tic = time.monotonic()
    for iteration in range(200):
        remain = seconds-(time.monotonic()-tic)
        if remain <= 0:
            return {"n":n, "status":"timeout", "iterations":iteration}
        A = lil_matrix((len(rows),var_count), dtype=float)
        for i,t in enumerate(rows):
            for j,v in t.items():
                A[i,j] = v
        c = np.zeros(var_count)
        c[m:] = -1
        res = milp(c, integrality=np.ones(var_count),
                   bounds=Bounds(np.zeros(var_count),np.ones(var_count)),
                   constraints=LinearConstraint(A.tocsr(),lows,highs),
                   options={"time_limit":remain,"mip_rel_gap":0.0})
        if res.x is None:
            return {"n":n,"status":f"solver_{res.status}","message":res.message}

        chosen = [e for j,e in enumerate(E) if res.x[j]>0.5]
        adj = [[] for _ in range(n+1)]
        for a,b in chosen:
            adj[a].append(b)
            adj[b].append(a)
        if not all(len(a)==2 for a in adj):
            raise AssertionError("Degree constraints unexpectedly violated")

        remaining=set(range(n+1))
        components=[]
        while remaining:
            first=next(iter(remaining))
            comp={first}
            remaining.remove(first)
            stack=[first]
            while stack:
                v=stack.pop()
                for w in adj[v]:
                    if w in remaining:
                        remaining.remove(w)
                        comp.add(w)
                        stack.append(w)
            components.append(comp)

        if len(components)==1:
            if res.status!=0:
                return {"n":n,"status":f"solver_{res.status}",
                        "message":"connected feasible path, not certified optimal"}
            # Delete dummy 0 from the unique Hamiltonian cycle.
            path=[]
            previous=-1
            current=0
            while True:
                nxt=next(x for x in adj[current] if x!=previous)
                previous,current=current,nxt
                if current==0:
                    break
                path.append(current)
            if len(path)!=n or set(path)!=set(range(1,n+1)):
                raise AssertionError("Invalid reconstructed Hamiltonian path")
            diffs={abs(a-b) for a,b in zip(path,path[1:])}
            if any(math.gcd(a,b)!=1 for a,b in zip(path,path[1:])):
                raise AssertionError("Found noncoprime path edge")
            if len(diffs)!=round(-res.fun):
                raise AssertionError("Difference-label objective mismatch")
            bound=min(n-1,(n+3)//2)
            return {"n":n,"status":"optimal","D":len(diffs),"upper_bound":bound,
                    "attains_bound":len(diffs)==bound,"path":path,
                    "iterations":iteration+1,
                    "elapsed_seconds":round(time.monotonic()-tic,3)}

        # Standard subtour elimination: no proper component may be a cycle.
        for comp in components:
            if len(comp)==n+1:
                continue
            add({j:1 for j,(a,b) in enumerate(E) if a in comp and b in comp},
                -np.inf,len(comp)-1)
    return {"n":n,"status":"subtour_iteration_limit"}


if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--n",type=int,default=12)
    ap.add_argument("--seconds",type=float,default=90)
    args=ap.parse_args()
    print(solve(args.n,args.seconds))
