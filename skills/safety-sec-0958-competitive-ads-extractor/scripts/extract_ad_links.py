import sys
import re

def extract_links(content):
    # Search for common ad library link patterns (placeholder)
    fb_ads = re.findall(r'https://www\.facebook\.com/ads/library/\?id=\d+', content)
    linkedin_ads = re.findall(r'https://www\.linkedin\.com/ad-library/ads/\?adId=\d+', content)
    
    return {
        "Facebook Ads": list(set(fb_ads)),
        "LinkedIn Ads": list(set(linkedin_ads))
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_ad_links.py <file_with_content>")
        sys.exit(1)
        
    with open(sys.argv[1], 'r') as f:
        content = f.read()
        
    links = extract_links(content)
    for platform, found in links.items():
        if found:
            print(f"--- {platform} ---")
            for link in found:
                print(link)
        else:
            print(f"No {platform} found.")
