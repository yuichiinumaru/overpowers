# Installing overpowers for Codex

Quick setup to enable overpowers skills in Codex.

## Installation

1. **Clone overpowers repository**:
   ```bash
   mkdir -p ~/.codex/overpowers
   cd ~/.codex/overpowers
   git clone https://github.com/yuichiinumaru/overpowers.git .
   ```

2. **Create personal skills directory**:
   ```bash
   mkdir -p ~/.codex/skills
   ```

3. **Update ~/.codex/AGENTS.md** to include this overpowers section:
   ```markdown
   ## overpowers System

   <EXTREMELY_IMPORTANT>
   You have overpowers. overpowers teach you new skills and capabilities. RIGHT NOW run: `~/.codex/overpowers/.codex/overpowers-codex bootstrap` and follow the instructions it returns.
   </EXTREMELY_IMPORTANT>
   ```

## Verification

Test the installation:
```bash
~/.codex/overpowers/.codex/overpowers-codex bootstrap
```

You should see skill listings and bootstrap instructions. The system is now ready for use.