#!/usr/bin/env python3
"""Independent falsification checks for P003 (max-flow) and P009 (prime pairs).

Requires SciPy only for P003. All comparisons are exact integer tests.

Examples:
  python audits/verify_p003_p009.py --factors 100,500,3000 --palette 1000000
"""
import argparse
from math import isqrt


def prime_flags(limit):
    flags = bytearray(b"\x01") * (limit + 1)
    flags[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            flags[p*p::p] = b"\x00" * len(flags[p*p::p])
    return flags


def verify_p003(n):
    from scipy.sparse import coo_matrix
    from scipy.sparse.csgraph import maximum_flow

    prime = prime_flags(4*n)
    edges = []
    odd_degrees = [0] * n
    even_degrees = [0] * n
    for i in range(n):
        for j in range(n):
            if prime[2*i + 2*j + 3]:
                edges.append((i,j))
                odd_degrees[i] += 1
                even_degrees[j] += 1
    delta = min(min(odd_degrees), min(even_degrees))
    rows, cols, caps = [], [], []
    def add(u,v,capacity):
        rows.append(u)
        cols.append(v)
        caps.append(capacity)
    source, sink = 0, 2*n+1
    for i in range(n):
        add(source, 1+i, delta)
        add(1+n+i, sink, delta)
    for i,j in edges:
        add(1+i, 1+n+j, 1)
    graph = coo_matrix((caps,(rows,cols)),
                       shape=(2*n+2,2*n+2),dtype="int64").tocsr()
    value = maximum_flow(graph,source,sink,method="dinic").flow_value
    print(f"P003 n={n} edges={len(edges)} delta={delta} "
          f"flow={value} target={n*delta} equality={value==n*delta}")
    return value==n*delta


def verify_p009(max_n):
    # Bound 4*max_n covers every candidate p=2n+q, q<2n.
    prime=prime_flags(4*max_n)
    missing=[]
    max_q = 0
    max_q_at = None
    for n in range(2,max_n+1):
        witness = next((q for q in range(3,2*n,2)
                        if prime[q] and prime[2*n+q]),None)
        if witness is None:
            missing.append(n)
        elif witness > max_q:
            max_q,max_q_at=witness,n
    print(f"P009 n=2..{max_n}, missing={len(missing)}, "
          f"max_least_q={max_q}, first_n={max_q_at}, "
          f"first_missing={missing[:10]}")
    return not missing


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--factors",default="100,500,3000")
    p.add_argument("--palette",type=int,default=1000000)
    a=p.parse_args()
    factors=[int(x) for x in a.factors.split(",") if x]
    all_factor=all(verify_p003(n) for n in factors)
    all_palette=verify_p009(a.palette)
    raise SystemExit(0 if all_factor and all_palette else 1)
