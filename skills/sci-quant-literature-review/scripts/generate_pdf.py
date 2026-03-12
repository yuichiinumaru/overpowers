import argparse
import subprocess
import os
import shutil

def check_dependencies():
    """Check if pandoc and xelatex are available."""
    deps = {
        "pandoc": shutil.which("pandoc"),
        "xelatex": shutil.which("xelatex")
    }
    
    for name, path in deps.items():
        if path:
            print(f"OK: {name} found at {path}")
        else:
            print(f"MISSING: {name} not found in PATH")
    
    return all(deps.values())

def generate_pdf(input_file, output_file, citation_style=None, toc=True, numbers=True):
    """Generate PDF from Markdown using Pandoc."""
    cmd = ["pandoc", input_file, "-o", output_file]
    
    # Use xelatex for better Unicode/Font support
    cmd.extend(["--pdf-engine=xelatex"])
    
    if toc:
        cmd.append("--toc")
    
    if numbers:
        cmd.append("--number-sections")
        
    # Meta-data for variables
    cmd.extend(["-V", "geometry:margin=1in"])
    
    print(f"Running command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Successfully generated {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error generating PDF: {e}")
        print(f"Pandoc stderr: {e.stderr}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to professional PDF.')
    parser.add_argument('input', nargs='?', help='Input Markdown file')
    parser.add_argument('--output', help='Output PDF file')
    parser.add_argument('--citation-style', help='Citation style (apa, nature, etc.)')
    parser.add_argument('--no-toc', action='store_false', dest='toc', help='Disable table of contents')
    parser.add_argument('--no-numbers', action='store_false', dest='numbers', help='Disable section numbering')
    parser.add_argument('--check-deps', action='store_true', help='Check system dependencies')

    args = parser.parse_args()

    if args.check_deps:
        check_dependencies()
        return

    if not args.input:
        parser.print_help()
        return

    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} not found.")
        return

    output_path = args.output or f"{os.path.splitext(args.input)[0]}.pdf"
    
    generate_pdf(args.input, output_path, args.citation_style, args.toc, args.numbers)

if __name__ == "__main__":
    main()
