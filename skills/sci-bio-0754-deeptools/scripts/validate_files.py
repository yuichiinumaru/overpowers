import os
import sys
import argparse

def validate_bam(bam_files):
    results = []
    for f in bam_files:
        exists = os.path.exists(f)
        index_exists = os.path.exists(f + ".bai") or os.path.exists(f[:-4] + ".bai") if f.endswith(".bam") else False
        results.append((f, exists, index_exists))
    return results

def validate_bed(bed_files):
    results = []
    for f in bed_files:
        exists = os.path.exists(f)
        # Simple format check (at least 3 columns)
        valid_format = False
        if exists:
            try:
                with open(f, 'r') as fh:
                    for line in fh:
                        if line.startswith('#') or not line.strip(): continue
                        cols = line.split('\t')
                        if len(cols) >= 3:
                            valid_format = True
                        break
            except: pass
        results.append((f, exists, valid_format))
    return results

def main():
    parser = argparse.ArgumentParser(description="Validate files for deepTools analysis")
    parser.add_argument("--bam", nargs="+", help="BAM files to validate")
    parser.add_argument("--bed", nargs="+", help="BED files to validate")
    parser.add_argument("--bigwig", nargs="+", help="bigWig files to validate")
    
    args = parser.parse_args()
    
    if args.bam:
        print("\n--- BAM Validation ---")
        for f, exists, idx in validate_bam(args.bam):
            status = "✅" if exists and idx else "❌"
            idx_status = "Index found" if idx else "Index MISSING"
            print(f"{status} {f}: {'Exists' if exists else 'MISSING'}, {idx_status}")

    if args.bed:
        print("\n--- BED Validation ---")
        for f, exists, fmt in validate_bed(args.bed):
            status = "✅" if exists and fmt else "❌"
            fmt_status = "Format OK" if fmt else "Format INVALID (min 3 columns)"
            print(f"{status} {f}: {'Exists' if exists else 'MISSING'}, {fmt_status}")

    if args.bigwig:
        print("\n--- bigWig Validation ---")
        for f in args.bigwig:
            exists = os.path.exists(f)
            status = "✅" if exists else "❌"
            print(f"{status} {f}: {'Exists' if exists else 'MISSING'}")

if __name__ == "__main__":
    main()
