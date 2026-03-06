#!/usr/bin/env python3
import argparse
import os

def generate_template(name, description, comp_type, tech):
    template = f"""# C4 Component Level: {name}

## Overview

- **Name**: {name}
- **Description**: {description}
- **Type**: {comp_type}
- **Technology**: {tech}

## Purpose

[Detailed description of what this component does and what problems it solves]

## Software Features

- [Feature 1]: [Description]
- [Feature 2]: [Description]
- [Feature 3]: [Description]

## Code Elements

This component contains the following code-level elements:

- [c4-code-file-1.md](./c4-code-file-1.md) - [Description]

## Interfaces

### [Interface Name]

- **Protocol**: [REST/GraphQL/gRPC/Events/etc.]
- **Description**: [What this interface provides]
- **Operations**:
  - `operationName(params): ReturnType` - [Description]

## Dependencies

### Components Used

- [Component Name]: [How it's used]

### External Systems

- [External System]: [How it's used]

## Component Diagram

```mermaid
C4Component
    title Component Diagram for {name}

    Container_Boundary(container, "{name} Container") {{
        Component(comp1, "{name} Core", "{comp_type}", "{description}")
    }}
```
"""
    return template

def main():
    parser = argparse.ArgumentParser(description='Generate a C4 Component documentation template.')
    parser.add_argument('--name', help='Component name')
    parser.add_argument('--desc', help='Short description')
    parser.add_argument('--type', help='Component type (Application, Service, Library, etc.)')
    parser.add_argument('--tech', help='Primary technologies used')
    parser.add_argument('--output', help='Output file name', default='C4-COMPONENT.md')

    args = parser.parse_args()

    name = args.name or input("Component Name: ")
    desc = args.desc or input("Description: ")
    comp_type = args.type or input("Type (Service/Library/etc): ")
    tech = args.tech or input("Technology: ")

    content = generate_template(name, desc, comp_type, tech)
    
    with open(args.output, 'w') as f:
        f.write(content)
    
    print(f"Generated {args.output}")

if __name__ == "__main__":
    main()
