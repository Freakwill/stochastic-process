# Markov Process

[TOC]

*Keywords* Markov process


## Markov process

Markov process/Markov chain:
$P(X_n|X_{n-1},\cdots X_{1})=P(X_n|X_{n-1})$

Homogeneous: $P(X_n|X_{n-1})$ is not related to $n$

### Discrete States

**Definition(Markov process)**

1. $P(X_n=j|X_{n-1}=i)=A_{ij}$ (stochastic matrix/**transition matrix**)
2. $P(X_0=i)=p_i$ (start proba.)

*Fact*

1. $P(X_n=j|X_0=i)=P^{n}_{ij}$
2. $P(X_n=j)=(pP^n)_j$
3. $E(g(X_n)|X_0=i)=(P^{n}g)_i$

transition kernel:
$K(X=x, A)=P_x(A)$

transition matrix: $K_{ij}$

### Concepts

only for discrete cases!

- irreducible: for $i,j$ exists $n$, $K^n_{ij}>0$ (connect/communicate $i\to j$)
- recurrent(resp. transient): for $i$, $\sum_n K^n_{ii}=\infty$(resp. $<\infty$) iff $E(\sharp\{x_n=i\}|x_1=i)=\infty$ iff $P(\eta_i=\sharp\{x_n=i\}=\infty|x_1=i)=1$
- positive: exists $\pi K=\pi$
- priodic/apriodic: limiting distr.
- ergodic(non-null rec. & apriodic): exists unique $\pi$

*Facts.*
1. irrducible => recurrent xor transient
2. positive => recurrent
3. irrducible => positive iff $E_i\tau_i<\infty$ ($\pi_i=\frac{1}{E_i\tau_i}$ )

### invariant distr.
*Definition*
distr.: $X_{n+1}| X_n$
transition kenerl: $K$

**Detail balance condition**: $K(y,x)f(x)=K(x,y)f(y)$

*Theorem*
$X_n$: $K$-chain, satisfies DBC with PDF $\pi$ ==>
1. $\pi$ is inv. density of $X_n$ ($\pi K=\pi$)
2. $X_n$: reversible

*Fact*
$X_n$: $K$-chain, with inv. density $\pi$ ==>
$$
\|K^n\circ \mu-\pi\|_{TV} \searrow 
$$

*Theorem*
$X_n$: $K$-chain, with inv. density $\pi$ ==>
1. descrete: positive recurrent aperiodic
$$
\|K^n_x-\pi\|_{1} \searrow 0
$$
2. continuous: Harris positive and aperiodic

$$
\|K^n\circ\mu-\pi\|_{TV} \searrow 0
$$



GitHub: https://github.com/Freakwill/stochastic-process

