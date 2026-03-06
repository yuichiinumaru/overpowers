import argparse
import os
import glob
import csv

def generate_samplesheet(data_dir, pipeline, output_file):
    print(f"Generating samplesheet for {pipeline} using data in {data_dir}...")

    # Very simplified logic for finding paired fastq files
    r1_files = sorted(glob.glob(os.path.join(data_dir, "*_R1*.fastq.gz")))
    r2_files = sorted(glob.glob(os.path.join(data_dir, "*_R2*.fastq.gz")))

    if not r1_files:
        print(f"Warning: No *_R1*.fastq.gz files found in {data_dir}")
        return

    if pipeline == "rnaseq":
        header = ["sample", "fastq_1", "fastq_2", "strandedness"]
        rows = []
        for r1 in r1_files:
            sample_name = os.path.basename(r1).split('_R1')[0]
            r2_match = r1.replace('_R1', '_R2')
            r2 = r2_match if os.path.exists(r2_match) else ""
            rows.append([sample_name, os.path.abspath(r1), os.path.abspath(r2), "auto"])

    elif pipeline == "atacseq":
        header = ["sample", "fastq_1", "fastq_2", "replicate"]
        rows = []
        for r1 in r1_files:
            sample_name = os.path.basename(r1).split('_R1')[0]
            r2_match = r1.replace('_R1', '_R2')
            r2 = r2_match if os.path.exists(r2_match) else ""
            rows.append([sample_name, os.path.abspath(r1), os.path.abspath(r2), "1"])

    elif pipeline == "sarek":
        header = ["patient", "sample", "lane", "fastq_1", "fastq_2", "status"]
        rows = []
        for i, r1 in enumerate(r1_files):
            sample_name = os.path.basename(r1).split('_R1')[0]
            r2_match = r1.replace('_R1', '_R2')
            r2 = r2_match if os.path.exists(r2_match) else ""
            # Default to normal (status 0) for demonstration
            rows.append([f"patient{i+1}", sample_name, "L001", os.path.abspath(r1), os.path.abspath(r2), "0"])
    else:
        print(f"Unsupported pipeline: {pipeline}")
        return

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

    print(f"Created samplesheet: {output_file}")
    print(f"Contains {len(rows)} samples.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate samplesheet for nf-core pipelines")
    parser.add_argument("directory", help="Directory with FASTQ files")
    parser.add_argument("pipeline", choices=["rnaseq", "atacseq", "sarek"], help="Target pipeline")
    parser.add_argument("-o", "--output", default="samplesheet.csv", help="Output file")
    args = parser.parse_args()

    generate_samplesheet(args.directory, args.pipeline, args.output)
