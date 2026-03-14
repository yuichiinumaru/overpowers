<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# [https://ai.gopubby.com/claude-code-setup-skills-hooks-agents-mcp-blueprint-80bdef0c62f6](https://ai.gopubby.com/claude-code-setup-skills-hooks-agents-mcp-blueprint-80bdef0c62f6)

sintetize este artigo e veja se tem algum repo linkado nele. se tiver, analise pfvr

O artigo original não foi acessível diretamente, mas combinando os resultados de busca consegui reconstruir seu conteúdo principal. O título real é **"I Turned Claude Code Into an Operating System — Here's the Blueprint"**, publicado em 2 de março de 2026 no GoPubby. Ele apresenta uma arquitetura de 6 camadas que transforma o Claude Code num OS completo com 32 skills, 17 hooks, agentes e MCP servers sob um modelo de zero-trust security.[^1_1][^1_2]

***

## Arquitetura de 6 Camadas

O blueprint organiza o Claude Code nas seguintes camadas:[^1_3][^1_2]

1. **CLAUDE.md** — o arquivo de roteamento central; define estrutura de projeto, convenções, onde coisas vivem, o que nunca tocar. Não descreve "o que o agente é", mas "como seu mundo funciona"
2. **Skills** — arquivos `.md` em `~/.claude/skills/`. Sem SDK, sem build step: markdown puro com instruções, templates de código, endpoints de API e exemplos. Ativados por nome (`/skill-name`) ou por contexto
3. **Hooks** — shell commands que disparam em eventos específicos (`PreToolUse`, `PostToolUse`, `SubagentStart`, `PreCommit` etc.). Usados para validação, bloqueio de arquivos sensíveis, logging
4. **Subagentes** — o agente principal delega tarefas em paralelo para workers com seus próprios context windows. Ex: agente líder spawna um de segurança, um de arquitetura, um de implementação[^1_4]
5. **MCP Servers** — integração com ferramentas externas (GitHub, DBs, APIs internas) via Model Context Protocol
6. **Zero-Trust Permissions** — cada subagente recebe apenas os tools mínimos necessários (ex: code-reviewer com `Read`, `Grep`, `Glob` mas sem `Write` ou `Edit`)[^1_5]

***

## Repos Relacionados ao Tema

O artigo não linka um repo próprio diretamente, mas o ecossistema descrito está fortemente associado a dois repos relevantes encontrados:[^1_6][^1_7]

### [`disler/claude-code-hooks-multi-agent-observability`](https://github.com/disler/claude-code-hooks-multi-agent-observability)

Implementa exatamente o padrão de hooks descrito no artigo:[^1_6]

- Pipeline: `Claude Agents → Hook Scripts → HTTP POST → Bun Server → SQLite → WebSocket → Vue Client`
- Scripts Python para cada evento: `pre_tool_use.py`, `post_tool_use.py`, `user_prompt_submit.py`, `subagent_stop.py`
- Dashboard em Vue 3 com timeline em tempo real de eventos dos agentes


### [`disler/claude-code-hooks-mastery`](https://github.com/disler/claude-code-hooks-mastery)

Foca em workflows de build/validate com times de agentes especializados orquestrados via task system. Padrão `/plan_w_team` para coordenação multi-agente.[^1_7]

***

## Pontos Chave para um AI Engineer

- **Skills como documentação executável**: um arquivo `.md` de ~200 linhas pode encapsular todo o contexto de um domínio (SQL schema, API endpoints, edge cases) sem nenhuma linha de código[^1_3]
- **Hooks são o sistema nervoso**: interceptam qualquer ação antes/depois de acontecer — equivalente a middleware num servidor, mas para comportamento de agente[^1_8]
- **Zero-trust por design**: limitar tools por subagente reduz surface area de erros e ataques de prompt injection, que o artigo chama de "skeleton key problem"[^1_9]

Tópicos que valem a pena pesquisar a mais para complementar este aprendizado: `Claude Code SDK subagent spawning API`, `MCP server authoring best practices 2026`, `prompt injection defenses in multi-agent systems`.
<span style="display:none">[^1_10][^1_11][^1_12][^1_13][^1_14][^1_15]</span>

<div align="center">⁂</div>

