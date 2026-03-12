#!/usr/bin/env python3
import os
import requests
import sys

class FREDQuery:
    """Helper class to query the FRED API."""
    
    BASE_URL = "https://api.stlouisfed.org/fred"

    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("FRED_API_KEY")
        if not self.api_key:
            print("Error: FRED_API_KEY environment variable not set.")
            sys.exit(1)

    def _get(self, endpoint, params=None):
        if params is None:
            params = {}
        params["api_key"] = self.api_key
        params["file_type"] = "json"
        
        response = requests.get(f"{self.BASE_URL}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

    def get_series(self, series_id):
        """Get series metadata."""
        return self._get("series", {"series_id": series_id})

    def get_observations(self, series_id, **kwargs):
        """Get observations for a series."""
        params = {"series_id": series_id}
        params.update(kwargs)
        return self._get("series/observations", params)

    def search_series(self, text, **kwargs):
        """Search for series."""
        params = {"search_text": text}
        params.update(kwargs)
        return self._get("series/search", params)

    def get_category(self, category_id=0):
        """Get category info."""
        return self._get("category", {"category_id": category_id})

    def get_category_series(self, category_id):
        """Get series in a category."""
        return self._get("category/series", {"category_id": category_id})

if __name__ == "__main__":
    # Quick test if run directly
    fred = FREDQuery()
    print("FRED Query Class initialized successfully.")
