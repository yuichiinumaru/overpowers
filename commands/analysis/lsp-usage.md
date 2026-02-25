---
name: lsp-usage
description: "Instructions for using Language Server Protocol (LSP) tools via CLI wrappers or mcp-servers."
---

# LSP Usage Guide

To use LSP features in overpowers, use the `mcp-server-lsp` or equivalent CLI tools.

## Supported Operations

### Definition
Find where a symbol is defined.
\`\`\`bash
# If using a CLI wrapper
lsp-cli definition --file src/main.ts --line 10 --char 5
\`\`\`

### References
Find all usages of a symbol.
\`\`\`bash
lsp-cli references --file src/main.ts --line 10 --char 5
\`\`\`

### Diagnostics
Get compile-time errors.
\`\`\`bash
# Check entire project
tsc --noEmit  # TypeScript
cargo check   # Rust
go vet ./...  # Go
\`\`\`

## Agent Strategy
Since we don't have a persistent LSP process in the script runner:
1. Use **static analysis tools** (`grep`, `ast-grep`, `find`) for most searches.
2. Use **compiler checks** (`tsc`, `cargo`, `go`) for diagnostics.
3. Use **Librarian** agent for external documentation.
