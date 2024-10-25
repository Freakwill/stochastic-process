# Introduction of Stochastic Process

[TOC]

*Keywords* Stochastic process


## Stochastic process

**Stochastic process**: seq. of rvs $\{X_t\}$ on event/sample sp. $(\Omega,\mathscr{A})$

### Definition/Concepts

**Definition(Stochastic process)**

1. $(\Omega,\mathscr{A}_t)$: measurable sp.（seq of $\sigma$-algebra on X）
2. Stochastic process: seq. of measurable mapping/rv $X_t: (\Omega,\mathscr{A}_t)\to Y$
3. $t\in T$:po-set, $\mathscr{A}_t$: nondecreasing (*filtration*)

$t\mapsto X_t(\omega)$: *trajectory/path* on $Y$ (path-valued measurable mapping/rv)

Denoted as $X_t \sim \mathscr{A}_t$

Distribution: family of joint distr. $P(X_{t_1},\cdots,X_{t_m}\in A\subset\mathbb{R}^m)$, or $F(X_{t_1},\cdots,X_{t_m})$

*Joint Measurable*: $(t,\omega)\mapsto X_t(\omega)$ is measurable in the product sp. 

*Example*
discrete time series $X_n, n=1,2,\cdots$, continuous time series $X_t, t\in[0,\infty)$
($T=\mathcal{Z}$ or $[0,\infty)$ by default)

*Special case*
Stochastic process: seq. of $X_t: (X,\mathscr{A}_t)\to Y$, $\mathscr{A}_t=\mathscr{A}$

`Past` of $X_t$ related to `Present` $s$: $\mathscr{F}_s^0 := \sigma(X_t, t\leq s)$;
`Future` of $X_t$ related to `Present` $s$: $\mathscr{F}_s^1 := \sigma(X_t, t\geq s)$

*Trivial case*
$X_t$: iid

*Special case*
Stochastic process: seq. of events $A_t \sim \mathscr{A}_t$, i.e. $X_t=1_{A_t}: A_t\in \mathscr{A}_t$

**Definition**

- Stop time: $T \leq t \sim \mathscr{A}_t$
- Optional time: $T < t \sim \mathscr{A}_t$

**Definition**

- $P(X_t=Y_t)=1$: $X_t=Y_t$ a.s. $\omega$ for $t\in T$
- $X_t\sim Y_t$: $P(X_{t_1},\cdots,X_{t_m})=P(Y_{t_1},\cdots,Y_{t_m})$ for $t\in T$
- $P(X_t=Y_t, t\in T)=1$ (a.s.)

*Remark* Stoch measure sp. $(X,\mathscr{A},\mu_n)$。Generalizaion: $A \to f \to \mu$, set -> function -> measure

### Modification

*Continuous Stoch.P.*
$t\mapsto X_t(\omega)$: continous a.s.

Continous modification

Progressively measurable modification

*Fact*
1. Stoch.p. $X\sim \mathscr{F}_t$ is measurable iff it has Progressively measurable modification


### Markov Chain

*Markov Chain*
$P(A\cap B| X_t) = P(A|X_t) P(B|X_t), A\in \mathsrc{F}_t^0, B\in \mathsrc{F}_t^1$
i.e. $P(B| X_t,A) = P(B|X_t)$
==> $P(X_s|X_t, X_{t\leq s})=P(X_s|X_t), s> t$

> The past is independent of the future relative to the present

**Definiton** Brown Motion



*Reference*

- Kai Lai Chuang, J. B. Wash, Markov Process, Brownian Motion and Time Symmetry, 2004.
- D. Revuz, M, Yor, Continous Martingales and Brownian Motion, 1999
- I. Karatzas and S. E. Shreve, Brownian Motion and Stochastic Calculus, 1998
- Richard L. Bass. Stochastic Process.

