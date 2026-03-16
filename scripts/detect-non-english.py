#!/usr/bin/env python3
"""
Detect non-English content in agents, skills, workflows, and hooks.
Exports detailed results to .docs/tasks/planning/non-english-items.md
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import json

# Base directory
BASE_DIR = Path("/home/sephiroth/Work/overpowers")

# Directories to scan
SCAN_DIRS = {
    "agents": BASE_DIR / "agents",
    "skills": BASE_DIR / "skills",
    "workflows": BASE_DIR / "workflows",
    "hooks": BASE_DIR / "hooks",
}

# Output directory
OUTPUT_DIR = BASE_DIR / ".docs" / "tasks" / "planning"
OUTPUT_FILE = OUTPUT_DIR / "non-english-items.md"


def is_english_text(text):
    """
    Heuristic to detect if text is primarily English.
    Returns (is_english, confidence, detected_languages)
    """
    # Common non-English character ranges
    non_english_patterns = {
        "Chinese": r"[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]",
        "Japanese": r"[\u3040-\u309f\u30a0-\u30ff\u3190-\u319f]",
        "Korean": r"[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f]",
        "Arabic": r"[\u0600-\u06ff\u0750-\u077f]",
        "Cyrillic": r"[\u0400-\u04ff\u0500-\u052f]",
        "Greek": r"[\u0370-\u03ff\u1f00-\u1fff]",
        "Hebrew": r"[\u0590-\u05ff]",
        "Thai": r"[\u0e00-\u0e7f]",
        "Vietnamese": r"[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]",
        "Portuguese_accents": r"[ãõçáéíóúàèìòùâêîôûäëïöüÿ]",
        "Spanish_accents": r"[áéíóúñ¿¡]",
        "French_accents": r"[àâçéèêëïîôùûüÿœæ]",
        "German_accents": r"[äöüßÄÖÜ]",
    }
    
    # Count non-English characters
    detected = {}
    total_chars = len(text)
    
    for lang, pattern in non_english_patterns.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            count = len(matches)
            percentage = (count / total_chars * 100) if total_chars > 0 else 0
            if percentage > 1:  # More than 1% of text
                detected[lang] = {
                    "count": count,
                    "percentage": round(percentage, 2)
                }
    
    # Determine if primarily English
    # If any significant non-English content detected (>5%)
    is_english = all(v["percentage"] < 5 for v in detected.values())
    
    # Calculate confidence
    if not detected:
        confidence = 0.95  # High confidence it's English
    else:
        max_non_english = max(v["percentage"] for v in detected.values())
        confidence = max(0.5, 1.0 - (max_non_english / 100))
    
    return is_english, confidence, detected


def extract_frontmatter_metadata(content, file_path):
    """Extract metadata from YAML frontmatter"""
    metadata = {}
    
    # Try to extract YAML frontmatter
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        
        # Extract common fields
        for field in ['name', 'description', 'role', 'persona', 'department']:
            match = re.search(rf'{field}:\s*(.+?)(?:\n|$)', frontmatter, re.IGNORECASE)
            if match:
                metadata[field] = match.group(1).strip()
    
    return metadata


def scan_file(file_path):
    """Scan a single file for non-English content"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        return None
    
    # Skip very small files (< 50 chars)
    if len(content) < 50:
        return None
    
    # Extract frontmatter metadata
    metadata = extract_frontmatter_metadata(content, file_path)
    
    # Check full content
    is_english, confidence, detected_langs = is_english_text(content)
    
    # Also check just the frontmatter metadata
    metadata_text = ' '.join(str(v) for v in metadata.values())
    meta_is_english, meta_confidence, meta_detected = is_english_text(metadata_text) if metadata_text else (True, 1.0, {})
    
    result = {
        "path": str(file_path.relative_to(BASE_DIR)),
        "is_english": is_english,
        "confidence": round(confidence, 3),
        "detected_languages": detected_langs,
        "metadata": metadata,
        "metadata_is_english": meta_is_english,
        "metadata_confidence": round(meta_confidence, 3),
        "metadata_detected": meta_detected,
        "size_kb": round(len(content) / 1024, 2),
    }
    
    return result


def scan_directory(dir_path, category):
    """Scan all files in a directory recursively"""
    results = []
    
    if not dir_path.exists():
        print(f"⚠️  Directory not found: {dir_path}")
        return results
    
    # Get all files (recursively)
    all_files = []
    for root, dirs, files in os.walk(dir_path):
        # Skip hidden directories and common non-text directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', '.git']]
        
        for file in files:
            if file.endswith(('.md', '.txt', '.json', '.yaml', '.yml', '.toml')):
                all_files.append(Path(root) / file)
    
    print(f"📂 Scanning {category}: {len(all_files)} files...")
    
    for file_path in all_files:
        result = scan_file(file_path)
        if result:
            results.append(result)
    
    return results


