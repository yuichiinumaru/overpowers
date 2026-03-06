#!/usr/bin/env python3
import argparse

def export(input_file, fmt):
    print(f"Exporting {input_file} to {fmt}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('--format', default='csv')
    args = parser.parse_args()
    export(args.input_file, args.format)
