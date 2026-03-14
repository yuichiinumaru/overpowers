# Feature Plan: Graph-based Continuity (Mindmodel Context)

## 1. Overview
Transition the project's continuity tracking from flat Markdown files to a graph-based structure integrated with the `overpowers-graph-ext`. This allows for better relationship mapping between agent sessions, tasks, skills, and architectural decisions.

## 2. Goals & Success Criteria
- **Goal:** Enable graph-based visualization and traversal of project continuity.
- **Success Criteria:**
  - `continuity-*.md` files are represented as nodes in `overpowers-graph.json`.
  - Relationships between agent sessions and the components they modify are explicitly mapped.
  - The `overpowers-graph-ext` can resolve dependencies involving continuity records.

## 3. Vertical Slices & Milestones

### Slice 1: Metadata Standardization
- **Objective:** Add YAML frontmatter to all continuity files to make them parsable by the graph engine.
- **Deliverables:** Updated `continuity-*.md` files with `type: continuity` and `related_to` fields.

### Slice 2: Graph Builder Enhancement
- **Objective:** Update the `buildGraph` script to scan `.agents/` for continuity files.
- **Deliverables:** Modified `extensions/overpowers-graph-ext/src/build-graph.ts`.

### Slice 3: Validation & Visualization
- **Objective:** Rebuild the graph and verify the new nodes and edges.
- **Deliverables:** Updated `overpowers-graph.json` containing continuity nodes.

## 4. Risks & Mitigations
- **Context Bloat:** Adding all logs to the graph might make the JSON file too large. -> **Mitigation:** Only include high-level metadata in the graph node; keep the body in the Markdown file.
- **Parsing Errors:** Non-standard Markdown in continuity files might break the parser. -> **Mitigation:** Use robust regex or a formal Markdown parser for frontmatter extraction.

## 5. Exit Conditions
- [x] All `continuity-*.md` files have valid YAML frontmatter.
- [x] `build-graph.ts` successfully indexes continuity files.
- [x] `overpowers-graph.json` includes at least one continuity node with relationships.
