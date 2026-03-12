import cobra
from cobra.io import load_model, read_sbml_model
import argparse
import sys

def run_fba(model_path):
    print(f"🧬 Loading metabolic model: {model_path}...")
    try:
        if model_path in ["textbook", "ecoli", "salmonella"]:
            model = load_model(model_path)
        else:
            model = read_sbml_model(model_path)
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return
        
    print(f"✅ Model loaded: {model.id}")
    print(f"   Reactions: {len(model.reactions)}")
    print(f"   Metabolites: {len(model.metabolites)}")
    
    print("🚀 Running Flux Balance Analysis (FBA)...")
    solution = model.optimize()
    
    print(f"✨ Status: {solution.status}")
    print(f"✨ Objective Value (Growth Rate): {solution.objective_value:.4f}")
    
    # Show top fluxes
    print("\n🔝 Top 10 Fluxes:")
    print(solution.fluxes.abs().sort_values(ascending=False).head(10))
    return solution

def main():
    parser = argparse.ArgumentParser(description="Run FBA on a metabolic model using COBRApy.")
    parser.add_argument("model", help="Path to SBML model or name of built-in model (textbook, ecoli)")
    
    args = parser.parse_args()
    run_fba(args.model)

if __name__ == "__main__":
    main()
