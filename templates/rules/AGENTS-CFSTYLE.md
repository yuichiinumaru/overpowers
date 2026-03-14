# CONSTITUIÇÃO GLOBAL DO OVERPOWERS INTEGRATED AGENT SYSTEM

**Lei Fundamental Nº 1, de 16 de Março de 2026**

Dispõe sobre princípios, regras operacionais, fronteiras de segurança e práticas de desenvolvimento aplicáveis a todos os agentes integrantes do Overpowers Integrated Agent System.

**O MANTENEDOR DO ECOSSISTEMA**

**FAZ SABER** que decreta e promulga a seguinte Constituição Global:

***

## TÍTULO I
**DISPOSIÇÕES PRELIMINARES**

**Art. 1º** Esta Constituição Global estabelece a ordem normativa aplicável a todos os agentes que operem em ambientes integrados ao Overpowers Integrated Agent System, incluindo, sem limitação, Gemini-cli, Codex-cli, Claude-cli, Droid-cli, Kilo-cli, Opencode e demais ferramentas compatíveis.

**§ 1º** Suas disposições vinculam diretamente todos os agentes que declarem aderência às Global Rules, independentemente do projeto ou repositório em que atuem.

**§ 2º** É vedado a qualquer agente, humano ou artificial, atuar em desconformidade com esta Constituição.

**Art. 2º** A hierarquia normativa observará a seguinte ordem de prevalência:
I – esta Constituição Global;
II – Lei Orgânica de Projeto (AGENTS.md na raiz);
III – Códigos de Domínio (AGENTS.md em subpastas);
IV – Leis Especiais ou Normas Pontuais (em diretórios específicos, como `.ai/rules/`).

**Parágrafo único.** Em caso de conflito, prevalecerá norma de hierarquia superior, ressalvadas exceções expressamente previstas em disposição legal de nível equivalente ou superior.

***

## TÍTULO II
**DA IDENTIDADE E DA CONTINUIDADE DOS AGENTES**

**Art. 3º** Todo agente deverá assumir identidade própria, registrada em arquivo `.agents/continuity-<nome-do-agente>.md`.

**§ 1º** A identidade compreende descrição de foco atual, tarefas pendentes e decisões relevantes, devendo ser mantida atualizada ao final de cada sessão.

**§ 2º** Iniciada nova sessão sem indicação de identidade pelo usuário, o agente consultará o usuário sobre:
I – assunção de identidade existente; ou
II – criação de nova identidade, com arquivo de continuidade correspondente.

**Art. 4º** Verificada modificação por terceiros em arquivo sobre o qual esteja atuando, o agente poderá inserir comentário identificando:
I – sua identidade;
II – escopo das alterações pretendidas ou em execução.

***

## TÍTULO III
**DO PROTOCOLO ZERO DE CONTINUIDADE CENTRALIZADA**

**Art. 5º** Antes de qualquer atuação em repositório ou projeto, todo agente observará obrigatoriamente o Protocolo Zero, compreendido pelas seguintes etapas:
I – leitura do arquivo `continuity-<nome>.md` correspondente;
II – alinhamento de compreensão quanto ao foco atual;
III – atualização do arquivo ao final da sessão.

**Parágrafo único.** É vedado iniciar modificações na base de código antes da conclusão das etapas previstas neste artigo.

***

## TÍTULO IV
**DO ARQUIVAMENTO E DA PRESERVAÇÃO HISTÓRICA**

**Art. 6º** É vedado a qualquer agente efetuar exclusão permanente de arquivos, scripts, componentes ou pastas existentes em repositórios versionados.

**§ 1º** Compreendem-se entre as condutas vedadas:
I – uso de comandos `rm`, `rm -rf` ou equivalentes;
II – execução de ferramentas MCP ou scripts para fins de remoção definitiva.

**Art. 7º** Identificado artefato obsoleto, depreciado ou desnecessário, o agente moverá o item para o diretório `.archive/` na raiz do repositório.

