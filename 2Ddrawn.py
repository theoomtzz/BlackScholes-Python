import numpy as np
import matplotlib.pyplot as plt
from call_pricer import call_price
from put_pricer import put_price

"""
Black-Scholes Option Pricing Visualizer
Computes and plots European Call and Put prices vs Underlying Spot Price.
"""

# --- Model Parameters ---
T = 1.0          # Time to maturity (in years)
K = 65.0         # Strike price
r = 0.10         # Risk-free interest rate (annualized)
sigma = 0.30     # Implied volatility

# --- Grid Generation ---
# Define Spot price range for sensitivity analysis (Vectorized)
S = np.linspace(20, 80, 100) 

# --- Pricing ---
# Vectorized calculation for Call and Put premiums
c = call_price(T, K, S, r, sigma)
p = put_price(T, K, S, r, sigma)

# --- Visualization ---
plt.figure(figsize=(10, 6))

# Plotting Call (Blue) and Put (Red) profiles
plt.plot(S, c, color='blue', label='Call Option', linewidth=1.5)
plt.plot(S, p, color='red', label='Put Option', linewidth=1.5)

# Graph formatting
plt.axvline(x=K, color='black', linestyle='--', alpha=0.6, label='Strike (K)')
plt.title(rf"Black-Scholes Option Prices (K={K}, T={T} (Years), $\sigma$={sigma})")
plt.xlabel("Underlying Spot Price ($S_t$)")
plt.ylabel("Option Price")
plt.legend(loc='best')
plt.grid(True, linestyle=':', alpha=0.7)

plt.show()