# Conversational UAT (User Acceptance Testing) Protocol

> **Context:** Traditional agent handoffs often consist of a monolithic "I have finished the task, please verify everything" message. This pushes an enormous cognitive load onto the user to test multiple moving parts at once. Conversational UAT enforces a step-by-step, interactive verification process focused on the user's perspective, making testing surgical, fast, and far less overwhelming.

## Core Directives

1. **Deconstruct the Deliverables:** Once an implementation phase is complete, break down the newly completed features into distinct, user-testable behaviors.
2. **One Test At A Time:** Do NOT ask the user to verify all behaviors at once. 
   - Present **Action 1** (e.g., "Can you try logging in with an invalid password?").
   - Wait for the user's result.
   - If the user responds with "Works" or "OK", immediately present **Action 2**.
3. **No Interrogation:** Use plain text, polite instructions. Do not generate massive checklists for the user. Your role is continuous guidance.
4. **Immediate Diagnosis on Failure:** If the user reports an issue or failure during a step, *stop the UAT progression*. 
   - Acknowledge the gap.
   - Transition immediately into the `scientific-debugging.md` protocol to resolve that specific constraint before continuing the UAT pipeline.
5. **Final UAT Sign-off:** Only when all individual behaviors have been conversationally tested and verified does the task officially graduate to "Completed".
