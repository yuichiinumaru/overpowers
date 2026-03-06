from skbio import Sequence, DNA, RNA, Protein
import argparse

def analyze_sequence(seq_str, seq_type):
    if seq_type == 'dna':
        seq = DNA(seq_str)
    elif seq_type == 'rna':
        seq = RNA(seq_str)
    elif seq_type == 'protein':
        seq = Protein(seq_str)
    
    print(f"Sequence: {seq}")
    print(f"Length: {len(seq)}")
    if seq_type in ['dna', 'rna']:
        print(f"GC content: {seq.gc_content()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scikit-bio sequence analysis")
    parser.add_argument("--seq", required=True)
    parser.add_argument("--type", choices=['dna', 'rna', 'protein'], required=True)
    args = parser.parse_args()
    analyze_sequence(args.seq, args.type)
