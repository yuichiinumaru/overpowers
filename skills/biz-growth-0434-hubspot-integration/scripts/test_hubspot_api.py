#!/usr/bin/env python3
"""
HubSpot API Tester
A basic script to test a connection to the HubSpot API using a private app token.
"""
import sys
import argparse
import json
try:
    import urllib.request
    from urllib.error import URLError, HTTPError
except ImportError:
    print("Error: urllib module is missing. Please check your Python installation.")
    sys.exit(1)

def test_connection(token, object_type="contacts", limit=5):
    """
    Test connection to HubSpot API and fetch a few objects.
    """
    url = f"https://api.hubapi.com/crm/v3/objects/{object_type}?limit={limit}"

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    req = urllib.request.Request(url, headers=headers)

    print(f"Testing connection to HubSpot API: {url}...")

    try:
        with urllib.request.urlopen(req) as response:
            status_code = response.getcode()
            response_data = response.read()
            data = json.loads(response_data)

            print(f"Success! Status Code: {status_code}")
            print(f"Retrieved {len(data.get('results', []))} {object_type}.")

            for item in data.get('results', []):
                print(f" - ID: {item.get('id')}, Created: {item.get('createdAt')}")

    except HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        if e.code == 401:
            print("Tip: Check if your token is valid.")
        sys.exit(1)
    except URLError as e:
        print(f"URL Error: {e.reason}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="HubSpot API Connection Tester")
    parser.add_argument("--token", required=True, help="HubSpot Private App Token")
    parser.add_argument("--object", default="contacts", help="CRM Object to fetch (contacts, companies, deals). Default: contacts")
    parser.add_argument("--limit", type=int, default=5, help="Number of records to fetch (default: 5)")

    args = parser.parse_args()

    test_connection(args.token, args.object, args.limit)

if __name__ == "__main__":
    main()
