
import numpy as np
def exponential_growth(P0, r, t):
    """Population growth without resource constraints."""
    return P0 * np.exp(r * np.asarray(t, dtype=float))

def logistic_growth(P0, r, K, t):
    """Population growth with a carrying capacity."""
    if P0 <= 0 or K <= 0 or P0 > K or r < 0:
        raise ValueError("Require 0 < P0 <= K and r >= 0.")
    t = np.asarray(t, dtype=float)
    A = (K - P0) / P0
    return K / (1 + A * np.exp(-r * t))
