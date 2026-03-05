#!/bin/bash
gh project list --owner @me --format json | jq -r '.projects[] | "[\(.number)] \(.title) (ID: \(.id))"'
