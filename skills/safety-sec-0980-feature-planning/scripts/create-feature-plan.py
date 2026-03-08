#!/usr/bin/env python3
import os
import sys
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print("Usage: create-feature-plan.py <feature-name>")
        sys.exit(1)

    feature_name = sys.argv[1]
    slug = feature_name.lower().replace(" ", "-")
    
    tasks_dir = "docs/tasks"
    os.makedirs(tasks_dir, exist_ok=True)
    
    # Simple logic to find next number (mocked for simplicity)
    next_num = "0100" # In a real script, this would parse existing files
    
    plan_path = os.path.join(tasks_dir, f"{next_num}-feature-{slug}.md")
    
    content = f"""## Feature: {feature_name}

### Overview
[Brief description of what will be built and why]

### Architecture Decisions
- [Decision 1]
- [Decision 2]

### Implementation Tasks

#### Task 1: [Component]
- **File**: `path/to/file`
- **Description**: [Description]
- **Dependencies**: None

### Testing Strategy
- [Testing Approach]
"""
    
    with open(plan_path, "w") as f:
        f.write(content)
    
    print(f"Created feature plan template at: {plan_path}")

if __name__ == "__main__":
    main()
