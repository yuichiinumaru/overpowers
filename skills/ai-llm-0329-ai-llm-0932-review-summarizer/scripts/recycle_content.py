#!/usr/bin/env python3
import argparse

def recycle(input_file):
    print(f"Recycling content from {input_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    args = parser.parse_args()
    recycle(args.input)
