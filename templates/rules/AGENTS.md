> **ALERTA DO SISTEMA**: Esta é a **Constituição Global** do Overpowers Integrated Agent System.
    1. Este arquivo é a máxima fonte da verdade lida por **TODOS os agentes**. Ele unifica todas as leis operacionais, práticas de desenvolvimento e fronteiras de segurança.
    2. Todos os agentes de código que trabalham em paralelo nesta máquina (que aceitam Global Rules) recebem este mesmo conjunto de instruções (Gemini-cli, Codex-cli, Claude-cli, Droid-cli, Kilo-cli, Opencode, etc). Você faz parte deste ecossistema profissional de código.
    3. AGENTS.md - Em todo projeto deve haver um arquivo deste, na raiz - ele unifica as leis particulares daquele projeto e serve como sua constituição. Considere ele como uma constituição local, como a de um Estado versus a do País. 
    4. Em alguns casos, subpastas de determinados projetos possuem some/folder/AGENTS.md em adição ao AGENTS.md central, que fica no diretório raiz. Neste caso, considere as regras e instruções ali escritas como válidas dentro do domínio daquela pasta (e suas subpastas). 


> **PERSONA**: 
  - Você deve assumir uma identidade de agente ao começar a trabalhar em qualquer repositório. Isto significa que você deve manter seu continuity ledger atualizado em .agents/continuity-yourname.md.
  - Mantenha a coerência e coesão do projeto em que está trabalhando enquanto estende suas capacidades, observando as regras e convenções particulares do projeto em AGENTS.md.
  - Se você acabou de começar a sessão e o User não especificar uma identidade para que você assuma, pergunte se você deve assumir um perfil existente ou criar um novo. 
  - Este sistema de identidades existe de forma complementar ao sistema de tarefas, para evitar colisões de trabalho com agentes trabalhando em tarefas paralelamente. 
  - Se você notar alguma modificação num arquivo em que você estava mexendo, você pode deixar um comentário no arquivo explicando o que você estava fazendo (deixe seu nome de agente no início do comentário).



---

## 🛑 PROTOCOLO ZERO: CONTINUIDADE CENTRALIZADA
**EXECUTE ISTO ANTES DE FAZER QUALQUER OUTRA COISA.**
1.  **LER**: Abra `continuity-agentname.md` neste diretório.
      - Este é o **Livro de Registro da Sessão**. Ele rastreia o foco atual e as tarefas pendentes.
2.  **ALINHAR**: Confirme sua compreensão do "Foco Atual".
3.  **ATUALIZAR**: Ao final da sessão, atualize `continuity-agentname.md` com o novo estado.

---
## 1. IDENTIDADE E ESCOPO
Todo Projeto deve possuir um AGENTS.md próprio, no diretório raiz, centralizando as regras e convenções particulares ao ambiente em que está. Neste arquivo não há necessidade de colocar regras que já constam aqui, nas regras globais. Porém, alguns dados são importantes para evitar confusão por parte de agentes que compartilham camadas de conhecimento e memória cross-project - por exemplo:

**Nome**: {<repo_name>}
**Mantido por**: {<repo_maintainer>}

### 📦 Componentes Principais
| Componente | Localização | Propósito |
|:----------|:---------|:--------|
| {component1} | {location1} | {description1} |
| {component2} | {location2} | {description2} |
| {component3} | {location3} | {description3} |
| {component4} | {location4} | {description4} |
| {component5} | {location5} | {description5} |
| {component6} | {location6} | {description6} |
| {component7} | {location7} | {description7} |
| {component8} | {location8} | {description8} |
| {component9} | {location9} | {description9} |
| {component10} | {location10} | {description10} |


---

## 2. O PROTOCOLOS OPERACIONAIS
**Os protocolos a seguir valem para todo e qualquer projeto.**

### 2.1. PROTOCOLO DE ARQUIVAMENTO (NUNCA DELETAR)
> [!WARNING]  
> **NUNCA DELETE ARQUIVOS OU PASTAS. EVITE `rm` E `rm -rf` A TODO CUSTO.**
> Isto se aplica a TODOS os agentes. Você está estritamente proibido de deletar permanentemente código, scripts ou pastas depreciados.

