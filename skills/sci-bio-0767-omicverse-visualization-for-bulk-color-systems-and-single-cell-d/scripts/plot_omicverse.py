import omicverse as ov
import scanpy as sc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

def plot_volcano(csv_file: str, log2fc_col: str, pval_col: str, title: str, out_file: str):
    """Create a volcano plot using OmicVerse."""
    print(f"Reading {csv_file}...")
    try:
        df = pd.read_csv(csv_file, index_col=0)
    except Exception as e:
        print(f"Error reading {csv_file}: {e}")
        return False

    if log2fc_col not in df.columns or pval_col not in df.columns:
        print(f"Error: Columns '{log2fc_col}' or '{pval_col}' not found.")
        print(f"Available columns: {df.columns.tolist()}")
        return False

    print("Generating volcano plot...")

    # Standardizing expected columns for omicverse
    df['log2FoldChange'] = df[log2fc_col]
    df['padj'] = df[pval_col]

    try:
        ov.pl.volcano(
            df,
            x='log2FoldChange',
            y='padj',
            title=title,
            save=out_file
        )
        print(f"Saved volcano plot to {out_file}")
        return True
    except Exception as e:
        print(f"Error creating plot: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create OmicVerse visualizations")
    subparsers = parser.add_subparsers(dest="command", help="Plot type")

    # Volcano plot
    parser_volcano = subparsers.add_parser("volcano", help="Create a volcano plot")
    parser_volcano.add_argument("--input", required=True, help="Input CSV file with differential expression results")
    parser_volcano.add_argument("--logfc", default="log2FoldChange", help="Column name for Log2 Fold Change")
    parser_volcano.add_argument("--pval", default="padj", help="Column name for adjusted p-value")
    parser_volcano.add_argument("--title", default="Volcano Plot", help="Plot title")
    parser_volcano.add_argument("--out", default="volcano_plot.pdf", help="Output PDF file")

    args = parser.parse_args()

    if args.command == "volcano":
        plot_volcano(args.input, args.logfc, args.pval, args.title, args.out)
    else:
        parser.print_help()
