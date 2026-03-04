# Regras de Operação do Jules (Orquestração de Agentes)
Este documento define as regras fundamentais e boas práticas para delegar tarefas e operar agentes Jules no repositório.

## 🔴 1. A REGRA DE OURO: Anti-Git nos Prompts

> **ESTA É A REGRA MAIS IMPORTANTE. VIOLÁ-LA CAUSA PRs VAZIOS (+0/-0).**

- **NUNCA** mencione `git`, `commit`, `push`, `branch`, `checkout`, `merge` ou qualquer instrução de controle de versão nos prompts enviados ao Jules.
- **NEM MESMO INSTRUÇÕES NEGATIVAS** como "não use git" — qualquer referência a git, mesmo negada, faz o agente tentar manipular branches internamente.
- **O Problema**: A sandbox do Jules restringe `git push`. Se ele "comitar" internamente, a Submit Tool nativa vê que não há uncommitted changes e cria um PR vazio (+0/-0).
- **A Solução**: Abolir 100% das referências a git nos prompts. O Jules deve usar suas ferramentas internas e o fluxo natural de devolução (onde a plataforma cria a branch e faz o PR por ele).

## 2. Disparo de Agentes (Mandatório)
- **Sempre use `jules remote new`**: NUNCA use o comando local `jules new`. Você DEVE usar `jules remote new` para garantir que as sessões fiquem visíveis na UI da plataforma. Sessões locais deixam o usuário cego na UI.
- **Sempre via Wrapper**: Nunca chame `jules remote new` diretamente. Use SEMPRE o script `skills/jules-dispatch-login/scripts/jules-launcher.sh`.
  - O script lança **2 sessões paralelas idênticas** para cada task (redundância contra alucinações).
  - Hard Limit: 15 sessões ativas (100/dia) por conta free/pro. Como duplicamos = máximo **7 tarefas por vez** (14 jobs).

## 3. Rotação de Contas (Quota)
- A cada **7 tarefas disparadas** (14 jobs), o supervisor (`jules-orchestrator`) DEVE pausar e comandar que o usuário execute `jules login` para rotacionar a conta Google autenticada.
- O skill `jules-dispatch-login` gerencia a autenticação e tracking de quota.

## 4. Branch Target (Limitação da Plataforma)
- **A Limitação**: O comando `jules remote new` via terminal NÃO suporta escolher a branch alvo do Pull Request. Ele sempre atira para a branch definida como Default no repositório remoto.
- **O Workaround**: Uma única vez, entrar na interface Web do Jules, mudar a branch pelo dropdown para `staging`, e lançar uma task simbólica. O sistema grava `staging` como Default Branch e todas as futuras invocações CLI cairão em `staging`.
- **Branches Base**: `main`, `staging`, `backup`, `development-*`.

## 5. Fallback: Recuperação de PRs Vazios
Se o Jules enviar um PR vazio (+0/-0), o trabalho NÃO está perdido:
1. Capturar o `SESSION_ID` gravado automaticamente pelo script launcher
2. Backup de segurança local: `jj commit -m "backup: pre-jules-pull"`
3. Puxar o código gerado e aplicar: `jules remote pull --session <SESSION_ID> --apply`
4. Verificar diff, resolver conflitos se houver, e comitar via `jj`

## 6. Nomenclatura e Diretórios
- **Diretório Operacional (`.agents/`)**: Prompts, relatórios e configurações vão em `.agents/`. Scripts de launch vão em `skills/jules-dispatch-login/scripts/`.
- **Salvamento de Relatórios**: Jules salva relatórios em `.agents/reports/`.
- **Nomenclatura Segura (HEX Tag)**: Formato `agent-task_nome-hex.md`. **NUNCA** datas/horas no nome (LLMs alucinam anos como "2024"). Use hash hex de 4 dígitos ou ID da task.

## 7. O Tabu da Tasklist (Prevenção de Conflicts)
- O Jules é **estritamente proibido** de marcar tarefas como completas (`[x]`) no indexador global `docs/tasklist.md`. Múltiplos agentes concorrentes causam merge conflicts.
- Ele apenas marca checkboxes internos dentro do arquivo de task correspondente (ex: `docs/tasks/123-nome-da-task.md`).
- O arquivamento de tarefas e atualização da Master Tasklist ficam a cargo do usuário humano ou script orquestrador isolado.

## 8. Ciclo de Vida de Planejamento (Discovery)
- **Epics e Scavenging**: Ideias de refatoração, propostas ou auditorias NÃO geram código. Elas criam "Proposals/Epics" em `docs/tasks/planning/`.
- Somente quando o Tech Lead ou `TaskMaster` aprovarem a proposta e transformarem em tarefa concreta com Exit Conditions claras em `docs/tasks/`, a execução inicia.

## 9. Sincronização de Conhecimento
- Após qualquer branch significativa fundida, promover Sincronização de Conhecimento consolidando memórias para impedir degradação de contexto nos agentes subsequentes.