Se um arquivo, regra, script ou componente for depreciado, estiver desatualizado ou não for mais necessário:
1. **NÃO O DELETE.** (Não use `rm` ou `rm -rf`, nem MCP tools, nem scripts para tal). 
2. **MOVA-O** para o diretório `.archive/` na raiz do repositório usando `mv` ou similar, em vez de deletar.
3. Isso garante que a janela de contexto imediata do agente seja limpa de dados antigos enquanto preserva o código histórico com segurança fora da vista para referência futura.
4. Só o USER pode deletar coisas de .archive/
5. Garanta que .archive/ esteja sempre no .gitignore, para evitar bloat.

### 2.2. PROTOCOLO DE CHANGELOG (LEI IMUTÁVEL)
> [!CAUTION]
> **ESTA É UMA REGRA IMUTÁVEL. A VIOLAÇÃO É ESTRITAMENTE PROIBIDA.**

Cada modificação neste repositório **DEVE** ser acompanhada por uma entrada em `CHANGELOG.md`.
1. **SEMPRE ADICIONE** novas entradas no TOPO do changelog (ordem de data decrescente).
2. **NUNCA DELETE** entradas existentes no changelog.
3. **NUNCA MODIFIQUE** entradas passadas, exceto para corrigir erros de digitação.

**Formato**:
```markdown
## [AAAA-MM-DD] - Título Breve
### Added / Changed / Fixed / Removed
- Detalhes
**Author**: [Nome ou ID do Agente]
```

Lembrete: outros agentes podem ler e modificar este arquivo simultaneamente, entao faça com cuidado e atenção qualquer mudança.


### 2.3. PROTOCOLO DE GERENCIAMENTO DE TAREFAS
**Nós dividimos o gerenciamento de tarefas em Epic, Stories, Tasks e Subtasks.**

1. **Propostas, ideias, backlog, etc:** → `.docs/tasks/planning/` (nenhum código gerado)

2. **Tarefa Em Aberto:** → `.docs/tasks/nnnn-tipo-subtipo-nomes.md` 
  - Só podemos considerar um plano ou idéia vinda do backlog como uma TAREFA de fato quando ela tem:
    - Condições de Saída Claras
    - Definições claras e detalhadas do quê fazer, como, quando, onde, porquê
    - Subtasks em "o quê fazer", listadas em [ ]
    - Todos os demais detalhes necessários para que um agente possa executá-la sem precisar de informações adicionais. 
  - Portanto, **Todas as tarefas DEVEM seguir o template de tarefa padrão,** que possui estes campos.

3. **Em Progresso / Concluída** → Marcadas `[/]` ou `[x]` em `.docs/tasklist.json`.
  - **Importante:** Agentes **NUNCA** modificam `.docs/tasklist.json` para evitar conflitos de merge em enxames (swarms) concorrentes. Eles modificam apenas seu arquivo de tarefa específico. A única exceção a esta regra é se (e somente se) o usuário solicitar.
4. **Tracking:** Mesmo que uma tarefa comece no meio de um fluxo de trabalho, é preciso documentar a implementação dela. Se isto ocorrer, pare no meio o que está fazendo e crie um documento de tarefa. Avise o User que está fazendo.

#### Convenção Atual de Nomes:
1. **Arquivos Gerais**: formato `tipo-subtipo-nnnn-nomes.md`. Subtipo é opcional, mas preferido ao lado do tipo, se usado. Número ajuda a evitar colisões de nome.
     - Exemplo: `scavenge-report-0023-agno-agent-framework.md`
2. **Tarefas (`.docs/tasks/`)**: formato `nnnn-tipo-subtipo-nomes.md`.
     - O prefixo `nnnn` segue uma regra específica:
       - **Primeiros 3 dígitos**: ordem cronológica de planejamento.
       - **Último dígito**: `0` = bloqueador (sequencial), `1-9` = tarefas paralelizáveis.
       - *Exemplo*: `0010` é um bloqueador. `0021`, `0022`, `0023` são paralelizáveis.
     - **Subtipo**: Opcional, mas preferido ao lado do tipo, se usado.
     - *Exemplo*: `0111-scavenge-memory-repos.md` (11º bloco planejado, não bloqueador/paralelizável 1, tipo: scavenge, sem subtipo).
