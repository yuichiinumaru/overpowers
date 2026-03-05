import sympy
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Sympy Complex Analysis Helper")
    parser.add_argument("operation", choices=["residue", "limit", "diff", "series"], help="Operation to perform")
    parser.add_argument("expr", help="Mathematical expression")
    parser.add_argument("--var", default="z", help="Variable (default: z)")
    parser.add_argument("--at", help="Point at which to evaluate (for residue, limit, series)")
    parser.add_argument("--order", type=int, default=1, help="Order (for diff or series)")
    
    args = parser.parse_args()
    
    try:
        z = sympy.Symbol(args.var)
        f = sympy.sympify(args.expr)
        at_point = sympy.sympify(args.at) if args.at else 0
        
        if args.operation == "residue":
            result = sympy.residue(f, z, at_point)
            print(f"Residue of {f} at {args.var}={at_point}:")
            print(result)
            
        elif args.operation == "limit":
            result = sympy.limit(f, z, at_point)
            print(f"Limit of {f} as {args.var}->{at_point}:")
            print(result)
            
        elif args.operation == "diff":
            result = sympy.diff(f, z, args.order)
            print(f"{args.order}-th derivative of {f} w.r.t {args.var}:")
            print(result)
            
        elif args.operation == "series":
            result = sympy.series(f, z, at_point, args.order)
            print(f"Series expansion of {f} at {args.var}={at_point} up to order {args.order}:")
            print(result)
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
