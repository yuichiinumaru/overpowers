import os
import requests
import json
import argparse

class ReddapiClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("REDDAPI_API_KEY")
        self.base_url = "https://reddapi.dev/api/v1"
        if not self.api_key:
            raise ValueError("REDDAPI_API_KEY environment variable is not set")

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def semantic_search(self, query, limit=100):
        url = f"{self.base_url}/search/semantic"
        data = {"query": query, "limit": limit}
        response = requests.post(url, headers=self._get_headers(), json=data)
        response.raise_for_status()
        return response.json()

    def get_trends(self):
        url = f"{self.base_url}/trends"
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def get_subreddits(self, limit=100):
        url = f"{self.base_url.replace('/v1', '')}/subreddits"
        params = {"limit": limit}
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()

def main():
    parser = argparse.ArgumentParser(description="Reddapi CLI Helper")
    parser.add_argument("--search", help="Perform semantic search")
    parser.add_argument("--trends", action="store_true", help="Get trending topics")
    parser.add_argument("--limit", type=int, default=10, help="Limit results")
    
    args = parser.parse_args()
    
    try:
        client = ReddapiClient()
        
        if args.search:
            results = client.semantic_search(args.search, args.limit)
            print(json.dumps(results, indent=2))
            
        if args.trends:
            results = client.get_trends()
            print(json.dumps(results, indent=2))
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
