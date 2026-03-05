from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.problems import get_problem
from pymoo.optimize import minimize
import numpy as np

def main():
    # 1. Define or select problem
    # Rastrigin is a standard single-objective benchmark problem
    problem = get_problem("rastrigin", n_var=10)

    # 2. Choose single-objective algorithm (Genetic Algorithm)
    algorithm = GA(
        pop_size=100,
        eliminate_duplicates=True
    )

    # 3. Configure termination criteria (200 generations)
    termination = ('n_gen', 200)

    # 4. Run optimization
    print("Starting single-objective optimization (Rastrigin)...")
    result = minimize(
        problem,
        algorithm,
        termination,
        seed=1,
        verbose=True
    )

    # 5. Extract best solution
    print("\nOptimization Complete.")
    print(f"Best solution found: \n{result.X}")
    print(f"Best objective value: {result.F[0]:.6f}")

if __name__ == "__main__":
    main()
