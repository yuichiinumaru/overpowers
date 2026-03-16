#!/usr/bin/env python3
"""
Helper script to calculate empirical time complexity of Python functions.
Provides objective measurements for the Research Engineer to critique algorithms.
"""
import time
import numpy as np
import matplotlib.pyplot as plt
import argparse
import sys
from scipy.optimize import curve_fit

def measure_time(func, generator, sizes, trials=3):
    """Measures execution time of func over different input sizes."""
    times = []
    for n in sizes:
        trial_times = []
        for _ in range(trials):
            data = generator(n)
            start = time.perf_counter()
            func(data)
            end = time.perf_counter()
            trial_times.append(end - start)
        times.append(np.median(trial_times))
    return np.array(times)

def fit_complexities(n, t):
    """Fits execution times to common complexity classes."""
    def o_1(x, c): return c * np.ones_like(x)
    def o_n(x, a, b): return a * x + b
    def o_nlogn(x, a, b): return a * x * np.log2(x) + b
    def o_n2(x, a, b): return a * x**2 + b
    def o_n3(x, a, b): return a * x**3 + b

    models = {
        "O(1)": o_1,
        "O(N)": o_n,
        "O(N log N)": o_nlogn,
        "O(N^2)": o_n2,
        "O(N^3)": o_n3
    }

    results = {}
    for name, model in models.items():
        try:
            popt, pcov = curve_fit(model, n, t, maxfev=10000)
            residuals = t - model(n, *popt)
            ss_res = np.sum(residuals**2)
            ss_tot = np.sum((t - np.mean(t))**2)
            r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
            results[name] = r_squared
        except Exception:
            results[name] = -1.0

    best_fit = max(results.items(), key=lambda x: x[1])
    return best_fit, results

if __name__ == "__main__":
    print("Academic Research Engineer - Empirical Complexity Analyzer")
    print("Provides objective data to falsify inefficient implementations.")
    print("Usage: Import this module and use measure_time and fit_complexities.")
