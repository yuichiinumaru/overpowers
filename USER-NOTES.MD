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
