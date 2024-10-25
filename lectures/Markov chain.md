# Markov Process

[TOC]

*Keywords* Markov process


## Markov process

Markov process:
$P(X_n|X_{n-1},\cdots X_{1})=P(X_n|X_{n+1})$

Homogeneous: $P(X_n|X_{n+1})$ is not related to $n$


### Discrete States

**Definition(Markov process)**
1. $P(X_n=j|X_{n-1}=i)=A_{ij}$ (stochastic matrix/**transition matrix**)
2. $P(X_0=i)=p_i$ (start proba.)

*Fact*
1. $P(X_n=j|X_0=i)=P^{n}_{ij}$
2. $P(X_n=j)=(pP^n)_j$
3. $E(g(X_n)|X_0=i)=(P^{n}g)_i$


