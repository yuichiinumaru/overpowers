import omicverse as ov
import anndata
import pandas as pd
import argparse
import sys

def run_combat(input_files, output_h5ad, output_csv):
    print(f"🧬 Starting ComBat batch correction for {len(input_files)} cohorts...")
    ov.ov_plot_set()
    
    adatas = []
    for i, f in enumerate(input_files):
        print(f"📥 Loading batch {i+1}: {f}")
        df = pd.read_csv(f, index_col=0)
        # Assuming genes are rows, samples are columns. AnnData expects samples as rows.
        adata = anndata.AnnData(df.T)
        adata.obs['batch'] = f"batch_{i+1}"
        adatas.append(adata)
        
    print("🔄 Concatenating batches...")
    combined = anndata.concat(adatas, merge='same')
    
    print("🚀 Running ComBat...")
    ov.bulk.batch_correction(combined, batch_key='batch')
    
    print(f"💾 Saving harmonized AnnData to {output_h5ad}")
    combined.write_h5ad(output_h5ad, compression='gzip')
    
    if output_csv:
        print(f"💾 Exporting corrected matrix to {output_csv}")
        # layer 'batch_correction' contains corrected values
        corrected_df = combined.to_df(layer='batch_correction').T
        corrected_df.to_csv(output_csv)
        
    print("✅ Done.")

def main():
    parser = argparse.ArgumentParser(description="Bulk RNA-seq batch correction with ComBat.")
    parser.add_argument("--inputs", nargs='+', required=True, help="Input CSV files (one per batch)")
    parser.add_argument("--output-h5ad", default="adata_batch.h5ad", help="Output H5AD file")
    parser.add_argument("--output-csv", help="Output corrected CSV file")
    
    args = parser.parse_args()
    run_combat(args.inputs, args.output_h5ad, args.output_csv)

if __name__ == "__main__":
    main()
