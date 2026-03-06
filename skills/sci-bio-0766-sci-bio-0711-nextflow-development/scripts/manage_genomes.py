import argparse

def check_genome(genome):
    print(f"Checking availability of genome: {genome}...")
    print("This requires an actual implementation connected to an iGenomes index or similar.")
    print("Assuming not locally cached for demonstration.")
    return False

def download_genome(genome):
    print(f"Simulating download of genome index for {genome}...")
    print("Normally this would fetch reference fasta, gtf, and built indices (STAR/Salmon/BWA).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage reference genomes")
    parser.add_argument("command", choices=["check", "download"])
    parser.add_argument("genome", help="Genome key (e.g., GRCh38, GRCm39)")

    args = parser.parse_args()

    if args.command == "check":
        check_genome(args.genome)
    elif args.command == "download":
        download_genome(args.genome)
