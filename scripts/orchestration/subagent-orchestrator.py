#!/usr/bin/env python3
"""
Subagent Orchestrator - Dispatch multiple opencode subagents in parallel to analyze repos.
Each subagent analyzes one repo and outputs a markdown report.
"""

import subprocess
import os
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration
ARCHIVE_DIR = Path("/home/sephiroth/.config/opencode/archive")
OUTPUT_DIR = Path("/home/sephiroth/.config/opencode/Overpowers/docs")
INVENTORY_FILE = OUTPUT_DIR / "inventory.md"
MODEL = "google/antigravity-claude-sonnet-4-5-thinking"
MAX_PARALLEL = 3  # Number of concurrent subagents

# Prompt template
PROMPT_TEMPLATE = '''Você é um analista de repositórios de Claude Code.

TAREFA: Analisar {repo_path} e identificar assets úteis.

INSTRUÇÕES:
1. Leia {inventory_file} para saber o que já temos (389 agents, 148 skills, 227 commands)
2. Analise o repo alvo e identifique assets NOVOS e ÚTEIS
3. Foque em: agents, skills, workflows, commands, scripts úteis
4. Ignore: __init__.py, testes, configs genéricos, node_modules, .git

OUTPUT em markdown (máximo 40 linhas):

## Repositório: {repo_name}
(estrutura resumida - max 10 linhas)

## Novos Assets Recomendados
| Tipo | Nome | Descrição | Prioridade |
(tabela com itens úteis que NÃO temos - max 6 itens)

## Recomendação
(1 frase: SKIP se nada útil, ou IMPORTAR com justificativa)'''


def get_repos_to_analyze():
    """Get list of repos in archive directory."""
    repos = []
    for item in sorted(ARCHIVE_DIR.iterdir()):
        if item.is_dir() and not item.name.startswith('.'):
            repos.append(item)
    return repos


def analyze_repo(repo_path: Path, index: int) -> dict:
    """Run opencode subagent to analyze a single repo."""
    repo_name = repo_path.name
    output_file = OUTPUT_DIR / f"{index:02d}-{repo_name}.md"
    
    prompt = PROMPT_TEMPLATE.format(
        repo_path=repo_path,
        repo_name=repo_name,
        inventory_file=INVENTORY_FILE
    )
    
    # Build command
    cmd = [
        "opencode", "run",
        prompt,
        "--model", MODEL
    ]
    
    print(f"🚀 [{index:02d}] Starting: {repo_name}")
    start_time = time.time()
    
    try:
        # Set OPENCODE_PERMISSION to allow for non-interactive mode
        env = os.environ.copy()
        env['OPENCODE_PERMISSION'] = '"allow"'
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,  # 5 min max per repo
            cwd=str(repo_path),
            env=env
        )
        
        elapsed = time.time() - start_time
        
        # Extract only the markdown output (skip ANSI codes and permission prompts)
        output = result.stdout
        
        # Find where the actual content starts
        lines = output.split('\n')
        content_lines = []
        capture = False
        for line in lines:
            if line.startswith('## Repositório') or line.startswith('# '):
                capture = True
            if capture:
                # Remove ANSI escape codes
                clean_line = line
                for code in ['\x1b[?25l', '\x1b[?25h', '\x1b[J', '\x1b[999D']:
                    clean_line = clean_line.replace(code, '')
                if not clean_line.startswith('│') and not clean_line.startswith('◆') and not clean_line.startswith('◇'):
                    content_lines.append(clean_line)
        
        content = '\n'.join(content_lines).strip()
        
        if content:
            # Add header
            final_content = f"# {index:02d} - {repo_name}\n\n> Análise automática por subagent\n\n{content}"
            output_file.write_text(final_content)
            print(f"✅ [{index:02d}] Done: {repo_name} ({elapsed:.1f}s) -> {output_file.name}")
            return {"repo": repo_name, "status": "success", "file": str(output_file), "time": elapsed}
        else:
            print(f"⚠️ [{index:02d}] Empty: {repo_name} ({elapsed:.1f}s)")
            return {"repo": repo_name, "status": "empty", "time": elapsed}
            
    except subprocess.TimeoutExpired:
        print(f"⏰ [{index:02d}] Timeout: {repo_name}")
        return {"repo": repo_name, "status": "timeout"}
    except Exception as e:
        print(f"❌ [{index:02d}] Error: {repo_name} - {e}")
        return {"repo": repo_name, "status": "error", "error": str(e)}


def main():
    """Main orchestration function."""
    repos = get_repos_to_analyze()
    print(f"\n📦 Found {len(repos)} repos to analyze")
    print(f"🔧 Using model: {MODEL}")
    print(f"⚡ Max parallel: {MAX_PARALLEL}")
    print(f"📁 Output dir: {OUTPUT_DIR}\n")
    
    # For testing, limit to first 3 repos
    test_repos = repos[:3]
    print(f"🧪 TEST MODE: Analyzing first {len(test_repos)} repos only\n")
    
    results = []
    start_total = time.time()
    
    with ThreadPoolExecutor(max_workers=MAX_PARALLEL) as executor:
        futures = {
            executor.submit(analyze_repo, repo, idx + 2): repo  # Start from 02 since 01 is done
            for idx, repo in enumerate(test_repos)
        }
        
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
    
    # Summary
    elapsed_total = time.time() - start_total
    success = sum(1 for r in results if r["status"] == "success")
    
    print(f"\n{'='*50}")
    print(f"📊 Summary: {success}/{len(results)} successful")
    print(f"⏱️ Total time: {elapsed_total:.1f}s")
    print(f"📁 Reports saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
