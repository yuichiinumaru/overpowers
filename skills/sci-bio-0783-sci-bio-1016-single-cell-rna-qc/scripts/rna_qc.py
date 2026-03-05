import scanpy as sc
import argparse

def run_qc(input_file, output_file):
    adata = sc.read_h5ad(input_file)
    adata.var['mt'] = adata.var_names.str.startswith('MT-')
    sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)
    # Apply standard filters
    sc.pp.filter_cells(adata, min_genes=200)
    sc.pp.filter_genes(adata, min_cells=3)
    adata = adata[adata.obs.pct_counts_mt < 5, :]
    adata.write(output_file)
    print(f"QC completed. Data saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Single-cell RNA QC helper")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    run_qc(args.input, args.output)
