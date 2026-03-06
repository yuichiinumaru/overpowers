#!/usr/bin/env python3
"""
Micro-SaaS Launch Checklist Generator
Generates a step-by-step checklist to go from idea to MVP launch for indie hackers.
"""
import sys
import argparse

def generate_checklist(product_name):
    """
    Generate a markdown checklist for Micro-SaaS launch.
    """
    print(f"# Micro-SaaS Launch Checklist: {product_name}\n")

    print("## Phase 1: Idea Validation (1 Week)")
    print("- [ ] Define the specific problem you are solving.")
    print("- [ ] Identify your exact target audience (niche down).")
    print("- [ ] Speak to 5-10 people in that audience to confirm the pain point.")
    print("- [ ] Check competitors: If there are none, it might not be a good market. If there are many, find your angle.")

    print("\n## Phase 2: The Landing Page (2 Days)")
    print("- [ ] Buy a domain name.")
    print("- [ ] Set up a simple landing page (e.g., Carrd, Webflow).")
    print("- [ ] Write clear copy: Problem -> Solution -> Benefit -> Call to Action.")
    print("- [ ] Add an email capture form for early access/waitlist.")

    print("\n## Phase 3: Build the MVP (2-4 Weeks)")
    print("- [ ] Scope down features. What is the absolutely minimum required to solve the core problem?")
    print("- [ ] Choose your stack: Stick to what you know best to build fast.")
    print("- [ ] Integrate payment processing (e.g., Stripe) from Day 1.")
    print("- [ ] Set up basic analytics (e.g., Plausible, PostHog).")

    print("\n## Phase 4: Launch & Distribution")
    print("- [ ] Email your waitlist: Offer an early-bird discount.")
    print("- [ ] Launch on Product Hunt.")
    print("- [ ] Share your journey on Indie Hackers / Twitter (Build in Public).")
    print("- [ ] Post in relevant niche communities (Reddit, Discord, Facebook Groups) where your audience hangs out.")

    print("\n## Phase 5: Iterate & Grow")
    print("- [ ] Talk to your first paying customers. Why did they buy?")
    print("- [ ] Fix critical bugs immediately.")
    print("- [ ] Focus on one marketing channel that works and double down.")
    print("- [ ] Set up automated onboarding emails.")

def main():
    parser = argparse.ArgumentParser(description="Micro-SaaS Launch Checklist Generator")
    parser.add_argument("--product", required=True, help="Name of your Micro-SaaS product")

    args = parser.parse_args()

    generate_checklist(args.product)

if __name__ == "__main__":
    main()
