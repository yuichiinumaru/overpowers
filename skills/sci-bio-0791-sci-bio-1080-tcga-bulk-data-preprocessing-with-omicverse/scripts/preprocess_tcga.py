import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="TCGA bulk data preprocessing with omicverse")
    parser.add_argument("--sample-sheet", required=True, help="Path to TCGA sample sheet (TSV)")
    parser.add_argument("--download-dir", required=True, help="Path to decompressed expression archives directory")
    parser.add_argument("--clinical-dir", required=True, help="Path to clinical cart directory")
    parser.add_argument("--output-prefix", default="ov_tcga", help="Output prefix for generated files")
    parser.add_argument("--plot", action="store_true", help="Generate survival plots")
    parser.add_argument("--gene", help="Specific gene for survival plot")

    args = parser.parse_args()

    try:
        import omicverse as ov
        import scanpy as sc
    except ImportError:
        print("Error: omicverse or scanpy not installed. Please install with: pip install omicverse scanpy", file=sys.stderr)
        sys.exit(1)

    print(f"Initializing TCGA preprocessing...")
    if args.plot:
        ov.plot_set()

    # Initialize the helper
    aml_tcga = ov.bulk.pyTCGA(args.sample_sheet, args.download_dir, args.clinical_dir)

    print("Building AnnData object...")
    aml_tcga.adata_init()

    raw_path = f"{args.output_prefix}_raw.h5ad"
    print(f"Saving raw AnnData to {raw_path}...")
    aml_tcga.adata.write_h5ad(raw_path, compression='gzip')

    print("Initializing metadata and clinical information...")
    aml_tcga.adata_meta_init()
    aml_tcga.survial_init() # Note spelling 'survial'

    if args.plot and args.gene:
        print(f"Plotting survival curve for {args.gene}...")
        aml_tcga.survival_analysis(args.gene, layer='deseq_normalize', plot=True)
    elif args.plot:
        print("Running survival analysis for all genes (this may take time)...")
        aml_tcga.survial_analysis_all()

    final_path = f"{args.output_prefix}_survival_all.h5ad"
    print(f"Exporting results to {final_path}...")
    aml_tcga.adata.write_h5ad(final_path, compression='gzip')
    print("Done!")

if __name__ == "__main__":
    main()
