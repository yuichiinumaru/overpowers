#!/usr/bin/env python3
import sys

def test_cal_api(endpoint):
    print(f"Testing Cal.com API endpoint: {endpoint}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        test_cal_api(sys.argv[1])
    else:
        print("Usage: ./calcom_api_tester.py <endpoint>")
