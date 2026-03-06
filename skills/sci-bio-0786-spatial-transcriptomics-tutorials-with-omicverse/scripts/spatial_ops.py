import scanpy as sc
import argparse

def run_spatial_tutorial(input_file, output_file):
    print(f"Running spatial transcriptomics tutorial pipeline on {input_file}")
    # adata = sc.read_h5ad(input_file)
    # sc.pp.filter_cells(adata, min_genes=200)
    # sc.pl.spatial(adata)
    # adata.write(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spatial transcriptomics tutorial helper")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    run_spatial_tutorial(args.input, args.output)
