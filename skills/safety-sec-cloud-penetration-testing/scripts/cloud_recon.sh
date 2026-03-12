#!/bin/bash
# cloud_recon.sh - Wrapper for cloud penetration testing recon commands

CLOUD_PROVIDER=$1

if [ -z "$CLOUD_PROVIDER" ]; then
    echo "Usage: $0 {aws|gcp|azure}"
    # removed exit
fi

echo "Starting recon for $CLOUD_PROVIDER..."

if [ "$CLOUD_PROVIDER" == "aws" ]; then
    echo "[*] Checking AWS caller identity..."
    aws sts get-caller-identity || echo "AWS CLI not configured or missing credentials"

    echo "[*] Listing S3 buckets..."
    aws s3 ls || echo "Failed to list buckets"

elif [ "$CLOUD_PROVIDER" == "gcp" ]; then
    echo "[*] Checking GCP active account..."
    gcloud auth list || echo "gcloud not configured"

    echo "[*] Listing GCP projects..."
    gcloud projects list || echo "Failed to list projects"

elif [ "$CLOUD_PROVIDER" == "azure" ]; then
    echo "[*] This script assumes Az module is installed."
    echo "[*] You would run: Connect-AzAccount"

else
    echo "Unknown provider: $CLOUD_PROVIDER"
fi

echo "Recon checks complete."
