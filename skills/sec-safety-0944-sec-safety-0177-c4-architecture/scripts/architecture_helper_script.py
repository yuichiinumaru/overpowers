#!/usr/bin/env python3
import sys

def generate_c4(structurizr_file):
    print(f"Generating C4 Architecture diagram from: {structurizr_file}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        generate_c4(sys.argv[1])
    else:
        print("Usage: ./c4_generator.py <structurizr_file>")
