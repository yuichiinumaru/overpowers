import argparse
from qutip import *

def main():
    parser = argparse.ArgumentParser(description='Analyze quantum systems using QuTiP.')
    parser.add_argument('--steady-state', action='store_true', help='Find steady state of a system')
    parser.add_argument('--N', type=int, default=10, help='Fock space dimension')
    parser.add_argument('--kappa', type=float, default=0.1, help='Cavity decay rate')
    parser.add_argument('--n-thermal', type=float, default=0.01, help='Thermal excitation')

    args = parser.parse_args()

    if args.steady_state:
        print(f"Finding steady state for driven-dissipative cavity (N={args.N})...")
        a = destroy(args.N)
        H = a.dag() * a # Simple number Hamiltonian
        # Lindblad operators for relaxation and thermal excitation
        c_ops = [
            (args.kappa * (1 + args.n_thermal))**0.5 * a,
            (args.kappa * args.n_thermal)**0.5 * a.dag()
        ]
        
        rho_ss = steadystate(H, c_ops)
        print("\nSteady State Density Matrix:")
        print(rho_ss)
        print(f"\nAverage occupation: {expect(a.dag()*a, rho_ss):.4f}")
        print(f"Von Neumann entropy: {entropy_vn(rho_ss):.4f}")
    else:
        print("Use --steady-state for a demo analysis.")

if __name__ == "__main__":
    main()
