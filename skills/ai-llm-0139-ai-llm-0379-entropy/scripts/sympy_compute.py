import sys

def compute(expression, action="simplify"):
    print(f"Entropy Calculation: {action} {expression}")
    print("Error: Sympy not installed in this environment. Please run via uv if available.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sympy_compute.py <expression> [action]")
        sys.exit(1)
    compute(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "simplify")
