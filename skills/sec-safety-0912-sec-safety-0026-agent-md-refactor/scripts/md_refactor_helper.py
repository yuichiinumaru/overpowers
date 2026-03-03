import re
import os

class MarkdownRefactorHelper:
    """Helper to analyze and refactor bloated agent instruction files."""
    def __init__(self, file_path):
        self.file_path = file_path
        self.content = ""
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                self.content = f.read()

    def get_sections(self):
        """Split content by headers (Level 1 and 2)."""
        sections = re.split(r'\n(?=#+ )', self.content)
        return sections

    def analyze_redundancy(self):
        """Identify potentially redundant phrases."""
        redundant_patterns = [
            r"write clean code",
            r"don't introduce bugs",
            r"follow best practices",
            r"use descriptive variable names",
            r"don't commit secrets"
        ]
        found = []
        for pattern in redundant_patterns:
            if re.search(pattern, self.content, re.IGNORECASE):
                found.append(pattern)
        return found

    def suggest_structure(self):
        """Suggest categories based on header names."""
        headers = re.findall(r'^#+ (.+)$', self.content, re.MULTILINE)
        categories = []
        for h in headers:
            if any(term in h.lower() for term in ['typescript', 'ts', 'javascript', 'js']):
                categories.append('typescript.md')
            elif 'test' in h.lower():
                categories.append('testing.md')
            elif any(term in h.lower() for term in ['style', 'convention', 'naming']):
                categories.append('code-style.md')
            elif any(term in h.lower() for term in ['git', 'pr', 'commit']):
                categories.append('git-workflow.md')
            elif any(term in h.lower() for term in ['architecture', 'pattern', 'structure']):
                categories.append('architecture.md')
        return sorted(list(set(categories)))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python md_refactor_helper.py <file_path>")
        sys.exit(1)
    
    helper = MarkdownRefactorHelper(sys.argv[1])
    print(f"Analyzing {sys.argv[1]}...")
    
    redundant = helper.analyze_redundancy()
    if redundant:
        print("\nPotentially redundant instructions found:")
        for r in redundant:
            print(f"- {r}")
            
    suggested = helper.suggest_structure()
    if suggested:
        print("\nSuggested linked files:")
        for s in suggested:
            print(f"- .claude/{s}")
