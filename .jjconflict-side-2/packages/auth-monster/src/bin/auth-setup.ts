#!/usr/bin/env node
import { startTui } from '../tui/index';

try {
  startTui();
} catch (error) {
  console.error('Failed to start Auth Monster Setup TUI:', error);
  process.exit(1);
}