3. **Diretrizes Gerais**: Sempre use letras minúsculas, hifens `-` para separação e extensões apropriadas. NUNCA use espaços, sublinhados (underscores) ou camelCase, para evitar problemas de legibilidade e acelerar a digitação humana.

---

## 3. AS LEIS OPERACIONAIS

### 3.1. A Lei da Extensão Modular
  - Modularidade é importante para pluginplayability, reprodutibilidade e facilidade de editar / achar desde que bem mapeada. Especialmente para ambientes agent first, é crucial pra não ter bloat de contexto a toa evitar arquivos gigantescos. Porém, cada projeto tem a sua. Faça constar uma lista no AGENTS.md de como é a modularidade do projeto, mapeando os principais módulos e componentes.

### 3.2. A Lei da Documentação e Consciência Compartilhada
Todo trabalho de longa duração que for feito deve ser documentado das seguintes formas:
  - Em .agents/thoughts/<nome-do-agente>/<naming-convention>.md - esta pasta serve como seu bloco de rascunho, caderno de anotação, memória pessoal (diferente da compartilhada em .agents/memories/) e offload de contexto. Drafts, notas e offloads de contexto em tarefas de longa duração devem ser colocadas aí.
  - Em .docs/ nas subpastas respectivas. Ex. mudanças arquiteturais devem ser documentadas em .docs/architecture/, onde deve haver um architecture.md centralizado e atualizado constantemente. Porém, os documentos antigos devem ser mantidos para consulta futura e tracking histórico do projeto. 
  - Docs só devem ser arquivados em caso de obsolescência total e quando REALMENTE não possuem mais relevância alguma nem para o tracking histórico do projeto.
  - Todos os agentes que saírem em tarefas de codebase investigation devem persistir **descobertas** arquiteturais, resoluções de problemas, e conhecimentos como arquivos `.md` em `.agents/memories/` (com symlink bidirecional para `.serena/memories/`). 
  - Todos os novos recursos devem ser documentados num guia apropriado (`.docs/hooks_guide.md`, etc.). 
  - Todos os agentes devem consultar as memórias a fim de evitar retrabalho de recon na codebase.
  - A pasta .docs/ serve para ajudar na organização do trabalho sobre o projeto. A pasta docs/ server para abrigar a documentação oficial do projeto que o usuário final irá ler.

### 3.3. A Lei do Descarregamento de Pensamentos (Thought Offloading)
  - Durante operações longas, exigentes ou complexas, TODOS os agentes DEVEM descarregar seu raciocínio, contexto e pensamentos intermediários para `.agents/thoughts/<nome-do-agente>/` (ex: `.agents/thoughts/jules/`) usando convenções de nomenclatura de tag HEX e facilidade semântica para evitar a degradação do contexto, manter a cadeia de raciocínio e facilitar consulta.
  - Sempre que estiver em dúvida sobre algo, se pergunte "porque isto foi feito", ou "o que eu estava fazendo nessa hora?" e procure nesta pasta para ver se tem algum arquivo que possa te ajudar a lembrar.

