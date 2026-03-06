#!/usr/bin/env python3
"""
Email Template Generator
Generates common business email templates.
"""
import sys
import argparse

def generate_template(template_type, sender_name, recipient_name, context):
    """
    Generate standard business email templates.
    """
    templates = {
        "meeting": f"""Subject: Request for Meeting: {context}

Hi {recipient_name},

I hope this email finds you well.

I would like to request a brief meeting to discuss {context}. Would you have 15-30 minutes available sometime next week?

Please let me know a few times that work for you, or feel free to book directly on my calendar here: [Link]

Looking forward to connecting.

Best regards,
{sender_name}
""",
        "followup": f"""Subject: Following up: {context}

Hi {recipient_name},

I'm following up on our previous conversation regarding {context}.

Could you please provide an update on the status or let me know if you need any additional information from my side?

Thanks,
{sender_name}
""",
        "introduction": f"""Subject: Introduction: {sender_name} and {recipient_name}

Hi {recipient_name},

I'm writing to introduce myself. I am {sender_name} and I focus on {context}.

I've been following your work and would love to connect to discuss potential synergies.

Best,
{sender_name}
"""
    }

    if template_type in templates:
        print(templates[template_type])
    else:
        print(f"Template type '{template_type}' not found. Available types: {', '.join(templates.keys())}")

def main():
    parser = argparse.ArgumentParser(description="Business Email Template Generator")
    parser.add_argument("--type", choices=['meeting', 'followup', 'introduction'], required=True, help="Type of email template")
    parser.add_argument("--sender", required=True, help="Sender's name")
    parser.add_argument("--recipient", required=True, help="Recipient's name")
    parser.add_argument("--context", required=True, help="Brief context or topic for the email")

    args = parser.parse_args()

    generate_template(args.type, args.sender, args.recipient, args.context)

if __name__ == "__main__":
    main()
