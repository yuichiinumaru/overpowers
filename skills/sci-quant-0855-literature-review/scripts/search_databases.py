import json
import argparse
import os

def deduplicate_results(results):
    seen_dois = set()
    unique_results = []
    for item in results:
        doi = item.get('doi')
        if doi:
            if doi not in seen_dois:
                seen_dois.add(doi)
                unique_results.append(item)
        else:
            # Fallback to title if no DOI
            title = item.get('title', '').lower().strip()
            if title and title not in seen_dois:
                seen_dois.add(title)
                unique_results.append(item)
    return unique_results

def main():
    parser = argparse.ArgumentParser(description='Process, deduplicate, and format search results.')
    parser.add_argument('input', help='Input JSON file with search results')
    parser.add_argument('--deduplicate', action='store_true', help='Deduplicate results by DOI or title')
    parser.add_argument('--format', choices=['markdown', 'json'], default='markdown', help='Output format')
    parser.add_argument('--output', help='Output file path')
    parser.add_argument('--rank', choices=['citations', 'date'], help='Rank results')
    parser.add_argument('--year-start', type=int, help='Filter by start year')
    parser.add_argument('--year-end', type=int, help='Filter by end year')
    parser.add_argument('--summary', action='store_true', help='Generate summary')

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} not found.")
        return

    with open(args.input, 'r') as f:
        try:
            results = json.load(f)
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON from {args.input}")
            return

    if args.deduplicate:
        results = deduplicate_results(results)

    # Simple year filtering
    if args.year_start or args.year_end:
        filtered = []
        for item in results:
            year_str = item.get('year')
            if year_str:
                try:
                    year = int(year_str)
                    if args.year_start and year < args.year_start:
                        continue
                    if args.year_end and year > args.year_end:
                        continue
                except ValueError:
                    pass
            filtered.append(item)
        results = filtered

    # Simple ranking
    if args.rank == 'citations':
        results.sort(key=lambda x: int(x.get('citations', 0)), reverse=True)
    elif args.rank == 'date':
        results.sort(key=lambda x: str(x.get('year', '')), reverse=True)

    output_content = ""
    if args.format == 'json':
        output_content = json.dumps(results, indent=2)
    else:
        # Generate Markdown
        if args.summary:
            output_content += f"# Literature Search Summary\n\nTotal unique results: {len(results)}\n\n"
        
        for i, item in enumerate(results):
            output_content += f"### {i+1}. {item.get('title', 'No Title')}\n"
            output_content += f"- **Authors**: {item.get('authors', 'N/A')}\n"
            output_content += f"- **Year**: {item.get('year', 'N/A')}\n"
            output_content += f"- **Journal**: {item.get('journal', 'N/A')}\n"
            output_content += f"- **DOI**: {item.get('doi', 'N/A')}\n"
            output_content += f"- **Citations**: {item.get('citations', '0')}\n"
            if item.get('abstract'):
                output_content += f"\n**Abstract**: {item.get('abstract')}\n"
            output_content += "\n---\n\n"

    if args.output:
        with open(args.output, 'w') as f:
            f.write(output_content)
        print(f"Results saved to {args.output}")
    else:
        print(output_content)

if __name__ == "__main__":
    main()
