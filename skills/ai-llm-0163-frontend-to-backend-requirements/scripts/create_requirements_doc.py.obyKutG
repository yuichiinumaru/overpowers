#!/usr/bin/env python3
import sys
import os
from pathlib import Path

def create_requirements_doc(feature_name):
    target_dir = Path(f".claude/docs/ai/{feature_name}")
    target_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = target_dir / "backend-requirements.md"
    
    template = f"""# Backend Requirements: {feature_name}

## Context
[What we're building, who it's for, what problem it solves]

## Screens/Components

### [Screen Name]
**Purpose**: What this screen does

**Data I need to display**:
- [Description of data piece]

**Actions**:
- [Action description] → [Expected outcome]

**States to handle**:
- **Empty**: [When/why]
- **Loading**: [What's being fetched]
- **Error**: [What user sees]

**Business rules affecting UI**:
- [Rule]

## Uncertainties
- [ ] TBD

## Questions for Backend
- [ ] TBD

## Discussion Log
[Backend responses, decisions made]
"""
    with open(file_path, "w") as f:
        f.write(template)
    
    print(f"Created requirements document: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: create_requirements_doc.py <feature-name>")
        sys.exit(1)
    create_requirements_doc(sys.argv[1])
