import os
import requests
import sys
import json

class KagiClient:
    def __init__(self, token=None):
        self.token = token or os.environ.get('KAGI_API_TOKEN')
        if not self.token:
            print("Error: KAGI_API_TOKEN environment variable not set.")
            sys.exit(1)
        self.base_url = "https://kagi.com/api/v0"
        self.headers = {"Authorization": f"Bot {self.token}"}

    def search(self, query, limit=10):
        url = f"{self.base_url}/search"
        params = {"q": query, "limit": limit}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def fastgpt(self, query, cache=True):
        url = f"{self.base_url}/fastgpt"
        data = {"query": query, "cache": cache}
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    # Test client
    client = KagiClient()
    print("Kagi Client initialized successfully.")
