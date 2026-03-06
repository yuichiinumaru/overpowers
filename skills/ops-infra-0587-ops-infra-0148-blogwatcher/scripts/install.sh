#!/bin/bash
# Install blogwatcher CLI

if ! command -v go &> /dev/null; then
    echo "❌ go could not be found. Please install Go to install blogwatcher."
else
    echo "Installing blogwatcher..."
    if go install github.com/Hyaxia/blogwatcher/cmd/blogwatcher@latest; then
        echo "✅ blogwatcher installed successfully."
        echo "Make sure \$(go env GOPATH)/bin is in your PATH."
    else
        echo "❌ Failed to install blogwatcher."
    fi
fi
