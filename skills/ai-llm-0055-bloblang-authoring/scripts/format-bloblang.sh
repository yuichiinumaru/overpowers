#!/bin/bash

# Generates category-organized XML reference files
# This is a placeholder for the actual Bloblang documentation generator
DIR=$(mktemp -d -t bloblang-refs-XXXXXX)
echo "Generating Bloblang references in $DIR"
# Mock generation
touch "$DIR/functions-General.xml"
touch "$DIR/methods-General.xml"
echo "BLOBLREF_DIR=$DIR"
