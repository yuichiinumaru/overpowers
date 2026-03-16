import os
import argparse
from pathlib import Path
from markitdown import MarkItDown

def batch_convert(input_dir, output_dir):
    md = MarkItDown()
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    for file_path in input_path.iterdir():
        if file_path.is_file():
            try:
                print(f"Converting {file_path.name}...")
                result = md.convert(str(file_path))
                output_file = output_path / f"{file_path.stem}.md"
                output_file.write_text(result.text_content)
                print(f"✓ Saved to {output_file}")
            except Exception as e:
                print(f"✗ Failed to convert {file_path.name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch convert files to Markdown.")
    parser.add_argument("--input", required=True, help="Input directory")
    parser.add_argument("--output", required=True, help="Output directory")
    
    args = parser.parse_args()
    batch_convert(args.input, args.output)
