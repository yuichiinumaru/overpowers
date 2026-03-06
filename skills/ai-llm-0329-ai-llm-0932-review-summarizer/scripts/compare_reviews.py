#!/usr/bin/env python3
import argparse

def compare(files):
    print(f"Comparing reviews from {files}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+')
    args = parser.parse_args()
    compare(args.files)
