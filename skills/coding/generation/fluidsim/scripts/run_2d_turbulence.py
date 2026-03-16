#!/usr/bin/env python3
"""
Basic 2D turbulence simulation script using fluidsim.
"""
from math import pi
import argparse

try:
    from fluidsim.solvers.ns2d.solver import Simul
except ImportError:
    print("Error: fluidsim not installed. Install with 'uv pip install fluidsim'")
    exit(1)

def run_simulation(nx, ny, nu, t_end):
    params = Simul.create_default_params()
    params.oper.nx = nx
    params.oper.ny = ny
    params.oper.Lx = 2 * pi
    params.oper.Ly = 2 * pi

    params.nu_2 = nu
    params.time_stepping.t_end = t_end
    params.time_stepping.USE_CFL = True

    params.init_fields.type = "noise"
    params.output.periods_save.phys_fields = t_end / 10.0
    params.output.periods_save.spectra = t_end / 20.0

    print(f"Starting simulation: {nx}x{ny}, nu={nu}, t_end={t_end}")
    sim = Simul(params)
    sim.time_stepping.start()

    print(f"Simulation completed. Output saved to: {sim.output.path_run}")
    return sim.output.path_run

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run 2D Navier-Stokes turbulence simulation")
    parser.add_argument("--nx", type=int, default=256, help="Grid points in X")
    parser.add_argument("--ny", type=int, default=256, help="Grid points in Y")
    parser.add_argument("--nu", type=float, default=1e-4, help="Kinematic viscosity")
    parser.add_argument("--t_end", type=float, default=10.0, help="End time")

    args = parser.parse_args()
    run_simulation(args.nx, args.ny, args.nu, args.t_end)
