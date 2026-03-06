import omicverse as ov
import argparse
import pandas as pd

def run_deseq2(input_file, treatment, control, output_prefix):
    print("🧬 Starting DESeq2 analysis...")
    ov.utils.ov_plot_set()
    
    print(f"📥 Loading counts: {input_file}")
    data = pd.read_csv(input_file, sep='\t', index_col=0, header=1)
    
    # Clean column names
    data.columns = [c.split('/')[-1].replace('.bam', '') for c in data.columns]
    
    print("🚀 Running DESeq2...")
    dds = ov.bulk.pyDEG(data)
    dds.drop_duplicates_index()
    
    # Run analysis
    treatment_groups = treatment.split(',')
    control_groups = control.split(',')
    
    dds.deg_analysis(treatment_groups, control_groups, method='DEseq2')
    
    print(f"💾 Saving results to {output_prefix}_deseq2.csv")
    dds.result.to_csv(f"{output_prefix}_deseq2.csv")
    
    print("📊 Generating volcano plot...")
    dds.plot_volcano(save=f"{output_prefix}_volcano.png")
    
    print("✅ Done.")

def main():
    parser = argparse.ArgumentParser(description="Bulk RNA-seq DESeq2 analysis with omicverse.")
    parser.add_argument("--input", required=True, help="Input count matrix (TSV)")
    parser.add_argument("--treatment", required=True, help="Comma-separated treatment sample IDs")
    parser.add_argument("--control", required=True, help="Comma-separated control sample IDs")
    parser.add_argument("--output", default="analysis", help="Output prefix")
    
    args = parser.parse_args()
    run_deseq2(args.input, args.treatment, args.control, args.output)

if __name__ == "__main__":
    main()
