import argparse
import sys
import csv
import os

def create_template(output_file):
    header = ["complex_name", "protein_path", "ligand_description", "protein_sequence"]
    example_data = [
        ["complex1", "protein1.pdb", "CC(=O)Oc1ccccc1C(=O)O", ""],
        ["complex2", "", "COc1ccc(C#N)cc1", "MSKGEELFTGVVPILVELDGDVNGHKF"]
    ]

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(example_data)
    print(f"Template created at {output_file}")

def validate_csv(input_file):
    print(f"Validating {input_file}...")
    try:
        with open(input_file, 'r') as f:
            reader = csv.DictReader(f)
            required = ["complex_name", "protein_path", "ligand_description", "protein_sequence"]
            missing = [col for col in required if col not in reader.fieldnames]

            if missing:
                print(f"❌ Missing required columns: {missing}", file=sys.stderr)
                return False

            for i, row in enumerate(reader, start=2):
                if not row['protein_path'] and not row['protein_sequence']:
                    print(f"❌ Row {i}: Must provide either protein_path or protein_sequence", file=sys.stderr)
                    return False
                if not row['ligand_description']:
                    print(f"❌ Row {i}: Missing ligand_description", file=sys.stderr)
                    return False

            print("✅ CSV format is valid")
            return True
    except FileNotFoundError:
        print(f"❌ File not found: {input_file}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"❌ Error reading CSV: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="Prepare batch CSV for DiffDock")
    parser.add_argument("input", nargs="?", help="Input CSV to validate")
    parser.add_argument("--create", action="store_true", help="Create template")
    parser.add_argument("--validate", action="store_true", help="Validate input CSV")
    parser.add_argument("--output", default="batch_input.csv", help="Output file for template")

    args = parser.parse_args()

    if args.create:
        create_template(args.output)
    elif args.validate and args.input:
        sys.exit(0 if validate_csv(args.input) else 1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
