#!/usr/bin/env python3
"""Live trading CLI for the simulation platform.

Usage:
    # Bind (get credentials):
    python live_trade.py bind --pair-code ABCD-EFGH --name "利弗莫尔v2"

    # Check status:
    python live_trade.py status --key ak_xxx --secret as_xxx

    # Open long:
    python live_trade.py open-long --key ak_xxx --secret as_xxx --amount 1000 --leverage 10

    # Open short:
    python live_trade.py open-short --key ak_xxx --secret as_xxx --amount 1000 --leverage 10

    # Close position:
    python live_trade.py close --key ak_xxx --secret as_xxx --side LONG

    # Get price:
    python live_trade.py price --key ak_xxx --secret as_xxx

    # Order history:
    python live_trade.py orders --key ak_xxx --secret as_xxx

    # Trade history:
    python live_trade.py trades --key ak_xxx --secret as_xxx

    # Save/load credentials:
    python live_trade.py bind ... --save /tmp/agent_creds.json
    python live_trade.py status --creds /tmp/agent_creds.json
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from trading_client import TradingClient


def load_client(args) -> TradingClient:
    if hasattr(args, "creds") and args.creds:
        with open(args.creds) as f:
            creds = json.load(f)
        return TradingClient(
            api_key=creds["api_key"],
            api_secret=creds["api_secret"],
            agent_id=creds.get("agent_id", ""),
        )
    return TradingClient(
        api_key=getattr(args, "key", ""),
        api_secret=getattr(args, "secret", ""),
        agent_id=getattr(args, "agent_id", ""),
    )


def cmd_bind(args):
    client = TradingClient()
    result = client.bind(
        args.pair_code,
        display_name=args.name,
        persona=getattr(args, "persona", "") or args.name,
        description=getattr(args, "description", "") or f"{args.name} trading bot",
        fingerprint=args.fingerprint or "",
    )
    print(json.dumps(result, indent=2))

    if "api_secret" in result and args.save:
        with open(args.save, "w") as f:
            json.dump(result, f, indent=2)
        print(f"\nCredentials saved to {args.save}", file=sys.stderr)


def cmd_status(args):
    client = load_client(args)
    account = client.get_account()
    positions = client.get_positions()
    price = client.get_price()

    print("=== Account ===")
    print(json.dumps(account, indent=2))
    print("\n=== Positions ===")
    print(json.dumps(positions, indent=2))
    print("\n=== Price ===")
    print(json.dumps(price, indent=2))


def cmd_price(args):
    client = load_client(args)
    print(json.dumps(client.get_price(), indent=2))


def cmd_open_long(args):
    client = load_client(args)
    result = client.open_long(args.amount, args.leverage, args.order_id or "")
    print(json.dumps(result, indent=2))


def cmd_open_short(args):
    client = load_client(args)
    result = client.open_short(args.amount, args.leverage, args.order_id or "")
    print(json.dumps(result, indent=2))


def cmd_close(args):
    client = load_client(args)
    result = client.close_position(args.side, args.qty or "")
    print(json.dumps(result, indent=2))


def cmd_orders(args):
    client = load_client(args)
    print(json.dumps(client.get_orders(args.limit), indent=2))


def cmd_trades(args):
    client = load_client(args)
    print(json.dumps(client.get_trades(args.limit), indent=2))


def main():
    parser = argparse.ArgumentParser(description="Live trading CLI")
    sub = parser.add_subparsers(dest="command")

    # bind
    p = sub.add_parser("bind", help="Bind agent with pair code")
    p.add_argument("--pair-code", required=True)
    p.add_argument("--name", default="Bot")
    p.add_argument("--persona", default="", help="Bot persona (e.g. 趋势死磕派)")
    p.add_argument("--description", default="", help="Bot description")
    p.add_argument("--fingerprint", default="")
    p.add_argument("--save", default="", help="Save credentials to JSON file")

    # status
    p = sub.add_parser("status", help="Account + positions + price")
    p.add_argument("--key", default="")
    p.add_argument("--secret", default="")
    p.add_argument("--agent-id", default="")
    p.add_argument("--creds", default="", help="Load from credentials JSON")

    # price
    p = sub.add_parser("price", help="Get mark price")
    p.add_argument("--key", default="")
    p.add_argument("--secret", default="")
    p.add_argument("--creds", default="")

    # open-long
    p = sub.add_parser("open-long", help="Open long position")
    p.add_argument("--key", default="")
    p.add_argument("--secret", default="")
    p.add_argument("--agent-id", default="")
    p.add_argument("--creds", default="")
    p.add_argument("--amount", required=True, help="Notional USDT")
    p.add_argument("--leverage", type=int, required=True)
    p.add_argument("--order-id", default="")

    # open-short
    p = sub.add_parser("open-short", help="Open short position")
    p.add_argument("--key", default="")
    p.add_argument("--secret", default="")
    p.add_argument("--agent-id", default="")
    p.add_argument("--creds", default="")
    p.add_argument("--amount", required=True, help="Notional USDT")
    p.add_argument("--leverage", type=int, required=True)
    p.add_argument("--order-id", default="")

    # close
    p = sub.add_parser("close", help="Close position")
    p.add_argument("--key", default="")
    p.add_argument("--secret", default="")
    p.add_argument("--agent-id", default="")
    p.add_argument("--creds", default="")
    p.add_argument("--side", required=True, choices=["LONG", "SHORT"])
    p.add_argument("--qty", default="", help="BTC qty, empty=close all")

    # orders
    p = sub.add_parser("orders", help="Order history")
    p.add_argument("--key", default="")
    p.add_argument("--secret", default="")
    p.add_argument("--creds", default="")
    p.add_argument("--limit", type=int, default=20)

    # trades
    p = sub.add_parser("trades", help="Trade history")
    p.add_argument("--key", default="")
    p.add_argument("--secret", default="")
    p.add_argument("--creds", default="")
    p.add_argument("--limit", type=int, default=20)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    cmds = {
        "bind": cmd_bind, "status": cmd_status, "price": cmd_price,
        "open-long": cmd_open_long, "open-short": cmd_open_short,
        "close": cmd_close, "orders": cmd_orders, "trades": cmd_trades,
    }
    cmds[args.command](args)


if __name__ == "__main__":
    main()
