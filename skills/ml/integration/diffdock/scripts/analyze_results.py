#!/usr/bin/env python3
import argparse
import os
import csv

def analyze_directory(results_dir, threshold=None):
    results = []
    if not os.path.exists(results_dir):
        print(f"Error: Directory {results_dir} not found.")
        return results

    for item in os.listdir(results_dir):
        complex_dir = os.path.join(results_dir, item)
        if os.path.isdir(complex_dir):
            score_file = os.path.join(complex_dir, "confidence_scores.txt")
            if os.path.exists(score_file):
                with open(score_file, 'r') as f:
                    for line in f:
                        if "score" in line.lower():
                            parts = line.strip().split()
                            try:
                                score = float(parts[-1])
                                if threshold is None or score >= threshold:
                                    results.append({"complex": item, "score": score})
                            except ValueError:
                                pass
    return sorted(results, key=lambda x: x["score"], reverse=True)

def main():
    parser = argparse.ArgumentParser(description="Analyze DiffDock results")
    parser.add_argument("results_dir", help="Directory containing DiffDock results")
    parser.add_argument("--top", type=int, default=5, help="Show top N per complex")
    parser.add_argument("--threshold", type=float, help="Filter by confidence threshold")
    parser.add_argument("--export", help="Export to CSV")
    parser.add_argument("--best", type=int, help="Show top N predictions across all complexes")

    args = parser.parse_args()

    print(f"Analyzing results in {args.results_dir}...")
    results = analyze_directory(args.results_dir, args.threshold)

    if not results:
        print("No valid results found to analyze.")
        return

    print(f"Found predictions for {len(set(r['complex'] for r in results))} complexes.")

    if args.best:
        print(f"\nTop {args.best} predictions overall:")
        for r in results[:args.best]:
            print(f"- {r['complex']}: {r['score']}")

    if args.export:
        with open(args.export, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["complex", "score"])
            writer.writeheader()
            writer.writerows(results)
        print(f"\nResults exported to {args.export}")

if __name__ == "__main__":
    main()
