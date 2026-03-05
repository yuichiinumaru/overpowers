import os
import subprocess
import argparse
import shutil
import tempfile

def render_docx(docx_path, output_dir):
    if not os.path.exists(docx_path):
        print(f"Error: File '{docx_path}' not found.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Use a temporary directory for the conversion
    with tempfile.TemporaryDirectory() as tmp_dir:
        # 1. Convert DOCX to PDF using LibreOffice
        print(f"Converting {docx_path} to PDF...")
        try:
            subprocess.run([
                "soffice", 
                "--headless", 
                "--convert-to", "pdf", 
                "--outdir", tmp_dir, 
                docx_path
            ], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during PDF conversion: {e}")
            return
        except FileNotFoundError:
            print("Error: 'soffice' (LibreOffice) not found. Please install it.")
            return

        pdf_filename = os.path.splitext(os.path.basename(docx_path))[0] + ".pdf"
        pdf_path = os.path.join(tmp_dir, pdf_filename)

        if not os.path.exists(pdf_path):
            print("Error: PDF file was not generated.")
            return

        # 2. Convert PDF to PNGs using pdftoppm
        print(f"Converting PDF to PNGs...")
        try:
            subprocess.run([
                "pdftoppm", 
                "-png", 
                pdf_path, 
                os.path.join(output_dir, "page")
            ], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during PNG conversion: {e}")
            return
        except FileNotFoundError:
            print("Error: 'pdftoppm' not found. Please install poppler-utils.")
            return

    print(f"Rendering complete. Pages saved in: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render a DOCX file to PNG images.")
    parser.add_argument("docx_path", help="Path to the DOCX file")
    parser.add_argument("--output_dir", default="rendered_pages", help="Directory to save the rendered pages")
    args = parser.parse_args()

    render_docx(args.docx_path, args.output_dir)
