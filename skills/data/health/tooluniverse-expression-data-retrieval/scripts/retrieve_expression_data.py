import argparse
import sys
import json

def main():
    parser = argparse.ArgumentParser(description="ToolUniverse Expression Data Retrieval")
    parser.add_argument("--query", help="Query string for ArrayExpress (e.g., 'breast cancer RNA-seq')")
    parser.add_argument("--species", help="Species (e.g., 'Homo sapiens')")
    parser.add_argument("--accession", help="Specific experiment accession (e.g., E-MTAB-*)")
    parser.add_argument("--limit", type=int, default=10, help="Max results limit")
    parser.add_argument("--multi-omics", action="store_true", help="Search BioStudies for multi-omics data")

    args = parser.parse_args()

    try:
        from tooluniverse import ToolUniverse
    except ImportError:
        print("Error: tooluniverse not installed.", file=sys.stderr)
        sys.exit(1)

    tu = ToolUniverse()
    tu.load_tools()

    results = {}

    if args.accession:
        print(f"Retrieving details for accession: {args.accession}...")
        if args.accession.startswith(("E-MTAB", "E-GEOD")):
            details = tu.tools.arrayexpress_get_experiment_details(accession=args.accession)
            samples = tu.tools.arrayexpress_get_experiment_samples(accession=args.accession)
            files = tu.tools.arrayexpress_get_experiment_files(accession=args.accession)
            results = {"details": details, "samples": samples, "files": files}
        elif args.accession.startswith("S-BSST"):
            details = tu.tools.biostudies_get_study_details(accession=args.accession)
            sections = tu.tools.biostudies_get_study_sections(accession=args.accession)
            files = tu.tools.biostudies_get_study_files(accession=args.accession)
            results = {"details": details, "sections": sections, "files": files}
        else:
            print(f"Unknown accession format: {args.accession}")
            sys.exit(1)

    elif args.query:
        if args.multi_omics:
            print(f"Searching BioStudies for: {args.query}...")
            results = tu.tools.biostudies_search_studies(query=args.query, limit=args.limit)
        else:
            print(f"Searching ArrayExpress for: {args.query} (Species: {args.species})...")
            results = tu.tools.arrayexpress_search_experiments(keywords=args.query, species=args.species, limit=args.limit)
    else:
        parser.print_help()
        sys.exit(1)

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
