#!/usr/bin/env python3
import sys
from datetime import datetime

def generate_agenda():
    date_str = datetime.now().strftime("%Y-%m-%d")
    template = f"""# Council Meeting Agenda - {date_str}

## 1. Roll Call & Opening Remarks
- Present:
- Absent:

## 2. Review of Previous Action Items
- [ ] Item 1
- [ ] Item 2

## 3. Topics for Discussion
### Topic A
- Context:
- Proposals:
- Decision:

### Topic B
- Context:
- Proposals:
- Decision:

## 4. New Action Items
- [ ]

## 5. Next Meeting
- Date:
"""

    filename = f"COUNCIL_AGENDA_{date_str}.md"
    with open(filename, "w") as f:
        f.write(template)

    print(f"Created {filename}")

if __name__ == "__main__":
    generate_agenda()
