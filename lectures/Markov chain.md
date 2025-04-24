# Markov Process

[TOC]

*Keywords* Markov process

## Markov process

State sp. $S$

Markov process/Markov chain:
$P(X_n|X_{n-1},\cdots X_{1})=P(X_n|X_{n-1})$

Homogeneous: $P(X_n|X_{n-1})$ is not related to $n$

### Discrete States

**Definition(Markov process)**

1. $P(X_n=j|X_{n-1}=i)=K_{ij}$ (stochastic matrix/**transition matrix**)
2. $P(X_0=i)=p_i$ (start proba.)

*Fact*

1. $P(X_n=j|X_0=i)=P^{n}_{ij}$
2. $P(X_n=j)=(pP^n)_j$
3. $E(g(X_n)|X_0=i)=(P^{n}g)_i$



### General States

transition kernel:
$K(X=x, A)=P_x(A)$

$K_\epsilon=(1-\epsilon)\sum_i\epsilon^iK^i$

hitting time:

$\tau_A:=\inf\{n\geq 1: X_n\in A\}$

$\tau_A(1):=\tau_A$ and $\tau_A(k)$ is the $k$-th hitting time.

number of passages:

$\eta_A:=\sharp\{X_n\in A\}=\sum_n1_{A}(X_n)$

$E_x\eta_A=\sum_nP_x(X_n\in A)=\sum_nK^n(x,A)$



### Facts

1. $\{\eta_A=\infty\} =\{X_n\in A, i.o.\}$
2. $E_x\eta_A>0\iff \exists n P_x(X_n\in A)=K^n(x,A)>0$,  denoted as $x\to A$
3. $\tau_A<\infty = \bigcup_n(X_n\in A)$; $\tau_A(\omega)<\infty \iff \exists n, X_n(\omega)\in A$
4. $\eta_A\geq k\iff \tau_A(k)<\infty$; $\eta_A= k\iff \tau_A(k)<\infty,\tau_A(k+1)=\infty$
5. $P_x(\tau_A(k)<\infty)=\lim_kP_x^k(\tau_A<\infty)$; $P_x(\eta_A=\infty)=\lim_kP_x^k(\tau_A<\infty)$, $x\in A$
6. $\tau_A<\infty$ a.s. wrt $P_x$ for all $x\in A$  ==>$\eta_A=\infty$  a.s. ...



### Concepts

for discrete cases:

$\eta_i:=\sharp\{x_n=i\}$

- irreducible: for $i,j$ exists $n$, $K^n_{ij}>0$ (connect/communicate $i\to j$)
- recurrent(resp. transient): for $i$, $\sum_n K^n_{ii}=\infty$(resp. $<\infty$) iff $E(\eta_i|x_1=i)=\infty$ iff $P(\eta_i=\infty|x_1=i)=1$

for general cases:

- $\phi$-Irred. for all $A$ that $\phi A>0$, for $x\in A$, $x\to A$ denoted as $A\to A$
- $A$ is recurrent: $E_x\eta_A=\infty$ for all $x\in A$
- $A$ is transient: $\sup_x E_x\eta_A<\infty$ for all $x\in A$
- ($\phi$-)recurrent/transient: ($\exists \phi$) $\phi$-irred.for all $A$, $A$ is recurrent/transient
- $A$ is unif. transient: for all $x\in A$ exists $M$, $E_x\eta_A<M$.
- transient: $S=\cup_i B_i$, $B_i$: unif. transient
- $A$ Harris rec.: $\eta_A=\infty$ a.s. wrt $P_x$ for $x\in A$  (another def. is $\tau_A<\infty$ ...)
- Harris rec.: for all $A$, $A$ Harris rec.

- $\pi$ is invariant (proba.) measure: exists $\pi$, $\pi K=\pi$ and $\pi$ is a (proba.) measure ($\sigma$ finite)
- positive: exists $\pi$, $\pi K=\pi$ and $\pi$ is a proba. measure/distr.
- priodic/apriodic: limiting distr.
- ergodic: pos. recurrent & apriodic iff exists unique invariant distr. $\pi$



Lemma:

1. $m\pi(A)\leq \int E_x\eta_Ad\pi(x),m\in \N$; $E_x\eta_A<\infty\Rightarrow \pi A=0$



*Facts.*

1. irrducible => recurrent xor transient
2. positive => recurrent (pos. recurrent)
3. irreducible => positive iff $E_i\tau_i<\infty$ ($\pi_i=\frac{1}{E_i\tau_i}$ )

**Kac thm**

$\phi$-irred. with an atom $\alpha$,  pos. iff $E_\alpha(\tau_\alpha)<\infty$$\pi(\alpha)=\frac{1}{E_\alpha(\tau_\alpha)}$ 

rec. ==> has a inv. ($\sigma$ finite) measure.

*Remark*

- irred.:  connectivity
- rec.: stab.
- pos. rec.: conv.



### Convergence thm

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

