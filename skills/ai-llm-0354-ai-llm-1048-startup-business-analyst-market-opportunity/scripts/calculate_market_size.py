#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate TAM, SAM, and SOM based on basic inputs.")
    parser.add_argument("--total-users", type=int, required=True, help="Total potential users worldwide")
    parser.add_argument("--arpu", type=float, required=True, help="Average Revenue Per User (annual)")
    parser.add_argument("--target-segment-pct", type=float, required=True, help="Percentage of total users in your serviceable segment (0-1)")
    parser.add_argument("--market-share-pct", type=float, required=True, help="Realistic market share percentage you can capture (0-1)")

    args = parser.parse_args()

    tam = args.total_users * args.arpu
    sam = tam * args.target_segment_pct
    som = sam * args.market_share_pct

    print(f"--- Market Opportunity Analysis ---")
    print(f"Assumptions:")
    print(f"  Total Potential Users: {args.total_users:,}")
    print(f"  ARPU (Annual): ${args.arpu:,.2f}")
    print(f"  Serviceable Segment: {args.target_segment_pct*100:.1f}%")
    print(f"  Target Market Share: {args.market_share_pct*100:.1f}%")
    print("\nResults:")
    print(f"  TAM (Total Addressable Market): ${tam:,.2f}")
    print(f"  SAM (Serviceable Available Market): ${sam:,.2f}")
    print(f"  SOM (Serviceable Obtainable Market): ${som:,.2f}")

if __name__ == "__main__":
    main()
