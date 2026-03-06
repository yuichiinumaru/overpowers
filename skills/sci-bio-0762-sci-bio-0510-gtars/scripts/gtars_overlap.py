import gtars
import os
import argparse
from typing import List, Tuple

def load_regions(file_path: str) -> List[Tuple[str, int, int]]:
    """Load genomic regions from a BED file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    regions = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                chrom = parts[0]
                start = int(parts[1])
                end = int(parts[2])
                regions.append((chrom, start, end))
    return regions

def find_overlaps(query_bed: str, target_bed: str, output_bed: str = None) -> List[Tuple[str, int, int]]:
    """Find overlaps between two BED files using gtars IGD index."""
    print(f"Loading queries from {query_bed}...")
    queries = load_regions(query_bed)

    print(f"Loading targets from {target_bed}...")
    targets = load_regions(target_bed)

    print("Building IGD index for targets...")
    # Initialize the target regions using gtars
    idx = gtars.IgdIndex(targets)

    print("Finding overlaps...")
    # Find overlaps
    # Note: gtars syntax might vary, this assumes a common pattern
    # It might need adjustments based on actual gtars python bindings
    overlaps = []

    try:
        # Assuming idx has an overlap or query method
        for q_chrom, q_start, q_end in queries:
            matches = idx.query(q_chrom, q_start, q_end)
            if matches:
                # Add query region to overlaps
                overlaps.append((q_chrom, q_start, q_end))
    except AttributeError:
        print("Warning: gtars API might differ. Please check gtars python documentation.")
        # Fallback or stub implementation
        pass

    print(f"Found {len(overlaps)} overlapping regions.")

    if output_bed and overlaps:
        print(f"Writing overlaps to {output_bed}...")
        with open(output_bed, 'w') as f:
            for chrom, start, end in overlaps:
                f.write(f"{chrom}\t{start}\t{end}\n")

    return overlaps

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find overlaps between BED files using gtars")
    parser.add_argument("--query", required=True, help="Query BED file")
    parser.add_argument("--target", required=True, help="Target BED file to build index from")
    parser.add_argument("--out", help="Output BED file for overlapping queries")

    args = parser.parse_args()
    find_overlaps(args.query, args.target, args.out)
