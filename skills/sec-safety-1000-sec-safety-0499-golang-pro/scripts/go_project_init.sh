#!/bin/bash

# Initialize a modern Go project structure following standard layouts

if [ -z "$1" ]; then
  echo "Usage: go_project_init.sh <module_name>"
  echo "Example: go_project_init.sh github.com/user/project"
  exit 1
fi

MODULE_NAME=$1
PROJECT_NAME=$(basename "$MODULE_NAME")

echo "🚀 Initializing Go module: $MODULE_NAME"
go mod init "$MODULE_NAME"

echo "📂 Creating directory structure..."
mkdir -p cmd/"$PROJECT_NAME"
mkdir -p internal/api
mkdir -p internal/service
mkdir -p pkg/utils
mkdir -p api/proto
mkdir -p deployments/docker
mkdir -p configs
mkdir -p scripts

echo "📄 Creating main.go template..."
cat <<EOF > cmd/"$PROJECT_NAME"/main.go
package main

import (
	"context"
	"fmt"
	"log/slog"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	// Initialize structured logging (Go 1.21+)
	logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))
	slog.SetDefault(logger)

	ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
	defer stop()

	slog.Info("starting $PROJECT_NAME service")

	<-ctx.Done()
	slog.Info("shutting down gracefully")
}
EOF

echo "📄 Creating Makefile template..."
cat <<EOF > Makefile
.PHONY: build test lint run

build:
	go build -o bin/$PROJECT_NAME ./cmd/$PROJECT_NAME

test:
	go test -v ./...

lint:
	golangci-lint run

run:
	go run ./cmd/$PROJECT_NAME/main.go
EOF

echo "📄 Creating golangci-lint config..."
cat <<EOF > .golangci.yml
linters:
  enable:
    - gofmt
    - govet
    - errcheck
    - staticcheck
    - unused
    - gosimple
    - misspell
    - revive
EOF

echo "✅ Project initialized successfully."
