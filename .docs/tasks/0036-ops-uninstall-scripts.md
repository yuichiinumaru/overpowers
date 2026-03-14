# Task 0036: Ops Uninstall Scripts Implementation

**Type:** Operations / Infrastructure  
**Priority:** CRITICAL  
**Status:** In Progress  
**Created:** 2026-03-16  
**Author:** Omega Agent  
**Subtasks:** 15 platform-specific implementations  

---

## Objective

Create a comprehensive uninstall system that safely reverses all Overpowers installation actions, sharing core logic with existing install scripts (DRY principle) and supporting dry-run mode, backups, and audit logging.

---

## Subtasks

### Phase 1: Foundation
- [x] 0036.1: Create `scripts/utils/uninstall-utils.sh` with core functions
- [ ] 0036.2: Create backup directory structure and retention policy
- [ ] 0036.3: Write unit tests for utility functions

### Phase 2: Platform Uninstall Scripts
- [ ] 0036.4: `uninstall-from-opencode.sh` (reference implementation)
- [ ] 0036.5: `uninstall-from-gemini.sh`
- [ ] 0036.6: `uninstall-from-antigravity.sh`
- [ ] 0036.7: `uninstall-from-kilo.sh`
- [ ] 0036.8: `uninstall-from-cursor.sh`
- [ ] 0036.9: `uninstall-from-windsurf.sh`
- [ ] 0036.10: `uninstall-from-claude-code.sh`
- [ ] 0036.11: `uninstall-from-codex.sh`
- [ ] 0036.12: `uninstall-from-factory.sh`
- [ ] 0036.13: `uninstall-from-qwen.sh`

### Phase 3: MCP & Plugin Uninstall
- [ ] 0036.14: `uninstall-mcps.sh`
- [ ] 0036.15: `uninstall-plugins.sh`
- [ ] 0036.16: `uninstall-personas.sh`

### Phase 4: Master Orchestrator
- [ ] 0036.17: `uninstall.sh` (master script)
- [ ] 0036.18: Integration testing
- [ ] 0036.19: Documentation
- [ ] 0036.20: User acceptance testing

---

## Problem Statement

Currently, Overpowers has:
- ✅ 28 install-related scripts
- ✅ 20 deploy scripts  
- ✅ 53 setup scripts
- ❌ **ZERO uninstall mechanisms**

Users cannot cleanly remove Overpowers without manual intervention, risking:
- Orphaned symlinks in platform configs
- Leftover MCP server entries
- Polluted environment variables
- Broken configurations

---

## Acceptance Criteria

### Must Have (MVP)
- [ ] `uninstall.sh` master orchestrator with platform selection
- [ ] Platform-specific uninstall scripts for all 10 platforms
- [ ] `uninstall-mcps.sh` for MCP server removal
- [ ] Mandatory backup creation before any removal
- [ ] `--dry-run` flag support across all scripts
- [ ] Comprehensive logging with timestamps
- [ ] Verification of all removals
- [ ] Restore capability from backups

### Should Have
- [ ] `uninstall-plugins.sh` for plugin cleanup
- [ ] Transaction-like rollback on failure
- [ ] Progress indicators for long operations
- [ ] Summary report of what was removed
- [ ] Conflict policy (backup vs remove vs abort)

### Nice to Have
- [ ] `--restore` flag to undo uninstall
- [ ] Selective uninstall (remove only specific components)
- [ ] Interactive mode with granular control
- [ ] Uninstall analytics (opt-in)

---

## Implementation Checklist

### Phase 1: Foundation (Estimated: 6 hours)
- [ ] Create `scripts/utils/uninstall-utils.sh`
  - [ ] `backup_before_remove()` function
  - [ ] `remove_symlink()` function
  - [ ] `verify_removal()` function
  - [ ] `log_dry()` for dry-run logging
  - [ ] `restore_from_backup()` function
- [ ] Create backup directory structure
- [ ] Implement backup retention policy (e.g., keep last 5 backups)
- [ ] Write unit tests for utility functions

### Phase 2: Platform Uninstalls (Estimated: 15 hours)
- [ ] `scripts/uninstall-from-opencode.sh` (reference implementation)
- [ ] `scripts/uninstall-from-gemini.sh`
- [ ] `scripts/uninstall-from-antigravity.sh`
- [ ] `scripts/uninstall-from-kilo.sh`
- [ ] `scripts/uninstall-from-cursor.sh`
- [ ] `scripts/uninstall-from-windsurf.sh`
- [ ] `scripts/uninstall-from-claude-code.sh`
- [ ] `scripts/uninstall-from-codex.sh`
- [ ] `scripts/uninstall-from-factory.sh`
- [ ] `scripts/uninstall-from-qwen.sh`

**Each script must:**
- [ ] Source `uninstall-utils.sh` and `deploy-utils.sh`
- [ ] Support `--dry-run` flag
- [ ] Backup before removal
- [ ] Remove only Overpowers-installed items
- [ ] Verify removals
- [ ] Print summary

### Phase 3: MCP & Plugin Uninstall (Estimated: 8 hours)
- [ ] `scripts/uninstall-mcps.sh`
  - [ ] Remove only Overpowers MCPs (preserve user MCPs)
  - [ ] Support all 10 platforms
  - [ ] Handle JSON and TOML configs
