import numpy as np
from scipy.interpolate import CubicSpline, make_interp_spline, interp1d
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Perform 1D interpolation using SciPy')
    parser.add_argument('--x', type=float, nargs='+', required=True, help='X coordinates of data points')
    parser.add_argument('--y', type=float, nargs='+', required=True, help='Y coordinates of data points')
    parser.add_argument('--point', type=float, required=True, help='Point to interpolate at')
    parser.add_argument('--method', choices=['cubic', 'bspline', 'linear'], default='cubic', help='Interpolation method')
    
    args = parser.parse_args()
    
    if len(args.x) != len(args.y):
        print("Error: x and y must have the same length")
        sys.exit(1)
        
    x = np.array(args.x)
    y = np.array(args.y)
    
    if args.method == 'cubic':
        cs = CubicSpline(x, y)
        result = cs(args.point)
    elif args.method == 'bspline':
        bspl = make_interp_spline(x, y, k=3)
        result = bspl(args.point)
    elif args.method == 'linear':
        f = interp1d(x, y, kind='linear')
        result = f(args.point)
        
    print(f"Interpolated value at {args.point} using {args.method}: {result}")

if __name__ == "__main__":
    main()
