---
name: ovp-rename-convention
description: "Renomeação em massa de skills com taxonomia L1-L2-L3 baseada em análise semântica, floors/ceils absolutos e chunking automático. Implementa fórmula sqrt(N) e validação em 2 camadas."
metadata:
  openclaw:
    category: "automation"
    tags: ['automation', 'taxonomy', 'rename', 'organization', 'naming-convention']
    version: "1.0.0"
    scripts:
      - scripts/analyze-taxonomy.py
      - scripts/generate-taxonomy.py
      - scripts/rename-by-convention.py
      - scripts/validate-taxonomy.py
---

# /ovp-rename-convention (Taxonomy-Based Mass Rename)

**Skill para reorganização semântica de skills** - Implementa taxonomia L1-L2-L3 com bases matemáticas (sqrt(N)), floors/ceils absolutos, e chunking automático.

---

## 🎯 4 Scripts (Pipeline Completo)

### **Script 1: `analyze-taxonomy.py`**

**Objetivo**: Analisar taxonomia atual e identificar problemas.

**O que faz**:
- Parse de nomes no formato `L1-L2-L3-nnnn-name`
- Conta distribuição por L1 (type), L2 (subtype), L3
- Valida contra floors/ceils absolutos
- Identifica chunking necessário (>150 skills/L3)

**Comando**:
```bash
python3 skills/ovp-rename-convention/scripts/analyze-taxonomy.py
```

**Output**: `.docs/taxonomy-analysis-report.json`

---

### **Script 2: `generate-taxonomy.py`**

**Objetivo**: Gerar nova taxonomia baseada em análise semântica.

**Fórmulas**:
```python
# Número ideal de tipos (L1)
ideal_types = sqrt(N) / 2  # Ex: sqrt(1300)/2 ≈ 18

# Número ideal de chunks
k = ceil(N / max_chunk)  # max_chunk=150
```

**Floors/Ceils**:
```python
MIN_TYPES = 10
MAX_TYPES = 20
MIN_SKILLS_PER_TYPE = 50
MAX_SKILLS_PER_TYPE = 500
MIN_SKILLS_PER_SUBTYPE = 5
MAX_SKILLS_PER_SUBTYPE = 80  # 2.5× média
MAX_CHUNK_SIZE = 150
```

**Comando**:
```bash
python3 skills/ovp-rename-convention/scripts/generate-taxonomy.py --levels 3
```

**Output**: `.docs/taxonomy-mapping.json`

---

### **Script 3: `rename-by-convention.py`**

**Objetivo**: Aplicar renomeação em massa.

**Modos**:
- `--mode dry-run`: Preview (não renomeia)
- `--mode apply`: Renomeia fisicamente
- `--mode interactive`: Pede confirmação por skill

**Comando**:
```bash
# Preview
python3 skills/ovp-rename-convention/scripts/rename-by-convention.py --mode dry-run

# Aplicar
python3 skills/ovp-rename-convention/scripts/rename-by-convention.py --mode apply
```

---

### **Script 4: `validate-taxonomy.py`**

**Objetivo**: Validar taxonomia após renomeação.

**Validações**:
1. Floors/Ceils absolutos (hard)
2. Filtro percentual 20% (soft)
3. Chunk sizes

**Comando**:
```bash
python3 skills/ovp-rename-convention/scripts/validate-taxonomy.py
```

---

## 📋 Workflow Típico

```bash
# 1. Analisar taxonomia atual
python3 skills/ovp-rename-convention/scripts/analyze-taxonomy.py

# Output esperado:
# 🔴 CRITICAL: ai: 1283 skills > 500 (precisa split)
# 🔴 CRITICAL: misc: 17 skills < 50 (precisa merge)

# 2. Gerar nova taxonomia
python3 skills/ovp-rename-convention/scripts/generate-taxonomy.py --levels 3

# Output: .docs/taxonomy-mapping.json
# Ex: ai-llm-chat-assistant → agent-memory-0001-chat-assistant

# 3. Preview (dry-run)
python3 skills/ovp-rename-convention/scripts/rename-by-convention.py --mode dry-run

# 4. Aplicar renomeação
python3 skills/ovp-rename-convention/scripts/rename-by-convention.py --mode apply

# 5. Validar
python3 skills/ovp-rename-convention/scripts/validate-taxonomy.py

# Output esperado:
# ✅ VALID (0 critical issues)
```

---

## 📊 Naming Convention

### **Formato: 3 Níveis**

```
L1-L2-L3-nnnn-skill-name/
├── SKILL.md
├── scripts/
└── references/
```

**Exemplos**:
```
agent-memory-0001-chat-assistant/
agent-orchestration-0002-researcher/
tools-search-0003-web-crawler/
workflows-ci-cd-0004-deploy-pipeline/
```

### **Formato: 2 Níveis** (fallback)

```
L1-L2-nnnn-skill-name/
```

**Exemplos**:
```
ai-llm-0001-chat-assistant/
dev-backend-0002-api-builder/
```

---

## 🧮 Matemática da Taxonomia

### **Fórmula sqrt(N)**

Para N skills:
```
tipos_ideais = sqrt(N) / 2
subtipos_por_tipo = sqrt(N / tipos_ideais)
```

**Exemplos**:
| N | Tipos Ideais | Subtipos/Tipo | Skills/L3 |
|---|--------------|---------------|-----------|
| 600 | 12 | 7 | 71 |
| 1300 | 18 | 8 | 90 |
| 3000 | 27 | 11 | 100 |

### **Chunking Automático**

Se L3 tem >150 skills:
```python
k = ceil(count / 150)
# Ex: 450 skills → k=3 chunks (150 cada)
```

---

## ⚠️ Validação em 2 Camadas

### **Camada 1: Floors/Ceils Absolutos**

```python
if skills_per_type < 50 or skills_per_type > 500:
    reject()  # CRITICAL
if skills_per_subtype < 5 or skills_per_subtype > 80:
    reject()  # CRITICAL
```

### **Camada 2: Filtro Percentual**

```python
if skills_per_type < media * 0.8:
    consider_merge()  # WARNING
if skills_per_type > media * 1.2:
    consider_split()  # WARNING
```

---

## 📚 References

- `references/taxonomy-rules.md` - Regras matemáticas detalhadas
- `references/l1-l2-categories.md` - Categorias válidas

---

## 🔧 Exemplos Avançados

### **Exemplo 1: LLM-Based Inference**

```bash
# Usa LLM para inferir L1-L2 (requer API key)
python3 skills/ovp-rename-convention/scripts/generate-taxonomy.py \
  --levels 3 \
  --use-llm
```

### **Exemplo 2: Interactive Mode**

```bash
# Confirma cada rename manualmente
python3 skills/ovp-rename-convention/scripts/rename-by-convention.py \
  --mode interactive
```

### **Exemplo 3: Custom Constraints**

Editar script e modificar:
```python
TAXONOMY_CONSTRAINTS = {
    'MIN_TYPES': 12,  # Custom
    'MAX_TYPES': 18,
    'MAX_CHUNK_SIZE': 120,  # Mais conservador
}
```

---

*Skill de Renomeação por Taxonomia - Versão 1.0*
