#!/bin/bash
DB_PATH="${1:-.agentdb/vectors.db}"
npx agentdb@latest stats "$DB_PATH"
