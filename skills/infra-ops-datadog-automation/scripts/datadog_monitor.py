#!/usr/bin/env python3
"""
Datadog Monitor Helper
Generates Rube MCP payloads for common Datadog monitor configurations.

Usage:
  python3 datadog_monitor.py --name "High CPU" --query "avg(last_5m):avg:system.cpu.user{env:prod} > 90" --message "@slack-alerts CPU is high"
"""

import argparse
import json

def generate_monitor_payload(args):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "rube/call_tool",
        "params": {
            "name": "DATADOG_CREATE_MONITOR",
            "arguments": {
                "name": args.name,
                "type": "metric alert",
                "query": args.query,
                "message": args.message,
                "tags": ["env:prod", "managed_by:script"]
            }
        }
    }

    print("Execute the following payload via Rube MCP:")
    print(json.dumps(payload, indent=2))

def main():
    parser = argparse.ArgumentParser(description="Datadog Monitor Creator Helper")
    parser.add_argument("--name", required=True, help="Monitor name")
    parser.add_argument("--query", required=True, help="Datadog monitor query")
    parser.add_argument("--message", required=True, help="Notification message (e.g. @slack-channel)")

    args = parser.parse_args()
    generate_monitor_payload(args)

if __name__ == "__main__":
    main()
