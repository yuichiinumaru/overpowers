#!/usr/bin/env python3
"""
Flight Search Formatter
Generates the CLI command for fast-flights based on user inputs.
"""
import sys
import argparse

def generate_command(origin, destination, date, return_date=None, adults=1, cabin="economy", max_stops=None):
    """
    Generate the fast-flights CLI command.
    """
    cmd = ["flights-search"]
    cmd.append(origin)
    cmd.append(destination)
    cmd.append(date)

    if return_date:
        cmd.append(return_date)

    cmd.append(f"--adults {adults}")

    if cabin != "economy":
        cmd.append(f"--cabin {cabin}")

    if max_stops is not None:
        cmd.append(f"--max-stops {max_stops}")

    print(" ".join(cmd))

def main():
    parser = argparse.ArgumentParser(description="Flight Search Command Generator")
    parser.add_argument("--origin", required=True, help="Origin Airport Code (e.g. SFO)")
    parser.add_argument("--destination", required=True, help="Destination Airport Code (e.g. JFK)")
    parser.add_argument("--date", required=True, help="Departure Date (YYYY-MM-DD)")
    parser.add_argument("--return-date", help="Return Date (YYYY-MM-DD)")
    parser.add_argument("--adults", type=int, default=1, help="Number of adults (default: 1)")
    parser.add_argument("--cabin", choices=['economy', 'premium_economy', 'business', 'first'], default='economy', help="Cabin class (default: economy)")
    parser.add_argument("--max-stops", type=int, help="Maximum number of stops")

    args = parser.parse_args()

    generate_command(args.origin, args.destination, args.date, args.return_date, args.adults, args.cabin, args.max_stops)

if __name__ == "__main__":
    main()
