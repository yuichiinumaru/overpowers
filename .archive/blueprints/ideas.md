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
