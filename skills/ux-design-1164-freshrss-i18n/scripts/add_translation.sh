#!/bin/bash

# Helper to add translation in FreshRSS
KEY=$1
VALUE=$2

if [ -z "$KEY" ] || [ -z "$VALUE" ]; then
    echo "Usage: ./add_translation.sh <key> <value>"
    echo "Example: ./add_translation.sh gen.action.my_new_button 'My New Button'"
    exit 1
fi

if [ ! -f "cli/manipulate.translation.php" ]; then
    echo "Error: cli/manipulate.translation.php not found. Are you in the FreshRSS root directory?"
    exit 1
fi

php cli/manipulate.translation.php -a add -k "$KEY" -v "$VALUE"
echo "Added translation key '$KEY' with value '$VALUE'"
