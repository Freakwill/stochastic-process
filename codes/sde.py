"""Numerical SDE

Euler-Maruyama method
Milstein method
"""

import numpy as np


# 漂移项系数函数 mu
def mu(x, t):
    return 0.75 * x

# 扩散项系数函数 sigma
def sigma(x, t):
    return 0.3 * x


def dsigma_dx(x, t):
    return 0.3


# 时间步长
dt = 1/250
# 总时间
T = 1.0
# 初始值
x0 = 1.0


def euler_maruyama_method():
    # Euler Maruyama scheme
    num_steps = int(T / dt)
    t = np.linspace(0, T, num_steps + 1)
    x = np.zeros(num_steps + 1)
    x[0] = x0
    dW = np.sqrt(dt) * np.random.randn(num_steps)
    for i in range(num_steps):
        x[i + 1] = x[i] + mu(x[i], t[i]) * dt + sigma(x[i], t[i]) * dW[i]
    return t, x


def milstein_method():
    num_steps = int(T / dt)
    t = np.linspace(0, T, num_steps + 1)
    x = np.zeros(num_steps + 1)
    x[0] = x0
    dW = np.sqrt(dt) * np.random.randn(num_steps)
    for i in range(num_steps):
        # 米尔斯坦方法的迭代公式
        x[i + 1] = (x[i] + mu(x[i], t[i]) * dt + sigma(x[i], t[i]) * dW[i]
            + 0.5 * sigma(x[i], t[i]) * dsigma_dx(x[i], t[i]) * (dW[i] ** 2 - dt))
    return t, x



import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)

for _ in range(8):
    t, x = euler_maruyama_method()
    ax.plot(t, x)

ax.set_xlabel('Time')
ax.set_ylabel('Solution')
ax.set_title('Milstein Scheme for SDE')
plt.show()
