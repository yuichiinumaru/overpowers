# Feature Plan: Graceful Degradation Fallbacks

## 1. Visão de Produto
**Objetivo:** Aumentar a resiliência do toolkit Overpowers garantindo que falhas em serviços externos, limites de taxa (rate limits) de API e timeouts resultem em degradação graciosa em vez de quebra completa do sistema.

**Problema:** Atualmente, scripts e skills dependem excessivamente de chamadas de API bem-sucedidas. Falhas frequentemente levam a crashes, forçando a interrupção da automação e intervenção manual do usuário. 

**Solução:** Implementar um padrão de "Graceful Degradation" (Degradação Graciosa) que permita que agentes e scripts usem modelos alternativos (fallbacks), retornem resultados parciais, e capturem erros estruturados que possam ser compreendidos por agentes superiores.

## 2. Requisitos (Requirements)
- [ ] Escanear scripts em `scripts/` e `skills/` para identificar chamadas de rede sem blocos de fallback.
- [ ] Padronizar a interface de erro e resposta degradada em chamadas de LLM.
- [ ] Criar ou aprimorar wrappers de chamada que implementem a lógica de "circuit breaker" ou fallback para LLMs de menor custo/raciocínio se o principal falhar.
- [ ] Garantir documentação em `AGENTS.md` ou `.docs/` sobre o padrão.

## 3. Critérios de Aceitação (Success Criteria)
- Testes ou invocações de fallback simulando indisponibilidade do LLM principal não quebram o fluxo, mas delegam o trabalho para o modelo substituto ou retornam um JSON de erro interpretável.
- Pelo menos os scripts chave do sistema de subagents estão adequados a este modelo.