[^1_1]: https://ai.gopubby.com/i-turned-claude-code-into-an-operating-system-heres-the-blueprint-80bdef0c62f6

[^1_2]: https://www.reddit.com/r/ClaudeCode/comments/1rltiv7/inside_a_116configuration_claude_code_setup/

[^1_3]: https://okhlopkov.com/claude-code-setup-mcp-hooks-skills-2026/

[^1_4]: https://www.reddit.com/r/ClaudeAI/comments/1lqn9ie/my_current_claude_code_sub_agents_workflow/

[^1_5]: https://claude.com/blog/skills-explained

[^1_6]: https://github.com/disler/claude-code-hooks-multi-agent-observability

[^1_7]: https://github.com/disler/claude-code-hooks-mastery

[^1_8]: https://code.claude.com/docs/en/hooks

[^1_9]: https://ai.gopubby.com/the-skeleton-key-problem-why-ai-agents-are-the-new-zero-day-risk-f64bae6bdc56

[^1_10]: https://code.claude.com/docs/en/skills

[^1_11]: https://platform.claude.com/cookbook/claude-agent-sdk-02-the-observability-agent

[^1_12]: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

[^1_13]: https://www.youtube.com/watch?v=dZW1uv_KLgM

[^1_14]: https://www.youtube.com/watch?v=Ik-Xbz2hvM0

[^1_15]: https://snyk.io/es/articles/top-claude-skills-developers/


---

# aqui, consegui ripar ele, da uma olhada melhor

Agora sim — artigo completo extraído do PDF. Aqui está a síntese detalhada:

***

## Artigo: "I Turned Claude Code Into an OS"

**Autor:** Delanoe Pirard | Publicado: 3 mar 2026 [^2_1]

O artigo narra como uma alucinação do Claude — que inventou 3 parâmetros inexistentes para `Depends()` do FastAPI causando 40 minutos de trabalho perdido — motivou a criação de uma arquitetura de 6 camadas que torna a alucinação **estruturalmente difícil**, não por confiar mais no modelo, mas por construir infraestrutura determinística ao redor dele.[^2_1]

***

## As 6 Camadas (de baixo pra cima)

```
LAYER 6 → MCP Servers         (drivers periféricos)
LAYER 5 → Security + Hooks    (sistema de permissões)
LAYER 4 → Agents              (processos especializados)
LAYER 3 → Skills              (shared libraries)
LAYER 2 → Memory              (filesystem persistente)
LAYER 1 → CLAUDE.md           (kernel)
```


### Layer 1 — CLAUDE.md como Kernel

Não é um arquivo de preferências — é o kernel que define comportamento padrão de toda sessão. Contém:[^2_1]

- **Protocolo anti-alucinação**: árvore de decisão que força Context7 antes de responder sobre APIs, WebSearch para fatos recentes, `Read` para conteúdo de arquivos
- **4 níveis de confiança**: HIGH (verificado por tool + 2 fontes), MEDIUM (1 fonte), LOW (só memória), UNKNOWN ("não sei") — cada claim técnico exige um nível declarado
- **Regras de `/compact`**: especifica exatamente o que preservar ao comprimir contexto (arquivos modificados, branch, tasks pendentes, decisões arquiteturais)


### Layer 2 — Memória Persistente

Diretório `memory/` com `MEMORY.md` (auto-carregado, max 200 linhas), `patterns.md`, `debugging.md`, `architecture.md`. Só armazena padrões **confirmados** em múltiplas sessões, nunca hipóteses. A distinção com `/compact`: compact é RAM (dentro da sessão), memory é storage (entre sessões).[^2_1]

### Layer 3 — 32 Skills em 10 Categorias

Skills são `.md` com frontmatter YAML em `~/.claude/skills/` — sem SDK, sem build step. Carregamento é **lazy**: só ativa quando a `description` do skill bate com o contexto da conversa (2–4 skills simultâneos tipicamente). Todas seguem o padrão **AAPEV**:[^2_1]


| Fase | Ação |
| :-- | :-- |
| ASSESS | Entender o problema |
| ANALYZE | Pesquisar antes de agir |
| PLAN | Propor um plano |
| EXECUTE | Implementar |
| VALIDATE | Testar o resultado |

