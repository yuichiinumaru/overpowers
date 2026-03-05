1. Criar workflow para ingerir toda documentação de uma library, dependencia ou framework usado em um projeto (por exemplo, Agno, SurrealDB, etc) nas memórias do Serena, Memcord, e / ou NotebookLM. Avaliar qual funciona melhor.

2. Criar workflow para ir no site da documentação de uma dependencia / library / framework (por exemplo, Agno, SurrealDB, etc) e pegar e listar todos os links das páginas da documentação num arquivo, deduplicar. Depois, criar um notebook no notebooklm com o nome da dependencia / library / framework e subir todos os links para ele, cada um como sendo uma fonte. Se ultrapassar 200 links, ele deve baixar os links em arquivos .md, consolidar arquivos .md espalhados por temas / grupos em um só arquivo .md maior para cada grupo, e aí sim subir para o notebooklm, cada arquivo como uma fonte.


3. workflow pra escanear a sessão inteira e verificar se novas regras de negocio ou mudanças de organização foram estipuladas ou criadas; avaliar se vale a pena adcionar elas no agents.md ou realizar update em alguma regra la existente. não fazer edits destrutivos


4. Revisar
workflows/01-specify-feature.md   - para 1 feature
workflows/01-specify-project.md  - para 1 projeto e todas as suas features (quando ta no início do projeto)
workflows/02-plan-all.md         - para 1 projeto e todas as suas features (quando ta no início do projeto)
workflows/02-plan-feature.md     - para 1 feature
workflows/03-task-feature.md     - para 1 feature
workflows/03-task-ongoing.md     - para 1 tarefa que começou e saiu fazendo no meio (acontece no vibecoding kkk)
workflows/03-task-project.md     - para 1 projeto e todas as suas features (quando ta no início do projeto)



5. Pesquisar melhores formas de orquestrar agentes via ACP e A2A
https://geminicli.com/docs/core/remote-agents/
https://geminicli.com/docs/core/subagents/
https://opencode.ai/docs/acp/
https://agentclientprotocol.com/get-started/registry


6. Criar um workflow para enrich tasks existentes (fazer pesquisas complementares, revisar, refinar etc) - exigir maior detalhamento nas regras e no template deixar isso mais claro (impor condições minimas mais claras)


perfeito! excelente.

unica modificação que eu fiz foi renomear os templates e criei uma copia em docs/tasks/

docs/tasks/000-template-feature-plan.md
docs/tasks/000-template-technical-design.md
docs/tasks/000-template.md
(mesma coisa em templates/tasks)

### 7.5. Specification-First Development (SDD)
When a task is of type `feature` (e.g., `0020-feature-auth-system.md`), it must be accompanied by detailed specs rather than nested in separate feature folders:
1. **Feature Plan**: Create `nnnn-type-subtype-names-feature-plan.md` alongside it in `docs/tasks/`. (follow the template docs/tasks/000-template-feature-plan.md)
2. **Technical Design**: Create `nnnn-type-subtype-names-technical-design.md` alongside it in `docs/tasks/`. (follow the template docs/tasks/000-template-technical-design.md)



agora tá perfeito!

o que eu gostaria agora de fazer
1. criar um template de AGENTS.md com base no nosso (ou modificar o templates/rules/AGENTS.md) que sirva para qualquer projeto, mas que aplique as mesmas regras de organização etc. Quero replicar o que fizemos aqui no overpowers para meus outros projetos, ta uma obra prima.

2. criar um workflow que use o template de 1 e só modifique as partes que sao unicas a cada projeto. se já existir um AGENTS.md no projeto em questão (por exemplo se eu aplicar no Khala-Agentmemory) ele vai aplicar o padrão AGENTS.md com as regras todas do template, mas vai tentar integrar regras já existentes ali ao template. em caso de regras contraditórias ou conflitantes, o agente deve perguntar qual deve prevalecer - as regras do template, ou as regras existentes.

3. criar um workflow em que o agente crie a estrutura de pastas de tasks em docs/ e copie os templates de tasks que criamos para docs/tasks/

4. criar um workflow em que o agente crie a pasta .agents, divida a codebase inteira em 10 "pedaços" e task 10 subagents para escanear em paralelo cada parte. os agents devem usar a pasta .agents/thoughts/ para guardar os relatórios parciais lá conforme forem investigando e analisando. no final, eles devem fazer um update das memórias para o serena mcp, memcord e outros (tipo o @beautifulMention) com o máximo de detalhes

5. criar um workflow em que o agente faça uma varredura completa na pasta docs/ existente e mova tudo que for inútil ou desatualizado para .archive/

6. criar um workflow em que o agente faça uma varredura completa na pasta archive/ e extraia de lá ideias para docs/tasks/planning. ele deve analisar a codebase e ver se faz sentido. tudo deve ser analisado. se ele encontrar arquivos perdidos q possam ir para outro local no projeto (sei la ficou perdido em merge conflict antigo), ele sugere ao user. ideias para planning podem ser: tasks antigas q nao foram executadas, plannings antigos q nao foram executados, arquivos de blueprints specs features, relatórios apontando problemas de performance segurança conectividade etc (podem virar tasks pra conserta-los), pesquisas, etc.

7. criar um workflow em que o agente analisa o conteúdo da pasta docs/tasks/planning/ e compara com a codebase pra ver o que ja foi implementado ou nao; o que ja foi implementado vai para .archive/ o que ainda não foi, ele avalia e determina se vale apena. o que valer apena, ele cria tarefas a partir do que encontrar, com base nos templates de tasks, com observação especial para casos onde é uma feature. DEPOIS, o que ele nao tiver certeza se vale apena, ele pergunta ao user se quer que faça tasks a partir dali e explica pq ta em duvida.
