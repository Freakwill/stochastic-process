# Introduction of Martingale

[TOC]

*Keywords* Martingale


## Martingale


### Concepts

**Definition(Martingale)**
$M_t$ is martingale (wrt $\mathsrc{F}_t$):
1. boundedness: $E|M_t|<\infty$
2. indep. $E(M_t|\mathsrc{F}_s)=M_s, s<t$


*Supplement* submaringale: $E(M_t|\mathsrc{F}_s)\leq M_s$, supermaringale: $E(M_t|\mathsrc{F}_s)\geq M_s$


*Example*

1. Brown motion $W_t$ and $W_t^2-t, e^{aW_t-a^2t/2}$ is mart.
2. $E(X|\mathsrc{F}_t)$ is mart.


*Reference*

- D. Revuz, M, Yor, Continous Martingales and Brownian Motion, 1999
- Richard L. Bass. Stochastic Process.

