import numpy as np
from scipy.stats import norm

def put_price(T, K, S, r, sigma):
    """
    Computes the Black-Scholes price for a European Put option.
    
    Parameters:
    -----------
    T     : Time to maturity in years (float)
    K     : Strike price (float)
    S     : Spot price of the underlying (float or numpy array)
    r     : Risk-free interest rate (decimal, e.g., 0.05 for 5%)
    sigma : Volatility of the underlying (decimal, e.g., 0.20 for 20%)
    
    Returns:
    --------
    put   : Put option price (float or numpy array)
    """
    
    # Pre-compute volatility term (Sigma * sqrt(T))
    # Optimization: avoids calculating sqrt(T) multiple times
    vol_sqrt_t = sigma * np.sqrt(T)

    # d1 and d2 calculation
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2 * T)) / vol_sqrt_t
    d2 = d1 - vol_sqrt_t

    # Cumulative distribution functions
    # For Puts, we use N(-d1) and N(-d2)
    N1, N2 = norm.cdf([-d1, -d2])

    # Black-Scholes Put Formula
    # P = K * e^(-rT) * N(-d2) - S * N(-d1)
    put = K * np.exp(-r * T) * N2 - S * N1
    
    return put