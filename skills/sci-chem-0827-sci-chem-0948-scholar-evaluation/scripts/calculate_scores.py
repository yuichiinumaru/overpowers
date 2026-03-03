import json
import argparse
import sys

def calculate_aggregate_scores(scores_dict, weights=None):
    """
    Calculate weighted aggregate scores from dimension ratings.
    scores_dict: {dimension_name: score_1_to_5}
    weights: {dimension_name: weight_multiplier}
    """
    if not scores_dict:
        return {"error": "Empty scores dictionary"}
        
    if weights is None:
        # Equal weighting by default
        weights = {k: 1.0 for k in scores_dict.keys()}
        
    total_weighted_score = 0
    total_weight = 0
    
    dimension_results = {}
    
    for dim, score in scores_dict.items():
        weight = weights.get(dim, 1.0)
        total_weighted_score += score * weight
        total_weight += weight
        
        # Qualitative label
        label = "Unknown"
        if score >= 4.5: label = "Excellent"
        elif score >= 3.5: label = "Good"
        elif score >= 2.5: label = "Adequate"
        elif score >= 1.5: label = "Needs Improvement"
        else: label = "Poor"
        
        dimension_results[dim] = {"score": score, "label": label}
        
    overall_avg = total_weighted_score / total_weight if total_weight > 0 else 0
    
    overall_label = "Unknown"
    if overall_avg >= 4.5: overall_label = "Excellent"
    elif overall_avg >= 3.5: overall_label = "Good"
    elif overall_avg >= 2.5: overall_label = "Adequate"
    elif overall_avg >= 1.5: overall_label = "Needs Improvement"
    else: overall_label = "Poor"
    
    return {
        "overall_average": round(overall_avg, 2),
        "overall_label": overall_label,
        "dimensions": dimension_results
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate ScholarEval scores")
    parser.add_argument("--scores", help="Path to dimension_scores.json")
    parser.add_argument("--output", help="Path to output report file")
    
    args = parser.parse_args()
    
    if args.scores:
        try:
            with open(args.scores, 'r') as f:
                scores_data = json.load(f)
            
            results = calculate_aggregate_scores(scores_data)
            
            report = json.dumps(results, indent=2)
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(report)
                print(f"Report saved to {args.output}")
            else:
                print(report)
        except Exception as e:
            print(f"Error: {e}")
    else:
        # Example usage output
        example_scores = {
            "Problem Formulation": 4,
            "Literature Review": 3,
            "Methodology": 5,
            "Analysis": 4,
            "Writing": 4
        }
        print("Example Output:")
        print(json.dumps(calculate_aggregate_scores(example_scores), indent=2))
