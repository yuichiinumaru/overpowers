#!/usr/bin/env python3
import sys
from datetime import datetime

def generate_template(company):
    date_str = datetime.now().strftime("%Y-%m-%d")
    template = f"""# Customer Research: {company}
Date: {date_str}

## 1. Company Overview
- Industry:
- Size:
- Target Market:

## 2. Key Pain Points
-
-
-

## 3. Current Solutions Used
-
-

## 4. Value Proposition Match
- How our solution helps:
- Potential objections:

## 5. Next Steps
-
"""

    filename = f"RESEARCH_{company.replace(' ', '_').upper()}.md"
    with open(filename, "w") as f:
        f.write(template)

    print(f"Created template at {filename}")

if __name__ == "__main__":
    company = sys.argv[1] if len(sys.argv) > 1 else "ACME_Corp"
    generate_template(company)
