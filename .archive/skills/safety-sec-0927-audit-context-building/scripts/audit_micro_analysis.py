#!/usr/bin/env python3
import argparse
import sys

TEMPLATE = """# Micro-Analysis: {function_name}

## 1. Purpose
{purpose}

## 2. Inputs & Assumptions
- **Parameters**: 
- **Implicit Inputs**: 
- **Preconditions**: 

## 3. Outputs & Effects
- **Return Values**: 
- **State Writes**: 
- **Events/Messages**: 
- **External Interactions**: 

## 4. Block-by-Block / Line-by-Line Analysis

### Block 1: [Lines X-Y]
- **What**: 
- **Why here**: 
- **Assumptions**: 
- **Invariants**: 
- **Dependencies**: 
- **5 Whys/Hows**: 

## 5. Cross-Function Dependencies
- **Internal Calls**: 
- **External Calls**: 
- **Shared State**: 

## 6. Completeness Checklist
- [ ] Purpose defined (2-3 sentences)
- [ ] Inputs & Assumptions documented
- [ ] Outputs & Effects documented
- [ ] Block-by-block analysis complete
- [ ] 5 Whys/Hows applied
- [ ] Invariants identified (min 3)
- [ ] Assumptions documented (min 5)
"""

def main():
    parser = argparse.ArgumentParser(description="Audit Micro-Analysis Template Generator")
    parser.add_argument("name", help="Function name")
    parser.add_argument("--purpose", default="[Describe the role of this function in the system]", help="Function purpose")
    args = parser.parse_args()

    output = TEMPLATE.format(function_name=args.name, purpose=args.purpose)
    print(output)

if __name__ == "__main__":
    main()
