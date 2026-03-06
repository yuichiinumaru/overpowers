import argparse

def fetch_sra_geo(command, accession, outdir=None, interactive=False):
    print(f"SRA/GEO Fetch utility: {command} on {accession}")
    if command == "info":
        print(f"Fetching metadata for {accession}...")
        print("Placeholder: Found 4 samples, RNA-seq data.")
    elif command == "download":
        print(f"Downloading {accession} to {outdir}...")
        if interactive:
            print("Interactive mode enabled.")
        print("Placeholder: Download complete.")
    elif command == "samplesheet":
        print(f"Generating samplesheet for {accession} using fastq dir {outdir}...")
        print("Placeholder: Created samplesheet.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch datasets from GEO/SRA")
    parser.add_argument("command", choices=["info", "download", "samplesheet"])
    parser.add_argument("accession", help="GEO or SRA accession (e.g., GSE110004)")
    parser.add_argument("-o", "--outdir", default="./fastq", help="Output directory")
    parser.add_argument("-i", "--interactive", action="store_true", help="Interactive download")
    args = parser.parse_args()

    fetch_sra_geo(args.command, args.accession, args.outdir, args.interactive)
