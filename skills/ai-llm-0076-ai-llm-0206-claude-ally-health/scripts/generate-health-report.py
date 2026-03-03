#!/usr/bin/env python3
import argparse
import os

TEMPLATE = """# Health Status Report: {name}

## Summary
{summary}

## Symptoms Tracked
{symptoms}

## Wellness Guidance
{guidance}

## Next Steps
- Consult with a medical professional.
- Track symptoms daily.
"""

def main():
    parser = argparse.ArgumentParser(description='Generate a Health Status Report.')
    parser.add_argument('name', help='Patient name')
    parser.add_argument('--summary', default='[Overall health summary]', help='Health summary')
    parser.add_argument('--symptoms', default='[List of symptoms]', help='Symptoms tracked')
    parser.add_argument('--guidance', default='[Wellness recommendations]', help='Wellness guidance')
    parser.add_argument('--output', help='Output file path')

    args = parser.parse_args()

    content = TEMPLATE.format(
        name=args.name,
        summary=args.summary,
        symptoms=args.symptoms,
        guidance=args.guidance
    )

    output_path = args.output or f"health-report-{args.name.lower().replace(' ', '-')}.md"
    
    with open(output_path, 'w') as f:
        f.write(content)
    
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
