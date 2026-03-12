import scanpy as sc
import argparse

def run_cpdb(input_file, species, output_dir):
    adata = sc.read_h5ad(input_file)
    print(f"Running CellPhoneDB for species: {species}")
    # Example: ov.cpdb.run(...)
    # results = ov.cpdb.plot_cpdb(...)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CellPhoneDB communication mapping")
    parser.add_argument("--input", required=True)
    parser.add_argument("--species", required=True)
    parser.add_argument("--output_dir", required=True)
    args = parser.parse_args()
    run_cpdb(args.input, args.species, args.output_dir)
