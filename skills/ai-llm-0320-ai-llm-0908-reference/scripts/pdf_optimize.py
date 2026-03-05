import os
import subprocess
import argparse

def run_qpdf(args):
    try:
        result = subprocess.run(["qpdf"] + args, capture_output=True, text=True)
        if result.returncode == 0:
            print("Operation successful.")
            return True
        else:
            print(f"Error: {result.stderr}")
            return False
    except FileNotFoundError:
        print("Error: qpdf command not found. Please install qpdf.")
        return False

def main():
    parser = argparse.ArgumentParser(description="PDF Optimization and Repair Utility")
    parser.add_argument("input", help="Input PDF file")
    parser.add_argument("--output", help="Output PDF file")
    parser.add_argument("--linearize", action="store_true", help="Optimize for web (linearize)")
    parser.add_argument("--compress", action="store_true", help="Compress PDF")
    parser.add_argument("--repair", action="store_true", help="Attempt to repair corrupted PDF")
    
    args = parser.parse_args()
    
    if not args.output:
        base, ext = os.path.splitext(args.input)
        args.output = f"{base}_optimized{ext}"
        
    qpdf_args = [args.input]
    
    if args.linearize:
        qpdf_args.append("--linearize")
        
    if args.compress:
        qpdf_args.extend(["--optimize-level=all"])
        
    if args.repair:
        # qpdf automatically attempts repair on open
        pass
        
    qpdf_args.append(args.output)
    
    run_qpdf(qpdf_args)

if __name__ == "__main__":
    main()
