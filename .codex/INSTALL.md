# Installing Overpowers for Codex

Quick setup to enable Overpowers skills in Codex.

## Installation

1. **Clone Overpowers repository**:
   ```bash
   mkdir -p ~/.codex/Overpowers
   cd ~/.codex/Overpowers
   git clone https://github.com/yuichiinumaru/Overpowers.git .
   ```

2. **Create personal skills directory**:
   ```bash
   mkdir -p ~/.codex/skills
   ```

3. **Update ~/.codex/AGENTS.md** to include this Overpowers section:
   ```markdown
   ## Overpowers System

   <EXTREMELY_IMPORTANT>
   You have Overpowers. Overpowers teach you new skills and capabilities. RIGHT NOW run: `~/.codex/Overpowers/.codex/Overpowers-codex bootstrap` and follow the instructions it returns.
   </EXTREMELY_IMPORTANT>
   ```

## Verification

Test the installation:
```bash
~/.codex/Overpowers/.codex/Overpowers-codex bootstrap
```

You should see skill listings and bootstrap instructions. The system is now ready for use.