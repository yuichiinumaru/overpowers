#!/usr/bin/env python3
import sys
import argparse

def generate_launch_playbook():
    return """
# Micro-SaaS Launch Playbook

## Week 1: Core MVP
- [ ] Day 1-2: Auth + basic UI
- [ ] Day 3-4: Core feature (one thing)
- [ ] Day 5-6: Stripe integration
- [ ] Day 7: Polish and bug fixes

## Week 2: Launch Ready
- [ ] Day 1-2: Landing page
- [ ] Day 3: Email flows (welcome, etc.)
- [ ] Day 4: Legal (privacy, terms)
- [ ] Day 5: Final testing
- [ ] Day 6-7: Soft launch

## Post-Launch Focus
- [ ] Get first paying customer
- [ ] Gather user feedback
- [ ] Fix critical bugs only (ignore feature requests initially)
- [ ] Iterate based on paying user feedback

**Remember**: Ship fast, don't build in secret, and charge based on value.
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Micro-SaaS Launch Playbook template.")
    parser.add_argument("--out", help="Output file (optional)")

    args = parser.parse_args()

    playbook = generate_launch_playbook()

    if args.out:
        with open(args.out, 'w') as f:
            f.write(playbook)
        print(f"Generated Micro-SaaS playbook at {args.out}")
    else:
        print(playbook)
