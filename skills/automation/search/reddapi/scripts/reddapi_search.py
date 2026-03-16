#!/usr/bin/env python3
import urllib.request
import urllib.parse
import json
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Query Reddapi")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=10, help="Number of results to return")
    parser.add_argument("--subreddit", help="Filter by subreddit")
    parser.add_argument("--sort", choices=["relevance", "hot", "top", "new"], default="relevance", help="Sort order")

    args = parser.parse_args()

    base_url = "https://reddapi.dev/api/search"
    query_params = {"q": args.query, "limit": args.limit, "sort": args.sort}

    if args.subreddit:
        query_params["subreddit"] = args.subreddit

    url = f"{base_url}?{urllib.parse.urlencode(query_params)}"

    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))

        print(json.dumps(data, indent=2))

    except urllib.error.URLError as e:
        print(f"Error connecting to Reddapi: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
