#!/usr/bin/env python3
import sys
import os

def create_template():
    template = """# Code Review

## Summary of Changes
-

## Security Aspects
- [ ] No hardcoded secrets
- [ ] Proper input validation
- [ ] Output encoding/sanitization
- [ ] Authz/Authn checks where appropriate

## Quality & Maintainability
- [ ] Follows coding standards
- [ ] Meaningful variable/function names
- [ ] Sufficient comments/documentation
- [ ] No dead code

## Testing
- [ ] Unit tests added/updated
- [ ] Edge cases considered
- [ ] Tests pass locally

## Performance
- [ ] No obvious N+1 queries
- [ ] Proper resource cleanup

## Additional Notes
"""

    filename = "REVIEW_TEMPLATE.md"
    if os.path.exists(filename):
        print(f"File {filename} already exists.")
        return

    with open(filename, "w") as f:
        f.write(template)

    print(f"Created {filename}")

if __name__ == "__main__":
    create_template()
