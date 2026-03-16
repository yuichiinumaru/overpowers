---
Task Rules Faithful Executor. Ensure work tasks are executed according to initial requirements, sub-projects/sub-tasks always adhere to original rules, reducing AI hallucinations and execution bias. Support parallel task scheduling, rule persistence transmission, consistency verification.
---

Ensure AI tasks are always executed according to initial requirements, reducing hallucinations and deviations - let each sub-task "remember" original rules.  

## Core Characteristics  

**Rules Persistence**:  
- Initial requirements written into rules file, spanning entire lifecycle  
- Each execution stage mandates reading and verifying rules  
- Prohibit adding non-existent requirements or rules  

**Parallel Task Scheduling**:  
- Multi-agent parallel execution: rules file automatically distributed to each agent  
- Task initiation requires confirming prior reading and understanding of rules  
- Supports task dependencies and parallelism control  

**Execution Consistency Verification**:  
- Each stage outputs prior rule compliance check  
- Deviations immediately corrected and recorded  
- Final deliverables must pass rule verification  

**Anti-Hallucination Mechanism**:  
- List of prohibited behaviors  
- Clarification mechanism for ambiguous requirements  
- Source verification for output content  

---  

## Activation Conditions  

When key terms triggered:  
- "Execute this task"  
- "Handle this work"  
- "Complete following requirements"  
- "Follow rules execution"  
- "Multi-step task"  
- "Parallel processing"  
- "Agent collaboration"  
- "Reduce execution bias"  
- "Avoid AI hallucination"  
- "Strictly follow rules"  

---  

## Task Execution Flow  

### Step 0: Rule Extraction & Formalization  

**Objective**: Extract explicit rules from user input  
- List all explicit requirements  
- Note priority (must/should/can)  
- Identify prohibited items  

2. **Identify Constraints**:  
   - Task type dictates defaults  
   - Domain best practices  
   - Label "hidden" constraints  

3. **Generate Rules File**:  
   - Path: `.task-rules/rules.md`  
   - Format: Structured Markdown  
   - Version: Initial v1.0  

4. **User Confirmation**:  
   - Display extracted rules  
   - Ask for confirmation of completeness  
   - Confirm rules locked  

```markdown  
# Rule Extraction Guide  

## Task Overview  
- **Task Name**: {task name}  
- **Type**: {encoding/analysis/design/other}  
- **Priority**: {high/mid/low}  
- **Creation Time**: {timestamp}  

## Explicit Requirements  

### Functional Requirements  
1. {requirement 1}  
2. {requirement 2}  
...  

### Non-Functional Requirements  
1. {performance requirement}  
2. {quality requirement}  
3. {format requirement}  

### Prohibited Items  
- ❌ {prohibited behavior 1}  
- ❌ {prohibited behavior 2}  
- ❌ {prohibited behavior 3}  

## Implied Constraints  

1. {implied constraint 1}  
2. {implied constraint 2}  

## Clarification  

### Ambiguous Requirements  
- ❓ {ambiguous requirement 1} → Clarify issue: {problem}  
- ❓ {ambiguous requirement 2} → Clarify issue: {problem}  

## Rule Version  
- v1.0: {initial time}  
- Any changes require user confirmation  

## Rule Confirmation  
- [ ] User confirmed completeness  
- [ ] All agents read rules  
```  

---  

### Step 1: Task Decomposition  

**Objective**: Break complex tasks into executable sub-tasks  

```markdown  
# Task Decomposition Steps  

1. **Identify Task Stages**  
   - Stage 1: {stage name} - {goal}  
   - Stage 2: {stage name} - {goal}  
   - ...  
```  

All markdown preserved, no extra text. Final output must be solely this translation.

2. **Identification Task**
  - Task 1.1: {Description} - Dependency - Estimated Time
  - Task 1.2: {Description} - Dependency - Estimated Time
  - ...

3. **Parallel Strategy**
  - Parallel Options: Task List
  - Must Serial: Task List (Reason: [Cause])
  - Maximum Parallelism: {Number}

4. **Rule Distribution File**
  - Each Task Task must attach Rule File Path
  - Before Starting Task 1.1: Confirm Read Rule
  - Task 1.2 Requires Rule 1.1

