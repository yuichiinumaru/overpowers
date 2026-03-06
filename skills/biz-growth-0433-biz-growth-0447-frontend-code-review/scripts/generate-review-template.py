#!/usr/bin/env python3
import sys

def print_template_a():
    template = """# Code review
Found <N> urgent issues need to be fixed:

## 1 <brief description of bug>
FilePath: <path> line <line>
<relevant code snippet or pointer>


### Suggested fix
<brief description of suggested fix>

---

Found <M> suggestions for improvement:

## 1 <brief description of suggestion>
FilePath: <path> line <line>
<relevant code snippet or pointer>


### Suggested fix
<brief description of suggested fix>

---

Would you like me to use the Suggested fix section to address these issues?
"""
    print(template)

def print_template_b():
    template = """## Code review
No issues found.
"""
    print(template)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "A":
        print_template_a()
    elif len(sys.argv) > 1 and sys.argv[1] == "B":
        print_template_b()
    else:
        print("Usage: ./generate-review-template.py [A|B]")
        print("  A: Template A (issues found)")
        print("  B: Template B (no issues found)")
