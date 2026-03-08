import pysam
import argparse

def index_file(filepath, file_type):
    if file_type == 'bam':
        pysam.index(filepath)
    elif file_type == 'vcf':
        pysam.tabix_index(filepath, preset='vcf')
    elif file_type == 'fasta':
        pysam.faidx(filepath)

def fetch_region(filepath, region, file_type):
    if file_type == 'bam':
        with pysam.AlignmentFile(filepath, "rb") as samfile:
            for read in samfile.fetch(region=region):
                print(read)
    elif file_type == 'vcf':
        with pysam.VariantFile(filepath) as vcf:
            for variant in vcf.fetch(region=region):
                print(variant)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pysam genomic operations helper")
    parser.add_argument("--action", choices=['index', 'fetch'], required=True)
    parser.add_argument("--file", required=True)
    parser.add_argument("--type", choices=['bam', 'vcf', 'fasta'], required=True)
    parser.add_argument("--region", help="Region in format chr:start-end")
    args = parser.parse_args()
    
    if args.action == 'index':
        index_file(args.file, args.type)
    elif args.action == 'fetch':
        fetch_region(args.file, args.region, args.type)
