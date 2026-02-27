---
name: youtube-skill-creator
description: Analisa vídeos do YouTube sequencialmente para identificar oportunidades de criação ou atualização de skills de agentes. Use para minerar procedimentos úteis de canais de tecnologia, tutoriais e documentações em vídeo.
---

# YouTube Skill Creator

Esta skill orienta o agente na análise de uma lista de vídeos do YouTube para extrair procedimentos operacionais que podem ser transformados em skills reutilizáveis.

## Fluxo de Trabalho

### 1. Preparação
Receba uma lista de URLs de vídeos (geralmente extraída pela skill `youtube-link-extractor`). O agente deve processar de 2 a 5 vídeos por vez para manter o foco e a qualidade da análise.

### 2. Análise Sequencial
Para cada vídeo na lista:
- **Assistir/Transcrever:** Use ferramentas de navegação ou transcrição para entender o conteúdo.
- **Identificar Procedimentos:** Procure por fluxos de trabalho com início, meio e fim claros ("como fazer").
- **Aplicar Scorecard:** Use os critérios em `references/skill_scorecard.md` para pontuar a viabilidade da skill (0-2 por item).

### 3. Documentação
Para cada oportunidade identificada, preencha o template em `templates/video_analysis_report.md`.
- **Criar Skill:** Se o workflow for novo e tiver alto ROI (Total >= 15).
- **Atualizar Skill:** Se o vídeo trouxer melhorias de confiabilidade, novos edge cases ou guardrails para uma skill já existente no repositório.

### 4. Consolidação
Após analisar o lote de vídeos, apresente um resumo das melhores oportunidades encontradas e sugira os próximos passos para a implementação das novas skills.

## Recursos Inclusos

- `references/skill_scorecard.md`: Critérios universais para avaliar se um procedimento deve virar uma skill.
- `templates/video_analysis_report.md`: Modelo de relatório para documentar cada oportunidade de skill encontrada.

## Melhores Práticas

- **Foco no "Como":** Ignore opiniões ou inspirações gerais; foque em receitas operacionais e passos técnicos.
- **ROI:** Priorize skills que automatizam tarefas frequentes ou que reduzem drasticamente o risco de erros em processos complexos.
- **Iteração:** Se um vídeo sozinho não for suficiente, anote a ideia e aguarde até que outros vídeos complementem o material necessário para uma skill robusta.
