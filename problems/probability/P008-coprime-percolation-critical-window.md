# P008 — The critical window of connectivity in the random coprime graph

**Area:** random graphs, probabilistic number theory, percolation  
**Origin:** discovery pass 3, 2026-10-28  
**Status:** exact critical-window question **open candidate**; leading-order threshold **proved here**, novelty of result unverified

## Model

Let \(C_n\) be the graph on vertices \(1,\ldots,n\) with distinct \(a,b\) adjacent if \(\gcd(a,b)=1\). Form \(C_n(p)\) by retaining each edge of \(C_n\) **independently** with probability \(p\). This is bond percolation on a deterministic arithmetic host graph, not the Erdős–Rényi model \(G(n,p)\).

Let \(\gamma\) denote the Euler–Mascheroni constant.

## Leading-order threshold: theorem

**Theorem (arithmetic connectivity transition; proof below).** For a fixed \(c>0\), put
\[
p_n=c\,\frac{\log n\,\log\log n}{n}.
\]
Then
\[
\Pr(C_n(p_n)\text{ is connected})\longrightarrow
\begin{cases}
0,&c<e^\gamma,\\
1,&c>e^\gamma.
\end{cases}
\]

In fact, for \(c<e^\gamma\), the graph has isolated vertices with high probability; and for \(c>e^\gamma\), it is connected with high probability.

This result is **not presented as a certified new theorem**. Its mathematical argument is supplied so that it can be independently audited and compared with the literature.

### Number-theoretic ingredients

Let \(d_n(v)\) be the degree of \(v\) in \(C_n\). Möbius inversion gives, uniformly for \(v\le n\),
\[
d_n(v)=n\frac{\varphi(v)}{v}+O(2^{\omega(v)}+1),
\]
where \(\omega(v)\) is the number of distinct prime factors of \(v\). Since \(\max_{v\le n}2^{\omega(v)}=n^{o(1)}\) and the classical minimal order of the totient ratio is
\[
\min_{1\le v\le n}\frac{\varphi(v)}{v}
 =\frac{e^{-\gamma}+o(1)}{\log\log n},
\]
we have
\[
\delta(C_n)\ge (e^{-\gamma}-o(1))\frac{n}{\log\log n}.
\]
Mertens' product theorem and the prime number theorem will also be used.

### Proof: subcritical side

Let \(y=\log n/(\log\log n)^2\) and let \(Q=\prod_{q\le y,\;q\ \mathrm{prime}}q\). The prime number theorem gives
\[
Q=\exp((1+o(1))y)=n^{o(1)},
\]
while Mertens' theorem gives
\[
\rho_Q:=\frac{\varphi(Q)}{Q}
 =\prod_{q\le y}(1-1/q)
 =\frac{e^{-\gamma}+o(1)}{\log\log n}.
\]

There are \(m=\lfloor n/Q\rfloor=n^{1-o(1)}\) vertices divisible by \(Q\). Each such \(v\) has
\[
d_n(v)\le\#\{1\le j\le n:\gcd(j,Q)=1\}\le n\rho_Q+Q
\]
by periodicity modulo \(Q\). No two such vertices are adjacent, since their gcd is divisible by \(Q>1\). Therefore their isolated-vertex events in the independently percolated graph involve **disjoint sets of random edges**, and hence are mutually independent.

For any of these vertices,
\[
\Pr(v\text{ isolated})=(1-p_n)^{d_n(v)}
 \ge(1-p_n)^{n\rho_Q+Q}
 =n^{-c e^{-\gamma}+o(1)}.
\]
For \(c<e^\gamma\), the expected number of isolates among these independent events is at least \(n^{1-c e^{-\gamma}-o(1)}\to\infty\). The probability that none is isolated is at most the exponential of minus this quantity, hence tends to zero. The graph is disconnected with high probability.

### Proof: supercritical side

