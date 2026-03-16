---
name: flutter-schema
description: "Flutter GetX three-tier architecture specification. Core + Shared + Modules vertical layering, business modules GetX-ified. Suitable for new module creation, directory design, code review. Supports scaffold for building directory structures."
metadata:
  openclaw:
    category: "development"
    tags: ['development', 'flutter', 'mobile']
    version: "1.0.0"
---

# Flutter GetX Three-Tier Architecture Specification

## Architecture Overview

**Vertical Layering** (Unidirectional dependency from top to bottom, modules depend on core and shared):

```
shared (bottom) ← core ← modules (top)
```

**GetX Structure within a Module**:

```
Binding (injection) + View ← Logic → State
```

## Layer Quick Reference

| Layer | Responsibility |
|------|------|
| **core** | Configuration, routing, services, utilities, common UI components |
| **shared** | Business base classes, storage, networking, reusable capabilities |
| **modules** | Business feature implementation, split by feature, inter-module communication via routing |

## Module Directory Template

```
{module}/
├── {feature}/                 # Sub-feature (optional)
│   ├── xxx_binding.dart
│   ├── xxx_logic.dart
│   ├── xxx_state.dart
│   ├── xxx_view.dart
│   ├── model/
│   └── view/
├── binding/
├── model/
├── view/
├── db/                        # Local data (optional)
└── upload/                    # Upload (optional)
```

## Naming Conventions

- binding / logic / state / view: `xxx_binding.dart` → `XxxBinding`, etc.
- Logic inherits the BaseController base class within the project.
- View files end with `_view`, and class names end with `Page` or `View`.
- Avoid using `widget` as a file or class name suffix.

## Dependency Constraints

- Only allow upper layers to depend on lower layers.
- Peer modules do not import each other; communicate via routing (Get.toNamed).
- Logic should not hold BuildContext or directly manipulate the UI.

## Scaffold Capabilities

When users request to **create directories**, **set up the architecture**, or **create a new module**:

**Full**: Create core/config, constants, navigation, utils, services, widgets; shared/data, domain; modules/{name}

**Incremental**: Create `{module_name}/` under modules. The `validate.py` script can be used to generate page skeletons.

Module names use lowercase underscores (e.g., order_list, user_profile).

## Page Generation

- Normal pages: `python ~/flutter-schema/scripts/validate.py <name> [dir]`

See [schema.md](schema.md) for complete instructions.
