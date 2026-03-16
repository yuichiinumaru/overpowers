#!/usr/bin/env python3
import argparse

def is_signal(text, noise_keywords):
    text_lower = text.lower()
    for keyword in noise_keywords:
        if keyword.lower() in text_lower:
            return False
    return True

def main():
    parser = argparse.ArgumentParser(description="Filter out noise lines from text based on keywords.")
    parser.add_argument("--input", required=True, help="Input file")
    parser.add_argument("--noise-words", required=True, help="Comma-separated list of words that indicate noise")
    parser.add_argument("--output", help="Output file (default: stdout)")

    args = parser.parse_args()

    noise_keywords = [w.strip() for w in args.noise_words.split(",")]

    signals = []
    try:
        with open(args.input, "r") as f:
            for line in f:
                if line.strip() and is_signal(line, noise_keywords):
                    signals.append(line.rstrip())
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if args.output:
        with open(args.output, "w") as f:
            for s in signals:
                f.write(f"{s}\n")
        print(f"Filtered output saved to {args.output}")
    else:
        for s in signals:
            print(s)

if __name__ == "__main__":
    main()
