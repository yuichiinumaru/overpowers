import sys

def parse_scholar_json(json_file):
    import json
    with open(json_file, 'r') as f:
        data = json.load(f)
    papers = data.get('papers', [])
    for paper in papers:
        title = paper.get('title')
        cites = paper.get('citations')
        print(f"{title} (Cited by: {cites})")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse_scholar_json(sys.argv[1])
    else:
        print("Usage: python citation_management_helper.py <scholar_json>")
