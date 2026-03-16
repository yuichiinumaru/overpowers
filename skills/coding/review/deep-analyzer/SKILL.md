---
name: system-project-deep-analyzer
description: Deep analysis of project boundaries, core concepts, module architecture, key algorithms, technical selection, and error troubleshooting.
tags: [analysis, system, architecture, auditing]
version: 1.0.0
---

# Project Deep Analyzer

This skill provides a structured methodology for deep analysis and understanding of software projects of any size. It guides the user or AI through six core dimensions for a comprehensive project audit.

## Core Analysis Process

### 1. System Boundary Analysis
Identify the project's external interactions and runtime environment.
- **Project Goal**: What core problem does it solve?
- **Runtime Environment**: Which platforms are supported (macOS/Linux/Windows)?
- **External Interfaces**: What CLIs, APIs, or SDKs are provided?
- **Tech Stack**: Core languages, frameworks, databases, and external services.
- **Installation and Usage**: Prerequisites, dependencies, and startup steps.

### 2. Core Concept System
Extract key domain models and terminology from the project.
- **Terminology List**: List all critical terms in the project.
- **Definition and Motivation**: Definition of each concept and the reason for its existence.
- **Relationship Map**: Hierarchical, dependency, or compositional relationships.
- **Core vs. Auxiliary**: Distinguish core business logic from peripheral support tools.
- **Code Mapping**: Specific locations of concepts within the code structure.

### 3. Module Architecture Analysis
Deconstruct the project's physical and logical organization.
- **Directory Structure**: Physical division of modules.
- **Responsibility Division**: Core responsibility and boundary of each module.
- **Dependency Relationships**: Coupling between modules and invocation chains.
- **Code Metrics**: Line counts, file counts, and what they reveal about the development focus.
- **Decoupling Suggestions**: Identify independently detachable modules and strong coupling points.

### 4. Core Algorithm Analysis
Deeply understand the project's logical heart.
- **Algorithm List**: Key algorithms used in the project and their roles.
- **Performance Evaluation**: Time/space complexity and limitations.
- **Data Structure**: Input/output of algorithms and core data flow.
- **Source Code Location**: Specific implementation files and functions for algorithms.

### 5. Technical Selection Assessment
Reflect on the rationality of design decisions.
- **In-house vs. Third-party**: Which parts are custom-built? Are there better alternatives?
- **Necessity Review**: Does the custom part show signs of over-engineering?
- **Refactoring Suggestions**: Which components should be retained or replaced if redesigned?
- **Knowledge Accumulation**: Technical highlights or algorithms worth absorbing from the project.

### 6. Error Troubleshooting and Analysis
Structured location and fixing of issues.
- **Log Positioning**: Locate specific files and functions through error logs.
- **Chain Traceability**: Analyze the complete call stack.
- **Root Cause**: Explain the underlying reason for the error.
- **Fix Plan**: Provide specific fix code or configuration suggestions.

## Use Cases

- **Joining a New Project**: Quickly establish a global perspective on an unfamiliar codebase.
- **Architecture Audit**: Identify design flaws or optimization opportunities in existing projects.
- **Technical Research**: Analyze implementation principles of open-source projects to assess integration suitability.
- **Complex Bug Location**: Solve difficult issues through structured call chain analysis.
