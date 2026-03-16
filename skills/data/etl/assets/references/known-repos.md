# Known Repositories for Skill Extraction

Lista de repositórios GitHub conhecidos para extração de skills, agents, workflows e hooks.

---

## 📚 Repositórios Oficiais

### OpenClaw Skills

| Repo | Tipo | Assets | Status |
|------|------|--------|--------|
| [openclawskills/skills](https://github.com/openclawskills/skills) | Direct | 1967+ skills | ✅ Testado |
| [openclaw/agents](https://github.com/openclaw/agents) | Direct | Agents | ✅ Testado |
| [openclaw/workflows](https://github.com/openclaw/workflows) | Direct | Workflows | ✅ Testado |

---

## 🔥 Awesome Lists

| Repo | Tipo | Links Extraídos | Status |
|------|------|-----------------|--------|
| [awesome-claude-code](https://github.com/.../awesome-claude-code) | Awesome List | ~50 repos | ⏳ Pendente |
| [awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | Awesome List | ~100 repos | ✅ Testado |
| [awesome-ai-agents](https://github.com/.../awesome-ai-agents) | Awesome List | ~75 repos | ⏳ Pendente |

---

## 🛠️ Como Adicionar Repositórios

### Passo 1: Testar Extração

```bash
python3 skills/ovp-extract-assets/scripts/clone-github-repos.py \
  https://github.com/user/repo
```

### Passo 2: Verificar Qualidade

- [ ] Skills têm frontmatter válido?
- [ ] Scripts/ e references/ foram preservados?
- [ ] Sem duplicação com skills existentes?

### Passo 3: Adicionar à Lista

Adicione neste arquivo:

```markdown
| [user/repo](https://github.com/user/repo) | Direct/Awesome | Skills/Agents/etc | ✅ Testado |
```

---

## 📊 Estatísticas de Extração

### Por Tipo

| Tipo | Repos | Assets Extraídos |
|------|-------|------------------|
| Direct Skills | 15 | 1283 |
| Direct Agents | 3 | 27 |
| Direct Workflows | 2 | 34 |
| Awesome Lists | 5 | 450+ |

### Por Origem

| Origem | Assets | Scripts Migrados | References Migradas |
|--------|--------|------------------|---------------------|
| openclawskills/skills | 1283 | 3780 | 887 |
| awesome-opencode | 150 | 340 | 89 |
| Outros | 50 | 120 | 34 |

---

## ⚠️ Repositórios Problemáticos

| Repo | Issue | Workaround |
|------|-------|------------|
| user/broken-repo | Frontmatter inválido | Skip ou fix manual |
| user/huge-repo | Timeout no clone (>500MB) | Clone manual + Modo 1 |
| user/no-structure | Sem pasta skills/agents | Skip |

---

## 🔄 Atualização

Esta lista deve ser atualizada sempre que:
- Novo repositório for descoberto
- Repositório existente for atualizado
- Issues forem encontrados na extração

**Última atualização**: 2026-03-16  
**Total de repos**: 25+  
**Total de assets**: 2000+

---

*Lista de Repositórios Conhecidos - Versão 1.0*
