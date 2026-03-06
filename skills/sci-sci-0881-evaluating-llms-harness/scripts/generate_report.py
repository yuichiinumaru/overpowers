#!/usr/bin/env python3
import json
import pandas as pd
import glob
import os
import argparse

def generate_report(results_dir):
    results = []

    # Find all json files in results dir
    for file_path in glob.glob(os.path.join(results_dir, "*.json")):
        model_name = os.path.basename(file_path).replace(".json", "").replace("-", "/")

        with open(file_path) as f:
            try:
                data = json.load(f)
                row = {"Model": model_name}

                if "results" in data:
                    for task, metrics in data["results"].items():
                        if "acc" in metrics:
                            row[task.upper()] = f"{metrics['acc']:.3f}"
                        elif "exact_match" in metrics:
                            row[task.upper()] = f"{metrics['exact_match']:.3f}"
                        elif "acc_norm" in metrics:
                            row[task.upper()] = f"{metrics['acc_norm']:.3f}"

                results.append(row)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    if results:
        df = pd.DataFrame(results)
        print(df.to_markdown(index=False))
    else:
        print("No valid results found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate markdown table from lm_eval results")
    parser.add_argument("--dir", default="results", help="Directory containing result JSONs")
    args = parser.parse_args()

    generate_report(args.dir)
