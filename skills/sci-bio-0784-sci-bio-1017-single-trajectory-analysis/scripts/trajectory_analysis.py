import scanpy as sc
import argparse

def run_trajectory(input_file, output_file):
    adata = sc.read_h5ad(input_file)
    sc.tl.paga(adata, groups='leiden')
    sc.pl.paga(adata, plot=False)
    sc.tl.draw_graph(adata, init_pos='paga')
    adata.write(output_file)
    print(f"Trajectory analysis completed. Data saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trajectory analysis helper")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    run_trajectory(args.input, args.output)
