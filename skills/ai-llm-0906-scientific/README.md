# Scientific Computing Skills

Open-source Agent Skills for computational materials science and numerical simulation workflows.

**Source**: Integrated from [HeshamFS/materials-simulation-skills](https://github.com/HeshamFS/materials-simulation-skills)

## Overview

These skills provide AI agents with expert-level guidance for numerical methods, stability analysis, and simulation campaign management. Each skill includes:
- `SKILL.md` with YAML frontmatter and step-by-step instructions
- `references/` for domain-specific knowledge loaded on demand
- CLI examples and decision guidance

## Skills Catalog

### Core Numerical Skills (6)

| Skill | Description |
|-------|-------------|
| `numerical-stability` | CFL analysis, von Neumann stability, stiffness detection, matrix conditioning |
| `numerical-integration` | Integrator selection, error norms, IMEX schemes, adaptive stepping |
| `linear-solvers` | Solver selection, preconditioner advice, convergence diagnostics, scaling |
| `time-stepping` | Time step planning, CFL coupling, output scheduling, checkpointing |
| `differentiation-schemes` | Scheme selection, stencil generation, truncation error, boundary handling |
| `mesh-generation` | Grid sizing, mesh types, quality metrics |

### Simulation Workflow Skills (4)

| Skill | Description |
|-------|-------------|
| `simulation-validator` | Pre-flight checks, runtime monitoring, post-flight validation |
| `parameter-optimization` | DOE sampling, optimizer selection, sensitivity analysis, surrogates |
| `simulation-orchestrator` | Parameter sweeps, campaign management, batch jobs, result aggregation |
| `post-processing` | Field extraction, time series analysis, statistics, derived quantities |

## Usage

Mention the skill by name in your request, or ask a task that matches its description:

```
Use numerical-stability to check if dt=1e-4 is stable for my 2D diffusion problem with D=1e-3.
```

```
Use simulation-orchestrator to set up a parameter sweep for kappa from 0.1 to 1.0.
```

## Requirements

- Python 3.10+
- NumPy (for stability analysis and matrix operations)
- Standard library only for orchestration and workflow skills

## Skill Dependencies

```
                parameter-optimization
                        |
                        v
simulation-validator --> simulation-orchestrator --> post-processing
        |                       |
        v                       v
numerical-stability      linear-solvers
        |                       |
        v                       v
time-stepping           mesh-generation
        |
        v
numerical-integration <--> differentiation-schemes
```

## Reference Files

Each skill includes reference materials in its `references/` subdirectory:

- **numerical-stability**: stability_criteria.md, common_pitfalls.md, scheme_catalog.md
- **numerical-integration**: method_catalog.md, splitting_catalog.md, imex_guidelines.md, error_control.md
- **linear-solvers**: solver_decision_tree.md, preconditioner_catalog.md, convergence_patterns.md
- **time-stepping**: cfl_coupling.md, ramping_strategies.md, output_checkpoint_guidelines.md
- **differentiation-schemes**: stencil_catalog.md, scheme_selection.md, boundary_handling.md
- **mesh-generation**: mesh_types.md, quality_metrics.md
- **parameter-optimization**: doe_methods.md, optimizer_selection.md, sensitivity_guidelines.md
- **simulation-orchestrator**: campaign_patterns.md, sweep_strategies.md
- **post-processing**: data_formats.md, derived_quantities_guide.md, comparison_metrics.md

## License

Apache 2.0 (inherited from source repository)

## Version

- **v1.0.0** (2025-01-19): Integrated into Overpowers skills collection
