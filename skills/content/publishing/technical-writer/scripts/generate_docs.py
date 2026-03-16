#!/usr/bin/env python3
import argparse

def generate_doc(doc_type):
    print(f"Generating technical documentation template: {doc_type}")
    if doc_type == "README":
        print("# Project Title\n## Installation\n## Usage")
    elif doc_type == "API":
        print("# API Reference\n## Endpoints\n## Authentication")

def main():
    parser = argparse.ArgumentParser(description="Technical Writer Tools")
    parser.add_argument("--type", choices=["README", "API"], required=True)
    args = parser.parse_args()
    generate_doc(args.type)

if __name__ == "__main__":
    main()
