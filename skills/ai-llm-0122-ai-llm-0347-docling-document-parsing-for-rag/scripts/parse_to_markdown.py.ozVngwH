#!/usr/bin/env python3
"""
Convert a document to Markdown using Docling.
"""
import sys
import argparse
from docling.document_converter import DocumentConverter

def main():
    parser = argparse.ArgumentParser(description="Convert document to Markdown using Docling.")
    parser.add_argument("input_source", help="Path to local file or URL")
    parser.add_argument("--output", help="Path to output markdown file (optional)")
    
    args = parser.parse_args()
    
    print(f"Converting: {args.input_source}...")
    converter = DocumentConverter()
    
    try:
        result = converter.convert(args.input_source)
        markdown_text = result.document.export_to_markdown()
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(markdown_text)
            print(f"Markdown saved to: {args.output}")
        else:
            print(markdown_text)
            
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
