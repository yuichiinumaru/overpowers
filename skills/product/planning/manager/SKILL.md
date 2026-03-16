---
name: cfa-task-manager
description: Skill para criação e gestão de tarefas estruturadas (Macros e Micros) seguindo o padrão CFA.
---

# Skill: CFA Task Manager

Esta habilidade é ativada quando o assistente percebe a necessidade de iniciar um novo fluxo de trabalho complexo, delegar tarefas a subagentes ou quando o usuário solicita uma organização de progresso.

## Regras de Ouro
1. **Macro primeiro:** Toda grande meta deve constar no `docs/tasklist.md`.
2. **Detalhe sempre:** Toda tarefa que gere alteração de código deve ter um arquivo correspondente em `docs/tasks/`.
3. **Template Rigoroso:** Use sempre o template definido em `docs/tasks/_task_template.md` (ou o padrão de cabeçalho abaixo).

## Como criar uma Macro-task
Adicione ao `docs/tasklist.md`:
```markdown
- [ ] [ID-TASK] Nome da Tarefa (Responsável: @agente)
```

## Como criar uma Detailed Task (Micro)
Crie o arquivo `docs/tasks/[id-task]-[contexto].md`:
- **Título**: Descrição curta.
- **Contexto**: Por que estamos fazendo isso?
- **Passos**: Lista de check.
- **Condições de Saída**: O que prova que a tarefa acabou? (Ex: Testes passando, Arq. X deletado).

## Gatilhos
- "Organize o que vamos fazer a seguir."
- "Crie uma tarefa para o subagente integrar o login."
- "Como está o progresso do projeto?"

---
**Dica:** Ao criar uma tarefa para o Jules (Cli), referencie explicitamente o `docs/branch-integration-guide.md` como primeira instrução.
