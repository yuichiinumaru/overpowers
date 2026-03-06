# Task: {Task Name Here}
<objective>
Phase: {e.g. 01-foundation}
Wave: {e.g. 1}

Define what this specific task accomplishes. 
Provide the context. What is the business value? What is the expected outcome?
</objective>

<files_modified>
- src/path/to/file1.ts
- src/path/to/file2.ts
*(CRITICAL: You may only modify files listed here to preserve parallel execution safety!)*
</files_modified>

<tasks>
  <task type="auto" tdd="true">
    <name>Task 1: [Action-oriented name]</name>
    <action>
      [Specific implementation instructions. Mention the library to use, the layout to adopt. Do not be vague.]
    </action>
    <verify>
      <automated>npm run test -- --grep "FeatureName"</automated>
    </verify>
    <done>[Acceptance criteria: E.g., The form successfully saves a User object to the DB.]</done>
  </task>

  <task type="checkpoint:human-verify" gate="blocking">
    <what-built>Authentication JWT Flow</what-built>
    <how-to-verify>
      Login onto `http://localhost:3000` with dummy credentials and verify the JWT exists in cookies.
    </how-to-verify>
  </task>
</tasks>

<context>
@templates/rules/agent-deviation-protocols.md
@templates/rules/checkpoint-protocol.md
</context>
