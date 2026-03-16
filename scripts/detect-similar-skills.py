#!/usr/bin/env python3
"""
Semantic Similarity Detector for Skills
Detects similar skills across different languages using sentence embeddings.
"""

import os
import json
import re
from pathlib import Path
from collections import defaultdict
import hashlib

# Try to import sentence-transformers, fall back to simpler method if not available
try:
    from sentence_transformers import SentenceTransformer
    USE_TRANSFORMERS = True
    MODEL_NAME = 'Qwen/Qwen3-Embedding-0.6B'
except ImportError:
    USE_TRANSFORMERS = False
    MODEL_NAME = None
    print("⚠️  sentence-transformers not installed.")
    print("📦 Install with: pip install sentence-transformers transformers torch")
    print(f"🤖 Will use keyword-only method. For better results, install and use model: {MODEL_NAME}")

# Base directory (resolved dynamically from script location)
BASE_DIR = Path(__file__).resolve().parent.parent
SKILLS_DIR = BASE_DIR / "skills"
OUTPUT_DIR = BASE_DIR / ".docs" / "tasks" / "planning"


def extract_text_from_markdown(file_path):
    """Extract meaningful text from markdown file (skip code blocks, focus on descriptions)"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        return ""
    
    # Extract frontmatter description
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    description = ""
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        desc_match = re.search(r'description:\s*(.+?)(?:\n|$)', frontmatter, re.IGNORECASE)
        if desc_match:
            description = desc_match.group(1).strip()
    
    # Extract first paragraph after frontmatter (usually the main description)
    content_after_frontmatter = content[frontmatter_match.end():] if frontmatter_match else content
    paragraphs = re.split(r'\n\s*\n', content_after_frontmatter)
    
    # Get first meaningful paragraph (skip headers)
    first_paragraph = ""
    for para in paragraphs[:3]:
        para = para.strip()
        if para and not para.startswith('#') and len(para) > 50:
            first_paragraph = para
            break
    
    # Combine description and first paragraph
    text = f"{description} {first_paragraph}".strip()
    
    # Remove code blocks, links, and markdown formatting
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # Remove links, keep text
    text = re.sub(r'[#*_`]', '', text)  # Remove markdown symbols
    
    return text


def compute_file_hash(text):
    """Compute a simple hash of text for quick comparison"""
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def normalize_text(text):
    """Normalize text for comparison (lowercase, remove extra spaces)"""
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text


def extract_keywords(text):
    """Extract potential keywords/names from text"""
    # Look for capitalized words, technical terms, etc.
    keywords = set()
    
    # Extract words that look like technical terms or names
    words = re.findall(r'\b[A-Za-z][A-Za-z0-9_-]{3,}\b', text)
    keywords.update(w.lower() for w in words)
    
    # Remove common English words
    stop_words = {
        'the', 'and', 'for', 'with', 'this', 'that', 'from', 'have', 'been',
        'are', 'was', 'were', 'has', 'had', 'will', 'would', 'could', 'should',
        'can', 'may', 'might', 'must', 'shall', 'need', 'dare', 'ought',
        'used', 'going', 'come', 'make', 'take', 'get', 'give', 'find',
        'skill', 'agent', 'support', 'when', 'user', 'use', 'used', 'using',
        'includes', 'including', 'feature', 'features', 'function', 'functions'
    }
    keywords -= stop_words
    
    return keywords


def jaccard_similarity(set1, set2):
    """Calculate Jaccard similarity between two sets"""
    if not set1 or not set2:
        return 0.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0.0


def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors"""
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = sum(a * a for a in vec1) ** 0.5
    norm2 = sum(b * b for b in vec2) ** 0.5
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot_product / (norm1 * norm2)


