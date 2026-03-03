ROLE: Automated Release Architect

TASK: Generate a comprehensive structured release note bridging the gap since the last major release version.

### Preamble (OBRIGATÓRIO)
- Execute AGENTS.md **Seção 0** em sua totalidade primeiro (ler knowledge, gerar tree.md, ler tasklist).
- Salve o rascunho em `.agents/reports/` (nunca em `.jules/`).
- Ao redigir arquivos com data/hora, pesquise a data atual na internet ANTES de escrever.

1. **Commit Telemetry Extraction**:
   - Obtenha os logs do git das últimas semanas ou do último ciclo. 
   - Execute o comando: `git log --pretty=format:"%h||%an||%aD||%s||%b" -n 50` para obter o log rico.
   
2. **Analysis & Synthesis**:
   - Categorize os commits como `✨ Features`, `🐛 Bug Fixes`, `🏗️ DX/Refactors` ou `🔥 Removals/Cleanup`.
   - Extraia a semântica de valor agregado por trás das manutenções, ignorando commits triviais como "fix typos". Resuma commits interconectados (vários fixes na mesma tela de UI se tornam 1 feature macro).

3. **Draft Generation**:
   - Redija o arquivo `CHANGELOG.md` ou um arquivo `docs/releases/release-notes-YYYY-MM-DD.md`.
   - Ele deve possuir duas subdivisões visuais claras:
     a) **Customer-Facing Output**: Parágrafos claros sobre os benefícios, sem jargão técnico forte.
     b) **Engineering Changelog**: Lista precisa de merges e pacotes afetados.
     
4. **Validation & PR**:
   - Revise o texto. Evite ser prolixo: foque no impacto real ao usuário final ou estabilidade global do sistema.
   - Commit o markdown gerado e submeta o Pull Request contra a branch `staging`.
