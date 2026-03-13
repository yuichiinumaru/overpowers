#!/usr/bin/env python3
import sys
import os

def init_doc(title):
    template = f"""# Documentation: {title}

## 1. Overview
[High-level summary of the component/service]

## 2. Key Features
- [Feature 1]
- [Feature 2]

## 3. Usage Examples
```typescript
// Example 1
import {{ thing }} from '@/lib/thing';
const result = thing();
```

## 4. API Reference
| Name | Type | Description |
|------|------|-------------|
| prop | string | purpose |

## 5. Maintenance
- [x] Last updated: [Date]
- [ ] Next review: [Date]
"""
    with open("DOCS.md", "w") as f:
        f.write(template)
    print("Initialized DOCS.md")

if __name__ == "__main__":
    title = sys.argv[1] if len(sys.argv) > 1 else "Component"
    init_doc(title)
