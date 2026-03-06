#!/bin/bash
# Helper script for sec-safety-0920-sec-safety-0054-alphafold-database

echo "Helper for sec-safety-0920-sec-safety-0054-alphafold-database"

# Command examples from SKILL.md:
# # Install gsutil
# uv pip install gsutil
# # List available data
# gsutil ls gs://public-datasets-deepmind-alphafold-v4/
# # Download entire proteomes (by taxonomy ID)
# gsutil -m cp gs://public-datasets-deepmind-alphafold-v4/proteomes/proteome-tax_id-9606-*.tar .
# # Download specific files
# gsutil cp gs://public-datasets-deepmind-alphafold-v4/accession_ids.csv .
# # Install Biopython for structure access
# uv pip install biopython
# # Install requests for API access
# uv pip install requests
# # For visualization and analysis
# uv pip install numpy matplotlib pandas scipy
# # For Google Cloud access (optional)
# uv pip install google-cloud-bigquery gsutil
