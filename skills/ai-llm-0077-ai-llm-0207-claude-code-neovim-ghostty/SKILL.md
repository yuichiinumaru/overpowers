---
name: claude-code-neovim-ghostty
description: Configures Ghostty panes and Neovim to seamlessly use Claude Code alongside Neovim without leaving the terminal. Focuses on setting up vim-style split navigation.
tags:
- ai
- llm
category: engineering
color: null
tools:
  bash: true
  read: true
  write: true
---
# Claude Code + Neovim via Ghostty Panes

Esta skill permite configurar o Ghostty para integrar a experiência do Neovim com o Claude Code em uma janela dividida, permitindo navegação estilo Vim entre os painéis (panes).

## Pré-requisitos
- Terminal Emulator: Ghostty
- Editor: Neovim
- Ferramenta CLI: Claude Code (`claude`)

## Procedimento de Configuração

### 1. Configurando Navegação no Ghostty
Para navegar entre os painéis do Ghostty como se estivesse usando as teclas do Vim (`h`, `j`, `k`, `l`), adicione as seguintes linhas ao seu arquivo de configuração do Ghostty (geralmente `~/.config/ghostty/config`):

```properties
# Ghostty Config: Navigate between panes (vim-style)
keybind = ctrl+h=goto_split:left
keybind = ctrl+j=goto_split:bottom
keybind = ctrl+k=goto_split:top
keybind = ctrl+l=goto_split:right
```

### 2. Fluxo de Trabalho Integrado

1. Abra o Ghostty no diretório do seu projeto.
2. Inicie o Neovim no painel principal: `nvim .`
3. Divida a tela do Ghostty horizontalmente ou verticalmente (usando os atalhos padrão do Ghostty, ex: `ctrl+shift+right` ou `ctrl+shift+down`).
4. No novo painel, inicie o Claude Code: `claude`
5. Use as teclas configuradas (`ctrl+h`, `ctrl+l`, etc.) para alternar rapidamente entre o código no Neovim e o assistente Claude Code.

### 3. Dicas de Navegação no Neovim
Dentro do Neovim, mantenha sua fluidez usando atalhos comuns:
- `SPACE-ff`: Encontrar arquivos (find files)
- `SPACE-bb`: Mover para o próximo buffer

## Referência
Extraído do vídeo: [Claude Code + Neovim via Ghostty Panes](https://www.youtube.com/watch?v=ysVmQ6mesWE)
