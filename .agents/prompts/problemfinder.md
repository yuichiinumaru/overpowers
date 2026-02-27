ROLE: Senior Architect & Project Manager

Task: Siga os passos abaixo e foque só em analisar e planejar, não implemente nada por enquanto.

### Preamble (OBRIGATÓRIO)
- Execute AGENTS.md **Seção 0** em sua totalidade primeiro (ler knowledge, gerar tree.md, ler tasklist).
- Comece listando suas memórias (knowledge) sobre este repositório e relendo todas para lembrar tudo o que sabe sobre o repo. No decorrer do processo, faça update progressivo das suas memórias.
- Não espere para fazer isso no final - faça no decorrer do processo, imediatamente após notar distinções e updates na codebase discrepantes com o que vc tinha de memórias.
- Salve todos os relatórios e análises em `.agents/reports/` (nunca em `.jules/`).
- Ao redigir relatórios com data/hora, pesquise a data atual na internet ANTES de escrever.

1. Analise a codebase em comparação com a documentação e avalie o estado de desenvolvimento da codebase. Leia docs/tasklist.md e docs/tasks/ e analise cuidadosamente o que tem lá, para entender o roadmap de desenvolvimento do projeto.

2. Faça uma auditoria completa das funcionalidades do projeto e pense o máximo de ideias que conseguir para visualização delas via UI.
  a) Procure por comentários em codigo e por mocks, stubs, fake code e liste onde precisa de implementação real (onde precisa de mock por questão de teste por exemplo deixa pra la)
  b) Run test suite e liste todos os erros que encontrar. Investigue a causa raiz deles. Não implemente fixes ainda.
  c) Procure, investigue e analize a estrutura da SurrealDB e a conexão backend frontend. Veja se há pontos incorretos, incompletos ou que merecem melhor implementação.
  d) Verifique se a SurrealDB está sendo utilizada ao máximo de suas capacidades atualmente (ela é uma database multimodel com graph, vector, doc, sql, keyvalue, time series, fulltext search, geospatial and timeseries) ou há pontos onde ela poderia ser melhor utilizada ou aproveitada.
  e) Procure por codigo duplicado, redundante, ou mal consolidado em merges.
  f) Procure por gaps na documentação do projeto. Ela serve não só como documentação mas também como uma forma de gestão do projeto e de manter seu desenvolvimento sob varias mãos sob controle, logo precisa que nenhum detalhe importante falte lá.
  g) Organização: Analise filename conventions, folder / file structure, modularidade / componentização e arquitetura - o que seria possível fazer para melhorar esses aspectos?
  h) Brainstorm: Pense no longo prazo, na versão mais foda possível do programa funcionando:
	- Como seria a melhor UX possível? Como a UI pode melhorar nisso?
	- Como seria o melhor backend possível dentro da tech stack escolhida?
	- Como podemos adicionar mais funcionalidades aproveitando o codigo já existente?
	- Como podemos adicionar mais funcionalidades criando coisas novas ou analisando outros repositórios?
	- Como podemos integrar melhor o que absorvemos de outros projetos?

3. Leia tasklist.md e analise cuidadosamente o que tem lá.
  - Adicione ou update macrotasks em docs/tasklist.md e respectivos arquivos detalhados em docs/tasks/ de acordo com o que achou, seguindo o template de docs/tasks/
  - Transforme em tarefas ou subtarefas tudo que encontrar que precisa ou pode ser melhorado.
  - Não destrua o conteúdo existente.
  - Não edite nenhum arquivo sem ler ele antes.
  - Não dê vereditos sem ter absoluta certeza antes: procure na documentação do projeto, online, ou na codebase a resposta sempre primeiro.

4. Faça 10 iterações / repetições sobre os passos 1-2-3.
	- Em cada iteração, melhore, refine, detalhe mais a fundo, expanda e otimize o planejamento de tarefas.
	- Falhar em planejar é planejar para falhar.

5. Code review, commit push. PRs devem ser direcionados para a branch `staging`.