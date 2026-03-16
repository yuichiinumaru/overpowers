import os
import re

task_file = '/home/sephiroth/Work/overpowers/.docs/tasks/0500-extraction-skills-batch-001.md'
with open(task_file, 'r') as f:
    task_content = f.read()

mapping = {
    'sync-changelog_SKILL.md': ('infra-ops-sync-changelog', 'Sync changelog automation and guidelines.', ['changelog', 'automation', 'infra']),
    'backend-patterns_SKILL.md': ('dev-backend-backend-patterns', 'Common backend development patterns and best practices.', ['backend', 'patterns', 'architecture']),
    'coding-standards_SKILL.md': ('dev-code-coding-standards', 'General coding standards and style guidelines.', ['standards', 'style', 'code']),
    'configure-ecc_SKILL.md': ('safety-sec-configure-ecc', 'Guidelines for configuring Elliptic Curve Cryptography (ECC).', ['security', 'ecc', 'crypto']),
    'continuous-learning-v2_SKILL.md': ('ai-llm-continuous-learning-v2', 'Advanced version of continuous learning for AI agents.', ['ai', 'learning', 'agents']),
    'continuous-learning_SKILL.md': ('ai-llm-continuous-learning', 'Continuous learning methodologies for AI.', ['ai', 'learning', 'methodology']),
    'cpp-testing_SKILL.md': ('dev-code-cpp-testing', 'Testing methodologies and frameworks for C++.', ['cpp', 'testing', 'c++']),
    'django-patterns_SKILL.md': ('dev-backend-django-patterns', 'Design patterns and best practices for Django framework.', ['django', 'python', 'backend']),
    'django-security_SKILL.md': ('safety-sec-django-security', 'Security best practices and configurations for Django.', ['django', 'security', 'python']),
    'eval-harness_SKILL.md': ('ai-llm-eval-harness', 'Evaluation harness for AI models and agents.', ['ai', 'eval', 'harness']),
    'golang-patterns_SKILL.md': ('dev-backend-golang-patterns', 'Design patterns and idiomatic practices for Golang.', ['golang', 'go', 'patterns']),
    'golang-testing_SKILL.md': ('dev-code-golang-testing', 'Testing strategies and frameworks for Golang.', ['golang', 'go', 'testing']),
    'iterative-retrieval_SKILL.md': ('ai-llm-iterative-retrieval', 'Iterative retrieval techniques for RAG and AI search.', ['ai', 'retrieval', 'rag']),
    'project-guidelines-example_SKILL.md': ('dev-code-project-guidelines-example', 'An example of project guidelines and structural rules.', ['guidelines', 'project', 'example']),
    'python-testing_SKILL.md': ('dev-code-python-testing', 'Testing methodologies and frameworks for Python.', ['python', 'testing', 'pytest']),
    'security-review_SKILL.md': ('safety-sec-security-review', 'Guidelines and checklists for conducting security reviews.', ['security', 'review', 'audit']),
    'security-scan_SKILL.md': ('safety-sec-security-scan', 'Procedures and tools for running security scans.', ['security', 'scan', 'tools']),
    'springboot-tdd_SKILL.md': ('dev-backend-springboot-tdd', 'Test-Driven Development (TDD) practices for Spring Boot.', ['java', 'springboot', 'tdd']),
    'strategic-compact_SKILL.md': ('infra-ops-strategic-compact', 'Strategic compact and high-level operational agreements.', ['strategy', 'ops', 'planning']),
    'tdd-workflow_SKILL.md': ('dev-code-tdd-workflow', 'Workflows and procedures for Test-Driven Development.', ['tdd', 'workflow', 'testing']),
    'verification-loop_SKILL.md': ('dev-code-verification-loop', 'Implementation of verification loops for code correctness.', ['verification', 'testing', 'quality']),
    'agent-harness-construction_SKILL.md': ('ai-llm-agent-harness-construction', 'Constructing harnesses for testing and running AI agents.', ['ai', 'agent', 'harness']),
    'agentic-engineering_SKILL.md': ('ai-llm-agentic-engineering', 'Principles and practices of agentic software engineering.', ['ai', 'engineering', 'agents']),
    'ai-first-engineering_SKILL.md': ('ai-llm-ai-first-engineering', 'Methodologies for AI-first engineering and development.', ['ai', 'engineering', 'methodology']),
    'article-writing_SKILL.md': ('content-media-article-writing', 'Guidelines and structures for writing articles.', ['content', 'writing', 'article'])
}

base_dir = '/home/sephiroth/Work/overpowers'
staging_dir = os.path.join(base_dir, '.archive/staging/skills')
skills_dir = os.path.join(base_dir, 'skills')

for filename, (new_name, default_desc, tags) in mapping.items():
    staged_path = os.path.join(staging_dir, filename)
    if os.path.exists(staged_path):
        with open(staged_path, 'r') as f:
            content = f.read()
        
        # Check if empty or garbled
        if len(content.strip()) < 10:
            status = '[Skipped]'
            os.remove(staged_path)
        else:
            status = '[x]'
            # Extract first sentence for description if possible
            desc = default_desc
            match = re.search(r'^(?!#)(.+?\.)\s', content, re.MULTILINE)
            if match and len(match.group(1)) > 15 and len(match.group(1)) < 150:
                desc = match.group(1).replace('\n', ' ').strip()
            
            frontmatter = f"""---
name: {new_name}
description: {desc}
version: 1.0.0
tags: {str(tags).replace("'", '"')}
---
"""
            # Add frontmatter to content
            new_content = frontmatter + "\n" + content
            
            # Save to new location
            dest_dir = os.path.join(skills_dir, new_name)
            os.makedirs(dest_dir, exist_ok=True)
            dest_path = os.path.join(dest_dir, 'SKILL.md')
            with open(dest_path, 'w') as f:
                f.write(new_content)
                
            # Clean up original
            os.remove(staged_path)
            
        # Update task file content
        pattern = r'\[ \] `\.archive/staging/skills/' + re.escape(filename) + r'`'
        replacement = f'{status} `.archive/staging/skills/{filename}`'
        task_content = re.sub(pattern, replacement, task_content)

with open(task_file, 'w') as f:
    f.write(task_content)

print("Batch processing complete.")
