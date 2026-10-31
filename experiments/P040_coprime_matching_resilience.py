#!/usr/bin/env python3
"""Exact Hall-obstruction enumeration for P040, no external packages."""
from itertools import combinations
from fractions import Fraction
from math import gcd
import argparse

def resilience(n):
    adj=[sum((1<<j) for j in range(n) if gcd(2*i+2,2*j+1)==1)
         for i in range(n)]
    d_e=[x.bit_count() for x in adj]
    d_o=[sum((x>>j)&1 for x in adj) for j in range(n)]
    best=Fraction(2)
    allmask=(1<<n)-1
    for k in range(1,n+1):
        odd_T=[sum(1<<j for j in T) for T in combinations(range(n),k-1)]
        for S in combinations(range(n),k):
            a=[sum((adj[i]>>j)&1 for i in S) for j in range(n)]
            for T in odd_T:
                U=allmask^T
                score=Fraction(0)
                for i in S:
                    score=max(score,Fraction((adj[i]&U).bit_count(),d_e[i]))
                    if score>=best:break
                else:
                    for j in range(n):
                        if U>>j&1:
                            score=max(score,Fraction(a[j],d_o[j]))
                            if score>=best:break
                if score<best:best=score
    return best

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--max-n",type=int,default=9)
    nmax=parser.parse_args().max_n
    known={2:Fraction(1),3:Fraction(2,3),4:Fraction(3,4),
           5:Fraction(3,5),6:Fraction(3,5),7:Fraction(1,2),
           8:Fraction(4,7),9:Fraction(1,2),10:Fraction(1,2)}
    for n in range(2,nmax+1):
        r=resilience(n)
        assert r==known[n],(n,r,known[n])
        print("P040 n=%d rho=%s"%(n,r))
    print("P040 exact finite Hall certificates passed")

if __name__=="__main__":
    main()
