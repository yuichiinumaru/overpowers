import os
import re
import difflib

def get_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove frontmatter for pure content comparison
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
            return content.strip()
    except:
        return ""

def similar(a, b):
    return difflib.SequenceMatcher(None, a, b).quick_ratio()

def find_duplicates_in_dir(directory, is_skill=False):
    items = {}
    print(f"\n==================================================")
    print(f"Scanning '{directory}/' for internal duplicates...")
    print(f"==================================================")
    
    if not os.path.exists(directory):
        print(f"Directory {directory} not found.")
        return
        
    for root, dirs, files in os.walk(directory):
        for file in files:
            if is_skill:
                if file == "SKILL.md":
                    item_name = os.path.basename(root)
                    filepath = os.path.join(root, file)
                else:
                    continue
            else:
                if file.endswith(".md") and file not in ["AGENTS.md", "README.md", "CHANGELOG.md"]:
                    item_name = file
                    filepath = os.path.join(root, file)
                else:
                    continue
                    
            content = get_content(filepath)
            # Apenas ignora arquivos muito vazios
            if content and len(content) > 50:
                items[filepath] = {
                    "name": item_name,
                    "sample": content[:1500].lower(), # Pega uma amostra generosa inicial para otimizar
                    "size": len(content)
                }
                
    print(f"Indexed {len(items)} items. Cross-comparing all of them...")
    
    filepaths = list(items.keys())
    duplicates_found = []
    
    for i in range(len(filepaths)):
        for j in range(i + 1, len(filepaths)):
            path1 = filepaths[i]
            path2 = filepaths[j]
            data1 = items[path1]
            data2 = items[path2]
            
            # Quick exact sample match
            if data1["sample"] == data2["sample"]:
                duplicates_found.append((data1, data2, 1.0))
                continue
                
            # Semantic match
            ratio = similar(data1["sample"], data2["sample"])
            # Threshold de 85% de similaridade
            if ratio > 0.85:
                duplicates_found.append((data1, data2, ratio))
                
    if duplicates_found:
        print(f"🚨 Found {len(duplicates_found)} potential duplicate pairs:\n")
        for d1, d2, ratio in sorted(duplicates_found, key=lambda x: x[2], reverse=True):
            print(f"  [Similarity: {ratio * 100:.1f}%]")
            print(f"    - {d1['name']} ({d1['size']} bytes)")
            print(f"    - {d2['name']} ({d2['size']} bytes)\n")
    else:
        print(f"✅ No internal duplicates found in {directory}.")

if __name__ == "__main__":
    find_duplicates_in_dir("agents", is_skill=False)
    find_duplicates_in_dir("workflows", is_skill=False)
    find_duplicates_in_dir("skills", is_skill=True)
