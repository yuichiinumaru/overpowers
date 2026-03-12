import sys

def solve(assertion):
    print(f"Proving: {assertion}")
    print("Error: Z3 not installed in this environment. Please run via uv if available.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python z3_solve.py <assertion>")
        sys.exit(1)
    solve(sys.argv[1])
