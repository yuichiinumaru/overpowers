# Task 0040: Ops Add Post-Install Validation

**Type:** Operations / Infrastructure  
**Priority:** MEDIUM  
**Status:** Pending  
**Created:** 2026-03-16  
**Author:** Omega Agent  
**Parent:** Install Scripts Analysis Improvements  

---

## Objective

Add comprehensive post-installation validation to verify all installations completed successfully and provide actionable error messages.

---

## Problem

Currently, no validation occurs after installation:
- Symlinks not verified after creation
- MCP configs not validated for JSON syntax
- No smoke tests for deployed agents/skills
- Users discover issues only when using platforms

---

## Acceptance Criteria

- [ ] Create `verify_deployment()` function in deploy-utils.sh
- [ ] Validate all symlinks point to existing targets
- [ ] Validate JSON/TOML configs are syntactically correct
- [ ] Test MCP server availability (optional)
- [ ] Generate validation report
- [ ] Provide fix suggestions for common issues
- [ ] Add `--verify-only` flag to install.sh

---

## Implementation

### Validation Function
```bash
verify_deployment() {
    local platform="$1"
    local errors=0
    
    log_info "Validating ${platform} deployment..."
    
    # Check symlinks
    for link in "${PLATFORM_DIR}"/*; do
        if [[ -L "${link}" ]]; then
            if [[ ! -e "${link}" ]]; then
                log_error "Broken symlink: ${link}"
                ((errors++))
            fi
        fi
    done
    
    # Validate JSON configs
    for json_file in "${PLATFORM_DIR}"/*.json; do
        if ! python3 -m json.tool "${json_file}" > /dev/null 2>&1; then
            log_error "Invalid JSON: ${json_file}"
            ((errors++))
        fi
    done
    
    # Validate TOML configs
    for toml_file in "${PLATFORM_DIR}"/*.toml; do
        if ! python3 -c "import tomllib; tomllib.load(open('${toml_file}'))" 2>/dev/null; then
            log_error "Invalid TOML: ${toml_file}"
            ((errors++))
        fi
    done
    
    if [[ ${errors} -gt 0 ]]; then
        log_error "Validation failed with ${errors} error(s)"
        print_fix_suggestions
        return 1
    fi
    
    log_info "Validation passed!"
    return 0
}

print_fix_suggestions() {
    echo ""
    echo -e "${YELLOW}Common fixes:${NC}"
    echo "  1. Check repo integrity: git status"
    echo "  2. Re-run install: ./install.sh"
    echo "  3. Check permissions: ls -la ~/.config/opencode"
    echo ""
}
```

---

## Integration Points

- [ ] Call at end of `install.sh`
- [ ] Call at end of each `deploy-to-*.sh`
- [ ] Call at end of `install-mcps.sh`
- [ ] Add standalone `verify-install.sh` script

---

## Validation Report Format

```
════════════════════════════════════════
  Installation Validation Report
════════════════════════════════════════

Platform: OpenCode
Status: ✅ PASSED

Checks:
  [✓] Symlinks valid (5/5)
  [✓] JSON configs valid (2/2)
  [✓] TOML configs valid (1/1)
  [✓] MCP servers configured (3/3)

Platform: Gemini CLI
Status: ⚠️ WARNINGS

Checks:
  [✓] Symlinks valid (4/4)
  [⚠] JSON configs valid (1/2) - 1 warning
  [✓] TOML configs valid (0/0)
  [✓] MCP servers configured (2/2)

Warnings:
  - ~/.gemini/settings.json: Unknown key "experimental.enableAgents"
    (This is expected for older Gemini CLI versions)

════════════════════════════════════════
```

---

## Dependencies

- Task 0037: Centralize Platform Paths
- Task 0039: Standardize Error Handling

---

**Estimated Effort:** 4 hours  
**Assigned To:** Unassigned
