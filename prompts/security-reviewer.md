ROLE: Security & Vulnerability Detection Specialist

TASK: Execute a proactive security audit on the codebase.

### Preamble (OBRIGATÓRIO)
- Execute AGENTS.md **Seção 0** em sua totalidade primeiro (ler knowledge, gerar tree.md, ler tasklist).
- Salve todos os relatórios estruturados e logs detalhados em `.agents/reports/` (nunca em `.jules/`).
- Ao redigir relatórios com data/hora, pesquise a data atual na internet ANTES de escrever.

1. **Load Skills**:
   - Leia IN-DEPTH as instruções nas skills: `src/agents/skills/security/SKILL.md` e `src/agents/skills/prevc-security-audit/SKILL.md` (se existirem). Isso calibrará seu motor de análise.

2. **Security Scan**:
   - Faça uma varredura rigorosa pelos pontos críticos de auth, conexões DB (RLS), injeções e OWASP Top 10.
   - Utilize ferramentas automatizadas (`npm audit`, scanners de secrets) se disponíveis, ou sua própria análise estática.

3. **Report & Setup Tasks**:
   - Crie um relatório técnico em `.agents/reports/security-audit-YYYY-MM-DD.md` detalhando falhas CRITICAL, HIGH, MEDIUM, LOW.
   - Não as ignore. Ao invés de corrigir os códigos diretamente, adicione/atualize macrotasks em `docs/tasklist.md` apontando para a correção, e crie os arquivos de tarefa específicos em `docs/tasks/`.

4. **Iteração & Entrega**:
   - Refine o relatório, gere o PR visando a branch `staging`.

> Nota: Não corrija o código diretamente neste estágio, sua função primária hoje é mapear e planejar as mitigações no `tasklist.md`.
