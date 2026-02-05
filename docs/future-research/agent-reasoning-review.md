# Future Research: Agent Reasoning & Architecture Review

> Status: PLANNED
> Priority: HIGH (when resources available)
> Created: 2026-01-19

## Context

During the overpowers Repository Recycling project (Phase 2), we encountered advanced agent reasoning patterns that warrant deeper investigation:

### BDI (Belief-Desire-Intention) Ontology
- **Source**: guanyang-antigravity-skills repository
- **Current Status**: Adopted as optional skill in `overpowers/skills/reasoning/bdi-mental-states/`
- **Concept**: Moves agents from simple reactive loops to goal-oriented intention tracking
  - **Beliefs**: Agent's knowledge about the world
  - **Desires**: Goals the agent wants to achieve
  - **Intentions**: Committed plans the agent is executing

### Why This Needs Review

1. **Core vs Optional**: BDI could be a foundational paradigm for all agents, not just an optional skill
2. **Integration Points**: How does BDI interact with:
   - Our existing `systematic-debugging` skill?
   - The `brainstorming` skill?
   - Multi-agent coordination (`swarm-orchestration`)?
3. **Performance**: Does BDI overhead improve or degrade agent performance on simple tasks?
4. **Model Compatibility**: Which LLM models respond best to BDI-structured prompts?

## Related Assets Adopted

- `bdi-mental-states` - Core BDI ontology
- `context-compression` - Context management
- `context-degradation` - Context rot detection
- `planning-with-files` - Task plan templates

## Research Questions

1. Should BDI become the default reasoning paradigm for complex agents?
2. Can we create a "reasoning mode selector" that chooses BDI vs simpler patterns based on task complexity?
3. How do we measure agent "intentionality" quality?
4. What's the token overhead of BDI vs reactive patterns?

## Proposed Approach

When ready to tackle this:
1. Create benchmark suite for agent reasoning quality
2. A/B test BDI vs current patterns on diverse tasks
3. Document findings in `overpowers/docs/research/`
4. If BDI proves superior, propose migration path

## Dependencies

- Proper testing infrastructure
- Time to design comprehensive benchmarks
- Access to multiple model backends for comparison

---

*This document created during Phase 2 integration to capture strategic research needs.*
