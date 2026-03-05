#!/usr/bin/env python3
import sys
import numpy as np
from scipy.integrate import solve_ivp

def solve_first_order_ode(f_str, t_span, y0, method='RK45'):
    # Convert string expression to a lambda function
    # Example: "lambda t, y: -y + t"
    try:
        f = eval(f_str)
    except Exception as e:
        print(f"Error evaluating function string: {e}")
        return

    t_eval = np.linspace(t_span[0], t_span[1], 100)
    sol = solve_ivp(f, t_span, [y0], method=method, t_eval=t_eval)

    if sol.success:
        print(f"Solution successful using {method}")
        print(f"y({t_span[1]}) = {sol.y[0][-1]}")
        # Print a few sample points
        print("\nSample Points (t, y):")
        for i in range(0, len(sol.t), 20):
            print(f"  {sol.t[i]:.2f}, {sol.y[0][i]:.4f}")
    else:
        print(f"Solution failed: {sol.message}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: solve_ode.py '<lambda_f>' '<t_start,t_end>' <y0> [method]")
        print("Example: solve_ode.py 'lambda t, y: -y' '0,5' 1")
        sys.exit(1)

    f_str = sys.argv[1]
    t_span = [float(x) for x in sys.argv[2].split(',')]
    y0 = float(sys.argv[3])
    method = sys.argv[4] if len(sys.argv) > 4 else 'RK45'

    solve_first_order_ode(f_str, t_span, y0, method)
