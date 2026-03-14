# Technical Design: Graceful Degradation Fallbacks

## 1. Arquitetura (Architecture)
O padrão de Degradação Graciosa (Graceful Degradation) deve ser implementado no nível dos conectores/wrappers (ex: Python scripts em `scripts/` e bash scripts de subagents).

## 2. Componentes e Mudanças (Components & Changes)
- **`scripts/utils/model_selector.py`**: Aprimorar para sempre retornar um modelo válido, mesmo que seja o mais básico (fallback of last resort).
- **Tratamento de Exceções**: Em scripts Python que fazem requisições para LLMs (usando requests, httpx, ou clientes de APIs específicas), envolver as chamadas em blocos `try-except`. Se um `Timeout` ou `RateLimitError` for capturado, o script deve invocar uma função de fallback. Se todos falharem, retornar um JSON `{ "error": "All models exhausted", "status": "degraded", "partial_results": ... }` para não quebrar o parser (stdout).
- **Circuit Breaker**: Introduzir lógicas leves de circuit breaker. Se um modelo falha repetidamente em um curto intervalo de tempo, o script o marca como indisponível para aquela sessão de fallback.

## 3. Testes (Testing Strategy)
- Adicionar um script de teste simulado `tests/test_graceful_degradation.py` que intencionalmente emula falhas de rede (`mocker.patch`) nas chamadas LLM.
- Verificar se o script Python processa o erro e retorna o status `degraded` em vez de abortar o processo com status de saída `1` (ou não-zero não tratado).
