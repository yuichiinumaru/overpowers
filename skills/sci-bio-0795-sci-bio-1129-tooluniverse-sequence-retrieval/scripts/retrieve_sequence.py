#!/usr/bin/env python3
import argparse
import sys
import json

try:
    from tooluniverse import ToolUniverse
except ImportError:
    print("Error: tooluniverse library not found. Please install it to use this script.")
    sys.exit(1)

def retrieve_sequence(accession=None, organism=None, gene=None, seq_type=None, format='fasta', limit=5):
    tu = ToolUniverse()
    tu.load_tools()
    
    if accession:
        print(f"Retrieving sequence for accession: {accession}...")
        try:
            sequence = tu.tools.NCBI_get_sequence(
                operation="fetch_sequence",
                accession=accession,
                format=format
            )
            return sequence
        except Exception as e:
            print(f"Error retrieving accession {accession}: {e}")
            return None
            
    elif organism or gene:
        print(f"Searching for sequences (Organism: {organism}, Gene: {gene})...")
        try:
            search_result = tu.tools.NCBI_search_nucleotide(
                operation="search",
                organism=organism,
                gene=gene,
                seq_type=seq_type,
                limit=limit
            )
            
            if search_result.get('status') == 'success' and search_result['data'].get('uids'):
                uids = search_result['data']['uids']
                print(f"Found {len(uids)} UIDs. Fetching accessions...")
                
                accessions_result = tu.tools.NCBI_fetch_accessions(
                    operation="fetch_accession",
                    uids=uids
                )
                
                if accessions_result.get('status') == 'success':
                    accessions = accessions_result['data'].get('accessions', [])
                    print(f"Accessions found: {', '.join(accessions)}")
                    
                    # Return the first one as a preview
                    first_acc = accessions[0]
                    print(f"Fetching first accession: {first_acc}...")
                    sequence = tu.tools.NCBI_get_sequence(
                        operation="fetch_sequence",
                        accession=first_acc,
                        format=format
                    )
                    return sequence
            else:
                print("No sequences found matching criteria.")
                return None
        except Exception as e:
            print(f"Error during search: {e}")
            return None
    else:
        print("Error: Must provide either accession or organism/gene.")
        return None

def main():
    parser = argparse.ArgumentParser(description='Retrieve biological sequences using ToolUniverse.')
    parser.add_argument('--accession', help='Accession number (e.g., "NC_000913.3")')
    parser.add_argument('--organism', help='Organism scientific name')
    parser.add_argument('--gene', help='Gene symbol')
    parser.add_argument('--type', choices=['complete_genome', 'mrna', 'refseq'], help='Sequence type')
    parser.add_argument('--format', choices=['fasta', 'genbank'], default='fasta', help='Output format (default: fasta)')
    parser.add_argument('--limit', type=int, default=5, help='Search limit (default: 5)')
    parser.add_argument('--output', help='Output file name')

    args = parser.parse_args()

    result = retrieve_sequence(args.accession, args.organism, args.gene, args.type, args.format, args.limit)
    
    if result:
        if args.output:
            with open(args.output, 'w') as f:
                f.write(result)
            print(f"Sequence saved to {args.output}")
        else:
            print(result)

if __name__ == "__main__":
    main()
