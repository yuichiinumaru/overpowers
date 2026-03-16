import allotropy
from allotropy.parser_factory import VendorType
from allotropy.allotrope_converter import AllotropeConverter
import argparse
import json

def convert_to_allotrope(input_file: str, vendor: str, output_file: str):
    """
    Convert instrument data to Allotrope Simple Model (ASM) format using allotropy.
    """
    print(f"Converting {input_file} for vendor {vendor}...")

    try:
        # Match the vendor string to the enum
        vendor_type = None
        for v in VendorType:
            if v.name == vendor:
                vendor_type = v
                break

        if not vendor_type:
            print(f"Error: Unsupported vendor '{vendor}'.")
            print("Supported vendors:")
            for v in VendorType:
                print(f"  - {v.name}")
            return False

        converter = AllotropeConverter()

        # Convert file to ASM dictionary
        asm_dict = converter.read_to_dict(
            file_path=input_file,
            vendor_type=vendor_type
        )

        # Save to JSON
        with open(output_file, 'w') as f:
            json.dump(asm_dict, f, indent=2)

        print(f"Successfully converted to {output_file}")
        return True

    except Exception as e:
        print(f"Conversion failed: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert instrument data to Allotrope format")
    parser.add_argument("--input", required=True, help="Input instrument data file")
    parser.add_argument("--vendor", required=True, help="Vendor type (e.g., BECKMAN_VI_CELL_BLU, AGILENT_TAPESTATION_ANALYSIS)")
    parser.add_argument("--out", default="output_asm.json", help="Output JSON file path")

    args = parser.parse_args()
    convert_to_allotrope(args.input, args.vendor, args.out)
