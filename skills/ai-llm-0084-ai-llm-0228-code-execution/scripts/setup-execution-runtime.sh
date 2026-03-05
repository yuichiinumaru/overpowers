#!/bin/bash

SETUP_SCRIPT="$HOME/.claude/plugins/marketplaces/mhattingpete-claude-skills/execution-runtime/setup.sh"

if [ -f "$SETUP_SCRIPT" ]; then
    echo "Running official setup script..."
    bash "$SETUP_SCRIPT"
else
    echo "Official setup script not found. Creating mock execution_runtime.py for development..."
    
    cat <<EOF > execution_runtime.py
class Filesystem:
    def copy_lines(self, path, start, end): return f"Mock lines from {path}"
    def paste_code(self, path, line, code): print(f"Mock paste to {path}")
    def search_replace(self, path, old, new): return 1

class CodeAnalysis:
    def find_functions(self, path, pattern=None): return []
    def analyze_dependencies(self, path): return {"complexity": 0}

class Transformations:
    def rename_identifier(self, root, old, new, pattern): return {"files_modified": 0}

class Git:
    def git_status(self): return ""
    def git_add(self, files): pass
    def git_commit(self, msg): pass

fs = Filesystem()
code = CodeAnalysis()
transform = Transformations()
git = Git()
EOF
    echo "Mock execution_runtime.py created."
fi
