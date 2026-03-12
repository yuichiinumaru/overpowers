import pandas as pd
import argparse
import sys
from arboreto.algo import grnboost2, genie3
from arboreto.utils import load_tf_names

def main():
    parser = argparse.ArgumentParser(description="Infer Gene Regulatory Network using Arboreto.")
    parser.add_argument("input", help="Input expression data (CSV/TSV, genes as columns)")
    parser.add_argument("output", help="Output network file (TSV)")
    parser.add_argument("--tf-file", help="File with transcription factor names (one per line)")
    parser.add_argument("--algo", default="grnboost2", choices=["grnboost2", "genie3"], help="Inference algorithm")
    parser.add_argument("--sep", default="\t", help="Input file separator")
    parser.add_argument("--seed", type=int, default=777, help="Random seed")
    
    args = parser.parse_args()
    
    print(f"🧬 Loading expression data from {args.input}...")
    try:
        expression_matrix = pd.read_csv(args.input, sep=args.sep)
    except Exception as e:
        print(f"❌ Error loading input file: {e}")
        sys.exit(1)
        
    tf_names = None
    if args.tf_file:
        print(f"🔍 Loading TFs from {args.tf_file}...")
        tf_names = load_tf_names(args.tf_file)
        
    print(f"🚀 Running {args.algo} inference (seed={args.seed})...")
    
    if args.algo == "grnboost2":
        network = grnboost2(expression_data=expression_matrix, tf_names=tf_names, seed=args.seed)
    else:
        network = genie3(expression_data=expression_matrix, tf_names=tf_names, seed=args.seed)
        
    print(f"✅ Inference complete. Saving results to {args.output}...")
    network.to_csv(args.output, sep="\t", index=False, header=False)
    print("✨ Done.")

if __name__ == '__main__':
    main()
