#!/usr/bin/env python3
import sys

def init_benchling(api_key):
    print(f"Initializing Benchling SDK client with provided key.")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        init_benchling(sys.argv[1])
    else:
        print("Usage: ./benchling_client.py <api_key>")
