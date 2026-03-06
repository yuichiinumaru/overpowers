#!/usr/bin/env python3
import sys

def test_brightdata(target_url):
    print(f"Testing BrightData proxy/scraping connection against: {target_url}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test_brightdata(sys.argv[1])
    else:
        print("Usage: ./brightdata_tester.py <target_url>")
