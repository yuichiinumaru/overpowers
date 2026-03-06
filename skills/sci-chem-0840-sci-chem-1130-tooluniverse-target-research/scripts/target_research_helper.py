import sys

def detect_naming_collisions(symbol, full_name, literature_titles):
    """Detect if gene symbol has naming collisions in literature."""
    bio_terms = ['protein', 'gene', 'cell', 'expression', 'mutation', 'kinase', 'receptor']
    off_topic_count = 0
    for title in literature_titles:
        title = title.lower()
        if not any(term in title for term in bio_terms):
            off_topic_count += 1
    total = len(literature_titles)
    if total > 0 and (off_topic_count / total) > 0.2:
        return True, "Potential collision detected (>20% off-topic titles)"
    return False, "No major collisions detected"

if __name__ == "__main__":
    titles = [
        "JAK protein expression in cells",
        "Just Another Kinase function",
        "Just Another Knowledge base (IT)",
        "JAK inhibitor development"
    ]
    collision, msg = detect_naming_collisions("JAK", "Janus kinase", titles)
    print(f"{collision}: {msg}")
