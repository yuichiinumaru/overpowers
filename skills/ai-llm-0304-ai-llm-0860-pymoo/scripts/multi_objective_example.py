from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.problems import get_problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
import numpy as np

def main():
    # 1. Define multi-objective problem
    # ZDT1 is a common bi-objective benchmark problem
    problem = get_problem("zdt1")

    # 2. Configure NSGA-II (standard for multi-objective)
    algorithm = NSGA2(
        pop_size=100,
        eliminate_duplicates=True
    )

    # 3. Run optimization to obtain Pareto front
    print("Starting multi-objective optimization (ZDT1)...")
    result = minimize(
        problem, 
        algorithm, 
        ('n_gen', 200), 
        seed=1,
        verbose=False
    )

    print(f"Optimization Complete. Found {len(result.F)} Pareto-optimal solutions.")

    # 4. Visualize trade-offs
    # In a real environment, this would open a window.
    # Here we just print the first few results.
    print("\nTop 5 Pareto-optimal objective values (f1, f2):")
    print(result.F[:5])

    # Note: To visualize, one would use:
    # plot = Scatter()
    # plot.add(result.F, label="Obtained Front")
    # plot.show()

if __name__ == "__main__":
    main()
