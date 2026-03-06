#!/usr/bin/env python3
# forecast.py
import argparse
import json
import urllib.request
import sys

def get_forecast(plz, days, return_json=False):
    url = f"https://www.meteoschweiz.admin.ch/product/output/forecast-chart/{plz}00.json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))

        if return_json:
            print(json.dumps(data, indent=2))
        else:
            print(f"Forecast for {plz}:")
            for day in data[:days]:
                print(f"Date: {day['date']}")
                print(f"Temp: {day['tempMin']} - {day['tempMax']} °C")
                print(f"Precip: {day['precipitation']} mm")
                print("---")
    except Exception as e:
        print(f"Failed to get forecast for {plz}. Note that some PLZs might not be found. Exception: {e}")
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="MeteoSwiss forecast")
    parser.add_argument("plz", help="Swiss postal code")
    parser.add_argument("--days", type=int, default=7, help="Number of days for forecast")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    get_forecast(args.plz, args.days, args.json)
