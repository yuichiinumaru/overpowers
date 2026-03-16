#!/usr/bin/env python3
"""
Helper script to convert presentation PDFs to images for visual review.
Requires PyMuPDF (fitz).
"""
import sys
import os
import argparse

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: PyMuPDF is not installed. Please install it using 'uv pip install PyMuPDF'")
    sys.exit(1)

def convert_pdf_to_images(pdf_path, output_prefix, dpi=150):
    if not os.path.exists(pdf_path):
        print(f"Error: File not found: {pdf_path}")
        return False

    output_dir = os.path.dirname(output_prefix)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        print(f"Opened {pdf_path} ({total_pages} pages)")

        # Calculate zoom factor for target DPI (default PDF is 72 DPI)
        zoom = dpi / 72.0
        mat = fitz.Matrix(zoom, zoom)

        generated_files = []
        for i in range(total_pages):
            page = doc.load_page(i)
            pix = page.get_pixmap(matrix=mat)

            output_file = f"{output_prefix}-{i+1:03d}.jpg"
            pix.save(output_file)
            generated_files.append(output_file)
            print(f"Saved {output_file}")

        doc.close()
        print(f"Successfully converted {total_pages} pages.")
        return generated_files

    except Exception as e:
        print(f"Error converting PDF: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF presentations to images for visual review")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("output_prefix", help="Prefix for output image files (e.g., 'review/slide')")
    parser.add_argument("--dpi", type=int, default=150, help="Resolution in DPI (default: 150)")

    args = parser.parse_args()
    convert_pdf_to_images(args.pdf_path, args.output_prefix, args.dpi)
