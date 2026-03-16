---
name: ovp-extract-assets
description: "Extração em massa de assets (skills, agents, workflows, hooks) de múltiplas origens (staging, GitHub, local). Suporta processamento, auditoria, migração de assets auxiliares e cleanup. Pipeline completo ou fases individuais."
metadata:
  openclaw:
    category: "automation"
    tags: ['automation', 'batch', 'extraction', 'migration', 'github', 'staging']
    version: "2.0.0"
    scripts:
      - scripts/process-all-staging.py
      - scripts/migrate-staging-assets.py
      - scripts/skill-assets-auditor.py
      - scripts/skill-origins-tracker.py
      - scripts/migrate-auxiliary-assets.py
      - scripts/mass-cleanup-staging.py
      - scripts/clone-github-repos.py
---

# /ovp-extract-assets (Batch Assets Extraction)

**Skill unificada para extração em massa de assets** - Skills, Agents, Workflows, Hooks de múltiplas origens (staging, GitHub, local) com pipeline completo de processamento, auditoria, migração de assets auxiliares e cleanup.

---

## 🎯 4 Modos de Operação

### **Modo 1: `process-staging`** (Processamento de Staging)

**Quando usar**: Você já tem arquivos em `.archive/staging/` e quer processá-los.

**Gatilhos**:
- "Processe o batch 0500-extraction-skills-batch-037"
- "Extraia todos os arquivos do staging"
- `/ovp-extract-assets --staging`

**O que faz**:
1. Lê arquivos de `.archive/staging/skills/`, `.archive/staging/agents/`, etc.
2. Padroniza frontmatter e formatação
3. Move para destinos finais (`skills/`, `agents/`, `workflows/`, `hooks/`)
4. Gera log em `.docs/batch-processing-log.json`
5. **NÃO deleta** staging (aguarda verificação)

**Script**: `scripts/process-all-staging.py`

**Exemplo**:
```bash
python3 skills/ovp-extract-assets/scripts/process-all-staging.py --batch all
```

---

### **Modo 2: `github-mine`** (Mineração de GitHub)

**Quando usar**: Quer extrair skills de repositórios GitHub diretamente.

**Gatilhos**:
- "Extraia skills deste repo: https://github.com/user/repo"
- "Clone e processe estes repositórios"
- `/ovp-extract-assets --github <urls>`

**O que faz**:
1. Clone shallow dos repositórios (apenas último commit)
2. Detecta tipo (direct skills vs awesome list)
3. Extrai para `.archive/staging/`
4. Executa Modo 1 automaticamente
5. Cleanup dos clones

**Script**: `scripts/clone-github-repos.py` + `scripts/process-all-staging.py`

**Exemplo**:
```bash
# URLs diretas
python3 skills/ovp-extract-assets/scripts/clone-github-repos.py \
  https://github.com/user/repo1 \
  https://github.com/user/repo2

# De arquivo
python3 skills/ovp-extract-assets/scripts/clone-github-repos.py --file repos.txt
```

---

### **Modo 3: `audit-and-migrate`** (Auditoria & Migração de Assets)

**Quando usar**: Quer auditar skills processados e migrar assets auxiliares (scripts/, references/).

**Gatilhos**:
- "Audite as skills e migre scripts e referências"
- "Quais skills têm assets auxiliares?"
- `/ovp-extract-assets --audit`

**O que faz**:
1. Lê `.docs/batch-processing-log.json` para skills processados
2. Rastreia origens via manifest.json
3. Identifica skills com scripts/, references/ na origem
4. Migra assets para `skills/<name>/scripts/` e `skills/<name>/references/`
5. Gera relatório em `.docs/skill-origins-report.json`

**Scripts**:
- `scripts/skill-origins-tracker.py` (identifica assets)
- `scripts/migrate-auxiliary-assets.py` (migra assets)

**Exemplo**:
```bash
# Auditoria completa
python3 skills/ovp-extract-assets/scripts/skill-origins-tracker.py

# Migração após auditoria
python3 skills/ovp-extract-assets/scripts/migrate-auxiliary-assets.py
```

---

### **Modo 4: `full-pipeline`** (Pipeline Completo)

**Quando usar**: Quer fazer TUDO de uma vez: GitHub → Staging → Process → Audit → Migrate → Cleanup.

**Gatilhos**:
- "Faça o pipeline completo deste repo"
- "Extraia, processe, audite e limpe"
- `/ovp-extract-assets --full <urls>`

**O que faz**:
1. **Fase 0**: Setup & Discovery
2. **Fase 1**: Clone GitHub → Staging (Modo 2)
3. **Fase 2**: Process & Standardize (Modo 1)
4. **Fase 3**: Audit & Migrate Assets (Modo 3)
5. **Fase 4**: Verificação (sample 10%)
6. **Fase 5**: Cleanup Staging

**Scripts**: Todos os scripts em sequência

