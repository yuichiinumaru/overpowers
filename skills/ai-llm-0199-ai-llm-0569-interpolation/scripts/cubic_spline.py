#!/usr/bin/env python3
from scipy.interpolate import CubicSpline
import numpy as np
import sys

def run_interpolation():
    # Example data points
    x = np.array([0, 1, 2, 3])
    y = np.array([0, 1, 4, 9])
    
    cs = CubicSpline(x, y)
    
    # Query point
    query_x = 1.5
    if len(sys.argv) > 1:
        try:
            query_x = float(sys.argv[1])
        except ValueError:
            pass
            
    print(f"Interpolating at x={query_x}")
    print(f"Result: {cs(query_x)}")

if __name__ == "__main__":
    run_interpolation()
