#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def brownian_motion(T, N, mu, sigma, S0):
    """
    Simulate a one-dimensional Brownian motion path.
    
    Parameters:
    T (float): Time horizon in years.
    N (int): Number of time steps.
    mu (float): Expected return rate.
    sigma (float): Volatility.
    S0 (float): Initial price.
    
    Returns:
    numpy array: Array of prices over time.
    """

    dt = T / N  # Time step size
    increments = np.random.normal(mu * dt, sigma * np.sqrt(dt), N)  # Generate random increments
    increments[0] = 0  # The first increment is zero since we start from the initial price
    prices = np.cumsum(increments) + S0  # Calculate cumulative sum of increments and add initial price
    return prices, increments

# Parameter settings
T = 1  # Time horizon of 1 year
N = 252 * 4  # Assuming 252 trading days in a year
mu = 0.05  # Expected annual return rate of 5%
sigma = 0.2  # Volatility of 20%
S0 = 0  # Initial price of 100

# Generate the Brownian motion path
prices, increments = brownian_motion(T, N, mu, sigma, S0)

import matplotlib.pyplot as plt
fig, ax = plt.subplots(2, 1, sharex=True)

ax[0].plot(prices)
ax[0].set_title('One-Dimensional Brownian Motion')
ax[1].plot(increments)
ax[1].set_title('Increments')
ax[1].set_xlabel('Time Steps')
ax[1].set_ylabel('Price')
ax[0].set_ylabel('Difference of Price')
ax[0].grid(True)
ax[1].grid(True)
plt.show()