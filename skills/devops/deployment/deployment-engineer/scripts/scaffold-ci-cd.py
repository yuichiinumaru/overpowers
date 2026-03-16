#!/usr/bin/env python3
import os
import sys

def create_github_action():
    content = """name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Environment
        run: echo "Setting up build environment..."
      - name: Build
        run: make build

  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Unit Tests
        run: make test
      - name: Security Scan
        run: echo "Running security scans..."

  deploy-staging:
    if: github.ref == 'refs/heads/develop'
    needs: test
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - name: Deploy to Staging
        run: echo "Deploying to staging..."

  deploy-production:
    if: github.ref == 'refs/heads/main'
    needs: test
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Deploy to Production
        run: echo "Deploying to production..."
"""
    os.makedirs(".github/workflows", exist_ok=True)
    with open(".github/workflows/pipeline.yml", "w") as f:
        f.write(content)
    print("Created .github/workflows/pipeline.yml")

def create_gitlab_ci():
    content = """stages:
  - build
  - test
  - deploy

build_job:
  stage: build
  script:
    - echo "Building..."

test_job:
  stage: test
  script:
    - echo "Testing..."

deploy_staging:
  stage: deploy
  script:
    - echo "Deploying to staging..."
  environment: staging
  only:
    - develop

deploy_production:
  stage: deploy
  script:
    - echo "Deploying to production..."
  environment: production
  only:
    - main
  when: manual
"""
    with open(".gitlab-ci.yml", "w") as f:
        f.write(content)
    print("Created .gitlab-ci.yml")

def main():
    print("Scaffolding CI/CD templates...")
    create_github_action()
    create_gitlab_ci()

if __name__ == "__main__":
    main()
