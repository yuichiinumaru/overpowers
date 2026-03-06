#!/usr/bin/env python3
import argparse

def compare_prices(keyword):
    print(f"Comparing prices for {keyword}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--keyword')
    args = parser.parse_args()
    compare_prices(args.keyword)
