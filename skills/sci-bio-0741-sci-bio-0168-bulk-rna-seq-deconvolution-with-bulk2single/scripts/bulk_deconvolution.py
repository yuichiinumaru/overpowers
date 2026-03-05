import omicverse as ov
import scanpy as sc
import argparse
import pandas as pd

def run_deconvolution(bulk_file, single_file, celltype_key, output_prefix):
    print("🧬 Starting Bulk2Single deconvolution...")
    ov.plot_set()
    
    print(f"📥 Loading bulk data: {bulk_file}")
    bulk_df = pd.read_csv(bulk_file, index_col=0)
    
    print(f"📥 Loading single-cell reference: {single_file}")
    adata = sc.read_h5ad(single_file)
    
    print("🚀 Initializing Bulk2Single model...")
    # Simplified initialization - in practice needs more params
    model = ov.bulk2single.Bulk2Single(
        bulk_data=bulk_df, 
        single_data=adata, 
        celltype_key=celltype_key
    )
    
    print("📊 Estimating cell fractions...")
    fractions = model.predicted_fraction()
    fractions.to_csv(f"{output_prefix}_fractions.csv")
    
    print("✨ Model ready for training and generation.")
    return model

def main():
    parser = argparse.ArgumentParser(description="Bulk RNA-seq deconvolution with Bulk2Single.")
    parser.add_argument("--bulk", required=True, help="Bulk counts CSV")
    parser.add_argument("--single", required=True, help="Single-cell reference H5AD")
    parser.add_argument("--celltype-key", default="clusters", help="Column in single-cell metadata with cell types")
    parser.add_argument("--output", default="deconv", help="Output prefix")
    
    args = parser.parse_args()
    run_deconvolution(args.bulk, args.single, args.celltype_key, args.output)

if __name__ == "__main__":
    main()
