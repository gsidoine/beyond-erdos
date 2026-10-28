#!/usr/bin/env python3
"""Numerical center b_n and Gumbel-window Monte Carlo for coprime percolation.

Requires numpy. Import the exact edge sampler in coprime_percolation.py.

Examples:
    python experiments/coprime_window.py --n 3000 --trials 40 --seed 90215

Use p=b_n+t*exp(gamma)*loglog(n)/n; b_n solves expected_isolates(p)=1.
These experiments DO NOT validate the asymptotic proof.
"""
import argparse
from math import exp, log

import numpy as np
from coprime_percolation import sample

EULER_GAMMA = 0.57721566490153286060651209


def host_degrees(n):
    """Exact coprime degrees by Mobius inversion (not pairwise gcd loops)."""
    mobius = np.ones(n+1, dtype=np.int64)
    mobius[0] = 0
    prime = np.ones(n+1, dtype=bool)
    prime[:2] = False
    for q in range(2,n+1):
        if prime[q]:
            mobius[q::q] *= -1
            mobius[q*q::q*q] = 0
            prime[q::q] = False
    degrees = np.zeros(n+1,dtype=np.int64)
    for k in range(1,n+1):
        if mobius[k]:
            degrees[k::k] += int(mobius[k])*(n//k)
    degrees[1] -= 1  # exclude self-edge 1--1
    if np.min(degrees[1:]) < 1:
        raise AssertionError("Unexpected isolated vertex in unthinned graph")
    return degrees[1:]


def solve_center(degrees):
    """Unique p with sum((1-p)**degree)==1, by monotone bisection."""
    lo,hi = 0.0,1.0
    for _ in range(75):
        mid=(lo+hi)/2
        mu=np.sum((1-mid)**degrees)
        if mu>1:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n",type=int,default=3000)
    parser.add_argument("--trials",type=int,default=40)
    parser.add_argument("--seed",type=int,default=90215)
    args=parser.parse_args()
    n=args.n
    if n<=5 or args.trials<1:
        parser.error("Require n>5 and trials>0")
    degrees=host_degrees(n)
    center=solve_center(degrees)
    width=exp(EULER_GAMMA)*log(log(n))/n
    nominal=log(n)*log(log(n))/n
    rng=np.random.default_rng(args.seed)
    print(f"n={n}, center={center:.9g}, center/nominal={center/nominal:.6f}, width={width:.9g}")
    print("t,p,expected_isolates,observed_mean_isolates,connected_count,trials,Gumbel_limit")
    for t in (-1.0,0.0,1.0):
        p=center+t*width
        if p<=0 or p>=1:
            raise ValueError("Window p outside (0,1); increase n")
        results=[sample(n,p,rng) for _ in range(args.trials)]
        mean_isolates=np.mean([count for count,_ in results])
        n_connected=sum(int(connected) for _,connected in results)
        expected=np.sum((1-p)**degrees)
        gumbel=exp(-exp(-t))
        print(f"{t},{p:.8g},{expected:.6g},{mean_isolates:.6g},"
              f"{n_connected},{args.trials},{gumbel:.6g}")
