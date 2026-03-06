#!/bin/bash
# Setup script for SCAIL 3D Pose Animation
echo "Setting up SCAIL environment..."
if [ ! -d "SCAIL" ]; then
    echo "Please clone the SCAIL repository first."
    echo "Example: git clone https://github.com/scail/scail-repo.git SCAIL"
    return 1 2>/dev/null || return 1
fi

cd SCAIL
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "Warning: requirements.txt not found in SCAIL directory."
fi
echo "Environment setup complete."
