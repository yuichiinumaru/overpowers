#!/usr/bin/env bash

# Helper script to scaffold a basic backend health check
# Usage: ./generate-healthcheck.sh [project_dir]

PROJECT_DIR=${1:-"."}
ROUTE_FILE="$PROJECT_DIR/health.ts"

cat << 'EOF' > "$ROUTE_FILE"
import { Router, Request, Response } from 'express';

const router = Router();

router.get('/health', (req: Request, res: Response) => {
  res.status(200).json({ status: 'OK', timestamp: new Date().toISOString() });
});

router.get('/ready', (req: Request, res: Response) => {
  // Add database connection check or other dependencies here
  const isReady = true;
  if (isReady) {
    res.status(200).json({ status: 'READY', timestamp: new Date().toISOString() });
  } else {
    res.status(503).json({ status: 'UNAVAILABLE', timestamp: new Date().toISOString() });
  }
});

export default router;
EOF

echo "Generated health check endpoints at $ROUTE_FILE"
