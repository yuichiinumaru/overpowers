import os
import argparse
from tavily import TavilyClient

def main():
    parser = argparse.ArgumentParser(description='Extract content from URLs using Tavily.')
    parser.add_argument('urls', nargs='+', help='URLs to extract content from')
    parser.add_argument('--query', help='Optional query to rerank chunks by relevance')
    parser.add_argument('--chunks', type=int, default=3, help='Chunks per source (default: 3)')

    args = parser.parse_args()

    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        print("Error: TAVILY_API_KEY environment variable not set.")
        return

    client = TavilyClient(api_key=api_key)
    print(f"Extracting content from {len(args.urls)} URLs...")
    
    try:
        response = client.extract(
            urls=args.urls,
            query=args.query,
            chunks_per_source=args.chunks
        )
        
        print("\nExtracted Content:")
        for result in response.get("results", []):
            print(f"--- Source: {result.get('url')} ---")
            print(result.get('raw_content', 'No content extracted.')[:500] + "...\n")
            
    except Exception as e:
        print(f"Error during extraction: {e}")

if __name__ == "__main__":
    main()
