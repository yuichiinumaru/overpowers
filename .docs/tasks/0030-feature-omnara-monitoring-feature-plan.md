# Feature Plan: Omnara PTY-based Flight Recorder

## 1. Overview
The "Omnara Flight Recorder" is a monitoring service designed to record every interaction (input and output) of a command-line session. By wrapping a target CLI command in a Pseudo-Terminal (PTY), the recorder can intercept data streams while maintaining full interactivity. This is crucial for security auditing, debugging complex agent interactions, and "flight recording" for post-incident analysis.

## 2. Goals & Success Criteria
- **Goal:** Create a robust, generalized PTY wrapper that logs all stdin/stdout activity.
- **Success Criteria:**
  - Can wrap any CLI command (e.g., `bash`, `python`, `claude`, `gemini`).
  - Records raw data streams with timestamps and direction markers (`IN`/`OUT`).
  - Maintains terminal features like colors, ANSI escape sequences, and window resizing.
  - Transparent to the user (the interactive experience is identical to running the command directly).

## 3. Vertical Slices & Milestones

### Slice 1: Generalized PTY Wrapper
- **Objective:** Create a Python script that takes a command as an argument and runs it in a PTY.
- **Deliverables:** `services/omnara-monitoring/omnara-flight-recorder.py`.

### Slice 2: Enhanced Logging & Metadata
- **Objective:** Implement structured logging with session metadata (PID, start time, command).
- **Deliverables:** Log files in `~/.overpowers/logs/` with unique naming.

### Slice 3: Integration Helper
- **Objective:** Provide a simple way to launch the recorder for standard tools.
- **Deliverables:** CLI aliases or a helper script `scripts/record-session.sh`.

## 4. Risks & Mitigations
- **Sensitive Data Exposure:** -> **Mitigation:** Logs are stored in a protected directory. Documentation should warn users that logs may contain secrets entered in the terminal.
- **Performance Overhead:** -> **Mitigation:** Use non-blocking I/O with `select` or `epoll` to minimize latency.
- **Terminal State Corruption:** -> **Mitigation:** Carefully restore terminal attributes (`termios`) on exit.

## 5. Exit Conditions
- [ ] Generalized flight recorder script is implemented and tested.
- [ ] Successfully recorded and verified sessions for multiple different CLI tools.
- [ ] Documentation updated in `.docs/services-guide.md`.
