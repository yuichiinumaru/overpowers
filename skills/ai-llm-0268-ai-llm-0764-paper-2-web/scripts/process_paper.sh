#!/bin/bash

# Process a paper using Paper2All pipeline.
# Usage: ./process_paper.sh <paper_dir> <output_dir> [flags]

PAPER_DIR="$1"
OUT_DIR="$2"
shift 2

if [ -z "$PAPER_DIR" ] || [ -z "$OUT_DIR" ]; then
  echo "Usage: $0 <paper_dir> <output_dir> [flags]"
  echo "Example: $0 ./papers/my_paper ./output/my_paper --generate-website"
  exit 1
fi

# Ensure absolute paths
PAPER_DIR=$(realpath "$PAPER_DIR")
OUT_DIR=$(realpath "$OUT_DIR")

# Try to find Paper2All installation
if [ -f "pipeline_all.py" ]; then
  P2A_DIR="."
elif [ -d "paper2all" ] && [ -f "paper2all/pipeline_all.py" ]; then
  P2A_DIR="paper2all"
else
  echo "Error: Paper2All installation (pipeline_all.py) not found."
  echo "Please run setup_paper2all.sh first or run this from the Paper2All directory."
  exit 1
fi

echo "Activating conda environment 'paper2all'..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate paper2all

echo "Running Paper2All pipeline..."
cd "$P2A_DIR" || exit 1
python pipeline_all.py \
  --input-dir "$PAPER_DIR" \
  --output-dir "$OUT_DIR" \
  --model-choice 1 \
  "$@"
