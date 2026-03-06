import json
import argparse
from datetime import datetime

def generate_article_schema(title, url, author, publisher, image_url):
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "url": url,
        "author": {
            "@type": "Person",
            "name": author
        },
        "publisher": {
            "@type": "Organization",
            "name": publisher,
            "logo": {
                "@type": "ImageObject",
                "url": f"{url}/logo.png"
            }
        },
        "image": image_url,
        "datePublished": datetime.now().strftime("%Y-%m-%d"),
        "dateModified": datetime.now().strftime("%Y-%m-%d")
    }
    return schema

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate JSON-LD Article Schema.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--author", required=True)
    parser.add_argument("--publisher", required=True)
    parser.add_argument("--image", required=True)
    args = parser.parse_args()
    
    schema = generate_article_schema(args.title, args.url, args.author, args.publisher, args.image)
    print(json.dumps(schema, indent=2))
