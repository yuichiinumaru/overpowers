#!/usr/bin/env python3
import sys

def sync_bamboohr(entity_type):
    print(f"Triggering sync for BambooHR entity: {entity_type}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sync_bamboohr(sys.argv[1])
    else:
        print("Usage: ./bamboohr_sync.py <entity_type>")
