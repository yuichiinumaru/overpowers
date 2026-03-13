#!/usr/bin/env python3
import os
import sys
import requests

class NotionClient:
    BASE_URL = "https://api.notion.com/v1"
    VERSION = "2025-09-03"

    def __init__(self, api_key=None):
        self.api_key = api_key or self._load_key()
        if not self.api_key:
            print("Error: Notion API key not found. Store it in ~/.config/notion/api_key")
            sys.exit(1)
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": self.VERSION,
            "Content-Type": "application/json"
        }

    def _load_key(self):
        path = os.path.expanduser("~/.config/notion/api_key")
        if os.path.exists(path):
            with open(path, "r") as f:
                return f.read().strip()
        return os.environ.get("NOTION_API_KEY")

    def search(self, query):
        url = f"{self.BASE_URL}/search"
        payload = {"query": query}
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def get_page(self, page_id):
        url = f"{self.BASE_URL}/pages/{page_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()

if __name__ == "__main__":
    client = NotionClient()
    print("Notion Client initialized successfully.")
