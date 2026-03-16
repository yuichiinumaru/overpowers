# O Pipeline de Colheita (Jules Pipeline)

## 🚨 REGRAS ESTRITAS DE EXECUÇÃO PARA O AGENTE (NÃO IGNORE) 🚨
**ATENÇÃO AGENTE DE IA:** Não tente ser espertinho com a execução desses scripts. Você tem a péssima tendência de alterar comandos com base em heurísticas genéricas de segurança. Siga estas regras EXATAMENTE como estão aqui:

1. **NÃO USE REDIRECIONAMENTO DE LOG (`> log.txt` ou `2>&1`):** Você deve rodar o script de launcher EXATAMENTE como `./scripts/jules-launcher-v2.sh <plan.json>`. Não anexe `> jules.log` nem tente dar `tail` nele. O Jules NÃO exibe logs no terminal progressivamente e não dá output interativo. Ele apenas faz a tarefa na nuvem e pronto.
2. **NÃO PULE O LOGIN:** Não decida por conta própria que "fazer login" não é a boa porque você acha que pode automatizar de outro jeito. A skill foi desenhada assim por um motivo. A forma devida de usar a skill é rodando o script de login quando solicitado.
3. **NÃO É UM COMANDO INTERATIVO QUE VAI TE TRAVAR:** O comando na CLI não é um prompt interativo no terminal em que você não vai conseguir responder. Ele vai abrir o navegador automaticamente. O usuário HUMANO vai saber que é para apenas clicar em outra conta no browser para logar e finalizar. Apenas rode o comando normalmente.

---

Para contornar limites de API, PRs vazios e facilitar a integração massiva de código do Jules, esta skill utiliza um pipeline de 4 estágios. Ele isola os diffs em uma área de staging ("quarentena") antes de aplicá-los na sua base de código principal usando Jujutsu.

## Estágio 1: Disparo (Launch & Log)
O script `prompt-tasker.py` (chamado por `jules-launcher-v2.sh`) envia a tarefa para a nuvem.
- **O que faz:** Ao receber o Session ID do Jules, ele imediatamente salva essa informação no arquivo de rastreamento `.agents/jules_sessions.json`.
- **Como usar:** `./scripts/jules-launcher-v2.sh caminho/para/seu/plano.json`

## Estágio 2: Colheita (Harvest)
Após o Jules concluir a execução na nuvem, você precisa puxar os diffs.
- **O que faz:** O script `jules-harvester.py` lê o arquivo de rastreamento `.agents/jules_sessions.json`, baixa os diffs através do comando `jules remote pull --diff` e os salva em `.archive/harvest/jules/<session_id>.diff`. Ele também gera um `HARVEST_REPORT.md` mostrando o tamanho de cada diff e quantos arquivos foram tocados, ajudando a identificar tarefas que falharam ou retornaram 0KB.
- **Como usar:** `python3 scripts/jules-harvester.py`

## Estágio 3: Pré-Visualização (Surgical Preview)
Antes de aplicar às cegas, audite o código.
- **O que faz:** O script `jules-auditor.py` lê os diffs salvos no diretório de harvest e gera um `PREVIEW_REPORT.md`. Este relatório contém as primeiras 10-15 linhas de contexto de cada arquivo alterado. Isso permite que você avalie rapidamente se o código faz sentido sem precisar abrir diffs com milhares de linhas.
- **Como usar:** `python3 scripts/jules-auditor.py`

## Estágio 4: Integração via Jujutsu (JJ Auto-Apply)
Quando escolher qual sessão integrar (baseado nos relatórios), aplique na sua codebase de forma segura.
- **O que faz:** O script `jj-jules-apply.sh` cria um novo commit Jujutsu com a descrição apropriada e tenta aplicar o patch usando o comando `patch`. Se houver conflitos, ele falhará graciosamente, deixando o patch pendente para resolução manual ou descarte via `jj abandon`.
- **Como usar:** `./scripts/jj-jules-apply.sh <SESSION_ID>`
