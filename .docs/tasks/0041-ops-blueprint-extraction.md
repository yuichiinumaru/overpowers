# 0041-ops-blueprint-extraction

## Objetivo

Extrair, adaptar e integrar os assets de valor do repositório `references/claude-code-blueprint/` para o ecossistema Overpowers, seguindo os padrões de nomenclatura, frontmatter e organização já estabelecidos.

## Origem

- `.agents/user/ideas2.md` — Artigo "I Turned Claude Code Into an Operating System"
- `.agents/user/diagram.md` — Análise arquitetural detalhada do Blueprint
- `.agents/user/origin.md` — Notas iniciais de comparação Blueprint vs Overpowers

## Condições de Saída

- [x] Todos os assets identificados foram triados (aceitar/rejeitar/adaptar)
- [x] Assets aceitos estão em seus destinos finais com frontmatter válido
- [x] CHANGELOG.md atualizado
- [x] Nenhum asset duplicado com skills/workflows já existentes

## Inventário de Assets (Source → Status)

### Skills (8 total — `references/claude-code-blueprint/skills/`)

| Skill | Valor p/ Overpowers | Ação | Destino |
|-------|---------------------|------|---------|
| `anti-hallucination` | 🟢 ALTO — decision tree, confidence levels, verification workflow | Adaptar | `skills/anti-hallucination/SKILL.md` |
| `core-protocols` | 🟡 MÉDIO — debugging protocol útil; output templates parcialmente cobertos | Adaptar (extrair debugging) | `skills/core-protocols/SKILL.md` |
| `research-protocol` | 🟢 ALTO — source hierarchy, citation formats, SOTA search strategy | Adaptar | `skills/research-protocol/SKILL.md` |
| `security-audit` | 🟢 ALTO — OWASP top 10 checklist, 4-phase scan, report template | Adaptar | `skills/security-audit/SKILL.md` |
| `brainstorm` | 🟡 MÉDIO — multi-agent pattern; já temos `/ovp-brainstorm` | Comparar e enriquecer | workflow existente |
| `code-patterns` | 🔴 BAIXO — referências genéricas (REST, Docker, CI/CD) | Rejeitar (genérico demais) | — |
| `commit-message` | 🔴 BAIXO — já temos `/ovp-commit`, `/ovp-agentic-commit` | Rejeitar (duplicado) | — |
| `uv-workflow` | 🔴 BAIXO — específico de `uv`; já usamos | Rejeitar (já coberto) | — |

### Hooks (11 total — `references/claude-code-blueprint/hooks/scripts/`)

| Hook | Valor p/ Overpowers | Ação | Destino |
|------|---------------------|------|---------|
| `bash-guard.sh` | 🟢 ALTO | ✅ Adaptado | `hooks/safety/bash-guard.sh` |
| `write-guard.sh` | 🟢 ALTO | ✅ Adaptado | `hooks/safety/write-guard.sh` |
| `write-format.sh` | 🟡 MÉDIO — auto-format after writes | Defer (futuro) | — |
| `session-start.sh` | — Já existe em Overpowers | Skipped | `hooks/session-start.sh` |
| `posttooluse-failure.sh` | 🟡 MÉDIO — tool failure logging | Defer (futuro) | — |
| `pre-compact.sh` | 🟡 MÉDIO — preserva contexto git | Defer (futuro) | — |
| `bash-vuln.sh` | 🟡 BAIXO — post-install vuln detection (27 linhas) | Rejeitar (nicho) | — |
| `permission-git.sh` | 🔴 BAIXO — redundante com bash-guard Art. 24 | Rejeitar | — |
| `session-end.sh` | 🟡 BAIXO — reminder de uncommitted files (23 linhas) | Defer | — |
| `stop.sh` | 🟡 BAIXO — git summary on task end (34 linhas) | Defer | — |
| `user-prompt-secrets.sh` | 🟢 MÉDIO — secret mention warning in prompts | Defer (futuro) | — |

### Agents (4 total — `references/claude-code-blueprint/agents/`)

| Agent | Valor p/ Overpowers | Ação |
|-------|---------------------|------|
| `finance-advisor` | 🔴 BAIXO — fora do escopo | Rejeitar |
| `midjourney-expert` | 🔴 BAIXO — fora do escopo | Rejeitar |
| `prompt-engineer` | 🟡 MÉDIO — conceito válido mas implementação Claude-specific | Avaliar |
| `research-synthesizer` | 🟡 MÉDIO — complementa research-protocol skill | Avaliar |

### Arquitetura & Padrões

| Asset | Valor | Ação |
|-------|-------|------|
| `CLAUDE.md` (kernel) | 🟢 ALTO — Anti-Hallucination Protocol, confidence levels, preservation rules | Extrair padrões |
| `settings.template.json` | 🟢 ALTO — permission model, hook lifecycle, zero-trust | Documentar padrões |
| `docs/architecture.md` | 🟡 MÉDIO — 6-layer model reference | Documentar |
| `rules/python.md` | 🟡 MÉDIO — path-scoped rules pattern | Avaliar |
| `rules/typescript.md` | 🟡 MÉDIO — path-scoped rules pattern | Avaliar |

## Subtarefas

- [x] **Batch 1 — Skills de Alto Valor**: ✅ `anti-hallucination`, `research-protocol`, `blueprint-security-audit`
- [x] **Batch 2 — Hooks de Alto Valor**: ✅ `bash-guard.sh`, `write-guard.sh` (session-start skipped)
- [x] **Batch 3 — Hooks Pendentes**: ✅ Triados — nenhum urgente para extração imediata
- [/] **Batch 4 — Padrões Arquiteturais + CHANGELOG**: Em progresso
- [ ] **Batch 5 — Enriquecimento**: Comparar `brainstorm` skill com `/ovp-brainstorm` existente

## Delegação Sugerida

- **Batches 1-3** (skills + hooks): Pode ser delegado a **Gemini-CLI/Kilo** (tarefas de formatting/adaptação)
- **Batch 4** (documentação arquitetural): Melhor executar localmente (requer contexto)
- **Batch 5** (comparação): Tarefa rápida, executar localmente
