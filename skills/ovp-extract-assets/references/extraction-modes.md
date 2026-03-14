# Extraction Modes Guide

Guia detalhado dos 4 modos de operação da skill `ovp-extract-assets`.

---

## Visão Geral

| Modo | Nome | Gatilho | Fases | Quando Usar |
|------|------|---------|-------|-------------|
| **1** | `process-staging` | Task file ou `--staging` | 2 → 4 → 5 | Batch já está em staging |
| **2** | `github-mine` | URLs GitHub | 1 → 2 → 4 → 5 | Extrair de repos GitHub |
| **3** | `audit-and-migrate` | `--audit` | 3 | Identificar assets auxiliares |
| **4** | `full-pipeline` | `--full <urls>` | 1 → 2 → 3 → 4 → 5 | Pipeline completo |

---

## Modo 1: Process Staging

### Quando Usar

- ✅ Você já executou `/ovp-batch-assets-extraction` antes e tem arquivos em `.archive/staging/`
- ✅ Tem um task file (`.docs/tasks/0500-extraction-skills-batch-*.md`)
- ✅ Quer apenas processar, sem clone ou auditoria

### Comando

```bash
python3 skills/ovp-extract-assets/scripts/process-all-staging.py --batch all
```

### O Que Acontece

1. Lê `.archive/staging/skills/*.md`, `.archive/staging/agents/*.md`, etc.
2. Padroniza frontmatter YAML
3. Move para `skills/<name>/SKILL.md`, `agents/ovp-<name>.md`, etc.
4. Gera `.docs/batch-processing-log.json`
5. **NÃO deleta** staging (aguarda verificação)

### Pós-Processamento

```bash
# 1. Verificar sample (manual, 10%)
# 2. Se OK, limpar staging
python3 skills/ovp-extract-assets/scripts/mass-cleanup-staging.py
```

---

## Modo 2: GitHub Mine

### Quando Usar

- ✅ Tem URLs de repositórios GitHub
- ✅ Quer extrair skills/agents/workflows/hooks
- ✅ Repo pode ser "direct skills" ou "awesome list"

### Comando

```bash
# URLs diretas
python3 skills/ovp-extract-assets/scripts/clone-github-repos.py \
  https://github.com/user/repo1 \
  https://github.com/user/repo2

# De arquivo
python3 skills/ovp-extract-assets/scripts/clone-github-repos.py --file repos.txt
```

### O Que Acontece

1. Clone shallow (último commit apenas)
2. Detecta tipo (direct vs awesome list)
3. Extrai para `.archive/staging/<tipo>/`
4. Cleanup dos clones

### Pós-Processamento

```bash
# Processar o que foi extraído
python3 skills/ovp-extract-assets/scripts/process-all-staging.py --batch all

# Opcional: Auditar e migrar assets
python3 skills/ovp-extract-assets/scripts/skill-origins-tracker.py
python3 skills/ovp-extract-assets/scripts/migrate-auxiliary-assets.py

# Cleanup final
python3 skills/ovp-extract-assets/scripts/mass-cleanup-staging.py
```

---

## Modo 3: Audit and Migrate

### Quando Usar

- ✅ Skills já processados em `skills/`
- ✅ Quer identificar quais têm assets auxiliares
- ✅ Quer migrar scripts/, references/ para as pastas corretas

### Comando

```bash
# 1. Auditoria (identifica assets)
python3 skills/ovp-extract-assets/scripts/skill-origins-tracker.py

# 2. Migração (após review do relatório)
python3 skills/ovp-extract-assets/scripts/migrate-auxiliary-assets.py
```

### O Que Acontece

**Auditoria**:
1. Lê `.docs/batch-processing-log.json`
2. Rastreia origens via `.archive/staging/manifest.json`
3. Identifica skills com scripts/, references/ na origem
4. Gera `.docs/skill-origins-report.json`

**Migração**:
1. Lê `.docs/skill-origins-report.json`
2. Copia scripts/ para `skills/<name>/scripts/`
3. Copia references/ para `skills/<name>/references/`
4. Gera `.docs/auxiliary-assets-migration-log.json`

### Output Esperado

```
📊 1645 skills com scripts/
📊 236 skills com references/
📊 3780 scripts migrados
📊 887 referências migradas
```

---

## Modo 4: Full Pipeline

### Quando Usar

- ✅ URLs GitHub fornecidas
- ✅ Quer TUDO automático: clone → process → audit → migrate → cleanup

### Comando

```bash
# One-liner (todos os scripts em sequência)
python3 skills/ovp-extract-assets/scripts/clone-github-repos.py <urls> && \
python3 skills/ovp-extract-assets/scripts/process-all-staging.py --batch all && \
python3 skills/ovp-extract-assets/scripts/skill-origins-tracker.py && \
python3 skills/ovp-extract-assets/scripts/migrate-auxiliary-assets.py && \
python3 skills/ovp-extract-assets/scripts/mass-cleanup-staging.py
```

### O Que Acontece

1. **Fase 1**: Clone GitHub → Staging
2. **Fase 2**: Process & Standardize
3. **Fase 3**: Audit & Migrate Assets
4. **Fase 4**: Verificação (sample 10%)
5. **Fase 5**: Cleanup Staging

### Atenção

- **Fase 4 requer aprovação manual** antes de prosseguir para Fase 5
- Sample de 10% deve ser verificado manualmente
- Se encontrar issues, reporte antes de cleanup

---

## Comparação de Modos

| Critério | Modo 1 | Modo 2 | Modo 3 | Modo 4 |
|----------|--------|--------|--------|--------|
| **Origem** | Staging | GitHub | Skills processados | GitHub |
| **Clone** | ❌ | ✅ | ❌ | ✅ |
| **Process** | ✅ | ✅ | ❌ | ✅ |
| **Audit** | ❌ | ❌ | ✅ | ✅ |
| **Migrate** | ❌ | ❌ | ✅ | ✅ |
| **Cleanup** | ✅ | ✅ | ❌ | ✅ |
| **Tempo** | ~5 min | ~15 min | ~10 min | ~30 min |
| **Aprovação** | Antes cleanup | Antes cleanup | Opcional | Antes cleanup |

---

## Exemplos por Cenário

### Cenário 1: Batch Semanal do Staging

```bash
# Segunda-feira: processar batch da semana
/ovp-extract-assets --task 0500-extraction-skills-batch-042.md

# Terça: auditar e migrar assets
/ovp-extract-assets --audit

# Quarta: cleanup após aprovação
python3 skills/ovp-extract-assets/scripts/mass-cleanup-staging.py
```

### Cenário 2: Mineração de Repositórios

```bash
# Extrair de múltiplos repos
/ovp-extract-assets --github \
  https://github.com/openclawskills/skills \
  https://github.com/user/awesome-agents \
  https://github.com/org/workflows

# Processar e migrar assets
python3 skills/ovp-extract-assets/scripts/process-all-staging.py --batch all
python3 skills/ovp-extract-assets/scripts/migrate-auxiliary-assets.py
```

### Cenário 3: Pipeline Completo

```bash
# Tudo automático (com aprovação na Fase 4)
/ovp-extract-assets --full https://github.com/user/repo
```

---

## Troubleshooting

### "Staging não existe"

Use Modo 2 ou 4 (GitHub) para criar staging primeiro.

### "Assets não foram migrados"

Execute Modo 3 (`--audit`) após processamento.

### "Cleanup falhou"

Verifique se Fase 4 foi completada e aprovada.

### "Clone timeout"

Repositório muito grande. Tente clone manual e use Modo 1.

---

*Guia de Modos de Extração - Versão 1.0*