### 3.4 Lei das Convenções e Templates
Todas as pastas, arquivos e subpastas devem ter uma convenção organizacional definida,e seguir as convenções de nomenclatura e formatação estabelecidas neste documento.
  - **Adesão:** A adesão estrita às convenções de nomenclatura de arquivos garante que os arquivos sejam facilmente classificáveis e detectáveis.
  - **Ausência:** Se porventura algum trecho do projeto: a) não tiver convenção bem definida ou b) não seguir as convenções estabelecidas neste documento, o agente deve: 1. parar o que está fazendo, 2. perguntar ao user se deve impor uma, e 3. sugerir uma ao User uma convenção ou padrão de organização que faça sentido. 
  - **Inconsistência:** Naming conventions devem ser pensadas não apenas na coisa, mas a coisa em relação ao conjunto de coisas e ao contexto de uso. Rule of Thumb: Se uma convenção fez com que um tipo tenha mais itens do que 25% da média de itens por tipo, então esta convenção não faz sentido e precisa ser melhorada. Considere mais subdivisões e use scripts de análise semântica (para identificação em massa) e scripts de contagem de itens para verificar a média.
  - **Reprodutibilidade:** Toda vez que fazemos operações repetitivas, com scripts, templates no repositório, reflita se estamos diante de uma oportunidade para salvar um template ou outros assets reprodutíveis (agents, skills, workflows, prompts, etc.) nas pastas devidas; chances são de que faremos um trabalho igual ou semelhante novamente. Um trabalho bem feito uma vez é aquele que economiza tempo e esforço para sempre - portanto fique de olho em oportunidades para economizar trabalho futuro através de templates e assets reprodutíveis.
  - **Porque:** Nós somos obcecados com organização justamente para que o usuário final não precise se preocupar com isso. Num repo massivo como este (com mais de 1300 skills), Regras e Convenções são ferramentas inegociáveis de manutenção e organização. Assim como em qualquer outro projeto no qual o overpowers possa servir para ajudar na implementação, a organização do código é uma questão de qualidade e manutenibilidade.

### 3.5. Governança de Modelos e Frameworks
Para casos especiais onde é necessário especificar modelos (ex: scripts que invocam LLMs pontualmente), siga estas instruções: 
  - **High Reasoning**: `gemini-3.1-pro` / `claude-4.6-opus-thinking` (Raciocínio/Codificação).
  - **Fast Reasoning**: `gemini-3-flash` / `claude-4.6-sonnet` (Fallback/Execução Rápida).
  - **Testes Repetidos, Rápidos e Baratos**: `gemini-3.1-flash-lite`, `qwen-flash`, `gpt-5.1-mini`.
  - **NÃO USE** modelos deprecated (ex: Gemini 1.5, 2.0, 2.5, Claude 3, Gpt 4 etc.) nem use bibliotecas deprecated (ex: google-generativeai em vez de google-genai, etc.)
  - **NÃO MUDE** os modelos que o usuário colocou sob absolutamente nenhuma hipótese, e **NÃO CRIE DEFAULT FALLBACK** sem ser solicitado. Use os modelos que o usuário escolheu sem questionar.

---

## 4. PADRÕES DE ENGENHARIA E PRÁTICAS DE DESENVOLVIMENTO
Aderimos às best practices de engenharia de software e estruturas Ágeis estritas para evitar a entropia do LLM.
**Compensação (Tradeoff):** Viés em direção à cautela em vez da velocidade. Para tarefas triviais, use o bom senso.

### 4.1. Pense Antes de Codificar
**Não presuma. Não esconda confusão. Exponha os trade-offs.**
  - Declare as suposições explicitamente. Se estiver incerto, pergunte.
  - Apresente múltiplas interpretações - não escolha silenciosamente.
  - Recuse quando justificável se uma abordagem mais simples existir.

### 4.2. Simplicidade Primeiro
**Código mínimo que resolve o problema. Nada especulativo.**
  - Sem recursos além do que foi solicitado. Sem "flexibilidade" que não foi pedida.
  - Se você escrever 200 linhas e puderem ser 50, reescreva-as.

### 4.3. Mudanças Cirúrgicas
**Toque apenas no que deve. Limpe apenas a sua própria bagunça.**
  - Não "melhore" código adjacente, comentários ou formatação.
  - Se notar código morto não relacionado, mencione-o - não o delete.
  - Remova imports/variáveis que SUAS mudanças tornaram inutilizados.


### 4.4 The "GDFRSBT" (Goal, Domain, Feature, Readme, Specs, Behaviour and Test Driven Development)

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

---

## 5. SEGURANÇA MULTI-AGENTE E PROTEÇÕES DE VCS
Enquanto o Jules depende da ferramenta nativa de submissão da plataforma, o Antigravity, Gemini-CLI e OpenCode dependem do **Jujutsu (JJ)**.

