#!/usr/bin/env bash
# Helper for camsnap operations

echo "--- camsnap Helper ---"
echo "Available actions:"
echo "1. Discover cameras"
echo "2. Check config"
echo "3. Take snapshot"
echo "4. Capture clip"

read -p "Select [1-4]: " choice

case $choice in
  1) cmd="camsnap discover --info" ;;
  2) cmd="camsnap doctor --probe" ;;
  3) read -p "Camera name: " cam; cmd="camsnap snap $cam --out snapshot.jpg" ;;
  4) read -p "Camera name: " cam; cmd="camsnap clip $cam --dur 5s --out clip.mp4" ;;
  *) echo "Invalid choice"; exit 1 ;;
esac

echo "Executing: $cmd"
eval $cmd
