#!/usr/bin/env python3
import argparse
from math import pi

try:
    from fluidsim.solvers.ns2d.solver import Simul
except ImportError:
    print("Error: fluidsim not installed. Run 'pip install fluidsim'")
    exit(1)

def main():
    parser = argparse.ArgumentParser(description="Run a 2D Navier-Stokes turbulence simulation with fluidsim.")
    parser.add_argument("--nx", type=int, default=256, help="Grid points in X and Y (default: 256)")
    parser.add_argument("--nu", type=float, default=1e-3, help="Viscosity (default: 1e-3)")
    parser.add_argument("--tend", type=float, default=10.0, help="End time (default: 10.0)")
    args = parser.parse_args()

    print(f"Setting up 2D turbulence simulation: {args.nx}x{args.nx}, nu={args.nu}, tend={args.tend}")

    params = Simul.create_default_params()
    params.oper.nx = params.oper.ny = args.nx
    params.oper.Lx = params.oper.Ly = 2 * pi
    params.nu_2 = args.nu
    params.time_stepping.t_end = args.tend
    params.time_stepping.USE_CFL = True
    params.init_fields.type = "noise"
    params.output.periods_save.phys_fields = max(args.tend / 10, 1.0)
    params.output.periods_save.spectra = max(args.tend / 20, 0.5)

    sim = Simul(params)
    print("Starting simulation...")
    sim.time_stepping.start()
    
    print("Simulation completed.")
    print("To plot results, use: sim.output.phys_fields.plot('vorticity')")

if __name__ == "__main__":
    main()
