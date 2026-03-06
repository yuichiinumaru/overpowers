#!/usr/bin/env python3
import sys
import argparse

def generate_email(email_type):
    templates = {
        "meeting": """Subject: Meeting Request: [Topic] - [Proposed Date/Time]

Hi [Name],

I'd like to discuss [specific topic] to [clear objective].

Could we meet for [duration] on [date options]?

Topics to cover:
- [Point 1]
- [Point 2]

Let me know if these times work for you.

Best regards,
[Name]""",
        "followup": """Subject: Following Up: [Original Topic]

Hi [Name],

I wanted to follow up on [previous conversation/email] from [date].

[Brief context reminder]

Could you let me know [specific ask] by [date]?

Thanks,
[Name]"""
    }

    return templates.get(email_type, templates["meeting"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate email templates")
    parser.add_argument("--type", choices=["meeting", "followup"], default="meeting", help="Type of email to generate")
    parser.add_argument("--out", help="Output file (optional)")

    args = parser.parse_args()

    email_content = generate_email(args.type)

    if args.out:
        with open(args.out, 'w') as f:
            f.write(email_content)
        print(f"Generated {args.type} email template at {args.out}")
    else:
        print(email_content)