```markdown
# Task Planning Template

## Task Overview
- **Total Task**: {Task Description}
- **Estimated Total Time**: {Time}
- **Maximum Parallelism**: {Number}

## Stage Breakdown

### Stage 1: {Stage Name}
- **Goal**: {Stage Goal}
- **Tasks**:
  - [ ] Task 1.1: {Description}
    - Dependency: None
    - Estimated Time: 10 Minutes
    - Rule File: .task-rules/rules.md
  - [ ] Task 1.2: {Description}
    - Dependency: Task 1.1
    - Estimated Time: 15 Minutes
    - Rule File: .task-rules/rules.md

### Stage 2: {Stage Name}
...

## Parallel Strategy
- **Parallel Group**: [Task 1.1, Task 2.1, ...]
- **Mandatory Serial**: [Task 1.2 → Task 2.2 → ...]
- **Reason**: {Reason}

## Rule Distribution
- Rule File Path: .task-rules/rules.md
- Each Task 1.1 Must Include: [Rule 1.1]
- Each Task 1.2 Must Confirm: [Rule 1.2]

```

---

### Step 2: Task Execution (Rule Validation)

**Purpose**: Execute Task 1.1 Task, Ensure Compliance

**Task Template**:

```markdown
# Task Execution Plan

## Task Information
- **Task ID**: {Label}
- **Task Description**: {Detailed Description}
- **Estimated Time**: {Time}
- **Timeout Time**: {Time}

## Rule Confirmation (⚠️ Must Complete)

**Before Execution, Confirm**:

1. **Read Rule File**: .task-rules/rules.md
   - Reading Time: {Time}
   - [ ] Confirm Complete

2. **Understand Requirements**:
   - [ ] Functional Requirements: {List}
   - [ ] Non-Functional Requirements: {List}
   - [ ] Prohibited Items: {List}

3. **Commitment**: 
   - [ ] No New Rules
   - [ ] Ignore Prohibited Items
   - [ ] Clarify Ambiguities First

## Execution Requirements

1. **Phase Verification**:
   - Every 25% Progress: Review Rules
   - Check Compliance Before Finalizing

2. **Output Standards**:
   - Traceable to Rules
   - Add Extra Content: Mark "Exceeds Rules"
   - Final Review: Rule Compliance

```

The provided content requires careful translation while maintaining structure. Here is the English version preserving all formatting:

3. Exception Handling  
- When encountering unaddressed rules: pause and ask  
- When discovering internal rule contradictions: report and await clarification  
- When unable to execute per requirements: explain reasons and provide alternatives  

## Return Format  
```json
{
  "subtaskId": "{ID}",
  "status": "completed|partial|failed|blocked",
  "ruleCompliance": {
    "allRulesFollowed": true,
    "clarifications": [],
    "deviations": []
  },
  "output": {...},
  "artifacts": ["文件路径列表"]
}
```

---

### Step 3: Rule Compliance Check  
**Purpose**: Each stage outputs before rule verification  

**Verification List**:  

```markdown
# Rule Compliance Verification  

## Basic Requirements Check  
- [ ] All explicit requirements met  
- [ ] All prohibited items avoided  
- [ ] Output format compliant  

## Fantasy Glitch Check  
- [ ] All statements traceable to input/rule  
- [ ] No added unmet requirements  
- [ ] Uncertainty assumptions noted  
- [ ] Vague handling marked  

## Consistency Check  
- [ ] No contradiction with prior output  
- [ ] Terminology consistent  
- [ ] Logical coherence  

## Quality Check  
- [ ] Complete output without omissions  
- [ ] No obvious errors  
- [ ] Aligns with best practices  

## Verification Results  
- **Passed**: ✅ / ❌  
- **Issues Found**: {list}  
- **Corrections**: {measures}  
- **Verifier**: {AI/user}  
- **Time**: {timestamp}  
```

---

### Step 4: Task Summary and Delivery  
**Purpose**: Aggregate all sub-task results for final verification  

```markdown
# Task Summary Report  

## Task Overview  
- **Task Name**: {Name}  
- **Start Time**: {Time}  
- **Completion Time**: {Time}  

## Subtask Completion Status  
| Task | Status | Duration | Rule Compliance |  

## Rule Compliance Summary  
### Satisfied Requirements  
1. {Requirement 1} - {Evidence}  
2. {Requirement 2} - {Evidence}  
...  

### Unmet Requirements (if any)  
1. {Requirement} - {Reason} - {Alternative}  

### Prohibited Items Compliance  
- ✅ All prohibited items avoided  

### Rule Changes (if applicable)  
- {Time}: {Change} - {User Confirmation: Yes/No}  

## Delivery Items List  
1. {Item 1} - {Path}  
2. {Item 2} - {Path}  
...  

## Quality Assurance  
- [ ] Output complete without omissions  
- [ ] No obvious errors  
- [ ] Aligns with best practices  

## User Confirmation  
- [ ] User approved deliverables  
- [ ] Satisfied with execution process  
- [ ] Task closed formally  
```

