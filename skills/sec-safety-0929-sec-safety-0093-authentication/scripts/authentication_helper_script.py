#!/usr/bin/env python3
import sys

def test_auth(endpoint, method):
    print(f"Testing {method} authentication against endpoint {endpoint}")

if __name__ == '__main__':
    if len(sys.argv) == 3:
        test_auth(sys.argv[1], sys.argv[2])
    else:
        print("Usage: ./auth_tester.py <endpoint> <auth_method>")
