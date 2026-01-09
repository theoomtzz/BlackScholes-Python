# Black-Scholes Option Pricing

A simple, vectorized Python implementation of the **Black-Scholes model** for pricing European Call and Put options. It includes scripts to visualize how option prices change with spot price and time to maturity.

## 🚀 Features

* **Vectorized:** Uses `NumPy` for fast calculations without loops.
* **Modular:** Separate logic for Call and Put pricing.
* **Visualization:** Includes 2D plots and 3D surfaces using `Matplotlib`.

## 📊 The Formulas

**Call Price:**
$$C = S_t N(d_1) - K e^{-rT} N(d_2)$$

**Put Price:**
$$P = K e^{-rT} N(-d_2) - S_t N(-d_1)$$

Where:
$$d_1 = \frac{\ln(S_t/K) + (r + \frac{\sigma^2}{2})T}{\sigma \sqrt{T}}$$
$$d_2 = d_1 - \sigma \sqrt{T}$$

## 📂 Files

* `call_pricer.py`: Call pricing function.
* `put_pricer.py`: Put pricing function.
* `2Ddrawn.py`: Script for 2D plots (Price vs Spot).
* `3Ddrawn.py`: Script for 3D surfaces (Price vs Spot vs Time).
* `requirements.txt`: List of dependencies.

## 🛠️ Usage

### 1. Installation
```bash
git clone [https://github.com/theoomtzz/BlackScholes-Python.git](https://github.com/theoomtzz/BlackScholes-Python.git)
cd BlackScholes-Python

# Create virtual env
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate
# Activate (Mac/Linux)
source .venv/bin/activate

pip install -r requirements.txt