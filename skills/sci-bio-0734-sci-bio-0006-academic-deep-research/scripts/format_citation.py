import sys

def format_apa(author, year, title, journal=None, volume=None, issue=None, pages=None, doi=None):
    """Simple APA 7th edition formatter."""
    citation = f"{author} ({year}). {title}."
    if journal:
        citation += f" *{journal}*"
        if volume:
            citation += f", {volume}"
            if issue:
                citation += f"({issue})"
        if pages:
            citation += f", {pages}"
    if doi:
        if not doi.startswith("http"):
            doi = f"https://doi.org/{doi}"
        citation += f" {doi}"
    return citation

def main():
    if len(sys.argv) < 4:
        print("Usage: format_citation.py <author> <year> <title> [journal] [volume] [issue] [pages] [doi]")
        sys.exit(1)
    
    args = sys.argv[1:]
    # Fill missing optional args with None
    while len(args) < 8:
        args.append(None)
        
    print(format_apa(*args))

if __name__ == "__main__":
    main()
