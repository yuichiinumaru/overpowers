#!/usr/bin/env python3
import sys
import os
from datetime import datetime
from pathlib import Path

def start_10x_session(product_name, session_num=1):
    target_dir = Path(f".claude/docs/ai/{product_name}/10x")
    target_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = target_dir / f"session-{session_num}.md"
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    template = f"""# 10x Analysis: {product_name}
Session {session_num} | Date: {date_str}

## Current Value
[What the product does today and for whom]

## The Question
What would make this 10x more valuable?

---

## Massive Opportunities
### 1. [Feature Name]
**What**: Description
**Why 10x**: Why this is transformative
**Unlocks**: What becomes possible
**Effort**: High
**Score**: 🔥

---

## Medium Opportunities
### 1. [Feature Name]
**What**: Description
**Why 10x**: Impact
**Effort**: Medium
**Score**: 👍

---

## Small Gems
### 1. [Feature Name]
**What**: Description
**Why powerful**: Why it punches above its weight
**Effort**: Low
**Score**: 🔥

---

## Recommended Priority
### Do Now
1. [Feature]

### Do Next
1. [Feature]

## Next Steps
- [ ] Research: ...
"""
    with open(file_path, "w") as f:
        f.write(template)
    
    print(f"Started 10x session document: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: start_10x_session.py <product-name> [session_number]")
        sys.exit(1)
    
    prod = sys.argv[1]
    num = sys.argv[2] if len(sys.argv) > 2 else 1
    start_10x_session(prod, num)
