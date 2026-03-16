---
name: ast-grep
description: Structural code search, linting, and rewriting tool based on Abstract Syntax Trees (AST).
tags: [coding, analysis, refactoring, linting, ast, structural-search]
version: 1.0.0
category: coding
subtype: review
---

# ast-grep (sg)

`ast-grep` is a fast, polyglot tool for structural code search, linting, and rewriting. Unlike text-based tools like `grep` or `sed`, `ast-grep` understands code syntax by operating on the Abstract Syntax Tree (AST), enabling precise refactoring and deep code analysis.

## Key Features

- **Isomorphic Patterns:** Write search patterns using the same syntax as the code you're searching for.
- **Structural Wildcards:** Use `$` followed by uppercase letters (e.g., `$A`, `$MATCH`) to match any single AST node.
- **High Performance:** Written in Rust and powered by tree-sitter for multi-threaded, blazing-fast execution.
- **Polyglot:** Supports 20+ languages including TypeScript, Python, Rust, Go, Java, and C++.
- **Interactive Mode:** Review and apply changes one by one with a batteries-included CLI experience.
- **YAML-based Linting:** Define complex, persistent rules for large-scale codebase maintenance.

## CLI Usage

The primary command is `ast-grep` or its alias `sg`.

### Basic Search and Rewrite

```bash
# Search for a pattern
sg --pattern 'console.log($MESSAGE)' --lang ts

# Rewrite code using wildcards
sg --pattern '$A && $A()' --rewrite '$A?.()' --lang ts

# Inline replacement with specific language
ast-grep -p 'var $VAR = $VAL' -r 'let $VAR = $VAL' -l js
```

### Common Flags

- `-p, --pattern`: The structure to find.
- `-r, --rewrite`: The replacement structure.
- `-l, --lang`: Target language extension.
- `-i, --interactive`: Interactively review each match before applying changes.
- `-u, --update-all`: Apply all changes without confirmation.
- `scan`: Run as a linter using rules defined in `sgconfig.yml`.

## Configuration & Rules

Rules are defined in YAML files, allowing for sophisticated logic using relational selectors like `inside`, `has`, `precedes`, etc.

### Example Rule ( Conceptual)

```yaml
id: no-unused-result
message: The result of $FUNC() is ignored.
severity: warning
language: rust
rule:
  pattern: $FUNC()
  not:
    inside:
      kind: let_declaration
```

## Installation

```bash
# Via Cargo (Rust)
cargo install ast-grep --locked

# Via NPM
npm install -g @ast-grep/cli

# Via Homebrew (macOS)
brew install ast-grep
```

## Vision

`ast-grep` bridges the gap between simple text search and complex compiler-based tools, giving developers a powerful yet accessible way to maintain and evolve large-scale codebases with surgical precision.
