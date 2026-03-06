#!/bin/bash

# Find the previous version tag first
git tag --sort=-version:refname | head -5

# Get commits between versions with PR numbers and authors
git log <previous-tag>..<current-tag> --pretty=format:"%h|%s|%an" --grep="#"
