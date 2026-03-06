import argparse
import json
import csv
import os

def flatten_asm(input_file, output_file=None):
    if not output_file:
        base, _ = os.path.splitext(input_file)
        output_file = f"{base}_flat.csv"

    print(f"Flattening {input_file} to 2D CSV...")

    try:
        with open(input_file, 'r') as f:
            data = json.load(f)

        # Basic flattening - actual implementation would be more complex
        # depending on the specific ASM schema type
        rows = []

        # This is a simplified flattening strategy suitable for a template script
        def extract_measurements(obj, prefix="", current_row=None):
            if current_row is None:
                current_row = {}

            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == "measurement-document" and isinstance(v, list):
                        for m in v:
                            row_copy = current_row.copy()
                            extract_measurements(m, "", row_copy)
                            rows.append(row_copy)
                    elif isinstance(v, (dict, list)):
                        extract_measurements(v, f"{prefix}{k}_", current_row)
                    else:
                        current_row[f"{prefix}{k}"] = v
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    extract_measurements(item, f"{prefix}{i}_", current_row)

        extract_measurements(data)

        if not rows:
            print("Warning: Could not extract measurements. Output may be empty.")

        if rows:
            # Get all unique headers
            headers = set()
            for r in rows:
                headers.update(r.keys())

            with open(output_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=sorted(list(headers)))
                writer.writeheader()
                writer.writerows(rows)

            print(f"Successfully flattened to {output_file}")

    except Exception as e:
        print(f"Error during flattening: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flatten ASM JSON to CSV")
    parser.add_argument("input", help="Input ASM JSON file")
    parser.add_argument("--output", help="Output CSV file path")
    args = parser.parse_args()

    flatten_asm(args.input, args.output)
