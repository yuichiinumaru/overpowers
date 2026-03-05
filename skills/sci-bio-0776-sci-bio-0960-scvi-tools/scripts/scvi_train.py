import scvi
import scanpy as sc
import argparse

def train_model(input_file, model_path):
    adata = sc.read_h5ad(input_file)
    scvi.model.SCVI.setup_anndata(adata)
    model = scvi.model.SCVI(adata)
    model.train()
    model.save(model_path, overwrite=True)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SCVI training helper")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    train_model(args.input, args.output)
