#!/usr/bin/env python3
"""
Helper script to interact with the Moltbook search API.
"""
import requests
import json
import argparse
import sys

API_BASE = "https://essencerouter.com/api/v1/moltbook"

def search(query, limit=10, tone=None, stance=None, time_range=None, explain=False):
    url = f"{API_BASE}/search"

    payload = {
        "query": query,
        "limit": limit
    }

    filters = {}
    if tone:
        filters["tone"] = tone
    if stance:
        filters["stance"] = stance
    if time_range:
        filters["time_range"] = time_range

    if filters:
        payload["filters"] = filters

    if explain:
        payload["explain"] = True

    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            json=payload
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling Moltbook API: {e}", file=sys.stderr)
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response body: {e.response.text}", file=sys.stderr)
        return None

def display_results(results):
    if not results or "posts" not in results:
        print("No results found or invalid response.")
        return

    print(f"Found {results.get('total', 0)} matches (showing {len(results['posts'])})")
    print("-" * 80)

    for i, post in enumerate(results["posts"], 1):
        author = post.get("author", "Unknown")
        submolt = post.get("submolt", "general")
        score = post.get("score", 0)
        date = post.get("created_at", "")[:10]

        # Format the distillation info if available
        distill = post.get("distillation", {})
        insight = distill.get("core_insight", "")
        p_tone = distill.get("tone", "")
        p_stance = distill.get("stance", "")

        print(f"{i}. [{submolt}] {author} (Score: {score}, Date: {date})")
        print(f"   Tone: {p_tone} | Stance: {p_stance}")

        # Print content (truncate if too long)
        content = post.get("content", "").replace('\n', ' ')
        if len(content) > 150:
            content = content[:147] + "..."
        print(f"   Content: {content}")

        if insight:
            print(f"   Insight: {insight}")

        print("-" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search Moltbook posts")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=10, help="Number of results to return")
    parser.add_argument("--tone", choices=["REFLECTIVE", "TECHNICAL", "PLAYFUL"], help="Filter by tone")
    parser.add_argument("--stance", choices=["ASSERT", "QUESTION", "SHARE"], help="Filter by stance")
    parser.add_argument("--time", choices=["last_24_hours", "last_7_days", "last_30_days", "all_time"], help="Time range")
    parser.add_argument("--explain", action="store_true", help="Include scoring explanations")
    parser.add_argument("--raw", action="store_true", help="Output raw JSON instead of formatted text")

    args = parser.parse_args()

    results = search(
        args.query,
        limit=args.limit,
        tone=args.tone,
        stance=args.stance,
        time_range=args.time,
        explain=args.explain
    )

    if results:
        if args.raw:
            print(json.dumps(results, indent=2))
        else:
            display_results(results)
