#!/bin/bash

# Setup environment for SCAIL 3D Pose Animation

REPO_URL="https://github.com/SCAIL-project/SCAIL" # Placeholder, update if different

echo "Cloning SCAIL repository..."
git clone $REPO_URL
cd SCAIL

echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. To activate: source SCAIL/venv/bin/activate"
