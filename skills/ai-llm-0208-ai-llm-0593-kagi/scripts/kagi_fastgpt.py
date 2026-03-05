import argparse
import json
from kagi_client import KagiClient

def main():
    parser = argparse.ArgumentParser(description='Ask FastGPT (LLM + web search)')
    parser.add_argument('query', help='Question or topic to summarize')
    parser.add_argument('--cache', type=bool, default=True, help='Enable/disable API cache (default: True)')
    parser.add_argument('--json', action='store_true', help='Output raw JSON data')
    
    args = parser.parse_args()
    
    try:
        client = KagiClient()
        results = client.fastgpt(args.query, args.cache)
        
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print(f"\n🧠 Kagi FastGPT Answer for: '{args.query}'\n")
            if 'data' in results:
                answer = results['data'].get('output', 'No answer generated.')
                references = results['data'].get('references', [])
                
                print(answer)
                
                if references:
                    print("\n📚 References:")
                    for idx, ref in enumerate(references, 1):
                        title = ref.get('title', 'No Title')
                        url = ref.get('url', 'No URL')
                        print(f"[{idx}] {title} - {url}")
                print()
            else:
                print("No results found.")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
