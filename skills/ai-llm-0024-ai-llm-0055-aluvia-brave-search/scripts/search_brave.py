import os
import sys
import requests
import argparse

def search(query, count=5):
    brave_api_key = os.environ.get("BRAVE_API_KEY")
    aluvia_api_key = os.environ.get("ALUVIA_API_KEY")
    
    if not brave_api_key:
        print("Error: BRAVE_API_KEY not set")
        return
    
    # Base implementation for Brave Search
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": brave_api_key
    }
    params = {"q": query, "count": count}
    
    # Note: Aluvia proxy logic would be integrated here if using Aluvia's SDK or proxy endpoint
    # Since specific Aluvia integration details are not provided in SKILL.md, 
    # we provide the standard Brave API call structure.
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        results = data.get("web", {}).get("results", [])
        
        if not results:
            print(f"No results found for '{query}'.")
            return

        for i, res in enumerate(results, 1):
            print(f"--- Result {i} ---")
            print(f"Title: {res.get('title')}")
            print(f"Link: {res.get('url')}")
            print(f"Snippet: {res.get('description')}\n")
            
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search web using Brave Search API')
    parser.add_argument('query', help='Search query')
    parser.add_argument('-n', '--number', type=int, default=5, help='Number of results')
    
    args = parser.parse_args()
    search(args.query, args.number)
