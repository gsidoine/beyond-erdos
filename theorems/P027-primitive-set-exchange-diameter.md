# Maximum primitive-set exchange graphs: exact distance and diameter

**Scope:** proved elementary structural theorem (internally checked), with no historical originality or publication claim. The maximum primitive-set family and its counting theory predate this note: [Liu–Pach–Palincza (2021)](https://doi.org/10.1017/S0963548321000018).

## Theorem

Let N=2n≥2, and let M_n consist of primitive subsets A⊂[N] of maximum size n. In the exchange graph G_n, adjacent states differ by replacing one chosen integer with another, while remaining in M_n.

For each odd u≤N, put

$$
C_u=\{2^e u:0\le e\le \lfloor\log_2(N/u)\rfloor\}.
$$

Every A∈M_n meets each C_u in exactly one vertex; write A∩C_u={2^{e_A(u)}u}. Then:

1. A vector of allowable exponents e=(e_u) describes a member of M_n **if and only if**

   $$
   e_u>e_v\quad\text{whenever }u,v\text{ are odd},\ u<v,\ u\mid v.
   $$

2. For any A,B∈M_n the exact graph distance is

   $$
   \boxed{d_{G_n}(A,B)=\#\{u\le N:\ u\text{ odd},\ e_A(u)\ne e_B(u)\}.}
   $$

3. The coordinatewise maximal and minimal feasible exponent assignments are

   $$
   e^{\max}_u=\left\lfloor\log_2\frac{N}{u}\right\rfloor,\qquad
   e^{\min}_u=\left\lfloor\log_3\frac{N}{u}\right\rfloor.
   $$

   Consequently,

   $$
   \boxed{\begin{aligned}
   \mathrm{diam}(G_n)
   &=\#\{u\text{ odd}:u\le N/4\}
   +\#\{u\text{ odd}:N/3<u\le N/2\}\\
   &=\frac{5N}{24}+O(1)=\frac{5n}{12}+O(1).
   \end{aligned}}
   $$

The family of exponent vectors is also closed under coordinatewise minimum and maximum, hence is a finite distributive lattice.

## Proof

The n sets C_u (one per odd integer u≤2n) partition [N] into chains under divisibility. No primitive set may select two from one C_u; because the upper half (n,2n] is primitive and has n elements, maximum primitive sets have size n and meet **every** C_u exactly once.

For distinct odd u,v, the divisibility relation 2^{e_u}u | 2^{e_v}v can hold only if u|v and e_u≤e_v. If u,v are distinct and u|v then automatically u<v. This proves (1).

For (2), each replacement affects a single chain C_u: all other chains must still be occupied, and removing one element then inserting another from a different chain would violate the one-per-chain property. Therefore at least one replacement is necessary for every coordinate on which two states differ.

To attain that bound, first update every coordinate with e_A(u)<e_B(u) to its target value, in **increasing order of odd u**. Increasing e_u cannot break an inequality e_u>e_v where u|v, because it only strengthens that inequality. The only possible obstruction involves a *proper odd divisor* v|u. If v itself is increased, it has been processed and already equals e_B(v)>e_B(u); if it will be decreased, its current value e_A(v) is larger than e_B(v)>e_B(u); and if unchanged, the target configuration is valid. Thus every increase is legal.

Next update each coordinate with e_A(u)>e_B(u), in **decreasing order of odd u**. Decreasing e_u cannot break any inequality e_v>e_u for a proper divisor v|u. For a proper multiple v of u, either its coordinate was increased in the first stage, decreased earlier in this stage, or left unchanged; in each case its current value equals e_B(v), and the target inequality e_B(u)>e_B(v) applies. Every decrease is legal. Each differing coordinate changes once, proving the distance formula.

For (3), put L_u=⌊log_2(N/u)⌋. If u|v with odd v/u≥3 then L_u≥L_v+1, so the coordinatewise upper bound e^{max}=L is itself feasible.

For any feasible vector e, consider the chain of odd multiples u,3u,9u,…,3^k u≤N, of maximal length k=⌊log_3(N/u)⌋. Successive strict inequalities force e_u≥k. The assignment e^{min}_u=k is feasible because any proper odd multiple v/u≥3 yields ⌊log_3(N/u)⌋≥1+⌊log_3(N/v)⌋, and 2^k u≤3^k u≤N. Hence e^{min} is coordinatewise minimal.

The Hamming distance between the bottom and top elements is an upper bound on every pair's distance (since each coordinate lies between the extremes), and is attained by this pair. Therefore the diameter counts the odd u for which

$$
\left\lfloor\log_2(N/u)\right\rfloor>
\left\lfloor\log_3(N/u)\right\rfloor.
$$

For t=N/u≥1, this strict inequality holds **precisely** for 2≤t<3 or t≥4. Indeed it fails on [1,2) and [3,4); for 2≤t<3 it holds; for t≥4, writing k=⌊log_3 t⌋, either k=1 (then log_2 t≥2) or k≥2 (then 3^k≥2^{k+1}, so ⌊log_2 t⌋≥k+1). Thus the odd u that contribute are those with N/3<u≤N/2 or u≤N/4, giving the displayed count. Counting odd integers in intervals yields 5N/24+O(1).

Finally, if e and f satisfy e_u≥e_v+1 and f_u≥f_v+1 for every proper odd divisibility pair u|v, then both pointwise min(e,f) and max(e,f) satisfy the same inequalities. This proves the distributive-lattice assertion. □

## Verification and novelty warning

The [exact graph checker](../experiments/P027_primitive_exchange_diameter.py) enumerates **all** maximum primitive sets on [2n] for n≤10, constructs their one-replacement graph and compares all-pairs shortest paths to Hamming distance and the diameter formula. All checks pass.

This proof is elementary once the classical dyadic-chain representation is used; it may be implicit in the primitive-set or distributive-lattice literature. It is **not** certified as original. The prospective [P027 research question](../problems/number-theory/P027-primitive-set-exchange-mixing.md) concerns the single-chain heat-bath **mixing time**, which is not established by graph connectivity and diameter.
