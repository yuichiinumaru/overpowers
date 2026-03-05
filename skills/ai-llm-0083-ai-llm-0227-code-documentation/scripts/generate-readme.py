#!/usr/bin/env python3
import argparse
import os

TEMPLATE = """# {name}

{description}

## Quick Start

```bash
npm install
npm run dev
```

## Installation

Detailed installation instructions...

## Usage

```typescript
import {{ something }} from '{name}';

// Example usage
const result = something.doThing();
```

## API Reference

### `functionName(param: Type): ReturnType`

Description of what the function does.

**Parameters:**
- `param` - Description of parameter

**Returns:** Description of return value

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `option1` | `string` | `'default'` | What it does |

## Contributing

How to contribute...

## License

MIT
"""

def main():
    parser = argparse.ArgumentParser(description='Generate a standard README.md')
    parser.add_argument('name', help='Project name')
    parser.add_argument('--description', default='[Project description]', help='Project description')
    parser.add_argument('--output', default='README.md', help='Output file path')

    args = parser.parse_args()

    content = TEMPLATE.format(
        name=args.name,
        description=args.description
    )

    with open(args.output, 'w') as f:
        f.write(content)
    
    print(f"Generated {args.output}")

if __name__ == "__main__":
    main()
