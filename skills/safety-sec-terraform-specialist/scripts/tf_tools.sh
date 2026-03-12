#!/bin/bash
# tf_tools.sh
# Utility script for common Terraform/OpenTofu operations

COMMAND="terraform"
if command -v tofu &> /dev/null; then
    COMMAND="tofu"
fi

function show_help {
    echo "Usage: ./tf_tools.sh [command] [dir]"
    echo ""
    echo "Commands:"
    echo "  fmt       Format all .tf files recursively"
    echo "  validate  Run 'init -backend=false' and 'validate' in the directory"
    echo "  docs      Generate module documentation using terraform-docs (must be installed)"
    echo "  sec       Run security scan using tfsec or checkov (must be installed)"
    echo ""
}

CMD=$1
TARGET_DIR=${2:-.}

if [ -z "$CMD" ]; then
    show_help
    exit 1
fi

case "$CMD" in
    fmt)
        echo "Formatting $TARGET_DIR using $COMMAND..."
        $COMMAND fmt -recursive "$TARGET_DIR"
        ;;
    validate)
        echo "Validating $TARGET_DIR using $COMMAND..."
        cd "$TARGET_DIR" || exit 1
        $COMMAND init -backend=false
        $COMMAND validate
        ;;
    docs)
        if ! command -v terraform-docs &> /dev/null; then
            echo "Error: terraform-docs is not installed."
            exit 1
        fi
        echo "Generating docs for $TARGET_DIR..."
        terraform-docs markdown table --output-file README.md --output-mode inject "$TARGET_DIR"
        ;;
    sec)
        if command -v tfsec &> /dev/null; then
            echo "Running tfsec in $TARGET_DIR..."
            tfsec "$TARGET_DIR"
        elif command -v checkov &> /dev/null; then
            echo "Running checkov in $TARGET_DIR..."
            checkov -d "$TARGET_DIR"
        else
            echo "Error: Neither tfsec nor checkov is installed."
            exit 1
        fi
        ;;
    *)
        show_help
        exit 1
        ;;
esac