Fix \(c>e^\gamma\), and let \(s_0=\lceil n/\sqrt{\log n}\rceil\). A graph is disconnected iff it has a nonempty vertex subset \(S\), \(|S|=s\le n/2\), with no retained edge crossing \(S\) and \(S^c\).

**Small cuts \(1\le s\le s_0\).** The minimum degree bound implies
\[
e_{C_n}(S,S^c)\ge s(\delta(C_n)-(s-1))
 \ge(e^{-\gamma}-o(1))\,s\,n/\log\log n,
\]
since \(s_0=o(n/\log\log n)\). Thus \(p_n e_{C_n}(S,S^c)\ge(1+\eta)s\log n\) for some fixed \(\eta>0\) and all large \(n\). Union bounding over at most \(n^s\) sets yields probability \(o(1)\) of any such empty cut.

**Large cuts \(s_0\le s\le n/2\).** Let \(H\) be the primes in \((\sqrt n,n]\). The prime number theorem gives \(h=|H|\sim n/\log n\). Every \(v\in[n]\) is coprime to **all but at most one** member of \(H\): no integer at most \(n\) has two distinct prime factors exceeding \(\sqrt n\). If \(|H\cap S^c|\ge h/2\), every vertex in \(S\) has at least \(h/2-1\) neighbors in \(H\cap S^c\); otherwise every vertex in \(S^c\) has at least \(h/2-1\) neighbors in \(H\cap S\). As \(s\le n-s\), either way
\[
e_{C_n}(S,S^c)\ge s(h/2-1)=(1/2-o(1))\,sn/\log n.
\]
For a fixed \(S\), the probability its cut is empty is therefore at most
\[
\exp(-(c/2-o(1))s\log\log n).
\]
Meanwhile
\[
{n\choose s}\le(en/s)^s
 \le\exp(s(1+\tfrac12\log\log n))
\]
because \(s\ge n/\sqrt{\log n}\). Since \(c>e^\gamma>1\), the resulting union bound over large \(s\) tends to zero.

Both ranges are controlled, so the graph is connected with high probability. \(\square\)

## New open candidate: critical window / connectivity vs isolation

For \(0<\lambda<\infty\) define \(p_n(\lambda)\) implicitly by
\[
\mu_n(p_n):=\sum_{v=1}^n(1-p_n)^{d_n(v)}=\lambda.
\]
For all sufficiently large \(n\), such \(p_n(\lambda)\in(0,1)\) exists and is unique. The theorem implies \(p_n(\lambda)\sim e^\gamma\log n\log\log n/n\).

**Question A (Poisson window).** Is the number of isolated vertices of \(C_n(p_n(\lambda))\) asymptotically Poisson with mean \(\lambda\)?

**Question B (connectivity window).** Is
\[
\lim_{n\to\infty}\Pr(C_n(p_n(\lambda))\text{ connected})=e^{-\lambda}?
\]
Equivalently at this scale, is having no isolated vertices asymptotically sufficient for connectivity? A process-level strengthening asks whether the last isolated vertex disappears at the same hitting time as full connectivity, with high probability.

This formulation does **not** call the already-proved leading threshold an open problem.

## Finite simulation

[\`experiments/coprime_percolation.py\`](../../experiments/coprime_percolation.py) samples the model by generating potential Erdős–Rényi edges via geometric waiting times and retaining only those with \(\gcd=1\). Fixed-seed runs at \(n=1000,3000,10000\) and \(c=1.0,1.4,1.78,2.2\) show the predicted movement from disconnected to connected. These moderate sizes **cannot** confirm the asymptotic constant.

## Related research and novelty caveat

Xiang Qi, *Random Meta-Structure* (2026 preprint, DOI 10.5281/zenodo.21737868) explicitly considers Bernoulli thinning of the coprime graph, but its coprime example discusses a heuristic **giant-component** scale, not the critical connectivity window proposed here. More general literature studies percolation on fixed dense graphs and inhomogeneous random graphs. The exact asymptotic connectivity theorem above is **not certified novel** and must be compared with general results before publication. See the dated literature audit.
