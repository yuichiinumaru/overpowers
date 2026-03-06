import omicverse as ov
import scanpy as sc
import argparse
import pandas as pd

def run_bulktrajblend(bulk_file, single_file, celltype_key, target_lineage, output_prefix):
    print("🧬 Starting BulkTrajBlend trajectory interpolation...")
    ov.plot_set()
    
    print(f"📥 Loading bulk data: {bulk_file}")
    bulk_df = pd.read_csv(bulk_file, index_col=0)
    
    print(f"📥 Loading single-cell atlas: {single_file}")
    adata = sc.read_h5ad(single_file)
    
    print("🚀 Initializing BulkTrajBlend...")
    # Simplified initialization
    bulktb = ov.bulk2single.BulkTrajBlend(
        bulk_seq=bulk_df, 
        single_seq=adata, 
        celltype_key=celltype_key
    )
    
    print(f"🌉 Interpolating {target_lineage} lineage...")
    # This requires a trained model in practice
    # bulktb.interpolation(target_lineage)
    
    print("✨ BulkTrajBlend object initialized.")
    return bulktb

def main():
    parser = argparse.ArgumentParser(description="BulkTrajBlend trajectory interpolation.")
    parser.add_argument("--bulk", required=True, help="Bulk counts CSV")
    parser.add_argument("--single", required=True, help="Single-cell atlas H5AD")
    parser.add_argument("--celltype-key", default="clusters", help="Column with cell types")
    parser.add_argument("--target", required=True, help="Target lineage to interpolate")
    parser.add_argument("--output", default="traj", help="Output prefix")
    
    args = parser.parse_args()
    run_bulktrajblend(args.bulk, args.single, args.celltype_key, args.target, args.output)

if __name__ == "__main__":
    main()
