# MCMC

## Popopulation MC

Idea: proposal distr. $q_{it}$ id different at each iteration and for each particle with this alogrithm.

*Algo.*
Return $z_i^{t}\sim \pi$

For $t$
1. For $i$
  - Select $q_{it}$
  - $\tilde{z}_i{(t)}\sim q_{it}$
  - $\rho_{i}^{(t)}\sim \frac{\pi(z_i^{(t)})}{q_{it}(\tilde{z}_i^{(t)})}$
2. Resample: draw $z_i^{t}$ from $\tilde{z}_i^{t}$, using $\rho_{i}^{(t)}$.

If $\pi$ is unscaled, then use biased form.

Integral:
$I_t=\frac{1}{n}\sum_i\rho_{i}^{(t)}h(z_{i}^{(t)})\approx E_{X\sim \pi}h(X)$


