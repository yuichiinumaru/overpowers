# Relatório de Mineração de YouTube (Teste Fernando Brasão)

## 1. Verificação Inicial e Extração de Links
A operação começou analisando o canal `https://youtube.com/@fernandobrasao`.
O uso de scripts leves falhou porque o YouTube utiliza carregamento dinâmico avançado. A solução adotada foi utilizar o Playwright (`scripts/helpers/yt_extractor.js`) para emular o scroll e capturar a árvore do DOM iterativamente.
**Resultado:** Extração de **600 links únicos** válidos, salvos em `skills/youtube-skill-creator/references/fernandobrasao_playwright_links.md`.

## 2. O Problema de Transcrição e Bloqueio de IP na Nuvem
Durante a fase de validação da skill `youtube-skill-creator` (testes diretos do vídeo e áudio do YouTube), nos deparamos com o bloqueio impiedoso do YouTube contra infraestruturas de nuvem (AWS/GCP, de onde este sandbox opera).
- Bibliotecas como `youtube-transcript-api` resultaram em falhas.
- CLI baseadas em scraping robusto, como `yt-dlp` (e todas as bibliotecas similares do ecossistema), retornam `HTTP Error 403: Forbidden`.
- Soluções de workaround (exportar cookies do navegador via Playwright e usá-los no yt-dlp, ou acionar solvers de JavaScript JS-Challenge como Deno) não superam o fingerprinting em nível de roteamento do Cloud.

**A Solução Híbrida:** Foi criado o helper local `scripts/helpers/youtube_audio_transcriber.js`. Como os agentes rodam via CLI e os usuários executam localmente nas suas próprias máquinas (onde o IP residencial/comercial passa pela malha do YouTube sem alertas graves), o script funciona baixando a flag `bestaudio` pelo `yt-dlp` local do usuário e, ato contínuo, transcreve localmente via Whisper.

## 3. Sobrecarga de Contexto ("Context Rot") vs Fluxo Cíclico
A diretriz pedia a avaliação de estressar o agente assistindo o "máximo de vídeos possível". Aqui detalhamos por que colocar 50+ vídeos de uma vez destrói a coerência do modelo:
- Modelos LLM que consomem tokens infinitos tendem a reescrever informações ao longo do prompt ou misturar o conteúdo de vídeos diferentes quando assuntos muito similares são concatenados.
- Se o agente assiste a 10 vídeos sobre "Engenharia de Prompt", as sub-técnicas são amalgamadas numa Skill monolítica ou em dezenas de Skills redundantes, perdendo granularidade.

**Estratégia Adotada e Implementada:**
Refinamos o workflow (`workflows/youtube-skill-mining.md`) e o agente (`agents/youtube-ripper.md`) para operarem através de **Gestão de Contexto e Recursive Loop**.
1. **Lotes Curtos (2 a 5 vídeos):** O agente transcreve poucos vídeos por vez.
2. **Buffer de Anotações:** Se o conhecimento do lote for bom, mas insuficiente para formar um procedimento claro e confiável ("não é skill ainda, é apenas dica"), o agente NÃO cria a skill. Ele arquiva essas notas num arquivo em `.agents/reports/youtube-mining-notes.md`.
3. **Loop Contínuo:** Ele avança para os próximos vídeos. Em determinado ponto, as novas transcrições cruzarão com as notas acumuladas no log temporário. Nesse instante, o agente funde tudo, descarta o log e crava uma Skill completa e inédita, não redundante.

Essa metodologia permite processar infinitos vídeos na esteira, evitando a criação de lixo e mantendo o agente sempre operando em um bloco de contexto higienizado (Janela de ~15k tokens no máximo).
