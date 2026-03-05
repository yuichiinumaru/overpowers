#!/usr/bin/env python3
import sys

def main():
    print("--- SBI Feedback Template Generator ---\n")
    
    situation = input("Situation (context): ")
    behavior = input("Behavior (observable action): ")
    impact = input("Impact (effect on team/project): ")
    
    template = f"""
## SBI Feedback Draft

**Situation**: {situation}
**Behavior**: {behavior}
**Impact**: {impact}

---
**Recommended Delivery**:
"During {situation}, I noticed that {behavior}. This resulted in {impact}. I'd love to hear your perspective on this."
"""
    print(template)

if __name__ == "__main__":
    main()