def generate_report(all_results):
    """Generate a detailed markdown report"""
    
    # Categorize results
    non_english = defaultdict(list)
    mixed = defaultdict(list)
    english = defaultdict(list)
    
    for category, results in all_results.items():
        for result in results:
            # Determine classification
            if not result["is_english"] or not result["metadata_is_english"]:
                if result["confidence"] < 0.7 or result["metadata_confidence"] < 0.7:
                    non_english[category].append(result)
                else:
                    mixed[category].append(result)
            else:
                english[category].append(result)
    
    # Generate report
    report = []
    report.append("# Non-English Content Detection Report\n")
    report.append(f"**Generated**: {Path.home()}/Work/overpowers/scripts/detect-non-english.py\n")
    report.append(f"**Base Directory**: `{BASE_DIR}`\n")
    report.append(f"**Total Files Scanned**: {sum(len(v) for v in all_results.values())}\n")
    
    # Summary statistics
    report.append("\n## 📊 Summary Statistics\n")
    report.append("| Category | Total | Non-English | Mixed | English |")
    report.append("|---------|-------|-------------|-------|---------|")
    
    for category in ["agents", "skills", "workflows", "hooks"]:
        total = len(all_results.get(category, []))
        ne = len(non_english.get(category, []))
        mx = len(mixed.get(category, []))
        en = len(english.get(category, []))
        report.append(f"| {category} | {total} | {ne} | {mx} | {en} |")
    
    total_all = sum(len(v) for v in all_results.values())
    ne_all = sum(len(v) for v in non_english.values())
    mx_all = sum(len(v) for v in mixed.values())
    en_all = sum(len(v) for v in english.values())
    report.append(f"| **TOTAL** | {total_all} | {ne_all} | {mx_all} | {en_all} |")
    
    # Detailed listings
    for category, label in [("agents", "Agents"), ("skills", "Skills"), 
                            ("workflows", "Workflows"), ("hooks", "Hooks")]:
        
        if non_english.get(category):
            report.append(f"\n## 🚫 Non-English {label}\n")
            report.append(f"**Count**: {len(non_english[category])} files\n")
            report.append("| File | Confidence | Detected Languages | Metadata | Size |")
            report.append("|------|------------|-------------------|----------|------|")
            
            for item in sorted(non_english[category], key=lambda x: x["confidence"]):
                langs = ", ".join(f"{k} ({v['percentage']}%)" for k, v in item["detected_languages"].items())
                meta_langs = ", ".join(f"{k} ({v['percentage']}%)" for k, v in item["metadata_detected"].items()) if item["metadata_detected"] else "English"
                meta_info = f"{item.get('metadata', {}).get('name', 'N/A')}"
                report.append(f"| `{item['path']}` | {item['confidence']:.1%} | {langs} | {meta_info} | {item['size_kb']} KB |")
        
        if mixed.get(category):
            report.append(f"\n## ⚠️ Mixed Language {label}\n")
            report.append(f"**Count**: {len(mixed[category])} files (may contain some non-English but mostly English)\n")
            report.append("| File | Confidence | Detected Languages | Metadata | Size |")
            report.append("|------|------------|-------------------|----------|------|")
            
            for item in sorted(mixed[category], key=lambda x: x["confidence"])[:50]:  # Limit to 50
                langs = ", ".join(f"{k} ({v['percentage']}%)" for k, v in item["detected_languages"].items())
                meta_langs = ", ".join(f"{k} ({v['percentage']}%)" for k, v in item["metadata_detected"].items()) if item["metadata_detected"] else "English"
                meta_info = f"{item.get('metadata', {}).get('name', 'N/A')}"
                report.append(f"| `{item['path']}` | {item['confidence']:.1%} | {langs} | {meta_info} | {item['size_kb']} KB |")
            
            if len(mixed[category]) > 50:
                report.append(f"\n*... and {len(mixed[category]) - 50} more files*")
    
    # Recommendations
    report.append("\n## 💡 Recommendations\n")
    report.append("""
### For Non-English Files:
1. **Translate to English**: Consider translating content to English for consistency
2. **Add English Metadata**: At minimum, ensure frontmatter metadata (name, description) is in English
3. **Document Language**: If keeping non-English content, document the language in the file metadata
4. **Create Language-Specific Variants**: Consider creating separate files for different languages

### For Mixed Language Files:
1. **Review Metadata**: Ensure file names and descriptions are in English
2. **Standardize**: Consider standardizing on English for technical documentation
3. **Add Language Tags**: Add language tags to frontmatter for better organization

### Naming Convention:
- Use English for all file names
- Use English for frontmatter metadata (name, description)
- Content can be in any language, but document it in metadata
""")
    
    # Export JSON data
    report.append("\n## 📁 Raw Data Export\n")
    report.append("Raw JSON data available at: `.docs/tasks/planning/non-english-data.json`\n")
    
    return "\n".join(report), {
        "non_english": dict(non_english),
        "mixed": dict(mixed),
        "english": dict(english),
        "all_results": all_results,
    }


def main():
    print("🔍 Non-English Content Detector\n")
    print("=" * 60)
    
    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Scan all directories
    all_results = {}
    for category, dir_path in SCAN_DIRS.items():
        results = scan_directory(dir_path, category)
        all_results[category] = results
        print(f"✅ Found {len(results)} files in {category}")
        print()
    
    # Generate report
    print("📝 Generating report...")
    report, data = generate_report(all_results)
    
    # Write markdown report
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"✅ Report saved to: {OUTPUT_FILE}")
    
    # Write JSON data
    json_file = OUTPUT_DIR / "non-english-data.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ JSON data saved to: {json_file}")
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 SUMMARY:")
    print(f"  Total files scanned: {sum(len(v) for v in all_results.values())}")
    print(f"  Non-English files: {sum(len(v) for v in data['non_english'].values())}")
    print(f"  Mixed language files: {sum(len(v) for v in data['mixed'].values())}")
    print(f"  English files: {sum(len(v) for v in data['english'].values())}")
    print("=" * 60)


if __name__ == "__main__":
    main()
