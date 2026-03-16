#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="Square Automation Helper")
    parser.add_argument("--action", choices=["process_payment", "list_orders", "create_invoice"], required=True)
    args = parser.parse_args()

    print(f"[Square Rube MCP] Action requested: {args.action}")
    if args.action == "process_payment":
        print("MOCK: Payment Processed.")
    elif args.action == "list_orders":
        print("MOCK: Listed 3 active orders.")
    elif args.action == "create_invoice":
        print("MOCK: Invoice sent to customer.")

if __name__ == "__main__":
    main()
