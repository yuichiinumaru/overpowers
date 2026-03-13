#!/usr/bin/env bash
# Shortcuts for openhue commands

echo "--- OpenHue Controller ---"
echo "1. Discover bridges"
echo "2. List lights"
echo "3. Turn all lights ON"
echo "4. Turn all lights OFF"
echo "5. List scenes"

read -p "Select [1-5]: " choice

case $choice in
  1) cmd="openhue discover" ;;
  2) cmd="openhue get light" ;;
  3) cmd="openhue set light all --on" ;;
  4) cmd="openhue set light all --off" ;;
  5) cmd="openhue get scene" ;;
  *) echo "Invalid choice"; exit 1 ;;
esac

echo "Executing: $cmd"
eval $cmd
