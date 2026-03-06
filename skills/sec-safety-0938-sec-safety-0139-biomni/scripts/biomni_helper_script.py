#!/usr/bin/env python3
import sys

def query_biomni(catalog_item):
    print(f"Querying Biomni catalog for: {catalog_item}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        query_biomni(sys.argv[1])
    else:
        print("Usage: ./biomni_query.py <catalog_item>")