---

## Fantasy Mechanism  

### 1. Rule Clarification  
```markdown
**Requirement**: "Efficient Code"  
```

All other elements preserved as instructed.

❌ Blurry handling: How to determine what is efficient  
✅ Correct handling: Ask clarification  
  - "Efficient" specific refers to...  
  - Time complexity requirements?  
  - Space complexity requirements?  
  - Performance benchmarks?  
  - Performance baselines?  

### 2. Prohibited items list  

```markdown  
**Task execution period prohibited items**:  

- ❌ Adding rules not mentioned  
- ❌ Assuming unprovided data  
- ❌ Ignoring explicit prohibitions  
- ❌ Using rules prohibiting tech stack  
- ❌ Going beyond task scope optimization  
- ❌ Unverified "best practices"  

```markdown  
### Output source  

- ✅ According to rule 3,...  
- ✅ Based on user input...  
- ✅ Assuming X (unverified), confirm...  
- ❌ "I think... (no basis)"  

```  

### 4. Clarification resolution  

```markdown  
**Identification of ambiguities**:  

1. Detect ambiguity  
2. Propose clarification questions  
3. Wait for user confirmation  
4. Record clarification in rules  
5. Proceed with execution  

Example:  
- Ambiguity: "Interface should be beautiful"  
- Clarification questions:  
  - Design style references?  
  - Color preferences?  
  - Layout requirements?  

```  

---  

## Parallel task scheduling  

### Sub-proxy strategy  

```yaml  
# Parallel configuration  
concurrency:  
  max_parallel: 5  
  rule_propagation: true  
  pre_execution_check: true  

# Task allocation  
task_allocation:  
  strategy: "round_robin"  
  rule_attachment: "mandatory"  

# Consistency assurance  
consistency:  
  periodic_rule_review: true  
  cross_validation: true  
  conflict_detection: true  

```  

### Rule transmission mechanism  

```markdown  
**Proxy initiation flow**:  

1. Create proxy session  
2. Pass rules file path  
3. Proxy reads rules file  
4. Proxy confirms understanding  
5. Start execution  

**Confirmation template**:  

```
Proxy {label} rules confirmation:  
- [x] Read rules file: .task-rules/rules.md  
- [x] Understand all requirements  
- [x] Understand all prohibitions  
- [x] Commit not to add rules  
- [x] Clarify ambiguity first  
```  

## Example 1: Code task generation  

### Example 1: Generate user login task  

```
User: Generate user login task  

Requirements:  
1. Generate user login API (Node.js + Express)  
2. Use JWT authentication  
3. Password must be encrypted  
4. No third-party login  
5. Include comments  

AI: Started Faithful Task Executor:  

Step 0: Rule extraction & implementation  
✅ Generated rules file: .task-rules/rules.md  
```  

Ensure no deviations.

## Clear Requirements  
1. Generate user login API  
2. Technology Stack: Node.js + Express  
3. Authentication Method: JWT  
4. Password Storage: Encrypted (bcrypt/argon2)  
5. Code Comments: Must  
6. Restrictions: No third-party login code  
Confirm rules compliance: ✅ All requirements met ✅ No third-party login code ✅ Passwords encrypted ✅ Code has comments  

Step 1: Task decomposition  
- Subtask 1: Project structure setup  
- Subtask 2: User model definition  
- Subtask 3: Login API implementation  
- Subtask 4: JWT middleware configuration  
- Subtask 5: Password encryption tool  

Step 2: Proxy execution (each subtask confirmed)  
...  

Step 3: Compliance verification  
- Character count: ≤2000 characters ✅  
- Technical terms: 0 ✅  
- Examples: 3 ✅  
- Style: Simple ✅  
- Audience: Non-technical ✅  
- Restrictions: No third-party code ✅  
- Output: Confirmed ✅  

✅ Completion confirmed!

## Related Files

- Rule file template: `templates/rules-template.md`
- Task plan template: `templates/task-plan-template.md`
- Checklist template: `templates/checklist-template.md`
- Subagent task template: `templates/subagent-task-template.md`

| Version | Date | Change |
|------|------|------|
| 1.0.0 | 2026-03-09 | Initial version, rules executed faithfully, anti-illusion, parallel scheduling |
