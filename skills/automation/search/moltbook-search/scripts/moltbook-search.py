#!/usr/bin/env python3
import sys
import argparse
import requests
import json

BASE_URL = "https://essencerouter.com/api/v1/moltbook"

def search(query, limit=10, tone=None, stance=None, time_range=None):
    url = f"{BASE_URL}/search"
    payload = {
        "query": query,
        "limit": limit,
        "filters": {}
    }
    if tone:
        payload["filters"]["tone"] = tone
    if stance:
        payload["filters"]["stance"] = stance
    if time_range:
        payload["filters"]["time_range"] = time_range

    try:
        response = requests.post(url, json=payload, timeout=15)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"success": False, "error": str(e)}

def main():
    parser = argparse.ArgumentParser(description="Search Moltbook posts.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=10, help="Max results")
    parser.add_argument("--tone", choices=["REFLECTIVE", "TECHNICAL", "PLAYFUL"], help="Filter by tone")
    parser.add_argument("--stance", choices=["ASSERT", "QUESTION", "SHARE"], help="Filter by stance")
    parser.add_argument("--time-range", help="Time range (e.g., 'today', 'last_7_days')")
    args = parser.parse_args()

    results = search(args.query, args.limit, args.tone, args.stance, args.time_range)
    
    if not results.get("results"):
        print("No results found.")
        if "error" in results:
            print(f"Error: {results['error']}")
        return

    print(f"Found {len(results['results'])} results for '{args.query}':\n")
    for i, res in enumerate(results["results"], 1):
        post = res["post"]
        dist = res["distillation"]
        print(f"{i}. [{post['author']}] in {post['submolt']} ({post['created_at']})")
        print(f"   Insight: {dist['core_insight']}")
        print(f"   URL: {post['url']}")
        print("-" * 40)

if __name__ == "__main__":
    main()
