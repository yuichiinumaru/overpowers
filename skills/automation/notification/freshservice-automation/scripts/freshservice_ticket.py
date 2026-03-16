#!/usr/bin/env python3
"""
Freshservice Ticket Helper
Generates Rube MCP payloads for creating tickets in Freshservice.

Usage:
  python3 freshservice_ticket.py --subject "Network Down" --desc "No internet access" --email "user@example.com" --priority 3
"""

import argparse
import json

def generate_payload(args):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "rube/call_tool",
        "params": {
            "name": "FRESHSERVICE_CREATE_TICKET",
            "arguments": {
                "subject": args.subject,
                "description": args.desc,
                "status": args.status,
                "priority": args.priority,
                "email": args.email,
                "type": args.type
            }
        }
    }
    print("Execute the following payload via Rube MCP:")
    print(json.dumps(payload, indent=2))
    print("\nNote: Status 2=Open. Priority: 1=Low, 2=Medium, 3=High, 4=Urgent")

def main():
    parser = argparse.ArgumentParser(description="Freshservice Ticket Generator Helper")
    parser.add_argument("--subject", required=True, help="Ticket subject")
    parser.add_argument("--desc", required=True, help="Ticket description (HTML supported)")
    parser.add_argument("--email", required=True, help="Requester's email")
    parser.add_argument("--status", type=int, default=2, help="Status code (default: 2)")
    parser.add_argument("--priority", type=int, default=2, help="Priority code (default: 2)")
    parser.add_argument("--type", default="Incident", help="Ticket type (Incident or Service Request)")

    args = parser.parse_args()
    generate_payload(args)

if __name__ == "__main__":
    main()
