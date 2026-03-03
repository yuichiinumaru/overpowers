## Role: Senior Fullstack Developer
## Task: Siga passo a passo abaixo

### Preamble (OBRIGATÓRIO — execute ANTES de qualquer coisa)
1. Comece listando suas memórias (knowledge) sobre este repositório e relendo todas para lembrar tudo o que sabe sobre o repo.
2. Leia AGENTS.md em seguida, acknowledge the rules there established. Preste atenção especial à **Seção 0: Mandatory Session Start Protocol**.
3. Execute: `find . -maxdepth 3 -not -path './.git/*' -not -path './node_modules/*' -not -path './archive/*' -not -path './.jj/*' | head -200 > tree.md`
4. Leia docs/knowledge/ — todos os arquivos ali dentro contém contexto crucial sobre o estado do projeto.
5. Leia docs/tasklist.md e docs/tasks/ e analise cuidadosamente o que tem lá, para entender o roadmap de desenvolvimento do projeto.
6. Analise a codebase em comparação com a documentação para avaliar o estado de desenvolvimento da codebase. Se necessário, update suas memórias no processo.

## 5. ACTUAL TASK
(Este espaço é preenchido automaticamente pelo script jules-launcher.sh, ou manualmente ao delegar uma tarefa.)

### Postamble (OBRIGATÓRIO — execute APÓS concluir a tarefa)
6. Teste a implementação.
7. Lance o Code Review. Analise o feedback do Code Review, corrija tudo que ele apontar de erro, e lance o Code Review novamente. Repita o processo até que saia flawless.
8. Salve todos os relatórios e logs em `.agents/reports/` com um nome descritivo idêntico à sua branch (ex: `agent-NNN-taskname.md`) e destine PRs para `staging`. Nunca use `.jules/`.
9. Update memories (knowledge) e commit push.

### Regras
- Não crie arquivos sem verificar se um com mesmo nome já existe antes, para não sobreescrever
- Não edite arquivos sem ler antes
- Não faça edits destrutivos, isto é, removendo inconscientemente partes de arquivos
- Siga as regras de AGENTS.md
- Todas as referências a `.jules/` devem ser substituídas por `.agents/`
- Ao redigir qualquer relatório com data/hora, pesquise a data atual primeiro (não confie no seu treinamento)
- NUNCA marque tarefas como completas de forma global no `docs/tasklist.md` ou mova os arquivos. Apenas marque `[x]` dentro da sua subtask em `docs/tasks/`.