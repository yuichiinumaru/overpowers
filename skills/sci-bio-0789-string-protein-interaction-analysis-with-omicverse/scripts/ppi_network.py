import scanpy as sc
import argparse

def plot_ppi(genes, species, output_file):
    print(f"Plotting PPI for genes: {genes} (Species: {species})")
    # Example logic using omicverse
    # ppi = ov.bulk.pyPPI(gene=genes, species=species)
    # ppi.interaction_analysis()
    # ppi.plot_network()
    # plt.savefig(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PPI network plotting helper")
    parser.add_argument("--genes", required=True, help="Comma-separated genes")
    parser.add_argument("--species", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    plot_ppi(args.genes.split(','), args.species, args.output)
