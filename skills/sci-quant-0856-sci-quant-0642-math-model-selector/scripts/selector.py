import sys

def main():
    print("=== Math Model Selector ===")
    print("Answer the following questions to find the right mathematical framework.\n")

    # Q1: Quantity
    print("Q1: What quantity or phenomenon are you trying to understand?")
    print("1) Physics problem (motion, energy, fields)")
    print("2) Economics/Social (growth, equilibrium, strategy)")
    print("3) Data patterns (correlation, prediction)")
    print("4) Logic/Discrete structures (sets, networks, computer science)")
    q1 = input("> ")

    # Q2: Change
    print("\nQ2: What changes, and how does it change?")
    print("1) Discrete steps (iterations, stages)")
    print("2) Continuous rate (speed, flow, decay)")
    print("3) Rate of rate matters (acceleration, oscillation)")
    print("4) Varies across space and time (heat, waves)")
    q2 = input("> ")

    # Q3: Uncertainty
    print("\nQ3: Is there randomness or uncertainty involved?")
    print("1) No, it's deterministic")
    print("2) Yes, inherent randomness (stochastic)")
    print("3) Yes, lack of knowledge (epistemic uncertainty)")
    q3 = input("> ")

    # Q4: Optimization
    print("\nQ4: Are you optimizing something (finding max/min)?")
    print("1) No, just modeling dynamics")
    print("2) Yes, simple smooth function (convex)")
    print("3) Yes, complex/multiple peaks (non-convex)")
    print("4) Yes, best choice from discrete set")
    q4 = input("> ")

    # Logic for Recommendation
    print("\n--- Framework Recommendation ---")
    
    if q4 in ['2', '3', '4']:
        if q4 == '2':
            print("Primary: Convex Optimization")
            print("Why: Efficient global minimum finding for smooth functions.")
        elif q4 == '3':
            print("Primary: Global Optimization (Gradient Descent, Evolutionary)")
            print("Why: Complex search space requires robust heuristics.")
        else:
            print("Primary: Integer/Combinatorial Programming")
            print("Why: Discrete decision space.")
    elif q2 == '2':
        if q3 == '1':
            print("Primary: First-order ODEs")
            print("Why: Modeling continuous rates of change deterministically.")
        else:
            print("Primary: Stochastic Differential Equations (SDEs)")
            print("Why: Continuous change with inherent randomness.")
    elif q2 == '3':
        print("Primary: Second-order ODEs")
        print("Why: Acceleration or oscillatory behavior requires higher order derivatives.")
    elif q2 == '4':
        print("Primary: Partial Differential Equations (PDEs)")
        print("Why: Modeling phenomena that vary across multiple independent variables.")
    elif q2 == '1':
        print("Primary: Difference Equations / Recurrence Relations")
        print("Why: Discrete-time dynamics.")
    elif q1 == '3':
        print("Primary: Statistical Learning / Regression")
        print("Why: Finding patterns in empirical data.")
    else:
        print("Primary: Algebraic Modeling")
        print("Why: Basic structural relationships.")

    print("\n--- Related Skills ---")
    print("- math-intuition-builder")
    print("- math-mode (symbolic verification)")

if __name__ == "__main__":
    main()
