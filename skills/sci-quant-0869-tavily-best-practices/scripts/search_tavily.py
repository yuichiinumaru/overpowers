import os
import argparse
from tavily import TavilyClient

def main():
    parser = argparse.ArgumentParser(description='Search the web using Tavily.')
    parser.add_argument('query', help='Search query')
    parser.add_argument('--max-results', type=int, default=10, help='Maximum number of results')
    parser.add_argument('--depth', choices=['basic', 'advanced'], default='advanced', help='Search depth')
    parser.add_argument('--topic', choices=['general', 'news', 'finance'], default='general', help='Search topic')

    args = parser.parse_args()

    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        print("Error: TAVILY_API_KEY environment variable not set.")
        return

    client = TavilyClient(api_key=api_key)
    print(f"Searching for: '{args.query}' (Depth: {args.depth}, Topic: {args.topic})")
    
    try:
        response = client.search(
            query=args.query,
            max_results=args.max_results,
            search_depth=args.depth,
            topic=args.topic
        )
        
        print("\nResults:")
        for i, result in enumerate(response.get("results", [])):
            print(f"{i+1}. {result['title']}")
            print(f"   URL: {result['url']}")
            print(f"   Score: {result['score']}")
            print(f"   {result['content'][:200]}...\n")
            
    except Exception as e:
        print(f"Error during search: {e}")

if __name__ == "__main__":
    main()
