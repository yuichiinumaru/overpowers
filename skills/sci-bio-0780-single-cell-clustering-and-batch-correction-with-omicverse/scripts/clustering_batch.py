import scanpy as sc
import argparse

def run_clustering_batch(input_file, batch_key, output_file):
    adata = sc.read_h5ad(input_file)
    print(f"Correcting batch: {batch_key}")
    # Example: ov.pp.harmony(adata, key=batch_key)
    sc.tl.leiden(adata)
    adata.write(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clustering and batch correction")
    parser.add_argument("--input", required=True)
    parser.add_argument("--batch_key", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    run_clustering_batch(args.input, args.batch_key, args.output)
