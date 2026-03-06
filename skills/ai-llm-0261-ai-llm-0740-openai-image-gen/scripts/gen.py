#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=1)
    parser.add_argument("--model")
    parser.add_argument("--prompt")
    parser.add_argument("--size")
    parser.add_argument("--quality")
    parser.add_argument("--out-dir")
    parser.add_argument("--background")
    parser.add_argument("--output-format")
    parser.add_argument("--style")

    args, unknown = parser.parse_known_args()
    print(f"Generating image with model {args.model}")

if __name__ == "__main__":
    main()
