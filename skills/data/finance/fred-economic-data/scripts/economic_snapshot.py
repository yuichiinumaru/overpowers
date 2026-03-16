#!/usr/bin/env python3
import os
import sys
import requests

def get_snapshot():
    api_key = os.environ.get("FRED_API_KEY")
    if not api_key:
        print("Error: FRED_API_KEY environment variable not set.")
        return

    indicators = {
        "GDP": "Gross Domestic Product",
        "UNRATE": "Unemployment Rate (%)",
        "CPIAUCSL": "CPI (All Urban Consumers)",
        "FEDFUNDS": "Federal Funds Effective Rate (%)",
        "DGS10": "10-Year Treasury Constant Maturity (%)",
        "SP500": "S&P 500"
    }

    print(f"{'Series ID':<10} | {'Value':<10} | {'Date':<12} | {'Description'}")
    print("-" * 70)

    for sid, desc in indicators.items():
        url = "https://api.stlouisfed.org/fred/series/observations"
        params = {
            "api_key": api_key,
            "series_id": sid,
            "file_type": "json",
            "limit": 1,
            "sort_order": "desc"
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            if data.get('observations'):
                latest = data['observations'][0]
                print(f"{sid:<10} | {latest['value']:<10} | {latest['date']:<12} | {desc}")
            else:
                print(f"{sid:<10} | {'N/A':<10} | {'N/A':<12} | {desc}")
        except Exception as e:
            print(f"{sid:<10} | Error fetching data")

if __name__ == "__main__":
    get_snapshot()
