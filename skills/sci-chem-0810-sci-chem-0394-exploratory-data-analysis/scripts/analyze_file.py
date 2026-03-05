#!/usr/bin/env python3
import argparse
import os
import sys
import json
from datetime import datetime

try:
    import pandas as pd
except ImportError:
    print("Error: pandas not found. Please install it with 'pip install pandas'.")
    sys.exit(1)

def analyze_tabular(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == '.csv':
        df = pd.read_csv(filepath)
    elif ext in ['.tsv', '.txt']:
        df = pd.read_csv(filepath, sep='\t')
    else:
        print(f"Unsupported tabular format: {ext}")
        return None
    
    report = {
        "filename": os.path.basename(filepath),
        "timestamp": str(datetime.now()),
        "shape": df.shape,
        "columns": list(df.columns),
        "dtypes": df.dtypes.apply(lambda x: str(x)).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "summary_stats": df.describe().to_dict()
    }
    return report

def generate_markdown_report(report):
    md = f"# EDA Report: {report['filename']}\n\n"
    md += f"- **Date**: {report['timestamp']}\n"
    md += f"- **Dimensions**: {report['shape'][0]} rows, {report['shape'][1]} columns\n\n"
    
    md += "## Column Information\n"
    md += "| Column | Type | Missing Values |\n"
    md += "|--------|------|----------------|\n"
    for col in report['columns']:
        md += f"| {col} | {report['dtypes'][col]} | {report['missing_values'][col]} |\n"
    
    md += "\n## Summary Statistics\n"
    stats_df = pd.DataFrame(report['summary_stats'])
    md += stats_df.to_markdown()
    
    return md

def main():
    parser = argparse.ArgumentParser(description='Perform Exploratory Data Analysis on scientific files.')
    parser.add_argument('filepath', help='Path to the file to analyze')
    parser.add_argument('--output', help='Output report file name (.md)')

    args = parser.parse_args()

    if not os.path.exists(args.filepath):
        print(f"Error: File {args.filepath} not found.")
        sys.exit(1)

    ext = os.path.splitext(args.filepath)[1].lower()
    
    if ext in ['.csv', '.tsv', '.txt']:
        report = analyze_tabular(args.filepath)
        if report:
            md_report = generate_markdown_report(report)
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(md_report)
                print(f"Report saved to {args.output}")
            else:
                print(md_report)
    else:
        print(f"Currently, this helper script only supports CSV/TSV formats for direct analysis.")
        print(f"For {ext} files, please refer to the specific reference in the SKILL.md.")

if __name__ == "__main__":
    main()
