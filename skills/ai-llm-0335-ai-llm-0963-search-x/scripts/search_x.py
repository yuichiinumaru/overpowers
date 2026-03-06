#!/usr/bin/env python3
import argparse
import urllib.parse
import webbrowser

def main():
    parser = argparse.ArgumentParser(description="Generate advanced X (Twitter) search queries.")
    parser.add_argument("query", help="Base search term")
    parser.add_argument("--from-user", help="Search tweets from a specific user")
    parser.add_argument("--to-user", help="Search tweets to a specific user")
    parser.add_argument("--since", help="Search tweets since date (YYYY-MM-DD)")
    parser.add_argument("--until", help="Search tweets until date (YYYY-MM-DD)")
    parser.add_argument("--min-faves", type=int, help="Minimum number of favorites/likes")
    parser.add_argument("--min-retweets", type=int, help="Minimum number of retweets")
    parser.add_argument("--open", action="store_true", help="Open the search in default browser")

    args = parser.parse_args()

    search_terms = [args.query]

    if args.from_user:
        search_terms.append(f"from:{args.from_user}")
    if args.to_user:
        search_terms.append(f"to:{args.to_user}")
    if args.since:
        search_terms.append(f"since:{args.since}")
    if args.until:
        search_terms.append(f"until:{args.until}")
    if args.min_faves:
        search_terms.append(f"min_faves:{args.min_faves}")
    if args.min_retweets:
        search_terms.append(f"min_retweets:{args.min_retweets}")

    full_query = " ".join(search_terms)
    encoded_query = urllib.parse.quote(full_query)
    search_url = f"https://x.com/search?q={encoded_query}&src=typed_query"

    print(f"Search Query: {full_query}")
    print(f"URL: {search_url}")

    if args.open:
        webbrowser.open(search_url)

if __name__ == "__main__":
    main()
