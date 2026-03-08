#!/usr/bin/env python3
"""
ordercli Command Generator
Generates common ordercli commands for tracking food deliveries.
"""
import sys
import argparse

def generate_command(action, service="foodora", **kwargs):
    """
    Generate the appropriate ordercli command.
    """
    base_cmd = f"ordercli {service}"

    if action == "login":
        email = kwargs.get('email')
        if not email:
            print("Error: email is required for login.", file=sys.stderr)
            sys.exit(1)
        print(f"{base_cmd} login --email {email} --password-stdin")

    elif action == "history":
        limit = kwargs.get('limit', 10)
        print(f"{base_cmd} history --limit {limit}")

    elif action == "show":
        code = kwargs.get('code')
        if not code:
            print("Error: order code is required for show.", file=sys.stderr)
            sys.exit(1)
        print(f"{base_cmd} history show {code}")

    elif action == "orders":
        print(f"{base_cmd} orders")

    elif action == "config":
        country = kwargs.get('country')
        if not country:
            print("Error: country code is required to set config.", file=sys.stderr)
            sys.exit(1)
        print(f"{base_cmd} config set --country {country}")

    else:
        print(f"Error: Unknown action '{action}'.", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="ordercli Command Generator")
    parser.add_argument("--action", choices=['login', 'history', 'show', 'orders', 'config'], required=True, help="Action to perform")
    parser.add_argument("--service", choices=['foodora'], default='foodora', help="Delivery service (default: foodora)")
    parser.add_argument("--email", help="Email for login")
    parser.add_argument("--limit", type=int, default=10, help="Limit for history (default: 10)")
    parser.add_argument("--code", help="Order code for show")
    parser.add_argument("--country", help="Country code for config (e.g. AT)")

    args = parser.parse_args()

    generate_command(args.action, args.service, email=args.email, limit=args.limit, code=args.code, country=args.country)

if __name__ == "__main__":
    main()
