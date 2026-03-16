---
description: Pipeline completo de extração em massa de assets (skills, agents, workflows, hooks) de múltiplas origens (GitHub, staging, local) com processamento, auditoria, migração de assets auxiliares e cleanup.
argument-hint: URLs de repositórios GitHub, task file, ou flags (--staging, --github, --full, --audit)
---

# /ovp-batch-assets-extraction (Pipeline Completo)

**Goal**: Extrair, processar, auditar e integrar assets (skills, agents, workflows, hooks) de múltiplas origens em um pipeline unificado de 5 fases.

---

## 📋 Fases do Pipeline

### **FASE 0: Setup & Discovery**

**Objetivo**: Entender origem, tipos e volume dos assets.

**Ações**:
1. **Detectar Origem**:
   - URLs GitHub fornecidas? → Modo GitHub
   - Task file especificado? → Modo Staging
   - Arquivos em `.archive/staging/`? → Modo Staging
   - Nenhum dos acima? → Perguntar usuário

2. **Detectar Tipos**:
   - Skills (`.archive/staging/skills/*.md` ou `skills/` no repo)
   - Agents (`.archive/staging/agents/*.md` ou `agents/` no repo)
   - Workflows (`.archive/staging/workflows/*.md` ou `workflows/` no repo)
   - Hooks (`.archive/staging/hooks/*.md` ou `hooks/` no repo)

3. **Estimar Volume**:
   - Contar arquivos em cada categoria
   - Reportar ao usuário: "Detectei X skills, Y agents, Z workflows, W hooks"

4. **Confirmar Escopo**:
   - "Processo tudo agora ou quer auditar primeiro?"
   - Opções: Full Pipeline, Process Only, Audit Only

---

### **FASE 1: Aquisição (Opcional, se origem = GitHub)**

**Objetivo**: Clonar repositórios e extrair para staging.

**Ações**:
1. **Clone Shallow** (apenas último commit):
   ```bash
   python3 skills/data/etl/assets/scripts/clone-github-repos.py <urls>
   ```

2. **Detectar Estrutura**:
   - Direct skills: Repo tem `skills/`, `agents/`, etc.
   - Awesome list: README com links para outros repos

3. **Extrair para Staging**:
   - Copiar arquivos para `.archive/staging/<tipo>/`
   - Prefixar com nome do repo para evitar colisões

4. **Cleanup Clone**:
   - Deletar diretórios temp/ após extração

**Output**: Arquivos em `.archive/staging/` prontos para processamento.

---

### **FASE 2: Processamento em Massa**

**Objetivo**: Padronizar e mover assets para destinos finais.

**Ações**:
1. **Ler Task File** (se aplicável):
   - `.docs/tasks/0500-extraction-skills-batch-*.md`
   - Obter lista de arquivos para processar

2. **Processar Cada Asset**:
   - **Skills**: Gerar frontmatter YAML, mover para `skills/<name>/SKILL.md`
   - **Agents**: Gerar frontmatter (`name: "ovp-..."`), mover para `agents/ovp-<name>.md`
   - **Workflows**: Gerar header block, mover para `workflows/ovp-<name>.md`
   - **Hooks**: Gerar header block, mover para `hooks/<name>.md`

3. **Padronizar Nomes**:
   - Skills: `<domain>-<subdomain>-<name>`
   - Agents: `ovp-<name>`
   - Workflows: `ovp-<name>`
   - Hooks: `<name>`

4. **Gerar Log**:
   - Salvar em `.docs/batch-processing-log.json`
   - Incluir: nome, batch, status, destination, timestamp

5. **Marcar Task File**:
   - Substituir `[ ]` por `[x]` para cada item processado

**Script**: `python3 skills/data/etl/assets/scripts/process-all-staging.py --batch all`

**Output**: Assets padronizados em `skills/`, `agents/`, `workflows/`, `hooks/`.

---

### **FASE 3: Auditoria & Migração de Assets (Opcional)**

**Objetivo**: Identificar e migrar assets auxiliares (scripts/, references/).

**Ações**:
1. **Auditoria de Origem**:
   ```bash
   python3 skills/data/etl/assets/scripts/skill-origins-tracker.py
   ```
   - Lê `.docs/batch-processing-log.json`
   - Rastreia origens via `.archive/staging/manifest.json`
   - Identifica skills com scripts/, references/ na origem
   - Gera `.docs/skill-origins-report.json`

2. **Gerar Relatório**:
   - High priority: 620 skills com scripts
   - Medium priority: 169 skills com references
   - Low priority: 1102 skills com outros arquivos

3. **Migrar Assets** (após aprovação):
   ```bash
   python3 skills/data/etl/assets/scripts/migrate-auxiliary-assets.py
   ```
   - Copia scripts/ para `skills/<name>/scripts/`
   - Copia references/ para `skills/<name>/references/`
   - Gera `.docs/auxiliary-assets-migration-log.json`

**Output**: Assets auxiliares migrados para pastas das skills.

---

### **FASE 4: Verificação (Obrigatória antes de Cleanup)**

**Objetivo**: Validar qualidade antes de deletar staging.

