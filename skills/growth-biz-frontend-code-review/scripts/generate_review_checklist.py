#!/usr/bin/env python3
"""
Frontend Code Review Checklist Generator
Outputs a standard markdown checklist for frontend pull requests.
"""
import sys
import argparse

def generate_checklist():
    """
    Generate standard PR checklist for frontend.
    """
    print("## Frontend Code Review Checklist\n")
    print("### Code Quality")
    print("- [ ] No console.log or debugger statements left in code.")
    print("- [ ] Proper TypeScript typing (avoid `any`).")
    print("- [ ] Components are reasonably sized and follow single-responsibility principle.")
    print("- [ ] Naming conventions are consistent (camelCase for vars/funcs, PascalCase for components).")

    print("\n### Performance")
    print("- [ ] Avoided unnecessary re-renders (useMemo/useCallback used correctly if needed).")
    print("- [ ] Large images are optimized/lazy-loaded.")
    print("- [ ] Third-party libraries are necessary and imported efficiently.")

    print("\n### Accessibility (a11y)")
    print("- [ ] Images have descriptive `alt` tags.")
    print("- [ ] Interactive elements are keyboard accessible (tabindex, focus states).")
    print("- [ ] ARIA labels are used appropriately where semantic HTML falls short.")

    print("\n### Testing")
    print("- [ ] Unit tests cover new utility functions and complex logic.")
    print("- [ ] Component tests cover basic rendering and user interactions.")

    print("\n### Security")
    print("- [ ] User input is sanitized before rendering or submitting.")
    print("- [ ] No sensitive keys or secrets exposed in frontend code.")

def main():
    parser = argparse.ArgumentParser(description="Frontend Code Review Checklist Generator")
    args = parser.parse_args()

    generate_checklist()

if __name__ == "__main__":
    main()
