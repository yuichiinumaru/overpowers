#!/usr/bin/env python3
import argparse
import os

def generate_template(name, short_desc):
    template = f"""# C4 Context Level: {name}

## System Overview

### Short Description

{short_desc}

### Long Description

[Detailed description of the system's purpose, capabilities, and the problems it solves]

## Personas

### Primary User

- **Type**: Human User
- **Description**: [Who this persona is and what they need]
- **Goals**: [What this persona wants to achieve]
- **Key Features Used**: [List of features this persona uses]

## System Features

### Core Feature

- **Description**: [What this feature does]
- **Users**: Primary User
- **User Journey**: [Link to user journey map]

## External Systems and Dependencies

### External API

- **Type**: API
- **Description**: [What this external system provides]
- **Integration Type**: API
- **Purpose**: [Why the system depends on this]

## System Context Diagram

```mermaid
C4Context
    title System Context Diagram for {name}

    Person(user, "User", "Uses {name}")
    System(system, "{name}", "{short_desc}")
    
    Rel(user, system, "Uses")
```

## Related Documentation

- [Container Documentation](./c4-container.md)
- [Component Documentation](./c4-component.md)
"""
    return template

def main():
    parser = argparse.ArgumentParser(description='Generate a C4 Context documentation template.')
    parser.add_argument('--name', help='System name')
    parser.add_argument('--desc', help='Short description')
    parser.add_argument('--output', help='Output file name', default='C4-CONTEXT.md')

    args = parser.parse_args()

    name = args.name or input("System Name: ")
    short_desc = args.desc or input("Short Description: ")

    content = generate_template(name, short_desc)
    
    with open(args.output, 'w') as f:
        f.write(content)
    
    print(f"Generated {args.output}")

if __name__ == "__main__":
    main()
