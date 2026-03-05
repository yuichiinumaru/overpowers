import argparse
import urllib.parse

def build_search_url(query, min_price=None, max_price=None, sort=None):
    base_url = "https://www.argos.co.uk/search/"
    encoded_query = urllib.parse.quote(query.replace(' ', '-').lower())
    url = f"{base_url}{encoded_query}/"
    
    if min_price is not None or max_price is not None:
        min_p = min_price if min_price is not None else 0
        max_p = max_price if max_price is not None else 1000000
        url += f"opt/price:{min_p}-{max_p}/"
        
    if sort:
        sort_map = {
            'rating': 'opt/sort:rating/',
            'price-asc': 'opt/sort:price/',
            'price-desc': 'opt/sort:price-desc/'
        }
        url += sort_map.get(sort, "")
        
    return url

def build_product_url(product_id):
    return f"https://www.argos.co.uk/product/{product_id}"

def main():
    parser = argparse.ArgumentParser(description='Build Argos URLs')
    subparsers = parser.add_argument_subparsers(dest='command')
    
    search_parser = subparsers.add_parser('search')
    search_parser.add_argument('query')
    search_parser.add_argument('--min-price', type=int)
    search_parser.add_argument('--max-price', type=int)
    search_parser.add_argument('--sort', choices=['rating', 'price-asc', 'price-desc'])
    
    product_parser = subparsers.add_parser('product')
    product_parser.add_argument('id')
    
    args = parser.parse_args()
    
    if args.command == 'search':
        print(build_search_url(args.query, args.min_price, args.max_price, args.sort))
    elif args.command == 'product':
        print(build_product_url(args.id))

if __name__ == "__main__":
    main()
