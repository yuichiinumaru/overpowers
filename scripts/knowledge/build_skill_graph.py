import os
import re
import kuzu
import yaml
import shutil

# Database path
DB_PATH = './.agents/skills_graph'
SKILLS_DIR = 'skills'

# Clean previous DB if exists to start fresh
if os.path.exists(DB_PATH):
    shutil.rmtree(DB_PATH)

print("Inicializando Kùzu Graph Database...")
db = kuzu.Database(DB_PATH)
conn = kuzu.Connection(db)

# 1. Define the Schema
print("Criando Schema do Grafo...")
# Nodes
conn.execute("CREATE NODE TABLE Skill (id STRING, name STRING, folder STRING, description STRING, PRIMARY KEY (id))")
conn.execute("CREATE NODE TABLE Tag (name STRING, PRIMARY KEY (name))")
conn.execute("CREATE NODE TABLE Concept (name STRING, PRIMARY KEY (name))")

# Edges
conn.execute("CREATE REL TABLE HAS_TAG (FROM Skill TO Tag)")
conn.execute("CREATE REL TABLE MENTIONS_CONCEPT (FROM Skill TO Concept)")

# Stopwords for simple concept extraction
STOPWORDS = {"this", "that", "the", "and", "for", "with", "when", "use", "using", "you", "your", "are", "can", "will", "from", "into", "how", "what", "where", "skill", "agent", "agents", "tool", "tools", "tasks", "task"}

def extract_concepts(text):
    if not text:
        return set()
    # Extract capitalized words or valid tech words (simple regex for Phase 1)
    words = re.findall(r'\b[A-Za-z0-9\-]+\b', text)
    concepts = set()
    for word in words:
        w = word.lower()
        if len(w) > 3 and w not in STOPWORDS:
            concepts.add(w)
    return concepts

# Track entities to avoid duplicate insertion errors on Nodes (Tags/Concepts)
inserted_tags = set()
inserted_concepts = set()

print(f"Lendo e processando Skills do diretório '{SKILLS_DIR}'...")

skill_count = 0
for folder in os.listdir(SKILLS_DIR):
    skill_path = os.path.join(SKILLS_DIR, folder)
    if not os.path.isdir(skill_path): continue
    
    skill_md = os.path.join(skill_path, 'SKILL.md')
    if not os.path.exists(skill_md): continue
    
    with open(skill_md, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse YAML frontmatter
    match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    
    name = folder
    description = ""
    tags = []
    
    if match:
        try:
            frontmatter = yaml.safe_load(match.group(1))
            if isinstance(frontmatter, dict):
                name = frontmatter.get('name', folder)
                description = frontmatter.get('description', '')
                raw_tags = frontmatter.get('tags', [])
                if isinstance(raw_tags, list):
                    tags = [str(t).lower().strip() for t in raw_tags if t]
        except yaml.YAMLError:
            pass # Fallback to regex if yaml fails
            
    if not description:
        # Fallback to simple extraction
        desc_match = re.search(r'description:\s*(.+)$', content, re.MULTILINE)
        if desc_match: description = desc_match.group(1).strip()

    # Create Skill Node
    # Escape quotes for cypher
    safe_name = str(name).replace('"', '\"').replace("'", "\\'")
    safe_desc = str(description).replace('"', '\"').replace("'", "\\'")
    safe_folder = str(folder).replace('"', '\"').replace("'", "\\'")
    
    conn.execute(f"CREATE (:Skill {{id: '{safe_folder}', name: '{safe_name}', folder: '{safe_folder}', description: '{safe_desc}'}})")
    
    # Process Tags
    for tag in tags:
        safe_tag = tag.replace('"', '\"').replace("'", "\\'")
        if safe_tag not in inserted_tags:
            conn.execute(f"CREATE (:Tag {{name: '{safe_tag}'}})")
            inserted_tags.add(safe_tag)
        conn.execute(f"MATCH (s:Skill), (t:Tag) WHERE s.id = '{safe_folder}' AND t.name = '{safe_tag}' CREATE (s)-[:HAS_TAG]->(t)")
    
    # Process Concepts from Description
    concepts = extract_concepts(description)
    for concept in concepts:
        safe_concept = concept.replace('"', '\"').replace("'", "\\'")
        if safe_concept not in inserted_concepts:
            conn.execute(f"CREATE (:Concept {{name: '{safe_concept}'}})")
            inserted_concepts.add(safe_concept)
        conn.execute(f"MATCH (s:Skill), (c:Concept) WHERE s.id = '{safe_folder}' AND c.name = '{safe_concept}' CREATE (s)-[:MENTIONS_CONCEPT]->(c)")

    skill_count += 1

print(f"\n✅ Grafo construído com sucesso!")
print(f"Total de Skills ingeridas: {skill_count}")
print(f"Total de Tags únicas: {len(inserted_tags)}")
print(f"Total de Conceitos (Palavras-chave) únicos extraídos: {len(inserted_concepts)}")

# Run a sample query to show clusters
print("\n🔍 Analisando o Grafo (Top 10 Conceitos mais conectados às Skills):")
results = conn.execute("MATCH (s:Skill)-[:MENTIONS_CONCEPT]->(c:Concept) RETURN c.name, COUNT(s) AS degree ORDER BY degree DESC LIMIT 10")
while results.has_next():
    print(results.get_next())
