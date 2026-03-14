# Technical Design: Omnara PTY-based Flight Recorder

## 1. Architecture Overview
The Omnara Flight Recorder is a Python-based utility that uses the `pty` module to spawn a child process in a pseudo-terminal. It acts as a transparent proxy between the user's terminal and the child process, intercepting and logging all data flow.

## 2. API Signatures & Data Contracts

### Usage
```bash
python3 omnara-flight-recorder.py [--log-path PATH] <command> [args...]
```

### Log Format
Logs will be stored as binary or UTF-8 text with structured markers:
```
[TIMESTAMP] [IN/OUT] DATA
```
Wait, a better "Flight Recorder" format might be a JSONL file or a raw binary log that can be replayed with `scriptreplay`. However, for easy indexing by agents, a text-based format with metadata is preferred.

## 3. Database & Schema Changes
- None. Uses local filesystem for logs.
- Default log directory: `~/.overpowers/logs/omnara/`.

## 4. System Dependencies
- Python 3.x
- `pty` module (built-in)
- `termios`, `tty` (built-in)
- `fcntl` (built-in)

## 5. Security & Performance Considerations
- **Security:** Logs may contain sensitive information. The default log directory should have restricted permissions (0700).
- **Performance:** Non-blocking reads and minimal processing per byte are essential.
- **Resizing:** The script must catch `SIGWINCH` signals and propagate window size changes to the child PTY to ensure the layout remains correct.

## 6. Testing Strategy
- **Manual Verification:** Wrap `bash`, run interactive commands (vim, top), and verify logs.
- **Automated Tests:** Scripted interactions with a dummy CLI to verify that `IN` and `OUT` sequences are correctly captured.
