#!/usr/bin/env python3
# current_weather.py
import argparse
import json
import urllib.request
import sys
import csv

def fetch_weather(station, return_json=False):
    url = "https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv"
    try:
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8').splitlines()
        reader = csv.DictReader(content, delimiter=';')
        data = None
        for row in reader:
            if row['stn'].upper() == station.upper():
                data = row
                break

        if not data:
            print(f"Station {station} not found or no data available.")
            sys.exit(1)

        if return_json:
            print(json.dumps(data, indent=2))
        else:
            print(f"Station: {data['stn']}")
            print(f"Time: {data['time']}")
            print(f"Temperature (°C)........................ {data.get('tre200s0', 'N/A')}")
            print(f"Rel. humidity (%)...................... {data.get('ure200s0', 'N/A')}")
            print(f"Wind speed (km/h)...................... {data.get('fu3010z0', 'N/A')}")
            print(f"Precipitation (mm)..................... {data.get('rre150z0', 'N/A')}")
    except Exception as e:
        print(f"Failed to fetch weather data: {e}")
        sys.exit(1)

def list_stations():
    url = "https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/info/stations.json"
    try:
        response = urllib.request.urlopen(url)
        content = json.loads(response.read().decode('utf-8'))
        print("Available stations:")
        for station in content:
            print(station['id'])
    except Exception as e:
        print(f"Failed to fetch station list: {e}")
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="MeteoSwiss current weather")
    parser.add_argument("--station", help="Station code (e.g. RAG, ZRH)")
    parser.add_argument("--list", action="store_true", help="List all available stations")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    args = parser.parse_args()

    if args.list:
        list_stations()
    elif args.station:
        fetch_weather(args.station, args.json)
    else:
        parser.print_help()
