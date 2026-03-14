#!/usr/bin/env python3
"""Fetch OHLCV data and save to local CSV.

Usage:
    python fetch_data.py --symbol BTC/USDT --timeframe 15m --days 148
    python fetch_data.py --symbol BTC/USDT --timeframe 1h --since 2025-01-01
"""

import argparse
import json
import hashlib
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.fetcher import fetch_ohlcv


def main():
    parser = argparse.ArgumentParser(description="Fetch OHLCV data")
    parser.add_argument("--symbol", default="BTC/USDT")
    parser.add_argument("--timeframe", default="15m")
    parser.add_argument("--days", type=int, default=148)
    parser.add_argument("--since", default=None, help="Start date: YYYY-MM-DD")
    parser.add_argument("--exchange", default="binance")
    parser.add_argument("--output", default=None, help="Output CSV path")
    args = parser.parse_args()

    df = fetch_ohlcv(
        symbol=args.symbol,
        timeframe=args.timeframe,
        days=args.days,
        exchange_id=args.exchange,
        since_date=args.since,
    )

    if args.output:
        df.to_csv(args.output, index=False)
        csv_path = args.output
    else:
        safe_sym = args.symbol.replace("/", "_")
        csv_path = f"data_{safe_sym}_{args.timeframe}_{args.days}d.csv"
        df.to_csv(csv_path, index=False)

    checksum_raw = ",".join(f"{v:.2f}" for v in df["close"])
    checksum = hashlib.sha256(checksum_raw.encode()).hexdigest()

    fingerprint = {
        "symbol": args.symbol,
        "timeframe": args.timeframe,
        "exchange": args.exchange,
        "start": str(df["timestamp"].iloc[0]),
        "end": str(df["timestamp"].iloc[-1]),
        "bars": len(df),
        "first_close": round(df["close"].iloc[0], 2),
        "last_close": round(df["close"].iloc[-1], 2),
        "checksum": checksum,
        "csv_path": csv_path,
    }

    print(json.dumps(fingerprint, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
