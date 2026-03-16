import argparse
import sys
import re

def analyze_post(text, platform):
    print(f"--- Analyzing post for {platform.upper()} ---\n")
    
    lines = text.strip().split('\n')
    line_count = len(lines)
    char_count = len(text)
    
    # Check hashtags
    hashtags = re.findall(r'#\w+', text)
    
    # Check marketing words
    marketing_words = ["game-changing", "seamless", "powerful", "revolutionize", "excellent", "really"]
    found_marketing = [word for word in marketing_words if word in text.lower()]
    
    if platform == "linkedin":
        if line_count > 5:
            print("❌ Warning: LinkedIn posts should be 3-5 lines max. Current:", line_count)
        else:
            print("✅ Line count is good.")
            
    elif platform == "twitter":
        if char_count > 280:
            print(f"❌ Warning: Twitter posts should be under 280 characters. Current: {char_count}")
        else:
            print("✅ Character count is good.")
            
    if hashtags:
        print(f"❌ Warning: Avoid hashtags unless platform culture expects them. Found: {', '.join(hashtags)}")
    else:
        print("✅ No hashtags found.")
        
    if found_marketing:
        print(f"❌ Warning: Avoid marketing fluff words. Found: {', '.join(found_marketing)}")
    else:
        print("✅ No marketing fluff words found.")
        
    if "!" * 2 in text:
         print("❌ Warning: Avoid excessive exclamation marks.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate social media post text")
    parser.add_argument("file", help="File containing the post text")
    parser.add_argument("--platform", choices=["linkedin", "twitter", "reddit"], required=True, help="Target platform")
    
    args = parser.parse_args()
    
    try:
        with open(args.file, 'r') as f:
            text = f.read()
        analyze_post(text, args.platform)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