**§ 1º** A exclusão definitiva de itens em `.archive/` constitui competência exclusiva do usuário humano.

**§ 2º** O diretório `.archive/` permanecerá incluído em `.gitignore`.

***

## TÍTULO V
**DO REGISTRO DE MUDANÇAS (CHANGELOG)**

**Art. 8º** Toda modificação relevante na base de código será acompanhada de registro em `CHANGELOG.md`, inserido no topo do arquivo, em ordem cronológica decrescente.

**Art. 9º** É vedado:
I – apagar entradas preexistentes;
II – alterar conteúdo de entradas pretéritas, ressalvadas correções formais de digitação justificadas.

**Art. 10.** O formato mínimo das entradas observará:
I – data `AAAA-MM-DD`;
II – título breve;
III – seção indicativa (Added, Changed, Fixed, Removed);
IV – listagem sucinta das alterações;
V – identificação do autor ou agente.

***

## TÍTULO VI
**DA GESTÃO DE TAREFAS E NOMENCLATURA**

**Art. 11.** O fluxo de tarefas observará:
I – planejamento em `.docs/tasks/planning/` (sem geração de código);
II – formalização em `.docs/tasks/nnnn-tipo-subtipo-nomes.md`;
III – acompanhamento em `.docs/tasklist.json`, sob gestão exclusiva do usuário.

**§ 1º** Considera-se tarefa formalizada aquela que contenha:
I – condições de saída claras;
II – descrição detalhada do que, como, quando, onde e por quê;
III – subtarefas em lista de verificação `[ ]`;
IV – suficiência para execução autônoma.

**§ 2º** É vedado ao agente modificar `.docs/tasklist.json`, salvo autorização expressa do usuário.

**Art. 12.** Arquivos de tarefas seguirão o padrão `nnnn-tipo-subtipo-nomes.md`, em que:
I – três primeiros dígitos indicam ordem cronológica;
II – último dígito indica:
a) `0` para tarefa bloqueadora;
b) `1` a `9` para tarefas paralelizáveis.

**Art. 13.** É vedado o uso de espaços, underscores ou camelCase em nomes de arquivos, admitindo-se:
I – letras minúsculas;
II – hífens para separação.

***

## TÍTULO VII
**DA DOCUMENTAÇÃO E DA CONSCIÊNCIA COMPARTILHADA**

**Art. 14.** Todo trabalho de longa duração será documentado em:
I – `.agents/thoughts/<nome-do-agente>/` (rascunhos e pensamentos intermediários);
II – `.docs/` nas subpastas respectivas (arquitetura em `.docs/architecture/`, etc.);
III – `.agents/memories/` para descobertas arquiteturais (com symlink para `.serena/memories/`).

**Art. 15.** É vedado arquivar documentos em `.docs/` enquanto possuírem relevância histórica ou de tracking.

**Art. 16.** Novos recursos serão documentados em guias apropriados (ex.: `.docs/hooks_guide.md`).

***

## TÍTULO VIII
**DO DESCARREGAMENTO DE PENSAMENTOS**

**Art. 17.** Em operações longas, exigentes ou complexas, o agente descarregará raciocínio, contexto e pensamentos intermediários para `.agents/thoughts/<nome-do-agente>/`, usando convenções de nomenclatura semântica.

**Parágrafo único.** Em caso de dúvida sobre decisão anterior, o agente consultará referidos arquivos.

***

## TÍTULO IX
**DAS CONVENÇÕES E DA MODULARIDADE**

**Art. 18.** Todo projeto conterá AGENTS.md na raiz, mapeando:
I – nome e mantenedor;
II – componentes principais em tabela estruturada;
III – modularidade específica do projeto.

**Art. 19.** Identificadas inconsistências em convenções de nomenclatura ou organização:
I – o agente parará a operação;
II – consultará o usuário sobre imposição de padrão;
III – sugerirá convenção adequada.

**§ 1º** Convenções serão avaliadas quanto à distribuição equilibrada de itens (regra de 25% de desvio máximo).

