# 01 - awesome-claude-code

> Análise por subagent via `opencode run`

## Repositório: awesome-claude-code

```
/home/sephiroth/.config/opencode/archive/awesome-claude-code/
├── .claude/commands/
│   └── evaluate-repository.md       # 1 comando
├── scripts/                          # 43 scripts Python
│   ├── badges/                       # Geração de badges
│   ├── categories/                   # Gerenciamento de categorias
│   ├── graphics/                     # Geração de SVGs/logos
│   ├── ids/                          # Geração de IDs únicos
│   ├── maintenance/                  # Health check e atualizações
│   ├── readme/                       # Geração multi-formato de READMEs
│   ├── resources/                    # Gerenciamento de recursos/PRs
│   ├── ticker/                       # Geração de ticker SVG
│   ├── utils/                        # Git/GitHub utilities
│   └── validation/                   # Validação de links/recursos
├── docs/                             # Documentação de processos
└── resources/claude.md-files/        # Exemplos de CLAUDE.md
```

## Novos Assets Recomendados

| Tipo | Nome | Descrição | Prioridade |
|------|------|-----------|------------|
| **Comando** | `evaluate-repository` | Sistema completo de avaliação de segurança para repos Claude Code (scores, checklists, red flags) | ⭐⭐⭐ ALTA |
| **Script** | `check_repo_health.py` | Health check de repositórios (útil para manutenção) | ⭐⭐ MÉDIA |
| **Script** | `generate_readme.py` | Sistema multi-formato para READMEs (awesome, flat, minimal, visual) | ⭐⭐ MÉDIA |
| **Script** | `validate_links.py` | Validação automática de links em docs | ⭐ BAIXA |
| **Script** | `generate_resource_id.py` | Geração de IDs únicos baseados em repo/nome | ⭐ BAIXA |
| **Workflow** | Processo de curadoria | Templates para submissão/avaliação de recursos community | ⭐⭐ MÉDIA |

## Recomendação Final

**Priorizar**: O comando `evaluate-repository` é ÚNICO e complementa perfeitamente nosso kit de segurança. Os scripts de README podem ser úteis se criarmos documentação multi-formato. O resto é específico para curadoria "awesome-list" style (não essencial para nós).
