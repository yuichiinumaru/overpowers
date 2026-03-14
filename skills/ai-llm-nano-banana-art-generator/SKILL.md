---
name: nano-banana-art-generator
description: Integrates Nano Banana Pro (v3) as an image generation skill within Claude/Agent
  workspaces to create highly customized, brand-consistent graphics from text content.
tags:
- ai
- llm
category: creative
color: null
tools:
  bash: true
  read: true
version: 1.0.0
---
# Nano Banana Art Generator Skill

Esta skill descreve como construir uma ponte (wrapper) para permitir que agentes de texto (como Claude ou agentes customizados que nativamente não geram imagens) utilizem a API/Ferramenta do Nano Banana Pro 3 para geração de arte estruturada e alinhada à marca.

## Estrutura da Skill

O objetivo é criar uma ferramenta que o agente principal possa chamar (um MCP ou um script CLI) com instruções precisas.

### 1. Definição da Ferramenta de Geração
Crie um script ou skill que encapsule a chamada para o Nano Banana. A skill deve aceitar parâmetros como:
- `content_topic`: O assunto do artigo ou post.
- `brand_guidelines`: Cores e estilos específicos (ex: "minimalista", "neon").

### 2. Prompt System (Injeção de Contexto)
O pulo do gato ("The Art Skill") não é apenas chamar um gerador de imagem, mas sim pre-processar o pedido. O agente deve:
1. Ler o conteúdo que o usuário quer ilustrar.
2. Formular um prompt de imagem altamente detalhado que traduza conceitos abstratos em elementos visuais (metáforas).
3. Injetar as diretrizes de branding fixas no final do prompt.
4. Enviar esse prompt robusto para o Nano Banana.

### 3. Exemplo de Execução
Em um ambiente configurado com MCPs (Model Context Protocol), o fluxo seria:
- **Usuário:** "Crie uma imagem de capa para meu blog post sobre cibersegurança e nuvem."
- **Agente (Claude):** Processa o pedido -> Extrai conceitos (nuvem, fechadura digital, dados fluindo) -> Formula o prompt técnico para a API -> Chama a skill `nano_banana_generate(prompt="...", style="...")`.
- **Skill:** Retorna a URL ou o arquivo da imagem gerada.

## Referência
Extraído do vídeo: [My Art Skill With Nano Banana 3](https://www.youtube.com/watch?v=-Ek68Uu9x5k)
