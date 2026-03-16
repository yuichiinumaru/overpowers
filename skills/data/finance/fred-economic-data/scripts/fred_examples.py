#!/usr/bin/env python3
from fred_query import FREDQuery
import os

def run_examples():
    fred = FREDQuery()
    
    print("--- Example 1: Get Series Info (GDP) ---")
    gdp_info = fred.get_series("GDP")
    print(f"Title: {gdp_info['seriess'][0]['title']}")
    print(f"Units: {gdp_info['seriess'][0]['units']}")
    
    print("\n--- Example 2: Get Latest Observations (Unemployment Rate) ---")
    unrate = fred.get_observations("UNRATE", limit=5, sort_order="desc")
    for obs in unrate['observations']:
        print(f"Date: {obs['date']}, Value: {obs['value']}%")
        
    print("\n--- Example 3: Search for Inflation Series ---")
    results = fred.search_series("consumer price index", limit=3)
    for series in results['seriess']:
        print(f"ID: {series['id']}, Title: {series['title']}")

if __name__ == "__main__":
    if "FRED_API_KEY" not in os.environ:
        print("Please set FRED_API_KEY environment variable to run examples.")
    else:
        run_examples()
