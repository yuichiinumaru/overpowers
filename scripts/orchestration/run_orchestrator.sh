#!/bin/bash
export OPENCODE_PERMISSION='"allow"'

echo "Iniciando verificação de PRs e merge via jj..."
opencode run "Verifique se temos pull requests (ou branches) que precisam ser mergiados na branch atual do repositório jj. Se houver, faça o merge ou rebase deles utilizando o jujutsu (jj). Não se preocupe em enviar pro github, apenas integre o trabalho localmente." --agent git_workflow_manager > .agents/reports/logs_merge.txt 2>&1

echo "Merge finalizado. Iniciando tasks pendentes em paralelo..."

opencode run "Conclua a task 009 descrita em docs/tasks/009-rebuild-mcp-infrastructure.md." --agent build_engineer > .agents/reports/logs_009.txt 2>&1 &
opencode run "Conclua a task 010 descrita em docs/tasks/010-recreate-semgrep-skill.md." --agent security_auditor > .agents/reports/logs_010.txt 2>&1 &
opencode run "Conclua a task 011 descrita em docs/tasks/011-reinstall-nlm-skill.md." --agent bash_expert > .agents/reports/logs_011.txt 2>&1 &
opencode run "Conclua a task 012 descrita em docs/tasks/012-reorganize-docs-directory.md." --agent documentation_specialist > .agents/reports/logs_012.txt 2>&1 &
opencode run "Conclua a task 013 descrita em docs/tasks/013-install-script-ux.md." --agent bash_expert > .agents/reports/logs_013.txt 2>&1 &
opencode run "Conclua a task 014 descrita em docs/tasks/014-fix-antigravity-mcp-config.md." --agent bash_expert > .agents/reports/logs_014.txt 2>&1 &
opencode run "Conclua a task 015 descrita em docs/tasks/015-update-tasklist-from-audit.md." --agent agile_sprint_planner > .agents/reports/logs_015.txt 2>&1 &
opencode run "Conclua a task 016 descrita em docs/tasks/016-second-audit.md." --agent compliance_auditor > .agents/reports/logs_016.txt 2>&1 &

echo "Aguardando conclusão de todos os subagentes..."
wait

echo "Todas as tasks finalizadas!"
