#!/usr/bin/env python3
import stripe
import argparse
import os
from datetime import datetime

def list_recent_events(api_key, limit=10):
    """Lists recent Stripe events."""
    stripe.api_key = api_key
    
    try:
        events = stripe.Event.list(limit=limit)
        print(f"--- Recent {len(events.data)} Stripe Events ---")
        for event in events.data:
            created = datetime.fromtimestamp(event.created).strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{created}] {event.id} - {event.type}")
    except Exception as e:
        print(f"Error fetching events: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List recent Stripe events.")
    parser.add_argument("--key", help="Stripe API Secret Key (or set STRIPE_SECRET_KEY env var)")
    parser.add_argument("--limit", type=int, default=10, help="Number of events to list (default: 10)")
    
    args = parser.parse_args()
    key = args.key or os.getenv("STRIPE_SECRET_KEY")
    
    if not key:
        print("Error: Stripe API Secret Key not provided. Use --key or set STRIPE_SECRET_KEY.")
    else:
        list_recent_events(key, args.limit)
