import argparse
import matplotlib.pyplot as plt
from qutip import *
import numpy as np

def plot_bloch(states=None):
    b = Bloch()
    if states:
        for s in states:
            b.add_states(s)
    b.show()

def plot_wigner(psi, x_range=5, res=200):
    xvec = np.linspace(-x_range, x_range, res)
    W = wigner(psi, xvec, xvec)
    plt.contourf(xvec, xvec, W, 100, cmap='RdBu')
    plt.colorbar()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Visualize quantum states using QuTiP.')
    parser.add_argument('--bloch', action='store_true', help='Show Bloch sphere')
    parser.add_argument('--wigner', action='store_true', help='Plot Wigner function')
    parser.add_argument('--N', type=int, default=20, help='Fock space dimension')
    parser.add_argument('--alpha', type=complex, default=2.0, help='Coherent state parameter')

    args = parser.parse_args()

    if args.bloch:
        print("Displaying Bloch sphere...")
        # Example: superposition state
        psi = (basis(2, 0) + basis(2, 1)).unit()
        plot_bloch([psi])
    elif args.wigner:
        print(f"Plotting Wigner function for coherent state alpha={args.alpha}...")
        psi = coherent(args.N, args.alpha)
        plot_wigner(psi)
    else:
        print("Use --bloch or --wigner to visualize states.")

if __name__ == "__main__":
    main()