A categoria mais densa é **AI/ML com 9 skills**: `nlp-transformers`, `computer-vision`, `mlops-training`, `agentic-ai`, `generative-models`, `reinforcement-learning`, `wandb-experiment`, `jupyter-execution`, `huggingface-workflow`.[^2_1]

### Layer 4 — 10 Agentes Especializados

Agentes têm model próprio (`sonnet` para tasks rotineiras, `opus` para análise complexa), tool whitelist, e color de identificação no terminal. Foram 18 inicialmente — `python-expert`, `typescript-expert` e `frontend-developer` foram **removidos** porque plugins comunitários fazem o mesmo com menos manutenção.[^2_1]

O destaque é o **brainstorm multi-agente**: o orchestrator spawna 4 agentes em paralelo, cada um propõe 2–3 abordagens com trade-offs e nível de confiança, e a síntese identifica consensos e divergências — "deliberação estruturada, não votação".[^2_1]

### Layer 5 — Zero-Trust: 78 Regras + 17 Hooks

**Permissões estáticas** em `settings.json`: 40 allows (`git:*`, `uv:*`, `docker:*`) + 38 denies (`sudo:*`, `chmod 777:*`, `write(~/.ssh/*)`, `write(*secret*)`).[^2_1]

**Hooks por tipo de evento** — os mais críticos:

- `PreToolUse(Bash)` → `bash-guard.sh`: bloqueia `rm -rf /`, fork bombs, `eval`, pipe para bash, escalonamento de privilégio
- `PreToolUse(Write)` → `write-guard.sh`: protege `.env`, `.pem`, `.ssh/`, e escaneia conteúdo com regex para 15+ formatos de secrets (OpenAI `sk-`, AWS `AKIA`, GitHub `ghp_`, JWT, DB URLs com senha)
- `PostToolUse(Write)` → `write-format.sh`: auto-formata com `prettier` (TS/JS) ou `ruff` (Python) — **determinístico, sem consumir tokens**
- `UserPromptSubmit` → `user-prompt-secrets.sh`: escaneia o prompt antes de enviar à API
- `PostToolUseFailure` → loga falhas em `~/.claude/logs/tool-failures.log` com rotação automática em 1MB

**Princípio fail-closed**: se o hook crashar, a resposta padrão é **deny** — nunca allow.[^2_1]

### Layer 6 — 6 MCP Servers

| Server | Função |
| :-- | :-- |
| `context7` | Docs em tempo real (coração do anti-alucinação) |
| `fetch` | Leitura de páginas web em Markdown |
| `git` | Operações avançadas de git |
| `huggingface` | Papers arXiv, modelos, datasets |
| `jupyter` | Execução de notebooks |
| `ide` | Comunicação com Cursor/VS Code |

[^2_1]

***

## O Repo: `Aedelon/claude-code-blueprint`

