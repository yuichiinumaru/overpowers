# Task 0039: Ops Standardize Error Handling

**Type:** Operations / Infrastructure  
**Priority:** MEDIUM  
**Status:** Pending  
**Created:** 2026-03-16  
**Author:** Omega Agent  
**Parent:** Install Scripts Analysis Improvements  

---

## Objective

Standardize error handling across all scripts with consistent `set` flags, trap handlers, and error reporting.

---

## Problem

Inconsistent error handling:
- Some scripts use `set -euo pipefail`, others don't
- No cleanup on failure (partial installs remain)
- Silent failures in some scripts
- No error codes or structured error messages

---

## Acceptance Criteria

- [ ] All scripts use `set -euo pipefail`
- [ ] All scripts have trap handlers for cleanup
- [ ] Consistent error message format
- [ ] Error codes for different failure types
- [ ] Rollback on critical failures
- [ ] Error logging to file for debugging

---

## Implementation Standard

### Required Header
```bash
#!/usr/bin/env bash
set -euo pipefail  # Exit on error, undefined vars, pipe failures

# Trap for cleanup
cleanup() {
    local exit_code=$?
    if [[ ${exit_code} -ne 0 ]]; then
        log_error "Script failed with exit code ${exit_code}"
        # Add rollback logic here
    fi
    exit ${exit_code}
}
trap cleanup EXIT
```

### Error Function
```bash
log_error() {
    echo -e "${RED}[ERROR]${NC} $*" >&2
    echo "$(date '+%Y-%m-%d %H:%M:%S') [ERROR] $*" >> "${LOG_FILE:-/dev/null}"
}
```

### Error Codes
```bash
readonly ERR_OK=0
readonly ERR_GENERAL=1
readonly ERR_MISSING_DEPS=2
readonly ERR_PERMISSION=3
readonly ERR_VALIDATION=4
readonly ERR_ROLLBACK=5
```

---

## Scripts to Update

### Priority 1 (Critical - Install/Uninstall)
- [ ] `install.sh`
- [ ] `uninstall.sh` (when created)
- [ ] `install-mcps.sh`
- [ ] `uninstall-mcps.sh` (when created)

### Priority 2 (Deploy Scripts)
- [ ] All 10 `deploy-to-*.sh` scripts
- [ ] All 10 `uninstall-from-*.sh` scripts (when created)

### Priority 3 (Utilities)
- [ ] `install-plugins.sh`
- [ ] `setup-*.sh` scripts (top 5 most used)

---

## Testing

- [ ] Test error propagation
- [ ] Test cleanup on failure
- [ ] Test rollback functionality
- [ ] Test error logging

---

## Dependencies

- Task 0037: Centralize Platform Paths (recommended)
- Task 0036: Uninstall Scripts Implementation

---

**Estimated Effort:** 6 hours  
**Assigned To:** Unassigned
