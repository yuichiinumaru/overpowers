import argparse
import json

def validate_apple(title, subtitle, keywords):
    issues = []
    if len(title) > 30:
        issues.append(f"Apple Title is too long: {len(title)}/30")
    if len(subtitle) > 30:
        issues.append(f"Apple Subtitle is too long: {len(subtitle)}/30")
    if len(keywords) > 100:
        issues.append(f"Apple Keywords field is too long: {len(keywords)}/100")
    return issues

def validate_google(title, short_desc):
    issues = []
    if len(title) > 50:
        issues.append(f"Google Title is too long: {len(title)}/50")
    if len(short_desc) > 80:
        issues.append(f"Google Short Description is too long: {len(short_desc)}/80")
    return issues

def main():
    parser = argparse.ArgumentParser(description='Validate and optimize store metadata')
    parser.add_argument('--platform', choices=['apple', 'google'], required=True)
    parser.add_argument('--title', required=True)
    parser.add_argument('--subtitle', help='Apple Subtitle')
    parser.add_argument('--keywords', help='Apple Keywords (comma separated)')
    parser.add_argument('--short_desc', help='Google Short Description')
    
    args = parser.parse_args()
    
    if args.platform == 'apple':
        issues = validate_apple(args.title, args.subtitle or "", args.keywords or "")
    else:
        issues = validate_google(args.title, args.short_desc or "")
        
    if issues:
        print("Validation Issues Found:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print(f"Metadata for {args.platform} is valid.")

if __name__ == "__main__":
    main()