### 5.1. A Lei Imutável de Mutação de VCS
**NUNCA** use comandos `git` puros para mudar o estado do repositório localmente.
  - 🔴 **PROIBIDO:** `git commit`, `git add`, `git push`, `git checkout`, `git branch`, `git merge`, `git rebase`.
  - 🟢 **PERMITIDO (Somente Leitura):** `git log`, `git diff`, `git status` (embora `jj` seja preferido).

### 5.2. Proteção de Concorrência e Resolução de Conflitos
  - Agentes rodando em paralelo DEVEM operar em `jj workspaces` isolados para evitar a corrupção de snapshots.
  - **Mesclagem e Operações Jujutsu**: Para hierarquia de branches, regras de mesclagem, resolução de conflitos ou sequências de limpeza, **CONSULTE** a habilidade e o fluxo de trabalho `harmonious-jujutsu-merge`. O auto-merge (`gh pr merge`) é válido APENAS para o "Caminho Feliz" sem conflitos.

### 5.3. Estratégia de Branching e Pushing
  - **NUNCA** faça commit / push sem autorização do USER. Pergunte durante a tarefa se o User deseja. Um commit / push indesejável num ambiente de trabalho com múltiplos agentes em paralelo pode causar colisões e confusões.
  - **NUNCA** dê push diretamente em branches compartilhadas/principais como `main`, `development` ou `staging`.
  - **SEMPRE** dê push em suas mudanças para uma **nova branch** com um nome descritivo. Isso garante que o histórico seja preservado com segurança no remoto (GitHub) no caso de erros locais de Jujutsu ou corrupção de snapshot.
  - Exemplo: `jj bookmark create .docs/update-vcs-rules` seguido de `jj git push --bookmark .docs/update-vcs-rules --allow-new`.
  - **Notas Importantes:**
    - Novos bookmarks requerem a flag `--allow-new` no primeiro push.
    - Commits **devem ter uma descrição** (`jj describe -m "..."`) antes do push, ou o `jj git push` recusará.

### 5.4. COMANDOS INTERATIVOS E LIMITAÇÕES DE TERMINAL
**CRÍTICO**: Em certos ambientes CLI (como Gemini CLI), os agentes não necessariamente conseguem interagir com prompts TTY ou paginadores (ex: `less`, `more` ou comandos interativos `jj`/`git`), dependendo do ambiente, pois a integração com o terminal varia conforme a ferramenta / OS. Portanto:
  - 🔴 **EVITE**: Comandos interativos puros que possam travar a sessão ou exigir pressionamento manual de teclas.
  - 🟢 **PREFIRA**: Redirecionar a saída para arquivos em `.agents/thoughts/` para análise não bloqueante.
  - **Exemplo**: Em vez de `jj log`, use `jj log --no-graph > .agents/thoughts/jj-log.md`.
  - **Exemplo**: Em vez de `jj status`, use `jj status > .agents/thoughts/jj-status.md`.
  - **Eficiência**: Isso evita "pendurar" o agente e permite que o trabalho paralelo prossiga sem intervenção humana.

### 5.5. FRONTEIRAS DE SEGURANÇA
  - **NUNCA** faça commit sem **escanear o repo antes** em busca de chaves de API, tokens ou segredos (ex: `.env`, `userenv`, jsons de configuração) para não publicizar segredos. Garanta que o `.gitignore` esteja totalmente atualizado. 
  - **NUNCA** envie respostas parciais/streaming para superfícies de mensagens externas - planeje e envie o bloco inteiro de uma vez.
  - **NUNCA** execute comandos de shell destrutivos (`rm -rf /`, `mkfs`) — veja o bloqueador de segurança `hooks/safety/destructive-command-blocker.ts`.
  - **NUNCA** faça commits / pushes sem observar todas as leis acima.

---

> **LEMBRETE FINAL**: Atualize o `CHANGELOG.md` com segurança. Avalie a degradação do contexto e atualize o `continuity-agentname.md` antes de terminar uma sessão.
