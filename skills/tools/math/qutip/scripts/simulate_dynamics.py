import argparse
import numpy as np
import matplotlib.pyplot as plt
from qutip import *

def simulate_damped_oscillator(N=20, omega=1.0, kappa=0.1, t_max=50, steps=200):
    H = omega * num(N)
    c_ops = [np.sqrt(kappa) * destroy(N)]
    psi0 = coherent(N, 2.0)
    tlist = np.linspace(0, t_max, steps)
    result = mesolve(H, psi0, tlist, c_ops, e_ops=[num(N)])
    return tlist, result.expect[0]

def main():
    parser = argparse.ArgumentParser(description='Simulate quantum dynamics using QuTiP.')
    parser.add_argument('--oscillator', action='store_true', help='Simulate a damped harmonic oscillator')
    parser.add_argument('--N', type=int, default=20, help='Hilbert space dimension')
    parser.add_argument('--omega', type=float, default=1.0, help='Frequency')
    parser.add_argument('--kappa', type=float, default=0.1, help='Decay rate')
    parser.add_argument('--output', help='Save plot to file')

    args = parser.parse_args()

    if args.oscillator:
        print(f"Simulating damped oscillator (N={args.N}, omega={args.omega}, kappa={args.kappa})...")
        tlist, expect = simulate_damped_oscillator(args.N, args.omega, args.kappa)
        
        plt.plot(tlist, expect)
        plt.xlabel('Time')
        plt.ylabel('⟨n⟩')
        plt.title('Photon Number Decay')
        
        if args.output:
            plt.savefig(args.output)
            print(f"Plot saved to {args.output}")
        else:
            plt.show()
    else:
        print("Use --oscillator for a demo simulation.")

if __name__ == "__main__":
    main()
