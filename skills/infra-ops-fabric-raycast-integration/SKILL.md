---
name: fabric-raycast-integration
description: Integrates Fabric commands directly into Raycast for rapid, unified access
  to AI scripts and workflows from the macOS Spotlight alternative.
tags:
- infra
- ops
category: productivity
color: null
tools:
  bash: true
  read: true
version: 1.0.0
---
# Fabric Integration with Raycast

Esta skill permite conectar o Fabric ao Raycast, permitindo que você dispare scripts e utilitários do Fabric nativamente através da interface do Raycast.

## Pré-requisitos
- macOS
- [Raycast](https://www.raycast.com/) instalado
- [Fabric](https://github.com/danielmiessler/fabric) instalado e configurado

## Procedimento de Integração

1. **Localizar os Scripts do Fabric:** Identifique o diretório onde o Fabric armazena seus padrões (patterns) ou scripts bash auxiliares. Geralmente localizado em `~/.config/fabric/patterns/` ou similar.
2. **Configurar Raycast Script Commands:**
   - Abra o Raycast e vá em `Settings > Extensions > Script Commands`.
   - Clique em `Add Directory` e aponte para o diretório de scripts do Fabric.
3. **Formatação de Scripts:**
   - Para que o Raycast reconheça os scripts do Fabric corretamente, eles precisam conter os cabeçalhos de metadados padrão do Raycast (ex: `@raycast.title`, `@raycast.mode`).
   - Você pode precisar criar wrappers (scripts intermediários) que chamem o comando do Fabric desejado e o formatem para o Raycast.

## Possível Aprimoramento
Uma abordagem mais integrada é hospedar um conjunto de scripts bash específicos para o Raycast *dentro* do diretório do Fabric. Isso permite que você simplesmente aponte o Raycast para esse diretório e herde instantaneamente todos os atalhos sem precisar configurar wrappers individualmente.

## Referência
Extraído do vídeo: [Fabric New Integration with Raycast](https://www.youtube.com/watch?v=iWFGuhRLvQA)
