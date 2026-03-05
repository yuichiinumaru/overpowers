import argparse
import os

def parse_recommendations(file_path):
    if not os.path.exists(file_path):
        return None
        
    recommendations = []
    current_rec = None
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        if not line or line.startswith("=") or line == "RECOMMENDATIONS FOR IMPROVEMENT":
            continue
            
        if line[0].isdigit() and ". " in line:
            if current_rec:
                recommendations.append(current_rec)
            current_rec = {
                "title": line.split(". ", 1)[1],
                "problem": "",
                "solutions": []
            }
        elif current_rec:
            if line.startswith("Problem:"):
                current_rec["problem"] = line.replace("Problem:", "").strip()
            elif line.startswith("- "):
                current_rec["solutions"].append(line[2:])
                
    if current_rec:
        recommendations.append(current_rec)
        
    return recommendations

def generate_plan(recommendations, output_path):
    plan = [
        "# Workflow Improvement Action Plan",
        "",
        "This plan is based on the analysis of your conversation history.",
        ""
    ]
    
    for rec in recommendations:
        plan.append(f"## {rec['title']}")
        plan.append(f"**Issue Identified**: {rec['problem']}")
        plan.append("\n### Action Items")
        for sol in rec['solutions']:
            plan.append(f"- [ ] {sol}")
        plan.append("")
        
    with open(output_path, 'w') as f:
        f.write("\n".join(plan))
        
    print(f"Action plan generated at: {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Generate a structured action plan from recommendations.')
    parser.add_argument('--input', default='recommendations.txt', help='Input recommendations file')
    parser.add_argument('--output', default='workflow_improvement_plan.md', help='Output plan file')

    args = parser.parse_args()
    
    recs = parse_recommendations(args.input)
    if recs:
        generate_plan(recs, args.output)
    else:
        print(f"Could not find or parse {args.input}")

if __name__ == "__main__":
    main()
