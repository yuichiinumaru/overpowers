import argparse
import json
from duckduckgo_search import DDGS

def search_text(keywords, max_results=8):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(keywords, max_results=max_results):
            results.append(r)
    return results

def search_news(keywords, max_results=5):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.news(keywords, max_results=max_results):
            results.append(r)
    return results

def main():
    parser = argparse.ArgumentParser(description="DuckDuckGo Search CLI Helper")
    parser.add_argument("query", help="Search query or 'news' followed by query")
    parser.add_argument("keywords", nargs="?", help="Keywords for news search")
    parser.add_argument("--max", type=int, default=8, help="Maximum number of results (default: 8)")
    parser.add_argument("--format", choices=["json", "text"], default="json", help="Output format (default: json)")
    
    args = parser.parse_args()
    
    if args.query == "news" and args.keywords:
        results = search_news(args.keywords, max_results=args.max)
    else:
        # If 'news' is the only argument, it searches for 'news'
        # Otherwise, query is the keywords for text search
        query = args.query if args.query != "news" or not args.keywords else args.keywords
        results = search_text(query, max_results=args.max)
        
    if args.format == "json":
        print(json.dumps(results, indent=2))
    else:
        for i, r in enumerate(results, 1):
            print(f"{i}. {r.get('title')}")
            print(f"   URL: {r.get('href') or r.get('url')}")
            print(f"   Snippet: {r.get('body') or r.get('snippet')}")
            print()

if __name__ == "__main__":
    main()
