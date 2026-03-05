import argparse
import os
import glob
from pymatgen.core import Structure

def convert_file(input_file, output_path, output_format=None):
    try:
        struct = Structure.from_file(input_file)
        if os.path.isdir(output_path):
            filename = os.path.basename(input_file)
            name, _ = os.path.splitext(filename)
            ext = output_format if output_format else "cif"
            output_file = os.path.join(output_path, f"{name}.{ext}")
        else:
            output_file = output_path
            
        struct.to(filename=output_file, fmt=output_format)
        print(f"Successfully converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error converting {input_file}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Convert between structure file formats using pymatgen.')
    parser.add_argument('input', help='Input file or pattern (e.g. *.cif)')
    parser.add_argument('output', help='Output file or directory')
    parser.add_argument('--format', help='Output format (cif, poscar, xyz, etc.)')
    parser.add_argument('--output-dir', help='Output directory for batch conversion')

    args = parser.parse_args()

    input_files = glob.glob(args.input)
    if not input_files:
        if os.path.exists(args.input):
            input_files = [args.input]
        else:
            print(f"Error: No files found matching {args.input}")
            return

    output_dest = args.output_dir if args.output_dir else args.output
    if len(input_files) > 1 and not os.path.isdir(output_dest):
        os.makedirs(output_dest, exist_ok=True)

    for f in input_files:
        convert_file(f, output_dest, args.format)

if __name__ == "__main__":
    main()
