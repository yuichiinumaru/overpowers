import argparse
import sys
import os

def extract_docx(file_path, output_path):
    print(f"Extracting docx from {file_path}")
    print("Mock extraction running...")

    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        sys.exit(1)

    extracted_text = "MOCK DOCX EXTRACTED CONTENT\n\nParagraph 1.\nParagraph 2."

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(extracted_text)

    print(f"Successfully extracted text to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Extract text and tables from .docx files.")
    parser.add_argument("file", help="Path to the .docx file")
    parser.add_argument("--output", required=True, help="Output text file path")
    args = parser.parse_args()

    extract_docx(args.file, args.output)

if __name__ == "__main__":
    main()