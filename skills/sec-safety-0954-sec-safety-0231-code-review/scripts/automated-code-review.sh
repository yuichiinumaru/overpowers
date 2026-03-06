#!/bin/bash
# Run automated code review tools
flake8 .
black --check .
eslint .
echo "Code review complete."
