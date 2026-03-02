#!/bin/bash
# Build local MCP packages in packages/ directory
# Called by install.sh before MCP configuration
#
# Handles:
#   - Node.js packages: npm install && npm run build
#   - Python packages: uv sync (if uv available) or pip install -e .

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
PACKAGES_DIR="$SCRIPT_DIR/packages"

echo "🔨 Building local MCP packages..."
echo ""

# --- Node.js packages ---
NODE_PACKAGES=(
  "In-Memoria"
  "DesktopCommanderMCP"
  "vibe-check-mcp-server"
)

for pkg in "${NODE_PACKAGES[@]}"; do
  PKG_DIR="$PACKAGES_DIR/$pkg"
  if [ ! -d "$PKG_DIR" ]; then
    echo "⏭️  Skipping $pkg (not cloned)"
    continue
  fi
  if [ ! -f "$PKG_DIR/package.json" ]; then
    echo "⏭️  Skipping $pkg (no package.json)"
    continue
  fi

  echo "📦 Building $pkg (Node.js)..."
  cd "$PKG_DIR"

  if [ ! -d "node_modules" ]; then
    npm install --silent 2>&1 | tail -3
  fi

  if grep -q '"build"' package.json 2>/dev/null; then
    npm run build --silent 2>&1 | tail -3
  fi

  echo "   ✅ $pkg built"
  cd "$SCRIPT_DIR"
done

echo ""

# --- Python packages ---
PYTHON_PACKAGES=(
  "serena"
  "notebooklm-mcp-cli"
)

HAS_UV=false
if command -v uv &>/dev/null; then
  HAS_UV=true
fi

for pkg in "${PYTHON_PACKAGES[@]}"; do
  PKG_DIR="$PACKAGES_DIR/$pkg"
  if [ ! -d "$PKG_DIR" ]; then
    echo "⏭️  Skipping $pkg (not cloned)"
    continue
  fi
  if [ ! -f "$PKG_DIR/pyproject.toml" ]; then
    echo "⏭️  Skipping $pkg (no pyproject.toml)"
    continue
  fi

  echo "🐍 Setting up $pkg (Python)..."
  cd "$PKG_DIR"

  if $HAS_UV; then
    uv sync 2>&1 | tail -3
  else
    echo "   ⚠️  uv not found, trying pip..."
    pip install -e . 2>&1 | tail -3
  fi

  echo "   ✅ $pkg ready"
  cd "$SCRIPT_DIR"
done

echo ""
echo "✅ All local packages built."
