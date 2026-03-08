# Scientific Debugging Protocol

> **Context:** When encountering an error or bug during execution or UAT, agents frequently fall into the trap of blindly reading random files or guessing fixes immediately. This rapidly burns through their context window, saturating memory with irrelevant code and causing severe hallucinations.

The Scientific Debugging Protocol isolates debugging into a controlled, empirical process, strictly managing state to maintain system hygiene.

## Core Directives

### 1. Hard Stop on Guessing
When a bug/error is identified, do not immediately formulate a hypothesis or start running random `grep`/`cat` commands on the codebase.

### 2. Isolate the Session
The orchestrator agent MUST pause the main executing loop to preserve its fast/clean context window.
- The master agent delegates the debugging to an entirely fresh, isolated instance (e.g., a subagent or a specifically dedicated fresh thought process).
- This isolation ensures that if the bug hunt requires scanning 15 files, the main agent's memory does not degrade.

### 3. The 5-Point Symptom Gathering
Before the isolated subagent begins the hunt, it must be explicitly fed the following 5 strict data points (gathered from logs or prompt interactions):
1. **Expected:** What the system should mathematically/logically do.
2. **Actual:** What the system is currently doing.
3. **Errors:** The exact raw error message or stack trace.
4. **Timeline:** When did this failure introduce itself? (e.g., "Broke after installing library X").
5. **Reproduction:** The exact minimal steps required to trigger the failure again.

### 4. Hypothesis & Experiment
The isolated debugging session operates strictly via:
- Formulate a hypothesis based *only* on the 5 symptoms.
- Read minimal code to verify the hypothesis.
- Implement a fix.
- Verify via the Nyquist Validation mechanism. 

### 5. Return to Main State
Once the bug is confirmed solved, the subagent shuts down. The main orchestrator resumes from its clean context state, simply acknowledging "Bug X resolved, continuing previous trajectory."
