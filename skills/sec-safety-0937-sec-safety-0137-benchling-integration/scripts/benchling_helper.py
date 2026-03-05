#!/usr/bin/env python3
import argparse
import sys

SNIPPETS = {
    "auth": """
from benchling_sdk.benchling import Benchling
from benchling_sdk.auth.api_key_auth import ApiKeyAuth

benchling = Benchling(
    url="https://your-tenant.benchling.com",
    auth_method=ApiKeyAuth("your_api_key")
)
""",
    "create_dna": """
from benchling_sdk.models import DnaSequenceCreate

sequence = benchling.dna_sequences.create(
    DnaSequenceCreate(
        name="My Plasmid",
        bases="ATCGATCG",
        is_circular=True,
        folder_id="fld_abc123"
    )
)
""",
    "inventory": """
from benchling_sdk.models import ContainerCreate

container = benchling.containers.create(
    ContainerCreate(
        name="Sample Tube 001",
        schema_id="cont_schema_abc123",
        parent_storage_id="box_abc123"
    )
)
"""
}

def main():
    parser = argparse.ArgumentParser(description="Benchling Code Snippet Helper")
    parser.add_argument("snippet", choices=SNIPPETS.keys(), help="Snippet to generate")
    
    args = parser.parse_args()
    print(SNIPPETS[args.snippet])

if __name__ == "__main__":
    main()
