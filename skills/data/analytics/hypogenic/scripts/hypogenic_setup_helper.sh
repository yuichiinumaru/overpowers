#!/bin/bash
set -euo pipefail

# Clone datasets if not present
echo "[*] Cloning required dataset repositories..."
if [ ! -d "data/HypoGeniC-datasets" ]; then
    git clone https://github.com/ChicagoHAI/HypoGeniC-datasets.git ./data/HypoGeniC-datasets
else
    echo "[*] HypoGeniC-datasets already exists."
fi

if [ ! -d "data/Hypothesis-agent-datasets" ]; then
    git clone https://github.com/ChicagoHAI/Hypothesis-agent-datasets.git ./data/Hypothesis-agent-datasets
else
    echo "[*] Hypothesis-agent-datasets already exists."
fi

# Ensure GROBID service script is present
echo "[*] Checking for GROBID setup scripts..."
if [ -f "./modules/setup_grobid.sh" ]; then
    echo "[*] Running GROBID setup..."
    bash ./modules/setup_grobid.sh
else
    echo "[-] GROBID setup script not found at ./modules/setup_grobid.sh"
    echo "    Make sure you are running this from the root of the Hypogenic framework."
fi

echo "[*] Setup helper complete."
