import os
import re
import difflib
import shutil
import datetime

def get_skill_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove frontmatter for pure content comparison
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL).strip()
            return content
    except:
        return ""

def similar(a, b):
    return difflib.SequenceMatcher(None, a, b).quick_ratio()

def choose_primary_skill(skill_names):
    """
    Escolhe o melhor nome para ser a pasta principal (primary).
    Evita nomes com muitos hifens ou identificadores longos.
    """
    # Prefer names without numbers like 0812
    no_numbers = [name for name in skill_names if not re.search(r'\d{3,}', name)]
    candidates = no_numbers if no_numbers else skill_names
    
    # Sort by length (shorter is usually cleaner)
    return sorted(candidates, key=len)[0]

def merge_directories(src_dir, dest_dir, src_skill_name, log_entries):
    """
    Move todo o conteúdo de src_dir para dest_dir, adicionando sufixos em caso de colisão.
    """
    for root, dirs, files in os.walk(src_dir):
        # Calculate relative path to mirror structure in dest_dir
        rel_path = os.path.relpath(root, src_dir)
        if rel_path == ".":
            target_dir = dest_dir
        else:
            target_dir = os.path.join(dest_dir, rel_path)
            
        os.makedirs(target_dir, exist_ok=True)
        
        for file in files:
            # Não precisamos copiar o SKILL.md redundante, pois eles são semanticamente iguais
            if file == "SKILL.md" and rel_path == ".":
                continue
                
            src_file = os.path.join(root, file)
            dest_file = os.path.join(target_dir, file)
            
            # Se houver colisão de nome (e não for o mesmo arquivo exato), adiciona sufixo
            if os.path.exists(dest_file):
                base, ext = os.path.splitext(file)
                # Ex: script_run_ai-llm-1234.py
                new_filename = f"{base}_{src_skill_name}{ext}"
                dest_file = os.path.join(target_dir, new_filename)
                log_entries.append(f"    - ⚠️ Colisão: Movido `{os.path.join(rel_path, file)}` como `{os.path.join(rel_path, new_filename)}`")
            else:
                log_entries.append(f"    - Movido `{os.path.join(rel_path, file)}`")
                
            shutil.move(src_file, dest_file)

def find_and_merge_similar_skills(directory="skills", threshold=1.0, dry_run=False):
    if not os.path.exists(directory):
        print(f"Directory {directory} not found.")
        return
        
    skills_data = {}
    print(f"Lendo skills de {directory}/...")
    
    for root, dirs, files in os.walk(directory):
        if "SKILL.md" in files:
            skill_name = os.path.basename(root)
            content = get_skill_content(os.path.join(root, "SKILL.md"))
            if content and len(content) > 50:
                skills_data[skill_name] = {
                    "path": root,
                    "sample": content[:1500].lower() # Amostra para comparação rápida
                }

    print(f"{len(skills_data)} skills indexadas. Buscando similaridades...")
    
    skill_names = list(skills_data.keys())
    processed = set()
    groups = []
    
    # Agrupa skills similares
    for i in range(len(skill_names)):
        name1 = skill_names[i]
        if name1 in processed:
            continue
            
        current_group = [name1]
        processed.add(name1)
        
        for j in range(i + 1, len(skill_names)):
            name2 = skill_names[j]
            if name2 in processed:
                continue
                
            ratio = similar(skills_data[name1]["sample"], skills_data[name2]["sample"])
            if ratio >= threshold:
                current_group.append(name2)
                processed.add(name2)
                
        if len(current_group) > 1:
            groups.append(current_group)

    if not groups:
        print("Nenhuma skill similar encontrada.")
        return

    print(f"Encontrados {len(groups)} grupos de skills similares. Iniciando o merge (Dry Run: {dry_run})...")
    
    report = [f"# Relatório de Merge de Skills Similares (Threshold {threshold*100}%) - DRY RUN: {dry_run}", ""]
    
    for group in groups:
        primary = choose_primary_skill(group)
        duplicates = [s for s in group if s != primary]
        
        primary_path = skills_data[primary]["path"]
        
        report.append(f"## Grupo Consolidado: `{primary}`")
        report.append(f"- **Skill Principal:** `{primary}` (Mantida como base)")
        
        for dup in duplicates:
            dup_path = skills_data[dup]["path"]
            report.append(f"- **Skill Mesclada & Removida:** `{dup}`")
            
            if not dry_run:
                log_entries = []
                merge_directories(dup_path, primary_path, dup, log_entries)
                
                if log_entries:
                    report.extend(log_entries)
                else:
                    report.append("    - (Nenhum arquivo extra para mover além do SKILL.md)")
                    
                # Remove o diretório original que agora deve estar vazio
                try:
                    shutil.rmtree(dup_path)
                except Exception as e:
                    report.append(f"    - ❌ Erro ao deletar pasta {dup_path}: {e}")
            else:
                report.append("    - [Dry Run] Arquivos seriam movidos e pasta original apagada.")
                
        report.append("")

    # Salva o relatório
    os.makedirs(".agents/thoughts", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = f".agents/thoughts/merged_skills_report_{timestamp}.md"
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report))
        
    print(f"\nMerge {'simulado' if dry_run else 'concluído'}! Relatório detalhado salvo em: {report_path}")

if __name__ == "__main__":
    find_and_merge_similar_skills(dry_run=False)
