#!/bin/bash
# Setup script to clone example datasets for Hypogenic

echo "Setting up Hypogenic datasets..."
mkdir -p data

# Clone HypoGeniC examples (data-driven only)
if [ ! -d "data/HypoGeniC-datasets" ]; then
    echo "Cloning HypoGeniC datasets..."
    git clone https://github.com/ChicagoHAI/HypoGeniC-datasets.git data/HypoGeniC-datasets || echo "Warning: Failed to clone HypoGeniC-datasets."
else
    echo "HypoGeniC-datasets already exists."
fi

# Clone HypoRefine/Union examples (literature + data)
if [ ! -d "data/Hypothesis-agent-datasets" ]; then
    echo "Cloning Hypothesis-agent datasets..."
    git clone https://github.com/ChicagoHAI/Hypothesis-agent-datasets.git data/Hypothesis-agent-datasets || echo "Warning: Failed to clone Hypothesis-agent-datasets (repository might be private or moved)."
else
    echo "Hypothesis-agent-datasets already exists."
fi

echo "Setup complete."
