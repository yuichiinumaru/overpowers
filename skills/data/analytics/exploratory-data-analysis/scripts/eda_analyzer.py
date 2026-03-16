import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Perform Exploratory Data Analysis")
    parser.add_argument("filepath", help="Path to scientific data file")
    parser.add_argument("output", nargs="?", help="Output markdown report file")

    args = parser.parse_args()

    if not os.path.exists(args.filepath):
        print(f"Error: File {args.filepath} not found.", file=sys.stderr)
        sys.exit(1)

    _, ext = os.path.splitext(args.filepath)
    ext = ext.lower()

    out_file = args.output if args.output else f"{os.path.basename(args.filepath)}_eda_report.md"

    print(f"Analyzing {args.filepath}...")
    print(f"Detected extension: {ext}")

    # Very basic simulation of the analysis logic
    with open(out_file, 'w') as f:
        f.write(f"# Exploratory Data Analysis Report\n\n")
        f.write(f"**File**: {args.filepath}\n")
        f.write(f"**Type**: {ext}\n\n")

        if ext in ['.csv', '.tsv', '.xlsx']:
            f.write("## Tabular Data Analysis\n")
            try:
                import pandas as pd
                if ext == '.csv': df = pd.read_csv(args.filepath)
                elif ext == '.tsv': df = pd.read_csv(args.filepath, sep='\t')
                else: df = pd.read_excel(args.filepath)
                f.write(f"- Dimensions: {df.shape[0]} rows, {df.shape[1]} columns\n")
                f.write(f"- Columns: {', '.join(df.columns[:5])}...\n")
                f.write(f"- Missing values:\n```\n{df.isnull().sum().head()}\n```\n")
            except Exception as e:
                f.write(f"Failed to parse with pandas: {e}\n")

        elif ext in ['.fasta', '.fastq']:
            f.write("## Sequence Data Analysis\n")
            try:
                from Bio import SeqIO
                fmt = 'fasta' if ext == '.fasta' else 'fastq'
                seqs = list(SeqIO.parse(args.filepath, fmt))
                f.write(f"- Number of sequences: {len(seqs)}\n")
                if seqs:
                    lens = [len(s) for s in seqs]
                    f.write(f"- Average length: {sum(lens)/len(lens):.1f}\n")
            except Exception as e:
                f.write(f"Failed to parse with Biopython: {e}\n")

        else:
            f.write("## General Analysis\n")
            f.write(f"Size: {os.path.getsize(args.filepath)} bytes\n")
            f.write("Advanced parsing requires specific libraries based on format.\n")

        f.write("\n## Recommendations\n")
        f.write("Review specific reference files for advanced analysis of this format.\n")

    print(f"Report generated: {out_file}")

if __name__ == "__main__":
    main()
