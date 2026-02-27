---
name: youtube-link-extractor
description: Extração eficiente de links de vídeos, shorts e transmissões ao vivo (lives) de canais do YouTube sem necessidade de API Key. Use para coletar todos os links de um canal e organizar em documentos Markdown.
---

# YouTube Link Extractor

Esta skill permite extrair todos os links de vídeos de um canal do YouTube navegando pelas abas de Vídeos, Shorts e Ao Vivo (Streams).

## Fluxo de Trabalho

### 1. Navegação
Navegue até a aba específica do canal que deseja extrair:
- Vídeos: `https://www.youtube.com/@username/videos`
- Shorts: `https://www.youtube.com/@username/shorts`
- Lives: `https://www.youtube.com/@username/streams`

### 2. Extração
Use o script localizado em `scripts/extract_links.js` com a ferramenta `browser_console_exec`. 

**Dica:** O script já possui lógica para detectar e extrair links de vídeos normais, lives e shorts automaticamente com base no contexto da página.

### 3. Consolidação
Após coletar os links de cada aba, use um script Python para remover duplicatas e formatar em um arquivo `.md`.

## Scripts Inclusos

- `scripts/extract_links.js`: Script JavaScript para execução no console do navegador. Realiza scroll automático e coleta de links únicos.

## Melhores Práticas

- **Scroll:** O YouTube carrega conteúdo dinamicamente. O script realiza scrolls automáticos, mas para canais muito grandes, pode ser necessário aumentar o número de iterações.
- **Filtros:** Sempre limpe os links removendo parâmetros de query (como `&t=...` ou `&pp=...`) para evitar duplicatas.
- **Organização:** Ao criar o arquivo Markdown, separe os links por categorias (Vídeos, Shorts, Lives) para melhor legibilidade.
