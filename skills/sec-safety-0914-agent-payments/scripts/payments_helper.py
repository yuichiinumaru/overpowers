#!/usr/bin/env python3
import json
import argparse
import sys

def create_payment_link_payload(amount):
    """Generate payload for creating a payment link."""
    amount_int = int(amount)
    if amount_int < 10:
        print("Error: Minimum amount is $10", file=sys.stderr)
        sys.exit(1)

    payload = {
        "amount": amount_int
    }
    return json.dumps(payload, indent=2)

def configure_auto_refill_payload(enabled, threshold, amount):
    """Generate payload for configuring auto-refill."""
    payload = {
        "enabled": str(enabled).lower() == 'true',
        "threshold": int(threshold),
        "amount": int(amount)
    }
    return json.dumps(payload, indent=2)

def user_upgrade_payload(user_id, tier):
    """Generate payload for user tier upgrade."""
    valid_tiers = ["free", "pro", "enterprise"]
    if tier not in valid_tiers:
        print(f"Error: Invalid tier '{tier}'. Must be one of {valid_tiers}", file=sys.stderr)
        sys.exit(1)

    payload = {
        "user_id": user_id,
        "tier": tier
    }
    return json.dumps(payload, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flow Nexus Payments Payload Generator")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Payment link parser
    payment_parser = subparsers.add_parser("payment-link", help="Create a payment link payload")
    payment_parser.add_argument("--amount", required=True, type=int, help="Amount in USD (min 10)")

    # Auto-refill parser
    refill_parser = subparsers.add_parser("auto-refill", help="Configure auto-refill payload")
    refill_parser.add_argument("--enabled", required=True, choices=["true", "false"], help="Enable/disable auto-refill")
    refill_parser.add_argument("--threshold", required=True, type=int, help="Balance threshold to trigger refill")
    refill_parser.add_argument("--amount", required=True, type=int, help="Amount to refill")

    # Upgrade parser
    upgrade_parser = subparsers.add_parser("upgrade", help="User upgrade payload")
    upgrade_parser.add_argument("--user-id", required=True, help="User ID")
    upgrade_parser.add_argument("--tier", required=True, choices=["free", "pro", "enterprise"], help="Target tier")

    args = parser.parse_args()

    if args.command == "payment-link":
        print(create_payment_link_payload(args.amount))
    elif args.command == "auto-refill":
        print(configure_auto_refill_payload(args.enabled, args.threshold, args.amount))
    elif args.command == "upgrade":
        print(user_upgrade_payload(args.user_id, args.tier))
    else:
        parser.print_help()
        sys.exit(1)
