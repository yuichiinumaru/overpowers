#!/usr/bin/env python3
import numpy as np
from scipy.integrate import solve_ivp
import sys

def solve_numerical(f_str, t_span, y0):
    # f_str should be a lambda-like string, e.g., "lambda t, y: -y"
    try:
        f = eval(f_str)
        sol = solve_ivp(f, t_span, y0, method='RK45')
        return sol
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python numerical_ode.py \"lambda t, y: -y\" \"[0, 5]\" \"[1]\"")
        sys.exit(1)
    
    f_str = sys.argv[1]
    t_span = eval(sys.argv[2])
    y0 = eval(sys.argv[3])
    
    sol = solve_numerical(f_str, t_span, y0)
    if isinstance(sol, str):
        print(sol)
    else:
        print(f"t: {sol.t}")
        print(f"y: {sol.y}")
