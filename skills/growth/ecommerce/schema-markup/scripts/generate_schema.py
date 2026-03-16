#!/usr/bin/env python3
import json
import argparse

def generate_organization_schema(name, url, logo):
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": name,
        "url": url,
        "logo": logo
    }

def main():
    parser = argparse.ArgumentParser(description="Generate JSON-LD Schema Markup")
    parser.add_argument("--type", choices=["Organization", "Article", "Product"], required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--url", required=True)
    args = parser.parse_args()

    schema = generate_organization_schema(args.name, args.url, f"{args.url}/logo.png")
    print(json.dumps(schema, indent=2))

if __name__ == "__main__":
    main()
