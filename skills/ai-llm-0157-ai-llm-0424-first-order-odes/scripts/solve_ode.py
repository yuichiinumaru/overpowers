import sympy as sp
import sys

def solve_symbolic(equation_str, ics=None):
    x = sp.symbols('x')
    y = sp.Function('y')(x)
    
    # Simple parser for basic ODEs like "y' + y = x"
    # Note: This is very basic, real sympy_compute.py would be better
    # But for a helper script, we can use sp.sympify or similar
    
    # Expecting something like "Derivative(y, x) + y - x"
    try:
        expr = sp.sympify(equation_str)
        solution = sp.dsolve(expr, y, ics=ics)
        return solution
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python solve_ode.py \"Derivative(y, x) + y - x\"")
        sys.exit(1)
    
    eq = sys.argv[1]
    print(solve_symbolic(eq))
