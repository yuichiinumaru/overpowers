import argparse
import json

def main():
    parser = argparse.ArgumentParser(description="Content Research Helper")
    parser.add_argument("topic", help="Topic to research")
    parser.add_argument("--output", default="research_notes.md", help="Output markdown file")
    
    args = parser.parse_args()
    
    print(f"Researching topic: {args.topic}...")
    
    template = f"""# Research Notes: {args.topic}

## Key Findings
- [Point 1]
- [Point 2]
- [Point 3]

## Credible Sources
1. [Source Name] - [URL]
2. [Source Name] - [URL]

## Quotes and Data
- "[Quote]" - [Source]
- [Data Point] - [Source]

## Citations (APA)
- [Author] ([Year]). [Title]. [Publication].
"""

    with open(args.output, "w") as f:
        f.write(template)
        
    print(f"Research template generated: {args.output}")
    print("Next step: Use 'google_web_search' or 'web_fetch' to populate the findings.")

if __name__ == "__main__":
    main()
