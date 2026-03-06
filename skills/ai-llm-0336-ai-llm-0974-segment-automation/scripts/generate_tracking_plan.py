#!/usr/bin/env python3
import json
import argparse
import os

def create_event(name, description, properties):
    return {
        "name": name,
        "description": description,
        "rules": {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": properties,
            "required": list(properties.keys())
        }
    }

def main():
    parser = argparse.ArgumentParser(description="Generate a basic Segment Tracking Plan.")
    parser.add_argument("--output", default="tracking_plan.json", help="Output file path")

    args = parser.parse_args()

    # Template basic events
    events = []

    # Page Viewed
    events.append(create_event(
        "Page Viewed",
        "Triggered when a user views a page",
        {
            "path": {"type": "string"},
            "url": {"type": "string"},
            "title": {"type": "string"}
        }
    ))

    # User Signed Up
    events.append(create_event(
        "Signed Up",
        "Triggered when a new user completes the signup process",
        {
            "userId": {"type": "string"},
            "plan_type": {"type": "string", "enum": ["free", "pro", "enterprise"]},
            "source": {"type": "string"}
        }
    ))

    plan = {
        "display_name": "Basic SaaS Tracking Plan",
        "rules": {
            "events": events
        }
    }

    with open(args.output, "w") as f:
        json.dump(plan, f, indent=2)

    print(f"Generated tracking plan at {args.output}")

if __name__ == "__main__":
    main()
