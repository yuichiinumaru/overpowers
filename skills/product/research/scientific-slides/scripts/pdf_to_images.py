import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Convert PDF to images for visual inspection.')
    parser.add_argument('input', help='Input PDF file')
    parser.add_argument('output_prefix', help='Output prefix (e.g. output/slide)')
    parser.add_argument('--dpi', type=int, default=150, help='Resolution DPI')

    args = parser.parse_args()

    print(f"Converting {args.input} to images at {args.dpi} DPI...")
    out_dir = os.path.dirname(args.output_prefix)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir)
        print(f"Created output directory: {out_dir}")
        
    print(f"Saving images with prefix: {args.output_prefix}")
    print("Note: This is a placeholder script. Real implementation would use pdf2image or poppler.")

if __name__ == "__main__":
    main()
