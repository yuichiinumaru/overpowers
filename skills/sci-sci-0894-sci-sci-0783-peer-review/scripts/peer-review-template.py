#!/usr/bin/env python3
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Generate a peer review template")
    parser.add_argument('--title', default="Manuscript Title", help="Title of the manuscript")
    parser.add_argument('--authors', default="Authors", help="Authors of the manuscript")
    parser.add_argument('--journal', default="Journal Name", help="Target journal")
    parser.add_argument('--type', choices=["article", "review", "grant"], default="article", help="Type of review")

    args = parser.parse_args()

    template = f"""# Peer Review Report

**Manuscript Title:** {args.title}
**Authors:** {args.authors}
**Journal/Venue:** {args.journal}
**Review Type:** {args.type.capitalize()}

## 1. Summary of the Work
[Provide a brief 1-2 paragraph summary of the manuscript's main objective, methodology, and key findings. This demonstrates to the authors and editor that you have understood the work.]

## 2. General Impression and Major Comments
[Provide your overall assessment of the work's significance, novelty, and validity. Highlight the major strengths and fundamental flaws that need addressing before publication.]

### Major Issue 1: [Title of issue]
[Detailed explanation of the issue, why it's a problem, and specific recommendations on how to address it.]

### Major Issue 2: [Title of issue]
[Detailed explanation...]

## 3. Methodology and Statistical Evaluation
- **Experimental Design:** [Assess whether the design is appropriate to answer the research question]
- **Statistical Rigor:** [Evaluate the statistical methods used, sample size justification, and interpretation of p-values/effect sizes]
- **Reproducibility:** [Assess if the methods are described with sufficient detail to allow replication]

## 4. Minor Comments
[List minor issues such as typos, formatting errors, unclear phrasing, missing citations, or small clarifications needed.]
1. Page X, Line Y: ...
2. Figure Z: ...

## 5. Recommendation
[ ] Accept without revisions
[ ] Minor revisions
[ ] Major revisions
[ ] Reject
"""
    print(template)

if __name__ == '__main__':
    main()
