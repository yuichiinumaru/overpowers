#!/bin/bash

# Setup Paper2All environment.
# Usage: ./setup_paper2all.sh [install_dir]

INSTALL_DIR="${1:-./paper2all}"

echo "Cloning Paper2All to ${INSTALL_DIR}..."
git clone https://github.com/YuhangChen1/Paper2All.git "$INSTALL_DIR"
cd "$INSTALL_DIR" || exit 1

echo "Setting up conda environment 'paper2all'..."
conda create -n paper2all python=3.11 -y
source $(conda info --base)/etc/profile.d/conda.sh
conda activate paper2all

echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Done. Please configure your .env file in ${INSTALL_DIR}"
echo "Example .env content:"
echo "OPENAI_API_KEY=your_key_here"
