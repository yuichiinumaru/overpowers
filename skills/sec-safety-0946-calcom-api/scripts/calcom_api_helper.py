#!/usr/bin/env python3
import sys

EXAMPLES = {
    "auth": "Authorization: Bearer cal_<your_api_key>",
    "check_slots": "GET https://api.cal.com/v2/slots?startTime=2024-01-15T00:00:00Z&endTime=2024-01-22T00:00:00Z&eventTypeId=123",
    "create_booking": """POST https://api.cal.com/v2/bookings
Content-Type: application/json

{
  "start": "2024-01-15T10:00:00Z",
  "eventTypeId": 123,
  "attendee": {
    "name": "John Doe",
    "email": "john@example.com",
    "timeZone": "America/New_York"
  }
}""",
    "webhook": """POST https://api.cal.com/v2/webhooks
Content-Type: application/json

{
  "subscriberUrl": "https://your-app.com/webhook",
  "triggers": ["BOOKING_CREATED", "BOOKING_CANCELLED"]
}"""
}

def main():
    if len(sys.argv) < 2:
        print("Usage: calcom_api_helper.py [auth|check_slots|create_booking|webhook]")
        sys.exit(1)
        
    example = sys.argv[1]
    if example in EXAMPLES:
        print(f"--- Example for {example} ---")
        print(EXAMPLES[example])
    else:
        print(f"Unknown example: {example}")

if __name__ == "__main__":
    main()
