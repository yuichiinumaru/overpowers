import csv
import argparse
import json
import sys

def calculate_rice(reach, impact, confidence, effort):
    # Impact mapping
    impact_map = {
        "massive": 3.0,
        "high": 2.0,
        "medium": 1.0,
        "low": 0.5,
        "minimal": 0.25
    }
    
    # Confidence mapping
    confidence_map = {
        "high": 1.0,
        "medium": 0.8,
        "low": 0.5
    }
    
    # Effort mapping
    effort_map = {
        "xl": 13.0,
        "l": 8.0,
        "m": 5.0,
        "s": 3.0,
        "xs": 1.0
    }
    
    i = impact_map.get(impact.lower(), 1.0)
    c = confidence_map.get(confidence.lower(), 0.8)
    
    # Check if effort is numeric or mapped
    try:
        e = float(effort)
    except ValueError:
        e = effort_map.get(effort.lower(), 5.0)
        
    if e == 0:
        e = 0.5 # Avoid division by zero
        
    return (float(reach) * i * c) / e

def create_sample_csv(filename):
    fieldnames = ['name', 'reach', 'impact', 'confidence', 'effort']
    data = [
        {'name': 'Feature A', 'reach': '1000', 'impact': 'high', 'confidence': 'high', 'effort': 'm'},
        {'name': 'Feature B', 'reach': '500', 'impact': 'massive', 'confidence': 'medium', 'effort': 'l'},
        {'name': 'Feature C', 'reach': '2000', 'impact': 'medium', 'confidence': 'high', 'effort': 's'},
        {'name': 'Feature D', 'reach': '100', 'impact': 'low', 'confidence': 'low', 'effort': 'xs'},
    ]
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Created sample file: {filename}")

def main():
    parser = argparse.ArgumentParser(description='RICE Prioritizer')
    parser.add_argument('input', help='CSV file with feature data or "sample" to create a sample file')
    parser.add_argument('--capacity', type=float, help='Team capacity in person-months')
    parser.add_argument('--output', choices=['text', 'json', 'csv'], default='text', help='Output format')
    
    args = parser.parse_args()
    
    if args.input == 'sample':
        create_sample_csv('sample_features.csv')
        return

    features = []
    try:
        with open(args.input, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                score = calculate_rice(row['reach'], row['impact'], row['confidence'], row['effort'])
                row['rice_score'] = score
                features.append(row)
    except FileNotFoundError:
        print(f"Error: File {args.input} not found.")
        sys.exit(1)

    # Sort by RICE score descending
    features.sort(key=lambda x: x['rice_score'], reverse=True)

    if args.output == 'json':
        print(json.dumps(features, indent=2))
    elif args.output == 'csv':
        if features:
            writer = csv.DictWriter(sys.stdout, fieldnames=features[0].keys())
            writer.writeheader()
            writer.writerows(features)
    else:
        print(f"{'Feature Name':<30} | {'Reach':<8} | {'Impact':<8} | {'Conf':<8} | {'Effort':<6} | {'RICE Score'}")
        print("-" * 85)
        accumulated_effort = 0
        for f in features:
            status = ""
            # Map effort for display if it was mapped in calculation
            effort_val = f['effort']
            try:
                e_float = float(effort_val)
            except ValueError:
                effort_map = {"xl": 13.0, "l": 8.0, "m": 5.0, "s": 3.0, "xs": 1.0}
                e_float = effort_map.get(effort_val.lower(), 5.0)
            
            accumulated_effort += e_float
            if args.capacity and accumulated_effort > args.capacity:
                status = " (Over Capacity)"
                
            print(f"{f['name']:<30} | {f['reach']:<8} | {f['impact']:<8} | {f['confidence']:<8} | {f['effort']:<6} | {f['rice_score']:.2f}{status}")

if __name__ == "__main__":
    main()
