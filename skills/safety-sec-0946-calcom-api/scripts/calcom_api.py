import os
import requests
import json
import argparse
import sys

CALCOM_API_URL = "https://api.cal.com/v2"

def get_headers(api_key):
    if not api_key:
        print("Error: CALCOM_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

def get_bookings(api_key, status=None, after_start=None):
    params = {}
    if status:
        params['status'] = status
    if after_start:
        params['afterStart'] = after_start
    response = requests.get(f"{CALCOM_API_URL}/bookings", headers=get_headers(api_key), params=params)
    response.raise_for_status()
    return response.json()

def main():
    parser = argparse.ArgumentParser(description="Cal.com API v2 Helper Script")
    parser.add_argument("--api-key", default=os.getenv("CALCOM_API_KEY"), help="Cal.com API Key (or set CALCOM_API_KEY env var)")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    bookings_parser = subparsers.add_parser("bookings", help="List bookings")
    bookings_parser.add_argument("--status", help="Filter by booking status")
    bookings_parser.add_argument("--after-start", help="Filter bookings after this date (ISO 8601)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        if args.command == "bookings":
            result = get_bookings(args.api_key, args.status, args.after_start)
            print(json.dumps(result, indent=2))
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}", file=sys.stderr)
        if hasattr(e, 'response') and e.response is not None:
            print(e.response.text, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