**Ações**:
1. **Sample 10% Aleatório**:
   - Selecionar 10% dos skills processados
   - Exemplo: 1283 skills → 128 para review

2. **Verificar Cada Sample**:
   - ✅ Frontmatter presente e válido
   - ✅ Description não-vazia
   - ✅ UTF-8 encoding (sem caracteres corrompidos)
   - ✅ Sem links quebrados óbvios

3. **Gerar Relatório de Sample**:
   - PASS: Sem issues
   - WARNING: Issues menores (ex: descrição genérica)
   - FAIL: Issues críticos (ex: encoding corrompido)

4. **Aprovação do Usuário**:
   - Mostrar sample results
   - "Sample: 92% PASS, 8% WARNING, 0% FAIL. Prosseguir com cleanup?"
   - Aguardar confirmação explícita

**Output**: Aprovação (ou não) para cleanup.

---

### **FASE 5: Cleanup (Após Aprovação)**

**Objetivo**: Limpar staging e temp directories.

**Ações**:
1. **Verificar Aprovação**:
   - Confirmar que Fase 4 foi completada
   - Confirmar aprovação do usuário

2. **Cleanup Staging**:
   ```bash
   python3 skills/data/etl/assets/scripts/mass-cleanup-staging.py
   ```
   - Deletar arquivos processados de `.archive/staging/`
   - Preservar duplicados (11 skills que já existiam)
   - Preservar agents/workflows/hooks não processados

3. **Cleanup Temp**:
   - Deletar `temp/` se existir
   - Deletar clones git órfãos

4. **Gerar Log Final**:
   - Salvar em `.docs/mass-cleanup-log.json`
   - Incluir: total deleted, errors, timestamp

**Output**: Staging limpo, apenas assets não processados restantes.

---

## 🎯 Modos de Operação

### **Modo A: Full Pipeline (GitHub → Cleanup)**

```bash
/ovp-batch-assets-extraction --full https://github.com/user/repo1 https://github.com/user/repo2
```

**Executa**: Fases 0 → 1 → 2 → 3 → 4 → 5

**Quando usar**: Repositórios GitHub, quer tudo automático.

---

### **Modo B: Staging Only**

```bash
/ovp-batch-assets-extraction --staging --task 0500-extraction-skills-batch-037.md
```

**Executa**: Fases 0 → 2 → 4 → 5

**Quando usar**: Já tem task file com batch do staging.

---

### **Modo C: Audit Only**

```bash
/ovp-batch-assets-extraction --audit
```

**Executa**: Fase 3 apenas

**Quando usar**: Quer identificar assets antes de migrar.

---

### **Modo D: Interativo**

```bash
/ovp-batch-assets-extraction
```

**Executa**: Agente decide baseado no contexto

**Quando usar**: Não tem certeza do modo, quer que agente analise.

---

## 📊 Exemplo de Execução Completa

```
📋 FASE 0: Setup & Discovery
   Origem: GitHub (2 URLs fornecidas)
   Tipos: Skills, Agents
   Volume estimado: ~500 skills, ~20 agents

📥 FASE 1: Aquisição
   Clonando https://github.com/user/repo1... ✅
   Clonando https://github.com/user/repo2... ✅
   Extraindo para staging... ✅ 523 arquivos
   Cleanup clones... ✅

📝 FASE 2: Processamento
   Processando 523 arquivos...
   ✅ 520 migrados para skills/
   ✅ 3 migrados para agents/
   📝 Log: .docs/batch-processing-log.json

🔍 FASE 3: Auditoria
   Auditando origens...
   📊 487 skills com scripts/
   📊 89 skills com references/
   Migrando assets... ✅ 2341 arquivos
   📝 Log: .docs/auxiliary-assets-migration-log.json

✅ FASE 4: Verificação
   Sample 10%: 52 skills
   ✅ 48 PASS (92%)
   ⚠️  4 WARNING (8%)
   ❌ 0 FAIL (0%)
   
   ⚠️  Aprovação necessária: "Sample OK, prosseguir com cleanup?"
   👤  Usuário: "sim"

🧹 FASE 5: Cleanup
   Limp staging... ✅ 520 arquivos deletados
   📝 Log: .docs/mass-cleanup-log.json

🎉 Pipeline completo! 523 assets integrados.
```

---

## ⚠️ Importante

1. **Fase 4 é obrigatória** antes de cleanup
2. **NÃO delete staging** sem aprovação do usuário
3. **Assets auxiliares** (Fase 3) são opcionais - pular se não necessário
4. **GitHub clones** são deletados automaticamente após Fase 1

---

## 📚 Scripts Utilizados

Todos os scripts estão em `skills/data/etl/assets/scripts/`:

- `clone-github-repos.py` - Fase 1
- `process-all-staging.py` - Fase 2
- `migrate-staging-assets.py` - Fase 2 (agents/workflows/hooks)
- `skill-origins-tracker.py` - Fase 3
- `migrate-auxiliary-assets.py` - Fase 3
- `mass-cleanup-staging.py` - Fase 5

---

*Workflow unificado para extração em massa - Versão 1.0*
