import scanpy as sc
import argparse

def run_preprocessing(input_file, output_file):
    adata = sc.read_h5ad(input_file)
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata)
    adata.write(output_file)
    print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Single-cell preprocessing helper")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    run_preprocessing(args.input, args.output)
