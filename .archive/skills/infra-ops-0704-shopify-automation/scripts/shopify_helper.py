#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="Shopify Automation Helper")
    parser.add_argument("--action", choices=["get_products", "create_order", "list_customers"], required=True)
    args = parser.parse_args()

    print(f"[Shopify Rube MCP] Action requested: {args.action}")
    if args.action == "get_products":
        print("MOCK: Return 5 products from Shopify.")
    elif args.action == "create_order":
        print("MOCK: Order created successfully.")
    elif args.action == "list_customers":
        print("MOCK: List of 10 customers.")

if __name__ == "__main__":
    main()
