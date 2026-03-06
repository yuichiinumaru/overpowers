#!/usr/bin/env python3
import json
import argparse
import sys
from datetime import datetime, timedelta

def create_mandate_payload(agent_id, amount_cents, currency="USD", period="daily", merchant_restrictions=None):
    """Generate a payload for creating an active mandate."""
    expires = datetime.utcnow() + timedelta(days=365) # Default 1 year expiry

    payload = {
        "agent_id": agent_id,
        "amount_cents": int(amount_cents),
        "currency": currency,
        "period": period,
        "kind": "intent",
        "merchant_restrictions": merchant_restrictions or [],
        "expires_at": expires.strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    return json.dumps(payload, indent=2)

def create_auth_payload(mandate_id, amount_cents, merchant, description):
    """Generate a payload for payment authorization."""
    payload = {
        "mandate_id": mandate_id,
        "amount_cents": int(amount_cents),
        "merchant": merchant,
        "description": description
    }
    return json.dumps(payload, indent=2)

def create_consensus_payload(payment_id, required_agents, threshold):
    """Generate a payload for requesting consensus."""
    payload = {
        "payment_id": payment_id,
        "required_agents": required_agents,
        "threshold": int(threshold),
        "timeout_seconds": 300
    }
    return json.dumps(payload, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Agentic Payments Payload Generator")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Mandate parser
    mandate_parser = subparsers.add_parser("create-mandate", help="Create a mandate payload")
    mandate_parser.add_argument("--agent-id", required=True, help="Agent ID")
    mandate_parser.add_argument("--amount", required=True, type=int, help="Amount in cents")
    mandate_parser.add_argument("--currency", default="USD", help="Currency code")
    mandate_parser.add_argument("--period", default="daily", choices=["daily", "weekly", "monthly"], help="Spend period")
    mandate_parser.add_argument("--merchants", nargs="*", help="Allowed merchants")

    # Auth parser
    auth_parser = subparsers.add_parser("authorize", help="Create an authorization payload")
    auth_parser.add_argument("--mandate-id", required=True, help="Mandate ID")
    auth_parser.add_argument("--amount", required=True, type=int, help="Amount in cents")
    auth_parser.add_argument("--merchant", required=True, help="Merchant name")
    auth_parser.add_argument("--desc", required=True, help="Description")

    # Consensus parser
    consensus_parser = subparsers.add_parser("consensus", help="Create a consensus payload")
    consensus_parser.add_argument("--payment-id", required=True, help="Payment ID")
    consensus_parser.add_argument("--agents", required=True, nargs="+", help="Required agent IDs")
    consensus_parser.add_argument("--threshold", required=True, type=int, help="Number of approvals required")

    args = parser.parse_args()

    if args.command == "create-mandate":
        print(create_mandate_payload(args.agent_id, args.amount, args.currency, args.period, args.merchants))
    elif args.command == "authorize":
        print(create_auth_payload(args.mandate_id, args.amount, args.merchant, args.desc))
    elif args.command == "consensus":
        print(create_consensus_payload(args.payment_id, args.agents, args.threshold))
    else:
        parser.print_help()
        sys.exit(1)
