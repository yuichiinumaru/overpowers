import argparse
import sys
import json

def main():
    parser = argparse.ArgumentParser(description="ToolUniverse Rare Disease Diagnosis Advisor")
    parser.add_argument("--action", choices=["standardize_phenotype", "match_diseases", "variant_interpretation", "clingen_evidence"], required=True)
    parser.add_argument("--symptoms", nargs="+", help="List of symptoms for standardize_phenotype")
    parser.add_argument("--keywords", nargs="+", help="List of keywords for match_diseases")
    parser.add_argument("--variant", help="Variant HGVS string for variant_interpretation")
    parser.add_argument("--gene", help="Gene symbol for clingen_evidence")

    args = parser.parse_args()

    try:
        from tooluniverse import ToolUniverse
    except ImportError:
        print("Error: tooluniverse not installed.", file=sys.stderr)
        sys.exit(1)

    tu = ToolUniverse()
    tu.load_tools()

    if args.action == "standardize_phenotype":
        if not args.symptoms:
            print("Error: --symptoms required", file=sys.stderr)
            sys.exit(1)
        hpo_terms = []
        for symptom in args.symptoms:
            results = tu.tools.HPO_search_terms(query=symptom)
            if results:
                hpo_terms.append({
                    'original': symptom,
                    'hpo_id': results[0]['id'],
                    'hpo_name': results[0]['name']
                })
        print(json.dumps(hpo_terms, indent=2))

    elif args.action == "match_diseases":
        if not args.keywords:
            print("Error: --keywords required", file=sys.stderr)
            sys.exit(1)
        candidate_diseases = []
        for keyword in args.keywords:
            results = tu.tools.Orphanet_search_diseases(operation="search_diseases", query=keyword)
            if results.get('status') == 'success':
                candidate_diseases.extend(results['data']['results'])
        print(json.dumps(candidate_diseases[:5], indent=2)) # Output top 5 for brevity

    elif args.action == "variant_interpretation":
        if not args.variant:
            print("Error: --variant required", file=sys.stderr)
            sys.exit(1)
        result = tu.tools.ClinVar_search_variants(query=args.variant)
        out = {
            'clinvar_id': result.get('id'),
            'classification': result.get('clinical_significance'),
            'review_status': result.get('review_status'),
            'conditions': result.get('conditions')
        }
        print(json.dumps(out, indent=2))

    elif args.action == "clingen_evidence":
        if not args.gene:
            print("Error: --gene required", file=sys.stderr)
            sys.exit(1)
        validity = tu.tools.ClinGen_search_gene_validity(gene=args.gene)
        print(json.dumps(validity, indent=2))

if __name__ == "__main__":
    main()
