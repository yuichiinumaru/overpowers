---
name: transition-design
description: "Analyze adjacent clip boundary frames, design optimal transition effects, and output transition design instructions. Use case: All clips have been processed and need clip-to-clip transitions designed. Avoid use case: Clip processing not complete, missing material Handle information."
metadata:
  openclaw:
    category: "design"
    tags: ['design', 'creative', 'graphics']
    version: "1.0.0"
---

## When to use

Use this skill when:
- All clips have been processed.
- Transitions between clips need to be designed.

Avoid using when:
- Clip processing is not complete.
- Handle information is missing.

## Core principles

- **Golden Rule**: Transitions cannot "eat" narrative content frames; rough cut boundaries are absolute boundaries.
- **Force a hard cut when handles are insufficient.**
- **Default to hard cuts** unless the narrative requires other transitions.

## Workflow

**Step 1: Frame-level analysis**
Obtain three key data points:
- Rough cut data: In/out points and available handles for Clip A and Clip B.
- Visual content: Motion vectors, lighting, and composition of boundary frames.
- Storyboard intent: Suggested transition type in the script.

**Step 2: Handle validation**
Consult [handle-logic-kb.md](references/handle-logic-kb.md) to verify transition feasibility:
- Calculate (Tail Handle + Head Handle).
- If < required transition frames → force Hard Cut.

**Step 3: Strategy selection**
Consult [transition-kb.md](references/transition-kb.md) to select the transition type based on narrative intent and technical feasibility:
- **Hard Cut**: Default choice, used for continuous action, dialogue, or when handles are insufficient.
- **Dissolve**: Used for passage of time or change of location.
- **Wipe/Other**: For special narrative needs.

**Step 4: Generate transition design instructions**
- **Decision Status**:
  - Validation Result: Following / Adapting / Overriding
  - Rationale: Explain any deviation from script intent.
- **Transition Strategy**:
  - Type: Final transition type.
  - Timing Mode: Center Cut / Start Cut / End Cut.
- **Frame-Level Specifications**:
  - Total Duration (Frames)
  - Handle Consumption: Number of extension frames from A's tail / Number of extension frames from B's head.
- **Effect Parameters**:
  - Interpolation: Linear / Ease-In / Ease-Out.
  - Visual Attributes: Direction, edge softness, etc.

**Step 5: Output transition design**
Assemble `transition_designs`.

## References

For detailed reference information, please consult:

- [transition-kb.md](references/transition-kb.md) - Defines transition types, usage scenarios, and effect parameters.
- [handle-logic-kb.md](references/handle-logic-kb.md) - Defines the concept of handles, calculation methods, and transition constraints.

## Tools
