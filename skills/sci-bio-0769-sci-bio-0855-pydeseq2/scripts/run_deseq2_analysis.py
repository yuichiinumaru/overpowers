import argparse
import sys
try:
    import pandas as pd
    from pydeseq2.dds import DeseqDataSet
    from pydeseq2.ds import DeseqStats
except ImportError:
    print("Error: Required packages not installed. Run 'pip install pandas pydeseq2'", file=sys.stderr)
    sys.exit(1)

def run_analysis(counts_file, metadata_file, design, contrast, output_dir, min_counts=10, alpha=0.05):
    print(f"Loading counts from {counts_file} and metadata from {metadata_file}...")

    # Load data
    counts_df = pd.read_csv(counts_file, index_col=0)
    metadata = pd.read_csv(metadata_file, index_col=0)

    # Check orientation and transpose if necessary
    if counts_df.shape[1] < counts_df.shape[0] and len(set(counts_df.columns).intersection(metadata.index)) < len(set(counts_df.index).intersection(metadata.index)):
        print("Transposing counts matrix (assuming rows are genes, columns are samples)")
        counts_df = counts_df.T

    # Align indices
    common_samples = counts_df.index.intersection(metadata.index)
    if len(common_samples) == 0:
        print("Error: No common samples between counts and metadata indices.")
        sys.exit(1)

    counts_df = counts_df.loc[common_samples]
    metadata = metadata.loc[common_samples]
    print(f"Using {len(common_samples)} samples.")

    # Filter genes
    genes_to_keep = counts_df.columns[counts_df.sum(axis=0) >= min_counts]
    counts_df = counts_df[genes_to_keep]
    print(f"Filtering complete. Kept {len(genes_to_keep)} genes with total counts >= {min_counts}.")

    # Initialize DESeq2
    print(f"Initializing DESeq2 with design formula: {design}")
    dds = DeseqDataSet(
        counts=counts_df,
        metadata=metadata,
        design=design,
        refit_cooks=True
    )

    print("Running DESeq2 pipeline...")
    dds.deseq2()

    # Testing
    print(f"Performing Wald test for contrast: {contrast}")
    ds = DeseqStats(dds, contrast=contrast, alpha=alpha)
    ds.summary()

    # Export results
    import os
    os.makedirs(output_dir, exist_ok=True)

    results_file = os.path.join(output_dir, "deseq2_results.csv")
    ds.results_df.to_csv(results_file)
    print(f"Saved full results to {results_file}")

    significant = ds.results_df[ds.results_df.padj < alpha]
    sig_file = os.path.join(output_dir, "significant_genes.csv")
    significant.to_csv(sig_file)
    print(f"Found {len(significant)} significant genes (padj < {alpha}). Saved to {sig_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run PyDESeq2 Analysis")
    parser.add_argument("--counts", required=True, help="Counts CSV file")
    parser.add_argument("--metadata", required=True, help="Metadata CSV file")
    parser.add_argument("--design", required=True, help="Design formula (e.g., '~condition')")
    parser.add_argument("--contrast", nargs=3, required=True, help="Contrast [variable, test_level, ref_level]")
    parser.add_argument("--output", default="results", help="Output directory")
    parser.add_argument("--min-counts", type=int, default=10, help="Minimum total counts to keep a gene")
    parser.add_argument("--alpha", type=float, default=0.05, help="FDR threshold")

    args = parser.parse_args()

    run_analysis(args.counts, args.metadata, args.design, args.contrast, args.output, args.min_counts, args.alpha)
