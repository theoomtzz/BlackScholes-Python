import numpy as np
from scipy.stats import norm

def call_price(T, K, S, r, sigma):
    """
    Computes the Black-Scholes price for a European Call option.
    
    Parameters:
    -----------
    T     : Time to maturity in years (float)
    K     : Strike price (float)
    S     : Spot price of the underlying (float or numpy array)
    r     : Risk-free interest rate (decimal, e.g., 0.05 for 5%)
    sigma : Volatility of the underlying (decimal, e.g., 0.20 for 20%)
    
    Returns:
    --------
    price : Call option price (float or numpy array)
    """
    
    # Pre-compute volatility term to optimize performance
    # Denominator in d1 and subtraction term for d2
    vol_sqrt_t = sigma * np.sqrt(T)

    # d1 and d2 calculation
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2 * T)) / vol_sqrt_t
    d2 = d1 - vol_sqrt_t

    # Cumulative distribution functions
    # Using vectorized input for norm.cdf is more efficient than individual calls
    N1, N2 = norm.cdf([d1, d2])

    # Black-Scholes formula
    call = S * N1 - K * np.exp(-r * T) * N2
    
    return call