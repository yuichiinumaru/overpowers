#!/usr/bin/env python3
import sys
from duckduckgo_search import DDGS

def search_x(query: str, max_results: int = 5) -> list[dict]:
    search_query = f"site:x.com OR site:twitter.com {query}"
    with DDGS() as ddgs:
        results = list(ddgs.text(search_query, max_results=max_results))
        return [
            {
                "title": r.get("title", ""),
                "snippet": r.get("body", ""),
                "url": r.get("href", ""),
                "source": "X"
            }
            for r in results
        ]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(search_x(sys.argv[1]))
    else:
        print("Usage: python3 search_x.py <query>")
