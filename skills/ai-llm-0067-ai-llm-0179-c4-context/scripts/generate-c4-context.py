#!/usr/bin/env python3
import argparse
import os

TEMPLATE = """# C4 Context Level: {name}

## System Overview

### Short Description
{short_description}

### Long Description
{long_description}

## Personas

### User
- **Type**: Human User
- **Description**: Standard user
- **Goals**: Accomplish tasks
- **Key Features Used**: Main features

## System Features

### Feature 1
- **Description**: What it does
- **Users**: User

## User Journeys

### Main Journey
1. Step 1: Description
2. Step 2: Description

## External Systems and Dependencies

### External System 1
- **Type**: API
- **Description**: External service
- **Integration Type**: REST
- **Purpose**: Why it's needed

## System Context Diagram

```mermaid
C4Context
    title System Context Diagram for {name}

    Person(user, "User", "Uses the system")
    System(system, "{name}", "{short_description}")
    System_Ext(external1, "External System 1", "External service")

    Rel(user, system, "Uses")
    Rel(system, external1, "Uses", "API")
```
"""

def main():
    parser = argparse.ArgumentParser(description='Generate a C4 Context documentation file.')
    parser.add_argument('name', help='System name')
    parser.add_argument('--short', default='[One-sentence description]', help='Short description')
    parser.add_argument('--long', default='[Detailed description]', help='Long description')
    parser.add_argument('--output', help='Output file path')

    args = parser.parse_args()

    content = TEMPLATE.format(
        name=args.name,
        short_description=args.short,
        long_description=args.long
    )

    output_path = args.output or f"c4-context-{args.name.lower().replace(' ', '-')}.md"
    
    with open(output_path, 'w') as f:
        f.write(content)
    
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
