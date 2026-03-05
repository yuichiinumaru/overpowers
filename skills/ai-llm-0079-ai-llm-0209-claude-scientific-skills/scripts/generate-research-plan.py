#!/usr/bin/env python3
import argparse
import os

TEMPLATE = """# Research Plan: {title}

## Objective
{objective}

## Methodology
{methodology}

## Data Sources
{data_sources}

## Analysis Plan
{analysis_plan}

## Expected Outcomes
{expected_outcomes}

## Timeline
- Phase 1: Literature Review
- Phase 2: Data Collection
- Phase 3: Analysis
- Phase 4: Reporting
"""

def main():
    parser = argparse.ArgumentParser(description='Generate a Scientific Research Plan.')
    parser.add_argument('title', help='Research title')
    parser.add_argument('--objective', default='[Define research objective]', help='Research objective')
    parser.add_argument('--methodology', default='[Describe methodology]', help='Research methodology')
    parser.add_argument('--data-sources', default='[List data sources]', help='Data sources')
    parser.add_argument('--analysis-plan', default='[Describe analysis steps]', help='Analysis plan')
    parser.add_argument('--expected-outcomes', default='[Describe expected results]', help='Expected outcomes')
    parser.add_argument('--output', help='Output file path')

    args = parser.parse_args()

    content = TEMPLATE.format(
        title=args.title,
        objective=args.objective,
        methodology=args.methodology,
        data_sources=args.data_sources,
        analysis_plan=args.analysis_plan,
        expected_outcomes=args.expected_outcomes
    )

    output_path = args.output or f"research-plan-{args.title.lower().replace(' ', '-')}.md"
    
    with open(output_path, 'w') as f:
        f.write(content)
    
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
