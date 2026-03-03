# Tracker Journal

## Ignored Paths
- node_modules/
- dist/
- build/
- .git/
- .next/
- coverage/
- htmlcov/
- *.egg-info/
- __pycache__/
- packages/legacy/ (Assimilated legacy code, low priority)

## Context
- **2025-05-25**: Initial audit. Found mock data in AgentWise and hardcoded init in WS-MCP. Created tasks 074 and 075.
- **Packages Scanned**: Focused on `packages/` and `services/`.
- **Known Issues**:
  - `packages/khala/khala/kernel/cognition/graph/retriever.py` has a potential N+1 query pattern but seems optimized for now. Monitor if dataset grows.
