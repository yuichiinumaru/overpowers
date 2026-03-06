#!/usr/bin/env python3
import sys

def main():
    print("Generating Free Tool Strategy Scorecard...")
    
    template = """# Free Tool Strategy Scorecard

| Factor | Score (1-5) |
|--------|-------|
| Search demand exists | |
| Audience match to buyers | |
| Uniqueness vs. existing tools | |
| Natural path to product | |
| Build feasibility | |
| Maintenance burden (inverse) | |
| Link-building potential | |
| Share-worthiness | |

**Total Score**: /40

**Interpretation**:
- **25+**: Strong candidate
- **15-24**: Promising, needs refinement
- **<15**: Reconsider or scope differently
"""

    with open("Tool-Strategy-Scorecard.md", "w") as f:
        f.write(template)
        
    print("Created Tool-Strategy-Scorecard.md")

if __name__ == "__main__":
    main()
