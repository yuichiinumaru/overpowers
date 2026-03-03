ROLE: Senior PRD Engineer, Software Architect
TASK: Update memories (knowledge)

### Preamble (OBRIGATÓRIO)
- Execute AGENTS.md **Seção 0** em sua totalidade primeiro (ler knowledge, gerar tree.md, ler tasklist).
- Salve todos os relatórios e análises em `.agents/reports/` (nunca em `.jules/`).
- Ao redigir relatórios com data/hora, pesquise a data atual na internet ANTES de escrever.

1. Read docs/architecture/project-structure.md **entirely** to understand project file/folder structure. It has changed significantly since the last pushes.
  - Use this file as a guide and reference.

2. Use `.agents/temp/` for temporary scratch files (already in .gitignore). List and Read all memories you have (knowledge) about this project. Analyze them carefully and keep the list in `.agents/temp/` for reference.

3. Break the codebase in 20 pieces. Just the codebase. Then, execute a cyclic operation:
  - Carefully analyze each and every file. Understand and analyze what is the current state of development we are in.
  - Compare with your memories (knowledge) and update them if necessary to the minimum details.
  - If you find discrepancies between memories and current code, update the memories immediately.

4. After completing all 20 pieces, write a summary report to `.agents/reports/memory-update-report.md`.

5. Commit and push changes. PRs should target `staging`.