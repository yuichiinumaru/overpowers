#!/bin/bash

# I18N Helper
# Requirement: pnpm and lingui

usage() {
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  extract    Extract new messages from source code"
    echo "  compile    Regenerate compiled catalogs"
    echo "  check      Verify translations (missing translations and key=translation check)"
    echo ""
}

case "$1" in
    extract)
        echo "Extracting messages..."
        pnpm lingui:extract
        ;;
    compile)
        echo "Compiling catalogs..."
        pnpm lingui:compile
        ;;
    check)
        echo "Running translation checks..."
        /home/sephiroth/Work/overpowers/scripts/lingui-check.sh
        /home/sephiroth/Work/overpowers/scripts/i18n-check-key-equals-translation.sh
        ;;
    *)
        usage
        exit 1
        ;;
esac
