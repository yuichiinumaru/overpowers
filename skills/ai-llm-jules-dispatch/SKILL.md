---
name: jules-orchestrator
description: Complete management of Jules lifecycle: Login, Dispatch, Harvest, Triage, and Integration.
tags:
- ai
- llm
- automation
- orchestration
---

# Jules Orchestrator (Consolidated Skill)

This skill provides a unified workflow for managing the entire lifecycle of **Jules** (Google's asynchronous AI agent) within the Overpowers toolkit. It covers authentication, task dispatching, branch harvesting, parallel triage, and surgical integration.

## 1. Authentication & Quota Management

Jules Pro accounts have strict limits. This skill manages the rotation and monitoring of these quotas.

- **Concurrent Limit**: 15 tasks per account.
- **Daily Limit**: 100 tasks per account.
- **Redundancy Factor**: 1 defined task = 2 actual Jules jobs (for QA).
- **Execution Pattern**: Launch 7 tasks (14 jobs), then rotate accounts.

### Account Rotation
1. **Invoke Login**: Run `jules login`.
2. **Authenticate**: Follow the browser link.
3. **Select Account**: Choose a fresh account with available quota.

---

## 2. The Jules Pipeline (4-Stage Workflow)

To prevent API limits and manage massive diffs effectively, follow this pipeline:

1. **Launch**: `./scripts/01-jules-launch.sh <plan.json>`
   - Dispatches tasks and logs to `.agents/jules_sessions.json`.
2. **Harvest**: `python3 scripts/02-jules-harvest.py`
   - Fetches branches and pulls raw `.diff` files into `.archive/harvest/jules/`.
3. **Triage**: `python3 scripts/03-jules-preview.py`
   - Generates local context for surgical preview.
4. **Apply**: `./scripts/04-jj-apply.sh <SESSION_ID>` or `./scripts/04-scaffold-adapt.sh`
   - Safely integrates the chosen work via Jujutsu or manual adaptation.

---

## 3. Harvesting & Worktree Management

Jules delivers work as git branches. Harvesting organizes them into worktrees for parallel analysis.

### Directory Structure
```
project/
├── .jules/
│   ├── pending/       # Waiting for completion
│   ├── harvested/    # Catalog of fetched branches ({branch}.md)
│   ├── triage/       # Assessment reports
│   └── HARVEST-INDEX.md
└── branches/          # Git worktrees (gitignored)
```

### Harvest Process
1. **Fetch**: `git fetch --all --prune`
2. **Worktrees**: Create a worktree for each new `origin/jules/*` branch.
3. **Catalog**: Generate stats and commit summaries in `.jules/harvested/`.

---

## 4. Parallel Triage Strategy

Use swarms or multiple tasks to analyze branches in parallel. Categorize each branch:

| Category | Recommendation |
|:---|:---|
| ✅ **MERGE** | High value, low friction. Ready for direct integration. |
| 🔧 **ADAPT** | Valuable logic but needs pattern/style adjustments. |
| 📝 **DOCS-ONLY** | Extract plans, diagrams, or documentation only. |
| ❌ **DISCARD** | Low value, redundant, or misaligned with roadmap. |


## Analysis Checklist

### 1. Code Quality (1-10)
- [ ] Code compiles/runs
- [ ] Follows project conventions
- [ ] Has adequate comments
- [ ] Error handling present
- [ ] No obvious bugs

### 2. Value Assessment
- [ ] Solves intended problem
- [ ] Novel approach (vs existing code)
- [ ] Reusable components
- [ ] Good documentation

### 3. Integration Complexity
- [ ] Self-contained (easy)
- [ ] Minor adaptations needed (medium)
- [ ] Major refactoring required (hard)
- [ ] Conflicts with existing code (very hard)

### 4. Conflict Detection
Check for conflicts with:
- Existing file paths
- Naming conventions
- Architecture patterns
- Dependencies

---

## 5. Surgical Integration & Cleanup

Integration must be surgical. Never bulk-merge without understanding.

### Integration Categories
- **MERGE**: Cherry-pick files, adapt paths, run tests, commit with attribution.
- **ADAPT**: Extract core patterns, rewrite following Overpowers conventions.
- **DOCS**: Move to `docs/proposals/` or relevant documentation folders.
- **DISCARD**: Remove local worktree and delete remote branch.

---

## 6. Maintenance & Cleanup

After successful integration or discarding:
1. **Update Index**: Mark status as `Integrated` in `HARVEST-INDEX.md`.
2. **Remove Worktrees**: `git worktree remove branches/{branch-name}`.
3. **Archive Records**: Move metadata from `harvested/` to `archived/`.

---

## ⚠️ MANDATORY RULES FOR AGENTS ⚠️
- **READ GUIDE.md**: Critical anti-hallucination rules are in `GUIDE.md`.
- **NO DELETES**: Follow **Protocol Zero**. Use `.archive/` instead of `rm`.
- **VCS SAFETY**: Use **Jujutsu (JJ)** for all repository mutations. NEVER use raw `git commit/push`.
- **OFFLOAD THOUGHTS**: Use `.agents/thoughts/jules/` for long operations.


# GUIDE: O Pipeline de Colheita (Jules Pipeline)

## 🚨 REGRAS ESTRITAS DE EXECUÇÃO PARA O AGENTE (NÃO IGNORE) 🚨
**ATENÇÃO AGENTE DE IA:** Não tente ser espertinho com a execução desses scripts. Você tem a péssima tendência de alterar comandos com base em heurísticas genéricas de segurança. Siga estas regras EXATAMENTE como estão aqui:

1. **NÃO USE REDIRECIONAMENTO DE LOG (`> log.txt` ou `2>&1`):** Você deve rodar o script de launcher EXATAMENTE como `./scripts/jules-launcher-v2.sh <plan.json>`. Não anexe `> jules.log` nem tente dar `tail` nele. O Jules NÃO exibe logs no terminal progressivamente e não dá output interativo. Ele apenas faz a tarefa na nuvem e pronto.
2. **NÃO PULE O LOGIN:** Não decida por conta própria que "fazer login" não é a boa porque você acha que pode automatizar de outro jeito. A skill foi desenhada assim por um motivo. A forma devida de usar a skill é rodando o script de login quando solicitado.
3. **NÃO É UM COMANDO INTERATIVO QUE VAI TE TRAVAR:** O comando na CLI não é um prompt interativo no terminal em que você não vai conseguir responder. Ele vai abrir o navegador automaticamente. O usuário HUMANO vai saber que é para apenas clicar em outra conta no browser para logar e finalizar. Apenas rode o comando normalmente.

---

Para contornar limites de API, PRs vazios e facilitar a integração massiva de código do Jules, esta skill utiliza um pipeline de 4 estágios. Ele isola os diffs em uma área de staging ("quarentena") antes de aplicá-los na sua base de código principal usando Jujutsu.

## Estágio 1: Disparo (Launch & Log)
O script `01-prompt-helper.py` (chamado por `01-jules-launch.sh`) envia a tarefa para a nuvem.
- **O que faz:** Ao receber o Session ID do Jules, ele imediatamente salva essa informação no arquivo de rastreamento `.agents/jules_sessions.json`.
- **Como usar:** `./scripts/01-jules-launch.sh caminho/para/seu/plano.json`

## Estágio 2: Colheita (Harvest)
Após o Jules concluir a execução na nuvem, você precisa puxar os diffs.
- **O que faz:** O script `02-jules-harvest.py` lê o arquivo de rastreamento `.agents/jules_sessions.json`, baixa os diffs através do comando `jules remote pull --diff` e os salva em `.archive/harvest/jules/<session_id>.diff`. Ele também gera um `HARVEST_REPORT.md` mostrando o tamanho de cada diff e quantos arquivos foram tocados, ajudando a identificar tarefas que falharam ou retornaram 0KB.
- **Como usar:** `python3 scripts/02-jules-harvest.py`

## Estágio 3: Pré-Visualização (Surgical Preview)
Antes de aplicar às cegas, audite o código.
- **O que faz:** O script `03-jules-preview.py` lê os diffs salvos no diretório de harvest e gera um `PREVIEW_REPORT.md`. Este relatório contém as primeiras 10-15 linhas de contexto de cada arquivo alterado. Isso permite que você avalie rapidamente se o código faz sentido sem precisar abrir diffs com milhares de linhas.
- **Como usar:** `python3 scripts/03-jules-preview.py`

## Estágio 4: Integração via Jujutsu (JJ Auto-Apply)
Quando escolher qual sessão integrar (baseado nos relatórios), aplique na sua codebase de forma segura.
- **O que faz:** O script `04-jj-apply.sh` cria um novo commit Jujutsu com a descrição apropriada e tenta aplicar o patch usando o comando `patch`. Se houver conflitos, ele falhará graciosamente, deixando o patch pendente para resolução manual ou descarte via `jj abandon`.
- **Como usar:** `./scripts/04-jj-apply.sh <SESSION_ID>`
