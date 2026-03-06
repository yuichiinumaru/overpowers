#!/usr/bin/env python3
import sys

def main():
    checklist = """## Email Composition Checklist

Please review your email against this checklist before sending:

- [ ] Clear, specific subject line
- [ ] Appropriate greeting
- [ ] Purpose stated upfront
- [ ] Key points organized with bullets/numbers
- [ ] Clear call to action or next steps
- [ ] Appropriate tone for audience
- [ ] Proofread for typos
- [ ] Attachments included (if mentioned)
- [ ] Recipients correct (To, CC, BCC)
- [ ] Professional signature
"""

    with open("email_checklist.md", "w") as f:
        f.write(checklist)
    print("Generated email_checklist.md in the current directory.")

if __name__ == "__main__":
    main()
