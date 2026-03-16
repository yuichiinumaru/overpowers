#!/usr/bin/env python3
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Fetch news for aggregator skill")
    parser.add_argument("--topic", help="Topic to fetch news for", default="general")
    parser.add_argument("--limit", type=int, default=10, help="Number of articles to fetch")
    args = parser.parse_args()

    print(f"Fetching {args.limit} news articles for topic '{args.topic}'...", file=sys.stderr)
    print("Fetched successfully.")

if __name__ == "__main__":
    main()
