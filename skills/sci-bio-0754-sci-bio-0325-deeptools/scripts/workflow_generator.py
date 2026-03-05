import sys
import argparse

WORKFLOWS = {
    'chipseq_qc': {
        'desc': 'ChIP-seq quality control (Correlation, PCA, Fingerprint)',
        'template': """#!/bin/bash
# ChIP-seq QC Workflow
set -e

BAMS="{chip_bams} {input_bam}"
THREADS={threads}

echo "Step 1: multiBamSummary..."
multiBamSummary bins --bamfiles $BAMS -p $THREADS -o results_summary.npz

echo "Step 2: plotCorrelation (Heatmap)..."
plotCorrelation -in results_summary.npz --corMethod pearson --skipZeros --plotTitle "Pearson Correlation" \\
    --whatToShow heatmap --colorMap RdYlBu_r --plotNumbers -o heatmap_correlation.png

echo "Step 3: plotPCA..."
plotPCA -in results_summary.npz -o pca.png --plotTitle "PCA Analysis"

echo "Step 4: plotFingerprint..."
plotFingerprint -b $BAMS -p $THREADS --extendReads 200 --ignoreDuplicates \\
    --plotTitle "ChIP-seq Fingerprint" -o fingerprint.png

echo "✅ QC complete. Check heatmap_correlation.png, pca.png, and fingerprint.png"
"""
    },
    'chipseq_analysis': {
        'desc': 'Complete ChIP-seq analysis (Coverage, Comparison)',
        'template': """#!/bin/bash
# ChIP-seq Analysis Workflow
set -e

INPUT_BAM="{input_bam}"
CHIP_BAM="{chip_bams}"
GENOME_SIZE={genome_size}
THREADS={threads}

echo "Step 1: bamCoverage (RPGC normalization)..."
bamCoverage --bam $CHIP_BAM -o chip.bw --normalizeUsing RPGC --effectiveGenomeSize $GENOME_SIZE \\
    --extendReads 200 --ignoreDuplicates -p $THREADS

echo "Step 2: bamCompare (log2 ratio over input)..."
bamCompare -b1 $CHIP_BAM -b2 $INPUT_BAM -o ratio.bw --operation log2 \\
    --scaleFactorsMethod readCount -p $THREADS

echo "✅ Analysis complete. chip.bw and ratio.bw generated."
"""
    }
}

def main():
    parser = argparse.ArgumentParser(description="Generate deepTools workflow scripts")
    parser.add_argument("workflow", choices=list(WORKFLOWS.keys()) + ['--list'], help="Workflow type or --list")
    parser.add_argument("-o", "--output", help="Output script path")
    parser.add_argument("--input-bam", default="input.bam", help="Control/Input BAM file")
    parser.add_argument("--chip-bams", default="sample.bam", help="ChIP/Sample BAM file(s)")
    parser.add_argument("--genome-size", default="2913022398", help="Effective genome size (default: hg38)")
    parser.add_argument("--threads", default="8", help="Number of processors")

    if '--list' in sys.argv:
        print("\nAvailable Workflows:")
        for k, v in WORKFLOWS.items():
            print(f"  - {k}: {v['desc']}")
        return

    args = parser.parse_args()
    
    if args.workflow in WORKFLOWS:
        tpl = WORKFLOWS[args.workflow]['template']
        content = tpl.format(
            input_bam=args.input_bam,
            chip_bams=args.chip_bams,
            genome_size=args.genome_size,
            threads=args.threads
        )
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(content)
            print(f"✅ Workflow script saved to: {args.output}")
        else:
            print(content)

if __name__ == "__main__":
    main()
