import requests
import argparse
import sys

def get_llms_txt(base_url):
    url = f"{base_url.rstrip('/')}/llms.txt"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching llms.txt: {e}")
        return None

def search_docs(base_url, query):
    url = f"{base_url.rstrip('/')}/api/search"
    try:
        response = requests.get(url, params={"query": query})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error searching docs: {e}")
        return None

def get_raw_mdx(url):
    if not url.endswith(".mdx"):
        url = f"{url}.mdx"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching raw MDX: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Fumadocs Content Fetcher")
    parser.add_argument("base_url", help="Base URL of the Fumadocs site")
    parser.add_argument("--list", action="store_true", help="Fetch and list pages from llms.txt")
    parser.add_argument("--search", help="Search for a term using the API")
    parser.add_argument("--fetch", help="Fetch raw MDX for a specific page URL")
    
    args = parser.parse_args()
    
    if args.list:
        content = get_llms_txt(args.base_url)
        if content:
            print(content)
            
    if args.search:
        results = search_docs(args.base_url, args.search)
        if results:
            for res in results:
                print(f"- {res.get('title')}: {res.get('url')}")
                
    if args.fetch:
        mdx = get_raw_mdx(args.fetch)
        if mdx:
            print(mdx)

if __name__ == "__main__":
    main()
