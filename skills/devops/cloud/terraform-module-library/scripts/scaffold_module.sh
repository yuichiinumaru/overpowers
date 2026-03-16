#!/bin/bash
MODULE=$1
if [ -z "$MODULE" ]; then
    echo "Usage: $0 <module-name>"
else
    echo "Scaffolding Terraform module: $MODULE"
    mkdir -p "$MODULE"
    touch "$MODULE/main.tf" "$MODULE/variables.tf" "$MODULE/outputs.tf" "$MODULE/README.md"
    echo "Done."
fi
