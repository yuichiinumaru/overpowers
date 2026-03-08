import argparse
import pandas as pd
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
import os

def run_deseq2(counts_file: str, metadata_file: str, design_factors: str,
               ref_level: str = None, test_level: str = None,
               min_counts: int = 10, output_dir: str = "results"):
    """
    Run DESeq2 analysis on RNA-seq count data using PyDESeq2.
    """
    print(f"Loading data...")
    try:
        # Load counts (expecting samples as rows, genes as columns)
        # If genes are rows, it needs transposition
        counts = pd.read_csv(counts_file, index_col=0)
        metadata = pd.read_csv(metadata_file, index_col=0)
    except Exception as e:
        print(f"Error loading files: {e}")
        return False

    print(f"Loaded {counts.shape[0]} samples and {counts.shape[1]} genes.")
    print(f"Loaded metadata for {metadata.shape[0]} samples.")

    # Align indices
    common_samples = counts.index.intersection(metadata.index)
    if len(common_samples) < len(counts.index):
        print(f"Warning: Only {len(common_samples)} samples matched between counts and metadata.")
        counts = counts.loc[common_samples]
        metadata = metadata.loc[common_samples]

    # Filter low count genes
    keep_genes = counts.sum(axis=0) >= min_counts
    counts = counts.loc[:, keep_genes]
    print(f"Filtered to {counts.shape[1]} genes with >= {min_counts} total counts.")

    # Initialize DESeq2 Dataset
    print(f"Initializing DESeq2 with design factor: {design_factors}")
    try:
        dds = DeseqDataSet(
            counts=counts,
            metadata=metadata,
            design_factors=design_factors,
            refit_cooks=True,
            n_cpus=8
        )

        # Fit models
        print("Fitting dispersion and calculating size factors...")
        dds.deseq2()

        # Create contrast if specified
        contrast = None
        if ref_level and test_level:
            print(f"Testing contrast: {design_factors} {test_level} vs {ref_level}")
            contrast = [design_factors, test_level, ref_level]
        else:
            print(f"Testing primary factor: {design_factors}")

        # Run statistical tests
        print("Running statistical tests...")
        stat_res = DeseqStats(dds, contrast=contrast, n_cpus=8)
        stat_res.summary()

        # LFC Shrinkage (optional but recommended)
        print("Applying LFC shrinkage...")
        stat_res.lfc_shrink(coeff=stat_res.coef_name)

        # Save results
        os.makedirs(output_dir, exist_ok=True)
        results_df = stat_res.results_df

        out_file = os.path.join(output_dir, "deseq2_results.csv")
        results_df.to_csv(out_file)
        print(f"Saved complete results to {out_file}")

        # Filter significant genes (padj < 0.05 and |log2FC| > 1)
        sig_genes = results_df[(results_df.padj < 0.05) & (results_df.log2FoldChange.abs() > 1)]
        sig_file = os.path.join(output_dir, "significant_genes.csv")
        sig_genes.to_csv(sig_file)
        print(f"Saved {len(sig_genes)} significant genes to {sig_file}")

        return True

    except Exception as e:
        print(f"DESeq2 analysis failed: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run DESeq2 analysis using PyDESeq2")
    parser.add_argument("--counts", required=True, help="Path to raw counts CSV (samples as rows, genes as columns)")
    parser.add_argument("--metadata", required=True, help="Path to metadata CSV (samples as rows, conditions as columns)")
    parser.add_argument("--design", required=True, help="Column name in metadata to use for design")
    parser.add_argument("--ref", help="Reference level for contrast (e.g., 'Control')")
    parser.add_argument("--test", help="Test level for contrast (e.g., 'Treatment')")
    parser.add_argument("--min_counts", type=int, default=10, help="Minimum total counts per gene")
    parser.add_argument("--outdir", default="results", help="Output directory")

    args = parser.parse_args()

    run_deseq2(
        counts_file=args.counts,
        metadata_file=args.metadata,
        design_factors=args.design,
        ref_level=args.ref,
        test_level=args.test,
        min_counts=args.min_counts,
        output_dir=args.outdir
    )
