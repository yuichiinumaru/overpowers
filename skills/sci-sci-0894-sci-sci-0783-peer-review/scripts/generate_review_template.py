#!/usr/bin/env python3
"""
Helper script to generate a structured markdown template for peer review.
"""
import argparse
import sys

def generate_template(review_type):
    if review_type == "manuscript":
        return """# Peer Review Report

## Summary Assessment
**Recommendation:** [Accept / Minor Revisions / Major Revisions / Reject]

[Brief paragraph summarizing the manuscript's core contribution, strengths, and primary weaknesses.]

## 1. Major Concerns
*Issues that affect the validity of the conclusions or require significant new work.*

- **[Category e.g., Methodology]:** [Detailed description of the issue]
- **[Category e.g., Data Analysis]:** [Detailed description of the issue]

## 2. Minor Issues
*Issues that can be addressed through text changes, minor re-analysis, or formatting.*

- **Page X, Line Y:** [Specific issue]
- **Figure Z:** [Specific issue with figure]

## 3. Evaluation by Section

### Abstract & Introduction
[Feedback]

### Methods
[Feedback on rigor, reproducibility, controls]

### Results & Figures
[Feedback on data presentation, statistical analysis]

### Discussion & Conclusions
[Feedback on interpretation, limitations, significance]
"""
    elif review_type == "presentation":
        return """# Presentation Review Report

## Summary Statement
[Overall impression, appropriateness for audience, key strengths and weaknesses.]
**Recommendation:** [Ready to present / Minor revisions / Major revisions]

## 1. Layout and Formatting Issues (By Slide)
*Visual design issues identified from image review.*

- **Slide X:** [Issue description e.g., Text overflow making content unreadable]
- **Slide Y:** [Issue description e.g., Insufficient contrast between text and background]

## 2. Content and Structure Feedback
*Feedback on the narrative arc and scientific content.*

- **Narrative Flow:** [Feedback]
- **Clarity of Objectives:** [Feedback]
- **Methods Summary:** [Feedback]
- **Data Presentation:** [Feedback]
- **Conclusions:** [Feedback]

## 3. Design and Accessibility
[Feedback on overall visual appeal, colorblind accessibility, consistency]

## 4. Timing and Scope
[Feedback on slide count vs intended duration, level of detail]
"""
    else:
        return "Unknown review type. Choose 'manuscript' or 'presentation'."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a peer review template")
    parser.add_argument("--type", choices=["manuscript", "presentation"], default="manuscript",
                        help="Type of review template to generate")

    args = parser.parse_args()
    print(generate_template(args.type))
