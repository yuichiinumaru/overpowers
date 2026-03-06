#!/usr/bin/env python3
import argparse

CHECKLIST = [
    ("Title Tags", "Are they descriptive, containing keywords, and under 60 chars?"),
    ("Meta Descriptions", "Are they compelling and under 160 chars?"),
    ("Header Tags (H1-H6)", "Is there a logical structure? One H1 per page?"),
    ("URL Structure", "Are URLs short, descriptive, and using hyphens?"),
    ("Image Alt Text", "Do all informative images have descriptive alt attributes?"),
    ("Internal Linking", "Is there a logical internal link structure?"),
    ("Mobile Responsiveness", "Does the site work well on mobile devices?"),
    ("Page Speed", "Does the page load quickly? (Check Core Web Vitals)"),
    ("Canonical Tags", "Are they implemented to prevent duplicate content?"),
    ("robots.txt", "Is it correctly configured? Not blocking important pages?"),
    ("Sitemap.xml", "Does it exist and is it up-to-date?")
]

def main():
    parser = argparse.ArgumentParser(description="Generate a markdown SEO Audit Checklist.")
    parser.add_argument("--url", required=True, help="Target URL being audited")
    parser.add_argument("--output", help="Output markdown file")

    args = parser.parse_args()

    markdown = f"# SEO Audit Review: {args.url}\n\n"
    markdown += "## Technical & On-Page Checklist\n\n"

    for item, desc in CHECKLIST:
        markdown += f"### [ ] {item}\n"
        markdown += f"**Check**: {desc}\n\n"
        markdown += "**Findings**:\n"
        markdown += "- (Add notes here)\n\n"
        markdown += "**Recommendations**:\n"
        markdown += "- (Add action items here)\n\n"
        markdown += "---\n\n"

    if args.output:
        with open(args.output, "w") as f:
            f.write(markdown)
        print(f"Audit checklist generated at {args.output}")
    else:
        print(markdown)

if __name__ == "__main__":
    main()