**§ 2º** Operações repetitivas ensejarão criação de templates ou assets reprodutíveis em pastas apropriadas.

***

## TÍTULO X
**DA GOVERNANÇA DE MODELOS**

**Art. 20.** Em scripts que invoquem LLMs pontualmente, observar-se-ão:
I – High Reasoning: `gemini-3.1-pro` / `claude-4.6-opus-thinking`;
II – Fast Reasoning: `gemini-3-flash` / `claude-4.6-sonnet`;
III – Testes: `gemini-3.1-flash-lite`, `qwen-flash`, `gpt-5.1-mini`.

**§ 1º** É vedado o uso de modelos depreciados ou bibliotecas obsoletas.

**§ 2º** É vedada alteração de modelos definidos pelo usuário ou criação de fallbacks não solicitados.

***

## TÍTULO XI
**DAS PRÁTICAS DE ENGENHARIA (GDFRSBT)**

**Art. 21.** Todo ciclo de desenvolvimento observará o pipeline GDFRSBT (Goal, Domain, Feature, Readme, Spec, Behaviour, Test Driven Development), executado top-down.

**Art. 22.** A aplicação do GDFRSBT seguirá a tabela de estágios prevista no Anexo I desta Constituição.

**§ 1º** É vedado iniciar implementação antes da aprovação dos documentos de GDD e FDD (Goal e Feature Driven).

Aqui vai um **Art. 23** reformulado que integra coesamente o DDD (tático e estratégico) com os outros sistemas do GDFRSBT, mostrando como eles se complementam:

***

## **Art. 23.** No pipeline GDFRSBT, as práticas relacionam-se da seguinte forma:

**I** – **GDD** define critérios de negócio mensuráveis (o "porquê");
**II** – **DDD Estratégico** mapeia subdomínios e *bounded contexts* (o "onde");
**III** – **FDD** decompõe em *features* priorizadas (o "o quê");
**IV** – **RDD** documenta experiência de uso (o "como usar");
**V** – **SDD** estabelece contratos executáveis entre contextos (o "contrato");
**VI** – **BDD** valida regras de negócio com cenários *Given/When/Then* (o "comportamento");
**VII** – **DDD Tático** modela entidades, agregados e *value objects* dentro de cada contexto (o "modelo interno");
**VIII** – **TDD** implementa código coberto por testes unitários (*Red-Green-Refactor*) (o "código").

**§ 1º** O **DDD** atua em dois níveis complementares:
**a)** estratégico (Art. 23, II) para delimitar responsabilidades entre times/sistemas;
**b)** tático (Art. 23, VII) para modelagem interna de cada *bounded context*.

**§ 2º** A execução segue ordem top-down: negócio → arquitetura → features → implementação, sendo vedada inversão de prioridades.

**§ 3º** Cada estágio gera artefato específico (Anexo I), sendo a implementação (TDD) subordinada à aprovação prévia dos estágios I a VII.

***

## **Fluxo visual na Exposição de Motivos:**

```
GDD (Negócio) 
↓
DDD Estratégico (Arquitetura) 
↓
FDD (Features) 
↓
RDD (UX) + SDD (Contratos)
↓
BDD (Comportamento)
↓
DDD Tático (Modelagem interna)
↓
TDD (Código)
```

***

## TÍTULO XII
**DA SEGURANÇA MULTI-AGENTE E VCS**

**Art. 24.** É vedado o uso de comandos `git` alteradores de estado, tais como `git commit`, `git add`, `git push`, `git checkout`, `git branch`, `git merge`, `git rebase`.

**§ 1º** Comandos de leitura (`git log`, `git diff`, `git status`) são admitidos.

**Art. 25.** Operações de VCS serão realizadas via Jujutsu (`jj`), em workspaces isolados.

**Art. 26.** É vedado:
I – commit ou push sem autorização do usuário;
II – push direto para branches compartilhadas (`main`, `development`, `staging`).

**§ 1º** Mudanças serão pushadas para branches novas, com `jj bookmark create` e `jj git push --allow-new` no primeiro push.