**Exemplo**:
```bash
# Pipeline completo
python3 skills/ovp-extract-assets/scripts/clone-github-repos.py <urls>
python3 skills/ovp-extract-assets/scripts/process-all-staging.py --batch all
python3 skills/ovp-extract-assets/scripts/skill-origins-tracker.py
python3 skills/ovp-extract-assets/scripts/migrate-auxiliary-assets.py
python3 skills/ovp-extract-assets/scripts/mass-cleanup-staging.py
```

---

## 📋 Workflow Típico

### **Cenário A: Batch do Staging (Mais Comum)**

```bash
# 1. Processar batch
python3 skills/ovp-extract-assets/scripts/process-all-staging.py --batch all

# 2. (Opcional) Auditar assets
python3 skills/ovp-extract-assets/scripts/skill-origins-tracker.py

# 3. (Opcional) Migrar assets auxiliares
python3 skills/ovp-extract-assets/scripts/migrate-auxiliary-assets.py

# 4. Verificar sample manualmente (10%)
# 5. Se OK, limpar staging
python3 skills/ovp-extract-assets/scripts/mass-cleanup-staging.py
```

### **Cenário B: GitHub Direto**

```bash
# 1. Clone e extraia
python3 skills/ovp-extract-assets/scripts/clone-github-repos.py https://github.com/user/repo

# 2. Processar
python3 skills/ovp-extract-assets/scripts/process-all-staging.py --batch all

# 3. Auditar e migrar
python3 skills/ovp-extract-assets/scripts/skill-origins-tracker.py
python3 skills/ovp-extract-assets/scripts/migrate-auxiliary-assets.py

# 4. Limpar
python3 skills/ovp-extract-assets/scripts/mass-cleanup-staging.py
```

### **Cenário C: Só Auditoria**

```bash
# Só identificar assets, sem migrar
python3 skills/ovp-extract-assets/scripts/skill-origins-tracker.py

# Review do relatório em .docs/skill-origins-report.json
# Decidir se migra ou não
```

---

## 🔧 Scripts Disponíveis

| Script | Função | Modo |
|--------|--------|------|
| `process-all-staging.py` | Processa staging → skills/agents/etc | 1 |
| `migrate-staging-assets.py` | Migra agents/workflows/hooks | 1 |
| `clone-github-repos.py` | Clone GitHub → staging | 2 |
| `skill-origins-tracker.py` | Auditoria de origem | 3 |
| `migrate-auxiliary-assets.py` | Migra scripts/refs | 3 |
| `mass-cleanup-staging.py` | Limpeza segura | 4 |

---

## 📊 Logs Gerados

| Log | Localização | Conteúdo |
|-----|-------------|----------|
| `batch-processing-log.json` | `.docs/` | Skills processados, status, origens |
| `staging-assets-audit.json` | `.docs/` | Agents/workflows/hooks migrados |
| `skill-origins-report.json` | `.docs/` | Origens e assets auxiliares |
| `auxiliary-assets-migration-log.json` | `.docs/` | Assets migrados |
| `mass-cleanup-log.json` | `.docs/` | Cleanup do staging |

---

## ⚠️ Importante

1. **Sempre verifique sample 10%** antes de cleanup
2. **NÃO delete staging** até verificação completa
3. **Assets auxiliares** são identificados mas NÃO migrados automaticamente (requer confirmação)
4. **GitHub clones** são deletados automaticamente após extração

---

## 📚 Referências

- `references/extraction-modes.md` - Guia detalhado dos modos
- `references/known-repos.md` - Repositórios GitHub conhecidos
- `references/migration-checklist.md` - Checklist de migração

---

## 🚀 Exemplos de Uso

### Exemplo 1: Processar Batch Específico
```bash
python3 skills/ovp-extract-assets/scripts/process-all-staging.py --batch 037
```

### Exemplo 2: Múltiplos Repos GitHub
```bash
python3 skills/ovp-extract-assets/scripts/clone-github-repos.py \
  https://github.com/openclawskills/skills \
  https://github.com/user/awesome-agents \
  https://github.com/org/workflows
```

### Exemplo 3: Auditoria Completa
```bash
# 1. Identificar assets
python3 skills/ovp-extract-assets/scripts/skill-origins-tracker.py

# 2. Review do relatório
cat .docs/skill-origins-report.json | jq '.recommendations.summary'

# 3. Migrar se aprovado
python3 skills/ovp-extract-assets/scripts/migrate-auxiliary-assets.py
```

### Exemplo 4: Pipeline Completo (One-Liner)
```bash
# GitHub → Staging → Process → Audit → Migrate → Cleanup
python3 skills/ovp-extract-assets/scripts/clone-github-repos.py <url> && \
python3 skills/ovp-extract-assets/scripts/process-all-staging.py --batch all && \
python3 skills/ovp-extract-assets/scripts/skill-origins-tracker.py && \
python3 skills/ovp-extract-assets/scripts/migrate-auxiliary-assets.py && \
python3 skills/ovp-extract-assets/scripts/mass-cleanup-staging.py
```

---

*Skill unificada para extração em massa - Versão 2.0*
