#!/usr/bin/env python3
"""Optional numerical eigensolver for the FULL P027 heat-bath chain.

Requires numpy and scipy; NOT part of dependency-free CI.
Numerical gaps are exploratory evidence, never proofs for arbitrary n.
"""
import argparse
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh
from P027_autonomous_coordinates import cap, feasible_exponents


def heatbath_matrix(n):
    N = 2 * n
    odd, states = feasible_exponents(n)
    ids = {s: i for i, s in enumerate(states)}
    rows, cols, vals = [], [], []
    for i, s in enumerate(states):
        for j, u in enumerate(odd):
            candidate_ids = []
            for new_exp in range(cap(N, u, 2) + 1):
                t = s[:j] + (new_exp,) + s[j + 1:]
                if t in ids:
                    candidate_ids.append(ids[t])
            assert candidate_ids
            p = 1.0 / (n * len(candidate_ids))
            for dst in candidate_ids:
                rows.append(i)
                cols.append(dst)
                vals.append(p)
    P = csr_matrix((vals, (rows, cols)),
                   shape=(len(states), len(states)))
    error = np.max(np.abs(np.asarray(P.sum(axis=1)).ravel() - 1))
    assert error < 1e-12, error
    return P


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-values", default="6,10,18,25,30")
    args = parser.parse_args()
    print("n   states   gap(P_n)      n*gap")
    for n in (int(s) for s in args.n_values.split(",")):
        P = heatbath_matrix(n)
        if P.shape[0] < 2:
            continue
        if P.shape[0] <= 100:
            eig = np.linalg.eigvalsh(P.toarray())[-2:]
        else:
            eig = eigsh(P, k=2, which="LA", return_eigenvectors=False,
                        tol=1e-10)
        lam2 = sorted(eig)[-2]
        gap = 1 - lam2
        print(f"{n:<4}{P.shape[0]:<9}{gap:.9f}   {n*gap:.7f}")
        assert gap > 0


if __name__ == "__main__":
    main()