class SemanticSimilarityDetector:
    def __init__(self):
        self.model = None
        self.skill_data = []
        
        if USE_TRANSFORMERS:
            print(f"🧠 Loading sentence transformer model: {MODEL_NAME}...")
            print("💡 This may take a few minutes on first run (downloads ~500MB)")
            try:
                # Use Qwen3-Embedding-0.6B - lightweight multilingual model
                # 0.6B params fits easily on RTX 3070 8GB VRAM
                import torch
                device = 'cuda' if torch.cuda.is_available() else 'cpu'
                self.model = SentenceTransformer(
                    MODEL_NAME,
                    trust_remote_code=True,
                    device=device
                )
                print(f"✅ Model loaded successfully on {self.model.device}")
            except Exception as e:
                print(f"⚠️  Failed to load model: {e}")
                print("📝 Falling back to keyword-only method")
                self.model = None
    
    def scan_skills(self):
        """Scan all skills and extract text"""
        print("📂 Scanning skills directory...")
        
        skills = []
        for root, dirs, files in os.walk(SKILLS_DIR):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for file in files:
                if file.endswith('.md'):
                    file_path = Path(root) / file
                    
                    # Extract skill name from directory
                    skill_dir = Path(root).relative_to(SKILLS_DIR)
                    
                    text = extract_text_from_markdown(file_path)
                    if text and len(text) > 20:
                        skills.append({
                            'path': str(file_path.relative_to(BASE_DIR)),
                            'skill_name': str(skill_dir),
                            'file': file,
                            'text': text,
                            'normalized': normalize_text(text),
                            'keywords': extract_keywords(text),
                            'hash': compute_file_hash(normalize_text(text))
                        })
        
        print(f"✅ Found {len(skills)} skills with meaningful content")
        self.skill_data = skills
        return skills
    
    def compute_embeddings(self):
        """Compute sentence embeddings for all skills"""
        if not self.model:
            print("⚠️  No model available, skipping embeddings")
            return
        
        print("🧮 Computing embeddings...")
        # Truncate texts to 512 chars — embedding models have token limits anyway,
        # and the first ~512 chars capture skill purpose well enough for similarity
        texts = [skill['text'][:512] for skill in self.skill_data]
        
        # Encode one at a time — text lengths vary wildly (10 chars to 10K+),
        # making batched attention matrices unpredictable for VRAM
        import torch
        total = len(texts)
        for i, text in enumerate(texts):
            if (i + 1) % 100 == 0 or i == 0:
                print(f"   Encoding {i + 1}/{total}...")
            embedding = self.model.encode([text], show_progress_bar=False)
            self.skill_data[i]['embedding'] = embedding[0].tolist()
            # Clear CUDA cache every 200 items to prevent fragmentation
            if (i + 1) % 200 == 0 and torch.cuda.is_available():
                torch.cuda.empty_cache()
        
        print("✅ Embeddings computed")
    
    def find_similar_skills(self, threshold=0.6, min_keyword_similarity=0.3):
        """Find similar skills using both embeddings and keyword overlap"""
        print("🔍 Finding similar skills...")
        
        similar_pairs = []
        
        # Group by hash first (exact duplicates)
        hash_groups = defaultdict(list)
        for skill in self.skill_data:
            hash_groups[skill['hash']].append(skill)
        
        # Add exact duplicates
        for hash_val, group in hash_groups.items():
            if len(group) > 1:
                for i in range(len(group)):
                    for j in range(i + 1, len(group)):
                        similar_pairs.append({
                            'skill1': group[i],
                            'skill2': group[j],
                            'similarity': 1.0,
                            'method': 'exact_hash'
                        })
        
        # If we have embeddings, use cosine similarity
        if self.model and all('embedding' in s for s in self.skill_data):
            print("   Using cosine similarity on embeddings...")
            for i, skill1 in enumerate(self.skill_data):
                for j, skill2 in enumerate(self.skill_data[i + 1:], i + 1):
                    # Skip if already found as exact duplicate
                    if skill1['hash'] == skill2['hash']:
                        continue
                    
                    # Calculate cosine similarity
                    cos_sim = cosine_similarity(skill1['embedding'], skill2['embedding'])
                    
                    # Calculate keyword similarity
                    kw_sim = jaccard_similarity(skill1['keywords'], skill2['keywords'])
                    
                    # Combined score (weighted average)
                    combined_score = 0.7 * cos_sim + 0.3 * kw_sim
                    
                    if combined_score >= threshold or kw_sim >= min_keyword_similarity:
                        similar_pairs.append({
                            'skill1': skill1,
                            'skill2': skill2,
                            'similarity': combined_score,
                            'cosine_similarity': cos_sim,
                            'keyword_similarity': kw_sim,
                            'method': 'embedding+keywords'
                        })
        else:
            # Fallback to keyword-only similarity
            print("   Using keyword-only similarity...")
            for i, skill1 in enumerate(self.skill_data):
                for j, skill2 in enumerate(self.skill_data[i + 1:], i + 1):
                    if skill1['hash'] == skill2['hash']:
                        continue
                    
                    kw_sim = jaccard_similarity(skill1['keywords'], skill2['keywords'])
                    if kw_sim >= min_keyword_similarity:
                        similar_pairs.append({
                            'skill1': skill1,
                            'skill2': skill2,
                            'similarity': kw_sim,
                            'keyword_similarity': kw_sim,
                            'method': 'keywords_only'
                        })
        
        # Sort by similarity
        similar_pairs.sort(key=lambda x: x['similarity'], reverse=True)
        
        print(f"✅ Found {len(similar_pairs)} similar pairs")
        return similar_pairs
    
    def generate_report(self, similar_pairs):
        """Generate a detailed markdown report"""
        report = []
        report.append("# Semantic Similarity Detection Report\n")
        report.append(f"**Generated**: {Path.home()}/Work/overpowers/scripts/detect-similar-skills.py\n")
        report.append(f"**Total Skills Analyzed**: {len(self.skill_data)}\n")
        report.append(f"**Similar Pairs Found**: {len(similar_pairs)}\n")
        
        if USE_TRANSFORMERS and self.model:
            report.append(f"**Model**: {MODEL_NAME}\n")
        else:
            report.append("**Model**: Keyword-only (sentence-transformers not installed)\n")
        
        # Summary statistics
        report.append("\n## 📊 Summary Statistics\n")
        
        # Group by similarity ranges
        high_sim = [p for p in similar_pairs if p['similarity'] >= 0.8]
        med_sim = [p for p in similar_pairs if 0.6 <= p['similarity'] < 0.8]
        low_sim = [p for p in similar_pairs if 0.3 <= p['similarity'] < 0.6]
        
        report.append(f"| Similarity Range | Count | Action Recommended |")
        report.append(f"|-----------------|-------|-------------------|")
        report.append(f"| High (≥80%) | {len(high_sim)} | ⚠️ Review for duplicates |")
        report.append(f"| Medium (60-80%) | {len(med_sim)} | ℹ️ Check for translations |")
        report.append(f"| Low (30-60%) | {len(low_sim)} | 📝 May be related |")
        
        # Detailed listings
        if high_sim:
            report.append("\n## 🚨 High Similarity Pairs (≥80%)\n")
            report.append("These skills are very similar - check if they're duplicates or translations:\n")
            
            for i, pair in enumerate(high_sim[:50], 1):
                report.append(f"### {i}. Similarity: {pair['similarity']:.1%}\n")
                report.append(f"**Skill 1**: `{pair['skill1']['path']}`\n")
                report.append(f"  - Keywords: {', '.join(list(pair['skill1']['keywords'])[:10])}\n")
                report.append(f"  - Preview: {pair['skill1']['text'][:200]}...\n")
                report.append(f"\n**Skill 2**: `{pair['skill2']['path']}`\n")
                report.append(f"  - Keywords: {', '.join(list(pair['skill2']['keywords'])[:10])}\n")
                report.append(f"  - Preview: {pair['skill2']['text'][:200]}...\n")
                
                if 'cosine_similarity' in pair:
                    report.append(f"\n**Scores**: Cosine={pair.get('cosine_similarity', 0):.1%}, Keywords={pair.get('keyword_similarity', 0):.1%}\n")
                report.append("\n---\n")
        
        if med_sim:
            report.append(f"\n## ⚠️ Medium Similarity Pairs (60-80%)\n")
            report.append(f"**Count**: {len(med_sim)} pairs\n")
            report.append("These may be translations or variations of the same concept:\n")
            
            for i, pair in enumerate(med_sim[:30], 1):
                report.append(f"{i}. **{pair['similarity']:.1%}**: `{pair['skill1']['skill_name']}` ↔ `{pair['skill2']['skill_name']}`\n")
        
        # Language clusters
        report.append("\n## 🌍 Potential Translation Clusters\n")
        report.append("Groups of skills that appear to be translations of each other:\n\n")
        
        # Simple clustering by skill name similarity
        clusters = self._find_translation_clusters(similar_pairs)
        for i, cluster in enumerate(clusters[:20], 1):
            report.append(f"### Cluster {i}\n")
            for skill in cluster:
                report.append(f"- `{skill['path']}`\n")
            report.append("\n")
        
        # Recommendations
        report.append("\n## 💡 Recommendations\n")
        report.append("""
### For High Similarity Pairs:
1. **Verify if duplicates**: Check if skills are exact duplicates
2. **Identify translations**: If same functionality in different languages, consider:
   - Keeping both with clear language labels
   - Translating to English and archiving originals
   - Creating multilingual documentation

### For Translation Clusters:
1. **Group by functionality**: Skills in same cluster likely do the same thing
2. **Choose canonical version**: Pick English version as primary
3. **Batch translate**: Translate all non-English versions together
4. **Update references**: Ensure all references point to correct versions

### Installation:
To improve detection accuracy, install sentence-transformers:
```bash
pip install sentence-transformers
```
This enables multilingual semantic similarity detection.
""")
        
        return "\n".join(report)
    
    def _find_translation_clusters(self, similar_pairs, threshold=0.5):
        """Find clusters of potentially translated skills"""
        # Simple union-find clustering
        parent = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        # Union skills above threshold
        for pair in similar_pairs:
            if pair['similarity'] >= threshold:
                path1 = pair['skill1']['path']
                path2 = pair['skill2']['path']
                union(path1, path2)
        
        # Group by parent
        clusters = defaultdict(list)
        for skill in self.skill_data:
            path = skill['path']
            if path in parent:
                clusters[find(path)].append(skill)
        
        # Return clusters with more than one skill
        return [c for c in clusters.values() if len(c) > 1]
    
    def save_results(self, similar_pairs, report):
        """Save results to files"""
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        
        # Save markdown report
        report_file = OUTPUT_DIR / "similar-skills-report.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"✅ Report saved to: {report_file}")
        
        # Save JSON data
        json_file = OUTPUT_DIR / "similar-skills-data.json"
        data = {
            'total_skills': len(self.skill_data),
            'similar_pairs_count': len(similar_pairs),
            'similar_pairs': [
                {
                    'skill1_path': p['skill1']['path'],
                    'skill2_path': p['skill2']['path'],
                    'similarity': p['similarity'],
                    'method': p['method'],
                    'skill1_keywords': list(p['skill1']['keywords'])[:20],
                    'skill2_keywords': list(p['skill2']['keywords'])[:20],
                }
                for p in similar_pairs
            ],
            'clusters': [
                [
                    {
                        'path': s['path'],
                        'skill_name': s['skill_name'],
                        'keywords': list(s['keywords'])[:10]
                    }
                    for s in cluster
                ]
                for cluster in self._find_translation_clusters(similar_pairs)
            ]
        }
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ JSON data saved to: {json_file}")


def main():
    print("🔍 Semantic Similarity Detector for Skills\n")
    print("=" * 60)
    
    detector = SemanticSimilarityDetector()
    
    # Scan skills
    detector.scan_skills()
    
    # Compute embeddings if model available
    if detector.model:
        detector.compute_embeddings()
    
    # Find similar skills
    similar_pairs = detector.find_similar_skills(threshold=0.6)
    
    # Generate and save report
    report = detector.generate_report(similar_pairs)
    detector.save_results(similar_pairs, report)
    
    print("\n" + "=" * 60)
    print("📊 SUMMARY:")
    print(f"  Total skills analyzed: {len(detector.skill_data)}")
    print(f"  Similar pairs found: {len(similar_pairs)}")
    print(f"  High similarity (≥80%): {len([p for p in similar_pairs if p['similarity'] >= 0.8])}")
    print(f"  Translation clusters: {len(detector._find_translation_clusters(similar_pairs))}")
    print("=" * 60)


if __name__ == "__main__":
    main()
