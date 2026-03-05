import argparse
import json

def calculate_ice(impact, confidence, ease):
    """ICE Score: Impact * Confidence * Ease"""
    return impact * confidence * ease

def calculate_rice(reach, impact, confidence, effort):
    """RICE Score: (Reach * Impact * Confidence) / Effort"""
    return (reach * impact * confidence) / effort

def calculate_matrix(criteria, options):
    """
    Weighted Decision Matrix
    criteria: list of { "name": str, "weight": float }
    options: list of { "name": str, "scores": { criteria_name: score } }
    """
    results = []
    for opt in options:
        total_score = 0
        for crit in criteria:
            score = opt["scores"].get(crit["name"], 0)
            total_score += score * crit["weight"]
        results.append({
            "name": opt["name"],
            "total_score": round(total_score, 2)
        })
    
    # Sort by total score descending
    results.sort(key=lambda x: x["total_score"], reverse=True)
    return results

def main():
    parser = argparse.ArgumentParser(description="Decision Frameworks Helper")
    subparsers = parser.add_subparsers(dest="command")
    
    # ICE Parser
    ice_parser = subparsers.add_parser("ice", help="Calculate ICE Score")
    ice_parser.add_argument("--impact", type=float, required=True, help="Impact (1-10)")
    ice_parser.add_argument("--confidence", type=float, required=True, help="Confidence (1-10)")
    ice_parser.add_argument("--ease", type=float, required=True, help="Ease (1-10)")
    
    # RICE Parser
    rice_parser = subparsers.add_parser("rice", help="Calculate RICE Score")
    rice_parser.add_argument("--reach", type=float, required=True, help="Reach (estimated count)")
    rice_parser.add_argument("--impact", type=float, required=True, help="Impact (score)")
    rice_parser.add_argument("--confidence", type=float, required=True, help="Confidence (%)")
    rice_parser.add_argument("--effort", type=float, required=True, help="Effort (person-months)")
    
    # Matrix Parser
    matrix_parser = subparsers.add_parser("matrix", help="Calculate Weighted Decision Matrix from JSON")
    matrix_parser.add_argument("--input", type=str, required=True, help="Path to input JSON file")
    
    args = parser.parse_args()
    
    if args.command == "ice":
        score = calculate_ice(args.impact, args.confidence, args.ease)
        print(f"ICE Score: {score}")
    elif args.command == "rice":
        score = calculate_rice(args.reach, args.impact, args.confidence, args.effort)
        print(f"RICE Score: {score}")
    elif args.command == "matrix":
        with open(args.input, 'r') as f:
            data = json.load(f)
            results = calculate_matrix(data["criteria"], data["options"])
            print("Weighted Decision Matrix Results:")
            for res in results:
                print(f"- {res['name']}: {res['total_score']}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
