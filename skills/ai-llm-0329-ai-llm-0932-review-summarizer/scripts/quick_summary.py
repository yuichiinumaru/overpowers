#!/usr/bin/env python3
import argparse

def summarize(input_file):
    print(f"Generating quick summary for {input_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()
    summarize(args.input_file)
