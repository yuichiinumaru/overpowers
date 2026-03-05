# Scan Report: HeshamFS-materials-simulation-skills

## Repository Overview
- **Source**: HeshamFS
- **Purpose**: Agent skills for computational materials science and numerical simulation
- **Domain**: Scientific computing / Materials science

## Contents Inventory

### Core Numerical Skills
| Skill | Description |
|-------|-------------|
| numerical-stability | CFL analysis, von Neumann stability, stiffness detection |
| numerical-integration | Integrator selection, error norms, adaptive stepping |
| linear-solvers | Solver selection, preconditioner advice, convergence |
| time-stepping | Time step planning, checkpointing |
| differentiation-schemes | Scheme selection, stencil generation, truncation error |
| mesh-generation | Grid sizing, mesh quality metrics |

### Simulation Workflow Skills
| Skill | Description |
|-------|-------------|
| simulation-validator | Pre-flight, runtime, post-flight validation |
| parameter-optimization | DOE sampling, optimizer selection, sensitivity |
| simulation-orchestrator | Parameter sweeps, campaign management |
| post-processing | Field extraction, time series, statistics |

### Reference Materials
- Stencil catalogs
- Preconditioner patterns
- Convergence patterns
- CFL coupling guidelines

## Key Files
- skills/core-numerical/*/SKILL.md
- skills/simulation-workflow/*/SKILL.md
- examples/*/README.md
- tests/ (Python unittest suite)

## Quality Assessment
- **Structure**: Excellent - skills with scripts and references
- **Coverage**: Complete numerical simulation workflow
- **Domain Expertise**: High - specialized materials science
