#!/usr/bin/env python3
"""
Batch convert all documents in a directory to Markdown using Docling.
"""
import os
import sys
import argparse
from pathlib import Path
from docling.document_converter import DocumentConverter

def main():
    parser = argparse.ArgumentParser(description="Batch convert documents to Markdown using Docling.")
    parser.add_argument("input_dir", help="Directory containing documents")
    parser.add_argument("output_dir", help="Directory to save markdown files")
    parser.add_argument("--ext", default="pdf,docx,pptx", help="Comma-separated extensions to process")
    
    args = parser.parse_args()
    
    input_path = Path(args.input_dir)
    output_path = Path(args.output_dir)
    extensions = [f".{ext.strip().lower()}" for ext in args.ext.split(",")]
    
    if not input_path.exists():
        print(f"Error: Input directory '{args.input_dir}' not found.")
        sys.exit(1)
        
    output_path.mkdir(parents=True, exist_ok=True)
    
    converter = DocumentConverter()
    
    for file in input_path.iterdir():
        if file.suffix.lower() in extensions:
            print(f"Processing: {file.name}...")
            try:
                result = converter.convert(str(file))
                markdown_text = result.document.export_to_markdown()
                
                output_file = output_path / f"{file.stem}.md"
                output_file.write_text(markdown_text)
                print(f"  [OK] Saved to {output_file.name}")
            except Exception as e:
                print(f"  [FAILED] {file.name}: {e}")

if __name__ == "__main__":
    main()
