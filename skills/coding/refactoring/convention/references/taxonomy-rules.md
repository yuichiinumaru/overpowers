# Taxonomy Rules

Regras matemáticas e constraints para design de taxonomia.

---

## 📐 Fórmulas Fundamentais

### **1. Número Ideal de Tipos (L1)**

```python
import math

def ideal_num_types(n: int) -> int:
    """
    Calcula número ideal de tipos baseado em sqrt(N).
    
    Para N=1300 skills:
    sqrt(1300) ≈ 36
    36 / 2 = 18 tipos
    """
    return max(10, min(20, int(math.sqrt(n) / 2)))
```

**Exemplos**:
| N (skills) | sqrt(N) | Tipos Ideais |
|------------|---------|--------------|
| 600 | 24.5 | 12 |
| 1300 | 36.1 | 18 |
| 3000 | 54.8 | 27 → 20 (max) |
| 5000 | 70.7 | 35 → 20 (max) |

---

### **2. Número Ideal de Subtipos (L2)**

```python
def ideal_num_subtypes(n: int, num_types: int) -> int:
    """
    Calcula número ideal de subtipos por tipo.
    
    Para N=1300, 18 tipos:
    1300 / 18 ≈ 72 skills/tipo
    sqrt(72) ≈ 8-9 subtipos
    """
    skills_per_type = n / num_types
    return max(4, min(20, int(math.sqrt(skills_per_type))))
```

---

### **3. Chunking Automático (L3)**

```python
def optimal_k(n: int, max_chunk: int = 150, min_chunk: int = 40) -> int:
    """
    Calcula número de chunks necessário.
    
    Regra: k > 2 sempre que N > 300
    """
    if n <= max_chunk:
        return 1
    
    k = math.ceil(n / max_chunk)
    avg = n / k
    
    # Consolida se chunks muito pequenos
    while avg < min_chunk and k > 1:
        k -= 1
        avg = n / k
    
    return k
```

**Exemplos**:
| N | max_chunk | k | avg_chunk |
|---|-----------|---|-----------|
| 60 | 150 | 1 | 60 |
| 200 | 150 | 2 | 100 |
| 450 | 150 | 3 | 150 |
| 1300 | 150 | 9 | 144 |

---

## 🚧 Floors/Ceils Absolutos

### **Hard Constraints (Rejeição Automática)**

```python
TAXONOMY_CONSTRAINTS = {
    # Níveis
    'MIN_TYPES': 10,           # Floor absoluto
    'MAX_TYPES': 20,           # Ceiling absoluto
    
    # Skills por tipo
    'MIN_SKILLS_PER_TYPE': 50,   # Floor absoluto
    'MAX_SKILLS_PER_TYPE': 500,  # Ceiling absoluto
    
    # Subtipos por tipo
    'MIN_SUBTYPES_PER_TYPE': 4,
    'MAX_SUBTYPES_PER_TYPE': 20,
    
    # Skills por subtipo
    'MIN_SKILLS_PER_SUBTYPE': 5,
    'MAX_SKILLS_PER_SUBTYPE': 80,  # 2.5× média
    
    # Chunk size
    'MAX_CHUNK_SIZE': 150,
    'MIN_CHUNK_SIZE': 40,
}
```

### **Validação em 2 Camadas**

```python
def validate_taxonomy(distribution: Dict) -> List[Issue]:
    issues = []
    
    # CAMADA 1: Floors/Ceils absolutos (HARD)
    if num_types < MIN_TYPES:
        issues.append(Issue('CRITICAL', 'Muito poucos tipos'))
    if num_types > MAX_TYPES:
        issues.append(Issue('WARNING', 'Muitos tipos'))
    
    for type_name, skills in distribution.items():
        if len(skills) < MIN_SKILLS_PER_TYPE:
            issues.append(Issue('CRITICAL', f'{type_name}: muito poucas skills'))
        if len(skills) > MAX_SKILLS_PER_TYPE:
            issues.append(Issue('CRITICAL', f'{type_name}: muitas skills'))
    
    # CAMADA 2: Filtro percentual (SOFT)
    media = total_skills / num_types
    
    for type_name, skills in distribution.items():
        if len(skills) < media * 0.8:
            issues.append(Issue('WARNING', f'{type_name}: abaixo da média'))
        if len(skills) > media * 1.2:
            issues.append(Issue('WARNING', f'{type_name}: acima da média'))
    
    return issues
```

---

## 📊 Entropia e Informação

### **Por que Floors/Ceils Importam**

Dois tipos com 650 e 650 skills passam no filtro de 20%, mas são **inúteis semanticamente**:

```
❌ RUIM (passa no filtro 20%):
- ai: 650 skills
- misc: 650 skills
→ Entropia: 1 bit (binário, sem discriminação)

✅ BOM (18 tipos):
- agent: 72 skills
- tools: 72 skills
- workflows: 72 skills
- ...
→ Entropia: log2(18) ≈ 4.2 bits (muito mais discriminação)
```

### **Entropia por Token**

Nome: `agent-memory-0001-chat-assistant`

| Token | Informação | Bits |
|-------|------------|------|
| `agent` | L1: categoria top-level | log2(18) ≈ 4.2 |
| `memory` | L2: subcategoria | log2(8) ≈ 3.0 |
| `0001` | ID: identificador único | log2(150) ≈ 7.2 |
| `chat-assistant` | Nome: descrição | Variável |

**Total**: ~14.4 bits de informação semântica antes do nome descritivo.

---

## 🔄 Reorganização Dinâmica

### **Quando Reorganizar**

```python
def should_reorganize(distribution: Dict) -> bool:
    # 1. Floors/Ceils violados
    if any(count < 50 or count > 500 for count in distribution.values()):
        return True
    
    # 2. Desequilíbrio > 40%
    counts = list(distribution.values())
    media = sum(counts) / len(counts)
    if max(counts) > media * 1.4 or min(counts) < media * 0.6:
        return True
    
    # 3. Crescimento > 50% desde última org
    if total_skills > last_reorg_count * 1.5:
        return True
    
    return False
```

### **Frequência Sugerida**

| N Skills | Frequência | Gatilho |
|----------|------------|---------|
| <500 | Anual | Crescimento >50% |
| 500-1500 | Semestral | Desequilíbrio >40% |
| 1500-5000 | Trimestral | Violação floors/ceils |
| >5000 | Mensal | Auto-organização contínua |

---

## 📚 Referências Acadêmicas

1. **Miller, G.A. (1956)**. "The Magical Number Seven, Plus or Minus Two"
   - Humanos discriminam 7±2 categorias por nível

2. **Hearst, M. (2000)**. "Hierarchical Document Categorization"
   - sqrt(N) como heurística para número de categorias

3. **SKOS (Simple Knowledge Organization System)**
   - Padrão W3C para taxonomias de conhecimento

4. **Information-Theoretic Taxonomy Design**
   - Maximização de entropia por label

---

*Regras de Taxonomia - Versão 1.0*
