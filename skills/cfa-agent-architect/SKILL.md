---
name: cfa-agent-architect
description: Habilidade mestre para projetar e validar novos agentes baseados na Cognitive Fusion Architecture (CFA).
---

# Skill: CFA Agent Architect

Esta habilidade é ativada quando o usuário solicita a criação, rascunho ou refatoração de um agente de IA no repositório. Ela garante que o assistente siga o rigor da constituição `AGENTS.md`.

## Procedimento de Escrita (Como usar)

### 1. Sabatina Abstrata (Fase I)
Sempre que detectar um desejo de criar um agente, não responda com código. 
- Analise o objetivo político/técnico.
- Proponha melhorias táticas de "Antifragilidade" e "Evasão de Script".
- Destaque o que falta no rascunho para que ele seja "Elite".

### 2. Design de KBs (Fase II)
Divida o cérebro do agente em módulos:
- **Herdados:** KBs fundamentais de raciocínio.
- **Exclusivos:** Dicionários de domínio e contratos de dados.

### 3. Escrita de System Prompt (Fase III/IV)
Garante que o JSON do agente contenha:
- `inner_monologue` obrigatório.
- `extraction_goals` em vez de perguntas fixas.
- `validation_gates` para evitar o "Lero-Lero".

## Exemplos de Gatilho
- "Quero fazer um agente para X..."
- "Analise este draft de prompt..."
- "Como estruturo o conhecimento de Y?"

---
**Dica Pro:** Sempre consulte o `Knowledge` para ver se já existe um `kb_` que resolva parte do problema de domínio do usuário.
