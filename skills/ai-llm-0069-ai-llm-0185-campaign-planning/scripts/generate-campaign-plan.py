#!/usr/bin/env python3
import argparse
import os

def generate_template(name):
    template = f"""# Campaign Plan: {name}

## 1. Objective
Define what success looks like.
- **SMART Goal**: [e.g., Generate 200 MQLs from mid-market SaaS within 6 weeks]
- **Primary KPI**: [e.g., Conversions]

## 2. Audience
Define who you are trying to reach.
- **Profile**: [Role] at [company type] who is struggling with [pain point] and looking for [desired outcome].
- **Demographics**: [e.g., CTOs at Series B Startups]
- **Psychographics**: [e.g., Concerned about scaling costs]

## 3. Message
Craft the core message.
- **Core Message**: [One sentence summary]
- **Supporting Points**:
  1. [Benefit 1]
  2. [Benefit 2]
  3. [Benefit 3]
- **Call to Action**: [e.g., Download the whitepaper]

## 4. Channels
Select channels where your audience is.
- **Owned**: [e.g., Email, Blog]
- **Paid**: [e.g., LinkedIn Ads]
- **Earned**: [e.g., PR]

## 5. Measure
How will you know it worked?
- [Metric 1]: [Target]
- [Metric 2]: [Target]

## Content Calendar
| Date | Content Piece | Channel | Audience | Owner | Status |
|------|--------------|---------|----------|-------|--------|
|      |              |         |          |       |        |
"""
    return template

def main():
    parser = argparse.ArgumentParser(description='Generate a Campaign Plan template.')
    parser.add_argument('--name', help='Campaign name', default='New Campaign')
    parser.add_argument('--output', help='Output file name', default='CAMPAIGN-PLAN.md')

    args = parser.parse_args()

    name = args.name
    if not args.name and not os.environ.get('NON_INTERACTIVE'):
        name = input("Campaign Name [New Campaign]: ") or 'New Campaign'

    content = generate_template(name)
    
    with open(args.output, 'w') as f:
        f.write(content)
    
    print(f"Generated {args.output}")

if __name__ == "__main__":
    main()
