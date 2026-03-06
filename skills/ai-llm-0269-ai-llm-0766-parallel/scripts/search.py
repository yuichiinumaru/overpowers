#!/usr/bin/env python3
import argparse
import json
import os
import sys

try:
    from parallel import Parallel
except ImportError:
    print("Error: parallel-web package not installed. Run 'pip install parallel-web'", file=sys.stderr)
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Search via Parallel.ai API")
    parser.add_argument("query", help="The search objective")
    parser.add_argument("--max-results", type=int, default=10, help="Maximum number of results to return")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    api_key = os.environ.get("PARALLEL_API_KEY")
    if not api_key:
        print("Error: PARALLEL_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    client = Parallel(api_key=api_key)

    try:
        response = client.beta.search(
            mode="one-shot",
            max_results=args.max_results,
            objective=args.query
        )

        if args.json:
            print(json.dumps(response, indent=2))
        else:
            for i, result in enumerate(response.get('results', [])):
                print(f"--- Result {i+1} ---")
                print(f"Title: {result.get('title')}")
                print(f"URL: {result.get('url')}")
                print(f"Excerpts: {' '.join(result.get('excerpts', []))}")
                print()
    except Exception as e:
        print(f"Search failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
