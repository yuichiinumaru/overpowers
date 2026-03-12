#!/usr/bin/env python3
"""
ConvertKit (Kit) Helper Script

This script provides helper functions to interact with ConvertKit via Rube MCP
patterns as defined in the skill documentation.

Usage:
  python3 convertkit_helper.py --action list_subscribers [--email user@example.com]
  python3 convertkit_helper.py --action tag_subscriber --subscriber-id 123 --tag-id 456
  python3 convertkit_helper.py --action list_broadcasts
"""

import argparse
import sys
import json

def get_base_payload(tool_name):
    return {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "rube/call_tool",
        "params": {
            "name": tool_name,
            "arguments": {}
        }
    }

def print_mcp_instruction(payload):
    print("Execute the following payload via Rube MCP:")
    print(json.dumps(payload, indent=2))
    print("\nNote: Use the appropriate client command to send this payload.")

def list_subscribers(args):
    payload = get_base_payload("KIT_LIST_SUBSCRIBERS")
    if args.email:
        payload["params"]["arguments"]["email_address"] = args.email
    if args.status:
        payload["params"]["arguments"]["status"] = args.status
    payload["params"]["arguments"]["per_page"] = args.per_page

    print_mcp_instruction(payload)

def tag_subscriber(args):
    if not args.subscriber_id or not args.tag_id:
        print("Error: --subscriber-id and --tag-id are required for tagging.")
        sys.exit(1)

    payload = get_base_payload("KIT_TAG_SUBSCRIBER")
    payload["params"]["arguments"]["subscriber_id"] = args.subscriber_id
    payload["params"]["arguments"]["tag_id"] = args.tag_id

    print_mcp_instruction(payload)

def list_broadcasts(args):
    payload = get_base_payload("KIT_LIST_BROADCASTS")
    payload["params"]["arguments"]["per_page"] = args.per_page
    if args.include_count:
        payload["params"]["arguments"]["include_total_count"] = "true"

    print_mcp_instruction(payload)

def main():
    parser = argparse.ArgumentParser(description="ConvertKit Automation Helper")
    parser.add_argument("--action", required=True, choices=["list_subscribers", "tag_subscriber", "list_broadcasts"])
    parser.add_argument("--email", help="Email address to search for")
    parser.add_argument("--status", choices=["active", "inactive", "cancelled"], help="Filter by status")
    parser.add_argument("--subscriber-id", type=int, help="Subscriber ID for tagging")
    parser.add_argument("--tag-id", type=int, help="Tag ID for tagging")
    parser.add_argument("--per-page", type=int, default=50, help="Results per page (1-500)")
    parser.add_argument("--include-count", action="store_true", help="Include total count in response")

    args = parser.parse_args()

    if args.action == "list_subscribers":
        list_subscribers(args)
    elif args.action == "tag_subscriber":
        tag_subscriber(args)
    elif args.action == "list_broadcasts":
        list_broadcasts(args)

if __name__ == "__main__":
    main()
