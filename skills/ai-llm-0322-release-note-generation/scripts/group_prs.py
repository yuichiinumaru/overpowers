import json
import os
import csv
import argparse

def group_prs(json_file, output_dir):
    if not os.path.exists(json_file):
        print(f"Error: {json_file} not found.")
        return

    with open(json_file, 'r') as f:
        prs = json.load(f)

    os.makedirs(output_dir, exist_ok=True)
    
    label_groups = {}
    
    for pr in prs:
        labels = [l['name'] for l in pr.get('labels', [])]
        # Filtering logic from SKILL.md: keeps Product-*, Area-*, GitHub*, *Plugin, Issue-*
        relevant_labels = [l for l in labels if any(l.startswith(p) or l.endswith(p) for p in ['Product-', 'Area-', 'GitHub', 'Plugin', 'Issue-'])]
        
        if not relevant_labels:
            relevant_labels = ['Unlabeled']
            
        for label in relevant_labels:
            if label not in label_groups:
                label_groups[label] = []
            label_groups[label].append(pr)

    for label, pr_list in label_groups.items():
        safe_label = label.replace('/', '_').replace(' ', '_')
        output_path = os.path.join(output_dir, f"{safe_label}.csv")
        with open(output_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Number', 'Title', 'Author', 'URL', 'ClosedAt'])
            for pr in pr_list:
                writer.writerow([
                    pr.get('number'),
                    pr.get('title'),
                    pr.get('author', {}).get('login'),
                    pr.get('url'),
                    pr.get('closedAt')
                ])
        print(f"Generated {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Group PRs by label")
    parser.add_argument("--input", default="milestone_prs.json", help="Input JSON file")
    parser.add_argument("--output", default="grouped_csv", help="Output directory for CSVs")
    
    args = parser.parse_args()
    group_prs(args.input, args.output)

if __name__ == "__main__":
    main()
