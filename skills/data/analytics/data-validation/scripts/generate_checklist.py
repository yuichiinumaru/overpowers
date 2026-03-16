#!/usr/bin/env python3
"""
Data Validation Checklist Generator
Generates a markdown checklist for data validation based on the SKILL.md.

Usage:
  python3 generate_checklist.py --output validation_checklist.md
"""

import argparse
import sys
import datetime

def generate_checklist(output_file):
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    content = f"""# Data Validation Checklist ({date_str})

## Pre-Delivery QA Checklist

### Data Quality Checks
- [ ] **Source verification**: Confirmed which tables/data sources were used.
- [ ] **Freshness**: Data is current enough for the analysis.
- [ ] **Completeness**: No unexpected gaps in time series.
- [ ] **Null handling**: Checked null rates and handled appropriately.
- [ ] **Deduplication**: Confirmed no double-counting.
- [ ] **Filter verification**: All WHERE clauses are correct.

### Calculation Checks
- [ ] **Aggregation logic**: GROUP BY includes all non-aggregated columns.
- [ ] **Denominator correctness**: Denominators are non-zero and correct.
- [ ] **Date alignment**: Comparisons use the same time period.
- [ ] **Join correctness**: JOIN types are appropriate (INNER vs LEFT).
- [ ] **Metric definitions**: Metrics match stakeholder definitions.
- [ ] **Subtotals sum**: Parts add up to the whole.

### Reasonableness Checks
- [ ] **Magnitude**: Numbers are in a plausible range.
- [ ] **Trend continuity**: No unexplained jumps or drops.
- [ ] **Cross-reference**: Key numbers match other known sources.
- [ ] **Order of magnitude**: Total figures are in the right ballpark.
- [ ] **Edge cases**: Boundaries handled correctly.

### Presentation Checks
- [ ] **Chart accuracy**: Bar charts start at zero, axes labeled.
- [ ] **Number formatting**: Appropriate precision.
- [ ] **Title clarity**: Titles state the insight.
- [ ] **Caveat transparency**: Known limitations stated.
- [ ] **Reproducibility**: Someone else could recreate this analysis.
"""
    try:
        with open(output_file, 'w') as f:
            f.write(content)
        print(f"Checklist generated at {output_file}")
    except Exception as e:
        print(f"Error generating checklist: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Data Validation Checklist Generator")
    parser.add_argument("--output", default="validation_checklist.md", help="Output file path")
    args = parser.parse_args()

    generate_checklist(args.output)

if __name__ == "__main__":
    main()
