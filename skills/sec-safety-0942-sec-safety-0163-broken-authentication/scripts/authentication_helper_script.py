#!/usr/bin/env python3
import sys

def fuzz_auth(login_endpoint):
    print(f"Running broken authentication tests against: {login_endpoint}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fuzz_auth(sys.argv[1])
    else:
        print("Usage: ./broken_auth_fuzzer.py <login_endpoint>")
