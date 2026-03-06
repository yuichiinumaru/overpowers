import argparse
import sys

TEMPLATES = {
    "bug": """Hi {name},

Thank you for reporting this — I can see how {impact} would be frustrating for your team.

I've confirmed the issue and escalated it to our engineering team as a {priority} level. Here's what we know so far:
- {what_is_happening}
- {cause}
- {workaround}

I'll update you by {deadline} with a resolution timeline. In the meantime, {workaround_action}.

Let me know if you have any questions or if this is impacting you in other ways I should know about.

Best,
{your_name}""",

    "feature_decline": """Hi {name},

Thank you for sharing this request — I can see why {capability} would be valuable for {use_case}.

I discussed this with our product team, and this isn't something we're planning to build in the near term. The primary reason is {reason}.

That said, I want to make sure you can accomplish your goal. Here are some alternatives:
- {alternative1}
- {alternative2}

I've also documented your request in our feedback system, and if our direction changes, I'll let you know.

Would any of these alternatives work for your team? Happy to dig deeper into any of them.

Best,
{your_name}""",

    "follow_up": """Hi {name},

I wanted to check in — I sent over {what_was_sent} on {date} and wanted to make sure it didn't get lost in the shuffle.

{reminder}

If now isn't a good time, no worries — just let me know when would be better, and I'm happy to reconnect then.

Best,
{your_name}"""
}

def main():
    parser = argparse.ArgumentParser(description="Customer Response Drafter")
    parser.add_argument("type", choices=TEMPLATES.keys(), help="Type of response template")
    parser.add_argument("--name", required=True, help="Customer name")
    parser.add_argument("--your-name", required=True, help="Your name")
    
    # Template specific args would be many, using a generic approach for now
    args, unknown = parser.parse_known_args()
    
    template = TEMPLATES[args.type]
    
    # Simple interactive prompt for missing placeholders
    import re
    placeholders = re.findall(r'\{(.*?)\}', template)
    data = {"name": args.name, "your_name": args.your_name}
    
    for p in placeholders:
        if p not in data:
            val = input(f"Enter value for '{p}': ")
            data[p] = val
            
    print("\n--- DRAFT RESPONSE ---\n")
    print(template.format(**data))
    print("\n----------------------")

if __name__ == "__main__":
    main()
