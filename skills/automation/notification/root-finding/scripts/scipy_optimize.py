import argparse
import sys
import numpy as np
from scipy.optimize import brentq, newton

def main():
    parser = argparse.ArgumentParser(description="Scipy Root Finding Helper")
    parser.add_argument("method", choices=["brentq", "newton"], help="Root finding method")
    parser.add_argument("expr", help="Function expression in terms of x (e.g., 'x**2 - 2')")
    parser.add_argument("--a", type=float, help="Left bound (for brentq)")
    parser.add_argument("--b", type=float, help="Right bound (for brentq)")
    parser.add_argument("--x0", type=float, help="Initial guess (for newton)")
    parser.add_argument("--fprime", help="Derivative expression (optional for newton)")
    
    args = parser.parse_args()
    
    # Create lambda from expression
    f = eval(f"lambda x: {args.expr}")
    
    try:
        if args.method == "brentq":
            if args.a is None or args.b is None:
                print("Error: brentq requires --a and --b bounds.")
                sys.exit(1)
            root = brentq(f, args.a, args.b)
            print(f"Root found using brentq: {root}")
            
        elif args.method == "newton":
            if args.x0 is None:
                print("Error: newton requires initial guess --x0.")
                sys.exit(1)
            
            df = None
            if args.fprime:
                df = eval(f"lambda x: {args.fprime}")
                
            root = newton(f, args.x0, fprime=df)
            print(f"Root found using newton: {root}")
            
        print(f"Verification: f(root) = {f(root)}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
