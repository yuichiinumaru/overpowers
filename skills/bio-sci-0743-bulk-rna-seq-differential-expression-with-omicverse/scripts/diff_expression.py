import omicverse as ov
import argparse
import pandas as pd

def run_deg(input_file, treatment, control, method, output_prefix):
    print(f"🧬 Starting differential expression analysis (method={method})...")
    ov.plot_set()
    
    print(f"📥 Loading counts: {input_file}")
    data = pd.read_csv(input_file, sep='\t', index_col=0, header=1)
    
    # Clean column names
    data.columns = [c.split('/')[-1].replace('.bam', '') for c in data.columns]
    
    print("🚀 Initializing DEG object...")
    dds = ov.bulk.pyDEG(data)
    dds.drop_duplicates_index()
    
    # Normalize
    dds.normalize()
    
    # Run analysis
    treatment_groups = treatment.split(',')
    control_groups = control.split(',')
    
    print("🧬 Running analysis...")
    dds.deg_analysis(treatment_groups, control_groups, method=method)
    
    print(f"💾 Saving results to {output_prefix}_deg.csv")
    dds.result.to_csv(f"{output_prefix}_deg.csv")
    
    print("📊 Generating volcano plot...")
    dds.plot_volcano(save=f"{output_prefix}_volcano.png")
    
    print("✅ Done.")

def main():
    parser = argparse.ArgumentParser(description="Bulk RNA-seq DEG analysis with omicverse.")
    parser.add_argument("--input", required=True, help="Input count matrix (TSV)")
    parser.add_argument("--treatment", required=True, help="Comma-separated treatment sample IDs")
    parser.add_argument("--control", required=True, help="Comma-separated control sample IDs")
    parser.add_argument("--method", default="ttest", choices=["ttest", "edgepy", "limma", "DEseq2"], help="Analysis method")
    parser.add_argument("--output", default="analysis", help="Output prefix")
    
    args = parser.parse_args()
    run_deg(args.input, args.treatment, args.control, args.method, args.output)

if __name__ == "__main__":
    main()