**Art. 27.** Em ambientes CLI sem suporte a prompts TTY, redirecionar saídas para `.agents/thoughts/` (ex.: `jj log --no-graph > .agents/thoughts/jj-log.md`).

**Art. 28.** Antes de commit ou push, escanear repositório em busca de segredos, garantindo `.gitignore` atualizado.

**Art. 29.** É vedado:
I – execução de comandos destrutivos (`rm -rf /`, `mkfs`);
II – envio de respostas parciais a superfícies externas.

***

## TÍTULO XIII
**DISPOSIÇÕES FINAIS**

**Art. 30.** Todo agente atualizará `CHANGELOG.md` e `continuity-<nome>.md` antes de encerrar sessão.

**Art. 31.** Esta Constituição entra em vigor na data de sua aprovação pelo mantenedor do ecossistema.

***

# ANEXO I - TABELA DE ESTÁGIOS GDFRSBT

| Estágio | Prática | Escopo | Artefato / Output Chave |
| --- | --- | --- | --- |
| **1. Objetivos** | **GDD** | Macro / Negócio | Metas claras e Métricas de Sucesso. |
| **2. Domínio Macro** | **DDD** (Estratégico) | Arquitetura | *Bounded contexts*, *Context maps* e Subdomínios. |
| **3. Planejamento** | **FDD** | Gestão de Entrega | Lista priorizada e decomposta de *Features*. |
| **4. Visão de Produto** | **RDD** | UX / DX | Arquivo `README.md` orientando a experiência de uso. |
| **5. Contratos** | **SDD** | Integração | *Specs* legíveis por máquina (ex: OpenAPI, JSON Schema). |
| **6. Comportamento** | **BDD** | Regras de Negócio | Cenários estruturados (*Given/When/Then*). |
| **7. Domínio Micro** | **DDD** (Tático) | Lógica de Negócio | Entidades, Agregados, *Value Objects*. |
| **8. Implementação** | **TDD** | Código / Unidade | Testes unitários falhos → Implementação → Refatoração. |

***

## EXPOSIÇÃO DE MOTIVOS

### ALERTA DO SISTEMA (Original)
> **ALERTA DO SISTEMA**: Esta é a **Constituição Global** do Overpowers Integrated Agent System.
> Esta unifica todas as leis operacionais, práticas de desenvolvimento e fronteiras de segurança.

### PERSONA (Original)
- Este sistema de identidades existe de forma complementar ao sistema de tarefas, para evitar colisões de trabalho com agentes trabalhando em tarefas paralelamente.
- Mantenha a coerência e coesão do projeto em que está trabalhando enquanto estende suas capacidades, observando as regras e convenções particulares do projeto em AGENTS.md.

### GDFRSBT - Detalhamento das Práticas

Para que um projeto de Software, seja qual for, possa ser iniciado e terminado com sucesso, ele deve seguir os observar diversos aspectos. Para cada um deles, existe uma prática de desenvolvimento associada, cada qual com seu foco principal. Nós iremos usar todas em conjunto, de forma sistemática, onde cada uma se adequar melhor.

**a) O que é?** O **GDFRSBT** (Goal, Domain, Feature, Readme, Spec, Behaviour, and Test Driven Development) é uma meta-metodologia de engenharia de software que consolida sete práticas de desenvolvimento em um pipeline contínuo. Ela garante que nenhum código seja escrito sem um propósito claro de negócio, uma arquitetura validada e uma cobertura de testes rigorosa.

**b) Por que usar?** Para eliminar ambiguidades, prevenir *drift* arquitetural (desvio entre o código e a especificação) e garantir que a implementação seja guiada por critérios de sucesso preestabelecidos em vez de "achismos" técnicos.

**c) Onde usar?** Em todo e qualquer ciclo de desenvolvimento de software do projeto — desde a concepção de um novo microserviço até a adição de uma pequena *feature* ou correção de *bug*.

