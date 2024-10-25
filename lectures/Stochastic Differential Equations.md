# Stochastic DE

*Abrev.*
- SDE: stochastic diff. eq.
- SI(E): stocahstic integral (eqations)
- rv: random varable

## Introduction
But SDE:
$$
d X_t = \mu_t(X_t)d t+\sigma_t(X_t)d B_t
$$
where the first term of the rhs is **drift**, the second term is **diffusion**.

For the odd property of Brown motion, we can not define directly $\omega \mapsto \frac{\mathrm{d} B(t,\omega)}{\mathrm{d} t}$. SDE dose not have the strict meaning of analysis. It should be understood as the following SIE:
$$
X_t = X_0 + \int_0^t \mu_t(X_t)dt+ \int_0^t \sigma_t(X_t)dB_t
$$
where the integral of drift is Lebesgue-integral on interval (random-valued), and the integral of diffusion is SI, should not be regarded as an rv,
$$
\omega \mapsto \int_0^t \sigma_t(X_t(\omega))dB_t(\omega)
$$
and $dB_t(\omega)$ is not a "random measure".

## Ito integral
The integral is restained to $[0,1]$ for convenience.

**Definition(OIP)**
SP $\{Z(t)\in L^2,t\in [0,1]\}$:**OIP** with zero mean and finite var, If
$$
E((Z(t_4)-Z(t_3))\overline{(Z(t_2)-Z(t_1))})=0, 0\leq t_1<t_2\leq t_3<t_4\leq 1,
$$
and $Z(t)$ is cad, i.e. $E|Z(t+h)-Z(t)|^2\to 0,h\to0+$.


1. Consider $f=\chi_{(t,s]}$ (note the compatibility with addition)
$$
I(f):=\int_0^1f(\nu)\mathrm{d} Z(\nu)=Z_s-Z_t.
$$
2. define $I$ on simple function.
3. Continous extension $I:L^2[0,1]\to L^2$, based on distr. $F(t)=E|Z(t)-Z(0)|^2$. 
$$
\|I(f)\|_2=\|f\|_2.
$$

Brown motion is OIP. Leads to Wiener integral.

1. Consider constant-valued process
$$
\chi_{(a,b]}(t)X,0\leq a<b\leq 1
$$
and 
$$
I = \int_0^1S(t)\mathrm{d} Z(t)=X(Z(b)-Z(a))
$$
2. For simple SP:
$$
S(t)=\sum_{i=0}^{n-1}\chi_{(t_i,t_{i+1}]}(t)X_i,X_0=0,0=t_0<t_1<\cdots<t_n=1
$$
==>
$$
\int_0^1 S(t)\mathrm{d} Z(t)=\sum_iX_i(Z(t_{i+1})-Z(t_i))
$$
3. $X(t)$ as function $X: [0,1]\times \Omega\to \R$ is measurable, and
$$
\|X(t)\|_2=\int_0^1E|X(t)|^2\mathrm{d} t<\infty
$$
and adapt filtration $\mathscr{F}_t$ that is a martingale with $Z(t)$. such functional sp $\mathcal{V}\subset L^2([0,1]\times \Omega)$ is Hilbert sp. and subsp. of simple processes is dense in $\mathcal{V}$. When $\{t_i\}$ is refine enough, the simple processes
$$
S_n(t)=\sum_{i=0}^{n-1}X(t_i)\chi_{(t_i,t_{i+1}]}(t)\to X(t)\in \mathcal{V},
$$
==> $I(S_n(t))\to \int_0^1X(t)\mathrm{d} Z(t)$.

**Ito isometric theorem**
If $S(t)$ is simple, then
$$
E(\int_0^1S(t)\mathrm{d} Z(t))^2=\|S(t)\|^2,
$$
then it holds for all $X\in\mathcal{V}$ for density of simple processes. (Ito integral op. $I$ has continuous extenstion!)

*Proof.*
With the knowledge of martingale, to verify the density of simple processes.


 ### Ito formula

**Theorem(Ito formula)**
If $dX_t =\mu_tdt+\sigma_tdW_t$, then
$$
df(t,X_t)=\mu_t'dt+\sigma_t'dW_t\\
\mu_t'=\partial_t f+\partial_x f(t,X_t) \mu_t + \frac{1}{2}\partial_{xx} f(t,X_t)\sigma_t^2\\
\sigma_t'=\partial_x f(t,X_t)\sigma_t
$$
and
$$
(Ef(t,X_t))'=E\mu_t'=\partial_t Ef+E\partial_x f(t,X_t) \mu_t + \frac{1}{2}E\partial_{xx} f(t,X_t)\sigma_t^2
$$

*Corollary.* $df(X_t) = f'(X_t)dt+f''(X_t)(dX_t)^2$

*Corollary.* If $f(t, X_t)=\log p_t(X_t)$, then
$$
(H_t(X_t))'=E\partial_x f(t,X_t) \mu_t + \frac{1}{2}E\partial_{xx} f(t,X_t)\sigma_t^2
$$

**Theorem(Ito formula for high-dim)**
If $d$-dim process $dX_t =\mu_tdt+\sigma_tdW_t,\mu_t\in\R^d,\sigma_t\in\R^{d\times p}, W_t\in\R^p$(sample sp.), then
$$
f(t,X_t)=\mu_t'dt+\sigma_t'dW_t\\
\mu_t'=\partial_t f+\nabla_x f(t,X_t) \cdot \mu_t + \frac{1}{2} \langle H f(t,X_t),\sigma_t \sigma_t^T\rangle_F\\
\sigma_t'=(\nabla_x f(t,X_t))^T\sigma_t
$$

## Fokker-Planck Equation
SDE:
$$
d X_t = \mu_t(X_t)dt+ \sigma_t(X_t)dB_t
$$

Note *diffusion matrix* $A_t:    =\sigma_t\sigma^T_t$

*Fact.* transition prob. density from $X_s=y$ to $X_t$:
$$
p(x,t)=p_{st}(x|y),s\leq t
$$
is the solution to PDE
$$
\partial_t p(x,t) = L^* p, t>s\\
p(x,s)=\delta_{xy}
$$
where $L^*f:=-\mathrm{div}_x \mu_t(x) f(x)+\frac{1}{2}\sum_{ij}\partial_{x_i,x_j} A_t(x)f(x)$, adj. of $Lf:=\mu_t\cdot\nabla f+\frac{1}{2}H(f)\cdot_F A_t$

*Proof.* Use Ito formula for $f(X_t)$ and the fact of duality $(Lf,g)=(f,L^*g)$, so PDE: $(f, L^*p)=ELf= \partial_tEf$

---
*exercise*

1. compute $f(t,X_t)=e^{-\theta t} X_t$, given $X_t \sim I.P.(\mu_t,\sigma_t)$.

2. compute $f(t,X_t)=\phi(X_t)$,

*References*
Richard F. Bass. Stochastic Processes. Cambridge University Press, 2011.