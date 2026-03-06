import json
import sys
import argparse

def generate_query():
    parser = argparse.ArgumentParser(description="Generate a valid JSON for web_search_advanced_exa people research.")
    parser.add_argument("query", help="The main search query.")
    parser.add_argument("--category", choices=["people", "personal site", "news", "auto"], default="people", 
                        help="Exa search category.")
    parser.add_argument("--num-results", type=int, default=20, help="Number of results to return.")
    parser.add_argument("--type", choices=["auto", "deep", "neural"], default="auto", help="Search type.")
    parser.add_argument("--livecrawl", choices=["always", "fallback", "never"], default="fallback", help="Live crawl mode.")
    parser.add_argument("--variants", nargs="+", help="Query variants.")

    args = parser.parse_args()

    query_obj = {
        "query": args.query,
        "numResults": args.num_results,
        "type": args.type,
        "livecrawl": args.livecrawl
    }

    if args.category != "auto":
        query_obj["category"] = args.category

    if args.variants:
        query_obj["additionalQueries"] = args.variants

    # Apply restrictions for 'people' category
    if args.category == "people":
        print("Note: Applying 'people' category restrictions (LinkedIn domains only, no date filters).")
        query_obj["includeDomains"] = ["linkedin.com"]
        # Remove any date filters if they were to be added (not implemented in this script yet)

    print("\nGenerated web_search_advanced_exa call:\n")
    print(json.dumps(query_obj, indent=2))

if __name__ == "__main__":
    generate_query()
