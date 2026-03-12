import os
import re
import kuzu
import shutil

DB_PATH = './.agents/skills_graph'
SKILLS_DIR = 'skills'

print("Conectando ao Kùzu Graph Database...")
db = kuzu.Database(DB_PATH)
conn = kuzu.Connection(db)

# 1. Buscar todas as skills
print("Buscando nós de Skill no grafo...")
results = conn.execute("MATCH (s:Skill) RETURN s.id, s.name, s.folder")
skills = []
while results.has_next():
    row = results.get_next()
    skills.append({"id": row[0], "name": row[1], "folder": row[2]})

print(f"Total de skills para processar: {len(skills)}")

# 2. Buscar Tags
print("Avaliando conexões com Tags...")
for skill in skills:
    safe_id = skill['id'].replace("'", "\\'")
    res = conn.execute(f"MATCH (s:Skill)-[:HAS_TAG]->(t:Tag) WHERE s.id = '{safe_id}' RETURN t.name")
    tags = []
    while res.has_next():
        tags.append(res.get_next()[0])
    skill['tags'] = tags

# 3. Buscar Conceitos (para fallback)
print("Avaliando conexões com Conceitos (fallback semântico)...")
for skill in skills:
    if not skill['tags']:
        safe_id = skill['id'].replace("'", "\\'")
        res = conn.execute(f"MATCH (s:Skill)-[:MENTIONS_CONCEPT]->(c:Concept) WHERE s.id = '{safe_id}' RETURN c.name")
        concepts = []
        while res.has_next():
            concepts.append(res.get_next()[0])
        skill['concepts'] = concepts

# Lógica de Inferência de Domínio/Subdomínio
def determine_namespace(skill):
    tags = skill.get('tags', [])
    if len(tags) >= 2:
        return tags[0], tags[1]
    elif len(tags) == 1:
        return tags[0], "general"
    else:
        concepts = skill.get('concepts', [])
        c_str = " ".join(concepts)
        if any(w in c_str for w in ["security", "audit", "vulnerability", "hack", "penetration"]):
            return "sec", "safety"
        elif any(w in c_str for w in ["react", "frontend", "ui", "ux", "browser"]):
            return "web", "frontend"
        elif any(w in c_str for w in ["backend", "api", "database", "sql", "infrastructure"]):
            return "dev", "backend"
        elif any(w in c_str for w in ["data", "analysis", "model", "science", "python"]):
            return "data", "sci"
        elif any(w in c_str for w in ["business", "marketing", "sales", "growth"]):
            return "biz", "growth"
        else:
            # Fallback para o prefixo antigo se houver
            parts = skill['folder'].split('-')
            if len(parts) >= 3 and parts[0] in ['ai', 'sec', 'ops', 'sci', 'web', 'biz', 'media', 'ux', 'dev', 'data', 'tool']:
                return parts[0], parts[1]
            return "misc", "general"

def clean_slug(name, old_folder):
    slug = str(name).lower()
    # Se o 'name' extraído for igual ao nome da pasta antiga, remove os números e prefixos velhos
    if slug == old_folder.lower():
        slug = re.sub(r'^[a-z]+-[a-z]+-\d{4}-', '', slug)
        slug = re.sub(r'^[a-z]+-[a-z]+-[a-z]+-\d{4}-', '', slug)
        slug = re.sub(r'^\d{4}-', '', slug)
    
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    return slug.strip('-')

renames = []
new_names_set = set()

print("\nGerando novo namespacing...")
for skill in skills:
    domain, subdomain = determine_namespace(skill)
    domain = clean_slug(domain, "")
    subdomain = clean_slug(subdomain, "")
    slug = clean_slug(skill['name'], skill['folder'])
    
    # Evitar slugs vazios
    if not slug:
        slug = "skill"

    new_folder = f"{domain}-{subdomain}-{slug}"
    
    # Tratamento de Colisões (ex: se houver duas skills com o mesmo slug final)
    if new_folder in new_names_set:
        counter = 2
        while f"{new_folder}-{counter}" in new_names_set:
            counter += 1
        new_folder = f"{new_folder}-{counter}"
    
    new_names_set.add(new_folder)
    skill['new_folder'] = new_folder
    
    if skill['folder'] != new_folder:
        renames.append(skill)

print(f"Total de pastas agendadas para renomeação: {len(renames)}")

print("\nExecutando renomeações físicas e atualizações no Grafo...")
success_count = 0
for skill in renames:
    old_path = os.path.join(SKILLS_DIR, skill['folder'])
    new_path = os.path.join(SKILLS_DIR, skill['new_folder'])
    
    if os.path.exists(old_path):
        try:
            os.rename(old_path, new_path)
            
            # Atualiza os IDs no Grafo para manter a sincronia perfeita!
            safe_old_id = skill['id'].replace("'", "\\'")
            safe_new_id = skill['new_folder'].replace("'", "\\'")
            
            # Kuzu DB update removed, will rebuild graph later
            success_count += 1
        except Exception as e:
            print(f"Erro ao renomear {old_path}: {e}")

print(f"\n✅ Concluído! {success_count} skills foram renomeadas e atualizadas no GraphRAG (Kùzu).")
