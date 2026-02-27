ROLE: Code Cleanup & Refactoring Specialist (Dead Code Eliminator)

TASK: Execute a comprehensive cleanup session targeting dead code, unused dependencies, and duplicates.

### Preamble (OBRIGATÓRIO)
- Execute AGENTS.md **Seção 0** em sua totalidade primeiro (ler knowledge, gerar tree.md, ler tasklist).
- Salve todos os registros de deleção e logs `.agents/reports/` (nunca em `.jules/`).
- Ao redigir relatórios com data/hora, pesquise a data atual na internet ANTES de escrever.

1. **Load Skills**:
   - Leia IN-DEPTH as instruções e diretrizes nas skills: `src/agents/skills/code-refactoring/SKILL.md`, `src/agents/skills/code-auditor/SKILL.md` e `src/agents/skills/prevc-refactoring/SKILL.md` (se existirem). Absorva essa metodologia pesadamente antes de atuar.

2. **Detection Phase**:
   - Cace código morto, exports nunca usados (`knip`, `ts-prune`), duplicações grosseiras e dependências no pacote que não têm import no projeto (`depcheck`).

3. **Risk Assessment & Removal**:
   - Procure por dependências mascaradas (imports dinâmicos, scripts shell). 
   - SÓ delete código com a CERTEZA de que é inútil ou após consolidá-lo efetivamente.
   - OBRIGATÓRIO: Rode as suítes de tipagem (`pnpm typecheck`, `tsc`, `nox` ou `pytest`) para validar que nada quebrou. Faça iterativamente: apague, teste. Se falhar, dê rollback e não delete.

4. **Documentation & Deliver**:
   - Registre tudo em `docs/archive/DELETION_LOG.md` (crie se não existir/anexe ao final) mapeando o que foi removido, a razão e os ganhos (redução de espaço/organização).
   - Lance um PR visando a branch `staging` listando as deleções.
