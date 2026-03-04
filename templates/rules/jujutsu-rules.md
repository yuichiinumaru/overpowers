# Regras do Jujutsu (Resolvimento de Conflitos e Controle de Versão)
Este protocolo instrui como tratar conflitos de código utilizando Jujutsu VCS, otimizado para o cenário de agentes operando massivamente em paralelo.

## 1. Merging & Sincronização Harmoniosa (jj)
- **Merge com o Jujutsu**: Sempre priorize utilizar a skill de `harmonious-jujutsu-merge` através do OpenCode/Moltbot ou o comando nativo `jj merge` para resolução de conflitos originados dos múltiplos PRs dos agentes Jules.
- **Vantagem Concorrente**: O Jujutsu lida com ramificações simultâneas de múltiplos agentes e modificações conflitantes ordens de magnitude melhor que os *octopus merges* do Git padrão. Ele preserva nativamente a estrutura do código durante conflitos sem injetar "conflict markers" textuais (`<<<<<<< HEAD`) da mesma forma restritiva que o Git tradicional.

## 2. Delegação em Fluxos de Auto-Merge
- Em fluxogramas e scripts de Auto-Merge (ex: `scripts/auto_merge_mothership.sh`), utilizar o `gh pr merge` é válido apenas na "Happy Path" (quando não há conflitos).
- Assim que o GitHub alertar sobre conflito no CLI para o merge, o **fallback essencial** é engatilhar a ferramenta via linha de comando requisitando que um Especialista em Jujutsu realize o merge de forma graciosa sem expor marcadores do git na source code final, integrando a branch do PR diretamente para `staging`.

## 3. Prevenção e Cleanup
- Operações de merge via Jujutsu em scripts devem ser seguidas de cleanup (`git branch -D` e exclusão remota da branch da feature unida) para manter a repolight.
- Certifique-se de que nenhum artefato isolado nas workspaces virtuais do Jujutsu escape do isolamento e pare no branch principal se não estiver resolvido.
