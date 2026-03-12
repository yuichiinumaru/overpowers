#!/usr/bin/env python3
import sys

INITIALIZATION_TEMPLATE = """
from biomni.agent import A1
from biomni.config import default_config

# Initialize agent
agent = A1(
    path='./data',  # Path to data lake
    llm='claude-sonnet-4-20250514'  # LLM model selection
)

# Optional: Adjust configuration
default_config.timeout_seconds = 1200
default_config.max_iterations = 50
"""

COMMAND_EXAMPLES = {
    "crispr": "Design a genome-wide CRISPR knockout screen for identifying genes affecting autophagy in HEK293 cells.",
    "scrnaseq": "Analyze this single-cell RNA-seq dataset: perform QC, identify clusters, and annotate cell types. File: data.h5ad",
    "admet": "Predict ADMET properties for these drug candidates: [SMILES strings]",
    "gwas": "Interpret GWAS results for Alzheimer's: map variants to causal genes and perform pathway enrichment."
}

def main():
    if len(sys.argv) < 2:
        print("Usage: biomni_helper.py [init|examples]")
        sys.exit(1)
    
    action = sys.argv[1]
    if action == "init":
        print(INITIALIZATION_TEMPLATE)
    elif action == "examples":
        for key, val in COMMAND_EXAMPLES.items():
            print(f"{key}: {val}")
    else:
        print(f"Unknown action: {action}")

if __name__ == "__main__":
    main()