- [ ] `scripts/uninstall-plugins.sh`
  - [ ] Remove plugins installed via `install-plugins.sh`
  - [ ] Clean up opencode.json entries
- [ ] `scripts/uninstall-personas.sh`

### Phase 4: Master Orchestrator (Estimated: 6 hours)
- [ ] `uninstall.sh` (root directory)
  - [ ] Platform detection (mirror install.sh)
  - [ ] Platform selection UI (gum or fallback)
  - [ ] Conflict policy selection
  - [ ] Phase orchestration (backup → MCPs → symlinks → cleanup)
  - [ ] Final summary with restore instructions
- [ ] Integration testing across all platforms
- [ ] Edge case handling (partial installs, missing files, etc.)

### Phase 5: Documentation & Testing (Estimated: 5 hours)
- [ ] User documentation (README section)
- [ ] Developer documentation (how to extend)
- [ ] Test scenarios:
  - [ ] Fresh install → uninstall (clean state)
  - [ ] Partial install → uninstall (error recovery)
  - [ ] Reinstall after uninstall (no残留)
  - [ ] Dry-run accuracy test
  - [ ] Backup/restore cycle
- [ ] CI/CD integration (automated uninstall test)

---

## Technical Specifications

### Backup Naming Convention
```bash
{item}.overpowers-backup.{YYYYMMDD-HHMMSS}.{type}
# Examples:
agents.overpowers-backup.20260316-143022.symlink
skills.overpowers-backup.20260316-143022.directory
opencode.json.overpowers-backup.20260316-143022.file
```

### Backup Retention
- Keep last 5 backups per item type
- Auto-cleanup on successful uninstall + 7 days

### Dry-Run Output
```bash
[DRY-RUN] Would: Remove symlink /home/user/.config/opencode/agents
[DRY-RUN] Would: Backup /home/user/.config/opencode/skills
[DRY-RUN] Would: Remove MCP entry "serena" from opencode.json
```

### Log Format
```bash
2026-03-16 14:30:22 [INFO] Starting uninstall for platform: OpenCode
2026-03-16 14:30:23 [BACKUP] Created backup: skills.overpowers-backup.20260316-143023
2026-03-16 14:30:24 [REMOVE] Removed symlink: /home/user/.config/opencode/agents
2026-03-16 14:30:25 [VERIFY] Verified removal: /home/user/.config/opencode/agents
```

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Accidental user data loss | LOW | CRITICAL | Mandatory backups, verify before remove, only remove known Overpowers items |
| Partial uninstall leaves broken state | MEDIUM | HIGH | Transaction-like rollback, state validation at each step |
| User MCPs removed | LOW | MEDIUM | Track installed MCPs during install, only remove tracked entries |
| Symlinks point to wrong targets | LOW | MEDIUM | Validate symlink targets before removal, log mismatches |
| Permissions prevent removal | MEDIUM | LOW | Pre-flight permission check, clear error messages |
| Backup disk space exhaustion | LOW | LOW | Retention policy (keep last 5), compression for large backups |

---

## Dependencies

### Internal
- `scripts/utils/deploy-utils.sh` (reuse colors, logging, platform detection)
- `scripts/utils/create-symlinks.sh` (understand symlink creation for reversal)
- `scripts/install-mcps.sh` (understand MCP installation for clean removal)

### External
- None (pure bash + Python for JSON/TOML manipulation)

---

## Success Metrics

- ✅ All 10 platforms supported
- ✅ 100% reversal of install actions
- ✅ Zero user data loss in testing
- ✅ Dry-run accuracy > 99%
- ✅ Backup success rate 100%
- ✅ User documentation complete
- ✅ All test scenarios pass

---

## Related Documents

- **Planning Document:** `.docs/tasks/planning/install-scripts-analysis.md`
- **Install Script:** `install.sh`
- **Deploy Utils:** `scripts/utils/deploy-utils.sh`
- **MCP Installer:** `scripts/install-mcps.sh`

---

## Notes

### Design Decisions

1. **Why separate scripts per platform?**
   - Mirrors install structure for maintainability
   - Allows independent testing
   - Easier to debug platform-specific issues

2. **Why mandatory backups?**
   - Safety first - users can recover from mistakes
   - Enables `--restore` functionality
   - Builds trust in the uninstall process

3. **Why dry-run first?**
   - Users can audit before committing
   - Helps identify issues early
   - Educational value (understand what will change)

4. **Why not use existing package managers?**
   - Overpowers is a meta-layer across multiple platforms
   - No single package manager supports all 10 platforms
   - Custom solution allows fine-grained control

### Future Enhancements (Post-MVP)

- Snapshot-based rollback (integration with Timeshift/snapper)
- Remote uninstall (for enterprise deployments)
- Uninstall analytics (opt-in, privacy-preserving)
- Migration mode (uninstall from platform A, install to platform B)

---

**Estimated Total Effort:** 40 hours  
**Sprint Allocation:** 2 sprints (20 hours/sprint)  
**Assigned To:** Unassigned  
**Review Date:** After implementation complete
