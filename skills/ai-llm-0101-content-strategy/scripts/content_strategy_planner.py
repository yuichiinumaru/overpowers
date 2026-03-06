import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Content Strategy Planner")
    parser.add_argument("--company", required=True, help="Company name")
    parser.add_argument("--pillars", help="Comma-separated core pillars")
    parser.add_argument("--output", default="content_strategy.md", help="Output markdown file")
    
    args = parser.parse_args()
    pillars = [p.strip() for p in args.pillars.split(",")] if args.pillars else ["[Pillar 1]", "[Pillar 2]", "[Pillar 3]"]
    
    content = f"""# Content Strategy for {args.company}

## Core Content Pillars
{"".join([f"- **{p}**: [Rationale and target audience]\\n" for p in pillars])}

## Content Roadmap (30-60-90 Days)

### Day 1-30: Foundation
- [Article 1] - Target Keyword: [Keyword]
- [Article 2] - Target Keyword: [Keyword]

### Day 31-60: Authority
- [Article 3] - Target Keyword: [Keyword]
- [Article 4] - Target Keyword: [Keyword]

### Day 61-90: Growth
- [Article 5] - Target Keyword: [Keyword]
- [Article 6] - Target Keyword: [Keyword]

## Customer Research Insights
- **Common Questions**: [Insight 1]
- **Objections**: [Insight 2]
- **Language Patterns**: [Specific phrases to use]

## Distribution Plan
- **Primary Channels**: [Platform 1], [Platform 2]
- **Repurposing Matrix**: [How content moves between formats]
"""

    with open(args.output, "w") as f:
        f.write(content)
        
    print(f"Content strategy template generated: {args.output}")

if __name__ == "__main__":
    main()
