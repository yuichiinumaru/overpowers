#!/usr/bin/env python3
import argparse

def analyze(input_file):
    print(f"Analyzing sentiment in {input_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()
    analyze(args.input_file)
