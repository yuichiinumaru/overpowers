#!/usr/bin/env python3
import json
import time
import hmac
import hashlib
import requests
import argparse

def simulate_webhook(url, event_type, secret=None):
    """Simulates a Stripe webhook event."""
    timestamp = int(time.time())
    
    # Dummy payload structure based on Stripe events
    payload_obj = {
        "id": f"evt_test_{timestamp}",
        "object": "event",
        "api_version": "2023-10-16",
        "created": timestamp,
        "type": event_type,
        "data": {
            "object": {
                "id": f"obj_test_{timestamp}",
                "object": event_type.split('.')[0],
                "customer": "cus_test_123",
                "amount": 2000,
                "currency": "usd",
                "status": "succeeded" if "succeeded" in event_type else "active"
            }
        }
    }
    
    payload_str = json.dumps(payload_obj)
    headers = {'Content-Type': 'application/json'}
    
    if secret:
        # Generate Stripe-Signature header
        signed_payload = f"{timestamp}.{payload_str}"
        signature = hmac.new(
            secret.encode('utf-8'),
            signed_payload.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        headers['Stripe-Signature'] = f"t={timestamp},v1={signature}"
    
    print(f"Sending {event_type} to {url}...")
    try:
        response = requests.post(url, data=payload_str, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate a Stripe webhook event.")
    parser.add_argument("url", help="Target webhook URL")
    parser.add_argument("--type", default="payment_intent.succeeded", help="Event type (default: payment_intent.succeeded)")
    parser.add_argument("--secret", help="Stripe webhook signing secret (optional)")
    
    args = parser.parse_args()
    simulate_webhook(args.url, args.type, args.secret)
