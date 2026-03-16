import re
import requests
import argparse
import sys

def extract_urls(text):
    return re.findall(r'(https?://[^\s\)]+)', text)

def verify_url(url):
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        return response.status_code < 400
    except:
        try:
            response = requests.get(url, timeout=5, allow_redirects=True, stream=True)
            return response.status_code < 400
        except:
            return False

def main():
    parser = argparse.ArgumentParser(description="URL Verification Protocol Helper")
    parser.add_argument("file", help="Markdown file to verify URLs in")
    
    args = parser.parse_args()
    
    with open(args.file, 'r') as f:
        content = f.read()
        
    urls = extract_urls(content)
    unique_urls = list(set(urls))
    
    print(f"Found {len(unique_urls)} unique URLs. Verifying...")
    
    broken = []
    for url in unique_urls:
        if not verify_url(url):
            broken.append(url)
            print(f"[BROKEN] {url}")
        else:
            print(f"[OK] {url}")
            
    if broken:
        print(f"\nVerification FAILED. {len(broken)} broken URLs found.")
        sys.exit(1)
    else:
        print("\nAll URLs verified successfully.")

if __name__ == "__main__":
    main()
