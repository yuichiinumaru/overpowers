#!/usr/bin/env bash
# =============================================================================
# create-symlinks.sh
# =============================================================================
# Common logic for symlinking or copying overpowers assets.
#
# Usage:
#   source scripts/utils/create-symlinks.sh
#   create_symlinks "/target/dir" "${SYMLINKS[@]}"
#
# Requirements:
#   Expects SYMLINKS array where each item is formatted as "source_path:target_name"
#   e.g. ("agents:agents" "skills:skills")
# =============================================================================

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Helpers if not already defined
type log_info &>/dev/null || log_info()  { echo -e "${GREEN}[✓]${NC} $*"; }
type log_warn &>/dev/null || log_warn()  { echo -e "${YELLOW}[!]${NC} $*"; }
type log_skip &>/dev/null || log_skip()  { echo -e "${CYAN}[~]${NC} $*"; }
type log_error &>/dev/null || log_error() { echo -e "${RED}[✗]${NC} $*"; }

create_symlinks() {
    if [[ $# -lt 2 ]]; then
        log_error "Usage: create_symlinks <target_dir> <mappings_array...>"
        return 1
    fi

    local target_dir="$1"
    shift
    local mappings=("$@")

    local repo_root
    # Assuming this script is correctly located in OVERPOWERS_ROOT/scripts/utils
    repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

    for mapping in "${mappings[@]}"; do
        local src_rel="${mapping%%:*}"
        local tgt_name="${mapping##*:}"

        local src_abs="${repo_root}/${src_rel}"
        local tgt_abs="${target_dir}/${tgt_name}"

        # Check if source exists
        if [[ ! -e "${src_abs}" ]]; then
            log_warn "Source not found: ${src_abs}. Skipping ${tgt_name}."
            continue
        fi

        # Ensure target's parent directory exists
        local parent_dir
        parent_dir="$(dirname "${tgt_abs}")"
        if [[ ! -d "${parent_dir}" ]]; then
            mkdir -p "${parent_dir}"
        fi

        # Remove existing symlink or warn about existing real dir
        if [[ -L "${tgt_abs}" ]]; then
            local current_target
            current_target="$(readlink -f "${tgt_abs}" 2>/dev/null || echo '<broken>')"
            if [[ "${current_target}" == "${src_abs}" ]]; then
                log_skip "${tgt_name} already points to the correct source. Skipping."
                continue
            fi
            log_warn "Removing stale symlink: ${tgt_abs} -> ${current_target}"
            rm "${tgt_abs}"
        elif [[ -e "${tgt_abs}" ]]; then
            if [[ "${OVERPOWERS_CONFLICT_POLICY:-replace}" == "copy" ]]; then
                if [[ -d "${src_abs}" ]]; then
                    log_info "Merging assets into existing directory: ${tgt_abs}"
                    mkdir -p "${tgt_abs}"
                    cp -rn "${src_abs}/"* "${tgt_abs}/" 2>/dev/null || true
                else
                    log_info "File already exists, skipping: ${tgt_abs}"
                fi
                continue
            else
                log_warn "${tgt_abs} exists as a real file/directory. Backing up to ${tgt_abs}.bak"
                mv "${tgt_abs}" "${tgt_abs}.bak"
            fi
        fi

        # Create symlink or copy
        if [[ "${OVERPOWERS_CONFLICT_POLICY:-replace}" == "copy" ]]; then
            cp -r "${src_abs}" "${tgt_abs}"
            log_info "${tgt_name} (copied) <- ${src_abs}"
        else
            ln -s "${src_abs}" "${tgt_abs}"
            log_info "${tgt_name} (symlinked) -> ${src_abs}"
        fi
    done
    return 0
}