O artigo linka explicitamente um **companion repo open-source**: **[github.com/Aedelon/claude-code-blueprint](https://github.com/Aedelon/claude-code-blueprint)**. Ele contém:[^2_1]

- `CLAUDE.md` com protocolo anti-alucinação
- 8 skills curadas
- 4 agentes
- 11 hooks (2 sanitizados para remover paths pessoais)
- Template de permissões zero-trust
- Regras path-scoped por linguagem

Vou buscar o repo agora para analisar a estrutura real:

<div align="center">⁂</div>

[^2_1]: 5dd2c76e-6e67-4094-8fcb-bed2365bd397.pdf


---

# beleza! analise esses 2 artigos e compare as abordagens. Veja se consegue pegar inspiração neles para sugerir melhorias ao sistema da Aedelon:

[https://arxiv.org/html/2602.23193v1](https://arxiv.org/html/2602.23193v1)
[https://arxiv.org/html/2511.09030v1](https://arxiv.org/html/2511.09030v1)

Sim — os dois artigos são **bem complementares**, e juntos apontam melhorias importantes para o sistema da Aedelon.  O blueprint da Aedelon já é forte em governança prática no runtime — skills, hooks, agentes, MCP e zero-trust — mas os papers mostram dois upgrades claros: um modelo mais **determinístico** de estado e execução, e um modelo mais **estatístico** de correção de erros em passos críticos.[^3_1][^3_2][^3_3]

## Leitura comparada

O paper **ESAA** propõe separar intenção e efeito: o agente não escreve direto no projeto; ele emite JSON validado, e um orquestrador determinístico valida, registra em log append-only, aplica os efeitos e recompõe o estado por replay com hash de verificação.  O paper **MAKER/MDAP** vai em outra direção: quebrar tarefas em micro-passos, aplicar votação “first-to-ahead-by-k” e descartar respostas com sinais de unreliability, para escalar até tarefas de mais de 1 milhão de passos com zero erro.[^3_2][^3_3]


| Eixo | Aedelon | ESAA | MAKER / MDAP |
| :-- | :-- | :-- | :-- |
| Núcleo da abordagem | Sistema operacional em 6 camadas com kernel, memory, skills, agents, security e MCP. [^3_1] | Sistema orientado a eventos com log imutável, replay e projeção verificável. [^3_3] | Decomposição extrema em microagentes com votação e red-flagging. [^3_2] |
| Como controla erros | Anti-hallucination, hooks, permissões, formatters, scans de segredo. [^3_1] | Contratos formais + validação de schema + replay + hash. [^3_3] | Votação por passo + descarte de respostas suspeitas. [^3_2] |
| Como trata escrita em arquivos | Claude ainda escreve direto, mas sob guards e hooks. [^3_1] | Agente não escreve direto; o orquestrador aplica efeitos autorizados. [^3_3] | Foca mais em decisão correta por passo do que em governança de escrita. [^3_2] |
| Estado de longo prazo | `memory/` e regras em `CLAUDE.md`. [^3_1] | Event store append-only + read model materializado. [^3_3] | Estado mínimo por micro-passo para reduzir degradação de contexto. [^3_2] |
| Multiagente | Especialização por domínio e brainstorm paralelo. [^3_1] | Especialização por task type com serialização por event store. [^3_3] | Micro-roles muito pequenos, não papéis “humanos”. [^3_2] |

## Onde a Aedelon já acerta

A Aedelon já internaliza várias ideias que os papers defendem: contexto enxuto por skill lazy-loaded, isolamento parcial por tool whitelist, defesa em profundidade por permissões + hooks, e memória persistente para evitar perda de contexto entre sessões.  O próprio ecossistema público sugere que isso já foi modularizado em skills distribuíveis, como `anti-hallucination` e `uv-workflow`, publicados como skills instaláveis.[^3_4][^3_5][^3_1]

A diferença é que o blueprint da Aedelon é mais forte em **operação segura no terminal**, enquanto ESAA é mais forte em **auditabilidade e reprodutibilidade**, e MAKER é mais forte em **correção probabilística de erro**.  Em outras palavras: Aedelon reduz erro por políticas e guard rails; ESAA reduz erro por contratos e replay; MAKER reduz erro por decomposição e quorum.[^3_3][^3_1][^3_2]

## Melhorias mais valiosas

1. **Trocar “write guardado” por “patch proposal + orchestrator apply”**. Hoje o sistema da Aedelon permite escrita direta sob hooks e permissões; inspirado em ESAA, o agente deveria propor patches estruturados, e só um orquestrador determinístico aplicar `Write/Edit` após schema validation, boundary checks e hashable audit trail.[^3_1][^3_3]
2. **Adicionar event store append-only do run**. Em vez de depender só de logs de hook e `memory/`, cada sessão relevante poderia gerar `activity.jsonl` com `task.claim`, `agent.result`, `output.rejected`, `file.apply`, `verify.ok` e `run.end`, o que daria replay, diff temporal e forense de decisões.[^3_3][^3_1]
3. **Criar um read-model canônico do projeto**. ESAA mostra valor em derivar um `roadmap.json` ou outro estado materializado a partir dos eventos; para Aedelon, isso poderia virar `state/project-view.json` com tarefas, arquivos tocados, branch, testes, riscos abertos e dependências, reduzindo a dependência de contexto conversacional bruto.[^3_1][^3_3]
4. **Aplicar quorum só em passos de alto risco**. O brainstorm da Aedelon já usa agentes paralelos, mas para ideação; MAKER sugere transformar isso em confiabilidade operacional: migrations, mudanças de auth, edits em config, refactors amplos e decisões arquiteturais poderiam exigir 3 amostras independentes e vitória por margem `k`, não apenas uma resposta boa.[^3_2][^3_1]
5. **Introduzir red-flagging explícito**. O blueprint da Aedelon já bloqueia comandos perigosos e vazamento de segredos, mas não trata resposta prolixa ou malformatada como sinal de baixa confiabilidade; MAKER mostra que comprimento excessivo e formato inválido podem ser usados para descartar amostras antes de virarem ação.[^3_2][^3_1]
6. **Medir confiabilidade por classe de tarefa**. MAKER estima taxa de sucesso por passo e usa isso para calibrar custo e quorum; a Aedelon poderia registrar métricas por skill/agente, como taxa de rollback, taxa de patch rejeitado, taxa de teste quebrado, taxa de reformatação corretiva e taxa de “verification needed”.[^3_1][^3_2]

## Blueprint sugerido para a Aedelon

Minha sugestão é evoluir o sistema para uma arquitetura híbrida: manter o stack atual de **skills + hooks + zero-trust + MCP**, mas adicionar uma camada acima chamada **Execution Ledger**.  Nessa camada, todo trabalho relevante vira: `task selected -> context slice -> agent proposal JSON -> validation -> quorum opcional -> orchestrator apply -> verify -> event persisted`.[^3_3][^3_2][^3_1]

Na prática, isso deixaria a Aedelon com três linhas de defesa: **política** via permissões/hooks, **determinismo** via contratos/event sourcing, e **confiabilidade estatística** via quorum/red-flagging em tarefas críticas.  Isso é especialmente coerente com o posicionamento original do artigo, que já trata Claude Code como plataforma programável e não como chatbot com terminal.[^3_2][^3_3][^3_1]

## Prioridade de implementação

Eu priorizaria assim: primeiro `event store + read model`, depois `JSON output contract para agentes`, depois `orchestrator-only apply`, e só então `quorum seletivo` para operações críticas.  Essa ordem dá o melhor ganho por complexidade, porque ESAA resolve auditabilidade e estado com pouco overhead, enquanto o modelo tipo MAKER custa mais e faz mais sentido apenas onde o erro é caro.[^3_3][^3_2]

Tópicos que valem apena pesquisar a mais para complementar este aprendizado: `event-sourced agent orchestration for codegen`, `quorum-based subagent validation for migrations`, `json-schema contracts for Claude Code agents`
<span style="display:none">[^3_10][^3_11][^3_12][^3_13][^3_14][^3_15][^3_16][^3_17][^3_18][^3_6][^3_7][^3_8][^3_9]</span>

<div align="center">⁂</div>

[^3_1]: 5dd2c76e-6e67-4094-8fcb-bed2365bd397.pdf

[^3_2]: https://ai.gopubby.com/i-turned-claude-code-into-an-operating-system-heres-the-blueprint-80bdef0c62f6

[^3_3]: https://okhlopkov.com/claude-code-setup-mcp-hooks-skills-2026/

[^3_4]: https://lobehub.com/it/skills/aedelon-claude-code-blueprint-anti-hallucination

[^3_5]: https://lobehub.com/pl/skills/aedelon-claude-code-blueprint-uv-workflow

[^3_6]: https://github.com/anthropics/claude-code

[^3_7]: https://github.com/langgptai/awesome-claude-prompts

[^3_8]: https://lobehub.com/ko/skills/aedelon-claude-code-blueprint-commit-message

[^3_9]: https://skillsllm.com/skill/cc-blueprint-toolkit

[^3_10]: https://www.reddit.com/r/ClaudeAI/comments/1mw5vnr/blueprintsmd_static_code_generator/

[^3_11]: https://n8ntemplates.me/templates/transform-github-repos-into-evidence-based-architecture-blueprints-with-claude-13362

[^3_12]: https://www.youtube.com/watch?v=7pKN_pjPW04

[^3_13]: https://hedleyproctor.com

[^3_14]: https://github.com/alirezarezvani/claude-skills

[^3_15]: https://www.aibase.com/de/repos/project/cc-blueprint-toolkit

[^3_16]: https://support.claude.com/en/articles/10167454-using-the-github-integration

[^3_17]: https://lobehub.com/fr/skills/aedelon-claude-code-blueprint-anti-hallucination

[^3_18]: https://github.com/topics/claude-code

