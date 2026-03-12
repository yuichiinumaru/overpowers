#!/usr/bin/env python3
import json
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Calculate TPR and TNR for evaluator validation")
    parser.add_argument("input_file", help="JSON file containing list of dicts with 'human_label' and 'judge_label' (Pass/Fail)")
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        sys.exit(1)

    tp, fp, tn, fn = 0, 0, 0, 0

    for item in data:
        human = item.get('human_label', '').lower()
        judge = item.get('judge_label', '').lower()

        # We assume binary Pass/Fail or true/false equivalent
        human_pass = human in ['pass', 'true', '1']
        judge_pass = judge in ['pass', 'true', '1']

        if human_pass and judge_pass:
            tp += 1
        elif human_pass and not judge_pass:
            fn += 1
        elif not human_pass and not judge_pass:
            tn += 1
        elif not human_pass and judge_pass:
            fp += 1

    total_human_pass = tp + fn
    total_human_fail = tn + fp

    tpr = tp / total_human_pass if total_human_pass > 0 else 0.0
    tnr = tn / total_human_fail if total_human_fail > 0 else 0.0

    accuracy = (tp + tn) / len(data) if data else 0.0

    print(f"Total samples: {len(data)}")
    print(f"Human Pass: {total_human_pass}, Human Fail: {total_human_fail}")
    print("-" * 30)
    print(f"True Positives (TP): {tp}")
    print(f"False Positives (FP): {fp}")
    print(f"True Negatives (TN): {tn}")
    print(f"False Negatives (FN): {fn}")
    print("-" * 30)
    print(f"TPR (Recall for Pass): {tpr:.4f}  (Target: >0.90)")
    print(f"TNR (Recall for Fail): {tnr:.4f}  (Target: >0.90)")
    print(f"Raw Accuracy:          {accuracy:.4f}  (Warning: misleading if classes imbalanced)")

    print("\nDisagreements to inspect:")
    for i, item in enumerate(data):
        human = item.get('human_label', '').lower()
        judge = item.get('judge_label', '').lower()
        human_pass = human in ['pass', 'true', '1']
        judge_pass = judge in ['pass', 'true', '1']

        if human_pass != judge_pass:
            trace_id = item.get('trace_id', f"Row {i+1}")
            disagreement_type = "False Pass (Judge=Pass, Human=Fail)" if judge_pass else "False Fail (Judge=Fail, Human=Pass)"
            print(f"- {trace_id}: {disagreement_type}")

if __name__ == "__main__":
    main()
