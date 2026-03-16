#!/bin/bash

GHOSTTY_CONFIG="$HOME/.config/ghostty/config"

if [ ! -f "$GHOSTTY_CONFIG" ]; then
    echo "Error: Ghostty config file not found at $GHOSTTY_CONFIG"
    exit 1
fi

echo "Adding Vim-style navigation to Ghostty config..."

# Keybinds to add
KEYBINDS=(
    "keybind = ctrl+h=goto_split:left"
    "keybind = ctrl+j=goto_split:bottom"
    "keybind = ctrl+k=goto_split:top"
    "keybind = ctrl+l=goto_split:right"
)

for keybind in "${KEYBINDS[@]}"; do
    if grep -qF "$keybind" "$GHOSTTY_CONFIG"; then
        echo "Already present: $keybind"
    else
        echo "$keybind" >> "$GHOSTTY_CONFIG"
        echo "Added: $keybind"
    fi
done

echo "Configuration updated. Restart Ghostty to apply changes."
