---
name: flutter-architecture
description: "Flutter Four-Layer Componentization + MVVM Project Architecture Specification. Applicable to Flutter project development, new module creation, directory structure design, code review, and architectural alignment. Supports direct creation/establishment of a complete MVVM + componentization directory structure within projects."
metadata:
  openclaw:
    category: "architecture"
    tags: ['architecture', 'governance', 'design']
    version: "1.0.0"
---

# Flutter Componentization + MVVM Architecture Specification

## Core Architecture

**Four-Layer Vertical Dependency** (Strictly Unidirectional):

```
app → business → component → foundation
```

**MVVM within Business Modules**:

```
View (page/view) → ViewModel → Repository → Model
```

## Layer Responsibilities Quick Reference

| Layer | Responsibility |
|------|------|
| **app** | Main engineering layer: global configuration, routing, startup items, module orchestration, no business logic |
| **business** | Business component layer: strong business implementation, split by module, inter-module communication via routing |
| **component** | Functional component layer: common company/team capabilities (payment, sharing, push, etc.), somewhat bound to business |
| **foundation** | Basic component layer: underlying capabilities unrelated to the company/project, strong portability |

## Business Module Directory Structure

```
{module}/
├── page/           # Pages: xxx_page.dart → XxxPage
├── view/           # Views: xxx_view.dart, xxx_navigation_bar.dart, etc.
├── view_model/
├── model/
└── repository/
```

## Page / View Naming (Mandatory)

- **page**: File `xxx_page.dart`, Class `XxxPage`
- **view**: Regular view `xxx_view.dart` → `XxxView`; Functional `xxx_navigation_bar.dart` → `XxxNavigationBar`
- **Strictly Forbidden**: Do not use the keyword `widget`

## Dependency Rules (Strictly Forbidden to Violate)

- Upper layers can depend on lower layers, lower layers cannot depend on upper layers
- Peer business modules do not import each other, only communicate via routing
- Unique dependency chain: `app → business → component → foundation`

## Directory Creation Capability (Scaffold)

When the user requests to **create directory structure**, **set up architecture**, **create new module**, or **scaffold**, create the following structure directly under the project's `lib/`:

**Full Creation** (New project or complete setup):
- `lib/app/config/`, `lib/app/pages/`
- `lib/business/{module}/` each module contains `page/`, `view/`, `view_model/`, `model/`, `repository/`
- `lib/component/` (can contain subdirectories like pay, share, push, update, etc.)
- `lib/foundation/` (network, image, router, db, utils, base, etc.)

**Incremental Creation** (Adding a new business module):
- Create `{module_name}/page/`, `view/`, `view_model/`, `model/`, `repository/` under `lib/business/`
- Module names use lowercase underscores (e.g., home, user_profile, scenario_learning)

When creating, follow the complete directory structure in [references/architecture.md](references/architecture.md) to ensure hierarchy and naming conform to the specifications.

## Complete Specification

Detailed directory structure, explanations for each layer, MVVM responsibilities, naming conventions, code examples, and Code Review standards can be found in [references/architecture.md](references/architecture.md).
