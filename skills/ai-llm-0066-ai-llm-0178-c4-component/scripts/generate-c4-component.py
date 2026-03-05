#!/usr/bin/env python3
import argparse
import os

TEMPLATE = """# C4 Component Level: {name}

## Overview

- **Name**: {name}
- **Description**: {description}
- **Type**: {type}
- **Technology**: {technology}

## Purpose

{purpose}

## Software Features

- Feature 1: Description
- Feature 2: Description

## Code Elements

- [c4-code-file-1.md](./c4-code-file-1.md) - Description

## Interfaces

### Interface Name

- **Protocol**: REST
- **Description**: Description
- **Operations**:
  - `operationName(params): ReturnType` - Description

## Dependencies

### Components Used

- Component Name: How it's used

### External Systems

- External System: How it's used

## Component Diagram

```mermaid
C4Component
    title Component Diagram for {name}

    Container_Boundary(container, "{name}") {{
        Component(component1, "Component 1", "Type", "Description")
    }}
```
"""

def main():
    parser = argparse.ArgumentParser(description='Generate a C4 Component documentation file.')
    parser.add_argument('name', help='Component name')
    parser.add_argument('--description', default='[Short description]', help='Component description')
    parser.add_argument('--type', default='Service', help='Component type')
    parser.add_argument('--tech', default='Python', help='Primary technology')
    parser.add_argument('--purpose', default='[Detailed description]', help='Detailed purpose')
    parser.add_argument('--output', help='Output file path')

    args = parser.parse_args()

    content = TEMPLATE.format(
        name=args.name,
        description=args.description,
        type=args.type,
        technology=args.tech,
        purpose=args.purpose
    )

    output_path = args.output or f"c4-component-{args.name.lower().replace(' ', '-')}.md"
    
    with open(output_path, 'w') as f:
        f.write(content)
    
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
