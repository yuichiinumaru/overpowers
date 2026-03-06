import argparse
import json
import os
import sys

try:
    from allotropy.parser_factory import Vendor
    from allotropy.to_allotrope import allotrope_from_file
except ImportError:
    print("Error: allotropy package not installed. Run 'pip install allotropy'", file=sys.stderr)
    sys.exit(1)

def convert_to_asm(input_file, vendor_name, output_file=None):
    if not output_file:
        base, _ = os.path.splitext(input_file)
        output_file = f"{base}_asm.json"

    print(f"Converting {input_file} using vendor parser: {vendor_name}")

    try:
        vendor_enum = getattr(Vendor, vendor_name.upper())
    except AttributeError:
        print(f"Error: Vendor '{vendor_name}' not found in allotropy Vendor enum.")
        print("Available vendors include:")
        for v in Vendor:
            print(f"  - {v.name}")
        sys.exit(1)

    try:
        asm_dict = allotrope_from_file(input_file, vendor_enum)

        with open(output_file, 'w') as f:
            json.dump(asm_dict, f, indent=2)

        print(f"Successfully converted to {output_file}")

    except Exception as e:
        print(f"Error during conversion: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert instrument data to Allotrope ASM JSON")
    parser.add_argument("input", help="Input instrument file")
    parser.add_argument("--vendor", required=True, help="Allotropy Vendor enum name (e.g., BECKMAN_VI_CELL_BLU)")
    parser.add_argument("--output", help="Output ASM JSON file path")
    args = parser.parse_args()

    convert_to_asm(args.input, args.vendor, args.output)
