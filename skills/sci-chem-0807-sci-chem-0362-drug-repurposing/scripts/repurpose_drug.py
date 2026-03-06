import argparse
import sys
import json

def main():
    parser = argparse.ArgumentParser(description="ToolUniverse Drug Repurposing")
    parser.add_argument("--action", choices=["disease_targets", "target_drugs", "drug_info"], required=True)
    parser.add_argument("--disease", help="Disease name for disease_targets")
    parser.add_argument("--target", help="Target gene symbol for target_drugs")
    parser.add_argument("--drug", help="Drug name for drug_info")

    args = parser.parse_args()

    try:
        from tooluniverse import ToolUniverse
    except ImportError:
        print("Error: tooluniverse not installed.", file=sys.stderr)
        sys.exit(1)

    tu = ToolUniverse()
    tu.load_tools()

    if args.action == "disease_targets":
        if not args.disease:
            print("Error: --disease required", file=sys.stderr)
            sys.exit(1)
        print(f"Finding targets for {args.disease}...")
        info = tu.tools.OpenTargets_get_disease_id_description_by_name(diseaseName=args.disease)
        if info and 'data' in info and 'id' in info['data']:
            targets = tu.tools.OpenTargets_get_associated_targets_by_disease_efoId(efoId=info['data']['id'], limit=10)
            print(json.dumps(targets, indent=2))
        else:
            print(f"Could not find disease: {args.disease}")

    elif args.action == "target_drugs":
        if not args.target:
            print("Error: --target required", file=sys.stderr)
            sys.exit(1)
        print(f"Finding drugs for target {args.target}...")
        drugs = tu.tools.DGIdb_get_drug_gene_interactions(gene_name=args.target)
        print(json.dumps(drugs, indent=2))

    elif args.action == "drug_info":
        if not args.drug:
            print("Error: --drug required", file=sys.stderr)
            sys.exit(1)
        print(f"Getting info for {args.drug}...")
        info = tu.tools.drugbank_get_drug_basic_info_by_drug_name_or_id(drug_name_or_drugbank_id=args.drug)
        print(json.dumps(info, indent=2))

if __name__ == "__main__":
    main()
