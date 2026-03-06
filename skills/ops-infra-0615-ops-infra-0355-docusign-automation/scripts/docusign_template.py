#!/usr/bin/env python3
"""
DocuSign Automation Helper
Generates Rube MCP payloads for common DocuSign workflows like creating an envelope from a template.

Usage:
  python3 docusign_template.py --template-id "1234-abcd" --role-name "Signer 1" --name "Jane Doe" --email "jane@example.com"
"""

import argparse
import json

def generate_envelope_payload(args):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "rube/call_tool",
        "params": {
            "name": "DOCUSIGN_CREATE_ENVELOPE_FROM_TEMPLATE",
            "arguments": {
                "templateId": args.template_id,
                "status": args.status,
                "templateRoles": [
                    {
                        "roleName": args.role_name,
                        "name": args.name,
                        "email": args.email
                    }
                ]
            }
        }
    }

    if args.subject:
        payload["params"]["arguments"]["emailSubject"] = args.subject

    print("Execute the following payload via Rube MCP:")
    print(json.dumps(payload, indent=2))

def main():
    parser = argparse.ArgumentParser(description="DocuSign Envelope Creator Helper")
    parser.add_argument("--template-id", required=True, help="DocuSign Template GUID")
    parser.add_argument("--role-name", required=True, help="Role name defined in the template")
    parser.add_argument("--name", required=True, help="Recipient Name")
    parser.add_argument("--email", required=True, help="Recipient Email")
    parser.add_argument("--status", choices=["created", "sent"], default="created", help="Envelope status (created=draft, sent=send now)")
    parser.add_argument("--subject", help="Custom email subject")

    args = parser.parse_args()
    generate_envelope_payload(args)

if __name__ == "__main__":
    main()
