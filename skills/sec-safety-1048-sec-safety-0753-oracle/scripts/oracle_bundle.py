#!/usr/bin/env python3
"""
Helper script to bundle files for use with oracle CLI.
"""
import argparse
import os

def bundle_files(files, output_file):
    print(f"Bundling {len(files)} files into {output_file}...")
    with open(output_file, 'w') as out_f:
        for f in files:
            if os.path.isfile(f):
                out_f.write(f"--- File: {f} ---\n")
                with open(f, 'r') as in_f:
                    out_f.write(in_f.read())
                out_f.write("\n\n")
            else:
                print(f"Warning: File {f} not found.")

def main():
    parser = argparse.ArgumentParser(description="Oracle File Bundler Helper")
    parser.add_argument("--files", nargs='+', required=True, help="List of files to bundle")
    parser.add_argument("--output", type=str, default="bundled_payload.txt", help="Output bundled file")

    args = parser.parse_args()
    bundle_files(args.files, args.output)
    print(f"Bundled payload ready: {args.output}")

if __name__ == "__main__":
    main()
