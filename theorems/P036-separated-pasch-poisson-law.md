# P036 — Poisson law for a separated arithmetic Pasch family

**Status:** internally proved. This is a *witness-family* theorem, not a proof of the global two-core threshold or of a full critical-window law. No claim of historical originality is made.

## A six-vertex family

For any integer $N$, choose three parameters independently in the disjoint intervals

$$
a\in I_1(N)=[\lceil .04N\rceil,\lfloor .05N\rfloor],\quad
b\in I_2(N)=[\lceil .10N\rceil,\lfloor .11N\rfloor],\quad
d\in I_3(N)=[\lceil .20N\rceil,\lfloor .21N\rfloor].
$$

For large $N$, the six forms

$$
L(a,b,d)=(a,b,d,a+b,a+d,a+b+d)
$$

lie in **six pairwise disjoint intervals** inside $[N]$. They support four Schur triples

$$
\{a,b,a+b\},\quad\{a,d,a+d\},\quad
\{b,a+d,a+b+d\},\quad\{d,a+b,a+b+d\}.
$$

All six vertices have degree two. Let $X_N$ count parameter triples for which all six integers are present in the independently retained random subset $[N]_p$.

**Theorem (critical witness Poisson law and supercritical existence).**

1. If $p=cN^{-1/2}$ for a fixed $c>0$, then

   $$
   \boxed{X_N\ \xrightarrow{\ d\ }\mathrm{Poisson}(10^{-6}c^6).}
   $$

   Consequently, the probability that the Schur hypergraph contains a nonempty 2-core has asymptotic lower bound

   $$
   \liminf_{N\to\infty}\Pr(\mathrm{core}_2\ne\varnothing)
   \ge1-\exp(-10^{-6}c^6).
   $$

2. If $pN^{1/2}\to\infty$, then

   $$
   \boxed{\Pr(X_N>0)\to1.}
   $$

   In particular, the nonempty-core event occurs with high probability above the $N^{-1/2}$ scale.

**No lower-threshold implication.** The theorem does not rule out other arithmetic 2-cores at $p=o(N^{-1/2})$. The stated probability is only a lower bound for the full core event.

## Proof

Put $T=I_1(N)\times I_2(N)\times I_3(N)$, so $|T|=(10^{-6}+o(1))N^3$, and let $I_t$ be the indicator that all six distinct labels in $L(t)$ are present. Thus $\mathbb E X_N=|T|p^6\to10^{-6}c^6$ in the critical window.

The six coefficient vectors are

$$
e_1,\ e_2,\ e_3,\ e_1+e_2,\ e_1+e_3,\ e_1+e_2+e_3.
$$

Every two are linearly independent over $\mathbb Q$; any three have rank at least two; **any four have rank three**. These ranks can be checked by a short finite enumeration (see accompanying verifier). The separated numerical ranges imply that two distinct parameter triples can share labels only at *matching positions*: they cannot exchange one form type for another.

For two distinct parameter triples $s,t$ sharing $k$ labels, the $k$ corresponding linear equations $L_i(s)=L_i(t)$ have rank $r$. The number of such ordered pairs is at most $O(N^{6-r})$. Moreover $k\le3$, because $k\ge4$ has rank three and would imply $s=t$. Consequently, the total numbers of ordered distinct parameter pairs sharing respectively one, two and three labels are bounded by

$$
O(N^5),\qquad O(N^4),\qquad O(N^4).
$$

The indicator family is dissociated: $I_s$ and $I_t$ are independent whenever their label sets are disjoint. Standard dependency-graph Poisson approximation (or the factorial-moment method) applies. The two error sums, up to absolute constants, are bounded by

$$
b_1\le O(N^5p^{12}),\qquad
b_2\le O(N^5p^{11}+N^4p^{10}+N^4p^9).
$$

At $p=cN^{-1/2}$ both tend to zero. Since $\mathbb E X_N\to10^{-6}c^6$, the Poisson assertion follows.

For $pN^{1/2}\to\infty$, the covariance calculation gives

$$
\frac{\mathrm{Var}(X_N)}{(\mathbb EX_N)^2}
\le\frac1{\mathbb EX_N}
+O\left(\frac1{Np}+\frac1{N^2p^2}+\frac1{N^2p^3}\right)=o(1).
$$

Chebyshev's inequality implies $\Pr(X_N=0)\to0$. QED.

## Interpretation and scope

This identifies a **rigorously nontrivial probability at the candidate critical scale** and a high-probability upper bound on the threshold for *some* nonempty 2-core. The sharp threshold and the full critical limiting law require control of **all possible arithmetic 2-core configurations**, not only these separated Pasch witnesses.

The proof is a direct application of classical Poisson approximation for dependent substructure indicators to a family of arithmetic linear forms. The mathematical contribution at this stage is the explicit witness and parameter-overlap calculation, not a novel probabilistic approximation theorem.

**Historical sources:** Graham–Rödl–Ruciński (1996), *On Schur Properties of Random Subsets of Integers*, J. Number Theory 61, 388–408, https://doi.org/10.1006/jnth.1996.0155, studies closely related cycle/handle substructures in exactly this Schur hypergraph; its Ramsey property differs from ordinary 2-core appearance. Source comparison at theorem level remains necessary. Classical probabilistic subgraph-count analogues include Stein–Chen dependency graph approximation and Janson–Łuczak–Ruciński, *Random Graphs* (2000).
