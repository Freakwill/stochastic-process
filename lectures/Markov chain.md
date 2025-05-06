# Markov Chain

[TOC]

*Keywords* Markov Chain, Irred., (null, pos., Harris)Recur., (A)perodic, egordic, inv measure/p.d.

## Markov Chain

State sp. $S$

Markov process/Markov chain:
$P(X_n|X_{n-1},\cdots X_{1})=P(X_n|X_{n-1})$

Homogeneous: $P(X_n|X_{n-1})$ is not related to $n$

### Discrete States

**Definition(Markov process)**

1. $P(X_n=j|X_{n-1}=i)=K_{ij}$ (stochastic matrix/**transition matrix**)
2. $P(X_0=i)=p_i$ (start proba.)



Hitting time and Number of passages:

$\tau_i:=\inf\{n\geq 1: X_n=i\}$

$\eta_i:=\sharp\{X_n=i\}=\sum_n1(X_n=i)$



*Fact.*

1. $P(X_n=j|X_0=i)=P^{n}_{ij}$
2. $P(X_n=j)=(pP^n)_j$
3. $E(g(X_n)|X_0=i)=(P^{n}g)_i$
4. $\{N_i≥k\} = \{T_i(k)<∞\}$
   $\{N_i=k\} = \{T_i(k)<∞,T_i(k+1)=∞\}$
   in finite cases, exists $i,N_i=∞ $
5. condi. mf: $P(N_i=k|X_0=i) = P(T_i<∞|X_0=i)^{k}P(T_i=∞|X_0=i)$
   condi. sf: $P(N_i≥k|X_0=i) = P(T_i<∞|X0=i)^k$

   $E(N_i) = \sum_ip_{ii}(n) = P(T_i<∞|X_0=i)/P(T_i=∞|X_0=i)$
   $E(N_i) = ∞  \iff  N_i=∞$, a.s. $\iff T_i<∞$, a.s.

6. If $j \to i$, then $p_{ii} \gg p_{ij}$ ($p_{ii}(n)\geq p_{ij}(m)$); $p_{ji} \gg p_{jj} \gg p_{ij}$;
    If $i \leftrightarrow j$, then $p_{ii} \sim p_{jj}$

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
2. $E_x\eta_A>0\iff \exists n, P_x(X_n\in A)=K^n(x,A)>0$,  denoted as $x\to A$
3. $\{\tau_A<\infty\} = \bigcup_n(X_n\in A)$; $\tau_A(\omega)<\infty \iff \exists n, X_n(\omega)\in A$
4. $\{\eta_A\geq k\}= \{\tau_A(k)<\infty\}$; $\{\eta_A= k\}=\{\tau_A(k)<\infty,\tau_A(k+1)=\infty\}$
5. $P_x(\tau_A(k)<\infty)=\lim_kP_x^k(\tau_A<\infty)$; $P_x(\eta_A=\infty)=\lim_kP_x^k(\tau_A<\infty)$, $x\in A$
6. $\tau_A<\infty$ a.s. wrt $P_x$ for all $x\in A$  ==> $\eta_A=\infty$  a.s. ...



### Concepts

#### For discrete cases:

- irreducible: for $i,j$ exists $n$, $p_{ij}(n)=K^n_{ij}>0$ (connect/communicate $i\to j$)
- recurrent(resp. transient): for $i$, $\sum_n K^n_{ii}=\infty$(resp. $<\infty$) iff $E_i(\eta_i)=\infty$ iff $\eta_i=\infty$, a.s.
- pos. rec: $m_i=E_im\tau_i<\infty$
- Excursion: $\mathcal{E}_k:X_{\tau_i(k)}=i,X_{\tau_i(k)+1},\cdots, X_{\tau_i(k+1)}=i$

#### For general cases:

- $A$ is Irred.:   for $x\in S$, $x\to A$, denoted as $S\to A$

- $\phi$-Irred.: for all $A$ that $\phi A>0$, for $x\in S$, $x\to A$, i.e. $S\to A$

- $A$ is recurrent: $E_x\eta_A=\infty$ for all $x\in A$

- $A$ is transient: $\sup_x E_x\eta_A<\infty$ for all $x\in A$

- ($\phi$-)recurrent/transient: ($\exists \phi$) $\phi$-irred.for all $A$, $A$ is recurrent/transient

- $A$ is unif. transient: for all $x\in A$ exists $M$, $E_x\eta_A<M$.

- transient: $S=\cup_i B_i$, $B_i$: unif. transient

- $A$ is Harris rec.: $\eta_A=\infty$ a.s. wrt $P_x$ for $x\in A$  (another def. is $\tau_A<\infty$ ...)

- Harris rec.: for all $A$, $A$ Harris rec.

- $\pi$ is invariant (proba.) measure: exists $\pi$, $\pi K=\pi$ and $\pi$ is a (proba.) measure ($\sigma$ finite)

- positive: exists $\pi$, $\pi K=\pi$ and $\pi$ is a proba. measure/distr.

- priodic/apriodic: limiting distr.

- ergodic: pos. recurrent & apriodic iff exists unique invariant distr. $\pi$

- atom $\alpha$ is ergodic:
  $$
  K^n(\alpha,\alpha)\to \pi(\alpha)
  $$
  



#### Facts

Lemma:

1. $n\pi(A)\leq \int E_x\eta_Ad\pi(x),n\in \N$; $E_x\eta_A<\infty\Rightarrow \pi A=0$, where $\pi$ is inv. proba.



*Facts.*

1. irrducible => recurrent xor transient; only one equivalence class.

2. positive => recurrent (pos. recurrent)

3. irreducible => positive iff $m_i:=E_i\tau_i<\infty$ ($\pi_i=\frac{1}{m_i}$ ) for discrete cases

4. irred. & rec. ==> E! unique inv/stationary mea. $\pi$
   $$
   π_j =\begin{cases}
   E \sharp\{X_t=j, 0<t≤\tau_i\},& j\neq i\\
    1,& j=i
   \end{cases}\\
   \sum_j\pi_j = m_i
   $$

**Kac thm**

$\phi$-irred. with an atom $\alpha$,  pos. iff $E_\alpha(\tau_\alpha)<\infty$, $\pi(\alpha)=\frac{1}{E_\alpha(\tau_\alpha)}$ 

rec. ==> has a inv. ($\sigma$ finite) measure.



*Remark*

- Irreducibility: the connectivity between states

- Recurrence: the stability
- Pos. recurrence: the convergence
- (a)priodic/ergodicity: existence of limit

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

1. descrete: positive recurrent aperiodic/ergodic
$$
\|K^n_x-\pi\|_{1} \searrow 0
$$
2. continuous: Harris positive and aperiodic

$$
\|K^n\circ\mu-\pi\|_{TV} \searrow 0
$$



# References



C. P. Robert, G. Casella. Monte Carlo Statistical Methods,2004.

GitHub: https://github.com/Freakwill/stochastic-process

