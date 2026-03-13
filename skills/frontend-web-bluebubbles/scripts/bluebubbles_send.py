#!/usr/bin/env python3
import json
import sys

def generate_bluebubbles_payload(action, target, message="", message_id=""):
    payload = {
        "action": action,
        "channel": "bluebubbles",
        "target": target
    }
    if message:
        payload["message"] = message
    if message_id:
        payload["messageId"] = message_id
        
    print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: bluebubbles_send.py <action> <target> [message] [message_id]")
        sys.exit(1)
    
    generate_bluebubbles_payload(
        sys.argv[1], 
        sys.argv[2], 
        sys.argv[3] if len(sys.argv) > 3 else "",
        sys.argv[4] if len(sys.argv) > 4 else ""
    )
