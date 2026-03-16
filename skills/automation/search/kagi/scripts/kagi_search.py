import argparse
import json
from kagi_client import KagiClient

def main():
    parser = argparse.ArgumentParser(description='Search web using Kagi Search API')
    parser.add_argument('query', help='Search query')
    parser.add_argument('--limit', type=int, default=10, help='Maximum number of results (default: 10)')
    parser.add_argument('--json', action='store_true', help='Output raw JSON data')
    
    args = parser.parse_args()
    
    try:
        client = KagiClient()
        results = client.search(args.query, args.limit)
        
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print(f"\n🔍 Kagi Search Results for: '{args.query}'\n")
            if 'data' in results:
                for idx, item in enumerate(results['data'], 1):
                    title = item.get('title', 'No Title')
                    url = item.get('url', 'No URL')
                    snippet = item.get('snippet', 'No snippet available.')
                    print(f"{idx}. {title}")
                    print(f"   URL: {url}")
                    print(f"   {snippet}\n")
            else:
                print("No results found.")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
