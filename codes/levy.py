#!/usr/bin/env python3

import numpy as np


def levy_process_simulation(T, num_steps, lambda_, mu, sigma):
    """
    Simulation of Lévy process

    参数:
    T (float): 总时间跨度
    num_steps (int): 时间步数，即将总时间划分成多少个小的时间间隔
    lambda_ (float): 泊松过程的强度参数，表示单位时间内事件发生的平均次数
    mu (float): 跳跃幅度的均值（对于复合泊松过程中的跳跃部分）
    sigma (float): 跳跃幅度的标准差（对于复合泊松过程中的跳跃部分）

    返回:
    times (numpy.ndarray): 时间点数组
    process_values (numpy.ndarray): Lévy过程在对应时间点的值的数组
    """
    dt = T / num_steps  # 每个时间步长的大小
    times = np.linspace(0, T, num_steps + 1)  # 生成时间点数组

    # 初始化Lévy过程的值数组，初始值设为0
    process_values = np.zeros(num_steps + 1)
    for i in range(1, num_steps + 1):
        # 先计算泊松过程部分，看是否有跳跃事件发生
        num_jumps = np.random.poisson(lambda_ * dt)
        if num_jumps > 0:
            # 如果有跳跃事件，生成相应的跳跃幅度（服从正态分布）并累加到过程值上
            jump_sizes = np.random.normal(mu, sigma, num_jumps)
            process_values[i] = process_values[i - 1] + np.sum(jump_sizes)
        else:
            # 如果没有跳跃事件，过程值保持不变
            process_values[i] = process_values[i - 1]

    return times, process_values


# 设置模拟参数
T = 10.0  # 总时间跨度，例如10个单位时间
num_steps = 1000  # 划分的时间步数
lambda_ = 0.5  # 泊松过程强度参数
mu = 0.  # 跳跃幅度均值
sigma = 1.  # 跳跃幅度标准差

times, process_values = levy_process_simulation(T, num_steps, lambda_, mu, sigma)


import matplotlib.pyplot as plt
plt.plot(times, process_values)
plt.xlabel('Time')
plt.ylabel('Lévy Process Value')
plt.title('Simulation of a Lévy Process (Compound Poisson Process)')
plt.show()