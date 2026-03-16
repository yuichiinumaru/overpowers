#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="Stripe Automation Helper")
    parser.add_argument("--action", choices=["charge", "refund", "subscription"], required=True)
    args = parser.parse_args()

    print(f"[Stripe Rube MCP] Action requested: {args.action}")
    if args.action == "charge":
        print("MOCK: Successful charge of $10.00.")
    elif args.action == "refund":
        print("MOCK: Refund issued.")
    elif args.action == "subscription":
        print("MOCK: Subscription created.")

if __name__ == "__main__":
    main()
