import os
import time
import argparse
from tavily import TavilyClient

def main():
    parser = argparse.ArgumentParser(description='Conduct AI-powered research using Tavily.')
    parser.add_argument('topic', help='Research topic or input')
    parser.add_argument('--model', choices=['mini', 'pro', 'auto'], default='auto', help='Research model')

    args = parser.parse_args()

    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        print("Error: TAVILY_API_KEY environment variable not set.")
        return

    client = TavilyClient(api_key=api_key)
    print(f"Starting research on: '{args.topic}' using model '{args.model}'...")
    
    try:
        result = client.research(
            input=args.topic,
            model=args.model
        )
        
        request_id = result.get("request_id")
        if not request_id:
            print("Failed to get request ID.")
            return
            
        print(f"Research started. Request ID: {request_id}")
        print("Polling for completion...")
        
        while True:
            response = client.get_research(request_id)
            status = response.get("status")
            print(f"Status: {status}")
            
            if status in ["completed", "failed"]:
                break
            time.sleep(5)
            
        if response.get("status") == "completed":
            print("\n=== Research Report ===")
            print(response.get("content"))
        else:
            print(f"\nResearch failed: {response}")
            
    except Exception as e:
        print(f"Error during research: {e}")

if __name__ == "__main__":
    main()
