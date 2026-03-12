#!/usr/bin/env python3
"""
Wrapper for Perplexity Search as described in SKILL.md
"""
import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Perplexity AI Search Wrapper")
    parser.add_argument("--ask", help="Quick question with AI answer (sonar)")
    parser.add_argument("--search", help="Direct web search - ranked results without AI synthesis")
    parser.add_argument("--research", help="AI-synthesized research (sonar-pro)")
    parser.add_argument("--reason", help="Chain-of-thought reasoning (sonar-reasoning-pro)")
    parser.add_argument("--deep", help="Deep comprehensive research (sonar-deep-research)")

    parser.add_argument("--max-results", type=int, default=10, help="Number of results (1-20)")
    parser.add_argument("--recency", choices=["day", "week", "month", "year"], help="Time filter")
    parser.add_argument("--domains", help="Limit to specific domains")

    args = parser.parse_args()

    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        print("Warning: PERPLEXITY_API_KEY not found in environment.", file=sys.stderr)

    print("Executing Perplexity Search...")
    # This is a stub for the actual API call logic
    if args.ask:
        print(f"Model: sonar\nQuery: {args.ask}")
    elif args.search:
        print(f"Model: None (Raw Search)\nQuery: {args.search}")
        print(f"Max Results: {args.max_results}, Recency: {args.recency}")
    elif args.research:
        print(f"Model: sonar-pro\nQuery: {args.research}")
    elif args.reason:
        print(f"Model: sonar-reasoning-pro\nQuery: {args.reason}")
    elif args.deep:
        print(f"Model: sonar-deep-research\nQuery: {args.deep}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
