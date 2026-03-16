#!/usr/bin/env python3
"""
Copywriting Framework Generator
Generates structured outlines for copywriting based on popular frameworks (AIDA, PAS, BAB).
"""
import sys
import argparse

def generate_aida(product, audience):
    """Attention, Interest, Desire, Action"""
    print(f"# AIDA Framework for '{product}' targeting '{audience}'\n")
    print("## Attention (Hook)")
    print("[Grab the reader's attention with a bold statement, question, or fact.]\n")
    print("## Interest (Problem/Solution)")
    print("[Keep them reading by explaining the problem and introducing the solution.]\n")
    print("## Desire (Benefits)")
    print("[Make them want it by explaining the benefits and showing proof/testimonials.]\n")
    print("## Action (CTA)")
    print("[Tell them exactly what to do next to get it.]\n")

def generate_pas(product, audience):
    """Problem, Agitation, Solution"""
    print(f"# PAS Framework for '{product}' targeting '{audience}'\n")
    print("## Problem (Pain Point)")
    print("[Clearly state the problem your audience is facing right now.]\n")
    print("## Agitation (Make it hurt)")
    print("[Emphasize the negative consequences of not solving the problem. Pour salt on the wound.]\n")
    print("## Solution (Your Product)")
    print("[Present your product as the ultimate fix to their pain.]\n")
    print("## Action (CTA)")
    print("[Tell them what to do next.]\n")

def generate_bab(product, audience):
    """Before, After, Bridge"""
    print(f"# BAB Framework for '{product}' targeting '{audience}'\n")
    print("## Before (Current State)")
    print("[Describe their world now, with the problem they're facing.]\n")
    print("## After (Future State)")
    print("[Describe the ideal world where the problem is completely solved.]\n")
    print("## Bridge (The Solution)")
    print("[Show how your product bridges the gap between the Before and the After.]\n")
    print("## Action (CTA)")
    print("[Tell them what to do next.]\n")

def main():
    parser = argparse.ArgumentParser(description="Copywriting Framework Generator")
    parser.add_argument("--product", required=True, help="Name of the product or service")
    parser.add_argument("--audience", required=True, help="Target audience description")
    parser.add_argument("--framework", choices=['aida', 'pas', 'bab'], default='aida', help="Copywriting framework to use (default: aida)")

    args = parser.parse_args()

    if args.framework == 'aida':
        generate_aida(args.product, args.audience)
    elif args.framework == 'pas':
        generate_pas(args.product, args.audience)
    elif args.framework == 'bab':
        generate_bab(args.product, args.audience)

if __name__ == "__main__":
    main()
