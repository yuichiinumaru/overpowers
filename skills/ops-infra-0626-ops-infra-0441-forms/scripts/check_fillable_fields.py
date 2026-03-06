#!/usr/bin/env python3
import sys
import PyPDF2

def check_fillable_fields(pdf_path):
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            fields = reader.get_fields()
            if fields:
                print(f"Yes, {pdf_path} has fillable fields.")
            else:
                print(f"No fillable fields found in {pdf_path}.")
    except Exception as e:
        print(f"Error reading PDF: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_fillable_fields.py <file.pdf>")
        sys.exit(1)
    check_fillable_fields(sys.argv[1])
