# Counting permutations with squarefree displacements

**Status:** internally proved asymptotic estimate from classical permanent inequalities. The general method and the squarefree-counting input are standard; historical priority of this particular application is unverified.

Let $M(N)$ be the number of permutations $\sigma$ of $\{1,\ldots,N\}$ such that $|\sigma(i)-i|$ is a positive squarefree integer for every $i$. Put $\delta=6/\pi^2$.

## Theorem

$$
\boxed{\log M(N)=\log(N!)+N\log\delta+O(\sqrt N).}
$$

In particular, $M(N)>0$ for all sufficiently large $N$.

### Proof

Let $A_N$ be the $N\times N$ zero-one matrix with $(A_N)_{ij}=1$ exactly when $|i-j|$ is positive and squarefree. Then $M(N)=\operatorname{per}(A_N)$.

The elementary squarefree-counting estimate is

$$
Q(x)=\sum_{k\le x}\mu^2(k)=\delta x+O(\sqrt x).
$$

It follows by inclusion–exclusion from $\mu^2(k)=\sum_{d^2\mid k}\mu(d)$, using $\sum_{d\ge1}\mu(d)d^{-2}=6/\pi^2$ and the bound $\sum_{d\le\sqrt x}1=O(\sqrt x)$. Therefore each row and column sum of $A_N$ belongs to

$$
[d-\eta,d+\eta],\qquad d=\delta N,\quad\eta=O(\sqrt N).
$$

We claim that for sufficiently large $N$ the bipartite graph of $A_N$ contains a spanning $k$-regular subgraph, with $k=d-O(\sqrt N)$. The standard integral flow criterion asks that for all left-side vertex sets $S$ and right-side vertex sets $T$,

$$
e(S,R\setminus T)\ge k(|S|-|T|)
$$

whenever $s=|S|>t=|T|$.

Set $k=\lfloor d-12\eta\rfloor$; increasing $\eta$ harmlessly makes it positive and the displayed degree interval valid. If $s\le d-\eta$, each left vertex in $S$ has at least $d-\eta-t$ neighbors in $R\setminus T$, so

$$
e(S,R\setminus T)\ge s(d-\eta-t)\ge (d-\eta)(s-t)\ge k(s-t).
$$

The middle inequality follows from $t(d-\eta-s)\ge0$. By symmetry the same argument works if $N-t\le d-\eta$, using the right vertex set $R\setminus T$.

Otherwise $s>d-\eta$ and $N-t>d-\eta$. Since $\delta>3/5$, for large $N$,

$$
s-t>2(d-\eta)-N>\frac N6.
$$

Deleting the edges incident with $L\setminus S$ and those incident with $T$ from the total graph gives

$$
e(S,R\setminus T)\ge
N(d-\eta)-(d+\eta)(N-s+t)
\ge d(s-t)-2N\eta.
$$

As $12\eta(s-t)>2N\eta$, the required flow inequality follows. The integral max-flow/min-cut theorem therefore gives a $k$-factor.

Its adjacency matrix $B\le A_N$ has all row and column sums $k$. By the van der Waerden permanent inequality applied to $B/k$,

$$
\operatorname{per}(A_N)\ge\operatorname{per}(B)
\ge N!\left(\frac{k}{N}\right)^N.
$$

Since $k=\delta N-O(\sqrt N)$, this implies

$$
\log M(N)\ge\log(N!)+N\log\delta-O(\sqrt N).
$$

For the reverse inequality, Brégman's theorem gives

$$
\operatorname{per}(A_N)\le
\prod_{i=1}^N(r_i!)^{1/r_i},
$$

where each row sum is $r_i=\delta N+O(\sqrt N)$. Stirling's formula now yields

$$
\log M(N)\le N(\log(\delta N)-1)+O(\sqrt N+\log N)
=\log(N!)+N\log\delta+O(\sqrt N).
$$

Combining the inequalities proves the theorem. $\square$

## Open question

Determine the optimal order of the remainder

$$
R(N)=\log M(N)-\log(N!)-N\log(6/\pi^2).
$$

The theorem proves $R(N)=O(\sqrt N)$ but does not establish boundedness, logarithmic order, an asymptotic formula, or oscillation. All claims of finer behavior require independent analysis of arithmetic correlations in the squarefree-displacement matrix.

## Exact finite values and source comparison

The [subset-dynamic-programming verifier](../experiments/P044_squarefree_displacement_permanent.py) computes the permanent exactly for small $N$.

The van der Waerden and Brégman–Minc permanent bounds are established results; see [Alon, matchings and subcubes, §2](https://web.math.princeton.edu/~nalon/PDFS/hypcube11.pdf). The related **squarefree-sum** permanent, requiring $i+\sigma(i)$ squarefree, is already [OEIS A398305](https://oeis.org/A398305). The present absolute-difference version is a different Toeplitz host; absence of an exact source in targeted searches does not certify novelty.
