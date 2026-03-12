import json
import argparse

def format_search_results(query, results):
    header = f"## Argos Search: {query}\n\n"
    table = "| Product | Price | Rating | Key Features |\n"
    table += "|---------|-------|--------|--------------|\n"
    
    for res in results:
        name = res.get('name', 'N/A')
        url = res.get('url', '#')
        price = res.get('price', 'N/A')
        rating = res.get('rating', 'N/A')
        reviews = res.get('reviews', 0)
        specs = res.get('specs', 'N/A')
        table += f"| [{name}]({url}) | £{price} | {rating}★ ({reviews} reviews) | {specs} |\n"
        
    return header + table

def main():
    parser = argparse.ArgumentParser(description='Format Argos search results')
    parser.add_argument('--query', required=True)
    parser.add_argument('--results', required=True, help='JSON string of results')
    
    args = parser.parse_args()
    
    try:
        results = json.loads(args.results)
        print(format_search_results(args.query, results))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
