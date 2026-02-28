# Regras de Operação do Jules (Orquestração de Agentes)
Este documento define as regras fundamentais e boas práticas para delegar tarefas e operar agentes Jules no repositório.

## 1. Disparo de Agentes (Mandatório)
- **Sempre use `jules remote new`**: NUNCA use o comando local `jules new`. Você DEVE usar `jules remote new` para garantir que as sessões fiquem visíveis na UI da plataforma. Sessões locais deixam o usuário cego na UI, impedindo-o de acompanhar o progresso ou debugar por que uma task falhou.

## 2. Nomenclatura e Diretórios
- **Diretório Operacional (`.agents/`)**: Os prompts, scripts de launch e relatórios base devem **sempre** usar a pasta `.agents/` ao invés da legada `.jules/`.
- **Salvamento de Relatórios**: O Jules sempre deve salvar seus relatórios de progresso ou logs em `.agents/reports/`.
- **Nomenclatura Segura (HEX Tag)**: O arquivo de relatório deve seguir o formato `agent-task_nome-hex.md`. **NUNCA** utilize datas/horas no nome do arquivo (como LLMs não têm acesso nativo de relógio a menos que busquem, eles costumam alucinar anos como "2024" corrompendo as timelines). Utilize um hash hexadecimal de 4 dígitos ou o ID da task.

## 3. Isolamento e Pull Requests
- **Staging Base**: O Jules SEMPRE inicia os trabalhos a partir de uma cópia atualizada da branch `staging` e cria sua própria branch de feature isolada (ex: `foreman-077-backend-schema`). 
- **PR Target**: Todos os Pull Requests resultantes da sua atuação são direcionados para `staging`.

## 4. O Tabu da Tasklist (Prevenção de Git Conflicts)
- O Jules é **estritamente proibido** de marcar tarefas como completas (`[x]`) no indexador global `docs/tasklist.md`. Múltiplos agentes operando concorrentemente e alterando a listagem mestre causam merge conflicts inevitáveis e severos.
- O Jules deve apenas marcar os checkboxes internos dentro do seu arquivo MD correspondente (ex: `docs/tasks/123-nome-da-task.md`).
- O arquivamento de tarefas em `completed/` e a atualização da Master Tasklist ficam a encargo do usuário humano, do Tech Lead ou via script orquestrador isolado.

## 5. Ciclo de Vida de Planejamento (Discovery)
- **Epics e Scavenging**: Qualquer ideia de refatoração, propostas trazidas de fora pelo "Scavenger", ou auditorias do "Inspector" não devem gerar código não-solicitado. Eles criam "Proposals/Epics" em `docs/tasks/planning/`.
- Somente quando o Tech Lead ou o `TaskMaster` aprovarem a proposta e transformarem em uma tarefa concreta com *Exit Conditions* muito claras dentro de `docs/tasks/`, a execução deve iniciar.

## 6. Sincronização de Conhecimento
- Após qualquer branch significativa fundida com o repopsitório, promova uma "Sincronização de Conhecimento" via `AgentDB/antigravity` injetando informações ou consolidando memórias para impedir degradação de contexto nos agentes que operarem posteriormente.
