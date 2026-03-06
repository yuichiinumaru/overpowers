#!/usr/bin/env python3
"""
Python Client Wrapper for VectCutAPI.
"""
import requests

class VectCutClient:
    def __init__(self, base_url="http://localhost:9001"):
        self.base_url = base_url

    def create_draft(self, width=1080, height=1920):
        res = requests.post(f"{self.base_url}/create_draft", json={"width": width, "height": height})
        if res.ok:
            return res.json().get("output", {}).get("draft_id")
        return None

    def save_draft(self, draft_id):
        res = requests.post(f"{self.base_url}/save_draft", json={"draft_id": draft_id})
        if res.ok:
            return res.json().get("output", {}).get("draft_url")
        return None

if __name__ == "__main__":
    print("VectCutAPI Client Library")
