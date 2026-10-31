#!/usr/bin/env python3
"""Finite certificates for prime-product induced cycles, no dependencies."""
from math import gcd, isqrt


def primes_up_to(n):
    sieve = bytearray(b"\x01") * (n+1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * ((n-p*p)//p+1)
    return [p for p in range(2,n+1) if sieve[p]]


def verify_hole(vertices):
    k=len(vertices)
    assert k >= 4 and len(set(vertices)) == k
    for i in range(k):
        for j in range(i+1,k):
            adjacent=(j==i+1 or (i==0 and j==k-1))
            assert (gcd(vertices[i],vertices[j])>1)==adjacent,(i,j,vertices)


def audit(n):
    ps=primes_up_to(n)
    x=isqrt(n)
    low=[p for p in ps if p<=x]
    high=[p for p in ps if p>x][:len(low)]
    m=len(low)
    if m<2 or len(high)<m: return
    cond=all(low[j-1]*high[m-j+1]<=n for j in range(2,m+1))
    labels=[]
    for a,b in zip(low,high[::-1]):
        labels += [a,b]
    edge_ok=all(labels[i]*labels[(i+1)%len(labels)]<=n
                for i in range(len(labels)))
    assert cond==edge_ok,(n,cond,edge_ok)
    if cond and len(labels)>=4:
        integers=[labels[i]*labels[(i+1)%len(labels)]
                  for i in range(len(labels))]
        verify_hole(integers)
    return m,cond


def main():
    for x in [10,20,30,40,50,100,200]:
        n=x*x
        m,cond=audit(n)
        print("N=%d pi(sqrt N)=%d saturation=%s" % (n,m,cond))
    # A concrete induced C4, corresponding to prime cycle 2-5-3-7-2.
    verify_hole([14,10,15,21])
    for x,q_expected,r_expected in [(113,127,5),(1327,1361,7),(15683,15727,9)]:
        local=primes_up_to(x+100)
        small=[p for p in local if p<=x]
        q=next(p for p in local if p>x)
        r=sum(p*q>x*x for p in small)
        assert (q,r)==(q_expected,r_expected),(x,q,r)
        print("x=%d: first prime above x=%d, defect lower bound=%d" % (x,q,r))
    print("P037 certificates passed")


if __name__ == "__main__":
    main()
