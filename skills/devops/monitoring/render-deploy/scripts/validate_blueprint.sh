#!/bin/bash
if [ ! -f "render.yaml" ]; then
    echo "❌ render.yaml not found in current directory."
    exit 1
fi

echo "🔍 Validating render.yaml..."
render blueprints validate
if [ $? -eq 0 ]; then
    echo "✅ render.yaml is valid."
else
    echo "❌ render.yaml validation failed."
    exit 1
fi
