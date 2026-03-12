import argparse
import json
from tdc.benchmark_group import admet_group

def main():
    parser = argparse.ArgumentParser(description='Run TDC benchmark group evaluation.')
    parser.add_argument('--group', default='admet', choices=['admet', 'dti', 'drugcombo'], help='Benchmark group name')
    parser.add_argument('--dataset', required=True, help='Dataset name in the group')
    parser.add_argument('--predictions', required=True, help='Path to JSON file with predictions for 5 seeds')
    parser.add_argument('--data-dir', default='data/', help='Directory for benchmark data')

    args = parser.parse_args()

    if args.group == 'admet':
        group = admet_group(path=args.data_dir)
    else:
        print(f"Error: Group {args.group} not implemented in this script yet.")
        return

    # Load predictions
    with open(args.predictions, 'r') as f:
        y_pred = json.load(f)
    
    # Ensure y_pred keys are integers if they were saved as strings in JSON
    y_pred = {int(k): v for k, v in y_pred.items()}

    print(f"Evaluating {args.dataset} in {args.group} group...")
    results = group.evaluate(y_pred, benchmark=args.dataset)
    print("\n=== Evaluation Results ===")
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
