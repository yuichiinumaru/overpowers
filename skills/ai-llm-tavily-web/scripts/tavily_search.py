#!/usr/bin/env python3
import os
import sys
import requests

def tavily_search(query):
    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        print("Error: TAVILY_API_KEY environment variable not set.")
        return

    url = "https://api.tavily.com/search"
    payload = {
        "api_key": api_key,
        "query": query,
        "search_depth": "smart"
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        results = response.json()
        
        print(f"--- Results for: {query} ---")
        for result in results.get("results", []):
            print(f"Title: {result.get('title')}")
            print(f"URL: {result.get('url')}")
            print(f"Snippet: {result.get('content')[:200]}...")
            print("-" * 20)
            
    except Exception as e:
        print(f"Error during Tavily search: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: tavily_search.py <query>")
        sys.exit(1)
    
    tavily_search(" ".join(sys.argv[1:]))
