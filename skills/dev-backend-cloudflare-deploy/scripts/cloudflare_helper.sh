#!/bin/bash
# Helper for Cloudflare Deploy

COMMAND=$1
shift

case $COMMAND in
  "auth_check")
    npx wrangler whoami
    ;;
  "list_projects")
    npx wrangler pages project list
    ;;
  "deploy_worker")
    echo "Deploying Cloudflare Worker..."
    npx wrangler deploy "$@"
    ;;
  "deploy_pages")
    DIRECTORY=$1
    shift
    echo "Deploying Cloudflare Pages from $DIRECTORY..."
    npx wrangler pages deploy "$DIRECTORY" "$@"
    ;;
  "info")
    echo "Cloudflare Deployment Helper"
    echo "Products: Workers (edge), Pages (full-stack), D1 (SQL), R2 (Storage)"
    ;;
  *)
    echo "Usage: $0 {auth_check|list_projects|deploy_worker|deploy_pages <dir>|info}"
    exit 1
    ;;
esac