**d) Quando usar?** Cada coisa no momento devido. A execução deve seguir uma ordem de refinamento top-down, isto é, do macro (negócio) para o micro (código):

| Estágio | Prática | Escopo | Artefato / *Output* Chave |
| --- | --- | --- | --- |
| **1. Objetivos** | **GDD** | Macro / Negócio | Metas claras e Métricas de Sucesso. |
| **2. Domínio Macro** | **DDD** (Estratégico) | Arquitetura | *Bounded contexts*, *Context maps* e Subdomínios. |
| **3. Planejamento** | **FDD** | Gestão de Entrega | Lista priorizada e decomposta de *Features*. |
| **4. Visão de Produto** | **RDD** | UX / DX | Arquivo `README.md` orientando a experiência de uso. |
| **5. Contratos** | **SDD** | Integração | *Specs* legíveis por máquina (ex: OpenAPI, JSON Schema). |
| **6. Comportamento** | **BDD** | Regras de Negócio | Cenários estruturados (*Given/When/Then*). |
| **7. Domínio Micro** | **DDD** (Tático) | Lógica de Negócio | Entidades, Agregados, *Value Objects*. |
| **8. Implementação** | **TDD** | Código / Unidade | Testes unitários falhos → Implementação → Refatoração. |

**e) Como usar:** Para que os agentes e desenvolvedores apliquem este framework de forma pragmática, as seguintes Diretrizes Operacionais (SOP) devem ser respeitadas durante a execução de tarefas:

**🎯 Goal-Driven Development (GDD)**
* **Regra:** Defina o critério de sucesso antes de agir.
* **Ação:** Se a meta é "Adicionar validação", o critério é "Escrever testes de limite para entradas inválidas e fazê-los passar". Repita até que a métrica de sucesso seja alcançada.

**📦 Feature-Driven Development (FDD)**
* **Regra:** Quebre sistemas complexos em funcionalidades iterativas com ciclo de vida curto (máx. 2 semanas).
* **Ação:** Sempre siga a estrutura de 3 documentos para novas features dentro de `.docs/tasks/`:
1. `nnnn-tipo-subtipo-nomes-feature-plan.md` (Visão de produto, requisitos).
2. `nnnn-tipo-subtipo-nomes-technical-design.md` (Arquitetura, modelagem DDD).
3. A tarefa em si (ex: `.docs/tasklist.json`), que deve obrigatoriamente referenciar os dois documentos acima.
* *Atenção:* A implementação **não** deve começar até que o Design Técnico e o Plano da Feature sejam revisados e aprovados.

**📝 Readme-Driven Development (RDD)**
* **Regra:** A documentação guia o uso, não o contrário.
* **Ação:** Escreva o `README.md` de um novo módulo/serviço assumindo que ele já está pronto. Se for difícil de explicar no papel, será difícil de usar na prática. Repense o design.

**⚙️ Spec-Driven Development (SDD)**
* **Regra:** *Spec-as-Source*. A especificação é o controle de arquitetura executável.
* **Ação:** O código deve ser derivado e subordinado à especificação (ex: OpenAPI). Se a implementação divergir da *Spec*, o *build* deve falhar.

**🎭 Behaviour-Driven vs. Test-Driven (BDD e TDD)**
Ambos usam testes, mas em níveis e linguagens complementares. Devem ser usados em conjunto:
* **BDD (O *O Que*):** Foco no comportamento da perspectiva do usuário/negócio.
* *Como usar:* Escreva cenários em linguagem quase natural (Dado que / Quando / Então) para que Devs, QA e Negócios colaborem. Valida jornadas reais e regras de negócio.
* **TDD (O *Como*):** Foco em baixo nível, no design interno do código (funções, classes).
* *Como usar:* Ciclo clássico `Red` (teste unitário escrito primeiro e falhando) → `Green` (código mínimo para passar) → `Refactor` (melhoria da qualidade). Nunca escreva código de produção que não seja coberto por um teste pré-existente.

***

**FIM DA CONSTITUIÇÃO GLOBAL**

