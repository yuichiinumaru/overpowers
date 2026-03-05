#!/usr/bin/env python3
import argparse
import os

TEMPLATE = """# Campaign Brief: {name}

## 1. Objective (SMART)
{objective}

## 2. Audience
{audience}

## 3. Message
- **Core Message**: {core_message}
- **Supporting Messages**:
  - Message 1: 
  - Message 2:
- **Call to Action**: {cta}

## 4. Channels
{channels}

## 5. Measure (Success Metrics)
{metrics}

## Content Calendar (Initial)
| Date | Content Piece | Channel | Audience | Owner | Status |
|------|--------------|---------|----------|-------|--------|
| TBD  | Launch Post  | Blog    | Primary  | TBD   | Draft  |
"""

def main():
    parser = argparse.ArgumentParser(description='Generate a Marketing Campaign Brief.')
    parser.add_argument('name', help='Campaign name')
    parser.add_argument('--objective', default='[Define SMART objective]', help='Campaign objective')
    parser.add_argument('--audience', default='[Define target audience]', help='Target audience')
    parser.add_argument('--message', default='[Define core message]', help='Core message')
    parser.add_argument('--cta', default='[Define call to action]', help='Call to action')
    parser.add_argument('--channels', default='[Define channels]', help='Channels')
    parser.add_argument('--metrics', default='[Define success metrics]', help='Success metrics')
    parser.add_argument('--output', help='Output file path')

    args = parser.parse_args()

    content = TEMPLATE.format(
        name=args.name,
        objective=args.objective,
        audience=args.audience,
        core_message=args.message,
        cta=args.cta,
        channels=args.channels,
        metrics=args.metrics
    )

    output_path = args.output or f"campaign-brief-{args.name.lower().replace(' ', '-')}.md"
    
    with open(output_path, 'w') as f:
        f.write(content)
    
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
