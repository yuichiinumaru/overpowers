#!/usr/bin/env python3
import sys

def sync_cal(event_id):
    print(f"Syncing Cal.com event ID: {event_id}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sync_cal(sys.argv[1])
    else:
        print("Usage: ./cal_sync.py <event_id>")
