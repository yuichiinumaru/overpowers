# Rule: Conda Environment 'mothership'

**Context**: This project uses a dedicated Conda environment to ensure dependency isolation and stability.

## Directive
*   **ALWAYS** use the conda environment named `mothership` for running any Python code, scripts, or tools within this workspace.
*   **Python Version**: 3.13 (Strict).
*   **Activation**: `conda activate mothership`
*   **Run Command**: `conda run -n mothership python <script.py>`

## Rationale
*   The `mothership` environment is specifically provisioned for this large-scale monorepo.
*   The default `base` or `12` environments may have conflicting dependencies.
*   We stick to Python 3.13 to future-proof the stack. Downgrade only if strictly necessary and authorized.

## Validation
*   Before running `pip install`, ensure you are in `(mothership)`.
*   Check `python --version` returns 3.13.x.
