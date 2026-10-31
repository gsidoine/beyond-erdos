#!/usr/bin/env python3
"""Integer permanent of the squarefree absolute-displacement matrix."""
from math import factorial

def flags(n):
    sf=[True]*(n+1);sf[0]=False
    for p in range(2,int(n**.5)+1):
        if sf[p]:
            for x in range(p*p,n+1,p*p): sf[x]=False
    return sf

def permanent(n):
    if n<1:raise ValueError("n must be positive")
    sf=flags(n-1)
    rows=[sum((1<<j) for j in range(n) if sf[abs(i-j)]) for i in range(n)]
    dp=[0]*(1<<n);dp[0]=1
    for mask in range(1,1<<n):
        k=mask.bit_count()-1
        bits=mask&rows[k];total=0
        while bits:
            bit=bits&-bits;total+=dp[mask^bit];bits-=bit
        dp[mask]=total
    return dp[-1]

def main():
    expected={2:1,3:2,4:9,5:24,6:116,7:672,8:4752,
              9:27072,10:142464,11:1030176,12:9010436,
              13:67803760,14:599240185,15:6360581538,
              16:76909066689,17:828796125504}
    for n,value in expected.items():
        actual=permanent(n)
        assert actual==value,(n,actual,value)
    print("P044 exact integer permanents verified for n=2..17.")
    print("M(17) =",permanent(17))

if __name__=="__main__":main()
