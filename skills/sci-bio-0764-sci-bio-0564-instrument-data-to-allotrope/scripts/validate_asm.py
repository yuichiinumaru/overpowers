import argparse
import json
import sys

def validate_asm(file_path, strict=False):
    print(f"Validating {file_path} against ASM specifications...")
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        warnings = []
        errors = []

        # Check basic structure
        if not isinstance(data, dict):
            errors.append("Root element is not a JSON object")

        # Check for calculated data aggregate
        if "calculated-data-aggregate-document" in data:
            calc_aggr = data["calculated-data-aggregate-document"]
            if "calculated-data-document" in calc_aggr:
                for doc in calc_aggr["calculated-data-document"]:
                    if "data-source-aggregate-document" not in doc:
                        warnings.append("Calculated data missing traceability (data-source-aggregate-document)")

        if errors:
            print("Validation FAILED with errors:")
            for e in errors:
                print(f"  - {e}")
            if strict:
                sys.exit(1)

        if warnings:
            print("Validation completed with warnings:")
            for w in warnings:
                print(f"  - {w}")
            if strict:
                sys.exit(1)

        if not errors and not warnings:
            print("Validation PASSED. ASM format is valid.")

    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: File {file_path} is not valid JSON.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate ASM JSON")
    parser.add_argument("input", help="Input ASM JSON file")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = parser.parse_args()

    validate_asm(args.input, args.strict)
