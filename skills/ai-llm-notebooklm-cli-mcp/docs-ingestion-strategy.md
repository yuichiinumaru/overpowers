# Estratégia de Ingestão de Documentação para NotebookLM

O NotebookLM é uma ferramenta fantástica para RAG (Retrieval-Augmented Generation) e Deep Research, mas possui uma limitação técnica: **um caderno (notebook) suporta no máximo 300 fontes (sources)**. 

Quando tentamos ingerir a documentação completa de um framework (como o Agno, React, Next.js), frequentemente nos deparamos com milhares de arquivos `.md` individuais. Fazer o upload de um por um não apenas estoura o limite de 300 fontes, como também polui o contexto de busca semântica, fragmentando o conhecimento.

A solução para isso é a **Ingestão Baseada em Chunks Semânticos (L1 Directory Chunking)**.

## O Método (Git Clone + Gitingest)

Em vez de enviar os arquivos brutos, usamos o CLI `gitingest` para concatenar diretórios inteiros (como `docs/memory` ou `docs/tools`) em arquivos Markdown únicos e coesos. Assim, transformamos 3.000 arquivos fragmentados em ~30 "livros" (chunks) altamente densos.

### Passo a Passo

1. **Clone o Repositório de Documentação:**
   Encontre o repositório oficial da documentação no GitHub e clone-o para a pasta de referências.
   ```bash
   cd references/
   git clone https://github.com/org/repo-docs
   ```

2. **Crie um Script Python de Chunking (`chunk_docs.py`):**
   Este script vai iterar pelos diretórios de nível 1 (L1) da documentação e usar o `gitingest` para mesclar cada pasta em um arquivo `.md` correspondente.

   ```python
   import os
   import subprocess
   from pathlib import Path

   repo_dir = Path("references/repo-docs")
   output_dir = Path("references/repo-chunks")
   output_dir.mkdir(parents=True, exist_ok=True)

   # Processa diretórios L1
   dirs = [d for d in repo_dir.iterdir() if d.is_dir() and not d.name.startswith('.')]

   for d in dirs:
       # Pula pastas de assets visuais
       if d.name in ['images', 'videos', 'public', 'assets']:
           continue
       
       print(f"Ingerindo diretório: {d.name}...")
       output_file = output_dir / f"docs-{d.name}.md"
       subprocess.run(["gitingest", str(d), "-o", str(output_file)])

   # Arquivos da raiz (README, index)
   print("Ingerindo arquivos da raiz...")
   root_files_dir = output_dir / "root_temp"
   root_files_dir.mkdir(exist_ok=True)

   root_files = [f for f in repo_dir.iterdir() if f.is_file() and not f.name.startswith('.')]
   for f in root_files:
       if f.suffix in ['.md', '.mdx', '.txt']:
           target = root_files_dir / f.name
           target.write_text(f.read_text(encoding='utf-8', errors='ignore'))

   root_output = output_dir / "docs-root-overview.md"
   subprocess.run(["gitingest", str(root_files_dir), "-o", str(root_output)])

   # Cleanup
   import shutil
   shutil.rmtree(root_files_dir)
   print("Chunking completo!")
   ```

3. **Gere um Relatório de Índice:**
   Crie um arquivo `index-report.md` explicando para a IA o que cada arquivo chunk contém (ex: "O arquivo `docs-memory.md` contém tudo sobre vector databases"). 

4. **Crie o Caderno e Faça o Upload:**
   Use o CLI ou MCP do NotebookLM para criar um novo caderno e adicionar todos os arquivos da pasta `repo-chunks` (que agora serão no máximo 30-40 arquivos, muito abaixo do limite de 300).

   ```bash
   nlm create "NOME DO FRAMEWORK"
   nlm add <NOTEBOOK_ID> references/repo-chunks/docs-memory.md
   # Repita para os demais
   ```

## Por que essa abordagem funciona?
- **Evita o Limite:** 3000 arquivos viram 30 arquivos.
- **Árvore de Arquivos:** O `gitingest` injeta a árvore de diretórios no início do arquivo, dando ao LLM consciência de contexto de onde aquela informação estava no projeto original.
- **RAG Mais Eficiente:** O modelo do NotebookLM performa incrivelmente bem quando a resposta inteira de um tópico (como "roteamento de agentes") está contida dentro da mesma fonte, reduzindo alucinações de cross-referencing.