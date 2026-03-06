#!/usr/bin/env python3
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Query Venue Templates")
    parser.add_argument("--venue", help="Name of the venue (e.g., Nature, NeurIPS)")
    parser.add_argument("--type", help="Type of document (e.g., article, poster, grant)")
    parser.add_argument("--keyword", help="Search keyword")
    parser.add_argument("--list-all", action="store_true", help="List all available templates")
    parser.add_argument("--requirements", action="store_true", help="Show requirements for the venue")

    args = parser.parse_args()

    if args.list_all:
        print("Available templates (simulated):")
        print("- assets/journals/nature_article.tex")
        print("- assets/journals/neurips_article.tex")
        print("- assets/posters/beamerposter_academic.tex")
        print("- assets/grants/nsf_proposal_template.tex")
        return

    if args.requirements and args.venue:
        print(f"Requirements for {args.venue} (simulated):")
        if args.venue.lower() == "nature":
            print("- Page limit: ~5 pages")
            print("- Citations: Numbered superscript")
        elif args.venue.lower() == "neurips":
            print("- Page limit: 8 pages + refs")
            print("- Anonymization: Required for initial submission")
        else:
            print(f"Loading requirements from references/...")
        return

    if args.venue:
        print(f"Template for {args.venue} (simulated): assets/journals/{args.venue.lower()}_article.tex")
    elif args.keyword:
        print(f"Found templates for keyword '{args.keyword}' (simulated):")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
