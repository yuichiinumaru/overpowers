#!/usr/bin/env python3
import os
import sys
import json
import requests
import pandas as pd

def get_fred_series(series_id, output_file=None):
    api_key = os.environ.get("FRED_API_KEY")
    if not api_key:
        print("Error: FRED_API_KEY environment variable not set.")
        sys.exit(1)

    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "api_key": api_key,
        "series_id": series_id,
        "file_type": "json"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        observations = data.get('observations', [])
        if not observations:
            print(f"No data found for series {series_id}")
            return

        if output_file:
            if output_file.endswith('.csv'):
                df = pd.DataFrame(observations)
                df.to_csv(output_file, index=False)
                print(f"Exported {len(observations)} observations to {output_file}")
            else:
                with open(output_file, 'w') as f:
                    json.dump(data, f, indent=2)
                print(f"Exported data to {output_file}")
        else:
            print(json.dumps(data, indent=2))

    except Exception as e:
        print(f"Error fetching data from FRED: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: get_fred_series.py <SERIES_ID> [output_file.csv|json]")
        sys.exit(1)
    
    series = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else None
    get_fred_series(series, output)
