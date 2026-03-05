import sys
import json
import argparse
import os
from parallel import Parallel

def main():
    parser = argparse.ArgumentParser(description="Search the web via Parallel.ai API.")
    parser.add_argument("query", help="The search query.")
    parser.add_argument("--max-results", type=int, default=10, help="Maximum number of results to return.")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format.")
    parser.add_argument("--api-key", help="Parallel.ai API key (overrides PARALLEL_API_KEY env var).")

    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("PARALLEL_API_KEY")
    if not api_key:
        print("Error: PARALLEL_API_KEY environment variable is not set.")
        sys.exit(1)

    try:
        client = Parallel(api_key=api_key)
        
        response = client.beta.search(
            mode="one-shot",
            max_results=args.max_results,
            objective=args.query
        )

        if args.json:
            # Check if response is a dict or a Pydantic model (many SDKs use Pydantic)
            if hasattr(response, 'model_dump'):
                print(json.dumps(response.model_dump(), indent=2))
            elif hasattr(response, 'to_dict'):
                print(json.dumps(response.to_dict(), indent=2))
            else:
                print(json.dumps(response, indent=2))
        else:
            # Handle both dict and object responses
            results = response.get("results") if isinstance(response, dict) else getattr(response, 'results', [])
            
            print(f"Search Results for: {args.query}\n")
            for i, result in enumerate(results, 1):
                title = result.get('title') if isinstance(result, dict) else getattr(result, 'title', 'No Title')
                url = result.get('url') if isinstance(result, dict) else getattr(result, 'url', 'No URL')
                excerpts = result.get('excerpts') if isinstance(result, dict) else getattr(result, 'excerpts', [])
                
                print(f"{i}. {title}")
                print(f"   URL: {url}")
                if excerpts:
                    excerpt = excerpts[0] if isinstance(excerpts, list) and excerpts else ""
                    print(f"   Excerpt: {excerpt[:200]}...")
                print()
            
            usage = response.get("usage") if isinstance(response, dict) else getattr(response, 'usage', 'N/A')
            print(f"API Usage: {usage}")

    except ImportError:
        print("Error: 'parallel-web' package not found. Please install it with: pip install parallel-web")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
