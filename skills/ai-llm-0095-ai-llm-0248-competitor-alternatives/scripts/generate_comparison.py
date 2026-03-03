import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Generate Competitor Comparison Page")
    parser.add_argument("--you", required=True, help="Your product name")
    parser.add_argument("--competitor", required=True, help="Competitor product name")
    parser.add_argument("--output", help="Output markdown file")
    
    args = parser.parse_args()
    
    output_file = args.output or f"{args.you.lower()}-vs-{args.competitor.lower()}.md"
    
    content = f"""# {args.you} vs {args.competitor}: Which is right for you?

## TL;DR
A quick summary of why {args.you} might be a better choice for certain teams, and where {args.competitor} still shines.

## Comparison Table

| Feature | {args.you} | {args.competitor} |
|---------|-----------|------------------|
| Core Focus | [Detail] | [Detail] |
| Pricing | [Detail] | [Detail] |
| Key Benefit | [Detail] | [Detail] |

## Why choose {args.you}?
- [Reason 1]
- [Reason 2]

## Why choose {args.competitor}?
- [Reason 1]
- [Reason 2]

## Conclusion
Final verdict based on use cases.
"""

    with open(output_file, "w") as f:
        f.write(content)
        
    print(f"Comparison page template generated: {output_file}")

if __name__ == "__main__":
    main()
