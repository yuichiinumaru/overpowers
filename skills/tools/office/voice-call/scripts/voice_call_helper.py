#!/usr/bin/env python3
"""
Voice Call Helper Script.
Provides testing and simulation for the voice-call plugin.
"""
import sys
import argparse

def initiate_call(to, message):
    print(f"Mock: Initiating voice call to {to}...")
    print(f"Message: {message}")
    print("Provider: mock")
    print("Call ID: call_abc123")
    print("Status: queued")

def get_status(call_id):
    print(f"Mock: Checking status for call {call_id}...")
    print("Status: completed")

def main():
    parser = argparse.ArgumentParser(description="Voice Call Helper")
    parser.add_argument("--call", metavar=('TO', 'MESSAGE'), nargs=2, help="Initiate a mock call")
    parser.add_argument("--status", metavar='CALL_ID', help="Check mock call status")

    args = parser.parse_args()

    if args.call:
        initiate_call(args.call[0], args.call[1])
    elif args.status:
        get_status(args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
