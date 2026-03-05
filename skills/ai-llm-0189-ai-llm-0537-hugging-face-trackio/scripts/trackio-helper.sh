#!/bin/bash
# trackio-helper.sh - Trackio CLI helper

echo "Trackio CLI Helper"
echo "------------------"

echo "1. List projects (JSON):"
echo "trackio list projects --json"

echo ""
echo "2. Get latest loss for a project:"
echo "trackio get metric --project \$PROJECT --run \$RUN --metric loss --json"

echo ""
echo "3. Sync to Hugging Face Space:"
echo "trackio sync --space_id \$SPACE_ID"

echo ""
echo "Note: Ensure 'trackio' package is installed and HF_TOKEN is set."
