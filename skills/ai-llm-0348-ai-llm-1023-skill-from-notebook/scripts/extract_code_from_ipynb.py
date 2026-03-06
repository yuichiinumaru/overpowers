#!/usr/bin/env python3
import argparse
import json
import os

def extract_code(notebook_path, output_script):
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)

        code_cells = [cell for cell in notebook.get('cells', []) if cell.get('cell_type') == 'code']

        with open(output_script, 'w', encoding='utf-8') as f:
            f.write("#!/usr/bin/env python3\n")
            f.write("# Auto-extracted from Jupyter Notebook\n\n")

            for i, cell in enumerate(code_cells):
                source = cell.get('source', [])
                if source:
                    f.write(f"# --- Cell {i+1} ---\n")
                    for line in source:
                        # Optional: filter out magic commands like !pip or %matplotlib
                        if not line.strip().startswith(('!', '%')):
                            f.write(line)
                    f.write("\n\n")

        print(f"Extracted {len(code_cells)} code cells to {output_script}")
        return True
    except Exception as e:
        print(f"Error processing notebook: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Extract python code from Jupyter notebook cells.")
    parser.add_argument("notebook", help="Path to the .ipynb file")
    parser.add_argument("--output", help="Output python file", default="extracted_script.py")

    args = parser.parse_args()

    if not args.notebook.endswith('.ipynb'):
        print("Warning: Input file does not have a .ipynb extension.")

    extract_code(args.notebook, args.output)

if __name__ == "__main__":
    main()
