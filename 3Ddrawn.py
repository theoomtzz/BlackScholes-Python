import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from call_pricer import call_price
from put_pricer import put_price

"""
Black-Scholes 3D Pricing Visualizer
Computes and plots European Call and Put prices surfaces vs Underlying Spot Price and Time to Maturity.
"""

# --- Model Parameters ---
T_max = 3      # Maximum Time to maturity (in years)
K = 65.0         # Strike price
r = 0.10         # Risk-free interest rate (annualized)
sigma = 0.30     # Implied volatility

# --- Grid Generation ---
# Define Spot price range and Time range for sensitivity analysis (Vectorized)
S = np.linspace(20, 120, 50)
T = np.linspace(0.1, T_max, 50)

# Create meshgrid for 3D plotting
S_mat, T_mat = np.meshgrid(S, T)

# --- Pricing ---
# Vectorized calculation for Call and Put premiums using matrices
c = call_price(T_mat, K, S_mat, r, sigma)
p = put_price(T_mat, K, S_mat, r, sigma)

# --- Visualization ---
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1, projection='3d')

# Plotting Call (Viridis cmap) and Put (Magma cmap) surfaces
# Alpha used for transparency to visualize intersection
ax.plot_surface(T_mat, S_mat, c, cmap='viridis', alpha=0.8, edgecolor='none')
ax.plot_surface(T_mat, S_mat, p, cmap='magma', alpha=0.6, edgecolor='none')

# Graph formatting
ax.set_title(rf"Black-Scholes Option Surfaces (K={K}, $\sigma$={sigma})")
ax.set_xlabel("Time to Maturity ($T$)")
ax.set_ylabel("Underlying Spot Price ($S_t$)")
ax.set_zlabel("Option Price")

# Custom legend (required for 3D surfaces)
legend_elements = [
    Line2D([0], [0], color='teal', lw=4, label='Call Option'),
    Line2D([0], [0], color='crimson', lw=4, label='Put Option')
]
ax.legend(handles=legend_elements, loc='upper left')

plt.tight_layout()
plt.show()